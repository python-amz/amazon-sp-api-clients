import hashlib
import hmac
import json
import os
import urllib
from datetime import datetime
from functools import reduce, cached_property
from time import sleep
from typing import Union
from urllib.parse import urlparse

import boto3
import requests
from cachetools import TTLCache
from requests import Response, Request
from requests.api import request
from requests.auth import AuthBase

from amazon_sp_api_clients.utils.exceptions import SellingApiError


class AwsSignV4(AuthBase):
    def __init__(self, *, service, aws_key, aws_secret, region, aws_session_token=None):
        self.service = service
        self.aws_key, self.aws_secret = aws_key, aws_secret
        self.aws_session_token = aws_session_token
        self.region = region

    def __call__(self, request: Request):
        # load data from instance
        region, service, aws_key, aws_secret, session = \
            self.region, self.service, self.aws_key, self.aws_secret, self.aws_session_token

        # Create a date for headers and the credential string
        now = datetime.utcnow()
        time_str = now.strftime('%Y%m%dT%H%M%SZ')
        date_str = now.strftime('%Y%m%d')

        # Parse request to get URL parts
        parsed_url = urlparse(request.url)
        host, uri, query = parsed_url.hostname, urllib.parse.quote(parsed_url.path), parsed_url.query

        headers = (('host', host), ('x-amz-date', time_str))
        headers = headers if session is None else (*headers, ('x-amz-security-token', session))
        header_str = ''.join((f'{k}:{v}\n' for k, v in headers))
        header_names = ';'.join((k for k, v in headers))

        body = request.body  # TODO Check if can change to request.data
        if body:
            if isinstance(body, str):
                payload = body.encode('utf-8')
            elif isinstance(body, bytes):
                payload = body
            else:
                raise TypeError('r.body type should be str or bytes')
        else:
            payload = b''
        payload_hash = hashlib.sha256(payload).hexdigest()
        request_str = f'{request.method}\n{uri}\n{query}\n{header_str}\n{header_names}\n{payload_hash}'
        action = 'aws4_request'
        scope_path = (date_str, region, service, action)
        scope_str = '/'.join(scope_path)
        request_hash = hashlib.sha256(request_str.encode('utf-8')).hexdigest()
        before_sign = f'AWS4-HMAC-SHA256\n{time_str}\n{scope_str}\n{request_hash}'
        secret_str = f'AWS4{self.aws_secret}'
        messages = tuple(message.encode('utf-8') for message in (secret_str, *scope_path, before_sign))
        # TODO check if the HMAC can be reused
        signature = reduce(lambda v1, v2: hmac.new(v1, v2, hashlib.sha256).digest(), messages)
        auth = f"AWS4-HMAC-SHA256 Credential={aws_key}/{scope_str}, SignedHeaders={header_names}, Signature={signature}"
        request.headers.update({'host': host, 'x-amz-date': time_str,
                                'Authorization': auth, 'x-amz-security-token': session})
        return request


class BaseSyncClient:
    # By assume role, a token will be received.
    _role_cache = TTLCache(maxsize=10, ttl=3000)

    # Refresh token can be used to get access token, access token will last for 1 hour
    _access_token_cache = TTLCache(maxsize=1000, ttl=3000)

    # Sometimes the response are required, however, current architecture is not able to return the response.
    # So, the last response is recorded here. Usually, the client will not request multiple requests. So, it will not
    # cause the data conflict.
    last_response: Response = None

    def __init__(self, *, refresh_token: str = None,
                 role_arn: str = None, endpoint: str = None, region: str = None, marketplace: str = None,
                 aws_key: str = None, aws_secret: str = None, lwa_key: str = None, lwa_secret: str = None,
                 ignore_quota_exceed: bool = True,
                 ):
        """Create a client.

        Args:
            region: from SP API documentation, like 'us-east-1'
            endpoint: from SP API documentation, like "https://sellingpartnerapi-eu.amazon.com"
            marketplace: from SP API documentation, like "A1F83G8C2ARO7P"
            aws_key: from AWS IAM, like 'xxxxxxxxxxxxxxxxxxxx'
            aws_secret: from AWS IAM, like "xxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            role_arn: from seller central or vendor central, like "arn:aws:iam::xxxxxxxxxxxx:role/sp_api_role"
            lwa_key: from seller central or vendor central
            lwa_secret: from seller central or vendor central
            refresh_token: from authorization workflow, like
                           "Atzr|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                           "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                           "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                           "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            ignore_quota_exceed: if True, when caught quota exceeded exception, wait 0.1s and resend
        """
        self._aws_key = os.environ.get('SP_API_AWS_KEY') if aws_key is None else aws_key
        self._aws_secret = os.environ.get('SP_API_AWS_SECRET') if aws_secret is None else aws_secret
        self._role_arn = os.environ.get('SP_API_ROLE_ARN') if role_arn is None else role_arn
        self._endpoint = os.environ.get('SP_API_ENDPOINT') if endpoint is None else endpoint
        self._region = os.environ.get('SP_API_REGION') if region is None else region
        self._marketplace = os.environ.get('SP_API_MARKETPLACE') if marketplace is None else marketplace
        self._refresh_token = os.environ.get('SP_API_REFRESH_TOKEN') if refresh_token is None else refresh_token
        self._lwa_key = os.environ.get('SP_API_LWA_KEY') if lwa_key is None else lwa_key
        self._lwa_secret = os.environ.get('SP_API_LWA_SECRET') if lwa_secret is None else lwa_secret
        self._client = boto3.client('sts', aws_access_key_id=self._aws_key, aws_secret_access_key=self._aws_secret)
        self._ignore_quota_exceeded = ignore_quota_exceed
        if any(i is None for i in (aws_key, aws_secret, self._role_arn, self._endpoint, self._region,
                                   self._marketplace, self._refresh_token, self._lwa_key, self._lwa_secret)):
            raise ValueError('Please set all parameters of the client')

    @cached_property
    def _parameters(self):
        return dict(
            role_arn=self._role_arn, endpoint=self._endpoint, region=self._region, marketplace=self._marketplace,
            refresh_token=self._refresh_token,
            aws_key=self._aws_key, aws_secret=self._aws_secret, lwa_key=self._lwa_key, lwa_secret=self._lwa_secret,
        )

    def __get_access_token(self, refresh_token: str):
        if refresh_token not in self._access_token_cache:
            data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token,
                    'client_id': self._lwa_key, 'client_secret': self._lwa_secret}
            headers = {'User-Agent': 'amazon-sp-api-clients',
                       'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'}
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
        data_bytes: bytes
        if data is None:
            data_bytes = b''
        elif isinstance(data, dict):
            data_bytes = json.dumps(data).encode()
        elif isinstance(data, bytes):
            data_bytes = data
        else:
            raise TypeError('data should be a dict or bytes')

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
        auth = AwsSignV4(service='execute-api',
                         aws_key=role.get('AccessKeyId'),
                         aws_secret=role.get('SecretAccessKey'),
                         region=self._region,
                         aws_session_token=role.get('SessionToken'))
        url = self._endpoint + path

        # process quota exceeded exception
        while True:
            response = request(method=method, url=url, data=data_bytes, headers=parsed_headers, auth=auth,
                               params=params)

            self.last_response = response
            if not check_exception:
                break

            # If found error, and the error is QuotaExceed, just resend the request
            e = self._get_response_json(response).get('errors', None)
            if e:
                if self._ignore_quota_exceeded and len(e) == 1 and 'code' in e[0] and e[0]['code'] in \
                        ('QuotaExceeded',):
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
