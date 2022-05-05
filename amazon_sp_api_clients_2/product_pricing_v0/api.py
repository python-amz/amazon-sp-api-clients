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
        Marketplace_id: str,
        Asins: list[str] = None,
        Skus: list[str] = None,
        Item_type: str,
        Item_condition: str = None,
        Offer_type: str = None,
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
            Marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            Asins: A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            Skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            Item_type: Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.
            Item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            Offer_type: Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.
        """
        path_parameters = {}

        url = "/products/pricing/v0/price".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        if Asins is not None:
            query_parameters["Asins"] = Asins

        if Skus is not None:
            query_parameters["Skus"] = Skus

        query_parameters["ItemType"] = Item_type

        if Item_condition is not None:
            query_parameters["ItemCondition"] = Item_condition

        if Offer_type is not None:
            query_parameters["OfferType"] = Offer_type

    def get_competitive_pricing(
        self,
        Marketplace_id: str,
        Asins: list[str] = None,
        Skus: list[str] = None,
        Item_type: str,
        Customer_type: str = None,
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
            Marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            Asins: A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            Skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            Item_type: Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.
            Customer_type: Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.
        """
        path_parameters = {}

        url = "/products/pricing/v0/competitivePrice".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        if Asins is not None:
            query_parameters["Asins"] = Asins

        if Skus is not None:
            query_parameters["Skus"] = Skus

        query_parameters["ItemType"] = Item_type

        if Customer_type is not None:
            query_parameters["CustomerType"] = Customer_type

    def get_listing_offers(
        self,
        Marketplace_id: str,
        Item_condition: str,
        Seller_sku: str,
        Customer_type: str = None,
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
            Marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            Item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            Seller_sku: Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
            Customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
        """
        path_parameters = {}

        path_parameters["SellerSKU"] = Seller_sku

        url = "/products/pricing/v0/listings/{SellerSKU}/offers".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        query_parameters["ItemCondition"] = Item_condition

        if Customer_type is not None:
            query_parameters["CustomerType"] = Customer_type

    def get_item_offers(
        self,
        Marketplace_id: str,
        Item_condition: str,
        Asin: str,
        Customer_type: str = None,
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
            Marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            Item_condition: Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            Asin: The Amazon Standard Identification Number (ASIN) of the item.
            Customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
        """
        path_parameters = {}

        path_parameters["Asin"] = Asin

        url = "/products/pricing/v0/items/{Asin}/offers".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        query_parameters["ItemCondition"] = Item_condition

        if Customer_type is not None:
            query_parameters["CustomerType"] = Customer_type
