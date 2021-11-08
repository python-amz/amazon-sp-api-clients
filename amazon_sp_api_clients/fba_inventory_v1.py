from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class Granularity:
    """
    Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "granularityType" in data:
            self.granularityType: str = str(data["granularityType"])
        else:
            self.granularityType: str = None
        if "granularityId" in data:
            self.granularityId: str = str(data["granularityId"])
        else:
            self.granularityId: str = None


class ReservedQuantity:
    """
    The quantity of reserved inventory.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "totalReservedQuantity" in data:
            self.totalReservedQuantity: int = int(data["totalReservedQuantity"])
        else:
            self.totalReservedQuantity: int = None
        if "pendingCustomerOrderQuantity" in data:
            self.pendingCustomerOrderQuantity: int = int(data["pendingCustomerOrderQuantity"])
        else:
            self.pendingCustomerOrderQuantity: int = None
        if "pendingTransshipmentQuantity" in data:
            self.pendingTransshipmentQuantity: int = int(data["pendingTransshipmentQuantity"])
        else:
            self.pendingTransshipmentQuantity: int = None
        if "fcProcessingQuantity" in data:
            self.fcProcessingQuantity: int = int(data["fcProcessingQuantity"])
        else:
            self.fcProcessingQuantity: int = None


class ResearchingQuantityEntry:
    """
    The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "quantity" in data:
            self.quantity: int = int(data["quantity"])
        else:
            self.quantity: int = None


class ResearchingQuantity:
    """
    The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "totalResearchingQuantity" in data:
            self.totalResearchingQuantity: int = int(data["totalResearchingQuantity"])
        else:
            self.totalResearchingQuantity: int = None
        if "researchingQuantityBreakdown" in data:
            self.researchingQuantityBreakdown: _List[ResearchingQuantityEntry] = [
                ResearchingQuantityEntry(datum) for datum in data["researchingQuantityBreakdown"]
            ]
        else:
            self.researchingQuantityBreakdown: _List[ResearchingQuantityEntry] = []


class UnfulfillableQuantity:
    """
    The quantity of unfulfillable inventory.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "totalUnfulfillableQuantity" in data:
            self.totalUnfulfillableQuantity: int = int(data["totalUnfulfillableQuantity"])
        else:
            self.totalUnfulfillableQuantity: int = None
        if "customerDamagedQuantity" in data:
            self.customerDamagedQuantity: int = int(data["customerDamagedQuantity"])
        else:
            self.customerDamagedQuantity: int = None
        if "warehouseDamagedQuantity" in data:
            self.warehouseDamagedQuantity: int = int(data["warehouseDamagedQuantity"])
        else:
            self.warehouseDamagedQuantity: int = None
        if "distributorDamagedQuantity" in data:
            self.distributorDamagedQuantity: int = int(data["distributorDamagedQuantity"])
        else:
            self.distributorDamagedQuantity: int = None
        if "carrierDamagedQuantity" in data:
            self.carrierDamagedQuantity: int = int(data["carrierDamagedQuantity"])
        else:
            self.carrierDamagedQuantity: int = None
        if "defectiveQuantity" in data:
            self.defectiveQuantity: int = int(data["defectiveQuantity"])
        else:
            self.defectiveQuantity: int = None
        if "expiredQuantity" in data:
            self.expiredQuantity: int = int(data["expiredQuantity"])
        else:
            self.expiredQuantity: int = None


class InventoryDetails:
    """
    Summarized inventory details. This object will not appear if the details parameter in the request is false.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "fulfillableQuantity" in data:
            self.fulfillableQuantity: int = int(data["fulfillableQuantity"])
        else:
            self.fulfillableQuantity: int = None
        if "inboundWorkingQuantity" in data:
            self.inboundWorkingQuantity: int = int(data["inboundWorkingQuantity"])
        else:
            self.inboundWorkingQuantity: int = None
        if "inboundShippedQuantity" in data:
            self.inboundShippedQuantity: int = int(data["inboundShippedQuantity"])
        else:
            self.inboundShippedQuantity: int = None
        if "inboundReceivingQuantity" in data:
            self.inboundReceivingQuantity: int = int(data["inboundReceivingQuantity"])
        else:
            self.inboundReceivingQuantity: int = None
        if "reservedQuantity" in data:
            self.reservedQuantity: ReservedQuantity = ReservedQuantity(data["reservedQuantity"])
        else:
            self.reservedQuantity: ReservedQuantity = None
        if "researchingQuantity" in data:
            self.researchingQuantity: ResearchingQuantity = ResearchingQuantity(data["researchingQuantity"])
        else:
            self.researchingQuantity: ResearchingQuantity = None
        if "unfulfillableQuantity" in data:
            self.unfulfillableQuantity: UnfulfillableQuantity = UnfulfillableQuantity(data["unfulfillableQuantity"])
        else:
            self.unfulfillableQuantity: UnfulfillableQuantity = None


class InventorySummary:
    """
    Inventory summary for a specific item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "fnSku" in data:
            self.fnSku: str = str(data["fnSku"])
        else:
            self.fnSku: str = None
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None
        if "inventoryDetails" in data:
            self.inventoryDetails: InventoryDetails = InventoryDetails(data["inventoryDetails"])
        else:
            self.inventoryDetails: InventoryDetails = None
        if "lastUpdatedTime" in data:
            self.lastUpdatedTime: str = str(data["lastUpdatedTime"])
        else:
            self.lastUpdatedTime: str = None
        if "productName" in data:
            self.productName: str = str(data["productName"])
        else:
            self.productName: str = None
        if "totalQuantity" in data:
            self.totalQuantity: int = int(data["totalQuantity"])
        else:
            self.totalQuantity: int = None


class Pagination:
    """
    The process of returning the results to a request in batches of a defined size called pages. This is done to exercise some control over result size and overall throughput. It's a form of traffic management.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class GetInventorySummariesResult:
    """
    The payload schema for the getInventorySummaries operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "granularity" in data:
            self.granularity: Granularity = Granularity(data["granularity"])
        else:
            self.granularity: Granularity = None
        if "inventorySummaries" in data:
            self.inventorySummaries: InventorySummaries = InventorySummaries(data["inventorySummaries"])
        else:
            self.inventorySummaries: InventorySummaries = None


class GetInventorySummariesResponse:
    """
    The Response schema.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetInventorySummariesResult = GetInventorySummariesResult(data["payload"])
        else:
            self.payload: GetInventorySummariesResult = None
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Error:
    """
    An error response returned when the request is unsuccessful.
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
    """
        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime and sellerSkus parameters:
    - All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted.
    - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored.
    - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.
    **Usage Plan:**
    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |
    For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def getInventorySummaries(
        self,
        granularityType: str,
        granularityId: str,
        marketplaceIds: _List[str],
        details: bool = None,
        startDateTime: str = None,
        sellerSkus: _List[str] = None,
        nextToken: str = None,
    ):
        url = "/fba/inventory/v1/summaries".format()
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
        if nextToken is not None:
            params["nextToken"] = nextToken
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=params)
        return {
            200: GetInventorySummariesResponse,
            400: GetInventorySummariesResponse,
            403: GetInventorySummariesResponse,
            404: GetInventorySummariesResponse,
            429: GetInventorySummariesResponse,
            500: GetInventorySummariesResponse,
            503: GetInventorySummariesResponse,
        }[response.status_code](self._get_response_json(response))
