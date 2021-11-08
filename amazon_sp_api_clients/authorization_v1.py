from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class GetAuthorizationCodeResponse:
    """
    The response schema for the GetAuthorizationCode operation.
    """

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
    """
    A Login with Amazon (LWA) authorization code.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "authorizationCode" in data:
            self.authorizationCode: str = str(data["authorizationCode"])
        else:
            self.authorizationCode: str = None


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

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
    """
    A list of error responses returned when a request is unsuccessful.
    """

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
        """
                With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization code that will allow you to call a Selling Partner API on behalf of a seller who has already authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that the seller previously granted you. The operation returns an LWA authorization code that can be exchanged for a refresh token and access token representing authorization to call the Selling Partner API on the seller's behalf. By using this API, sellers who have already authorized you for Amazon MWS do not need to re-authorize you for the Selling Partner API.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/authorization/v1/authorizationCode"
        params = {}
        if sellingPartnerId is not None:
            params["sellingPartnerId"] = sellingPartnerId
        if developerId is not None:
            params["developerId"] = developerId
        if mwsAuthToken is not None:
            params["mwsAuthToken"] = mwsAuthToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetAuthorizationCodeResponse,
            400: GetAuthorizationCodeResponse,
            403: GetAuthorizationCodeResponse,
            404: GetAuthorizationCodeResponse,
            413: GetAuthorizationCodeResponse,
            415: GetAuthorizationCodeResponse,
            429: GetAuthorizationCodeResponse,
            500: GetAuthorizationCodeResponse,
            503: GetAuthorizationCodeResponse,
        }[response.status_code]
        return None if response_type is None else response_type(self._get_response_json(response))
