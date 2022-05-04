import hashlib
import hmac
import json
import os
import urllib
from collections import OrderedDict
from datetime import datetime
from time import sleep
from typing import Union
from urllib.parse import urlparse

import boto3
import requests
from cachetools import TTLCache
from requests import Response
from requests.api import request
from requests.auth import AuthBase

from amazon_sp_api_clients.utils.exceptions import SellingApiError

TRUE_VALUES = (True, 'true', 't', 'yes', 'y')
FALSE_VALUES = (False, 'false', 'f', 'no', 'n')


def convert_bool(value):
    if isinstance(value, str):
        value = value.lower()
    if value in TRUE_VALUES:
        return True
    elif value in FALSE_VALUES:
        return False
    else:
        raise ValueError('Wrong boolean value')


class AWSSigV4(AuthBase):

    @staticmethod
    def sign_message(key: bytes, message: str):
        return hmac.new(key, message.encode('utf-8'), hashlib.sha256).digest()

    def __init__(self, service, **kwargs):
        # Set Service
        self.service = service

        # First, get credentials passed explicitly
        self.aws_access_key_id = kwargs.get('aws_access_key_id')
        self.aws_secret_access_key = kwargs.get('aws_secret_access_key')
        self.aws_session_token = kwargs.get('aws_session_token')
        # Next, try environment variables or use boto3

        # Last, fail if still not found
        if self.aws_access_key_id is None or self.aws_secret_access_key is None:
            raise KeyError("AWS Access Key ID and Secret Access Key are required")

        # Get Region passed explicitly
        self.region = kwargs.get('region')
        # Next, try environment variables or use boto3
        if self.region is None:
            self.region = os.environ.get('SP_AWS_REGION', 'us-east-1')

    def __call__(self, r):
        # Create a date for headers and the credential string
        t = datetime.utcnow()
        self.amazon_date = t.strftime('%Y%m%dT%H%M%SZ')
        self.datestamp = t.strftime('%Y%m%d')

        # Parse request to get URL parts
        p = urlparse(r.url)

        host = p.hostname
        uri = urllib.parse.quote(p.path)

        if len(p.query) > 0:
            qs = dict(map(lambda i: i.split('='), p.query.split('&')))
        else:
            qs = dict()

        canonical_querystring = "&".join(map(lambda x: '='.join(x), sorted(qs.items())))
        headers_to_sign = {'host': host, 'x-amz-date': self.amazon_date}
        if self.aws_session_token is not None:
            headers_to_sign['x-amz-security-token'] = self.aws_session_token

        ordered_headers = OrderedDict(sorted(headers_to_sign.items(), key=lambda t: t[0]))
        canonical_headers = ''.join(map(lambda h: ":".join(h) + '\n', ordered_headers.items()))
        signed_headers = ';'.join(ordered_headers.keys())

        if r.method == 'GET':
            payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()
        else:
            if r.body:
                if isinstance(r.body, str):
                    payload_hash = hashlib.sha256(r.body.encode('utf-8')).hexdigest()
                elif isinstance(r.body, bytes):
                    payload_hash = hashlib.sha256(r.body).hexdigest()
                else:
                    raise TypeError('r.body type should be str or bytes')

            else:
                payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()

        canonical_request = '\n'.join([r.method, uri, canonical_querystring,
                                       canonical_headers, signed_headers, payload_hash])

        credential_scope = '/'.join([self.datestamp, self.region, self.service, 'aws4_request'])
        string_to_sign = '\n'.join(['AWS4-HMAC-SHA256', self.amazon_date,
                                    credential_scope, hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()])

        kDate = self.sign_message(('AWS4' + self.aws_secret_access_key).encode('utf-8'), self.datestamp)
        kRegion = self.sign_message(kDate, self.region)
        kService = self.sign_message(kRegion, self.service)
        kSigning = self.sign_message(kService, 'aws4_request')
        signature = hmac.new(kSigning, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = "AWS4-HMAC-SHA256 Credential={}/{}, SignedHeaders={}, Signature={}".format(
            self.aws_access_key_id, credential_scope, signed_headers, signature)
        r.headers.update({
            'host': host,
            'x-amz-date': self.amazon_date,
            'Authorization': authorization_header,
            'x-amz-security-token': self.aws_session_token
        })
        return r


class BaseSyncClient:
    _role_cache = TTLCache(maxsize=10, ttl=3000)
    _access_token_cache = TTLCache(maxsize=1000, ttl=3000)

    # Sometime the response are required, however, current architecture is not able to return the response.
    # So, the last response is recorded here. Usually, the client will not request multiple requests. So, it will not
    # cause the data conflict.
    last_response: Response = None

    def __init__(self, *,
                 role_arn: str = None,
                 endpoint: str = None,
                 region: str = None,
                 marketplace_id: str = None,
                 refresh_token: str = None,
                 aws_access_key: str = None,
                 aws_secret_key: str = None,
                 lwa_client_key: str = None,
                 lwa_client_secret: str = None,
                 ):
        """Create a base client.

        Args:
            role_arn: "arn:aws:iam::xxxxxxxxxxxx:role/sp_api_role"
            endpoint: "https://sellingpartnerapi-eu.amazon.com"
            marketplace_id: "A1F83G8C2ARO7P"
            refresh_token:  "Atzr|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            aws_access_key: 'xxxxxxxxxxxxxxxxxxxx'
            aws_secret_key: "xxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            use_cache: if True, check if cached and return cached response, or get new response and save
        """
        if role_arn is None:
            role_arn = os.environ.get('SP_API_ROLE_ARN')
        if endpoint is None:
            endpoint = os.environ.get('SP_API_ENDPOINT')
        if region is None:
            region = os.environ.get('SP_API_REGION')
        if marketplace_id is None:
            marketplace_id = os.environ.get('SP_API_MARKETPLACE_ID')
        if refresh_token is None:
            refresh_token = os.environ.get('SP_API_REFRESH_TOKEN')
        if aws_access_key is None:
            aws_access_key = os.environ.get('SP_API_AWS_ACCESS_KEY')
        if aws_secret_key is None:
            aws_secret_key = os.environ.get('SP_API_AWS_SECRET_KEY')
        if lwa_client_key is None:
            lwa_client_key = os.environ.get('SP_API_LWA_CLIENT_KEY')
        if lwa_client_secret is None:
            lwa_client_secret = os.environ.get('SP_API_LWA_CLIENT_SECRET')
        self._client = boto3.client('sts', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        self._role_arn = role_arn
        self._endpoint = endpoint
        self._region = region
        self._marketplace_id = marketplace_id
        self._refresh_token = refresh_token
        self._aws_access_key = aws_access_key
        self._aws_secret_key = aws_secret_key
        self._client_id = lwa_client_key
        self._client_secret = lwa_client_secret

    def __get_access_token(self, refresh_token):
        if refresh_token not in self._access_token_cache:
            data = {
                'grant_type': 'refresh_token',
                'client_id': self._client_id,
                'client_secret': self._client_secret,
                'refresh_token': refresh_token,
            }
            headers = {
                'User-Agent': 'python-sp-api',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            }
            response = requests.post('https://api.amazon.com/auth/o2/token', data=data, headers=headers)
            access_token = response.json()['access_token']
            self._access_token_cache[refresh_token] = access_token
        return self._access_token_cache[refresh_token]

    @staticmethod
    def _get_response_json(response: requests.Response):
        try:
            return response.json()
        except json.JSONDecodeError:
            try:
                import demjson
            except ImportError:
                raise SellingApiError('Could not parse response, please try to install demjson')
            return demjson.decode(response.text)

    def request(self, path: str, *, data: Union[dict, bytes] = None, params: dict = None, headers=None,
                method='GET', check_exception=True) -> Response:

        # process params
        parsed_params = {}
        params is None or parsed_params.update(params)

        # process data
        parsed_data: bytes
        if data is None:
            parsed_data = b''
        elif isinstance(data, dict):
            parsed_data = json.dumps(data).encode()
        elif isinstance(data, bytes):
            parsed_data = data
        else:
            raise TypeError('data should be a dict or bytes')

        # process headers
        parsed_headers = {
            'host': self._endpoint[8:],
            'user-agent': 'python-sp-api',
            'x-amz-access-token': self.__get_access_token(self._refresh_token),
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
            'content-type': 'application/json'
        }
        headers is None or parsed_headers.update(headers)

        # process auth
        if 'role' not in self._role_cache:
            role = self._client.assume_role(RoleArn=self._role_arn, RoleSessionName='guid').get('Credentials')
            self._role_cache['role'] = role
        role = self._role_cache['role']
        auth = AWSSigV4('execute-api',
                        aws_access_key_id=role.get('AccessKeyId'),
                        aws_secret_access_key=role.get('SecretAccessKey'),
                        region=self._region,
                        aws_session_token=role.get('SessionToken'))
        url = self._endpoint + path

        # process quota exceeded exception
        while True:
            response = request(method=method, url=url, data=parsed_data, headers=parsed_headers,
                               auth=auth, params=params)

            self.last_response = response
            if not check_exception:
                break

            # If found error, and the error is QuotaExceed, just resend the request
            e = self._get_response_json(response).get('errors', None)
            if e:
                if len(e) == 1 and 'code' in e[0] and e[0]['code'] in ('QuotaExceeded',):
                    sleep(0.1)
                    continue
                else:
                    raise SellingApiError(e)
            else:
                break

        return response


class BaseDictObject:
    def __init__(self, data):
        self.data: dict = data

    def _get_value(self, klass: type, name: str):
        value = self.data.get(name, None)
        if value is None and klass is dict:
            return None
        return klass(value)


class BaseClients:
    def __init__(self, *,
                 role_arn: str = None,
                 endpoint: str = None,
                 region: str = None,
                 marketplace_id: str = None,
                 refresh_token: str = None,
                 aws_access_key: str = None,
                 aws_secret_key: str = None,
                 lwa_client_key: str = None,
                 lwa_client_secret: str = None,
                 ):
        """Create a base client.

        Args:
            role_arn: "arn:aws:iam::xxxxxxxxxxxx:role/sp_api_role"
            endpoint: "https://sellingpartnerapi-eu.amazon.com"
            marketplace_id: "A1F83G8C2ARO7P"
            refresh_token:  "Atzr|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            aws_access_key: 'xxxxxxxxxxxxxxxxxxxx'
            aws_secret_key: "xxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            use_cache: if True, check if cached and return cached response, or get new response and save
        """
        if role_arn is None:
            role_arn = os.environ.get('SP_API_ROLE_ARN')
        if endpoint is None:
            endpoint = os.environ.get('SP_API_ENDPOINT')
        if region is None:
            region = os.environ.get('SP_API_REGION')
        if marketplace_id is None:
            marketplace_id = os.environ.get('SP_API_MARKETPLACE_ID')
        if refresh_token is None:
            refresh_token = os.environ.get('SP_API_REFRESH_TOKEN')
        if aws_access_key is None:
            aws_access_key = os.environ.get('SP_API_AWS_ACCESS_KEY')
        if aws_secret_key is None:
            aws_secret_key = os.environ.get('SP_API_AWS_SECRET_KEY')
        if lwa_client_key is None:
            lwa_client_key = os.environ.get('SP_API_LWA_CLIENT_KEY')
        if lwa_client_secret is None:
            lwa_client_secret = os.environ.get('SP_API_LWA_CLIENT_SECRET')
        self._role_arn = role_arn
        self._endpoint = endpoint
        self._region = region
        self._marketplace_id = marketplace_id
        self._refresh_token = refresh_token
        self._aws_access_key = aws_access_key
        self._aws_secret_key = aws_secret_key
        self._client_id = lwa_client_key
        self._client_secret = lwa_client_secret
        self._parameters = dict(
            role_arn=role_arn,
            endpoint=endpoint,
            region=region,
            marketplace_id=marketplace_id,
            refresh_token=refresh_token,
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            lwa_client_key=lwa_client_key,
            lwa_client_secret=lwa_client_secret,
        )
