from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class CreateUploadDestinationResponse:
    """
    The response schema for the createUploadDestination operation.
    """

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
    """
    Information about an upload destination.
    """

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


class Uploads20201101Client(__BaseClient):
    """
        Creates an upload destination, returning the information required to upload a file to the destination and to programmatically access the file.
    **Usage Plan:**
    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .1 | 5 |
    For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

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
            params["contentMD5"] = contentMD5
        if contentType is not None:
            params["contentType"] = contentType
        response = self.request(url, method="POST", data=params)
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
