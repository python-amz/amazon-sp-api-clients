from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


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


class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Item:
    """
    A listings item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "sku" in data:
            self.sku: str = str(data["sku"])
        else:
            self.sku: str = None
        if "summaries" in data:
            self.summaries: ItemSummaries = ItemSummaries(data["summaries"])
        else:
            self.summaries: ItemSummaries = None
        if "attributes" in data:
            self.attributes: ItemAttributes = ItemAttributes(data["attributes"])
        else:
            self.attributes: ItemAttributes = None
        if "issues" in data:
            self.issues: ItemIssues = ItemIssues(data["issues"])
        else:
            self.issues: ItemIssues = None
        if "offers" in data:
            self.offers: ItemOffers = ItemOffers(data["offers"])
        else:
            self.offers: ItemOffers = None
        if "fulfillmentAvailability" in data:
            self.fulfillmentAvailability: _List[FulfillmentAvailability] = [
                FulfillmentAvailability(datum) for datum in data["fulfillmentAvailability"]
            ]
        else:
            self.fulfillmentAvailability: _List[FulfillmentAvailability] = []
        if "procurement" in data:
            self.procurement: ItemProcurement = ItemProcurement(data["procurement"])
        else:
            self.procurement: ItemProcurement = None


class ItemSummaryByMarketplace:
    """
    Summary details of a listings item for an Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None
        if "conditionType" in data:
            self.conditionType: str = str(data["conditionType"])
        else:
            self.conditionType: str = None
        if "status" in data:
            self.status: _List[str] = [str(datum) for datum in data["status"]]
        else:
            self.status: _List[str] = []
        if "fnSku" in data:
            self.fnSku: str = str(data["fnSku"])
        else:
            self.fnSku: str = None
        if "itemName" in data:
            self.itemName: str = str(data["itemName"])
        else:
            self.itemName: str = None
        if "createdDate" in data:
            self.createdDate: str = str(data["createdDate"])
        else:
            self.createdDate: str = None
        if "lastUpdatedDate" in data:
            self.lastUpdatedDate: str = str(data["lastUpdatedDate"])
        else:
            self.lastUpdatedDate: str = None
        if "mainImage" in data:
            self.mainImage: ItemImage = ItemImage(data["mainImage"])
        else:
            self.mainImage: ItemImage = None


class ItemImage:
    """
    Image for the listings item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "link" in data:
            self.link: str = str(data["link"])
        else:
            self.link: str = None
        if "height" in data:
            self.height: int = int(data["height"])
        else:
            self.height: int = None
        if "width" in data:
            self.width: int = int(data["width"])
        else:
            self.width: int = None


class ItemAttributes:
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data


class Issue:
    """
    An issue with a listings item.
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
        if "severity" in data:
            self.severity: str = str(data["severity"])
        else:
            self.severity: str = None
        if "attributeNames" in data:
            self.attributeNames: _List[str] = [str(datum) for datum in data["attributeNames"]]
        else:
            self.attributeNames: _List[str] = []


class ItemOfferByMarketplace:
    """
    Offer details of a listings item for an Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "offerType" in data:
            self.offerType: str = str(data["offerType"])
        else:
            self.offerType: str = None
        if "price" in data:
            self.price: Money = Money(data["price"])
        else:
            self.price: Money = None
        if "points" in data:
            self.points: Points = Points(data["points"])
        else:
            self.points: Points = None


class ItemProcurement:
    """
    Vendor procurement information for the listings item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "costPrice" in data:
            self.costPrice: Money = Money(data["costPrice"])
        else:
            self.costPrice: Money = None


class FulfillmentAvailability:
    """
    Fulfillment availability details for the listings item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "fulfillmentChannelCode" in data:
            self.fulfillmentChannelCode: str = str(data["fulfillmentChannelCode"])
        else:
            self.fulfillmentChannelCode: str = None
        if "quantity" in data:
            self.quantity: int = int(data["quantity"])
        else:
            self.quantity: int = None


class Money:
    """
    The currency type and the amount.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "currencyCode" in data:
            self.currencyCode: str = str(data["currencyCode"])
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = Decimal(data["amount"])
        else:
            self.amount: Decimal = None


class Points:
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points element is only returned in Japan (JP).
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "pointsNumber" in data:
            self.pointsNumber: int = int(data["pointsNumber"])
        else:
            self.pointsNumber: int = None


class PatchOperation:
    """
    Individual JSON Patch operation for an HTTP PATCH request.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "op" in data:
            self.op: str = str(data["op"])
        else:
            self.op: str = None
        if "path" in data:
            self.path: str = str(data["path"])
        else:
            self.path: str = None
        if "value" in data:
            self.value: _List[dict] = [dict(datum) for datum in data["value"]]
        else:
            self.value: _List[dict] = []


class ListingsItemPatchRequest:
    """
    The request body schema for the patchListingsItem operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None
        if "patches" in data:
            self.patches: _List[PatchOperation] = [PatchOperation(datum) for datum in data["patches"]]
        else:
            self.patches: _List[PatchOperation] = []


class ListingsItemPutRequest:
    """
    The request body schema for the putListingsItem operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None
        if "requirements" in data:
            self.requirements: str = str(data["requirements"])
        else:
            self.requirements: str = None
        if "attributes" in data:
            self.attributes: dict = dict(data["attributes"])
        else:
            self.attributes: dict = None


class ListingsItemSubmissionResponse:
    """
    Response containing the results of a submission to the Selling Partner API for Listings Items.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "sku" in data:
            self.sku: str = str(data["sku"])
        else:
            self.sku: str = None
        if "status" in data:
            self.status: str = str(data["status"])
        else:
            self.status: str = None
        if "submissionId" in data:
            self.submissionId: str = str(data["submissionId"])
        else:
            self.submissionId: str = None
        if "issues" in data:
            self.issues: _List[Issue] = [Issue(datum) for datum in data["issues"]]
        else:
            self.issues: _List[Issue] = []


class ItemSummaries(list, _List["ItemSummaryByMarketplace"]):
    """
    Summary details of a listings item.
    """

    def __init__(self, data):
        super().__init__([ItemSummaryByMarketplace(datum) for datum in data])
        self.data = data


class ItemIssues(list, _List["Issue"]):
    """
    Issues associated with the listings item.
    """

    def __init__(self, data):
        super().__init__([Issue(datum) for datum in data])
        self.data = data


class ItemOffers(list, _List["ItemOfferByMarketplace"]):
    """
    Offer details for the listings item.
    """

    def __init__(self, data):
        super().__init__([ItemOfferByMarketplace(datum) for datum in data])
        self.data = data


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """


class ListingsItems20210801Client(__BaseClient):
    def getListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
        includedData: _List[str] = None,
    ):
        """
                Returns details about a listings item for a selling partner.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        if includedData is not None:
            params["includedData"] = ",".join(map(str, includedData))
        response = self.request(url, method="GET", params=params)
        return {
            200: Item,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    def putListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        """
                Creates a new or fully-updates an existing listings item for a selling partner.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        response = self.request(url, method="PUT", data=params)
        return {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    def deleteListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        """
                Delete a listings item for a selling partner.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        response = self.request(url, method="DELETE", data=params)
        return {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    def patchListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        """
                Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        response = self.request(url, method="PATCH", data=params)
        return {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))
