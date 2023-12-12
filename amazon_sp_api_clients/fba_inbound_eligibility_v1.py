from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetItemEligibilityPreviewResponse(__BaseDictObject):
    """
    The response schema for the getItemEligibilityPreview operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ItemEligibilityPreview = self._get_value(ItemEligibilityPreview, "payload")
        else:
            self.payload: ItemEligibilityPreview = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ItemEligibilityPreview(__BaseDictObject):
    """
    The response object which contains the ASIN, marketplaceId if required, eligibility program, the eligibility status (boolean), and a list of ineligibility reason codes.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "program" in data:
            self.program: str = self._get_value(str, "program")
        else:
            self.program: str = None
        if "isEligibleForProgram" in data:
            self.isEligibleForProgram: bool = self._get_value(convert_bool, "isEligibleForProgram")
        else:
            self.isEligibleForProgram: bool = None
        if "ineligibilityReasonList" in data:
            self.ineligibilityReasonList: _List[str] = [str(datum) for datum in data["ineligibilityReasonList"]]
        else:
            self.ineligibilityReasonList: _List[str] = []


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


class FbaInboundEligibilityV1Client(__BaseClient):
    def getItemEligibilityPreview(
        self,
        asin: str,
        program: str,
        marketplaceIds: _List[str] = None,
    ):
        """
                This operation gets an eligibility preview for an item that you specify. You can specify the type of eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify the marketplace in which you want to determine the item's eligibility.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/fba/inbound/v1/eligibility/itemPreview"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if asin is not None:
            params["asin"] = asin
        if program is not None:
            params["program"] = program
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetItemEligibilityPreviewResponse,
            400: GetItemEligibilityPreviewResponse,
            401: GetItemEligibilityPreviewResponse,
            403: GetItemEligibilityPreviewResponse,
            404: GetItemEligibilityPreviewResponse,
            429: GetItemEligibilityPreviewResponse,
            500: GetItemEligibilityPreviewResponse,
            503: GetItemEligibilityPreviewResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
