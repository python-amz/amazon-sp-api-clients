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
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _asinidentifier_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ASINIdentifier(**data)

    asin: str = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AttributeSetListItem:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _attribute_set_list_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return AttributeSetListItem(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyBoxPriceType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _buy_box_price_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return BuyBoxPriceType(**data)

    landed_price: "MoneyType" = attrs.field(
        default=None,
    )

    listing_price: "MoneyType" = attrs.field(
        default=None,
    )

    points: Optional["Points"] = attrs.field(
        default=None,
    )

    shipping: "MoneyType" = attrs.field(
        default=None,
    )

    condition: str = attrs.field(
        default=None,
    )
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field(
        default=None,
    )

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field(
        default=None,
    )

    quantity_tier: Optional[int] = attrs.field(
        default=None,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller identifier for the offer.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CompetitivePriceType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _competitive_price_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CompetitivePriceType(**data)

    competitive_price_id: str = attrs.field(
        default=None,
    )
    """
    The pricing model for each price that is returned.
        Possible values:
        * 1 - New Buy Box Price.
        * 2 - Used Buy Box Price.
    """

    price: "PriceType" = attrs.field(
        default=None,
    )

    belongs_to_requester: Optional[bool] = attrs.field(
        default=None,
    )
    """
    Indicates whether or not the pricing information is for an offer listing that belongs to the requester. The requester is the seller associated with the SellerId that was submitted with the request. Possible values are: true and false.
    """

    condition: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates the condition of the item whose pricing information is returned. Possible values are: New, Used, Collectible, Refurbished, or Club.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field(
        default=None,
    )

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field(
        default=None,
    )

    quantity_tier: Optional[int] = attrs.field(
        default=None,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller identifier for the offer.
    """

    subcondition: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates the subcondition of the item whose pricing information is returned. Possible values are: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CompetitivePricingType:
    """
    Competitive pricing information for the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _competitive_pricing_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CompetitivePricingType(**data)

    competitive_prices: List["CompetitivePriceType"] = attrs.field(
        default=None,
    )
    """
    A list of competitive pricing information.
    """

    number_of_offer_listings: List["OfferListingCountType"] = attrs.field(
        default=None,
    )
    """
    The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned.
    """

    trade_in_value: Optional["MoneyType"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ConditionType:
    """
    Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _condition_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ConditionType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DetailedShippingTimeType:
    """
    The time range in which an item will likely be shipped once an order has been placed.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _detailed_shipping_time_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return DetailedShippingTimeType(**data)

    availability_type: Optional[
        Union[Literal["NOW"], Literal["FUTURE_WITHOUT_DATE"], Literal["FUTURE_WITH_DATE"]]
    ] = attrs.field(
        default=None,
    )
    """
    Indicates whether the item is available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE, FUTURE_WITH_DATE.
    """

    available_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The date when the item will be available for shipping. Only displayed for items that are not currently available for shipping.
    """

    maximum_hours: Optional[int] = attrs.field(
        default=None,
    )
    """
    The maximum time, in hours, that the item will likely be shipped after the order has been placed.

    Extra fields:
    {'schema_format': 'int64'}
    """

    minimum_hours: Optional[int] = attrs.field(
        default=None,
    )
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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentChannelType:
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _fulfillment_channel_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return FulfillmentChannelType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOffersResponse:
    """
    The response schema for the getListingOffers and getItemOffers operations.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_offers_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetOffersResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetOffersResult"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOffersResult:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_offers_result_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetOffersResult(**data)

    asin: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    identifier: "ItemIdentifier" = attrs.field(
        default=None,
    )
    """
    Information that identifies an item.
    """

    item_condition: "ConditionType" = attrs.field(
        default=None,
    )
    """
    Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club.
    """

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier.
    """

    offers: List["OfferDetail"] = attrs.field(
        default=None,
    )

    sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    The stock keeping unit (SKU) of the item.
    """

    summary: "Summary" = attrs.field(
        default=None,
    )
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """

    status: str = attrs.field(
        default=None,
    )
    """
    The status of the operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPricingResponse:
    """
    The response schema for the getPricing and getCompetitivePricing operations.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_pricing_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetPricingResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional[List["Price"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class IdentifierType:
    """
    Specifies the identifiers used to uniquely identify an item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _identifier_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return IdentifierType(**data)

    marketplace_asin: "ASINIdentifier" = attrs.field(
        default=None,
    )

    skuidentifier: Optional["SellerSKUIdentifier"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemIdentifier:
    """
    Information that identifies an item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_identifier_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemIdentifier(**data)

    asin: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    item_condition: "ConditionType" = attrs.field(
        default=None,
    )
    """
    Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club.
    """

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier. Specifies the marketplace from which prices are returned.
    """

    seller_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LowestPriceType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _lowest_price_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return LowestPriceType(**data)

    landed_price: "MoneyType" = attrs.field(
        default=None,
    )

    listing_price: "MoneyType" = attrs.field(
        default=None,
    )

    points: Optional["Points"] = attrs.field(
        default=None,
    )

    shipping: "MoneyType" = attrs.field(
        default=None,
    )

    condition: str = attrs.field(
        default=None,
    )
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    fulfillment_channel: str = attrs.field(
        default=None,
    )
    """
    Indicates whether the item is fulfilled by Amazon or by the seller.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field(
        default=None,
    )

    quantity_discount_type: Optional["QuantityDiscountType"] = attrs.field(
        default=None,
    )

    quantity_tier: Optional[int] = attrs.field(
        default=None,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class MoneyType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return MoneyType(**data)

    amount: Optional[float] = attrs.field(
        default=None,
    )
    """
    The monetary value.
    """

    currency_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferCountType:
    """
    The total number of offers for the specified condition and fulfillment channel.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _offer_count_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OfferCountType(**data)

    offer_count: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of offers in a fulfillment channel that meet a specific condition.

    Extra fields:
    {'schema_format': 'int32'}
    """

    condition: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
    """

    fulfillment_channel: Optional["FulfillmentChannelType"] = attrs.field(
        default=None,
    )
    """
    Indicates whether the item is fulfilled by Amazon or by the seller (merchant).
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferCustomerType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _offer_customer_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OfferCustomerType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferDetail:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _offer_detail_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OfferDetail(**data)

    condition_notes: Optional[str] = attrs.field(
        default=None,
    )
    """
    Information about the condition of the item.
    """

    is_buy_box_winner: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the offer is currently in the Buy Box. There can be up to two Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.
    """

    is_featured_merchant: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the seller of the item is eligible to win the Buy Box.
    """

    is_fulfilled_by_amazon: bool = attrs.field(
        default=None,
    )
    """
    When true, the offer is fulfilled by Amazon.
    """

    listing_price: "MoneyType" = attrs.field(
        default=None,
    )

    my_offer: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, this is the seller's offer.
    """

    points: Optional["Points"] = attrs.field(
        default=None,
    )

    prime_information: Optional["PrimeInformationType"] = attrs.field(
        default=None,
    )
    """
    Amazon Prime information.
    """

    seller_feedback_rating: Optional["SellerFeedbackType"] = attrs.field(
        default=None,
    )
    """
    Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.
    """

    seller_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller identifier for the offer.
    """

    shipping: "MoneyType" = attrs.field(
        default=None,
    )

    shipping_time: "DetailedShippingTimeType" = attrs.field(
        default=None,
    )
    """
    The time range in which an item will likely be shipped once an order has been placed.
    """

    ships_from: Optional["ShipsFromType"] = attrs.field(
        default=None,
    )
    """
    The state and country from where the item is shipped.
    """

    sub_condition: str = attrs.field(
        default=None,
    )
    """
    The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """

    offer_type: Optional["OfferCustomerType"] = attrs.field(
        default=None,
    )

    quantity_discount_prices: Optional[List["QuantityDiscountPriceType"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferListingCountType:
    """
    The number of offer listings with the specified condition.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _offer_listing_count_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OfferListingCountType(**data)

    count: int = attrs.field(
        default=None,
    )
    """
    The number of offer listings.

    Extra fields:
    {'schema_format': 'int32'}
    """

    condition: str = attrs.field(
        default=None,
    )
    """
    The condition of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OfferType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _offer_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OfferType(**data)

    buying_price: "PriceType" = attrs.field(
        default=None,
    )

    fulfillment_channel: str = attrs.field(
        default=None,
    )
    """
    The fulfillment channel for the offer listing. Possible values:
        * Amazon - Fulfilled by Amazon.
        * Merchant - Fulfilled by the seller.
    """

    item_condition: str = attrs.field(
        default=None,
    )
    """
    The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club.
    """

    item_sub_condition: str = attrs.field(
        default=None,
    )
    """
    The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
    """

    regular_price: "MoneyType" = attrs.field(
        default=None,
    )

    seller_sku: str = attrs.field(
        default=None,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """

    business_price: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    offer_type: Optional["OfferCustomerType"] = attrs.field(
        default=None,
    )

    quantity_discount_prices: Optional[List["QuantityDiscountPriceType"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class Points:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _points_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Points(**data)

    points_monetary_value: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    points_number: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of points.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Price:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _price_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Price(**data)

    asin: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    product: Optional["Product"] = attrs.field(
        default=None,
    )
    """
    An item.
    """

    seller_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """

    status: str = attrs.field(
        default=None,
    )
    """
    The status of the operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PriceType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _price_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PriceType(**data)

    landed_price: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    listing_price: "MoneyType" = attrs.field(
        default=None,
    )

    points: Optional["Points"] = attrs.field(
        default=None,
    )

    shipping: Optional["MoneyType"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class PrimeInformationType:
    """
    Amazon Prime information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _prime_information_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PrimeInformationType(**data)

    is_national_prime: bool = attrs.field(
        default=None,
    )
    """
    Indicates whether the offer is an Amazon Prime offer throughout the entire marketplace where it is listed.
    """

    is_prime: bool = attrs.field(
        default=None,
    )
    """
    Indicates whether the offer is an Amazon Prime offer.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Product:
    """
    An item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _product_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Product(**data)

    attribute_sets: Optional[List["AttributeSetListItem"]] = attrs.field(
        default=None,
    )
    """
    A list of product attributes if they are applicable to the product that is returned.
    """

    competitive_pricing: Optional["CompetitivePricingType"] = attrs.field(
        default=None,
    )
    """
    Competitive pricing information for the item.
    """

    identifiers: "IdentifierType" = attrs.field(
        default=None,
    )
    """
    Specifies the identifiers used to uniquely identify an item.
    """

    offers: Optional[List["OfferType"]] = attrs.field(
        default=None,
    )
    """
    A list of offers.
    """

    relationships: Optional[List["RelationshipListItem"]] = attrs.field(
        default=None,
    )
    """
    A list that contains product variation information, if applicable.
    """

    sales_rankings: Optional[List["SalesRankType"]] = attrs.field(
        default=None,
    )
    """
    A list of sales rank information for the item, by category.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class QuantityDiscountPriceType:
    """
    Contains pricing information that includes special pricing when buying in bulk.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _quantity_discount_price_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return QuantityDiscountPriceType(**data)

    listing_price: "MoneyType" = attrs.field(
        default=None,
    )

    quantity_discount_type: "QuantityDiscountType" = attrs.field(
        default=None,
    )

    quantity_tier: int = attrs.field(
        default=None,
    )
    """
    Indicates at what quantity this price becomes active.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class QuantityDiscountType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _quantity_discount_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return QuantityDiscountType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RelationshipListItem:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _relationship_list_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return RelationshipListItem(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SalesRankType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _sales_rank_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SalesRankType(**data)

    product_category_id: str = attrs.field(
        default=None,
    )
    """
    Identifies the item category from which the sales rank is taken.
    """

    rank: int = attrs.field(
        default=None,
    )
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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _seller_feedback_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SellerFeedbackType(**data)

    feedback_count: int = attrs.field(
        default=None,
    )
    """
    The number of ratings received about the seller.

    Extra fields:
    {'schema_format': 'int64'}
    """

    seller_positive_feedback_rating: Optional[float] = attrs.field(
        default=None,
    )
    """
    The percentage of positive feedback for the seller in the past 365 days.

    Extra fields:
    {'schema_format': 'double'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerSKUIdentifier:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _seller_skuidentifier_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SellerSKUIdentifier(**data)

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier.
    """

    seller_id: str = attrs.field(
        default=None,
    )
    """
    The seller identifier submitted for the operation.
    """

    seller_sku: str = attrs.field(
        default=None,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipsFromType:
    """
    The state and country from where the item is shipped.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _ships_from_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipsFromType(**data)

    country: Optional[str] = attrs.field(
        default=None,
    )
    """
    The country from where the item is shipped.
    """

    state: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state from where the item is shipped.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Summary:
    """
    Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _summary_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Summary(**data)

    buy_box_eligible_offers: Optional[List["OfferCountType"]] = attrs.field(
        default=None,
    )

    buy_box_prices: Optional[List["BuyBoxPriceType"]] = attrs.field(
        default=None,
    )

    competitive_price_threshold: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    list_price: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    lowest_prices: Optional[List["LowestPriceType"]] = attrs.field(
        default=None,
    )

    number_of_offers: Optional[List["OfferCountType"]] = attrs.field(
        default=None,
    )

    offers_available_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    When the status is ActiveButTooSoonForProcessing, this is the time when the offers will be available for processing.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    sales_rankings: Optional[List["SalesRankType"]] = attrs.field(
        default=None,
    )
    """
    A list of sales rank information for the item, by category.
    """

    suggested_lower_price_plus_shipping: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    total_offer_count: int = attrs.field(
        default=None,
    )
    """
    The number of unique offers contained in NumberOfOffers.

    Extra fields:
    {'schema_format': 'int32'}
    """


_asinidentifier_name_convert = {
    "ASIN": "asin",
    "MarketplaceId": "marketplace_id",
}

_attribute_set_list_item_name_convert = {}

_buy_box_price_type_name_convert = {
    "LandedPrice": "landed_price",
    "ListingPrice": "listing_price",
    "Points": "points",
    "Shipping": "shipping",
    "condition": "condition",
    "offerType": "offer_type",
    "quantityDiscountType": "quantity_discount_type",
    "quantityTier": "quantity_tier",
    "sellerId": "seller_id",
}

_competitive_price_type_name_convert = {
    "CompetitivePriceId": "competitive_price_id",
    "Price": "price",
    "belongsToRequester": "belongs_to_requester",
    "condition": "condition",
    "offerType": "offer_type",
    "quantityDiscountType": "quantity_discount_type",
    "quantityTier": "quantity_tier",
    "sellerId": "seller_id",
    "subcondition": "subcondition",
}

_competitive_pricing_type_name_convert = {
    "CompetitivePrices": "competitive_prices",
    "NumberOfOfferListings": "number_of_offer_listings",
    "TradeInValue": "trade_in_value",
}

_condition_type_name_convert = {}

_detailed_shipping_time_type_name_convert = {
    "availabilityType": "availability_type",
    "availableDate": "available_date",
    "maximumHours": "maximum_hours",
    "minimumHours": "minimum_hours",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_fulfillment_channel_type_name_convert = {}

_get_offers_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_offers_result_name_convert = {
    "ASIN": "asin",
    "Identifier": "identifier",
    "ItemCondition": "item_condition",
    "MarketplaceID": "marketplace_id",
    "Offers": "offers",
    "SKU": "sku",
    "Summary": "summary",
    "status": "status",
}

_get_pricing_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_identifier_type_name_convert = {
    "MarketplaceASIN": "marketplace_asin",
    "SKUIdentifier": "skuidentifier",
}

_item_identifier_name_convert = {
    "ASIN": "asin",
    "ItemCondition": "item_condition",
    "MarketplaceId": "marketplace_id",
    "SellerSKU": "seller_sku",
}

_lowest_price_type_name_convert = {
    "LandedPrice": "landed_price",
    "ListingPrice": "listing_price",
    "Points": "points",
    "Shipping": "shipping",
    "condition": "condition",
    "fulfillmentChannel": "fulfillment_channel",
    "offerType": "offer_type",
    "quantityDiscountType": "quantity_discount_type",
    "quantityTier": "quantity_tier",
}

_money_type_name_convert = {
    "Amount": "amount",
    "CurrencyCode": "currency_code",
}

_offer_count_type_name_convert = {
    "OfferCount": "offer_count",
    "condition": "condition",
    "fulfillmentChannel": "fulfillment_channel",
}

_offer_customer_type_name_convert = {}

_offer_detail_name_convert = {
    "ConditionNotes": "condition_notes",
    "IsBuyBoxWinner": "is_buy_box_winner",
    "IsFeaturedMerchant": "is_featured_merchant",
    "IsFulfilledByAmazon": "is_fulfilled_by_amazon",
    "ListingPrice": "listing_price",
    "MyOffer": "my_offer",
    "Points": "points",
    "PrimeInformation": "prime_information",
    "SellerFeedbackRating": "seller_feedback_rating",
    "SellerId": "seller_id",
    "Shipping": "shipping",
    "ShippingTime": "shipping_time",
    "ShipsFrom": "ships_from",
    "SubCondition": "sub_condition",
    "offerType": "offer_type",
    "quantityDiscountPrices": "quantity_discount_prices",
}

_offer_listing_count_type_name_convert = {
    "Count": "count",
    "condition": "condition",
}

_offer_type_name_convert = {
    "BuyingPrice": "buying_price",
    "FulfillmentChannel": "fulfillment_channel",
    "ItemCondition": "item_condition",
    "ItemSubCondition": "item_sub_condition",
    "RegularPrice": "regular_price",
    "SellerSKU": "seller_sku",
    "businessPrice": "business_price",
    "offerType": "offer_type",
    "quantityDiscountPrices": "quantity_discount_prices",
}

_points_name_convert = {
    "PointsMonetaryValue": "points_monetary_value",
    "PointsNumber": "points_number",
}

_price_name_convert = {
    "ASIN": "asin",
    "Product": "product",
    "SellerSKU": "seller_sku",
    "status": "status",
}

_price_type_name_convert = {
    "LandedPrice": "landed_price",
    "ListingPrice": "listing_price",
    "Points": "points",
    "Shipping": "shipping",
}

_prime_information_type_name_convert = {
    "IsNationalPrime": "is_national_prime",
    "IsPrime": "is_prime",
}

_product_name_convert = {
    "AttributeSets": "attribute_sets",
    "CompetitivePricing": "competitive_pricing",
    "Identifiers": "identifiers",
    "Offers": "offers",
    "Relationships": "relationships",
    "SalesRankings": "sales_rankings",
}

_quantity_discount_price_type_name_convert = {
    "listingPrice": "listing_price",
    "quantityDiscountType": "quantity_discount_type",
    "quantityTier": "quantity_tier",
}

_quantity_discount_type_name_convert = {}

_relationship_list_item_name_convert = {}

_sales_rank_type_name_convert = {
    "ProductCategoryId": "product_category_id",
    "Rank": "rank",
}

_seller_feedback_type_name_convert = {
    "FeedbackCount": "feedback_count",
    "SellerPositiveFeedbackRating": "seller_positive_feedback_rating",
}

_seller_skuidentifier_name_convert = {
    "MarketplaceId": "marketplace_id",
    "SellerId": "seller_id",
    "SellerSKU": "seller_sku",
}

_ships_from_type_name_convert = {
    "Country": "country",
    "State": "state",
}

_summary_name_convert = {
    "BuyBoxEligibleOffers": "buy_box_eligible_offers",
    "BuyBoxPrices": "buy_box_prices",
    "CompetitivePriceThreshold": "competitive_price_threshold",
    "ListPrice": "list_price",
    "LowestPrices": "lowest_prices",
    "NumberOfOffers": "number_of_offers",
    "OffersAvailableTime": "offers_available_time",
    "SalesRankings": "sales_rankings",
    "SuggestedLowerPricePlusShipping": "suggested_lower_price_plus_shipping",
    "TotalOfferCount": "total_offer_count",
}


class ProductPricingV0Client(BaseClient):
    def get_competitive_pricing(
        self,
        marketplace_id: str,
        item_type: Union[Literal["Asin"], Literal["Sku"]],
        asins: List[str] = None,
        skus: List[str] = None,
        customer_type: Union[Literal["Consumer"], Literal["Business"]] = None,
    ) -> Union[GetPricingResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_competitive_pricing_params,
            self._get_competitive_pricing_responses,
        )
        return response

    _get_competitive_pricing_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("Asins", "query"),
        ("Skus", "query"),
        ("ItemType", "query"),
        ("CustomerType", "query"),
    )

    _get_competitive_pricing_responses = {
        200: GetPricingResponse,
        400: GetPricingResponse,
        401: GetPricingResponse,
        403: GetPricingResponse,
        404: GetPricingResponse,
        429: GetPricingResponse,
        500: GetPricingResponse,
        503: GetPricingResponse,
    }

    def get_item_offers(
        self,
        marketplace_id: str,
        item_condition: Union[
            Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
        ],
        asin: str,
        customer_type: Union[Literal["Consumer"], Literal["Business"]] = None,
    ) -> Union[GetOffersResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_item_offers_params,
            self._get_item_offers_responses,
        )
        return response

    _get_item_offers_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ItemCondition", "query"),
        ("Asin", "path"),
        ("CustomerType", "query"),
    )

    _get_item_offers_responses = {
        200: GetOffersResponse,
        400: GetOffersResponse,
        401: GetOffersResponse,
        403: GetOffersResponse,
        404: GetOffersResponse,
        429: GetOffersResponse,
        500: GetOffersResponse,
        503: GetOffersResponse,
    }

    def get_listing_offers(
        self,
        marketplace_id: str,
        item_condition: Union[
            Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
        ],
        seller_sku: str,
        customer_type: Union[Literal["Consumer"], Literal["Business"]] = None,
    ) -> Union[GetOffersResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_listing_offers_params,
            self._get_listing_offers_responses,
        )
        return response

    _get_listing_offers_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ItemCondition", "query"),
        ("SellerSKU", "path"),
        ("CustomerType", "query"),
    )

    _get_listing_offers_responses = {
        200: GetOffersResponse,
        400: GetOffersResponse,
        401: GetOffersResponse,
        403: GetOffersResponse,
        404: GetOffersResponse,
        429: GetOffersResponse,
        500: GetOffersResponse,
        503: GetOffersResponse,
    }

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
    ) -> Union[GetPricingResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_pricing_params,
            self._get_pricing_responses,
        )
        return response

    _get_pricing_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("Asins", "query"),
        ("Skus", "query"),
        ("ItemType", "query"),
        ("ItemCondition", "query"),
        ("OfferType", "query"),
    )

    _get_pricing_responses = {
        200: GetPricingResponse,
        400: GetPricingResponse,
        401: GetPricingResponse,
        403: GetPricingResponse,
        404: GetPricingResponse,
        429: GetPricingResponse,
        500: GetPricingResponse,
        503: GetPricingResponse,
    }
