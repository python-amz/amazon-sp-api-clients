from .base import BaseClient as __BaseClient
from typing import List as _List


class Granularity:
    def __init__(self, data):
        super().__init__()
        if "granularityType" in data:
            self.granularityType: str = str(data["granularityType"])
        else:
            self.granularityType: str = None
        if "granularityId" in data:
            self.granularityId: str = str(data["granularityId"])
        else:
            self.granularityId: str = None


class ReservedQuantity:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "quantity" in data:
            self.quantity: int = int(data["quantity"])
        else:
            self.quantity: int = None


class ResearchingQuantity:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class GetInventorySummariesResult:
    def __init__(self, data):
        super().__init__()
        if "granularity" in data:
            self.granularity: Granularity = Granularity(data["granularity"])
        else:
            self.granularity: Granularity = None
        if "inventorySummaries" in data:
            self.inventorySummaries: InventorySummaries = InventorySummaries(data["inventorySummaries"])
        else:
            self.inventorySummaries: InventorySummaries = None


class GetInventorySummariesResponse:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__([InventorySummary(datum) for datum in data])


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])


class FbaInventoryClient(__BaseClient):
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
        data = {}
        if details is not None:
            data["details"] = (details,)
        if granularityType is not None:
            data["granularityType"] = (granularityType,)
        if granularityId is not None:
            data["granularityId"] = (granularityId,)
        if startDateTime is not None:
            data["startDateTime"] = (startDateTime,)
        if sellerSkus is not None:
            data["sellerSkus"] = ",".join(map(str, sellerSkus))
        if nextToken is not None:
            data["nextToken"] = (nextToken,)
        if marketplaceIds is not None:
            data["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=data)
        return {
            200: GetInventorySummariesResponse,
            400: GetInventorySummariesResponse,
            403: GetInventorySummariesResponse,
            404: GetInventorySummariesResponse,
            429: GetInventorySummariesResponse,
            500: GetInventorySummariesResponse,
            503: GetInventorySummariesResponse,
        }[response.status_code](response.json())
