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

    asin: str
    marketplace_id: str

    pass


@attrs.define
class AttributeSetList:

    pass


@attrs.define
class AttributeSetListType:

    actor: list[str]
    artist: list[str]
    aspect_ratio: str
    audience_rating: str
    author: list[str]
    back_finding: str
    band_material_type: str
    binding: str
    bluray_region: str
    brand: str
    cero_age_rating: str
    chain_type: str
    clasp_type: str
    color: str
    cpu_manufacturer: str
    cpu_type: str
    creator: list["CreatorType"]
    department: str
    director: list[str]
    edition: str
    episode_sequence: str
    esrb_age_rating: str
    feature: list[str]
    flavor: str
    format: list[str]
    gem_type: list[str]
    genre: str
    golf_club_flex: str
    hand_orientation: str
    hard_disk_interface: str
    hardware_platform: str
    hazardous_material_type: str
    is_adult_product: bool
    is_autographed: bool
    is_eligible_for_trade_in: bool
    is_memorabilia: bool
    issues_per_year: str
    item_part_number: str
    label: str
    languages: list["LanguageType"]
    legal_disclaimer: str
    manufacturer: str
    manufacturer_parts_warranty_description: str
    material_type: list[str]
    media_type: list[str]
    metal_stamp: str
    metal_type: str
    model: str
    number_of_discs: int
    number_of_issues: int
    number_of_items: int
    number_of_pages: int
    number_of_tracks: int
    operating_system: list[str]
    package_quantity: int
    part_number: str
    pegi_rating: str
    platform: list[str]
    processor_count: int
    product_group: str
    product_type_name: str
    product_type_subcategory: str
    publication_date: str
    publisher: str
    region_code: str
    release_date: str
    ring_size: str
    scent: str
    season_sequence: str
    seikodo_product_code: str
    shaft_material: str
    size: str
    size_per_pearl: str
    studio: str
    system_memory_type: str
    theatrical_release_date: str
    title: str
    warranty: str

    cpu_speed: "DecimalWithUnits"
    display_size: "DecimalWithUnits"
    golf_club_loft: "DecimalWithUnits"
    hard_disk_size: "DecimalWithUnits"
    item_dimensions: "DimensionType"
    list_price: "Price"
    manufacturer_maximum_age: "DecimalWithUnits"
    manufacturer_minimum_age: "DecimalWithUnits"
    maximum_resolution: "DecimalWithUnits"
    optical_zoom: "DecimalWithUnits"
    package_dimensions: "DimensionType"
    running_time: "DecimalWithUnits"
    small_image: "Image"
    subscription_length: "DecimalWithUnits"
    system_memory_size: "DecimalWithUnits"
    total_diamond_weight: "DecimalWithUnits"
    total_gem_weight: "DecimalWithUnits"
    weee_tax_value: "Price"
    pass


@attrs.define
class Categories:

    product_category_id: str
    product_category_name: str
    parent: dict[str, Any]
    # {'properties': {}}

    pass


@attrs.define
class CreatorType:

    role: str
    value: str

    pass


@attrs.define
class DecimalWithUnits:

    units: str
    value: Union[float, int]

    pass


@attrs.define
class DimensionType:

    height: "DecimalWithUnits"
    length: "DecimalWithUnits"
    weight: "DecimalWithUnits"
    width: "DecimalWithUnits"
    pass


@attrs.define
class Error:

    code: str
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetCatalogItemResponse:

    errors: "ErrorList"
    payload: "Item"
    pass


@attrs.define
class IdentifierType:

    marketplace_asin: "ASINIdentifier"
    skuidentifier: "SellerSKUIdentifier"
    pass


@attrs.define
class Image:

    url: str

    height: "DecimalWithUnits"
    width: "DecimalWithUnits"
    pass


@attrs.define
class Item:

    attribute_sets: "AttributeSetList"
    identifiers: "IdentifierType"
    relationships: "RelationshipList"
    sales_rankings: "SalesRankList"
    pass


@attrs.define
class ItemList:

    pass


@attrs.define
class LanguageType:

    audio_format: str
    name: str
    type: str

    pass


@attrs.define
class ListCatalogCategoriesResponse:

    errors: "ErrorList"
    payload: "ListOfCategories"
    pass


@attrs.define
class ListCatalogItemsResponse:

    errors: "ErrorList"
    payload: "ListMatchingItemsResponse"
    pass


@attrs.define
class ListMatchingItemsResponse:

    items: "ItemList"
    pass


@attrs.define
class ListOfCategories:

    pass


@attrs.define
class Price:

    amount: Union[float, int]
    currency_code: str

    pass


@attrs.define
class RelationshipList:

    pass


@attrs.define
class RelationshipType:

    color: str
    edition: str
    flavor: str
    gem_type: list[str]
    golf_club_flex: str
    hand_orientation: str
    hardware_platform: str
    material_type: list[str]
    metal_type: str
    model: str
    operating_system: list[str]
    package_quantity: int
    product_type_subcategory: str
    ring_size: str
    scent: str
    shaft_material: str
    size: str
    size_per_pearl: str

    golf_club_loft: "DecimalWithUnits"
    identifiers: "IdentifierType"
    item_dimensions: "DimensionType"
    total_diamond_weight: "DecimalWithUnits"
    total_gem_weight: "DecimalWithUnits"
    pass


@attrs.define
class SalesRankList:

    pass


@attrs.define
class SalesRankType:

    product_category_id: str
    rank: int
    # {'schema_format': 'int32'}

    pass


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str
    seller_id: str
    seller_sku: str

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
