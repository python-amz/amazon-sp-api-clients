from .base import BaseClient as __BaseClient
from typing import List as _List


class CreateRestrictedDataTokenRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "restrictedResources" in data:
            self.restrictedResources: _List[RestrictedResource] = [
                RestrictedResource(datum) for datum in data["restrictedResources"]
            ]
        else:
            self.restrictedResources: _List[RestrictedResource] = []


class RestrictedResource:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "method" in data:
            self.method: str = str(data["method"])
        else:
            self.method: str = None
        if "path" in data:
            self.path: str = str(data["path"])
        else:
            self.path: str = None


class CreateRestrictedDataTokenResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "restrictedDataToken" in data:
            self.restrictedDataToken: str = str(data["restrictedDataToken"])
        else:
            self.restrictedDataToken: str = None
        if "expiresIn" in data:
            self.expiresIn: int = int(data["expiresIn"])
        else:
            self.expiresIn: int = None


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


class ErrorList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Tokens20210301Client(__BaseClient):
    def createRestrictedDataToken(
        self,
        data: CreateRestrictedDataTokenRequest,
    ):
        url = "/tokens/2021-03-01/restrictedDataToken".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            200: CreateRestrictedDataTokenResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))
