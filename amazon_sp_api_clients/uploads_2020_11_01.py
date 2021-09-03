from .base import BaseClient as __BaseClient
from typing import List as _List


class CreateUploadDestinationResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: UploadDestination = UploadDestination(data["payload"])
        else:
            self.payload: UploadDestination = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class UploadDestination:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = str(data["uploadDestinationId"])
        else:
            self.uploadDestinationId: str = None
        if "url" in data:
            self.url: str = str(data["url"])
        else:
            self.url: str = None
        if "headers" in data:
            self.headers: dict = dict(data["headers"])
        else:
            self.headers: dict = None


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


class Uploads20201101Client(__BaseClient):
    def createUploadDestinationForResource(
        self,
        resource: str,
        marketplaceIds: _List[str],
        contentMD5: str,
        contentType: str = None,
    ):
        url = "/uploads/2020-11-01/uploadDestinations/{resource}".format(
            resource=resource,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if contentMD5 is not None:
            params["contentMD5"] = (contentMD5,)
        if contentType is not None:
            params["contentType"] = (contentType,)
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateUploadDestinationResponse,
            400: CreateUploadDestinationResponse,
            403: CreateUploadDestinationResponse,
            404: CreateUploadDestinationResponse,
            413: CreateUploadDestinationResponse,
            415: CreateUploadDestinationResponse,
            429: CreateUploadDestinationResponse,
            500: CreateUploadDestinationResponse,
            503: CreateUploadDestinationResponse,
        }[response.status_code](self._get_response_json(response))
