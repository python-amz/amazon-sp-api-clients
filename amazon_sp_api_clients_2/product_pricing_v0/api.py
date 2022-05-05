"""
Selling Partner API for Pricing
=============================================================================================
The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ProductPricingV0Client(BaseClient):
    def get_pricing(
        self,
        marketplace_id: str,
        asins: list[str] = None,
        skus: list[str] = None,
        item_type: str,
        item_condition: str = None,
        offer_type: str = None,
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
        path_parameters = {}
        url = "/products/pricing/v0/price"
        params = (  # name, param in, value, required
            ("MarketplaceId", "query", marketplace_id, True),
            ("Asins", "query", asins, False),
            ("Skus", "query", skus, False),
            ("ItemType", "query", item_type, True),
            ("ItemCondition", "query", item_condition, False),
            ("OfferType", "query", offer_type, False),
        )

    def get_competitive_pricing(
        self,
        marketplace_id: str,
        asins: list[str] = None,
        skus: list[str] = None,
        item_type: str,
        customer_type: str = None,
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
        path_parameters = {}
        url = "/products/pricing/v0/competitivePrice"
        params = (  # name, param in, value, required
            ("MarketplaceId", "query", marketplace_id, True),
            ("Asins", "query", asins, False),
            ("Skus", "query", skus, False),
            ("ItemType", "query", item_type, True),
            ("CustomerType", "query", customer_type, False),
        )

    def get_listing_offers(
        self,
        marketplace_id: str,
        item_condition: str,
        seller_sku: str,
        customer_type: str = None,
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
        path_parameters = {}
        url = "/products/pricing/v0/listings/{SellerSKU}/offers"
        params = (  # name, param in, value, required
            ("MarketplaceId", "query", marketplace_id, True),
            ("ItemCondition", "query", item_condition, True),
            ("SellerSKU", "path", seller_sku, True),
            ("CustomerType", "query", customer_type, False),
        )

    def get_item_offers(
        self,
        marketplace_id: str,
        item_condition: str,
        asin: str,
        customer_type: str = None,
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
        path_parameters = {}
        url = "/products/pricing/v0/items/{Asin}/offers"
        params = (  # name, param in, value, required
            ("MarketplaceId", "query", marketplace_id, True),
            ("ItemCondition", "query", item_condition, True),
            ("Asin", "path", asin, True),
            ("CustomerType", "query", customer_type, False),
        )
