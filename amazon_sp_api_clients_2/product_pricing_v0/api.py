"""
Selling Partner API for Pricing
=============================================================================================
The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient


class ProductPricingV0Client(BaseClient):
    def get_pricing(
        self,
        Marketplace_id,
        Asins=None,
        Skus=None,
        Item_type,
        Item_condition=None,
        Offer_type=None,
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
        url = "/products/pricing/v0/price"

    def get_competitive_pricing(
        self,
        Marketplace_id,
        Asins=None,
        Skus=None,
        Item_type,
        Customer_type=None,
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
        url = "/products/pricing/v0/competitivePrice"

    def get_listing_offers(
        self,
        Marketplace_id,
        Item_condition,
        Seller_sku,
        Customer_type=None,
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
        url = "/products/pricing/v0/listings/{SellerSKU}/offers"

    def get_item_offers(
        self,
        Marketplace_id,
        Item_condition,
        Asin,
        Customer_type=None,
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
        url = "/products/pricing/v0/items/{Asin}/offers"
