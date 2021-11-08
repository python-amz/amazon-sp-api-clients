from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class GetPricingResponse:
    """
    The response schema for the getPricing and getCompetitivePricing operations.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: PriceList = PriceList(data["payload"])
        else:
            self.payload: PriceList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetOffersResponse:
    """
    The response schema for the getListingOffers and getItemOffers operations.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetOffersResult = GetOffersResult(data["payload"])
        else:
            self.payload: GetOffersResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetOffersResult:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceID" in data:
            self.MarketplaceID: str = str(data["MarketplaceID"])
        else:
            self.MarketplaceID: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "SKU" in data:
            self.SKU: str = str(data["SKU"])
        else:
            self.SKU: str = None
        if "ItemCondition" in data:
            self.ItemCondition: ConditionType = ConditionType(data["ItemCondition"])
        else:
            self.ItemCondition: ConditionType = None
        if "status" in data:
            self.status: str = str(data["status"])
        else:
            self.status: str = None
        if "Identifier" in data:
            self.Identifier: ItemIdentifier = ItemIdentifier(data["Identifier"])
        else:
            self.Identifier: ItemIdentifier = None
        if "Summary" in data:
            self.Summary: Summary = Summary(data["Summary"])
        else:
            self.Summary: Summary = None
        if "Offers" in data:
            self.Offers: OfferDetailList = OfferDetailList(data["Offers"])
        else:
            self.Offers: OfferDetailList = None


class Price:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "status" in data:
            self.status: str = str(data["status"])
        else:
            self.status: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "Product" in data:
            self.Product: Product = Product(data["Product"])
        else:
            self.Product: Product = None


class Product:
    """
    An item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Identifiers" in data:
            self.Identifiers: IdentifierType = IdentifierType(data["Identifiers"])
        else:
            self.Identifiers: IdentifierType = None
        if "AttributeSets" in data:
            self.AttributeSets: AttributeSetList = AttributeSetList(data["AttributeSets"])
        else:
            self.AttributeSets: AttributeSetList = None
        if "Relationships" in data:
            self.Relationships: RelationshipList = RelationshipList(data["Relationships"])
        else:
            self.Relationships: RelationshipList = None
        if "CompetitivePricing" in data:
            self.CompetitivePricing: CompetitivePricingType = CompetitivePricingType(data["CompetitivePricing"])
        else:
            self.CompetitivePricing: CompetitivePricingType = None
        if "SalesRankings" in data:
            self.SalesRankings: SalesRankList = SalesRankList(data["SalesRankings"])
        else:
            self.SalesRankings: SalesRankList = None
        if "Offers" in data:
            self.Offers: OffersList = OffersList(data["Offers"])
        else:
            self.Offers: OffersList = None


class IdentifierType:
    """
    Specifies the identifiers used to uniquely identify an item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceASIN" in data:
            self.MarketplaceASIN: ASINIdentifier = ASINIdentifier(data["MarketplaceASIN"])
        else:
            self.MarketplaceASIN: ASINIdentifier = None
        if "SKUIdentifier" in data:
            self.SKUIdentifier: SellerSKUIdentifier = SellerSKUIdentifier(data["SKUIdentifier"])
        else:
            self.SKUIdentifier: SellerSKUIdentifier = None


class ASINIdentifier:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None


class SellerSKUIdentifier:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None


class CompetitivePricingType:
    """
    Competitive pricing information for the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CompetitivePrices" in data:
            self.CompetitivePrices: CompetitivePriceList = CompetitivePriceList(data["CompetitivePrices"])
        else:
            self.CompetitivePrices: CompetitivePriceList = None
        if "NumberOfOfferListings" in data:
            self.NumberOfOfferListings: NumberOfOfferListingsList = NumberOfOfferListingsList(
                data["NumberOfOfferListings"]
            )
        else:
            self.NumberOfOfferListings: NumberOfOfferListingsList = None
        if "TradeInValue" in data:
            self.TradeInValue: MoneyType = MoneyType(data["TradeInValue"])
        else:
            self.TradeInValue: MoneyType = None


class CompetitivePriceType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CompetitivePriceId" in data:
            self.CompetitivePriceId: str = str(data["CompetitivePriceId"])
        else:
            self.CompetitivePriceId: str = None
        if "Price" in data:
            self.Price: PriceType = PriceType(data["Price"])
        else:
            self.Price: PriceType = None
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None
        if "subcondition" in data:
            self.subcondition: str = str(data["subcondition"])
        else:
            self.subcondition: str = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = OfferCustomerType(data["offerType"])
        else:
            self.offerType: OfferCustomerType = None
        if "quantityTier" in data:
            self.quantityTier: int = int(data["quantityTier"])
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = QuantityDiscountType(data["quantityDiscountType"])
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "sellerId" in data:
            self.sellerId: str = str(data["sellerId"])
        else:
            self.sellerId: str = None
        if "belongsToRequester" in data:
            self.belongsToRequester: bool = convert_bool(data["belongsToRequester"])
        else:
            self.belongsToRequester: bool = None


class OfferListingCountType:
    """
    The number of offer listings with the specified condition.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Count" in data:
            self.Count: int = int(data["Count"])
        else:
            self.Count: int = None
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None


class MoneyType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: float = float(data["Amount"])
        else:
            self.Amount: float = None


class SalesRankType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ProductCategoryId" in data:
            self.ProductCategoryId: str = str(data["ProductCategoryId"])
        else:
            self.ProductCategoryId: str = None
        if "Rank" in data:
            self.Rank: int = int(data["Rank"])
        else:
            self.Rank: int = None


class PriceType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "LandedPrice" in data:
            self.LandedPrice: MoneyType = MoneyType(data["LandedPrice"])
        else:
            self.LandedPrice: MoneyType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = MoneyType(data["ListingPrice"])
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = MoneyType(data["Shipping"])
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = Points(data["Points"])
        else:
            self.Points: Points = None


class OfferType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "offerType" in data:
            self.offerType: OfferCustomerType = OfferCustomerType(data["offerType"])
        else:
            self.offerType: OfferCustomerType = None
        if "BuyingPrice" in data:
            self.BuyingPrice: PriceType = PriceType(data["BuyingPrice"])
        else:
            self.BuyingPrice: PriceType = None
        if "RegularPrice" in data:
            self.RegularPrice: MoneyType = MoneyType(data["RegularPrice"])
        else:
            self.RegularPrice: MoneyType = None
        if "businessPrice" in data:
            self.businessPrice: MoneyType = MoneyType(data["businessPrice"])
        else:
            self.businessPrice: MoneyType = None
        if "quantityDiscountPrices" in data:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = [
                QuantityDiscountPriceType(datum) for datum in data["quantityDiscountPrices"]
            ]
        else:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = []
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = str(data["FulfillmentChannel"])
        else:
            self.FulfillmentChannel: str = None
        if "ItemCondition" in data:
            self.ItemCondition: str = str(data["ItemCondition"])
        else:
            self.ItemCondition: str = None
        if "ItemSubCondition" in data:
            self.ItemSubCondition: str = str(data["ItemSubCondition"])
        else:
            self.ItemSubCondition: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None


class QuantityDiscountPriceType:
    """
    Contains pricing information that includes special pricing when buying in bulk.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "quantityTier" in data:
            self.quantityTier: int = int(data["quantityTier"])
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = QuantityDiscountType(data["quantityDiscountType"])
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "listingPrice" in data:
            self.listingPrice: MoneyType = MoneyType(data["listingPrice"])
        else:
            self.listingPrice: MoneyType = None


class Points:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PointsNumber" in data:
            self.PointsNumber: int = int(data["PointsNumber"])
        else:
            self.PointsNumber: int = None
        if "PointsMonetaryValue" in data:
            self.PointsMonetaryValue: MoneyType = MoneyType(data["PointsMonetaryValue"])
        else:
            self.PointsMonetaryValue: MoneyType = None


class ItemIdentifier:
    """
    Information that identifies an item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "ItemCondition" in data:
            self.ItemCondition: ConditionType = ConditionType(data["ItemCondition"])
        else:
            self.ItemCondition: ConditionType = None


class Summary:
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TotalOfferCount" in data:
            self.TotalOfferCount: int = int(data["TotalOfferCount"])
        else:
            self.TotalOfferCount: int = None
        if "NumberOfOffers" in data:
            self.NumberOfOffers: NumberOfOffers = NumberOfOffers(data["NumberOfOffers"])
        else:
            self.NumberOfOffers: NumberOfOffers = None
        if "LowestPrices" in data:
            self.LowestPrices: LowestPrices = LowestPrices(data["LowestPrices"])
        else:
            self.LowestPrices: LowestPrices = None
        if "BuyBoxPrices" in data:
            self.BuyBoxPrices: BuyBoxPrices = BuyBoxPrices(data["BuyBoxPrices"])
        else:
            self.BuyBoxPrices: BuyBoxPrices = None
        if "ListPrice" in data:
            self.ListPrice: MoneyType = MoneyType(data["ListPrice"])
        else:
            self.ListPrice: MoneyType = None
        if "CompetitivePriceThreshold" in data:
            self.CompetitivePriceThreshold: MoneyType = MoneyType(data["CompetitivePriceThreshold"])
        else:
            self.CompetitivePriceThreshold: MoneyType = None
        if "SuggestedLowerPricePlusShipping" in data:
            self.SuggestedLowerPricePlusShipping: MoneyType = MoneyType(data["SuggestedLowerPricePlusShipping"])
        else:
            self.SuggestedLowerPricePlusShipping: MoneyType = None
        if "SalesRankings" in data:
            self.SalesRankings: SalesRankList = SalesRankList(data["SalesRankings"])
        else:
            self.SalesRankings: SalesRankList = None
        if "BuyBoxEligibleOffers" in data:
            self.BuyBoxEligibleOffers: BuyBoxEligibleOffers = BuyBoxEligibleOffers(data["BuyBoxEligibleOffers"])
        else:
            self.BuyBoxEligibleOffers: BuyBoxEligibleOffers = None
        if "OffersAvailableTime" in data:
            self.OffersAvailableTime: str = str(data["OffersAvailableTime"])
        else:
            self.OffersAvailableTime: str = None


class OfferCountType:
    """
    The total number of offers for the specified condition and fulfillment channel.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None
        if "fulfillmentChannel" in data:
            self.fulfillmentChannel: FulfillmentChannelType = FulfillmentChannelType(data["fulfillmentChannel"])
        else:
            self.fulfillmentChannel: FulfillmentChannelType = None
        if "OfferCount" in data:
            self.OfferCount: int = int(data["OfferCount"])
        else:
            self.OfferCount: int = None


class LowestPriceType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None
        if "fulfillmentChannel" in data:
            self.fulfillmentChannel: str = str(data["fulfillmentChannel"])
        else:
            self.fulfillmentChannel: str = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = OfferCustomerType(data["offerType"])
        else:
            self.offerType: OfferCustomerType = None
        if "quantityTier" in data:
            self.quantityTier: int = int(data["quantityTier"])
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = QuantityDiscountType(data["quantityDiscountType"])
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "LandedPrice" in data:
            self.LandedPrice: MoneyType = MoneyType(data["LandedPrice"])
        else:
            self.LandedPrice: MoneyType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = MoneyType(data["ListingPrice"])
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = MoneyType(data["Shipping"])
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = Points(data["Points"])
        else:
            self.Points: Points = None


class BuyBoxPriceType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = OfferCustomerType(data["offerType"])
        else:
            self.offerType: OfferCustomerType = None
        if "quantityTier" in data:
            self.quantityTier: int = int(data["quantityTier"])
        else:
            self.quantityTier: int = None
        if "quantityDiscountType" in data:
            self.quantityDiscountType: QuantityDiscountType = QuantityDiscountType(data["quantityDiscountType"])
        else:
            self.quantityDiscountType: QuantityDiscountType = None
        if "LandedPrice" in data:
            self.LandedPrice: MoneyType = MoneyType(data["LandedPrice"])
        else:
            self.LandedPrice: MoneyType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = MoneyType(data["ListingPrice"])
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = MoneyType(data["Shipping"])
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = Points(data["Points"])
        else:
            self.Points: Points = None
        if "sellerId" in data:
            self.sellerId: str = str(data["sellerId"])
        else:
            self.sellerId: str = None


class OfferDetail:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MyOffer" in data:
            self.MyOffer: bool = convert_bool(data["MyOffer"])
        else:
            self.MyOffer: bool = None
        if "offerType" in data:
            self.offerType: OfferCustomerType = OfferCustomerType(data["offerType"])
        else:
            self.offerType: OfferCustomerType = None
        if "SubCondition" in data:
            self.SubCondition: str = str(data["SubCondition"])
        else:
            self.SubCondition: str = None
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "ConditionNotes" in data:
            self.ConditionNotes: str = str(data["ConditionNotes"])
        else:
            self.ConditionNotes: str = None
        if "SellerFeedbackRating" in data:
            self.SellerFeedbackRating: SellerFeedbackType = SellerFeedbackType(data["SellerFeedbackRating"])
        else:
            self.SellerFeedbackRating: SellerFeedbackType = None
        if "ShippingTime" in data:
            self.ShippingTime: DetailedShippingTimeType = DetailedShippingTimeType(data["ShippingTime"])
        else:
            self.ShippingTime: DetailedShippingTimeType = None
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = MoneyType(data["ListingPrice"])
        else:
            self.ListingPrice: MoneyType = None
        if "quantityDiscountPrices" in data:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = [
                QuantityDiscountPriceType(datum) for datum in data["quantityDiscountPrices"]
            ]
        else:
            self.quantityDiscountPrices: _List[QuantityDiscountPriceType] = []
        if "Points" in data:
            self.Points: Points = Points(data["Points"])
        else:
            self.Points: Points = None
        if "Shipping" in data:
            self.Shipping: MoneyType = MoneyType(data["Shipping"])
        else:
            self.Shipping: MoneyType = None
        if "ShipsFrom" in data:
            self.ShipsFrom: ShipsFromType = ShipsFromType(data["ShipsFrom"])
        else:
            self.ShipsFrom: ShipsFromType = None
        if "IsFulfilledByAmazon" in data:
            self.IsFulfilledByAmazon: bool = convert_bool(data["IsFulfilledByAmazon"])
        else:
            self.IsFulfilledByAmazon: bool = None
        if "PrimeInformation" in data:
            self.PrimeInformation: PrimeInformationType = PrimeInformationType(data["PrimeInformation"])
        else:
            self.PrimeInformation: PrimeInformationType = None
        if "IsBuyBoxWinner" in data:
            self.IsBuyBoxWinner: bool = convert_bool(data["IsBuyBoxWinner"])
        else:
            self.IsBuyBoxWinner: bool = None
        if "IsFeaturedMerchant" in data:
            self.IsFeaturedMerchant: bool = convert_bool(data["IsFeaturedMerchant"])
        else:
            self.IsFeaturedMerchant: bool = None


class PrimeInformationType:
    """
    Amazon Prime information.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IsPrime" in data:
            self.IsPrime: bool = convert_bool(data["IsPrime"])
        else:
            self.IsPrime: bool = None
        if "IsNationalPrime" in data:
            self.IsNationalPrime: bool = convert_bool(data["IsNationalPrime"])
        else:
            self.IsNationalPrime: bool = None


class SellerFeedbackType:
    """
    Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerPositiveFeedbackRating" in data:
            self.SellerPositiveFeedbackRating: float = float(data["SellerPositiveFeedbackRating"])
        else:
            self.SellerPositiveFeedbackRating: float = None
        if "FeedbackCount" in data:
            self.FeedbackCount: int = int(data["FeedbackCount"])
        else:
            self.FeedbackCount: int = None


class DetailedShippingTimeType:
    """
    The time range in which an item will likely be shipped once an order has been placed.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "minimumHours" in data:
            self.minimumHours: int = int(data["minimumHours"])
        else:
            self.minimumHours: int = None
        if "maximumHours" in data:
            self.maximumHours: int = int(data["maximumHours"])
        else:
            self.maximumHours: int = None
        if "availableDate" in data:
            self.availableDate: str = str(data["availableDate"])
        else:
            self.availableDate: str = None
        if "availabilityType" in data:
            self.availabilityType: str = str(data["availabilityType"])
        else:
            self.availabilityType: str = None


class ShipsFromType:
    """
    The state and country from where the item is shipped.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "State" in data:
            self.State: str = str(data["State"])
        else:
            self.State: str = None
        if "Country" in data:
            self.Country: str = str(data["Country"])
        else:
            self.Country: str = None


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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
        }[response.status_code]
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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
        }[response.status_code]
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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
        }[response.status_code]
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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
        }[response.status_code]
        return None if response_type is None else response_type(self._get_response_json(response))
