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
from datetime import date, datetime


@attrs.define
class ASINIdentifier:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """


@attrs.define
class AttributeSetList:
    """
    A list of attributes for the item.
    """

    pass


@attrs.define
class AttributeSetListType:
    """
    The attributes of the item.
    """

    actor: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The actor attributes of the item.
    """

    artist: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The artist attributes of the item.
    """

    aspect_ratio: str = attrs.field(
        kw_only=True,
    )
    """
    The aspect ratio attribute of the item.
    """

    audience_rating: str = attrs.field(
        kw_only=True,
    )
    """
    The audience rating attribute of the item.
    """

    author: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The author attributes of the item.
    """

    back_finding: str = attrs.field(
        kw_only=True,
    )
    """
    The back finding attribute of the item.
    """

    band_material_type: str = attrs.field(
        kw_only=True,
    )
    """
    The band material type attribute of the item.
    """

    binding: str = attrs.field(
        kw_only=True,
    )
    """
    The binding attribute of the item.
    """

    bluray_region: str = attrs.field(
        kw_only=True,
    )
    """
    The Bluray region attribute of the item.
    """

    brand: str = attrs.field(
        kw_only=True,
    )
    """
    The brand attribute of the item.
    """

    cero_age_rating: str = attrs.field(
        kw_only=True,
    )
    """
    The CERO age rating attribute of the item.
    """

    chain_type: str = attrs.field(
        kw_only=True,
    )
    """
    The chain type attribute of the item.
    """

    clasp_type: str = attrs.field(
        kw_only=True,
    )
    """
    The clasp type attribute of the item.
    """

    color: str = attrs.field(
        kw_only=True,
    )
    """
    The color attribute of the item.
    """

    cpu_manufacturer: str = attrs.field(
        kw_only=True,
    )
    """
    The CPU manufacturer attribute of the item.
    """

    cpu_type: str = attrs.field(
        kw_only=True,
    )
    """
    The CPU type attribute of the item.
    """

    creator: List["CreatorType"] = attrs.field(
        kw_only=True,
    )
    """
    The creator attributes of the item.
    """

    department: str = attrs.field(
        kw_only=True,
    )
    """
    The department attribute of the item.
    """

    director: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The director attributes of the item.
    """

    edition: str = attrs.field(
        kw_only=True,
    )
    """
    The edition attribute of the item.
    """

    episode_sequence: str = attrs.field(
        kw_only=True,
    )
    """
    The episode sequence attribute of the item.
    """

    esrb_age_rating: str = attrs.field(
        kw_only=True,
    )
    """
    The ESRB age rating attribute of the item.
    """

    feature: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The feature attributes of the item
    """

    flavor: str = attrs.field(
        kw_only=True,
    )
    """
    The flavor attribute of the item.
    """

    format: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The format attributes of the item.
    """

    gem_type: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The gem type attributes of the item.
    """

    genre: str = attrs.field(
        kw_only=True,
    )
    """
    The genre attribute of the item.
    """

    golf_club_flex: str = attrs.field(
        kw_only=True,
    )
    """
    The golf club flex attribute of the item.
    """

    hand_orientation: str = attrs.field(
        kw_only=True,
    )
    """
    The hand orientation attribute of the item.
    """

    hard_disk_interface: str = attrs.field(
        kw_only=True,
    )
    """
    The hard disk interface attribute of the item.
    """

    hardware_platform: str = attrs.field(
        kw_only=True,
    )
    """
    The hardware platform attribute of the item.
    """

    hazardous_material_type: str = attrs.field(
        kw_only=True,
    )
    """
    The hazardous material type attribute of the item.
    """

    is_adult_product: bool = attrs.field(
        kw_only=True,
    )
    """
    The adult product attribute of the item.
    """

    is_autographed: bool = attrs.field(
        kw_only=True,
    )
    """
    The autographed attribute of the item.
    """

    is_eligible_for_trade_in: bool = attrs.field(
        kw_only=True,
    )
    """
    The is eligible for trade in attribute of the item.
    """

    is_memorabilia: bool = attrs.field(
        kw_only=True,
    )
    """
    The is memorabilia attribute of the item.
    """

    issues_per_year: str = attrs.field(
        kw_only=True,
    )
    """
    The issues per year attribute of the item.
    """

    item_part_number: str = attrs.field(
        kw_only=True,
    )
    """
    The item part number attribute of the item.
    """

    label: str = attrs.field(
        kw_only=True,
    )
    """
    The label attribute of the item.
    """

    languages: List["LanguageType"] = attrs.field(
        kw_only=True,
    )
    """
    The languages attribute of the item.
    """

    legal_disclaimer: str = attrs.field(
        kw_only=True,
    )
    """
    The legal disclaimer attribute of the item.
    """

    manufacturer: str = attrs.field(
        kw_only=True,
    )
    """
    The manufacturer attribute of the item.
    """

    manufacturer_parts_warranty_description: str = attrs.field(
        kw_only=True,
    )
    """
    The manufacturer parts warranty description attribute of the item.
    """

    material_type: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The material type attributes of the item.
    """

    media_type: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The media type attributes of the item.
    """

    metal_stamp: str = attrs.field(
        kw_only=True,
    )
    """
    The metal stamp attribute of the item.
    """

    metal_type: str = attrs.field(
        kw_only=True,
    )
    """
    The metal type attribute of the item.
    """

    model: str = attrs.field(
        kw_only=True,
    )
    """
    The model attribute of the item.
    """

    number_of_discs: int = attrs.field(
        kw_only=True,
    )
    """
    The number of discs attribute of the item.
    """

    number_of_issues: int = attrs.field(
        kw_only=True,
    )
    """
    The number of issues attribute of the item.
    """

    number_of_items: int = attrs.field(
        kw_only=True,
    )
    """
    The number of items attribute of the item.
    """

    number_of_pages: int = attrs.field(
        kw_only=True,
    )
    """
    The number of pages attribute of the item.
    """

    number_of_tracks: int = attrs.field(
        kw_only=True,
    )
    """
    The number of tracks attribute of the item.
    """

    operating_system: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The operating system attributes of the item.
    """

    package_quantity: int = attrs.field(
        kw_only=True,
    )
    """
    The package quantity attribute of the item.
    """

    part_number: str = attrs.field(
        kw_only=True,
    )
    """
    The part number attribute of the item.
    """

    pegi_rating: str = attrs.field(
        kw_only=True,
    )
    """
    The PEGI rating attribute of the item.
    """

    platform: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The platform attributes of the item.
    """

    processor_count: int = attrs.field(
        kw_only=True,
    )
    """
    The processor count attribute of the item.
    """

    product_group: str = attrs.field(
        kw_only=True,
    )
    """
    The product group attribute of the item.
    """

    product_type_name: str = attrs.field(
        kw_only=True,
    )
    """
    The product type name attribute of the item.
    """

    product_type_subcategory: str = attrs.field(
        kw_only=True,
    )
    """
    The product type subcategory attribute of the item.
    """

    publication_date: str = attrs.field(
        kw_only=True,
    )
    """
    The publication date attribute of the item.
    """

    publisher: str = attrs.field(
        kw_only=True,
    )
    """
    The publisher attribute of the item.
    """

    region_code: str = attrs.field(
        kw_only=True,
    )
    """
    The region code attribute of the item.
    """

    release_date: str = attrs.field(
        kw_only=True,
    )
    """
    The release date attribute of the item.
    """

    ring_size: str = attrs.field(
        kw_only=True,
    )
    """
    The ring size attribute of the item.
    """

    scent: str = attrs.field(
        kw_only=True,
    )
    """
    The scent attribute of the item.
    """

    season_sequence: str = attrs.field(
        kw_only=True,
    )
    """
    The season sequence attribute of the item.
    """

    seikodo_product_code: str = attrs.field(
        kw_only=True,
    )
    """
    The Seikodo product code attribute of the item.
    """

    shaft_material: str = attrs.field(
        kw_only=True,
    )
    """
    The shaft material attribute of the item.
    """

    size: str = attrs.field(
        kw_only=True,
    )
    """
    The size attribute of the item.
    """

    size_per_pearl: str = attrs.field(
        kw_only=True,
    )
    """
    The size per pearl attribute of the item.
    """

    studio: str = attrs.field(
        kw_only=True,
    )
    """
    The studio attribute of the item.
    """

    system_memory_type: str = attrs.field(
        kw_only=True,
    )
    """
    The system memory type attribute of the item.
    """

    theatrical_release_date: str = attrs.field(
        kw_only=True,
    )
    """
    The theatrical release date attribute of the item.
    """

    title: str = attrs.field(
        kw_only=True,
    )
    """
    The title attribute of the item.
    """

    warranty: str = attrs.field(
        kw_only=True,
    )
    """
    The warranty attribute of the item.
    """

    cpu_speed: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    display_size: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    golf_club_loft: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    hard_disk_size: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    item_dimensions: "DimensionType" = attrs.field(
        kw_only=True,
    )

    list_price: "Price" = attrs.field(
        kw_only=True,
    )

    manufacturer_maximum_age: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    manufacturer_minimum_age: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    maximum_resolution: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    optical_zoom: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    package_dimensions: "DimensionType" = attrs.field(
        kw_only=True,
    )

    running_time: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    small_image: "Image" = attrs.field(
        kw_only=True,
    )

    subscription_length: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    system_memory_size: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    total_diamond_weight: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    total_gem_weight: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    weee_tax_value: "Price" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Categories:

    product_category_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the product category (or browse node).
    """

    product_category_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the product category (or browse node).
    """

    parent: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    The parent product category.

    Extra fields:
    {'properties': {}}
    """


@attrs.define
class CreatorType:
    """
    The creator type attribute of an item.
    """

    role: str = attrs.field(
        kw_only=True,
    )
    """
    The role of the value.
    """

    value: str = attrs.field(
        kw_only=True,
    )
    """
    The value of the attribute.
    """


@attrs.define
class DecimalWithUnits:
    """
    The decimal value and unit.
    """

    units: str = attrs.field(
        kw_only=True,
    )
    """
    The unit of the decimal value.
    """

    value: float = attrs.field(
        kw_only=True,
    )
    """
    The decimal value.
    """


@attrs.define
class DimensionType:
    """
    The dimension type attribute of an item.
    """

    height: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    length: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    weight: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    width: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class GetCatalogItemResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Item" = attrs.field(
        kw_only=True,
    )


@attrs.define
class IdentifierType:

    marketplace_asin: "ASINIdentifier" = attrs.field(
        kw_only=True,
    )

    skuidentifier: "SellerSKUIdentifier" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Image:
    """
    The image attribute of the item.
    """

    url: str = attrs.field(
        kw_only=True,
    )
    """
    The image URL attribute of the item.
    """

    height: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    width: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Item:
    """
    An item in the Amazon catalog.
    """

    attribute_sets: "AttributeSetList" = attrs.field(
        kw_only=True,
    )

    identifiers: "IdentifierType" = attrs.field(
        kw_only=True,
    )

    relationships: "RelationshipList" = attrs.field(
        kw_only=True,
    )

    sales_rankings: "SalesRankList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ItemList:
    """
    A list of items.
    """

    pass


@attrs.define
class LanguageType:
    """
    The language type attribute of an item.
    """

    audio_format: str = attrs.field(
        kw_only=True,
    )
    """
    The audio format attribute of the item.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name attribute of the item.
    """

    type: str = attrs.field(
        kw_only=True,
    )
    """
    The type attribute of the item.
    """


@attrs.define
class ListCatalogCategoriesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "ListOfCategories" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ListCatalogItemsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "ListMatchingItemsResponse" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ListMatchingItemsResponse:

    items: "ItemList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ListOfCategories:

    pass


@attrs.define
class Price:
    """
    The price attribute of the item.
    """

    amount: float = attrs.field(
        kw_only=True,
    )
    """
    The amount.
    """

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    The currency code of the amount.
    """


@attrs.define
class RelationshipList:
    """
    A list of variation relationship information, if applicable for the item.
    """

    pass


@attrs.define
class RelationshipType:
    """
    Specific variations of the item.
    """

    color: str = attrs.field(
        kw_only=True,
    )
    """
    The color variation of the item.
    """

    edition: str = attrs.field(
        kw_only=True,
    )
    """
    The edition variation of the item.
    """

    flavor: str = attrs.field(
        kw_only=True,
    )
    """
    The flavor variation of the item.
    """

    gem_type: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The gem type variations of the item.
    """

    golf_club_flex: str = attrs.field(
        kw_only=True,
    )
    """
    The golf club flex variation of an item.
    """

    hand_orientation: str = attrs.field(
        kw_only=True,
    )
    """
    The hand orientation variation of an item.
    """

    hardware_platform: str = attrs.field(
        kw_only=True,
    )
    """
    The hardware platform variation of an item.
    """

    material_type: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The material type variations of an item.
    """

    metal_type: str = attrs.field(
        kw_only=True,
    )
    """
    The metal type variation of an item.
    """

    model: str = attrs.field(
        kw_only=True,
    )
    """
    The model variation of an item.
    """

    operating_system: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The operating system variations of an item.
    """

    package_quantity: int = attrs.field(
        kw_only=True,
    )
    """
    The package quantity variation of an item.
    """

    product_type_subcategory: str = attrs.field(
        kw_only=True,
    )
    """
    The product type subcategory variation of an item.
    """

    ring_size: str = attrs.field(
        kw_only=True,
    )
    """
    The ring size variation of an item.
    """

    scent: str = attrs.field(
        kw_only=True,
    )
    """
    The scent variation of an item.
    """

    shaft_material: str = attrs.field(
        kw_only=True,
    )
    """
    The shaft material variation of an item.
    """

    size: str = attrs.field(
        kw_only=True,
    )
    """
    The size variation of an item.
    """

    size_per_pearl: str = attrs.field(
        kw_only=True,
    )
    """
    The size per pearl variation of an item.
    """

    golf_club_loft: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    identifiers: "IdentifierType" = attrs.field(
        kw_only=True,
    )

    item_dimensions: "DimensionType" = attrs.field(
        kw_only=True,
    )

    total_diamond_weight: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )

    total_gem_weight: "DecimalWithUnits" = attrs.field(
        kw_only=True,
    )


@attrs.define
class SalesRankList:
    """
    A list of sales rank information for the item by category.
    """

    pass


@attrs.define
class SalesRankType:

    product_category_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the item category from which the sales rank is taken.
    """

    rank: int = attrs.field(
        kw_only=True,
    )
    """
    The sales rank of the item within the item category.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier submitted for the operation.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """


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
