from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class CreateUploadDestinationResponse(__BaseDictObject):
    """
    The response schema for the createUploadDestination operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: UploadDestination = self._get_value(UploadDestination, "payload")
        else:
            self.payload: UploadDestination = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class UploadDestination(__BaseDictObject):
    """
    Information about an upload destination.
    """

    def __init__(self, data):
        super().__init__(data)
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = self._get_value(str, "uploadDestinationId")
        else:
            self.uploadDestinationId: str = None
        if "url" in data:
            self.url: str = self._get_value(str, "url")
        else:
            self.url: str = None
        if "headers" in data:
            self.headers: dict = self._get_value(dict, "headers")
        else:
            self.headers: dict = None


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
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
    def createUploadDestinationForResource(
        self,
        resource: str,
        marketplaceIds: _List[str],
        contentMD5: str,
        contentType: str = None,
    ):
        """
                Creates an upload destination, returning the information required to upload a file to the destination and to programmatically access the file.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/uploads/2020-11-01/uploadDestinations/{resource}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if contentMD5 is not None:
            params["contentMD5"] = contentMD5
        if contentType is not None:
            params["contentType"] = contentType
        response = self.request(
            path=url,
            method="POST",
            params=params,
        )
        response_type = {
            201: CreateUploadDestinationResponse,
            400: CreateUploadDestinationResponse,
            403: CreateUploadDestinationResponse,
            404: CreateUploadDestinationResponse,
            413: CreateUploadDestinationResponse,
            415: CreateUploadDestinationResponse,
            429: CreateUploadDestinationResponse,
            500: CreateUploadDestinationResponse,
            503: CreateUploadDestinationResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
