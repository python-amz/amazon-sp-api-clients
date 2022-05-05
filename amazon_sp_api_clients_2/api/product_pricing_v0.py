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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    quantity_tier: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    landed_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    listing_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    points: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/Points'}
    shipping: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OfferCustomerType'}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/QuantityDiscountType'}
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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    belongs_to_requester: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    quantity_tier: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    subcondition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/PriceType'}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OfferCustomerType'}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/QuantityDiscountType'}
    pass


@attrs.define
class CompetitivePricingType:

    competitive_prices: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/CompetitivePriceList'}
    number_of_offer_listings: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/NumberOfOfferListingsList'}
    trade_in_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class ConditionType:

    pass


@attrs.define
class DetailedShippingTimeType:

    availability_type: Union[Literal["NOW"], Literal["FUTURE_WITHOUT_DATE"], Literal["FUTURE_WITH_DATE"]]
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'enum': ['NOW', 'FUTURE_WITHOUT_DATE', 'FUTURE_WITH_DATE']}
    available_date: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    maximum_hours: int
    # {'type': 'integer', 'schema_format': 'int64', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    minimum_hours: int
    # {'type': 'integer', 'schema_format': 'int64', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

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
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/GetOffersResult'}
    pass


@attrs.define
class GetOffersResult:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    status: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    identifier: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ItemIdentifier'}
    item_condition: Union[
        Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ConditionType'}
    offers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OfferDetailList'}
    summary: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/Summary'}
    pass


@attrs.define
class GetPricingResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ErrorList'}
    payload: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/PriceList'}
    pass


@attrs.define
class IdentifierType:

    marketplace_asin: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ASINIdentifier'}
    skuidentifier: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/SellerSKUIdentifier'}
    pass


@attrs.define
class ItemIdentifier:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    item_condition: Union[
        Literal["New"], Literal["Used"], Literal["Collectible"], Literal["Refurbished"], Literal["Club"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ConditionType'}
    pass


@attrs.define
class LowestPriceType:

    condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    fulfillment_channel: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    quantity_tier: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    landed_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    listing_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    points: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/Points'}
    shipping: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OfferCustomerType'}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/QuantityDiscountType'}
    pass


@attrs.define
class LowestPrices:

    pass


@attrs.define
class MoneyType:

    amount: Union[float, int]
    # {'type': 'number', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    currency_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

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
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    fulfillment_channel: Union[Literal["Amazon"], Literal["Merchant"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/FulfillmentChannelType'}
    pass


@attrs.define
class OfferCustomerType:

    pass


@attrs.define
class OfferDetail:

    condition_notes: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    is_buy_box_winner: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    is_featured_merchant: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    is_fulfilled_by_amazon: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    my_offer: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    sub_condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    quantity_discount_prices: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/QuantityDiscountPriceType'), 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    listing_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    points: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/Points'}
    prime_information: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/PrimeInformationType'}
    seller_feedback_rating: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/SellerFeedbackType'}
    shipping: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    shipping_time: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/DetailedShippingTimeType'}
    ships_from: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/ShipsFromType'}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OfferCustomerType'}
    pass


@attrs.define
class OfferDetailList:

    pass


@attrs.define
class OfferListingCountType:

    count: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class OfferType:

    fulfillment_channel: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    item_condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    item_sub_condition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    quantity_discount_prices: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/QuantityDiscountPriceType'), 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    buying_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/PriceType'}
    regular_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    business_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    offer_type: Union[Literal["B2C"], Literal["B2B"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OfferCustomerType'}
    pass


@attrs.define
class OffersList:

    pass


@attrs.define
class Points:

    points_number: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    points_monetary_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class Price:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    status: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    product: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/Product'}
    pass


@attrs.define
class PriceList:

    pass


@attrs.define
class PriceType:

    landed_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    listing_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    points: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/Points'}
    shipping: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class PrimeInformationType:

    is_national_prime: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    is_prime: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class Product:

    attribute_sets: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/AttributeSetList'}
    competitive_pricing: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/CompetitivePricingType'}
    identifiers: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/IdentifierType'}
    offers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/OffersList'}
    relationships: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/RelationshipList'}
    sales_rankings: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/SalesRankList'}
    pass


@attrs.define
class QuantityDiscountPriceType:

    quantity_tier: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    listing_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    quantity_discount_type: Union[Literal["QUANTITY_DISCOUNT"]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/QuantityDiscountType'}
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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    rank: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class SellerFeedbackType:

    feedback_count: int
    # {'type': 'integer', 'schema_format': 'int64', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_positive_feedback_rating: Union[float, int]
    # {'type': 'number', 'schema_format': 'double', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class ShipsFromType:

    country: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    state: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    pass


@attrs.define
class Summary:

    offers_available_time: str
    # {'type': 'string', 'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}
    total_offer_count: int
    # {'type': 'integer', 'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>}

    buy_box_eligible_offers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/BuyBoxEligibleOffers'}
    buy_box_prices: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/BuyBoxPrices'}
    competitive_price_threshold: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    list_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
    lowest_prices: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/LowestPrices'}
    number_of_offers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/NumberOfOffers'}
    sales_rankings: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/SalesRankList'}
    suggested_lower_price_plus_shipping: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000014A97A153F0>, 'ref': '#/components/schemas/MoneyType'}
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
