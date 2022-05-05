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


@attrs.define
class ASINIdentifier:

    asin: str = attrs.field()
    marketplace_id: str = attrs.field()

    pass


@attrs.define
class AttributeSetList:

    pass


@attrs.define
class BuyBoxEligibleOffers:

    pass


@attrs.define
class BuyBoxPriceType:

    condition: str = attrs.field()
    quantity_tier: int = attrs.field()
    # {'schema_format': 'int32'}
    seller_id: str = attrs.field()

    landed_price: "MoneyType" = attrs.field()
    listing_price: "MoneyType" = attrs.field()
    points: "Points" = attrs.field()
    shipping: "MoneyType" = attrs.field()
    offer_type: "OfferCustomerType" = attrs.field()
    quantity_discount_type: "QuantityDiscountType" = attrs.field()
    pass


@attrs.define
class BuyBoxPrices:

    pass


@attrs.define
class CompetitivePriceList:

    pass


@attrs.define
class CompetitivePriceType:

    competitive_price_id: str = attrs.field()
    belongs_to_requester: bool = attrs.field()
    condition: str = attrs.field()
    quantity_tier: int = attrs.field()
    # {'schema_format': 'int32'}
    seller_id: str = attrs.field()
    subcondition: str = attrs.field()

    price: "PriceType" = attrs.field()
    offer_type: "OfferCustomerType" = attrs.field()
    quantity_discount_type: "QuantityDiscountType" = attrs.field()
    pass


@attrs.define
class CompetitivePricingType:

    competitive_prices: "CompetitivePriceList" = attrs.field()
    number_of_offer_listings: "NumberOfOfferListingsList" = attrs.field()
    trade_in_value: "MoneyType" = attrs.field()
    pass


@attrs.define
class ConditionType:

    pass


@attrs.define
class DetailedShippingTimeType:

    availability_type: Union[
        Literal["NOW"], Literal["FUTURE_WITHOUT_DATE"], Literal["FUTURE_WITH_DATE"]
    ] = attrs.field()
    available_date: str = attrs.field()
    maximum_hours: int = attrs.field()
    # {'schema_format': 'int64'}
    minimum_hours: int = attrs.field()
    # {'schema_format': 'int64'}

    pass


@attrs.define
class Error:

    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FulfillmentChannelType:

    pass


@attrs.define
class GetOffersResponse:

    errors: "ErrorList" = attrs.field()
    payload: "GetOffersResult" = attrs.field()
    pass


@attrs.define
class GetOffersResult:

    asin: str = attrs.field()
    marketplace_id: str = attrs.field()
    sku: str = attrs.field()
    status: str = attrs.field()

    identifier: "ItemIdentifier" = attrs.field()
    item_condition: "ConditionType" = attrs.field()
    offers: "OfferDetailList" = attrs.field()
    summary: "Summary" = attrs.field()
    pass


@attrs.define
class GetPricingResponse:

    errors: "ErrorList" = attrs.field()
    payload: "PriceList" = attrs.field()
    pass


@attrs.define
class IdentifierType:

    marketplace_asin: "ASINIdentifier" = attrs.field()
    skuidentifier: "SellerSKUIdentifier" = attrs.field()
    pass


@attrs.define
class ItemIdentifier:

    asin: str = attrs.field()
    marketplace_id: str = attrs.field()
    seller_sku: str = attrs.field()

    item_condition: "ConditionType" = attrs.field()
    pass


@attrs.define
class LowestPriceType:

    condition: str = attrs.field()
    fulfillment_channel: str = attrs.field()
    quantity_tier: int = attrs.field()
    # {'schema_format': 'int32'}

    landed_price: "MoneyType" = attrs.field()
    listing_price: "MoneyType" = attrs.field()
    points: "Points" = attrs.field()
    shipping: "MoneyType" = attrs.field()
    offer_type: "OfferCustomerType" = attrs.field()
    quantity_discount_type: "QuantityDiscountType" = attrs.field()
    pass


@attrs.define
class LowestPrices:

    pass


@attrs.define
class MoneyType:

    amount: Union[float, int] = attrs.field()
    currency_code: str = attrs.field()

    pass


@attrs.define
class NumberOfOfferListingsList:

    pass


@attrs.define
class NumberOfOffers:

    pass


@attrs.define
class OfferCountType:

    offer_count: int = attrs.field()
    # {'schema_format': 'int32'}
    condition: str = attrs.field()

    fulfillment_channel: "FulfillmentChannelType" = attrs.field()
    pass


@attrs.define
class OfferCustomerType:

    pass


@attrs.define
class OfferDetail:

    condition_notes: str = attrs.field()
    is_buy_box_winner: bool = attrs.field()
    is_featured_merchant: bool = attrs.field()
    is_fulfilled_by_amazon: bool = attrs.field()
    my_offer: bool = attrs.field()
    seller_id: str = attrs.field()
    sub_condition: str = attrs.field()
    quantity_discount_prices: list["QuantityDiscountPriceType"] = attrs.field()

    listing_price: "MoneyType" = attrs.field()
    points: "Points" = attrs.field()
    prime_information: "PrimeInformationType" = attrs.field()
    seller_feedback_rating: "SellerFeedbackType" = attrs.field()
    shipping: "MoneyType" = attrs.field()
    shipping_time: "DetailedShippingTimeType" = attrs.field()
    ships_from: "ShipsFromType" = attrs.field()
    offer_type: "OfferCustomerType" = attrs.field()
    pass


@attrs.define
class OfferDetailList:

    pass


@attrs.define
class OfferListingCountType:

    count: int = attrs.field()
    # {'schema_format': 'int32'}
    condition: str = attrs.field()

    pass


@attrs.define
class OfferType:

    fulfillment_channel: str = attrs.field()
    item_condition: str = attrs.field()
    item_sub_condition: str = attrs.field()
    seller_sku: str = attrs.field()
    quantity_discount_prices: list["QuantityDiscountPriceType"] = attrs.field()

    buying_price: "PriceType" = attrs.field()
    regular_price: "MoneyType" = attrs.field()
    business_price: "MoneyType" = attrs.field()
    offer_type: "OfferCustomerType" = attrs.field()
    pass


@attrs.define
class OffersList:

    pass


@attrs.define
class Points:

    points_number: int = attrs.field()
    # {'schema_format': 'int32'}

    points_monetary_value: "MoneyType" = attrs.field()
    pass


@attrs.define
class Price:

    asin: str = attrs.field()
    seller_sku: str = attrs.field()
    status: str = attrs.field()

    product: "Product" = attrs.field()
    pass


@attrs.define
class PriceList:

    pass


@attrs.define
class PriceType:

    landed_price: "MoneyType" = attrs.field()
    listing_price: "MoneyType" = attrs.field()
    points: "Points" = attrs.field()
    shipping: "MoneyType" = attrs.field()
    pass


@attrs.define
class PrimeInformationType:

    is_national_prime: bool = attrs.field()
    is_prime: bool = attrs.field()

    pass


@attrs.define
class Product:

    attribute_sets: "AttributeSetList" = attrs.field()
    competitive_pricing: "CompetitivePricingType" = attrs.field()
    identifiers: "IdentifierType" = attrs.field()
    offers: "OffersList" = attrs.field()
    relationships: "RelationshipList" = attrs.field()
    sales_rankings: "SalesRankList" = attrs.field()
    pass


@attrs.define
class QuantityDiscountPriceType:

    quantity_tier: int = attrs.field()
    # {'schema_format': 'int32'}

    listing_price: "MoneyType" = attrs.field()
    quantity_discount_type: "QuantityDiscountType" = attrs.field()
    pass


@attrs.define
class QuantityDiscountType:

    pass


@attrs.define
class RelationshipList:

    pass


@attrs.define
class SalesRankList:

    pass


@attrs.define
class SalesRankType:

    product_category_id: str = attrs.field()
    rank: int = attrs.field()
    # {'schema_format': 'int32'}

    pass


@attrs.define
class SellerFeedbackType:

    feedback_count: int = attrs.field()
    # {'schema_format': 'int64'}
    seller_positive_feedback_rating: Union[float, int] = attrs.field()
    # {'schema_format': 'double'}

    pass


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str = attrs.field()
    seller_id: str = attrs.field()
    seller_sku: str = attrs.field()

    pass


@attrs.define
class ShipsFromType:

    country: str = attrs.field()
    state: str = attrs.field()

    pass


@attrs.define
class Summary:

    offers_available_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    total_offer_count: int = attrs.field()
    # {'schema_format': 'int32'}

    buy_box_eligible_offers: "BuyBoxEligibleOffers" = attrs.field()
    buy_box_prices: "BuyBoxPrices" = attrs.field()
    competitive_price_threshold: "MoneyType" = attrs.field()
    list_price: "MoneyType" = attrs.field()
    lowest_prices: "LowestPrices" = attrs.field()
    number_of_offers: "NumberOfOffers" = attrs.field()
    sales_rankings: "SalesRankList" = attrs.field()
    suggested_lower_price_plus_shipping: "MoneyType" = attrs.field()
    pass


class ProductPricingV0Client(BaseClient):
    def get_competitive_pricing(
        self,
        marketplace_id: str,
        item_type: Union[Literal["Asin"], Literal["Sku"]],
        asins: list[str] = None,
        skus: list[str] = None,
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
        asins: list[str] = None,
        skus: list[str] = None,
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
