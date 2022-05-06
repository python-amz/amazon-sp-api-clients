"""
Selling Partner API for Pricing
=============================================================================================

The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class ASINIdentifier:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """


@attrs.define
class AttributeSetList:
    """
    A list of product attributes if they are applicable to the product that is returned.
    """

    pass


@attrs.define
class BuyBoxEligibleOffers:

    pass


@attrs.define
class BuyBoxPriceType:

    landed_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    listing_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    points: "Points" = attrs.field(
        kw_only=True,
    )

    shipping: "MoneyType" = attrs.field(
        kw_only=True,
    )

    condition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    offer_type: "OfferCustomerType" = attrs.field(
        kw_only=True,
    )

    quantity_discount_type: "QuantityDiscountType" = attrs.field(
        kw_only=True,
    )

    quantity_tier: int = attrs.field(
        kw_only=True,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier for the offer.
    """


@attrs.define
class BuyBoxPrices:

    pass


@attrs.define
class CompetitivePriceList:
    """
    A list of competitive pricing information.
    """

    pass


@attrs.define
class CompetitivePriceType:

    competitive_price_id: str = attrs.field(
        kw_only=True,
    )
    """
    The pricing model for each price that is returned.
        Possible values:
        * 1 - New Buy Box Price.
        * 2 - Used Buy Box Price.
    """

    price: "PriceType" = attrs.field(
        kw_only=True,
    )

    belongs_to_requester: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether or not the pricing information is for an offer listing that belongs to the requester. The requester is the seller associated with the SellerId that was submitted with the request. Possible values are: true and false.
    """

    condition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the condition of the item whose pricing information is returned. Possible values are: New, Used, Collectible, Refurbished, or Club.
    """

    offer_type: "OfferCustomerType" = attrs.field(
        kw_only=True,
    )

    quantity_discount_type: "QuantityDiscountType" = attrs.field(
        kw_only=True,
    )

    quantity_tier: int = attrs.field(
        kw_only=True,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier for the offer.
    """

    subcondition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the subcondition of the item whose pricing information is returned. Possible values are: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """


@attrs.define
class CompetitivePricingType:
    """
    Competitive pricing information for the item.
    """

    competitive_prices: "CompetitivePriceList" = attrs.field(
        kw_only=True,
    )

    number_of_offer_listings: "NumberOfOfferListingsList" = attrs.field(
        kw_only=True,
    )

    trade_in_value: "MoneyType" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ConditionType:
    """
    Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club.
    """

    pass


@attrs.define
class DetailedShippingTimeType:
    """
    The time range in which an item will likely be shipped once an order has been placed.
    """

    availability_type: Union[Literal["NOW"], Literal["FUTURE_WITHOUT_DATE"], Literal["FUTURE_WITH_DATE"]] = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the item is available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE, FUTURE_WITH_DATE.
    """

    available_date: str = attrs.field(
        kw_only=True,
    )
    """
    The date when the item will be available for shipping. Only displayed for items that are not currently available for shipping.
    """

    maximum_hours: int = attrs.field(
        kw_only=True,
    )
    """
    The maximum time, in hours, that the item will likely be shipped after the order has been placed.

    Extra fields:
    {'schema_format': 'int64'}
    """

    minimum_hours: int = attrs.field(
        kw_only=True,
    )
    """
    The minimum time, in hours, that the item will likely be shipped after the order has been placed.

    Extra fields:
    {'schema_format': 'int64'}
    """


@attrs.define
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class FulfillmentChannelType:
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """

    pass


@attrs.define
class GetOffersResponse:
    """
    The response schema for the getListingOffers and getItemOffers operations.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "GetOffersResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetOffersResult:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    identifier: "ItemIdentifier" = attrs.field(
        kw_only=True,
    )

    item_condition: "ConditionType" = attrs.field(
        kw_only=True,
    )

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """

    offers: "OfferDetailList" = attrs.field(
        kw_only=True,
    )

    sku: str = attrs.field(
        kw_only=True,
    )
    """
    The stock keeping unit (SKU) of the item.
    """

    summary: "Summary" = attrs.field(
        kw_only=True,
    )

    status: str = attrs.field(
        kw_only=True,
    )
    """
    The status of the operation.
    """


@attrs.define
class GetPricingResponse:
    """
    The response schema for the getPricing and getCompetitivePricing operations.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "PriceList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class IdentifierType:
    """
    Specifies the identifiers used to uniquely identify an item.
    """

    marketplace_asin: "ASINIdentifier" = attrs.field(
        kw_only=True,
    )

    skuidentifier: "SellerSKUIdentifier" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ItemIdentifier:
    """
    Information that identifies an item.
    """

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    item_condition: "ConditionType" = attrs.field(
        kw_only=True,
    )

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier. Specifies the marketplace from which prices are returned.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """


@attrs.define
class LowestPriceType:

    landed_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    listing_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    points: "Points" = attrs.field(
        kw_only=True,
    )

    shipping: "MoneyType" = attrs.field(
        kw_only=True,
    )

    condition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    fulfillment_channel: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the item is fulfilled by Amazon or by the seller.
    """

    offer_type: "OfferCustomerType" = attrs.field(
        kw_only=True,
    )

    quantity_discount_type: "QuantityDiscountType" = attrs.field(
        kw_only=True,
    )

    quantity_tier: int = attrs.field(
        kw_only=True,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define
class LowestPrices:

    pass


@attrs.define
class MoneyType:

    amount: float = attrs.field(
        kw_only=True,
    )
    """
    The monetary value.
    """

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    The currency code in ISO 4217 format.
    """


@attrs.define
class NumberOfOfferListingsList:
    """
    The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned.
    """

    pass


@attrs.define
class NumberOfOffers:

    pass


@attrs.define
class OfferCountType:
    """
    The total number of offers for the specified condition and fulfillment channel.
    """

    offer_count: int = attrs.field(
        kw_only=True,
    )
    """
    The number of offers in a fulfillment channel that meet a specific condition.

    Extra fields:
    {'schema_format': 'int32'}
    """

    condition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    fulfillment_channel: "FulfillmentChannelType" = attrs.field(
        kw_only=True,
    )


@attrs.define
class OfferCustomerType:

    pass


@attrs.define
class OfferDetail:

    condition_notes: str = attrs.field(
        kw_only=True,
    )
    """
    Information about the condition of the item.
    """

    is_buy_box_winner: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the offer is currently in the Buy Box. There can be up to two Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.
    """

    is_featured_merchant: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the seller of the item is eligible to win the Buy Box.
    """

    is_fulfilled_by_amazon: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the offer is fulfilled by Amazon.
    """

    listing_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    my_offer: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, this is the seller's offer.
    """

    points: "Points" = attrs.field(
        kw_only=True,
    )

    prime_information: "PrimeInformationType" = attrs.field(
        kw_only=True,
    )

    seller_feedback_rating: "SellerFeedbackType" = attrs.field(
        kw_only=True,
    )

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier for the offer.
    """

    shipping: "MoneyType" = attrs.field(
        kw_only=True,
    )

    shipping_time: "DetailedShippingTimeType" = attrs.field(
        kw_only=True,
    )

    ships_from: "ShipsFromType" = attrs.field(
        kw_only=True,
    )

    sub_condition: str = attrs.field(
        kw_only=True,
    )
    """
    The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """

    offer_type: "OfferCustomerType" = attrs.field(
        kw_only=True,
    )

    quantity_discount_prices: List["QuantityDiscountPriceType"] = attrs.field(
        kw_only=True,
    )


@attrs.define
class OfferDetailList:

    pass


@attrs.define
class OfferListingCountType:
    """
    The number of offer listings with the specified condition.
    """

    count: int = attrs.field(
        kw_only=True,
    )
    """
    The number of offer listings.

    Extra fields:
    {'schema_format': 'int32'}
    """

    condition: str = attrs.field(
        kw_only=True,
    )
    """
    The condition of the item.
    """


@attrs.define
class OfferType:

    buying_price: "PriceType" = attrs.field(
        kw_only=True,
    )

    fulfillment_channel: str = attrs.field(
        kw_only=True,
    )
    """
    The fulfillment channel for the offer listing. Possible values:
        * Amazon - Fulfilled by Amazon.
        * Merchant - Fulfilled by the seller.
    """

    item_condition: str = attrs.field(
        kw_only=True,
    )
    """
    The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club.
    """

    item_sub_condition: str = attrs.field(
        kw_only=True,
    )
    """
    The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """

    regular_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """

    business_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    offer_type: "OfferCustomerType" = attrs.field(
        kw_only=True,
    )

    quantity_discount_prices: List["QuantityDiscountPriceType"] = attrs.field(
        kw_only=True,
    )


@attrs.define
class OffersList:
    """
    A list of offers.
    """

    pass


@attrs.define
class Points:

    points_monetary_value: "MoneyType" = attrs.field(
        kw_only=True,
    )

    points_number: int = attrs.field(
        kw_only=True,
    )
    """
    The number of points.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define
class Price:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    product: "Product" = attrs.field(
        kw_only=True,
    )

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """

    status: str = attrs.field(
        kw_only=True,
    )
    """
    The status of the operation.
    """


@attrs.define
class PriceList:

    pass


@attrs.define
class PriceType:

    landed_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    listing_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    points: "Points" = attrs.field(
        kw_only=True,
    )

    shipping: "MoneyType" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PrimeInformationType:
    """
    Amazon Prime information.
    """

    is_national_prime: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the offer is an Amazon Prime offer throughout the entire marketplace where it is listed.
    """

    is_prime: bool = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the offer is an Amazon Prime offer.
    """


@attrs.define
class Product:
    """
    An item.
    """

    attribute_sets: "AttributeSetList" = attrs.field(
        kw_only=True,
    )

    competitive_pricing: "CompetitivePricingType" = attrs.field(
        kw_only=True,
    )

    identifiers: "IdentifierType" = attrs.field(
        kw_only=True,
    )

    offers: "OffersList" = attrs.field(
        kw_only=True,
    )

    relationships: "RelationshipList" = attrs.field(
        kw_only=True,
    )

    sales_rankings: "SalesRankList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class QuantityDiscountPriceType:
    """
    Contains pricing information that includes special pricing when buying in bulk.
    """

    listing_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    quantity_discount_type: "QuantityDiscountType" = attrs.field(
        kw_only=True,
    )

    quantity_tier: int = attrs.field(
        kw_only=True,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define
class QuantityDiscountType:

    pass


@attrs.define
class RelationshipList:
    """
    A list that contains product variation information, if applicable.
    """

    pass


@attrs.define
class SalesRankList:
    """
    A list of sales rank information for the item, by category.
    """

    pass


@attrs.define
class SalesRankType:

    product_category_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the item category from which the sales rank is taken.
    """

    rank: int = attrs.field(
        kw_only=True,
    )
    """
    The sales rank of the item within the item category.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define
class SellerFeedbackType:
    """
    Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.
    """

    feedback_count: int = attrs.field(
        kw_only=True,
    )
    """
    The number of ratings received about the seller.

    Extra fields:
    {'schema_format': 'int64'}
    """

    seller_positive_feedback_rating: float = attrs.field(
        kw_only=True,
    )
    """
    The percentage of positive feedback for the seller in the past 365 days.

    Extra fields:
    {'schema_format': 'double'}
    """


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier submitted for the operation.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """


@attrs.define
class ShipsFromType:
    """
    The state and country from where the item is shipped.
    """

    country: str = attrs.field(
        kw_only=True,
    )
    """
    The country from where the item is shipped.
    """

    state: str = attrs.field(
        kw_only=True,
    )
    """
    The state from where the item is shipped.
    """


@attrs.define
class Summary:
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """

    buy_box_eligible_offers: "BuyBoxEligibleOffers" = attrs.field(
        kw_only=True,
    )

    buy_box_prices: "BuyBoxPrices" = attrs.field(
        kw_only=True,
    )

    competitive_price_threshold: "MoneyType" = attrs.field(
        kw_only=True,
    )

    list_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    lowest_prices: "LowestPrices" = attrs.field(
        kw_only=True,
    )

    number_of_offers: "NumberOfOffers" = attrs.field(
        kw_only=True,
    )

    offers_available_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    When the status is ActiveButTooSoonForProcessing, this is the time when the offers will be available for processing.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    sales_rankings: "SalesRankList" = attrs.field(
        kw_only=True,
    )

    suggested_lower_price_plus_shipping: "MoneyType" = attrs.field(
        kw_only=True,
    )

    total_offer_count: int = attrs.field(
        kw_only=True,
    )
    """
    The number of unique offers contained in NumberOfOffers.

    Extra fields:
    {'schema_format': 'int32'}
    """


class ProductPricingV0Client(BaseClient):
    def get_competitive_pricing(
        self,
        marketplace_id: str,
        item_type: Union[Literal["Asin"], Literal["Sku"]],
        asins: List[str] = None,
        skus: List[str] = None,
        customer_type: Union[Literal["Consumer"], Literal["Business"]] = None,
    ):
        """
        Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            asins: A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            item_type: Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.
            customer_type: Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.
        """
        url = "/products/pricing/v0/competitivePrice"
        values = (
            marketplace_id,
            asins,
            skus,
            item_type,
            customer_type,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_competitive_pricing_params)
        return response

    _get_competitive_pricing_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("Asins", "query"),
        ("Skus", "query"),
        ("ItemType", "query"),
        ("CustomerType", "query"),
    )

    def get_item_offers(
        self,
        marketplace_id: str,
        item_condition: Union[
            Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
        ],
        asin: str,
        customer_type: Union[Literal["Consumer"], Literal["Business"]] = None,
    ):
        """
        Returns the lowest priced offers for a single item based on ASIN.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
        """
        url = "/products/pricing/v0/items/{Asin}/offers"
        values = (
            marketplace_id,
            item_condition,
            asin,
            customer_type,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_item_offers_params)
        return response

    _get_item_offers_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ItemCondition", "query"),
        ("Asin", "path"),
        ("CustomerType", "query"),
    )

    def get_listing_offers(
        self,
        marketplace_id: str,
        item_condition: Union[
            Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
        ],
        seller_sku: str,
        customer_type: Union[Literal["Consumer"], Literal["Business"]] = None,
    ):
        """
        Returns the lowest priced offers for a single SKU listing.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            seller_sku: Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
        """
        url = "/products/pricing/v0/listings/{SellerSKU}/offers"
        values = (
            marketplace_id,
            item_condition,
            seller_sku,
            customer_type,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_listing_offers_params)
        return response

    _get_listing_offers_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ItemCondition", "query"),
        ("SellerSKU", "path"),
        ("CustomerType", "query"),
    )

    def get_pricing(
        self,
        marketplace_id: str,
        item_type: Union[Literal["Asin"], Literal["Sku"]],
        asins: List[str] = None,
        skus: List[str] = None,
        item_condition: Union[
            Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
        ] = None,
        offer_type: Union[Literal["B2C"], Literal["B2B"]] = None,
    ):
        """
        Returns pricing information for a seller's offer listings based on seller SKU or ASIN.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            asins: A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            item_type: Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            offer_type: Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.
        """
        url = "/products/pricing/v0/price"
        values = (
            marketplace_id,
            asins,
            skus,
            item_type,
            item_condition,
            offer_type,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_pricing_params)
        return response

    _get_pricing_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("Asins", "query"),
        ("Skus", "query"),
        ("ItemType", "query"),
        ("ItemCondition", "query"),
        ("OfferType", "query"),
    )
