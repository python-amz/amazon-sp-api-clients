"""
Selling Partner API for Catalog Items
=============================================================================================
The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient


class CatalogItemsV0Client(BaseClient):
    def list_catalog_items(
        self,
        Marketplace_id,
        Query=None,
        Query_context_id=None,
        Seller_sku=None,
        UPC=None,
        EAN=None,
        ISBN=None,
        JAN=None,
    ):
        """
        Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value.

        MarketplaceId is always required. At least one of Query, SellerSKU, UPC, EAN, ISBN, JAN is also required.

        This operation returns a maximum of ten products and does not return non-buyable products.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 6 | 40 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Marketplace_id: A marketplace identifier. Specifies the marketplace for which items are returned.
            Query: Keyword(s) to use to search for items in the catalog. Example: 'harry potter books'.
            Query_context_id: An identifier for the context within which the given search will be performed. A marketplace might provide mechanisms for constraining a search to a subset of potential items. For example, the retail marketplace allows queries to be constrained to a specific category. The QueryContextId parameter specifies such a subset. If it is omitted, the search will be performed using the default context for the marketplace, which will typically contain the largest set of items.
            Seller_sku: Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
            UPC: A 12-digit bar code used for retail packaging.
            EAN: A European article number that uniquely identifies the catalog item, manufacturer, and its attributes.
            ISBN: The unique commercial book identifier used to identify books internationally.
            JAN: A Japanese article number that uniquely identifies the product, manufacturer, and its attributes.
        """
        url = "/catalog/v0/items"

    def get_catalog_item(
        self,
        Marketplace_id,
        asin,
    ):
        """
        Returns a specified item and its attributes.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 2 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Marketplace_id: A marketplace identifier. Specifies the marketplace for the item.
            asin: The Amazon Standard Identification Number (ASIN) of the item.
        """
        url = "/catalog/v0/items/{asin}"

    def list_catalog_categories(
        self,
        Marketplace_id,
        ASIN=None,
        Seller_sku=None,
    ):
        """
        Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1 | 40 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Marketplace_id: A marketplace identifier. Specifies the marketplace for the item.
            ASIN: The Amazon Standard Identification Number (ASIN) of the item.
            Seller_sku: Used to identify items in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
        """
        url = "/catalog/v0/categories"
