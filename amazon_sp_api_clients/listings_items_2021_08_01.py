from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


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


class ErrorList(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Item(__BaseDictObject):
    """
    A listings item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sku" in data:
            self.sku: str = self._get_value(str, "sku")
        else:
            self.sku: str = None
        if "summaries" in data:
            self.summaries: ItemSummaries = self._get_value(ItemSummaries, "summaries")
        else:
            self.summaries: ItemSummaries = None
        if "attributes" in data:
            self.attributes: ItemAttributes = self._get_value(ItemAttributes, "attributes")
        else:
            self.attributes: ItemAttributes = None
        if "issues" in data:
            self.issues: ItemIssues = self._get_value(ItemIssues, "issues")
        else:
            self.issues: ItemIssues = None
        if "offers" in data:
            self.offers: ItemOffers = self._get_value(ItemOffers, "offers")
        else:
            self.offers: ItemOffers = None
        if "fulfillmentAvailability" in data:
            self.fulfillmentAvailability: _List[FulfillmentAvailability] = [
                FulfillmentAvailability(datum) for datum in data["fulfillmentAvailability"]
            ]
        else:
            self.fulfillmentAvailability: _List[FulfillmentAvailability] = []
        if "procurement" in data:
            self.procurement: _List[ItemProcurement] = [ItemProcurement(datum) for datum in data["procurement"]]
        else:
            self.procurement: _List[ItemProcurement] = []


class ItemSummaryByMarketplace(__BaseDictObject):
    """
    Summary details of a listings item for an Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "productType" in data:
            self.productType: str = self._get_value(str, "productType")
        else:
            self.productType: str = None
        if "conditionType" in data:
            self.conditionType: str = self._get_value(str, "conditionType")
        else:
            self.conditionType: str = None
        if "status" in data:
            self.status: _List[str] = [str(datum) for datum in data["status"]]
        else:
            self.status: _List[str] = []
        if "fnSku" in data:
            self.fnSku: str = self._get_value(str, "fnSku")
        else:
            self.fnSku: str = None
        if "itemName" in data:
            self.itemName: str = self._get_value(str, "itemName")
        else:
            self.itemName: str = None
        if "createdDate" in data:
            self.createdDate: str = self._get_value(str, "createdDate")
        else:
            self.createdDate: str = None
        if "lastUpdatedDate" in data:
            self.lastUpdatedDate: str = self._get_value(str, "lastUpdatedDate")
        else:
            self.lastUpdatedDate: str = None
        if "mainImage" in data:
            self.mainImage: ItemImage = self._get_value(ItemImage, "mainImage")
        else:
            self.mainImage: ItemImage = None


class ItemImage(__BaseDictObject):
    """
    Image for the listings item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "link" in data:
            self.link: str = self._get_value(str, "link")
        else:
            self.link: str = None
        if "height" in data:
            self.height: int = self._get_value(int, "height")
        else:
            self.height: int = None
        if "width" in data:
            self.width: int = self._get_value(int, "width")
        else:
            self.width: int = None


class ItemAttributes(__BaseDictObject):
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    def __init__(self, data):
        super().__init__(data)


class Issue(__BaseDictObject):
    """
    An issue with a listings item.
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
        if "severity" in data:
            self.severity: str = self._get_value(str, "severity")
        else:
            self.severity: str = None
        if "attributeNames" in data:
            self.attributeNames: _List[str] = [str(datum) for datum in data["attributeNames"]]
        else:
            self.attributeNames: _List[str] = []


class ItemOfferByMarketplace(__BaseDictObject):
    """
    Offer details of a listings item for an Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "offerType" in data:
            self.offerType: str = self._get_value(str, "offerType")
        else:
            self.offerType: str = None
        if "price" in data:
            self.price: Money = self._get_value(Money, "price")
        else:
            self.price: Money = None
        if "points" in data:
            self.points: Points = self._get_value(Points, "points")
        else:
            self.points: Points = None


class ItemProcurement(__BaseDictObject):
    """
    Vendor procurement information for the listings item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "costPrice" in data:
            self.costPrice: Money = self._get_value(Money, "costPrice")
        else:
            self.costPrice: Money = None


class FulfillmentAvailability(__BaseDictObject):
    """
    Fulfillment availability details for the listings item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "fulfillmentChannelCode" in data:
            self.fulfillmentChannelCode: str = self._get_value(str, "fulfillmentChannelCode")
        else:
            self.fulfillmentChannelCode: str = None
        if "quantity" in data:
            self.quantity: int = self._get_value(int, "quantity")
        else:
            self.quantity: int = None


class Money(__BaseDictObject):
    """
    The currency type and the amount.
    """

    def __init__(self, data):
        super().__init__(data)
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = self._get_value(Decimal, "amount")
        else:
            self.amount: Decimal = None


class Points(__BaseDictObject):
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points element is only returned in Japan (JP).
    """

    def __init__(self, data):
        super().__init__(data)
        if "pointsNumber" in data:
            self.pointsNumber: int = self._get_value(int, "pointsNumber")
        else:
            self.pointsNumber: int = None


class PatchOperation(__BaseDictObject):
    """
    Individual JSON Patch operation for an HTTP PATCH request.
    """

    def __init__(self, data):
        super().__init__(data)
        if "op" in data:
            self.op: str = self._get_value(str, "op")
        else:
            self.op: str = None
        if "path" in data:
            self.path: str = self._get_value(str, "path")
        else:
            self.path: str = None
        if "value" in data:
            self.value: _List[dict] = [dict(datum) for datum in data["value"]]
        else:
            self.value: _List[dict] = []


class ListingsItemPatchRequest(__BaseDictObject):
    """
    The request body schema for the patchListingsItem operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "productType" in data:
            self.productType: str = self._get_value(str, "productType")
        else:
            self.productType: str = None
        if "patches" in data:
            self.patches: _List[PatchOperation] = [PatchOperation(datum) for datum in data["patches"]]
        else:
            self.patches: _List[PatchOperation] = []


class ListingsItemPutRequest(__BaseDictObject):
    """
    The request body schema for the putListingsItem operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "productType" in data:
            self.productType: str = self._get_value(str, "productType")
        else:
            self.productType: str = None
        if "requirements" in data:
            self.requirements: str = self._get_value(str, "requirements")
        else:
            self.requirements: str = None
        if "attributes" in data:
            self.attributes: dict = self._get_value(dict, "attributes")
        else:
            self.attributes: dict = None


class ListingsItemSubmissionResponse(__BaseDictObject):
    """
    Response containing the results of a submission to the Selling Partner API for Listings Items.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sku" in data:
            self.sku: str = self._get_value(str, "sku")
        else:
            self.sku: str = None
        if "status" in data:
            self.status: str = self._get_value(str, "status")
        else:
            self.status: str = None
        if "submissionId" in data:
            self.submissionId: str = self._get_value(str, "submissionId")
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
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/listings/2021-08-01/items/{sellerId}/{sku}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        if includedData is not None:
            params["includedData"] = ",".join(map(str, includedData))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: Item,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def putListingsItem(
        self,
        data: ListingsItemPutRequest,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        """
                Creates a new or fully-updates an existing listings item for a selling partner.
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/listings/2021-08-01/items/{sellerId}/{sku}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def deleteListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        """
                Delete a listings item for a selling partner.
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/listings/2021-08-01/items/{sellerId}/{sku}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def patchListingsItem(
        self,
        data: ListingsItemPatchRequest,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        """
                Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/listings/2021-08-01/items/{sellerId}/{sku}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = issueLocale
        response = self.request(
            path=url,
            method="PATCH",
            params=params,
            data=data.data,
        )
        response_type = {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
