from amazon_sp_api_clients_2.utils.exceptions import SellingApiError

try:
    from functools import cached_property
except ImportError:
    try:
        from cached_property import cached_property
    except ImportError:
        print('Please install cached_property for python < 3.8')
        raise

import hashlib
import hmac
import json
import os
import urllib
from datetime import datetime
from functools import reduce
from typing import Union
from urllib.parse import urlparse

import boto3
import requests
from cachetools import TTLCache
from requests import Response, Request
from requests.api import request
from requests.auth import AuthBase


class AwsSignV4(AuthBase):
    def __init__(self, *, service, aws_key, aws_secret, region, aws_session_token):
        self.service = service
        self.aws_key, self.aws_secret = aws_key, aws_secret
        self.aws_session_token = aws_session_token
        self.region = region

    def __call__(self, req: Request):
        # load data from instance
        region, service, aws_key, aws_secret, session = \
            self.region, self.service, self.aws_key, self.aws_secret, self.aws_session_token

        # Create a date for headers and the credential string
        now = datetime.utcnow()
        time_str = now.strftime('%Y%m%dT%H%M%SZ')
        date_str = now.strftime('%Y%m%d')

        # Parse request to get URL parts
        parsed_url = urlparse(req.url)
        host, uri, query = parsed_url.hostname, urllib.parse.quote(parsed_url.path), parsed_url.query
        # noinspection PyTypeChecker
        query = '&'.join(sorted(query.split('&')))  # the param should be sorted before sign
        headers = {'host': host, 'x-amz-date': time_str, 'x-amz-security-token': session}
        header_str = ''.join((f'{k}:{v}\n' for k, v in headers.items()))
        header_names = ';'.join(headers)

        body = req.body  # TODO Check if can change to request.data
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
        request_str = f'{req.method}\n{uri}\n{query}\n{header_str}\n{header_names}\n{payload_hash}'
        action = 'aws4_request'
        scopes = (date_str, region, service, action)
        scope_str = '/'.join(scopes)
        request_hash = hashlib.sha256(request_str.encode('utf-8')).hexdigest()
        string_to_sign = f'AWS4-HMAC-SHA256\n{time_str}\n{scope_str}\n{request_hash}'
        secret_str = f'AWS4{self.aws_secret}'
        messages = tuple(message.encode('utf-8') for message in (secret_str, *scopes, string_to_sign))
        # TODO check if the HMAC can be reused
        signature = reduce(lambda v1, v2: hmac.new(v1, v2, hashlib.sha256).digest(), messages).hex()
        auth = f"AWS4-HMAC-SHA256 Credential={aws_key}/{scope_str}, SignedHeaders={header_names}, Signature={signature}"
        req.headers = {**headers, 'Authorization': auth, **req.headers}
        return req


class BaseClient:
    ENVIRON_VARIABLES = (
        ('role_arn', 'SP_API_ROLE_ARN'),
        ('endpoint', 'SP_API_ENDPOINT'),
        ('region', 'SP_API_REGION'),
        ('marketplace', 'SP_API_MARKETPLACE'),
        ('refresh_token', 'SP_API_REFRESH_TOKEN'),
        ('aws_key', 'SP_API_AWS_KEY'),
        ('aws_secret', 'SP_API_AWS_SECRET'),
        ('lwa_key', 'SP_API_LWA_KEY'),
        ('lwa_secret', 'SP_API_LWA_SECRET'),
    )

    def __init__(self, *, refresh_token: str = None,
                 role_arn: str = None, endpoint: str = None, region: str = None, marketplace: str = None,
                 aws_key: str = None, aws_secret: str = None, lwa_key: str = None, lwa_secret: str = None,
                 check_errors=True, ignore_quota_exceed: bool = True,
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
            check_errors: if True, parse response to json and raise Exception if have errors
            ignore_quota_exceed: if True, when caught quota exceeded exception, wait 0.1s and resend
        """
        parameters = dict(
            role_arn=role_arn, endpoint=endpoint, region=region, marketplace=marketplace,
            refresh_token=refresh_token,
            aws_key=aws_key, aws_secret=aws_secret, lwa_key=lwa_key, lwa_secret=lwa_secret,
            check_errors=check_errors, ignore_quota_exceed=ignore_quota_exceed,
        )

        [parameters.__setitem__(k, os.environ.get(v)) for k, v in self.ENVIRON_VARIABLES if parameters[k] is None]
        self._aws_key = parameters['aws_key']
        self._aws_secret = parameters['aws_secret']
        self._role_arn = parameters['role_arn']
        self._endpoint = parameters['endpoint']
        self._region = parameters['region']
        self._marketplace = parameters['marketplace']
        self._refresh_token = parameters['refresh_token']
        self._lwa_key = parameters['lwa_key']
        self._lwa_secret = parameters['lwa_secret']
        if any(parameters[k] is None for k, v in self.ENVIRON_VARIABLES):
            raise ValueError('Please set all parameters of the client')
        self._parameters = parameters

        self._client = boto3.client('sts', aws_access_key_id=self._aws_key, aws_secret_access_key=self._aws_secret)
        self._check_errors = check_errors
        self._ignore_quota_exceeded = ignore_quota_exceed

    # Refresh token can be used to get access token, access token will last for 1 hour
    _lwa_access_token_cache = TTLCache(maxsize=1000, ttl=3000)

    def _get_access_token(self, refresh_token: str):
        # TODO should set waiting flag for multi thread support
        if refresh_token not in self._lwa_access_token_cache:
            data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token,
                    'client_id': self._lwa_key, 'client_secret': self._lwa_secret}
            headers = {'User-Agent': 'amazon-sp-api-clients',
                       'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'}
            response = requests.post('https://api.amazon.com/auth/o2/token', data=data, headers=headers)
            access_token = response.json()['access_token']
            self._lwa_access_token_cache[refresh_token] = access_token
        return self._lwa_access_token_cache[refresh_token]

    # By assume role, a token will be received
    _aws_auth_cache = TTLCache(maxsize=1, ttl=3000)

    def _get_aws_auth(self):
        # TODO should set waiting flag for multi thread support
        if 'auth' not in self._aws_auth_cache:
            role = self._client.assume_role(RoleArn=self._role_arn, RoleSessionName='guid').get('Credentials')
            self._aws_auth_cache['auth'] = AwsSignV4(
                service='execute-api', region=self._region, aws_session_token=role.get('SessionToken'),
                aws_key=role.get('AccessKeyId'), aws_secret=role.get('SecretAccessKey'))
        return self._aws_auth_cache['auth']

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

    # Sometimes the response are required, however, current architecture is not able to return the response.
    # So, the last response is recorded here.
    # Pay attention: in multi thread program, this may cause data conflict.
    last_response: Response = None

    def request(self, path: str, *, method='GET',
                params: dict[str, str] = None,
                data: Union[dict, str, bytes] = None,
                headers: dict[str, str] = None,
                ) -> Response:

        # process params
        params = {} if params is None else params
        data = b'' if data is None else data
        data = json.dumps(data) if isinstance(data, dict) else data
        data = data.encode('utf-8') if isinstance(data, str) else data
        headers = {} if headers is None else headers
        headers = {
            'content-type': 'application/json',
            'x-amz-access-token': self._get_access_token(self._refresh_token),
            **headers,
        }
        auth = self._get_aws_auth()
        url = f'{self._endpoint}{path}'
        response = request(method=method, url=url, data=data, headers=headers, auth=auth, params=params)
        self.last_response = response

        # TODO check errors and quota exceeded should be processed later, in case to avoid decode twice

        # process quota exceeded exception
        # if not self._check_errors:
        #     return response

        # If found error, and the error is QuotaExceed, just resend the request
        # errors = self._get_response_json(response).get('errors', None)
        # if errors:
        #     if self._ignore_quota_exceeded and len(errors) == 1 \
        #             and 'code' in errors[0] and errors[0]['code'] == 'QuotaExceeded':
        #         sleep(0.1)
        #         return self.request(path, data=data, params=params, headers=headers, method=method)
        #     else:
        #         raise SellingApiError(errors)

        return response


class BaseAmazonSpApiClients(BaseClient):
    selling_api_error = SellingApiError

    @cached_property
    def marketplaces(self):
        from .marketplaces import MarketPlaces
        return MarketPlaces
