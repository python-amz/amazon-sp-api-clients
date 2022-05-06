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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class ASINIdentifier:

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    A marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AttributeSetList:
    """
    A list of product attributes if they are applicable to the product that is returned.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AttributeSetListItem:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyBoxEligibleOffers:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyBoxPriceType:

    landed_price: Optional["MoneyType"] = attrs.field()

    listing_price: Optional["MoneyType"] = attrs.field()

    points: Optional["Points"] = attrs.field()

    shipping: Optional["MoneyType"] = attrs.field()

    condition: Optional[str] = attrs.field()
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field()

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field()

    quantity_tier: Optional[int] = attrs.field()
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier for the offer.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyBoxPrices:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CompetitivePriceList:
    """
    A list of competitive pricing information.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CompetitivePriceType:

    competitive_price_id: Optional[str] = attrs.field()
    """
    The pricing model for each price that is returned.
        Possible values:
        * 1 - New Buy Box Price.
        * 2 - Used Buy Box Price.
    """

    price: Optional["PriceType"] = attrs.field()

    belongs_to_requester: Optional[bool] = attrs.field()
    """
    Indicates whether or not the pricing information is for an offer listing that belongs to the requester. The requester is the seller associated with the SellerId that was submitted with the request. Possible values are: true and false.
    """

    condition: Optional[str] = attrs.field()
    """
    Indicates the condition of the item whose pricing information is returned. Possible values are: New, Used, Collectible, Refurbished, or Club.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field()

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field()

    quantity_tier: Optional[int] = attrs.field()
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier for the offer.
    """

    subcondition: Optional[str] = attrs.field()
    """
    Indicates the subcondition of the item whose pricing information is returned. Possible values are: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CompetitivePricingType:
    """
    Competitive pricing information for the item.
    """

    competitive_prices: Optional["CompetitivePriceList"] = attrs.field()

    number_of_offer_listings: Optional["NumberOfOfferListingsList"] = attrs.field()

    trade_in_value: Optional["MoneyType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ConditionType:
    """
    Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DetailedShippingTimeType:
    """
    The time range in which an item will likely be shipped once an order has been placed.
    """

    availability_type: Optional[
        Union[Literal["NOW"], Literal["FUTURE_WITHOUT_DATE"], Literal["FUTURE_WITH_DATE"]]
    ] = attrs.field()
    """
    Indicates whether the item is available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE, FUTURE_WITH_DATE.
    """

    available_date: Optional[str] = attrs.field()
    """
    The date when the item will be available for shipping. Only displayed for items that are not currently available for shipping.
    """

    maximum_hours: Optional[int] = attrs.field()
    """
    The maximum time, in hours, that the item will likely be shipped after the order has been placed.

    Extra fields:
    {'schema_format': 'int64'}
    """

    minimum_hours: Optional[int] = attrs.field()
    """
    The minimum time, in hours, that the item will likely be shipped after the order has been placed.

    Extra fields:
    {'schema_format': 'int64'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentChannelType:
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOffersResponse:
    """
    The response schema for the getListingOffers and getItemOffers operations.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["GetOffersResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOffersResult:

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    identifier: Optional["ItemIdentifier"] = attrs.field()

    item_condition: Optional["ConditionType"] = attrs.field()

    marketplace_id: Optional[str] = attrs.field()
    """
    A marketplace identifier.
    """

    offers: Optional["OfferDetailList"] = attrs.field()

    sku: Optional[str] = attrs.field()
    """
    The stock keeping unit (SKU) of the item.
    """

    summary: Optional["Summary"] = attrs.field()

    status: Optional[str] = attrs.field()
    """
    The status of the operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPricingResponse:
    """
    The response schema for the getPricing and getCompetitivePricing operations.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["PriceList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class IdentifierType:
    """
    Specifies the identifiers used to uniquely identify an item.
    """

    marketplace_asin: Optional["ASINIdentifier"] = attrs.field()

    skuidentifier: Optional["SellerSKUIdentifier"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemIdentifier:
    """
    Information that identifies an item.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    item_condition: Optional["ConditionType"] = attrs.field()

    marketplace_id: Optional[str] = attrs.field()
    """
    A marketplace identifier. Specifies the marketplace from which prices are returned.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller stock keeping unit (SKU) of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LowestPriceType:

    landed_price: Optional["MoneyType"] = attrs.field()

    listing_price: Optional["MoneyType"] = attrs.field()

    points: Optional["Points"] = attrs.field()

    shipping: Optional["MoneyType"] = attrs.field()

    condition: Optional[str] = attrs.field()
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    fulfillment_channel: Optional[str] = attrs.field()
    """
    Indicates whether the item is fulfilled by Amazon or by the seller.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field()

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field()

    quantity_tier: Optional[int] = attrs.field()
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LowestPrices:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class MoneyType:

    amount: Optional[float] = attrs.field()
    """
    The monetary value.
    """

    currency_code: Optional[str] = attrs.field()
    """
    The currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NumberOfOfferListingsList:
    """
    The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class NumberOfOffers:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferCountType:
    """
    The total number of offers for the specified condition and fulfillment channel.
    """

    offer_count: Optional[int] = attrs.field()
    """
    The number of offers in a fulfillment channel that meet a specific condition.

    Extra fields:
    {'schema_format': 'int32'}
    """

    condition: Optional[str] = attrs.field()
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    fulfillment_channel: Optional["FulfillmentChannelType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferCustomerType:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferDetail:

    condition_notes: Optional[str] = attrs.field()
    """
    Information about the condition of the item.
    """

    is_buy_box_winner: Optional[bool] = attrs.field()
    """
    When true, the offer is currently in the Buy Box. There can be up to two Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.
    """

    is_featured_merchant: Optional[bool] = attrs.field()
    """
    When true, the seller of the item is eligible to win the Buy Box.
    """

    is_fulfilled_by_amazon: Optional[bool] = attrs.field()
    """
    When true, the offer is fulfilled by Amazon.
    """

    listing_price: Optional["MoneyType"] = attrs.field()

    my_offer: Optional[bool] = attrs.field()
    """
    When true, this is the seller's offer.
    """

    points: Optional["Points"] = attrs.field()

    prime_information: Optional["PrimeInformationType"] = attrs.field()

    seller_feedback_rating: Optional["SellerFeedbackType"] = attrs.field()

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier for the offer.
    """

    shipping: Optional["MoneyType"] = attrs.field()

    shipping_time: Optional["DetailedShippingTimeType"] = attrs.field()

    ships_from: Optional["ShipsFromType"] = attrs.field()

    sub_condition: Optional[str] = attrs.field()
    """
    The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field()

    quantity_discount_prices: Optional[List["QuantityDiscountPriceType"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferDetailList:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferListingCountType:
    """
    The number of offer listings with the specified condition.
    """

    count: Optional[int] = attrs.field()
    """
    The number of offer listings.

    Extra fields:
    {'schema_format': 'int32'}
    """

    condition: Optional[str] = attrs.field()
    """
    The condition of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferType:

    buying_price: Optional["PriceType"] = attrs.field()

    fulfillment_channel: Optional[str] = attrs.field()
    """
    The fulfillment channel for the offer listing. Possible values:
        * Amazon - Fulfilled by Amazon.
        * Merchant - Fulfilled by the seller.
    """

    item_condition: Optional[str] = attrs.field()
    """
    The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club.
    """

    item_sub_condition: Optional[str] = attrs.field()
    """
    The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """

    regular_price: Optional["MoneyType"] = attrs.field()

    seller_sku: Optional[str] = attrs.field()
    """
    The seller stock keeping unit (SKU) of the item.
    """

    business_price: Optional["MoneyType"] = attrs.field()

    offer_type: Optional["OfferCustomerType"] = attrs.field()

    quantity_discount_prices: Optional[List["QuantityDiscountPriceType"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OffersList:
    """
    A list of offers.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Points:

    points_monetary_value: Optional["MoneyType"] = attrs.field()

    points_number: Optional[int] = attrs.field()
    """
    The number of points.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Price:

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    product: Optional["Product"] = attrs.field()

    seller_sku: Optional[str] = attrs.field()
    """
    The seller stock keeping unit (SKU) of the item.
    """

    status: Optional[str] = attrs.field()
    """
    The status of the operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PriceList:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PriceType:

    landed_price: Optional["MoneyType"] = attrs.field()

    listing_price: Optional["MoneyType"] = attrs.field()

    points: Optional["Points"] = attrs.field()

    shipping: Optional["MoneyType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PrimeInformationType:
    """
    Amazon Prime information.
    """

    is_national_prime: Optional[bool] = attrs.field()
    """
    Indicates whether the offer is an Amazon Prime offer throughout the entire marketplace where it is listed.
    """

    is_prime: Optional[bool] = attrs.field()
    """
    Indicates whether the offer is an Amazon Prime offer.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Product:
    """
    An item.
    """

    attribute_sets: Optional["AttributeSetList"] = attrs.field()

    competitive_pricing: Optional["CompetitivePricingType"] = attrs.field()

    identifiers: Optional["IdentifierType"] = attrs.field()

    offers: Optional["OffersList"] = attrs.field()

    relationships: Optional["RelationshipList"] = attrs.field()

    sales_rankings: Optional["SalesRankList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class QuantityDiscountPriceType:
    """
    Contains pricing information that includes special pricing when buying in bulk.
    """

    listing_price: Optional["MoneyType"] = attrs.field()

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field()

    quantity_tier: Optional[int] = attrs.field()
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class QuantityDiscountType:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RelationshipList:
    """
    A list that contains product variation information, if applicable.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RelationshipListItem:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SalesRankList:
    """
    A list of sales rank information for the item, by category.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SalesRankType:

    product_category_id: Optional[str] = attrs.field()
    """
    Identifies the item category from which the sales rank is taken.
    """

    rank: Optional[int] = attrs.field()
    """
    The sales rank of the item within the item category.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerFeedbackType:
    """
    Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.
    """

    feedback_count: Optional[int] = attrs.field()
    """
    The number of ratings received about the seller.

    Extra fields:
    {'schema_format': 'int64'}
    """

    seller_positive_feedback_rating: Optional[float] = attrs.field()
    """
    The percentage of positive feedback for the seller in the past 365 days.

    Extra fields:
    {'schema_format': 'double'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerSKUIdentifier:

    marketplace_id: Optional[str] = attrs.field()
    """
    A marketplace identifier.
    """

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier submitted for the operation.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller stock keeping unit (SKU) of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipsFromType:
    """
    The state and country from where the item is shipped.
    """

    country: Optional[str] = attrs.field()
    """
    The country from where the item is shipped.
    """

    state: Optional[str] = attrs.field()
    """
    The state from where the item is shipped.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Summary:
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """

    buy_box_eligible_offers: Optional["BuyBoxEligibleOffers"] = attrs.field()

    buy_box_prices: Optional["BuyBoxPrices"] = attrs.field()

    competitive_price_threshold: Optional["MoneyType"] = attrs.field()

    list_price: Optional["MoneyType"] = attrs.field()

    lowest_prices: Optional["LowestPrices"] = attrs.field()

    number_of_offers: Optional["NumberOfOffers"] = attrs.field()

    offers_available_time: Optional[datetime] = attrs.field()
    """
    When the status is ActiveButTooSoonForProcessing, this is the time when the offers will be available for processing.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    sales_rankings: Optional["SalesRankList"] = attrs.field()

    suggested_lower_price_plus_shipping: Optional["MoneyType"] = attrs.field()

    total_offer_count: Optional[int] = attrs.field()
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
