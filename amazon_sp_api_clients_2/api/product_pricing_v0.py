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

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    pass


@attrs.define
class AttributeSetList:

    pass


@attrs.define
class BuyBoxEligibleOffers:

    pass


@attrs.define
class BuyBoxPriceType:

    condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    quantity_tier: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    landed_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    listing_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    points: dict[str, Any]
    # {'ref': '#/components/schemas/Points', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    shipping: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'ref': '#/components/schemas/OfferCustomerType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'ref': '#/components/schemas/QuantityDiscountType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class BuyBoxPrices:

    pass


@attrs.define
class CompetitivePriceList:

    pass


@attrs.define
class CompetitivePriceType:

    competitive_price_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    belongs_to_requester: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}
    condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    quantity_tier: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    subcondition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    price: dict[str, Any]
    # {'ref': '#/components/schemas/PriceType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'ref': '#/components/schemas/OfferCustomerType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'ref': '#/components/schemas/QuantityDiscountType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class CompetitivePricingType:

    competitive_prices: list[dict[str, Any]]
    # {'ref': '#/components/schemas/CompetitivePriceList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    number_of_offer_listings: list[dict[str, Any]]
    # {'ref': '#/components/schemas/NumberOfOfferListingsList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    trade_in_value: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class ConditionType:

    pass


@attrs.define
class DetailedShippingTimeType:

    availability_type: Union[Literal["NOW"], Literal["FUTURE_WITHOUT_DATE"], Literal["FUTURE_WITH_DATE"]]
    # {'enum': ['NOW', 'FUTURE_WITHOUT_DATE', 'FUTURE_WITH_DATE'], 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    available_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    maximum_hours: int
    # {'schema_format': 'int64', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}
    minimum_hours: int
    # {'schema_format': 'int64', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FulfillmentChannelType:

    pass


@attrs.define
class GetOffersResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetOffersResult', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class GetOffersResult:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    status: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    identifier: dict[str, Any]
    # {'ref': '#/components/schemas/ItemIdentifier', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    item_condition: Union[
        Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
    ]
    # {'ref': '#/components/schemas/ConditionType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/OfferDetailList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    summary: dict[str, Any]
    # {'ref': '#/components/schemas/Summary', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class GetPricingResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    payload: list[dict[str, Any]]
    # {'ref': '#/components/schemas/PriceList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class IdentifierType:

    marketplace_asin: dict[str, Any]
    # {'ref': '#/components/schemas/ASINIdentifier', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    skuidentifier: dict[str, Any]
    # {'ref': '#/components/schemas/SellerSKUIdentifier', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class ItemIdentifier:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    item_condition: Union[
        Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
    ]
    # {'ref': '#/components/schemas/ConditionType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class LowestPriceType:

    condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    fulfillment_channel: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    quantity_tier: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}

    landed_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    listing_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    points: dict[str, Any]
    # {'ref': '#/components/schemas/Points', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    shipping: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'ref': '#/components/schemas/OfferCustomerType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'ref': '#/components/schemas/QuantityDiscountType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class LowestPrices:

    pass


@attrs.define
class MoneyType:

    amount: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'number'}
    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    pass


@attrs.define
class NumberOfOfferListingsList:

    pass


@attrs.define
class NumberOfOffers:

    pass


@attrs.define
class OfferCountType:

    offer_count: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}
    condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    fulfillment_channel: Union[Literal["Amazon"], Literal["Merchant"]]
    # {'ref': '#/components/schemas/FulfillmentChannelType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class OfferCustomerType:

    pass


@attrs.define
class OfferDetail:

    condition_notes: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    is_buy_box_winner: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}
    is_featured_merchant: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}
    is_fulfilled_by_amazon: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}
    my_offer: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    sub_condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    quantity_discount_prices: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/QuantityDiscountPriceType'), 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'array'}

    listing_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    points: dict[str, Any]
    # {'ref': '#/components/schemas/Points', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    prime_information: dict[str, Any]
    # {'ref': '#/components/schemas/PrimeInformationType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    seller_feedback_rating: dict[str, Any]
    # {'ref': '#/components/schemas/SellerFeedbackType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    shipping: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    shipping_time: dict[str, Any]
    # {'ref': '#/components/schemas/DetailedShippingTimeType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    ships_from: dict[str, Any]
    # {'ref': '#/components/schemas/ShipsFromType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'ref': '#/components/schemas/OfferCustomerType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class OfferDetailList:

    pass


@attrs.define
class OfferListingCountType:

    count: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}
    condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    pass


@attrs.define
class OfferType:

    fulfillment_channel: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    item_condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    item_sub_condition: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    quantity_discount_prices: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/QuantityDiscountPriceType'), 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'array'}

    buying_price: dict[str, Any]
    # {'ref': '#/components/schemas/PriceType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    regular_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    business_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'ref': '#/components/schemas/OfferCustomerType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class OffersList:

    pass


@attrs.define
class Points:

    points_number: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}

    points_monetary_value: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class Price:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    status: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    product: dict[str, Any]
    # {'ref': '#/components/schemas/Product', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class PriceList:

    pass


@attrs.define
class PriceType:

    landed_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    listing_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    points: dict[str, Any]
    # {'ref': '#/components/schemas/Points', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    shipping: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class PrimeInformationType:

    is_national_prime: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}
    is_prime: bool
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'boolean'}

    pass


@attrs.define
class Product:

    attribute_sets: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AttributeSetList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    competitive_pricing: dict[str, Any]
    # {'ref': '#/components/schemas/CompetitivePricingType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    identifiers: dict[str, Any]
    # {'ref': '#/components/schemas/IdentifierType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    offers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/OffersList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    relationships: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RelationshipList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    sales_rankings: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SalesRankList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    pass


@attrs.define
class QuantityDiscountPriceType:

    quantity_tier: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}

    listing_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'ref': '#/components/schemas/QuantityDiscountType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
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

    product_category_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    rank: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}

    pass


@attrs.define
class SellerFeedbackType:

    feedback_count: int
    # {'schema_format': 'int64', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}
    seller_positive_feedback_rating: Union[float, int]
    # {'schema_format': 'double', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'number'}

    pass


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    pass


@attrs.define
class ShipsFromType:

    country: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    state: str
    # {'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}

    pass


@attrs.define
class Summary:

    offers_available_time: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'string'}
    total_offer_count: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>, 'type': 'integer'}

    buy_box_eligible_offers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/BuyBoxEligibleOffers', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    buy_box_prices: list[dict[str, Any]]
    # {'ref': '#/components/schemas/BuyBoxPrices', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    competitive_price_threshold: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    list_price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    lowest_prices: list[dict[str, Any]]
    # {'ref': '#/components/schemas/LowestPrices', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    number_of_offers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/NumberOfOffers', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    sales_rankings: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SalesRankList', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
    suggested_lower_price_plus_shipping: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x0000017DF3CDB880>}
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
