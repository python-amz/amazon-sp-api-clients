from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetItemOffersBatchRequest(__BaseDictObject):
    """
    The request associated with the `getItemOffersBatch` API call.
    """

    def __init__(self, data):
        super().__init__(data)
        if "requests" in data:
            self.requests: ItemOffersRequestList = self._get_value(ItemOffersRequestList, "requests")
        else:
            self.requests: ItemOffersRequestList = None


class GetListingOffersBatchRequest(__BaseDictObject):
    """
    The request associated with the `getListingOffersBatch` API call.
    """

    def __init__(self, data):
        super().__init__(data)
        if "requests" in data:
            self.requests: ListingOffersRequestList = self._get_value(ListingOffersRequestList, "requests")
        else:
            self.requests: ListingOffersRequestList = None


class BatchOffersRequestParams(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: MarketplaceId = self._get_value(MarketplaceId, "MarketplaceId")
        else:
            self.MarketplaceId: MarketplaceId = None
        if "ItemCondition" in data:
            self.ItemCondition: ItemCondition = self._get_value(ItemCondition, "ItemCondition")
        else:
            self.ItemCondition: ItemCondition = None
        if "CustomerType" in data:
            self.CustomerType: CustomerType = self._get_value(CustomerType, "CustomerType")
        else:
            self.CustomerType: CustomerType = None


class GetItemOffersBatchResponse(__BaseDictObject):
    """
    The response associated with the `getItemOffersBatch` API call.
    """

    def __init__(self, data):
        super().__init__(data)
        if "responses" in data:
            self.responses: ItemOffersResponseList = self._get_value(ItemOffersResponseList, "responses")
        else:
            self.responses: ItemOffersResponseList = None


class GetListingOffersBatchResponse(__BaseDictObject):
    """
    The response associated with the `getListingOffersBatch` API call.
    """

    def __init__(self, data):
        super().__init__(data)
        if "responses" in data:
            self.responses: ListingOffersResponseList = self._get_value(ListingOffersResponseList, "responses")
        else:
            self.responses: ListingOffersResponseList = None


class BatchOffersResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "headers" in data:
            self.headers: HttpResponseHeaders = self._get_value(HttpResponseHeaders, "headers")
        else:
            self.headers: HttpResponseHeaders = None
        if "status" in data:
            self.status: GetOffersHttpStatusLine = self._get_value(GetOffersHttpStatusLine, "status")
        else:
            self.status: GetOffersHttpStatusLine = None
        if "body" in data:
            self.body: GetOffersResponse = self._get_value(GetOffersResponse, "body")
        else:
            self.body: GetOffersResponse = None


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


class GetPricingResponse(__BaseDictObject):
    """
    The response schema for the `getPricing` and `getCompetitivePricing` operations.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: PriceList = self._get_value(PriceList, "payload")
        else:
            self.payload: PriceList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOffersResponse(__BaseDictObject):
    """
    The response schema for the `getListingOffers` and `getItemOffers` operations.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetOffersResult = self._get_value(GetOffersResult, "payload")
        else:
            self.payload: GetOffersResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOffersResult(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceID" in data:
            self.MarketplaceID: str = self._get_value(str, "MarketplaceID")
        else:
            self.MarketplaceID: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "SKU" in data:
            self.SKU: str = self._get_value(str, "SKU")
        else:
            self.SKU: str = None
        if "ItemCondition" in data:
            self.ItemCondition: ConditionType = self._get_value(ConditionType, "ItemCondition")
        else:
            self.ItemCondition: ConditionType = None
        if "status" in data:
            self.status: str = self._get_value(str, "status")
        else:
            self.status: str = None
        if "Identifier" in data:
            self.Identifier: ItemIdentifier = self._get_value(ItemIdentifier, "Identifier")
        else:
            self.Identifier: ItemIdentifier = None
        if "Summary" in data:
            self.Summary: Summary = self._get_value(Summary, "Summary")
        else:
            self.Summary: Summary = None
        if "Offers" in data:
            self.Offers: OfferDetailList = self._get_value(OfferDetailList, "Offers")
        else:
            self.Offers: OfferDetailList = None


class HttpRequestHeaders(__BaseDictObject):
    """
    A mapping of additional HTTP headers to send/receive for the individual batch request.
    """

    def __init__(self, data):
        super().__init__(data)


class HttpResponseHeaders(__BaseDictObject):
    """
    A mapping of additional HTTP headers to send/receive for the individual batch request.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Date" in data:
            self.Date: str = self._get_value(str, "Date")
        else:
            self.Date: str = None


class GetOffersHttpStatusLine(__BaseDictObject):
    """
    The HTTP status line associated with the response.  For more information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
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


class BatchRequest(__BaseDictObject):
    """
    Common properties of batch requests against individual APIs.
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
        if "headers" in data:
            self.headers: HttpRequestHeaders = self._get_value(HttpRequestHeaders, "headers")
        else:
            self.headers: HttpRequestHeaders = None


class Price(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "status" in data:
            self.status: str = self._get_value(str, "status")
        else:
            self.status: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "Product" in data:
            self.Product: Product = self._get_value(Product, "Product")
        else:
            self.Product: Product = None


class Product(__BaseDictObject):
    """
    An item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Identifiers" in data:
            self.Identifiers: IdentifierType = self._get_value(IdentifierType, "Identifiers")
        else:
            self.Identifiers: IdentifierType = None
        if "AttributeSets" in data:
            self.AttributeSets: AttributeSetList = self._get_value(AttributeSetList, "AttributeSets")
        else:
            self.AttributeSets: AttributeSetList = None
        if "Relationships" in data:
            self.Relationships: RelationshipList = self._get_value(RelationshipList, "Relationships")
        else:
            self.Relationships: RelationshipList = None
        if "CompetitivePricing" in data:
            self.CompetitivePricing: CompetitivePricingType = self._get_value(
                CompetitivePricingType, "CompetitivePricing"
            )
        else:
            self.CompetitivePricing: CompetitivePricingType = None
        if "SalesRankings" in data:
            self.SalesRankings: SalesRankList = self._get_value(SalesRankList, "SalesRankings")
        else:
            self.SalesRankings: SalesRankList = None
        if "Offers" in data:
            self.Offers: OffersList = self._get_value(OffersList, "Offers")
        else:
            self.Offers: OffersList = None


class IdentifierType(__BaseDictObject):
    """
    Specifies the identifiers used to uniquely identify an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceASIN" in data:
            self.MarketplaceASIN: ASINIdentifier = self._get_value(ASINIdentifier, "MarketplaceASIN")
        else:
            self.MarketplaceASIN: ASINIdentifier = None
        if "SKUIdentifier" in data:
            self.SKUIdentifier: SellerSKUIdentifier = self._get_value(SellerSKUIdentifier, "SKUIdentifier")
        else:
            self.SKUIdentifier: SellerSKUIdentifier = None


class ASINIdentifier(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None


class SellerSKUIdentifier(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = self._get_value(str, "SellerId")
        else:
            self.SellerId: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None


class CompetitivePricingType(__BaseDictObject):
    """
    Competitive pricing information for the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CompetitivePrices" in data:
            self.CompetitivePrices: CompetitivePriceList = self._get_value(CompetitivePriceList, "CompetitivePrices")
        else:
            self.CompetitivePrices: CompetitivePriceList = None
        if "NumberOfOfferListings" in data:
            self.NumberOfOfferListings: NumberOfOfferListingsList = self._get_value(
                NumberOfOfferListingsList, "NumberOfOfferListings"
            )
        else:
            self.NumberOfOfferListings: NumberOfOfferListingsList = None
        if "TradeInValue" in data:
            self.TradeInValue: MoneyType = self._get_value(MoneyType, "TradeInValue")
        else:
            self.TradeInValue: MoneyType = None


class CompetitivePriceType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "CompetitivePriceId" in data:
            self.CompetitivePriceId: str = self._get_value(str, "CompetitivePriceId")
        else:
            self.CompetitivePriceId: str = None
        if "Price" in data:
            self.Price: PriceType = self._get_value(PriceType, "Price")
        else:
            self.Price: PriceType = None
        if "condition" in data:
            self.condition: str = self._get_value(str, "condition")
        else:
            self.condition: str = None
        if "subcondition" in data:
            self.subcondition: str = self._get_value(str, "subcondition")
        else:
            self.subcondition: str = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = self._get_value(OfferCustomerType, "offerType")
        else:
            self.offerType: OfferCustomerType = None
        if "quantityTier" in data:
            self.quantityTier: int = self._get_value(int, "quantityTier")
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = self._get_value(
                QuantityDiscountType, "quantityDiscountType"
            )
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "sellerId" in data:
            self.sellerId: str = self._get_value(str, "sellerId")
        else:
            self.sellerId: str = None
        if "belongsToRequester" in data:
            self.belongsToRequester: bool = self._get_value(convert_bool, "belongsToRequester")
        else:
            self.belongsToRequester: bool = None


class OfferListingCountType(__BaseDictObject):
    """
    The number of offer listings with the specified condition.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Count" in data:
            self.Count: int = self._get_value(int, "Count")
        else:
            self.Count: int = None
        if "condition" in data:
            self.condition: str = self._get_value(str, "condition")
        else:
            self.condition: str = None


class MoneyType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: float = self._get_value(float, "Amount")
        else:
            self.Amount: float = None


class SalesRankType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "ProductCategoryId" in data:
            self.ProductCategoryId: str = self._get_value(str, "ProductCategoryId")
        else:
            self.ProductCategoryId: str = None
        if "Rank" in data:
            self.Rank: int = self._get_value(int, "Rank")
        else:
            self.Rank: int = None


class PriceType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "LandedPrice" in data:
            self.LandedPrice: MoneyType = self._get_value(MoneyType, "LandedPrice")
        else:
            self.LandedPrice: MoneyType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = self._get_value(MoneyType, "ListingPrice")
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = self._get_value(MoneyType, "Shipping")
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = self._get_value(Points, "Points")
        else:
            self.Points: Points = None


class OfferType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "offerType" in data:
            self.offerType: OfferCustomerType = self._get_value(OfferCustomerType, "offerType")
        else:
            self.offerType: OfferCustomerType = None
        if "BuyingPrice" in data:
            self.BuyingPrice: PriceType = self._get_value(PriceType, "BuyingPrice")
        else:
            self.BuyingPrice: PriceType = None
        if "RegularPrice" in data:
            self.RegularPrice: MoneyType = self._get_value(MoneyType, "RegularPrice")
        else:
            self.RegularPrice: MoneyType = None
        if "businessPrice" in data:
            self.businessPrice: MoneyType = self._get_value(MoneyType, "businessPrice")
        else:
            self.businessPrice: MoneyType = None
        if "quantityDiscountPrices" in data:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = [
                QuantityDiscountPriceType(datum) for datum in data["quantityDiscountPrices"]
            ]
        else:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = []
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = self._get_value(str, "FulfillmentChannel")
        else:
            self.FulfillmentChannel: str = None
        if "ItemCondition" in data:
            self.ItemCondition: str = self._get_value(str, "ItemCondition")
        else:
            self.ItemCondition: str = None
        if "ItemSubCondition" in data:
            self.ItemSubCondition: str = self._get_value(str, "ItemSubCondition")
        else:
            self.ItemSubCondition: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None


class QuantityDiscountPriceType(__BaseDictObject):
    """
    Contains pricing information that includes special pricing when buying in bulk.
    """

    def __init__(self, data):
        super().__init__(data)
        if "quantityTier" in data:
            self.quantityTier: int = self._get_value(int, "quantityTier")
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = self._get_value(
                QuantityDiscountType, "quantityDiscountType"
            )
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "listingPrice" in data:
            self.listingPrice: MoneyType = self._get_value(MoneyType, "listingPrice")
        else:
            self.listingPrice: MoneyType = None


class Points(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "PointsNumber" in data:
            self.PointsNumber: int = self._get_value(int, "PointsNumber")
        else:
            self.PointsNumber: int = None
        if "PointsMonetaryValue" in data:
            self.PointsMonetaryValue: MoneyType = self._get_value(MoneyType, "PointsMonetaryValue")
        else:
            self.PointsMonetaryValue: MoneyType = None


class ItemIdentifier(__BaseDictObject):
    """
    Information that identifies an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "ItemCondition" in data:
            self.ItemCondition: ConditionType = self._get_value(ConditionType, "ItemCondition")
        else:
            self.ItemCondition: ConditionType = None


class Summary(__BaseDictObject):
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """

    def __init__(self, data):
        super().__init__(data)
        if "TotalOfferCount" in data:
            self.TotalOfferCount: int = self._get_value(int, "TotalOfferCount")
        else:
            self.TotalOfferCount: int = None
        if "NumberOfOffers" in data:
            self.NumberOfOffers: NumberOfOffers = self._get_value(NumberOfOffers, "NumberOfOffers")
        else:
            self.NumberOfOffers: NumberOfOffers = None
        if "LowestPrices" in data:
            self.LowestPrices: LowestPrices = self._get_value(LowestPrices, "LowestPrices")
        else:
            self.LowestPrices: LowestPrices = None
        if "BuyBoxPrices" in data:
            self.BuyBoxPrices: BuyBoxPrices = self._get_value(BuyBoxPrices, "BuyBoxPrices")
        else:
            self.BuyBoxPrices: BuyBoxPrices = None
        if "ListPrice" in data:
            self.ListPrice: MoneyType = self._get_value(MoneyType, "ListPrice")
        else:
            self.ListPrice: MoneyType = None
        if "CompetitivePriceThreshold" in data:
            self.CompetitivePriceThreshold: MoneyType = self._get_value(MoneyType, "CompetitivePriceThreshold")
        else:
            self.CompetitivePriceThreshold: MoneyType = None
        if "SuggestedLowerPricePlusShipping" in data:
            self.SuggestedLowerPricePlusShipping: MoneyType = self._get_value(
                MoneyType, "SuggestedLowerPricePlusShipping"
            )
        else:
            self.SuggestedLowerPricePlusShipping: MoneyType = None
        if "SalesRankings" in data:
            self.SalesRankings: SalesRankList = self._get_value(SalesRankList, "SalesRankings")
        else:
            self.SalesRankings: SalesRankList = None
        if "BuyBoxEligibleOffers" in data:
            self.BuyBoxEligibleOffers: BuyBoxEligibleOffers = self._get_value(
                BuyBoxEligibleOffers, "BuyBoxEligibleOffers"
            )
        else:
            self.BuyBoxEligibleOffers: BuyBoxEligibleOffers = None
        if "OffersAvailableTime" in data:
            self.OffersAvailableTime: str = self._get_value(str, "OffersAvailableTime")
        else:
            self.OffersAvailableTime: str = None


class OfferCountType(__BaseDictObject):
    """
    The total number of offers for the specified condition and fulfillment channel.
    """

    def __init__(self, data):
        super().__init__(data)
        if "condition" in data:
            self.condition: str = self._get_value(str, "condition")
        else:
            self.condition: str = None
        if "fulfillmentChannel" in data:
            self.fulfillmentChannel: FulfillmentChannelType = self._get_value(
                FulfillmentChannelType, "fulfillmentChannel"
            )
        else:
            self.fulfillmentChannel: FulfillmentChannelType = None
        if "OfferCount" in data:
            self.OfferCount: int = self._get_value(int, "OfferCount")
        else:
            self.OfferCount: int = None


class LowestPriceType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "condition" in data:
            self.condition: str = self._get_value(str, "condition")
        else:
            self.condition: str = None
        if "fulfillmentChannel" in data:
            self.fulfillmentChannel: str = self._get_value(str, "fulfillmentChannel")
        else:
            self.fulfillmentChannel: str = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = self._get_value(OfferCustomerType, "offerType")
        else:
            self.offerType: OfferCustomerType = None
        if "quantityTier" in data:
            self.quantityTier: int = self._get_value(int, "quantityTier")
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = self._get_value(
                QuantityDiscountType, "quantityDiscountType"
            )
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "LandedPrice" in data:
            self.LandedPrice: MoneyType = self._get_value(MoneyType, "LandedPrice")
        else:
            self.LandedPrice: MoneyType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = self._get_value(MoneyType, "ListingPrice")
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = self._get_value(MoneyType, "Shipping")
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = self._get_value(Points, "Points")
        else:
            self.Points: Points = None


class BuyBoxPriceType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "condition" in data:
            self.condition: str = self._get_value(str, "condition")
        else:
            self.condition: str = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = self._get_value(OfferCustomerType, "offerType")
        else:
            self.offerType: OfferCustomerType = None
        if "quantityTier" in data:
            self.quantityTier: int = self._get_value(int, "quantityTier")
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = self._get_value(
                QuantityDiscountType, "quantityDiscountType"
            )
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "LandedPrice" in data:
            self.LandedPrice: MoneyType = self._get_value(MoneyType, "LandedPrice")
        else:
            self.LandedPrice: MoneyType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = self._get_value(MoneyType, "ListingPrice")
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = self._get_value(MoneyType, "Shipping")
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = self._get_value(Points, "Points")
        else:
            self.Points: Points = None
        if "sellerId" in data:
            self.sellerId: str = self._get_value(str, "sellerId")
        else:
            self.sellerId: str = None


class OfferDetail(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MyOffer" in data:
            self.MyOffer: bool = self._get_value(convert_bool, "MyOffer")
        else:
            self.MyOffer: bool = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = self._get_value(OfferCustomerType, "offerType")
        else:
            self.offerType: OfferCustomerType = None
        if "SubCondition" in data:
            self.SubCondition: str = self._get_value(str, "SubCondition")
        else:
            self.SubCondition: str = None
        if "SellerId" in data:
            self.SellerId: str = self._get_value(str, "SellerId")
        else:
            self.SellerId: str = None
        if "ConditionNotes" in data:
            self.ConditionNotes: str = self._get_value(str, "ConditionNotes")
        else:
            self.ConditionNotes: str = None
        if "SellerFeedbackRating" in data:
            self.SellerFeedbackRating: SellerFeedbackType = self._get_value(SellerFeedbackType, "SellerFeedbackRating")
        else:
            self.SellerFeedbackRating: SellerFeedbackType = None
        if "ShippingTime" in data:
            self.ShippingTime: DetailedShippingTimeType = self._get_value(DetailedShippingTimeType, "ShippingTime")
        else:
            self.ShippingTime: DetailedShippingTimeType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = self._get_value(MoneyType, "ListingPrice")
        else:
            self.ListingPrice: MoneyType = None
        if "quantityDiscountPrices" in data:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = [
                QuantityDiscountPriceType(datum) for datum in data["quantityDiscountPrices"]
            ]
        else:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = []
        if "Points" in data:
            self.Points: Points = self._get_value(Points, "Points")
        else:
            self.Points: Points = None
        if "Shipping" in data:
            self.Shipping: MoneyType = self._get_value(MoneyType, "Shipping")
        else:
            self.Shipping: MoneyType = None
        if "ShipsFrom" in data:
            self.ShipsFrom: ShipsFromType = self._get_value(ShipsFromType, "ShipsFrom")
        else:
            self.ShipsFrom: ShipsFromType = None
        if "IsFulfilledByAmazon" in data:
            self.IsFulfilledByAmazon: bool = self._get_value(convert_bool, "IsFulfilledByAmazon")
        else:
            self.IsFulfilledByAmazon: bool = None
        if "PrimeInformation" in data:
            self.PrimeInformation: PrimeInformationType = self._get_value(PrimeInformationType, "PrimeInformation")
        else:
            self.PrimeInformation: PrimeInformationType = None
        if "IsBuyBoxWinner" in data:
            self.IsBuyBoxWinner: bool = self._get_value(convert_bool, "IsBuyBoxWinner")
        else:
            self.IsBuyBoxWinner: bool = None
        if "IsFeaturedMerchant" in data:
            self.IsFeaturedMerchant: bool = self._get_value(convert_bool, "IsFeaturedMerchant")
        else:
            self.IsFeaturedMerchant: bool = None


class PrimeInformationType(__BaseDictObject):
    """
    Amazon Prime information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "IsPrime" in data:
            self.IsPrime: bool = self._get_value(convert_bool, "IsPrime")
        else:
            self.IsPrime: bool = None
        if "IsNationalPrime" in data:
            self.IsNationalPrime: bool = self._get_value(convert_bool, "IsNationalPrime")
        else:
            self.IsNationalPrime: bool = None


class SellerFeedbackType(__BaseDictObject):
    """
    Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.
    """

    def __init__(self, data):
        super().__init__(data)
        if "SellerPositiveFeedbackRating" in data:
            self.SellerPositiveFeedbackRating: float = self._get_value(float, "SellerPositiveFeedbackRating")
        else:
            self.SellerPositiveFeedbackRating: float = None
        if "FeedbackCount" in data:
            self.FeedbackCount: int = self._get_value(int, "FeedbackCount")
        else:
            self.FeedbackCount: int = None


class DetailedShippingTimeType(__BaseDictObject):
    """
    The time range in which an item will likely be shipped once an order has been placed.
    """

    def __init__(self, data):
        super().__init__(data)
        if "minimumHours" in data:
            self.minimumHours: int = self._get_value(int, "minimumHours")
        else:
            self.minimumHours: int = None
        if "maximumHours" in data:
            self.maximumHours: int = self._get_value(int, "maximumHours")
        else:
            self.maximumHours: int = None
        if "availableDate" in data:
            self.availableDate: str = self._get_value(str, "availableDate")
        else:
            self.availableDate: str = None
        if "availabilityType" in data:
            self.availabilityType: str = self._get_value(str, "availabilityType")
        else:
            self.availabilityType: str = None


class ShipsFromType(__BaseDictObject):
    """
    The state and country from where the item is shipped.
    """

    def __init__(self, data):
        super().__init__(data)
        if "State" in data:
            self.State: str = self._get_value(str, "State")
        else:
            self.State: str = None
        if "Country" in data:
            self.Country: str = self._get_value(str, "Country")
        else:
            self.Country: str = None


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


class ListingOffersRequestList(list, _List["ListingOffersRequest"]):
    """
    A list of `getListingOffers` batched requests to run.
    """

    def __init__(self, data):
        super().__init__([ListingOffersRequest(datum) for datum in data])
        self.data = data


class ItemOffersRequestList(list, _List["ItemOffersRequest"]):
    """
    A list of `getListingOffers` batched requests to run.
    """

    def __init__(self, data):
        super().__init__([ItemOffersRequest(datum) for datum in data])
        self.data = data


class ItemOffersResponseList(list, _List["ItemOffersResponse"]):
    """
    A list of `getItemOffers` batched responses.
    """

    def __init__(self, data):
        super().__init__([ItemOffersResponse(datum) for datum in data])
        self.data = data


class ListingOffersResponseList(list, _List["ListingOffersResponse"]):
    """
    A list of `getListingOffers` batched responses.
    """

    def __init__(self, data):
        super().__init__([ListingOffersResponse(datum) for datum in data])
        self.data = data


class PriceList(list, _List["Price"]):
    """ """

    def __init__(self, data):
        super().__init__([Price(datum) for datum in data])
        self.data = data


class AttributeSetList(list, _List["dict"]):
    """
    A list of product attributes if they are applicable to the product that is returned.
    """

    def __init__(self, data):
        super().__init__([dict(datum) for datum in data])
        self.data = data


class RelationshipList(list, _List["dict"]):
    """
    A list that contains product variation information, if applicable.
    """

    def __init__(self, data):
        super().__init__([dict(datum) for datum in data])
        self.data = data


class CompetitivePriceList(list, _List["CompetitivePriceType"]):
    """
    A list of competitive pricing information.
    """

    def __init__(self, data):
        super().__init__([CompetitivePriceType(datum) for datum in data])
        self.data = data


class NumberOfOfferListingsList(list, _List["OfferListingCountType"]):
    """
    The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned.
    """

    def __init__(self, data):
        super().__init__([OfferListingCountType(datum) for datum in data])
        self.data = data


class SalesRankList(list, _List["SalesRankType"]):
    """
    A list of sales rank information for the item, by category.
    """

    def __init__(self, data):
        super().__init__([SalesRankType(datum) for datum in data])
        self.data = data


class OffersList(list, _List["OfferType"]):
    """
    A list of offers.
    """

    def __init__(self, data):
        super().__init__([OfferType(datum) for datum in data])
        self.data = data


class BuyBoxEligibleOffers(list, _List["OfferCountType"]):
    """ """

    def __init__(self, data):
        super().__init__([OfferCountType(datum) for datum in data])
        self.data = data


class BuyBoxPrices(list, _List["BuyBoxPriceType"]):
    """ """

    def __init__(self, data):
        super().__init__([BuyBoxPriceType(datum) for datum in data])
        self.data = data


class LowestPrices(list, _List["LowestPriceType"]):
    """ """

    def __init__(self, data):
        super().__init__([LowestPriceType(datum) for datum in data])
        self.data = data


class NumberOfOffers(list, _List["OfferCountType"]):
    """ """

    def __init__(self, data):
        super().__init__([OfferCountType(datum) for datum in data])
        self.data = data


class OfferDetailList(list, _List["OfferDetail"]):
    """ """

    def __init__(self, data):
        super().__init__([OfferDetail(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class HttpUri(str):
    """
    The URI associated with the individual APIs being called as part of the batch request.
    """


class HttpMethod(str):
    """
    The HTTP method associated with the individual APIs being called as part of the batch request.
    """


class OfferCustomerType(str):
    """ """


class QuantityDiscountType(str):
    """ """


class ConditionType(str):
    """
    Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club.
    """


class FulfillmentChannelType(str):
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """


class MarketplaceId(str):
    """
    A marketplace identifier. Specifies the marketplace for which prices are returned.
    """


class ItemCondition(str):
    """
    Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
    """


class Asin(str):
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """


class CustomerType(str):
    """
    Indicates whether to request Consumer or Business offers. Default is Consumer.
    """


class ItemOffersRequest(
    BatchRequest,
    BatchOffersRequestParams,
):
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class ListingOffersRequest(
    BatchRequest,
    BatchOffersRequestParams,
):
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class ItemOffersRequestParams(
    BatchOffersRequestParams,
):
    """ """

    def __init__(self, data):
        if "Asin" in data:
            self.Asin = data.pop("Asin")
        else:
            self.Asin = None
        self.data = data
        super().__init__(data)


class ItemOffersResponse(
    BatchOffersResponse,
):
    """ """

    def __init__(self, data):
        if "request" in data:
            self.request: ItemOffersRequestParams = ItemOffersRequestParams(data.pop("request"))
        else:
            self.request: ItemOffersRequestParams = None
        self.data = data
        super().__init__(data)


class ListingOffersRequestParams(
    BatchOffersRequestParams,
):
    """ """

    def __init__(self, data):
        if "SellerSKU" in data:
            self.SellerSKU = data.pop("SellerSKU")
        else:
            self.SellerSKU = None
        self.data = data
        super().__init__(data)


class ListingOffersResponse(
    BatchOffersResponse,
):
    """ """

    def __init__(self, data):
        if "request" in data:
            self.request: ListingOffersRequestParams = ListingOffersRequestParams(data.pop("request"))
        else:
            self.request: ListingOffersRequestParams = None
        self.data = data
        super().__init__(data)


class ProductPricingV0Client(__BaseClient):
    def getPricing(
        self,
        MarketplaceId: str,
        ItemType: str,
        Asins: _List[str] = None,
        Skus: _List[str] = None,
        ItemCondition: str = None,
        OfferType: str = None,
    ):
        """
                Returns pricing information for a seller's offer listings based on seller SKU or ASIN.
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/products/pricing/v0/price"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if Asins is not None:
            params["Asins"] = ",".join(map(str, Asins))
        if Skus is not None:
            params["Skus"] = ",".join(map(str, Skus))
        if ItemType is not None:
            params["ItemType"] = ItemType
        if ItemCondition is not None:
            params["ItemCondition"] = ItemCondition
        if OfferType is not None:
            params["OfferType"] = OfferType
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetPricingResponse,
            400: GetPricingResponse,
            401: GetPricingResponse,
            403: GetPricingResponse,
            404: GetPricingResponse,
            429: GetPricingResponse,
            500: GetPricingResponse,
            503: GetPricingResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getCompetitivePricing(
        self,
        MarketplaceId: str,
        ItemType: str,
        Asins: _List[str] = None,
        Skus: _List[str] = None,
        CustomerType: str = None,
    ):
        """
                Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/products/pricing/v0/competitivePrice"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if Asins is not None:
            params["Asins"] = ",".join(map(str, Asins))
        if Skus is not None:
            params["Skus"] = ",".join(map(str, Skus))
        if ItemType is not None:
            params["ItemType"] = ItemType
        if CustomerType is not None:
            params["CustomerType"] = CustomerType
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetPricingResponse,
            400: GetPricingResponse,
            401: GetPricingResponse,
            403: GetPricingResponse,
            404: GetPricingResponse,
            429: GetPricingResponse,
            500: GetPricingResponse,
            503: GetPricingResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getListingOffers(
        self,
        SellerSKU: str,
        MarketplaceId: str,
        ItemCondition: str,
        CustomerType: str = None,
    ):
        """
                Returns the lowest priced offers for a single SKU listing.
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 2 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/products/pricing/v0/listings/{SellerSKU}/offers"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if ItemCondition is not None:
            params["ItemCondition"] = ItemCondition
        if CustomerType is not None:
            params["CustomerType"] = CustomerType
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOffersResponse,
            400: GetOffersResponse,
            401: GetOffersResponse,
            403: GetOffersResponse,
            404: GetOffersResponse,
            429: GetOffersResponse,
            500: GetOffersResponse,
            503: GetOffersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getItemOffers(
        self,
        Asin: str,
        MarketplaceId: str,
        ItemCondition: str,
        CustomerType: str = None,
    ):
        """
                Returns the lowest priced offers for a single item based on ASIN.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/products/pricing/v0/items/{Asin}/offers"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if ItemCondition is not None:
            params["ItemCondition"] = ItemCondition
        if CustomerType is not None:
            params["CustomerType"] = CustomerType
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOffersResponse,
            400: GetOffersResponse,
            401: GetOffersResponse,
            403: GetOffersResponse,
            404: GetOffersResponse,
            429: GetOffersResponse,
            500: GetOffersResponse,
            503: GetOffersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getItemOffersBatch(
        self,
        data: GetItemOffersBatchRequest,
    ):
        """
                Returns the lowest priced offers for a batch of items based on ASIN.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.1 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/batches/products/pricing/v0/itemOffers"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetItemOffersBatchResponse,
            400: Errors,
            401: Errors,
            403: Errors,
            404: Errors,
            429: Errors,
            500: Errors,
            503: Errors,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getListingOffersBatch(
        self,
        data: GetListingOffersBatchRequest,
    ):
        """
                Returns the lowest priced offers for a batch of listings by SKU.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/batches/products/pricing/v0/listingOffers"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetListingOffersBatchResponse,
            400: Errors,
            401: Errors,
            403: Errors,
            404: Errors,
            429: Errors,
            500: Errors,
            503: Errors,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
