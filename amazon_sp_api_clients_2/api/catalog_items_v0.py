"""
Selling Partner API for Catalog Items
=============================================================================================

The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class ListCatalogItemsResponse:
    pass


@attrs.define
class ListMatchingItemsResponse:
    pass


@attrs.define
class ItemList:
    pass


@attrs.define
class GetCatalogItemResponse:
    pass


@attrs.define
class Item:
    pass


@attrs.define
class IdentifierType:
    pass


@attrs.define
class ASINIdentifier:
    pass


@attrs.define
class SellerSKUIdentifier:
    pass


@attrs.define
class AttributeSetList:
    pass


@attrs.define
class AttributeSetListType:
    pass


@attrs.define
class DecimalWithUnits:
    pass


@attrs.define
class CreatorType:
    pass


@attrs.define
class DimensionType:
    pass


@attrs.define
class LanguageType:
    pass


@attrs.define
class Image:
    pass


@attrs.define
class Price:
    pass


@attrs.define
class RelationshipList:
    pass


@attrs.define
class RelationshipType:
    pass


@attrs.define
class SalesRankList:
    pass


@attrs.define
class SalesRankType:
    pass


@attrs.define
class ListCatalogCategoriesResponse:
    pass


@attrs.define
class ListOfCategories:
    pass


@attrs.define
class Categories:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class Error:
    pass


class CatalogItemsV0Client(BaseClient):
    def get_catalog_item(
        self,
        marketplace_id: str,
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
            marketplace_id: A marketplace identifier. Specifies the marketplace for the item.
            asin: The Amazon Standard Identification Number (ASIN) of the item.
        """
        url = "/catalog/v0/items/{asin}"
        values = (
            marketplace_id,
            asin,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_catalog_item_params)
        return response

    _get_catalog_item_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("asin", "path"),
    )

    def list_catalog_categories(
        self,
        marketplace_id: str,
        asin: str = None,
        seller_sku: str = None,
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
            marketplace_id: A marketplace identifier. Specifies the marketplace for the item.
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            seller_sku: Used to identify items in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
        """
        url = "/catalog/v0/categories"
        values = (
            marketplace_id,
            asin,
            seller_sku,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_catalog_categories_params)
        return response

    _list_catalog_categories_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ASIN", "query"),
        ("SellerSKU", "query"),
    )

    def list_catalog_items(
        self,
        marketplace_id: str,
        query: str = None,
        query_context_id: str = None,
        seller_sku: str = None,
        upc: str = None,
        ean: str = None,
        isbn: str = None,
        jan: str = None,
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
            marketplace_id: A marketplace identifier. Specifies the marketplace for which items are returned.
            query: Keyword(s) to use to search for items in the catalog. Example: 'harry potter books'.
            query_context_id: An identifier for the context within which the given search will be performed. A marketplace might provide mechanisms for constraining a search to a subset of potential items. For example, the retail marketplace allows queries to be constrained to a specific category. The QueryContextId parameter specifies such a subset. If it is omitted, the search will be performed using the default context for the marketplace, which will typically contain the largest set of items.
            seller_sku: Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
            upc: A 12-digit bar code used for retail packaging.
            ean: A European article number that uniquely identifies the catalog item, manufacturer, and its attributes.
            isbn: The unique commercial book identifier used to identify books internationally.
            jan: A Japanese article number that uniquely identifies the product, manufacturer, and its attributes.
        """
        url = "/catalog/v0/items"
        values = (
            marketplace_id,
            query,
            query_context_id,
            seller_sku,
            upc,
            ean,
            isbn,
            jan,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_catalog_items_params)
        return response

    _list_catalog_items_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("Query", "query"),
        ("QueryContextId", "query"),
        ("SellerSKU", "query"),
        ("UPC", "query"),
        ("EAN", "query"),
        ("ISBN", "query"),
        ("JAN", "query"),
    )
