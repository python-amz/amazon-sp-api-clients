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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class ASINIdentifier:

    asin: str = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: str = attrs.field()
    """
    A marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AttributeSetListType:
    """
    The attributes of the item.
    """

    actor: Optional[List[str]] = attrs.field()
    """
    The actor attributes of the item.
    """

    artist: Optional[List[str]] = attrs.field()
    """
    The artist attributes of the item.
    """

    aspect_ratio: Optional[str] = attrs.field()
    """
    The aspect ratio attribute of the item.
    """

    audience_rating: Optional[str] = attrs.field()
    """
    The audience rating attribute of the item.
    """

    author: Optional[List[str]] = attrs.field()
    """
    The author attributes of the item.
    """

    back_finding: Optional[str] = attrs.field()
    """
    The back finding attribute of the item.
    """

    band_material_type: Optional[str] = attrs.field()
    """
    The band material type attribute of the item.
    """

    binding: Optional[str] = attrs.field()
    """
    The binding attribute of the item.
    """

    bluray_region: Optional[str] = attrs.field()
    """
    The Bluray region attribute of the item.
    """

    brand: Optional[str] = attrs.field()
    """
    The brand attribute of the item.
    """

    cero_age_rating: Optional[str] = attrs.field()
    """
    The CERO age rating attribute of the item.
    """

    chain_type: Optional[str] = attrs.field()
    """
    The chain type attribute of the item.
    """

    clasp_type: Optional[str] = attrs.field()
    """
    The clasp type attribute of the item.
    """

    color: Optional[str] = attrs.field()
    """
    The color attribute of the item.
    """

    cpu_manufacturer: Optional[str] = attrs.field()
    """
    The CPU manufacturer attribute of the item.
    """

    cpu_speed: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    cpu_type: Optional[str] = attrs.field()
    """
    The CPU type attribute of the item.
    """

    creator: Optional[List["CreatorType"]] = attrs.field()
    """
    The creator attributes of the item.
    """

    department: Optional[str] = attrs.field()
    """
    The department attribute of the item.
    """

    director: Optional[List[str]] = attrs.field()
    """
    The director attributes of the item.
    """

    display_size: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    edition: Optional[str] = attrs.field()
    """
    The edition attribute of the item.
    """

    episode_sequence: Optional[str] = attrs.field()
    """
    The episode sequence attribute of the item.
    """

    esrb_age_rating: Optional[str] = attrs.field()
    """
    The ESRB age rating attribute of the item.
    """

    feature: Optional[List[str]] = attrs.field()
    """
    The feature attributes of the item
    """

    flavor: Optional[str] = attrs.field()
    """
    The flavor attribute of the item.
    """

    format: Optional[List[str]] = attrs.field()
    """
    The format attributes of the item.
    """

    gem_type: Optional[List[str]] = attrs.field()
    """
    The gem type attributes of the item.
    """

    genre: Optional[str] = attrs.field()
    """
    The genre attribute of the item.
    """

    golf_club_flex: Optional[str] = attrs.field()
    """
    The golf club flex attribute of the item.
    """

    golf_club_loft: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    hand_orientation: Optional[str] = attrs.field()
    """
    The hand orientation attribute of the item.
    """

    hard_disk_interface: Optional[str] = attrs.field()
    """
    The hard disk interface attribute of the item.
    """

    hard_disk_size: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    hardware_platform: Optional[str] = attrs.field()
    """
    The hardware platform attribute of the item.
    """

    hazardous_material_type: Optional[str] = attrs.field()
    """
    The hazardous material type attribute of the item.
    """

    is_adult_product: Optional[bool] = attrs.field()
    """
    The adult product attribute of the item.
    """

    is_autographed: Optional[bool] = attrs.field()
    """
    The autographed attribute of the item.
    """

    is_eligible_for_trade_in: Optional[bool] = attrs.field()
    """
    The is eligible for trade in attribute of the item.
    """

    is_memorabilia: Optional[bool] = attrs.field()
    """
    The is memorabilia attribute of the item.
    """

    issues_per_year: Optional[str] = attrs.field()
    """
    The issues per year attribute of the item.
    """

    item_dimensions: Optional["DimensionType"] = attrs.field()
    """
    The dimension type attribute of an item.
    """

    item_part_number: Optional[str] = attrs.field()
    """
    The item part number attribute of the item.
    """

    label: Optional[str] = attrs.field()
    """
    The label attribute of the item.
    """

    languages: Optional[List["LanguageType"]] = attrs.field()
    """
    The languages attribute of the item.
    """

    legal_disclaimer: Optional[str] = attrs.field()
    """
    The legal disclaimer attribute of the item.
    """

    list_price: Optional["Price"] = attrs.field()
    """
    The price attribute of the item.
    """

    manufacturer: Optional[str] = attrs.field()
    """
    The manufacturer attribute of the item.
    """

    manufacturer_maximum_age: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    manufacturer_minimum_age: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    manufacturer_parts_warranty_description: Optional[str] = attrs.field()
    """
    The manufacturer parts warranty description attribute of the item.
    """

    material_type: Optional[List[str]] = attrs.field()
    """
    The material type attributes of the item.
    """

    maximum_resolution: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    media_type: Optional[List[str]] = attrs.field()
    """
    The media type attributes of the item.
    """

    metal_stamp: Optional[str] = attrs.field()
    """
    The metal stamp attribute of the item.
    """

    metal_type: Optional[str] = attrs.field()
    """
    The metal type attribute of the item.
    """

    model: Optional[str] = attrs.field()
    """
    The model attribute of the item.
    """

    number_of_discs: Optional[int] = attrs.field()
    """
    The number of discs attribute of the item.
    """

    number_of_issues: Optional[int] = attrs.field()
    """
    The number of issues attribute of the item.
    """

    number_of_items: Optional[int] = attrs.field()
    """
    The number of items attribute of the item.
    """

    number_of_pages: Optional[int] = attrs.field()
    """
    The number of pages attribute of the item.
    """

    number_of_tracks: Optional[int] = attrs.field()
    """
    The number of tracks attribute of the item.
    """

    operating_system: Optional[List[str]] = attrs.field()
    """
    The operating system attributes of the item.
    """

    optical_zoom: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    package_dimensions: Optional["DimensionType"] = attrs.field()
    """
    The dimension type attribute of an item.
    """

    package_quantity: Optional[int] = attrs.field()
    """
    The package quantity attribute of the item.
    """

    part_number: Optional[str] = attrs.field()
    """
    The part number attribute of the item.
    """

    pegi_rating: Optional[str] = attrs.field()
    """
    The PEGI rating attribute of the item.
    """

    platform: Optional[List[str]] = attrs.field()
    """
    The platform attributes of the item.
    """

    processor_count: Optional[int] = attrs.field()
    """
    The processor count attribute of the item.
    """

    product_group: Optional[str] = attrs.field()
    """
    The product group attribute of the item.
    """

    product_type_name: Optional[str] = attrs.field()
    """
    The product type name attribute of the item.
    """

    product_type_subcategory: Optional[str] = attrs.field()
    """
    The product type subcategory attribute of the item.
    """

    publication_date: Optional[str] = attrs.field()
    """
    The publication date attribute of the item.
    """

    publisher: Optional[str] = attrs.field()
    """
    The publisher attribute of the item.
    """

    region_code: Optional[str] = attrs.field()
    """
    The region code attribute of the item.
    """

    release_date: Optional[str] = attrs.field()
    """
    The release date attribute of the item.
    """

    ring_size: Optional[str] = attrs.field()
    """
    The ring size attribute of the item.
    """

    running_time: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    scent: Optional[str] = attrs.field()
    """
    The scent attribute of the item.
    """

    season_sequence: Optional[str] = attrs.field()
    """
    The season sequence attribute of the item.
    """

    seikodo_product_code: Optional[str] = attrs.field()
    """
    The Seikodo product code attribute of the item.
    """

    shaft_material: Optional[str] = attrs.field()
    """
    The shaft material attribute of the item.
    """

    size: Optional[str] = attrs.field()
    """
    The size attribute of the item.
    """

    size_per_pearl: Optional[str] = attrs.field()
    """
    The size per pearl attribute of the item.
    """

    small_image: Optional["Image"] = attrs.field()
    """
    The image attribute of the item.
    """

    studio: Optional[str] = attrs.field()
    """
    The studio attribute of the item.
    """

    subscription_length: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    system_memory_size: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    system_memory_type: Optional[str] = attrs.field()
    """
    The system memory type attribute of the item.
    """

    theatrical_release_date: Optional[str] = attrs.field()
    """
    The theatrical release date attribute of the item.
    """

    title: Optional[str] = attrs.field()
    """
    The title attribute of the item.
    """

    total_diamond_weight: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    total_gem_weight: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    warranty: Optional[str] = attrs.field()
    """
    The warranty attribute of the item.
    """

    weee_tax_value: Optional["Price"] = attrs.field()
    """
    The price attribute of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Categories:

    product_category_id: Optional[str] = attrs.field()
    """
    The identifier for the product category (or browse node).
    """

    product_category_name: Optional[str] = attrs.field()
    """
    The name of the product category (or browse node).
    """

    parent: Optional["CategoriesParent"] = attrs.field()
    """
    The parent product category.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CategoriesParent:
    """
    The parent product category.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreatorType:
    """
    The creator type attribute of an item.
    """

    role: Optional[str] = attrs.field()
    """
    The role of the value.
    """

    value: Optional[str] = attrs.field()
    """
    The value of the attribute.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DecimalWithUnits:
    """
    The decimal value and unit.
    """

    units: Optional[str] = attrs.field()
    """
    The unit of the decimal value.
    """

    value: Optional[float] = attrs.field()
    """
    The decimal value.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DimensionType:
    """
    The dimension type attribute of an item.
    """

    height: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    length: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    weight: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    width: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetCatalogItemResponse:

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Item"] = attrs.field()
    """
    An item in the Amazon catalog.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class IdentifierType:

    marketplace_asin: Optional["ASINIdentifier"] = attrs.field()

    skuidentifier: Optional["SellerSKUIdentifier"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Image:
    """
    The image attribute of the item.
    """

    height: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    url: Optional[str] = attrs.field()
    """
    The image URL attribute of the item.
    """

    width: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    An item in the Amazon catalog.
    """

    attribute_sets: Optional[List["AttributeSetListType"]] = attrs.field()
    """
    A list of attributes for the item.
    """

    identifiers: "IdentifierType" = attrs.field()

    relationships: Optional[List["RelationshipType"]] = attrs.field()
    """
    A list of variation relationship information, if applicable for the item.
    """

    sales_rankings: Optional[List["SalesRankType"]] = attrs.field()
    """
    A list of sales rank information for the item by category.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LanguageType:
    """
    The language type attribute of an item.
    """

    audio_format: Optional[str] = attrs.field()
    """
    The audio format attribute of the item.
    """

    name: Optional[str] = attrs.field()
    """
    The name attribute of the item.
    """

    type: Optional[str] = attrs.field()
    """
    The type attribute of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListCatalogCategoriesResponse:

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional[List["Categories"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListCatalogItemsResponse:

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ListMatchingItemsResponse"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListMatchingItemsResponse:

    items: Optional[List["Item"]] = attrs.field()
    """
    A list of items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Price:
    """
    The price attribute of the item.
    """

    amount: Optional[float] = attrs.field()
    """
    The amount.
    """

    currency_code: Optional[str] = attrs.field()
    """
    The currency code of the amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RelationshipType:
    """
    Specific variations of the item.
    """

    color: Optional[str] = attrs.field()
    """
    The color variation of the item.
    """

    edition: Optional[str] = attrs.field()
    """
    The edition variation of the item.
    """

    flavor: Optional[str] = attrs.field()
    """
    The flavor variation of the item.
    """

    gem_type: Optional[List[str]] = attrs.field()
    """
    The gem type variations of the item.
    """

    golf_club_flex: Optional[str] = attrs.field()
    """
    The golf club flex variation of an item.
    """

    golf_club_loft: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    hand_orientation: Optional[str] = attrs.field()
    """
    The hand orientation variation of an item.
    """

    hardware_platform: Optional[str] = attrs.field()
    """
    The hardware platform variation of an item.
    """

    identifiers: Optional["IdentifierType"] = attrs.field()

    item_dimensions: Optional["DimensionType"] = attrs.field()
    """
    The dimension type attribute of an item.
    """

    material_type: Optional[List[str]] = attrs.field()
    """
    The material type variations of an item.
    """

    metal_type: Optional[str] = attrs.field()
    """
    The metal type variation of an item.
    """

    model: Optional[str] = attrs.field()
    """
    The model variation of an item.
    """

    operating_system: Optional[List[str]] = attrs.field()
    """
    The operating system variations of an item.
    """

    package_quantity: Optional[int] = attrs.field()
    """
    The package quantity variation of an item.
    """

    product_type_subcategory: Optional[str] = attrs.field()
    """
    The product type subcategory variation of an item.
    """

    ring_size: Optional[str] = attrs.field()
    """
    The ring size variation of an item.
    """

    scent: Optional[str] = attrs.field()
    """
    The scent variation of an item.
    """

    shaft_material: Optional[str] = attrs.field()
    """
    The shaft material variation of an item.
    """

    size: Optional[str] = attrs.field()
    """
    The size variation of an item.
    """

    size_per_pearl: Optional[str] = attrs.field()
    """
    The size per pearl variation of an item.
    """

    total_diamond_weight: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """

    total_gem_weight: Optional["DecimalWithUnits"] = attrs.field()
    """
    The decimal value and unit.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SalesRankType:

    product_category_id: str = attrs.field()
    """
    Identifies the item category from which the sales rank is taken.
    """

    rank: int = attrs.field()
    """
    The sales rank of the item within the item category.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerSKUIdentifier:

    marketplace_id: str = attrs.field()
    """
    A marketplace identifier.
    """

    seller_id: str = attrs.field()
    """
    The seller identifier submitted for the operation.
    """

    seller_sku: str = attrs.field()
    """
    The seller stock keeping unit (SKU) of the item.
    """


class CatalogItemsV0Client(BaseClient):
    def get_catalog_item(
        self,
        marketplace_id: str,
        asin: str,
    ) -> Union[GetCatalogItemResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_catalog_item_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_catalog_item_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("asin", "path"),
    )

    _get_catalog_item_responses = {
        (200, "application/json"): GetCatalogItemResponse,
        (400, "application/json"): GetCatalogItemResponse,
        (401, "application/json"): GetCatalogItemResponse,
        (403, "application/json"): GetCatalogItemResponse,
        (404, "application/json"): GetCatalogItemResponse,
        (429, "application/json"): GetCatalogItemResponse,
        (500, "application/json"): GetCatalogItemResponse,
        (503, "application/json"): GetCatalogItemResponse,
    }

    def list_catalog_categories(
        self,
        marketplace_id: str,
        asin: str = None,
        seller_sku: str = None,
    ) -> Union[ListCatalogCategoriesResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_catalog_categories_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_catalog_categories_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ASIN", "query"),
        ("SellerSKU", "query"),
    )

    _list_catalog_categories_responses = {
        (200, "application/json"): ListCatalogCategoriesResponse,
        (400, "application/json"): ListCatalogCategoriesResponse,
        (401, "application/json"): ListCatalogCategoriesResponse,
        (403, "application/json"): ListCatalogCategoriesResponse,
        (404, "application/json"): ListCatalogCategoriesResponse,
        (429, "application/json"): ListCatalogCategoriesResponse,
        (500, "application/json"): ListCatalogCategoriesResponse,
        (503, "application/json"): ListCatalogCategoriesResponse,
    }

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
    ) -> Union[ListCatalogItemsResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_catalog_items_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

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

    _list_catalog_items_responses = {
        (200, "application/json"): ListCatalogItemsResponse,
        (400, "application/json"): ListCatalogItemsResponse,
        (401, "application/json"): ListCatalogItemsResponse,
        (403, "application/json"): ListCatalogItemsResponse,
        (404, "application/json"): ListCatalogItemsResponse,
        (429, "application/json"): ListCatalogItemsResponse,
        (500, "application/json"): ListCatalogItemsResponse,
        (503, "application/json"): ListCatalogItemsResponse,
    }
