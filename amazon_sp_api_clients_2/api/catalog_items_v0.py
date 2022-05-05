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
class ASINIdentifier:

    asin: str = attrs.field()
    marketplace_id: str = attrs.field()

    pass


@attrs.define
class AttributeSetList:

    pass


@attrs.define
class AttributeSetListType:

    actor: list[str] = attrs.field()
    artist: list[str] = attrs.field()
    aspect_ratio: str = attrs.field()
    audience_rating: str = attrs.field()
    author: list[str] = attrs.field()
    back_finding: str = attrs.field()
    band_material_type: str = attrs.field()
    binding: str = attrs.field()
    bluray_region: str = attrs.field()
    brand: str = attrs.field()
    cero_age_rating: str = attrs.field()
    chain_type: str = attrs.field()
    clasp_type: str = attrs.field()
    color: str = attrs.field()
    cpu_manufacturer: str = attrs.field()
    cpu_type: str = attrs.field()
    creator: list["CreatorType"] = attrs.field()
    department: str = attrs.field()
    director: list[str] = attrs.field()
    edition: str = attrs.field()
    episode_sequence: str = attrs.field()
    esrb_age_rating: str = attrs.field()
    feature: list[str] = attrs.field()
    flavor: str = attrs.field()
    format: list[str] = attrs.field()
    gem_type: list[str] = attrs.field()
    genre: str = attrs.field()
    golf_club_flex: str = attrs.field()
    hand_orientation: str = attrs.field()
    hard_disk_interface: str = attrs.field()
    hardware_platform: str = attrs.field()
    hazardous_material_type: str = attrs.field()
    is_adult_product: bool = attrs.field()
    is_autographed: bool = attrs.field()
    is_eligible_for_trade_in: bool = attrs.field()
    is_memorabilia: bool = attrs.field()
    issues_per_year: str = attrs.field()
    item_part_number: str = attrs.field()
    label: str = attrs.field()
    languages: list["LanguageType"] = attrs.field()
    legal_disclaimer: str = attrs.field()
    manufacturer: str = attrs.field()
    manufacturer_parts_warranty_description: str = attrs.field()
    material_type: list[str] = attrs.field()
    media_type: list[str] = attrs.field()
    metal_stamp: str = attrs.field()
    metal_type: str = attrs.field()
    model: str = attrs.field()
    number_of_discs: int = attrs.field()
    number_of_issues: int = attrs.field()
    number_of_items: int = attrs.field()
    number_of_pages: int = attrs.field()
    number_of_tracks: int = attrs.field()
    operating_system: list[str] = attrs.field()
    package_quantity: int = attrs.field()
    part_number: str = attrs.field()
    pegi_rating: str = attrs.field()
    platform: list[str] = attrs.field()
    processor_count: int = attrs.field()
    product_group: str = attrs.field()
    product_type_name: str = attrs.field()
    product_type_subcategory: str = attrs.field()
    publication_date: str = attrs.field()
    publisher: str = attrs.field()
    region_code: str = attrs.field()
    release_date: str = attrs.field()
    ring_size: str = attrs.field()
    scent: str = attrs.field()
    season_sequence: str = attrs.field()
    seikodo_product_code: str = attrs.field()
    shaft_material: str = attrs.field()
    size: str = attrs.field()
    size_per_pearl: str = attrs.field()
    studio: str = attrs.field()
    system_memory_type: str = attrs.field()
    theatrical_release_date: str = attrs.field()
    title: str = attrs.field()
    warranty: str = attrs.field()

    cpu_speed: "DecimalWithUnits" = attrs.field()
    display_size: "DecimalWithUnits" = attrs.field()
    golf_club_loft: "DecimalWithUnits" = attrs.field()
    hard_disk_size: "DecimalWithUnits" = attrs.field()
    item_dimensions: "DimensionType" = attrs.field()
    list_price: "Price" = attrs.field()
    manufacturer_maximum_age: "DecimalWithUnits" = attrs.field()
    manufacturer_minimum_age: "DecimalWithUnits" = attrs.field()
    maximum_resolution: "DecimalWithUnits" = attrs.field()
    optical_zoom: "DecimalWithUnits" = attrs.field()
    package_dimensions: "DimensionType" = attrs.field()
    running_time: "DecimalWithUnits" = attrs.field()
    small_image: "Image" = attrs.field()
    subscription_length: "DecimalWithUnits" = attrs.field()
    system_memory_size: "DecimalWithUnits" = attrs.field()
    total_diamond_weight: "DecimalWithUnits" = attrs.field()
    total_gem_weight: "DecimalWithUnits" = attrs.field()
    weee_tax_value: "Price" = attrs.field()
    pass


@attrs.define
class Categories:

    product_category_id: str = attrs.field()
    product_category_name: str = attrs.field()
    parent: dict[str, Any] = attrs.field()
    # {'properties': {}}

    pass


@attrs.define
class CreatorType:

    role: str = attrs.field()
    value: str = attrs.field()

    pass


@attrs.define
class DecimalWithUnits:

    units: str = attrs.field()
    value: Union[float, int] = attrs.field()

    pass


@attrs.define
class DimensionType:

    height: "DecimalWithUnits" = attrs.field()
    length: "DecimalWithUnits" = attrs.field()
    weight: "DecimalWithUnits" = attrs.field()
    width: "DecimalWithUnits" = attrs.field()
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
class GetCatalogItemResponse:

    errors: "ErrorList" = attrs.field()
    payload: "Item" = attrs.field()
    pass


@attrs.define
class IdentifierType:

    marketplace_asin: "ASINIdentifier" = attrs.field()
    skuidentifier: "SellerSKUIdentifier" = attrs.field()
    pass


@attrs.define
class Image:

    url: str = attrs.field()

    height: "DecimalWithUnits" = attrs.field()
    width: "DecimalWithUnits" = attrs.field()
    pass


@attrs.define
class Item:

    attribute_sets: "AttributeSetList" = attrs.field()
    identifiers: "IdentifierType" = attrs.field()
    relationships: "RelationshipList" = attrs.field()
    sales_rankings: "SalesRankList" = attrs.field()
    pass


@attrs.define
class ItemList:

    pass


@attrs.define
class LanguageType:

    audio_format: str = attrs.field()
    name: str = attrs.field()
    type: str = attrs.field()

    pass


@attrs.define
class ListCatalogCategoriesResponse:

    errors: "ErrorList" = attrs.field()
    payload: "ListOfCategories" = attrs.field()
    pass


@attrs.define
class ListCatalogItemsResponse:

    errors: "ErrorList" = attrs.field()
    payload: "ListMatchingItemsResponse" = attrs.field()
    pass


@attrs.define
class ListMatchingItemsResponse:

    items: "ItemList" = attrs.field()
    pass


@attrs.define
class ListOfCategories:

    pass


@attrs.define
class Price:

    amount: Union[float, int] = attrs.field()
    currency_code: str = attrs.field()

    pass


@attrs.define
class RelationshipList:

    pass


@attrs.define
class RelationshipType:

    color: str = attrs.field()
    edition: str = attrs.field()
    flavor: str = attrs.field()
    gem_type: list[str] = attrs.field()
    golf_club_flex: str = attrs.field()
    hand_orientation: str = attrs.field()
    hardware_platform: str = attrs.field()
    material_type: list[str] = attrs.field()
    metal_type: str = attrs.field()
    model: str = attrs.field()
    operating_system: list[str] = attrs.field()
    package_quantity: int = attrs.field()
    product_type_subcategory: str = attrs.field()
    ring_size: str = attrs.field()
    scent: str = attrs.field()
    shaft_material: str = attrs.field()
    size: str = attrs.field()
    size_per_pearl: str = attrs.field()

    golf_club_loft: "DecimalWithUnits" = attrs.field()
    identifiers: "IdentifierType" = attrs.field()
    item_dimensions: "DimensionType" = attrs.field()
    total_diamond_weight: "DecimalWithUnits" = attrs.field()
    total_gem_weight: "DecimalWithUnits" = attrs.field()
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
class SellerSKUIdentifier:

    marketplace_id: str = attrs.field()
    seller_id: str = attrs.field()
    seller_sku: str = attrs.field()

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
