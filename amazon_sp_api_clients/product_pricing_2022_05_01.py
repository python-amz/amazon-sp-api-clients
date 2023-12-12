from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetFeaturedOfferExpectedPriceBatchRequest(__BaseDictObject):
    """
    The request body for the `getFeaturedOfferExpectedPriceBatch` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "requests" in data:
            self.requests: FeaturedOfferExpectedPriceRequestList = self._get_value(
                FeaturedOfferExpectedPriceRequestList, "requests"
            )
        else:
            self.requests: FeaturedOfferExpectedPriceRequestList = None


class FeaturedOfferExpectedPriceRequestParams(__BaseDictObject):
    """
    The parameters for an individual request.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "sku" in data:
            self.sku: Sku = self._get_value(Sku, "sku")
        else:
            self.sku: Sku = None


class GetFeaturedOfferExpectedPriceBatchResponse(__BaseDictObject):
    """
    The response schema for the `getFeaturedOfferExpectedPriceBatch` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "responses" in data:
            self.responses: FeaturedOfferExpectedPriceResponseList = self._get_value(
                FeaturedOfferExpectedPriceResponseList, "responses"
            )
        else:
            self.responses: FeaturedOfferExpectedPriceResponseList = None


class CompetitiveSummaryBatchRequest(__BaseDictObject):
    """
    The `competitiveSummary` batch request data.
    """

    def __init__(self, data):
        super().__init__(data)
        if "requests" in data:
            self.requests: CompetitiveSummaryRequestList = self._get_value(CompetitiveSummaryRequestList, "requests")
        else:
            self.requests: CompetitiveSummaryRequestList = None


class CompetitiveSummaryRequest(__BaseDictObject):
    """
    An individual `competitiveSummary` request for an ASIN and `marketplaceId`.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: Asin = self._get_value(Asin, "asin")
        else:
            self.asin: Asin = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "includedData" in data:
            self.includedData: _List[CompetitiveSummaryIncludedData] = [
                CompetitiveSummaryIncludedData(datum) for datum in data["includedData"]
            ]
        else:
            self.includedData: _List[CompetitiveSummaryIncludedData] = []
        if "method" in data:
            self.method: HttpMethod = self._get_value(HttpMethod, "method")
        else:
            self.method: HttpMethod = None
        if "uri" in data:
            self.uri: HttpUri = self._get_value(HttpUri, "uri")
        else:
            self.uri: HttpUri = None


class CompetitiveSummaryBatchResponse(__BaseDictObject):
    """
    The response schema of the `competitiveSummaryBatch` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "responses" in data:
            self.responses: CompetitiveSummaryResponseList = self._get_value(
                CompetitiveSummaryResponseList, "responses"
            )
        else:
            self.responses: CompetitiveSummaryResponseList = None


class CompetitiveSummaryResponse(__BaseDictObject):
    """
    The response for the individual `competitiveSummary` request in the batch operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "status" in data:
            self.status: HttpStatusLine = self._get_value(HttpStatusLine, "status")
        else:
            self.status: HttpStatusLine = None
        if "body" in data:
            self.body: CompetitiveSummaryResponseBody = self._get_value(CompetitiveSummaryResponseBody, "body")
        else:
            self.body: CompetitiveSummaryResponseBody = None


class CompetitiveSummaryResponseBody(__BaseDictObject):
    """
    The `competitiveSummaryResponse` body for a requested ASIN and `marketplaceId`.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: Asin = self._get_value(Asin, "asin")
        else:
            self.asin: Asin = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "featuredBuyingOptions" in data:
            self.featuredBuyingOptions: _List[FeaturedBuyingOption] = [
                FeaturedBuyingOption(datum) for datum in data["featuredBuyingOptions"]
            ]
        else:
            self.featuredBuyingOptions: _List[FeaturedBuyingOption] = []
        if "errors" in data:
            self.errors: Errors = self._get_value(Errors, "errors")
        else:
            self.errors: Errors = None


class FeaturedBuyingOption(__BaseDictObject):
    """
    Describes a featured buying option which includes a list of segmented featured offers for a particular item condition.
    """

    def __init__(self, data):
        super().__init__(data)
        if "buyingOptionType" in data:
            self.buyingOptionType: str = self._get_value(str, "buyingOptionType")
        else:
            self.buyingOptionType: str = None
        if "segmentedFeaturedOffers" in data:
            self.segmentedFeaturedOffers: _List[SegmentedFeaturedOffer] = [
                SegmentedFeaturedOffer(datum) for datum in data["segmentedFeaturedOffers"]
            ]
        else:
            self.segmentedFeaturedOffers: _List[SegmentedFeaturedOffer] = []


class Offer(__BaseDictObject):
    """
    The offer data of a product.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerId" in data:
            self.sellerId: str = self._get_value(str, "sellerId")
        else:
            self.sellerId: str = None
        if "condition" in data:
            self.condition: Condition = self._get_value(Condition, "condition")
        else:
            self.condition: Condition = None
        if "fulfillmentType" in data:
            self.fulfillmentType: FulfillmentType = self._get_value(FulfillmentType, "fulfillmentType")
        else:
            self.fulfillmentType: FulfillmentType = None
        if "listingPrice" in data:
            self.listingPrice: MoneyType = self._get_value(MoneyType, "listingPrice")
        else:
            self.listingPrice: MoneyType = None
        if "shippingOptions" in data:
            self.shippingOptions: _List[ShippingOption] = [ShippingOption(datum) for datum in data["shippingOptions"]]
        else:
            self.shippingOptions: _List[ShippingOption] = []
        if "points" in data:
            self.points: Points = self._get_value(Points, "points")
        else:
            self.points: Points = None


class ShippingOption(__BaseDictObject):
    """
    The shipping option available for the offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shippingOptionType" in data:
            self.shippingOptionType: str = self._get_value(str, "shippingOptionType")
        else:
            self.shippingOptionType: str = None
        if "price" in data:
            self.price: MoneyType = self._get_value(MoneyType, "price")
        else:
            self.price: MoneyType = None


class FeaturedOfferSegment(__BaseDictObject):
    """
    Describes the segment in which the offer is featured.
    """

    def __init__(self, data):
        super().__init__(data)
        if "customerMembership" in data:
            self.customerMembership: str = self._get_value(str, "customerMembership")
        else:
            self.customerMembership: str = None
        if "segmentDetails" in data:
            self.segmentDetails: SegmentDetails = self._get_value(SegmentDetails, "segmentDetails")
        else:
            self.segmentDetails: SegmentDetails = None


class SegmentDetails(__BaseDictObject):
    """
    The details about the segment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "glanceViewWeightPercentage" in data:
            self.glanceViewWeightPercentage: float = self._get_value(float, "glanceViewWeightPercentage")
        else:
            self.glanceViewWeightPercentage: float = None


class Errors(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class FeaturedOfferExpectedPriceResponseBody(__BaseDictObject):
    """
    The featured offer expected price response data for a requested SKU.
    """

    def __init__(self, data):
        super().__init__(data)
        if "offerIdentifier" in data:
            self.offerIdentifier: OfferIdentifier = self._get_value(OfferIdentifier, "offerIdentifier")
        else:
            self.offerIdentifier: OfferIdentifier = None
        if "featuredOfferExpectedPriceResults" in data:
            self.featuredOfferExpectedPriceResults: FeaturedOfferExpectedPriceResultList = self._get_value(
                FeaturedOfferExpectedPriceResultList, "featuredOfferExpectedPriceResults"
            )
        else:
            self.featuredOfferExpectedPriceResults: FeaturedOfferExpectedPriceResultList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class FeaturedOfferExpectedPriceResult(__BaseDictObject):
    """
    The featured offer expected price result data for the requested offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "featuredOfferExpectedPrice" in data:
            self.featuredOfferExpectedPrice: FeaturedOfferExpectedPrice = self._get_value(
                FeaturedOfferExpectedPrice, "featuredOfferExpectedPrice"
            )
        else:
            self.featuredOfferExpectedPrice: FeaturedOfferExpectedPrice = None
        if "resultStatus" in data:
            self.resultStatus: str = self._get_value(str, "resultStatus")
        else:
            self.resultStatus: str = None
        if "competingFeaturedOffer" in data:
            self.competingFeaturedOffer: FeaturedOffer = self._get_value(FeaturedOffer, "competingFeaturedOffer")
        else:
            self.competingFeaturedOffer: FeaturedOffer = None
        if "currentFeaturedOffer" in data:
            self.currentFeaturedOffer: FeaturedOffer = self._get_value(FeaturedOffer, "currentFeaturedOffer")
        else:
            self.currentFeaturedOffer: FeaturedOffer = None


class FeaturedOfferExpectedPrice(__BaseDictObject):
    """
    The item price at or below which the target offer may be featured.
    """

    def __init__(self, data):
        super().__init__(data)
        if "listingPrice" in data:
            self.listingPrice: MoneyType = self._get_value(MoneyType, "listingPrice")
        else:
            self.listingPrice: MoneyType = None
        if "points" in data:
            self.points: Points = self._get_value(Points, "points")
        else:
            self.points: Points = None


class FeaturedOffer(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "offerIdentifier" in data:
            self.offerIdentifier: OfferIdentifier = self._get_value(OfferIdentifier, "offerIdentifier")
        else:
            self.offerIdentifier: OfferIdentifier = None
        if "condition" in data:
            self.condition: Condition = self._get_value(Condition, "condition")
        else:
            self.condition: Condition = None
        if "price" in data:
            self.price: Price = self._get_value(Price, "price")
        else:
            self.price: Price = None


class HttpHeaders(__BaseDictObject):
    """
    A mapping of additional HTTP headers to send/receive for an individual request within a batch.
    """

    def __init__(self, data):
        super().__init__(data)


class HttpStatusLine(__BaseDictObject):
    """
    The HTTP status line associated with the response to an individual request within a batch. For more information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
    """

    def __init__(self, data):
        super().__init__(data)
        if "statusCode" in data:
            self.statusCode: int = self._get_value(int, "statusCode")
        else:
            self.statusCode: int = None
        if "reasonPhrase" in data:
            self.reasonPhrase: str = self._get_value(str, "reasonPhrase")
        else:
            self.reasonPhrase: str = None


class HttpBody(__BaseDictObject):
    """
    Additional HTTP body information associated with an individual request within a batch.
    """

    def __init__(self, data):
        super().__init__(data)


class BatchRequest(__BaseDictObject):
    """
    The common properties for individual requests within a batch.
    """

    def __init__(self, data):
        super().__init__(data)
        if "uri" in data:
            self.uri: str = self._get_value(str, "uri")
        else:
            self.uri: str = None
        if "method" in data:
            self.method: HttpMethod = self._get_value(HttpMethod, "method")
        else:
            self.method: HttpMethod = None
        if "body" in data:
            self.body: HttpBody = self._get_value(HttpBody, "body")
        else:
            self.body: HttpBody = None
        if "headers" in data:
            self.headers: HttpHeaders = self._get_value(HttpHeaders, "headers")
        else:
            self.headers: HttpHeaders = None


class BatchResponse(__BaseDictObject):
    """
    The common properties for responses to individual requests within a batch.
    """

    def __init__(self, data):
        super().__init__(data)
        if "headers" in data:
            self.headers: HttpHeaders = self._get_value(HttpHeaders, "headers")
        else:
            self.headers: HttpHeaders = None
        if "status" in data:
            self.status: HttpStatusLine = self._get_value(HttpStatusLine, "status")
        else:
            self.status: HttpStatusLine = None


class OfferIdentifier(__BaseDictObject):
    """
    Identifies an offer from a particular seller on an ASIN.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "sellerId" in data:
            self.sellerId: str = self._get_value(str, "sellerId")
        else:
            self.sellerId: str = None
        if "sku" in data:
            self.sku: str = self._get_value(str, "sku")
        else:
            self.sku: str = None
        if "asin" in data:
            self.asin: Asin = self._get_value(Asin, "asin")
        else:
            self.asin: Asin = None
        if "fulfillmentType" in data:
            self.fulfillmentType: FulfillmentType = self._get_value(FulfillmentType, "fulfillmentType")
        else:
            self.fulfillmentType: FulfillmentType = None


class MoneyType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: float = self._get_value(float, "amount")
        else:
            self.amount: float = None


class Price(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "listingPrice" in data:
            self.listingPrice: MoneyType = self._get_value(MoneyType, "listingPrice")
        else:
            self.listingPrice: MoneyType = None
        if "shippingPrice" in data:
            self.shippingPrice: MoneyType = self._get_value(MoneyType, "shippingPrice")
        else:
            self.shippingPrice: MoneyType = None
        if "points" in data:
            self.points: Points = self._get_value(Points, "points")
        else:
            self.points: Points = None


class Points(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pointsNumber" in data:
            self.pointsNumber: int = self._get_value(int, "pointsNumber")
        else:
            self.pointsNumber: int = None
        if "pointsMonetaryValue" in data:
            self.pointsMonetaryValue: MoneyType = self._get_value(MoneyType, "pointsMonetaryValue")
        else:
            self.pointsMonetaryValue: MoneyType = None


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


class FeaturedOfferExpectedPriceRequestList(list, _List["FeaturedOfferExpectedPriceRequest"]):
    """
    A batched list of featured offer expected price requests.
    """

    def __init__(self, data):
        super().__init__([FeaturedOfferExpectedPriceRequest(datum) for datum in data])
        self.data = data


class FeaturedOfferExpectedPriceResponseList(list, _List["FeaturedOfferExpectedPriceResponse"]):
    """
    A batched list of featured offer expected price responses.
    """

    def __init__(self, data):
        super().__init__([FeaturedOfferExpectedPriceResponse(datum) for datum in data])
        self.data = data


class CompetitiveSummaryRequestList(list, _List["CompetitiveSummaryRequest"]):
    """
    A batched list of `competitiveSummary` requests.
    """

    def __init__(self, data):
        super().__init__([CompetitiveSummaryRequest(datum) for datum in data])
        self.data = data


class CompetitiveSummaryResponseList(list, _List["CompetitiveSummaryResponse"]):
    """
    The response list of the `competitiveSummaryBatch` operation.
    """

    def __init__(self, data):
        super().__init__([CompetitiveSummaryResponse(datum) for datum in data])
        self.data = data


class FeaturedOfferExpectedPriceResultList(list, _List["FeaturedOfferExpectedPriceResult"]):
    """
    A list of featured offer expected price results for the requested offer.
    """

    def __init__(self, data):
        super().__init__([FeaturedOfferExpectedPriceResult(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class CompetitiveSummaryIncludedData(str):
    """
    The supported types of data in the `getCompetitiveSummary` API.
    """


class HttpUri(str):
    """
    The URI associated with the individual APIs being called as part of the batch request.
    """


class HttpMethod(str):
    """
    The HTTP method associated with an individual request within a batch.
    """


class FulfillmentType(str):
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """


class MarketplaceId(str):
    """
    A marketplace identifier. Specifies the marketplace for which data is returned.
    """


class Sku(str):
    """
    The seller SKU of the item.
    """


class Condition(str):
    """
    The condition of the item.
    """


class Asin(str):
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """


class FeaturedOfferExpectedPriceRequest(
    BatchRequest,
    FeaturedOfferExpectedPriceRequestParams,
):
    """
    An individual featured offer expected price request for a particular SKU.
    """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class FeaturedOfferExpectedPriceResponse(
    BatchResponse,
):
    """ """

    def __init__(self, data):
        if "request" in data:
            self.request: FeaturedOfferExpectedPriceRequestParams = FeaturedOfferExpectedPriceRequestParams(
                data.pop("request")
            )
        else:
            self.request: FeaturedOfferExpectedPriceRequestParams = None
        if "body" in data:
            self.body: FeaturedOfferExpectedPriceResponseBody = FeaturedOfferExpectedPriceResponseBody(data.pop("body"))
        else:
            self.body: FeaturedOfferExpectedPriceResponseBody = None
        self.data = data
        super().__init__(data)


class SegmentedFeaturedOffer(
    Offer,
):
    """
    A product offer with segment information indicating where it's featured.
    """

    def __init__(self, data):
        if "featuredOfferSegments" in data:
            self.featuredOfferSegments = data.pop("featuredOfferSegments")
        else:
            self.featuredOfferSegments = None
        self.data = data
        super().__init__(data)


class ProductPricing20220501Client(__BaseClient):
    def getFeaturedOfferExpectedPriceBatch(
        self,
        data: GetFeaturedOfferExpectedPriceBatchRequest,
    ):
        """
                Returns the set of responses that correspond to the batched list of up to 40 requests defined in the request body. The response for each successful (HTTP status code 200) request in the set includes the computed listing price at or below which a seller can expect to become the featured offer (before applicable promotions). This is called the featured offer expected price (FOEP). Featured offer is not guaranteed, because competing offers may change, and different offers may be featured based on other factors, including fulfillment capabilities to a specific customer. The response to an unsuccessful request includes the available error text.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.033 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetFeaturedOfferExpectedPriceBatchResponse,
            400: Errors,
            401: Errors,
            403: Errors,
            404: Errors,
            429: Errors,
            500: Errors,
            503: Errors,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getCompetitiveSummary(
        self,
        data: CompetitiveSummaryBatchRequest,
    ):
        """
                Returns the competitive summary response including featured buying options for the ASIN and `marketplaceId` combination.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.033 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/batches/products/pricing/2022-05-01/items/competitiveSummary"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CompetitiveSummaryBatchResponse,
            400: Errors,
            403: Errors,
            404: Errors,
            429: Errors,
            500: Errors,
            503: Errors,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
