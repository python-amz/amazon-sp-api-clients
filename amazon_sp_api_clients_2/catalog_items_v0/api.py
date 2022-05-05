"""
Selling Partner API for Catalog Items
=============================================================================================
The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class CatalogItemsV0Client(BaseClient):
    def list_catalog_items(
        self,
        Marketplace_id: str,
        Query: str = None,
        Query_context_id: str = None,
        Seller_sku: str = None,
        UPC: str = None,
        EAN: str = None,
        ISBN: str = None,
        JAN: str = None,
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
        path_parameters = {}

        url = "/catalog/v0/items".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        if Query is not None:
            query_parameters["Query"] = Query

        if Query_context_id is not None:
            query_parameters["QueryContextId"] = Query_context_id

        if Seller_sku is not None:
            query_parameters["SellerSKU"] = Seller_sku

        if UPC is not None:
            query_parameters["UPC"] = UPC

        if EAN is not None:
            query_parameters["EAN"] = EAN

        if ISBN is not None:
            query_parameters["ISBN"] = ISBN

        if JAN is not None:
            query_parameters["JAN"] = JAN

    def get_catalog_item(
        self,
        Marketplace_id: str,
        asin: str,
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
        path_parameters = {}

        path_parameters["asin"] = asin

        url = "/catalog/v0/items/{asin}".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

    def list_catalog_categories(
        self,
        Marketplace_id: str,
        ASIN: str = None,
        Seller_sku: str = None,
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
        path_parameters = {}

        url = "/catalog/v0/categories".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        if ASIN is not None:
            query_parameters["ASIN"] = ASIN

        if Seller_sku is not None:
            query_parameters["SellerSKU"] = Seller_sku
