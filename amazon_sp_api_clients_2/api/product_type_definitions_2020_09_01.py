"""
Selling Partner API for Product Type Definitions
=============================================================================================

The Selling Partner API for Product Type Definitions provides programmatic access to attribute and data requirements for product types in the Amazon catalog. Use this API to return the JSON Schema for a product type that you can then use with other Selling Partner APIs, such as the Selling Partner API for Listings Items, the Selling Partner API for Catalog Items, and the Selling Partner API for Feeds (for JSON-based listing feeds).

For more information, see the [Product Type Definitions API Use Case Guide](doc:product-type-api-use-case-guide).
API Version: 2020-09-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


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
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_list_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ErrorList(**data)

    errors: List["Error"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductType:
    """
    An Amazon product type with a definition available.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _product_type_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ProductType(**data)

    marketplace_ids: List[str] = attrs.field(
        default=None,
    )
    """
    The Amazon marketplace identifiers for which the product type definition is available.
    """

    name: str = attrs.field(
        default=None,
    )
    """
    The name of the Amazon product type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductTypeDefinition:
    """
    A product type definition represents the attributes and data requirements for a product type in the Amazon catalog. Product type definitions are used interchangeably between the Selling Partner API for Listings Items, Selling Partner API for Catalog Items, and JSON-based listings feeds in the Selling Partner API for Feeds.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _product_type_definition_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ProductTypeDefinition(**data)

    locale: str = attrs.field(
        default=None,
    )
    """
    Locale of the display elements contained in the product type definition.
    """

    marketplace_ids: List[str] = attrs.field(
        default=None,
    )
    """
    Amazon marketplace identifiers for which the product type definition is applicable.
    """

    meta_schema: Optional["SchemaLink"] = attrs.field(
        default=None,
    )

    product_type: str = attrs.field(
        default=None,
    )
    """
    The name of the Amazon product type that this product type definition applies to.
    """

    product_type_version: "ProductTypeVersion" = attrs.field(
        default=None,
    )
    """
    The version details for an Amazon product type.
    """

    property_groups: "ProductTypeDefinitionPropertyGroups" = attrs.field(
        default=None,
    )
    """
    Mapping of property group names to property groups. Property groups represent logical groupings of schema properties that can be used for display or informational purposes.
    """

    requirements: Union[
        Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]
    ] = attrs.field(
        default=None,
    )
    """
    Name of the requirements set represented in this product type definition.
    """

    requirements_enforced: Union[Literal["ENFORCED"], Literal["NOT_ENFORCED"]] = attrs.field(
        default=None,
    )
    """
    Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all of the required attributes being present (such as for partial updates).
    """

    schema: "SchemaLink" = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=False)
class ProductTypeDefinitionPropertyGroups:
    """
    Mapping of property group names to property groups. Property groups represent logical groupings of schema properties that can be used for display or informational purposes.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _product_type_definition_property_groups_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ProductTypeDefinitionPropertyGroups(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductTypeList:
    """
    A list of Amazon product types with definitions available.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _product_type_list_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ProductTypeList(**data)

    product_types: List["ProductType"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductTypeVersion:
    """
    The version details for an Amazon product type.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _product_type_version_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ProductTypeVersion(**data)

    latest: bool = attrs.field(
        default=None,
    )
    """
    When true, the version indicated by the version identifier is the latest available for the Amazon product type.
    """

    release_candidate: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the version indicated by the version identifier is the prerelease (release candidate) for the Amazon product type.
    """

    version: str = attrs.field(
        default=None,
    )
    """
    Version identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PropertyGroup:
    """
    A property group represents a logical grouping of schema properties that can be used for display or informational purposes.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _property_group_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PropertyGroup(**data)

    description: Optional[str] = attrs.field(
        default=None,
    )
    """
    The description of the property group.
    """

    property_names: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The names of the schema properties for the property group.
    """

    title: Optional[str] = attrs.field(
        default=None,
    )
    """
    The display label of the property group.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SchemaLink:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _schema_link_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SchemaLink(**data)

    checksum: str = attrs.field(
        default=None,
    )
    """
    Checksum hash of the schema (Base64 MD5). Can be used to verify schema contents, identify changes between schema versions, and for caching.
    """

    link: "SchemaLinkLink" = attrs.field(
        default=None,
    )
    """
    Link to retrieve the schema.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SchemaLinkLink:
    """
    Link to retrieve the schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _schema_link_link_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SchemaLinkLink(**data)

    resource: str = attrs.field(
        default=None,
    )
    """
    URI resource for the link.
    """

    verb: Union[Literal["GET"]] = attrs.field(
        default=None,
    )
    """
    HTTP method for the link operation.
    """


_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_product_type_name_convert = {
    "marketplaceIds": "marketplace_ids",
    "name": "name",
}

_product_type_definition_name_convert = {
    "locale": "locale",
    "marketplaceIds": "marketplace_ids",
    "metaSchema": "meta_schema",
    "productType": "product_type",
    "productTypeVersion": "product_type_version",
    "propertyGroups": "property_groups",
    "requirements": "requirements",
    "requirementsEnforced": "requirements_enforced",
    "schema": "schema",
}

_product_type_definition_property_groups_name_convert = {}

_product_type_list_name_convert = {
    "productTypes": "product_types",
}

_product_type_version_name_convert = {
    "latest": "latest",
    "releaseCandidate": "release_candidate",
    "version": "version",
}

_property_group_name_convert = {
    "description": "description",
    "propertyNames": "property_names",
    "title": "title",
}

_schema_link_name_convert = {
    "checksum": "checksum",
    "link": "link",
}

_schema_link_link_name_convert = {
    "resource": "resource",
    "verb": "verb",
}


class ProductTypeDefinitions20200901Client(BaseClient):
    def get_definitions_product_type(
        self,
        product_type: str,
        marketplace_ids: List[str],
        seller_id: str = None,
        product_type_version: str = None,
        requirements: Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]] = None,
        requirements_enforced: Union[Literal["ENFORCED"], Literal["NOT_ENFORCED"]] = None,
        locale: Union[
            Literal["DEFAULT"],
            Literal["ar"],
            Literal["ar_AE"],
            Literal["de"],
            Literal["de_DE"],
            Literal["en"],
            Literal["en_AE"],
            Literal["en_AU"],
            Literal["en_CA"],
            Literal["en_GB"],
            Literal["en_IN"],
            Literal["en_SG"],
            Literal["en_US"],
            Literal["es"],
            Literal["es_ES"],
            Literal["es_MX"],
            Literal["es_US"],
            Literal["fr"],
            Literal["fr_CA"],
            Literal["fr_FR"],
            Literal["it"],
            Literal["it_IT"],
            Literal["ja"],
            Literal["ja_JP"],
            Literal["nl"],
            Literal["nl_NL"],
            Literal["pl"],
            Literal["pl_PL"],
            Literal["pt"],
            Literal["pt_BR"],
            Literal["pt_PT"],
            Literal["sv"],
            Literal["sv_SE"],
            Literal["tr"],
            Literal["tr_TR"],
            Literal["zh"],
            Literal["zh_CN"],
            Literal["zh_TW"],
        ] = None,
    ) -> Union[ErrorList, ProductTypeDefinition]:
        """
        Retrieve an Amazon product type definition.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            product_type: The Amazon product type name.
            seller_id: A selling partner identifier. When provided, seller-specific requirements and values are populated within the product type definition schema, such as brand names associated with the selling partner.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
                Note: This parameter is limited to one marketplaceId at this time.
            product_type_version: The version of the Amazon product type to retrieve. Defaults to "LATEST",. Prerelease versions of product type definitions may be retrieved with "RELEASE_CANDIDATE". If no prerelease version is currently available, the "LATEST" live version will be provided.
            requirements: The name of the requirements set to retrieve requirements for.
            requirements_enforced: Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all the required attributes being present (such as for partial updates).
            locale: Locale for retrieving display labels and other presentation details. Defaults to the default language of the first marketplace in the request.
        """
        url = "/definitions/2020-09-01/productTypes/{productType}"
        values = (
            product_type,
            seller_id,
            marketplace_ids,
            product_type_version,
            requirements,
            requirements_enforced,
            locale,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_definitions_product_type_params,
            self._get_definitions_product_type_responses,
        )
        return response

    _get_definitions_product_type_params = (  # name, param in
        ("productType", "path"),
        ("sellerId", "query"),
        ("marketplaceIds", "query"),
        ("productTypeVersion", "query"),
        ("requirements", "query"),
        ("requirementsEnforced", "query"),
        ("locale", "query"),
    )

    _get_definitions_product_type_responses = {
        200: ProductTypeDefinition,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def search_definitions_product_types(
        self,
        marketplace_ids: List[str],
        keywords: List[str] = None,
    ) -> Union[ErrorList, ProductTypeList]:
        """
        Search for and return a list of Amazon product types that have definitions available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            keywords: A comma-delimited list of keywords to search product types by.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
        """
        url = "/definitions/2020-09-01/productTypes"
        values = (
            keywords,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._search_definitions_product_types_params,
            self._search_definitions_product_types_responses,
        )
        return response

    _search_definitions_product_types_params = (  # name, param in
        ("keywords", "query"),
        ("marketplaceIds", "query"),
    )

    _search_definitions_product_types_responses = {
        200: ProductTypeList,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
