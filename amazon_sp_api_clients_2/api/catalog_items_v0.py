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
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _asinidentifier_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ASINIdentifier(**data)

    asin: str = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AttributeSetListType:
    """
    The attributes of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _attribute_set_list_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return AttributeSetListType(**data)

    actor: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The actor attributes of the item.
    """

    artist: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The artist attributes of the item.
    """

    aspect_ratio: Optional[str] = attrs.field(
        default=None,
    )
    """
    The aspect ratio attribute of the item.
    """

    audience_rating: Optional[str] = attrs.field(
        default=None,
    )
    """
    The audience rating attribute of the item.
    """

    author: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The author attributes of the item.
    """

    back_finding: Optional[str] = attrs.field(
        default=None,
    )
    """
    The back finding attribute of the item.
    """

    band_material_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The band material type attribute of the item.
    """

    binding: Optional[str] = attrs.field(
        default=None,
    )
    """
    The binding attribute of the item.
    """

    bluray_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Bluray region attribute of the item.
    """

    brand: Optional[str] = attrs.field(
        default=None,
    )
    """
    The brand attribute of the item.
    """

    cero_age_rating: Optional[str] = attrs.field(
        default=None,
    )
    """
    The CERO age rating attribute of the item.
    """

    chain_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The chain type attribute of the item.
    """

    clasp_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The clasp type attribute of the item.
    """

    color: Optional[str] = attrs.field(
        default=None,
    )
    """
    The color attribute of the item.
    """

    cpu_manufacturer: Optional[str] = attrs.field(
        default=None,
    )
    """
    The CPU manufacturer attribute of the item.
    """

    cpu_speed: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    cpu_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The CPU type attribute of the item.
    """

    creator: Optional[List["CreatorType"]] = attrs.field(
        default=None,
    )
    """
    The creator attributes of the item.
    """

    department: Optional[str] = attrs.field(
        default=None,
    )
    """
    The department attribute of the item.
    """

    director: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The director attributes of the item.
    """

    display_size: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    edition: Optional[str] = attrs.field(
        default=None,
    )
    """
    The edition attribute of the item.
    """

    episode_sequence: Optional[str] = attrs.field(
        default=None,
    )
    """
    The episode sequence attribute of the item.
    """

    esrb_age_rating: Optional[str] = attrs.field(
        default=None,
    )
    """
    The ESRB age rating attribute of the item.
    """

    feature: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The feature attributes of the item
    """

    flavor: Optional[str] = attrs.field(
        default=None,
    )
    """
    The flavor attribute of the item.
    """

    format: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The format attributes of the item.
    """

    gem_type: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The gem type attributes of the item.
    """

    genre: Optional[str] = attrs.field(
        default=None,
    )
    """
    The genre attribute of the item.
    """

    golf_club_flex: Optional[str] = attrs.field(
        default=None,
    )
    """
    The golf club flex attribute of the item.
    """

    golf_club_loft: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    hand_orientation: Optional[str] = attrs.field(
        default=None,
    )
    """
    The hand orientation attribute of the item.
    """

    hard_disk_interface: Optional[str] = attrs.field(
        default=None,
    )
    """
    The hard disk interface attribute of the item.
    """

    hard_disk_size: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    hardware_platform: Optional[str] = attrs.field(
        default=None,
    )
    """
    The hardware platform attribute of the item.
    """

    hazardous_material_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The hazardous material type attribute of the item.
    """

    is_adult_product: Optional[bool] = attrs.field(
        default=None,
    )
    """
    The adult product attribute of the item.
    """

    is_autographed: Optional[bool] = attrs.field(
        default=None,
    )
    """
    The autographed attribute of the item.
    """

    is_eligible_for_trade_in: Optional[bool] = attrs.field(
        default=None,
    )
    """
    The is eligible for trade in attribute of the item.
    """

    is_memorabilia: Optional[bool] = attrs.field(
        default=None,
    )
    """
    The is memorabilia attribute of the item.
    """

    issues_per_year: Optional[str] = attrs.field(
        default=None,
    )
    """
    The issues per year attribute of the item.
    """

    item_dimensions: Optional["DimensionType"] = attrs.field(
        default=None,
    )
    """
    The dimension type attribute of an item.
    """

    item_part_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The item part number attribute of the item.
    """

    label: Optional[str] = attrs.field(
        default=None,
    )
    """
    The label attribute of the item.
    """

    languages: Optional[List["LanguageType"]] = attrs.field(
        default=None,
    )
    """
    The languages attribute of the item.
    """

    legal_disclaimer: Optional[str] = attrs.field(
        default=None,
    )
    """
    The legal disclaimer attribute of the item.
    """

    list_price: Optional["Price"] = attrs.field(
        default=None,
    )
    """
    The price attribute of the item.
    """

    manufacturer: Optional[str] = attrs.field(
        default=None,
    )
    """
    The manufacturer attribute of the item.
    """

    manufacturer_maximum_age: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    manufacturer_minimum_age: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    manufacturer_parts_warranty_description: Optional[str] = attrs.field(
        default=None,
    )
    """
    The manufacturer parts warranty description attribute of the item.
    """

    material_type: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The material type attributes of the item.
    """

    maximum_resolution: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    media_type: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The media type attributes of the item.
    """

    metal_stamp: Optional[str] = attrs.field(
        default=None,
    )
    """
    The metal stamp attribute of the item.
    """

    metal_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The metal type attribute of the item.
    """

    model: Optional[str] = attrs.field(
        default=None,
    )
    """
    The model attribute of the item.
    """

    number_of_discs: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of discs attribute of the item.
    """

    number_of_issues: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of issues attribute of the item.
    """

    number_of_items: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of items attribute of the item.
    """

    number_of_pages: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of pages attribute of the item.
    """

    number_of_tracks: Optional[int] = attrs.field(
        default=None,
    )
    """
    The number of tracks attribute of the item.
    """

    operating_system: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The operating system attributes of the item.
    """

    optical_zoom: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    package_dimensions: Optional["DimensionType"] = attrs.field(
        default=None,
    )
    """
    The dimension type attribute of an item.
    """

    package_quantity: Optional[int] = attrs.field(
        default=None,
    )
    """
    The package quantity attribute of the item.
    """

    part_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The part number attribute of the item.
    """

    pegi_rating: Optional[str] = attrs.field(
        default=None,
    )
    """
    The PEGI rating attribute of the item.
    """

    platform: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The platform attributes of the item.
    """

    processor_count: Optional[int] = attrs.field(
        default=None,
    )
    """
    The processor count attribute of the item.
    """

    product_group: Optional[str] = attrs.field(
        default=None,
    )
    """
    The product group attribute of the item.
    """

    product_type_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The product type name attribute of the item.
    """

    product_type_subcategory: Optional[str] = attrs.field(
        default=None,
    )
    """
    The product type subcategory attribute of the item.
    """

    publication_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The publication date attribute of the item.
    """

    publisher: Optional[str] = attrs.field(
        default=None,
    )
    """
    The publisher attribute of the item.
    """

    region_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The region code attribute of the item.
    """

    release_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The release date attribute of the item.
    """

    ring_size: Optional[str] = attrs.field(
        default=None,
    )
    """
    The ring size attribute of the item.
    """

    running_time: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    scent: Optional[str] = attrs.field(
        default=None,
    )
    """
    The scent attribute of the item.
    """

    season_sequence: Optional[str] = attrs.field(
        default=None,
    )
    """
    The season sequence attribute of the item.
    """

    seikodo_product_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Seikodo product code attribute of the item.
    """

    shaft_material: Optional[str] = attrs.field(
        default=None,
    )
    """
    The shaft material attribute of the item.
    """

    size: Optional[str] = attrs.field(
        default=None,
    )
    """
    The size attribute of the item.
    """

    size_per_pearl: Optional[str] = attrs.field(
        default=None,
    )
    """
    The size per pearl attribute of the item.
    """

    small_image: Optional["Image"] = attrs.field(
        default=None,
    )
    """
    The image attribute of the item.
    """

    studio: Optional[str] = attrs.field(
        default=None,
    )
    """
    The studio attribute of the item.
    """

    subscription_length: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    system_memory_size: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    system_memory_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The system memory type attribute of the item.
    """

    theatrical_release_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The theatrical release date attribute of the item.
    """

    title: Optional[str] = attrs.field(
        default=None,
    )
    """
    The title attribute of the item.
    """

    total_diamond_weight: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    total_gem_weight: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    warranty: Optional[str] = attrs.field(
        default=None,
    )
    """
    The warranty attribute of the item.
    """

    weee_tax_value: Optional["Price"] = attrs.field(
        default=None,
    )
    """
    The price attribute of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Categories:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _categories_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Categories(**data)

    product_category_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the product category (or browse node).
    """

    product_category_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the product category (or browse node).
    """

    parent: Optional["CategoriesParent"] = attrs.field(
        default=None,
    )
    """
    The parent product category.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CategoriesParent:
    """
    The parent product category.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _categories_parent_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CategoriesParent(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreatorType:
    """
    The creator type attribute of an item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _creator_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreatorType(**data)

    role: Optional[str] = attrs.field(
        default=None,
    )
    """
    The role of the value.
    """

    value: Optional[str] = attrs.field(
        default=None,
    )
    """
    The value of the attribute.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DecimalWithUnits:
    """
    The decimal value and unit.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _decimal_with_units_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return DecimalWithUnits(**data)

    units: Optional[str] = attrs.field(
        default=None,
    )
    """
    The unit of the decimal value.
    """

    value: Optional[float] = attrs.field(
        default=None,
    )
    """
    The decimal value.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DimensionType:
    """
    The dimension type attribute of an item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _dimension_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return DimensionType(**data)

    height: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    length: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    weight: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    width: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetCatalogItemResponse:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_catalog_item_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetCatalogItemResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Item"] = attrs.field(
        default=None,
    )
    """
    An item in the Amazon catalog.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class IdentifierType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _identifier_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return IdentifierType(**data)

    marketplace_asin: Optional["ASINIdentifier"] = attrs.field(
        default=None,
    )

    skuidentifier: Optional["SellerSKUIdentifier"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class Image:
    """
    The image attribute of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _image_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Image(**data)

    height: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    url: Optional[str] = attrs.field(
        default=None,
    )
    """
    The image URL attribute of the item.
    """

    width: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    An item in the Amazon catalog.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Item(**data)

    attribute_sets: Optional[List["AttributeSetListType"]] = attrs.field(
        default=None,
    )
    """
    A list of attributes for the item.
    """

    identifiers: "IdentifierType" = attrs.field(
        default=None,
    )

    relationships: Optional[List["RelationshipType"]] = attrs.field(
        default=None,
    )
    """
    A list of variation relationship information, if applicable for the item.
    """

    sales_rankings: Optional[List["SalesRankType"]] = attrs.field(
        default=None,
    )
    """
    A list of sales rank information for the item by category.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LanguageType:
    """
    The language type attribute of an item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _language_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return LanguageType(**data)

    audio_format: Optional[str] = attrs.field(
        default=None,
    )
    """
    The audio format attribute of the item.
    """

    name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name attribute of the item.
    """

    type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The type attribute of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListCatalogCategoriesResponse:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _list_catalog_categories_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListCatalogCategoriesResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional[List["Categories"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListCatalogItemsResponse:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _list_catalog_items_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListCatalogItemsResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ListMatchingItemsResponse"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListMatchingItemsResponse:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _list_matching_items_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListMatchingItemsResponse(**data)

    items: Optional[List["Item"]] = attrs.field(
        default=None,
    )
    """
    A list of items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Price:
    """
    The price attribute of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _price_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Price(**data)

    amount: Optional[float] = attrs.field(
        default=None,
    )
    """
    The amount.
    """

    currency_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The currency code of the amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RelationshipType:
    """
    Specific variations of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _relationship_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return RelationshipType(**data)

    color: Optional[str] = attrs.field(
        default=None,
    )
    """
    The color variation of the item.
    """

    edition: Optional[str] = attrs.field(
        default=None,
    )
    """
    The edition variation of the item.
    """

    flavor: Optional[str] = attrs.field(
        default=None,
    )
    """
    The flavor variation of the item.
    """

    gem_type: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The gem type variations of the item.
    """

    golf_club_flex: Optional[str] = attrs.field(
        default=None,
    )
    """
    The golf club flex variation of an item.
    """

    golf_club_loft: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    hand_orientation: Optional[str] = attrs.field(
        default=None,
    )
    """
    The hand orientation variation of an item.
    """

    hardware_platform: Optional[str] = attrs.field(
        default=None,
    )
    """
    The hardware platform variation of an item.
    """

    identifiers: Optional["IdentifierType"] = attrs.field(
        default=None,
    )

    item_dimensions: Optional["DimensionType"] = attrs.field(
        default=None,
    )
    """
    The dimension type attribute of an item.
    """

    material_type: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The material type variations of an item.
    """

    metal_type: Optional[str] = attrs.field(
        default=None,
    )
    """
    The metal type variation of an item.
    """

    model: Optional[str] = attrs.field(
        default=None,
    )
    """
    The model variation of an item.
    """

    operating_system: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The operating system variations of an item.
    """

    package_quantity: Optional[int] = attrs.field(
        default=None,
    )
    """
    The package quantity variation of an item.
    """

    product_type_subcategory: Optional[str] = attrs.field(
        default=None,
    )
    """
    The product type subcategory variation of an item.
    """

    ring_size: Optional[str] = attrs.field(
        default=None,
    )
    """
    The ring size variation of an item.
    """

    scent: Optional[str] = attrs.field(
        default=None,
    )
    """
    The scent variation of an item.
    """

    shaft_material: Optional[str] = attrs.field(
        default=None,
    )
    """
    The shaft material variation of an item.
    """

    size: Optional[str] = attrs.field(
        default=None,
    )
    """
    The size variation of an item.
    """

    size_per_pearl: Optional[str] = attrs.field(
        default=None,
    )
    """
    The size per pearl variation of an item.
    """

    total_diamond_weight: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """

    total_gem_weight: Optional["DecimalWithUnits"] = attrs.field(
        default=None,
    )
    """
    The decimal value and unit.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SalesRankType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _sales_rank_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SalesRankType(**data)

    product_category_id: str = attrs.field(
        default=None,
    )
    """
    Identifies the item category from which the sales rank is taken.
    """

    rank: int = attrs.field(
        default=None,
    )
    """
    The sales rank of the item within the item category.

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerSKUIdentifier:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _seller_skuidentifier_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SellerSKUIdentifier(**data)

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier.
    """

    seller_id: str = attrs.field(
        default=None,
    )
    """
    The seller identifier submitted for the operation.
    """

    seller_sku: str = attrs.field(
        default=None,
    )
    """
    The seller stock keeping unit (SKU) of the item.
    """


_asinidentifier_name_convert = {
    "ASIN": "asin",
    "MarketplaceId": "marketplace_id",
}

_attribute_set_list_type_name_convert = {
    "Actor": "actor",
    "Artist": "artist",
    "AspectRatio": "aspect_ratio",
    "AudienceRating": "audience_rating",
    "Author": "author",
    "BackFinding": "back_finding",
    "BandMaterialType": "band_material_type",
    "Binding": "binding",
    "BlurayRegion": "bluray_region",
    "Brand": "brand",
    "CeroAgeRating": "cero_age_rating",
    "ChainType": "chain_type",
    "ClaspType": "clasp_type",
    "Color": "color",
    "CpuManufacturer": "cpu_manufacturer",
    "CpuSpeed": "cpu_speed",
    "CpuType": "cpu_type",
    "Creator": "creator",
    "Department": "department",
    "Director": "director",
    "DisplaySize": "display_size",
    "Edition": "edition",
    "EpisodeSequence": "episode_sequence",
    "EsrbAgeRating": "esrb_age_rating",
    "Feature": "feature",
    "Flavor": "flavor",
    "Format": "format",
    "GemType": "gem_type",
    "Genre": "genre",
    "GolfClubFlex": "golf_club_flex",
    "GolfClubLoft": "golf_club_loft",
    "HandOrientation": "hand_orientation",
    "HardDiskInterface": "hard_disk_interface",
    "HardDiskSize": "hard_disk_size",
    "HardwarePlatform": "hardware_platform",
    "HazardousMaterialType": "hazardous_material_type",
    "IsAdultProduct": "is_adult_product",
    "IsAutographed": "is_autographed",
    "IsEligibleForTradeIn": "is_eligible_for_trade_in",
    "IsMemorabilia": "is_memorabilia",
    "IssuesPerYear": "issues_per_year",
    "ItemDimensions": "item_dimensions",
    "ItemPartNumber": "item_part_number",
    "Label": "label",
    "Languages": "languages",
    "LegalDisclaimer": "legal_disclaimer",
    "ListPrice": "list_price",
    "Manufacturer": "manufacturer",
    "ManufacturerMaximumAge": "manufacturer_maximum_age",
    "ManufacturerMinimumAge": "manufacturer_minimum_age",
    "ManufacturerPartsWarrantyDescription": "manufacturer_parts_warranty_description",
    "MaterialType": "material_type",
    "MaximumResolution": "maximum_resolution",
    "MediaType": "media_type",
    "MetalStamp": "metal_stamp",
    "MetalType": "metal_type",
    "Model": "model",
    "NumberOfDiscs": "number_of_discs",
    "NumberOfIssues": "number_of_issues",
    "NumberOfItems": "number_of_items",
    "NumberOfPages": "number_of_pages",
    "NumberOfTracks": "number_of_tracks",
    "OperatingSystem": "operating_system",
    "OpticalZoom": "optical_zoom",
    "PackageDimensions": "package_dimensions",
    "PackageQuantity": "package_quantity",
    "PartNumber": "part_number",
    "PegiRating": "pegi_rating",
    "Platform": "platform",
    "ProcessorCount": "processor_count",
    "ProductGroup": "product_group",
    "ProductTypeName": "product_type_name",
    "ProductTypeSubcategory": "product_type_subcategory",
    "PublicationDate": "publication_date",
    "Publisher": "publisher",
    "RegionCode": "region_code",
    "ReleaseDate": "release_date",
    "RingSize": "ring_size",
    "RunningTime": "running_time",
    "Scent": "scent",
    "SeasonSequence": "season_sequence",
    "SeikodoProductCode": "seikodo_product_code",
    "ShaftMaterial": "shaft_material",
    "Size": "size",
    "SizePerPearl": "size_per_pearl",
    "SmallImage": "small_image",
    "Studio": "studio",
    "SubscriptionLength": "subscription_length",
    "SystemMemorySize": "system_memory_size",
    "SystemMemoryType": "system_memory_type",
    "TheatricalReleaseDate": "theatrical_release_date",
    "Title": "title",
    "TotalDiamondWeight": "total_diamond_weight",
    "TotalGemWeight": "total_gem_weight",
    "Warranty": "warranty",
    "WeeeTaxValue": "weee_tax_value",
}

_categories_name_convert = {
    "ProductCategoryId": "product_category_id",
    "ProductCategoryName": "product_category_name",
    "parent": "parent",
}

_categories_parent_name_convert = {}

_creator_type_name_convert = {
    "Role": "role",
    "value": "value",
}

_decimal_with_units_name_convert = {
    "Units": "units",
    "value": "value",
}

_dimension_type_name_convert = {
    "Height": "height",
    "Length": "length",
    "Weight": "weight",
    "Width": "width",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_get_catalog_item_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_identifier_type_name_convert = {
    "MarketplaceASIN": "marketplace_asin",
    "SKUIdentifier": "skuidentifier",
}

_image_name_convert = {
    "Height": "height",
    "URL": "url",
    "Width": "width",
}

_item_name_convert = {
    "AttributeSets": "attribute_sets",
    "Identifiers": "identifiers",
    "Relationships": "relationships",
    "SalesRankings": "sales_rankings",
}

_language_type_name_convert = {
    "AudioFormat": "audio_format",
    "Name": "name",
    "Type": "type",
}

_list_catalog_categories_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_list_catalog_items_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_list_matching_items_response_name_convert = {
    "Items": "items",
}

_price_name_convert = {
    "Amount": "amount",
    "CurrencyCode": "currency_code",
}

_relationship_type_name_convert = {
    "Color": "color",
    "Edition": "edition",
    "Flavor": "flavor",
    "GemType": "gem_type",
    "GolfClubFlex": "golf_club_flex",
    "GolfClubLoft": "golf_club_loft",
    "HandOrientation": "hand_orientation",
    "HardwarePlatform": "hardware_platform",
    "Identifiers": "identifiers",
    "ItemDimensions": "item_dimensions",
    "MaterialType": "material_type",
    "MetalType": "metal_type",
    "Model": "model",
    "OperatingSystem": "operating_system",
    "PackageQuantity": "package_quantity",
    "ProductTypeSubcategory": "product_type_subcategory",
    "RingSize": "ring_size",
    "Scent": "scent",
    "ShaftMaterial": "shaft_material",
    "Size": "size",
    "SizePerPearl": "size_per_pearl",
    "TotalDiamondWeight": "total_diamond_weight",
    "TotalGemWeight": "total_gem_weight",
}

_sales_rank_type_name_convert = {
    "ProductCategoryId": "product_category_id",
    "Rank": "rank",
}

_seller_skuidentifier_name_convert = {
    "MarketplaceId": "marketplace_id",
    "SellerId": "seller_id",
    "SellerSKU": "seller_sku",
}


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
            self._get_catalog_item_responses,
        )
        return response

    _get_catalog_item_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("asin", "path"),
    )

    _get_catalog_item_responses = {
        200: GetCatalogItemResponse,
        400: GetCatalogItemResponse,
        401: GetCatalogItemResponse,
        403: GetCatalogItemResponse,
        404: GetCatalogItemResponse,
        429: GetCatalogItemResponse,
        500: GetCatalogItemResponse,
        503: GetCatalogItemResponse,
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
            self._list_catalog_categories_responses,
        )
        return response

    _list_catalog_categories_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("ASIN", "query"),
        ("SellerSKU", "query"),
    )

    _list_catalog_categories_responses = {
        200: ListCatalogCategoriesResponse,
        400: ListCatalogCategoriesResponse,
        401: ListCatalogCategoriesResponse,
        403: ListCatalogCategoriesResponse,
        404: ListCatalogCategoriesResponse,
        429: ListCatalogCategoriesResponse,
        500: ListCatalogCategoriesResponse,
        503: ListCatalogCategoriesResponse,
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
            self._list_catalog_items_responses,
        )
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

    _list_catalog_items_responses = {
        200: ListCatalogItemsResponse,
        400: ListCatalogItemsResponse,
        401: ListCatalogItemsResponse,
        403: ListCatalogItemsResponse,
        404: ListCatalogItemsResponse,
        429: ListCatalogItemsResponse,
        500: ListCatalogItemsResponse,
        503: ListCatalogItemsResponse,
    }
