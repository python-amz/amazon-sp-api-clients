from .base import BaseClient as __BaseClient
from typing import List as _List


class GetAuthorizationCodeResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: AuthorizationCode = AuthorizationCode(data["payload"])
        else:
            self.payload: AuthorizationCode = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class AuthorizationCode:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "authorizationCode" in data:
            self.authorizationCode: str = str(data["authorizationCode"])
        else:
            self.authorizationCode: str = None


class Error:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
        else:
            self.details: str = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class AuthorizationV1Client(__BaseClient):
    def getAuthorizationCode(
        self,
        sellingPartnerId: str,
        developerId: str,
        mwsAuthToken: str,
    ):
        url = "/authorization/v1/authorizationCode".format()
        params = {}
        if sellingPartnerId is not None:
            params["sellingPartnerId"] = (sellingPartnerId,)
        if developerId is not None:
            params["developerId"] = (developerId,)
        if mwsAuthToken is not None:
            params["mwsAuthToken"] = (mwsAuthToken,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetAuthorizationCodeResponse,
            400: GetAuthorizationCodeResponse,
            403: GetAuthorizationCodeResponse,
            404: GetAuthorizationCodeResponse,
            413: GetAuthorizationCodeResponse,
            415: GetAuthorizationCodeResponse,
            429: GetAuthorizationCodeResponse,
            500: GetAuthorizationCodeResponse,
            503: GetAuthorizationCodeResponse,
        }[response.status_code](self.__get_response_json(response))
