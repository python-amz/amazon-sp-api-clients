from .base import BaseClient as __BaseClient
from typing import List as _List


class GetItemEligibilityPreviewResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ItemEligibilityPreview = ItemEligibilityPreview(data["payload"])
        else:
            self.payload: ItemEligibilityPreview = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ItemEligibilityPreview:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "program" in data:
            self.program: str = str(data["program"])
        else:
            self.program: str = None
        if "isEligibleForProgram" in data:
            self.isEligibleForProgram: bool = bool(data["isEligibleForProgram"])
        else:
            self.isEligibleForProgram: bool = None
        if "ineligibilityReasonList" in data:
            self.ineligibilityReasonList: _List[str] = [str(datum) for datum in data["ineligibilityReasonList"]]
        else:
            self.ineligibilityReasonList: _List[str] = []


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


class FbaInboundEligibilityClient(__BaseClient):
    def getItemEligibilityPreview(
        self,
        asin: str,
        program: str,
        marketplaceIds: _List[str] = None,
    ):
        url = "/fba/inbound/v1/eligibility/itemPreview".format()
        data = {}
        if marketplaceIds is not None:
            data["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if asin is not None:
            data["asin"] = (asin,)
        if program is not None:
            data["program"] = (program,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetItemEligibilityPreviewResponse,
            400: GetItemEligibilityPreviewResponse,
            401: GetItemEligibilityPreviewResponse,
            403: GetItemEligibilityPreviewResponse,
            404: GetItemEligibilityPreviewResponse,
            429: GetItemEligibilityPreviewResponse,
            500: GetItemEligibilityPreviewResponse,
            503: GetItemEligibilityPreviewResponse,
        }[response.status_code](response.json())
