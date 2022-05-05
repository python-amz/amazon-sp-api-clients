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
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    pass


@attrs.define
class AttributeSetList:

    pass


@attrs.define
class AttributeSetListType:

    actor: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    artist: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    aspect_ratio: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    audience_rating: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    author: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    back_finding: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    band_material_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    binding: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    bluray_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    brand: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    cero_age_rating: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    chain_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    clasp_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    color: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    cpu_manufacturer: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    cpu_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    creator: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Reference(ref='#/components/schemas/CreatorType'), 'type': 'array'}
    department: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    director: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    edition: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    episode_sequence: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    esrb_age_rating: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    feature: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    flavor: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    format: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    gem_type: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    genre: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    golf_club_flex: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    hand_orientation: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    hard_disk_interface: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    hardware_platform: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    hazardous_material_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    is_adult_product: bool
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'boolean'}
    is_autographed: bool
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'boolean'}
    is_eligible_for_trade_in: bool
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'boolean'}
    is_memorabilia: bool
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'boolean'}
    issues_per_year: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    item_part_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    label: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    languages: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Reference(ref='#/components/schemas/LanguageType'), 'type': 'array'}
    legal_disclaimer: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    manufacturer: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    manufacturer_parts_warranty_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    material_type: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    media_type: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    metal_stamp: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    metal_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    model: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    number_of_discs: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    number_of_issues: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    number_of_items: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    number_of_pages: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    number_of_tracks: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    operating_system: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    package_quantity: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    part_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    pegi_rating: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    platform: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    processor_count: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    product_group: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    product_type_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    product_type_subcategory: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    publication_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    publisher: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    region_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    release_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    ring_size: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    scent: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    season_sequence: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    seikodo_product_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    shaft_material: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    size: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    size_per_pearl: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    studio: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    system_memory_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    theatrical_release_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    warranty: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    cpu_speed: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    display_size: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    golf_club_loft: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    hard_disk_size: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    item_dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/DimensionType', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    list_price: dict[str, Any]
    # {'ref': '#/components/schemas/Price', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    manufacturer_maximum_age: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    manufacturer_minimum_age: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    maximum_resolution: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    optical_zoom: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    package_dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/DimensionType', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    running_time: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    small_image: dict[str, Any]
    # {'ref': '#/components/schemas/Image', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    subscription_length: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    system_memory_size: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    total_diamond_weight: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    total_gem_weight: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    weee_tax_value: dict[str, Any]
    # {'ref': '#/components/schemas/Price', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class Categories:

    product_category_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    product_category_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    parent: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'properties': {}, 'type': 'object'}

    pass


@attrs.define
class CreatorType:

    role: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    value: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    pass


@attrs.define
class DecimalWithUnits:

    units: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    value: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'number'}

    pass


@attrs.define
class DimensionType:

    height: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    length: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    width: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetCatalogItemResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Item', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class IdentifierType:

    marketplace_asin: dict[str, Any]
    # {'ref': '#/components/schemas/ASINIdentifier', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    skuidentifier: dict[str, Any]
    # {'ref': '#/components/schemas/SellerSKUIdentifier', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class Image:

    url: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    height: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    width: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class Item:

    attribute_sets: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AttributeSetList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    identifiers: dict[str, Any]
    # {'ref': '#/components/schemas/IdentifierType', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    relationships: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RelationshipList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    sales_rankings: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SalesRankList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class ItemList:

    pass


@attrs.define
class LanguageType:

    audio_format: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    pass


@attrs.define
class ListCatalogCategoriesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    payload: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ListOfCategories', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class ListCatalogItemsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ListMatchingItemsResponse', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class ListMatchingItemsResponse:

    items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ItemList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class ListOfCategories:

    pass


@attrs.define
class Price:

    amount: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'number'}
    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    pass


@attrs.define
class RelationshipList:

    pass


@attrs.define
class RelationshipType:

    color: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    edition: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    flavor: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    gem_type: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    golf_club_flex: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    hand_orientation: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    hardware_platform: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    material_type: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    metal_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    model: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    operating_system: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    package_quantity: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'integer'}
    product_type_subcategory: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    ring_size: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    scent: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    shaft_material: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    size: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    size_per_pearl: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

    golf_club_loft: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    identifiers: dict[str, Any]
    # {'ref': '#/components/schemas/IdentifierType', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    item_dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/DimensionType', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    total_diamond_weight: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    total_gem_weight: dict[str, Any]
    # {'ref': '#/components/schemas/DecimalWithUnits', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>}
    pass


@attrs.define
class SalesRankList:

    pass


@attrs.define
class SalesRankType:

    product_category_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    rank: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'schema_format': 'int32', 'type': 'integer'}

    pass


@attrs.define
class SellerSKUIdentifier:

    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB310>, 'type': 'string'}

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
