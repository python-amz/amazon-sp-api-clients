from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class Granularity(__BaseDictObject):
    """
    Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "granularityType" in data:
            self.granularityType: str = self._get_value(str, "granularityType")
        else:
            self.granularityType: str = None
        if "granularityId" in data:
            self.granularityId: str = self._get_value(str, "granularityId")
        else:
            self.granularityId: str = None


class ReservedQuantity(__BaseDictObject):
    """
    The quantity of reserved inventory.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalReservedQuantity" in data:
            self.totalReservedQuantity: int = self._get_value(int, "totalReservedQuantity")
        else:
            self.totalReservedQuantity: int = None
        if "pendingCustomerOrderQuantity" in data:
            self.pendingCustomerOrderQuantity: int = self._get_value(int, "pendingCustomerOrderQuantity")
        else:
            self.pendingCustomerOrderQuantity: int = None
        if "pendingTransshipmentQuantity" in data:
            self.pendingTransshipmentQuantity: int = self._get_value(int, "pendingTransshipmentQuantity")
        else:
            self.pendingTransshipmentQuantity: int = None
        if "fcProcessingQuantity" in data:
            self.fcProcessingQuantity: int = self._get_value(int, "fcProcessingQuantity")
        else:
            self.fcProcessingQuantity: int = None


class ResearchingQuantityEntry(__BaseDictObject):
    """
    The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "quantity" in data:
            self.quantity: int = self._get_value(int, "quantity")
        else:
            self.quantity: int = None


class ResearchingQuantity(__BaseDictObject):
    """
    The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalResearchingQuantity" in data:
            self.totalResearchingQuantity: int = self._get_value(int, "totalResearchingQuantity")
        else:
            self.totalResearchingQuantity: int = None
        if "researchingQuantityBreakdown" in data:
            self.researchingQuantityBreakdown: _List[ResearchingQuantityEntry] = [
                ResearchingQuantityEntry(datum) for datum in data["researchingQuantityBreakdown"]
            ]
        else:
            self.researchingQuantityBreakdown: _List[ResearchingQuantityEntry] = []


class UnfulfillableQuantity(__BaseDictObject):
    """
    The quantity of unfulfillable inventory.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalUnfulfillableQuantity" in data:
            self.totalUnfulfillableQuantity: int = self._get_value(int, "totalUnfulfillableQuantity")
        else:
            self.totalUnfulfillableQuantity: int = None
        if "customerDamagedQuantity" in data:
            self.customerDamagedQuantity: int = self._get_value(int, "customerDamagedQuantity")
        else:
            self.customerDamagedQuantity: int = None
        if "warehouseDamagedQuantity" in data:
            self.warehouseDamagedQuantity: int = self._get_value(int, "warehouseDamagedQuantity")
        else:
            self.warehouseDamagedQuantity: int = None
        if "distributorDamagedQuantity" in data:
            self.distributorDamagedQuantity: int = self._get_value(int, "distributorDamagedQuantity")
        else:
            self.distributorDamagedQuantity: int = None
        if "carrierDamagedQuantity" in data:
            self.carrierDamagedQuantity: int = self._get_value(int, "carrierDamagedQuantity")
        else:
            self.carrierDamagedQuantity: int = None
        if "defectiveQuantity" in data:
            self.defectiveQuantity: int = self._get_value(int, "defectiveQuantity")
        else:
            self.defectiveQuantity: int = None
        if "expiredQuantity" in data:
            self.expiredQuantity: int = self._get_value(int, "expiredQuantity")
        else:
            self.expiredQuantity: int = None


class InventoryDetails(__BaseDictObject):
    """
    Summarized inventory details. This object will not appear if the details parameter in the request is false.
    """

    def __init__(self, data):
        super().__init__(data)
        if "fulfillableQuantity" in data:
            self.fulfillableQuantity: int = self._get_value(int, "fulfillableQuantity")
        else:
            self.fulfillableQuantity: int = None
        if "inboundWorkingQuantity" in data:
            self.inboundWorkingQuantity: int = self._get_value(int, "inboundWorkingQuantity")
        else:
            self.inboundWorkingQuantity: int = None
        if "inboundShippedQuantity" in data:
            self.inboundShippedQuantity: int = self._get_value(int, "inboundShippedQuantity")
        else:
            self.inboundShippedQuantity: int = None
        if "inboundReceivingQuantity" in data:
            self.inboundReceivingQuantity: int = self._get_value(int, "inboundReceivingQuantity")
        else:
            self.inboundReceivingQuantity: int = None
        if "reservedQuantity" in data:
            self.reservedQuantity: ReservedQuantity = self._get_value(ReservedQuantity, "reservedQuantity")
        else:
            self.reservedQuantity: ReservedQuantity = None
        if "researchingQuantity" in data:
            self.researchingQuantity: ResearchingQuantity = self._get_value(ResearchingQuantity, "researchingQuantity")
        else:
            self.researchingQuantity: ResearchingQuantity = None
        if "unfulfillableQuantity" in data:
            self.unfulfillableQuantity: UnfulfillableQuantity = self._get_value(
                UnfulfillableQuantity, "unfulfillableQuantity"
            )
        else:
            self.unfulfillableQuantity: UnfulfillableQuantity = None


class InventorySummary(__BaseDictObject):
    """
    Inventory summary for a specific item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "fnSku" in data:
            self.fnSku: str = self._get_value(str, "fnSku")
        else:
            self.fnSku: str = None
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "condition" in data:
            self.condition: str = self._get_value(str, "condition")
        else:
            self.condition: str = None
        if "inventoryDetails" in data:
            self.inventoryDetails: InventoryDetails = self._get_value(InventoryDetails, "inventoryDetails")
        else:
            self.inventoryDetails: InventoryDetails = None
        if "lastUpdatedTime" in data:
            self.lastUpdatedTime: str = self._get_value(str, "lastUpdatedTime")
        else:
            self.lastUpdatedTime: str = None
        if "productName" in data:
            self.productName: str = self._get_value(str, "productName")
        else:
            self.productName: str = None
        if "totalQuantity" in data:
            self.totalQuantity: int = self._get_value(int, "totalQuantity")
        else:
            self.totalQuantity: int = None


class Pagination(__BaseDictObject):
    """
    The process of returning the results to a request in batches of a defined size called pages. This is done to exercise some control over result size and overall throughput. It's a form of traffic management.
    """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None


class GetInventorySummariesResult(__BaseDictObject):
    """
    The payload schema for the getInventorySummaries operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "granularity" in data:
            self.granularity: Granularity = self._get_value(Granularity, "granularity")
        else:
            self.granularity: Granularity = None
        if "inventorySummaries" in data:
            self.inventorySummaries: InventorySummaries = self._get_value(InventorySummaries, "inventorySummaries")
        else:
            self.inventorySummaries: InventorySummaries = None


class GetInventorySummariesResponse(__BaseDictObject):
    """
    The Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetInventorySummariesResult = self._get_value(GetInventorySummariesResult, "payload")
        else:
            self.payload: GetInventorySummariesResult = None
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Error(__BaseDictObject):
    """
    An error response returned when the request is unsuccessful.
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


class InventorySummaries(list, _List["InventorySummary"]):
    """
    A list of inventory summaries.
    """

    def __init__(self, data):
        super().__init__([InventorySummary(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class FbaInventoryV1Client(__BaseClient):
    def getInventorySummaries(
        self,
        granularityType: str,
        granularityId: str,
        marketplaceIds: _List[str],
        details: bool = None,
        startDateTime: str = None,
        sellerSkus: _List[str] = None,
        sellerSku: str = None,
        nextToken: str = None,
    ):
        """
                Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the `startDateTime`, `sellerSkus` and `sellerSku` parameters:
        - All inventory summaries with available details are returned when the `startDateTime`, `sellerSkus` and `sellerSku` parameters are omitted.
        - When `startDateTime` is provided, the operation returns inventory summaries that have had changes after the date and time specified. The `sellerSkus` and `sellerSku` parameters are ignored. **Important:** To avoid errors, use both `startDateTime` and `nextToken` to get the next page of inventory summaries that have changed after the date and time specified.
        - When the `sellerSkus` parameter is provided, the operation returns inventory summaries for only the specified `sellerSkus`. The `sellerSku` parameter is ignored.
        - When the `sellerSku` parameter is provided, the operation returns inventory summaries for only the specified `sellerSku`.
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/fba/inventory/v1/summaries"
        params = {}
        if details is not None:
            params["details"] = details
        if granularityType is not None:
            params["granularityType"] = granularityType
        if granularityId is not None:
            params["granularityId"] = granularityId
        if startDateTime is not None:
            params["startDateTime"] = startDateTime
        if sellerSkus is not None:
            params["sellerSkus"] = ",".join(map(str, sellerSkus))
        if sellerSku is not None:
            params["sellerSku"] = sellerSku
        if nextToken is not None:
            params["nextToken"] = nextToken
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetInventorySummariesResponse,
            400: GetInventorySummariesResponse,
            403: GetInventorySummariesResponse,
            404: GetInventorySummariesResponse,
            429: GetInventorySummariesResponse,
            500: GetInventorySummariesResponse,
            503: GetInventorySummariesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
