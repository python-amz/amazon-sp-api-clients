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

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductType:
    """
    An Amazon product type with a definition available.
    """

    marketplace_ids: List[str] = attrs.field()
    """
    The Amazon marketplace identifiers for which the product type definition is available.
    """

    name: str = attrs.field()
    """
    The name of the Amazon product type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductTypeDefinition:
    """
    A product type definition represents the attributes and data requirements for a product type in the Amazon catalog. Product type definitions are used interchangeably between the Selling Partner API for Listings Items, Selling Partner API for Catalog Items, and JSON-based listings feeds in the Selling Partner API for Feeds.
    """

    locale: str = attrs.field()
    """
    Locale of the display elements contained in the product type definition.
    """

    marketplace_ids: List[str] = attrs.field()
    """
    Amazon marketplace identifiers for which the product type definition is applicable.
    """

    meta_schema: Optional["SchemaLink"] = attrs.field()

    product_type: str = attrs.field()
    """
    The name of the Amazon product type that this product type definition applies to.
    """

    product_type_version: "ProductTypeVersion" = attrs.field()
    """
    The version details for an Amazon product type.
    """

    property_groups: "ProductTypeDefinitionPropertyGroups" = attrs.field()
    """
    Mapping of property group names to property groups. Property groups represent logical groupings of schema properties that can be used for display or informational purposes.
    """

    requirements: Union[
        Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]
    ] = attrs.field()
    """
    Name of the requirements set represented in this product type definition.
    """

    requirements_enforced: Union[Literal["ENFORCED"], Literal["NOT_ENFORCED"]] = attrs.field()
    """
    Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all of the required attributes being present (such as for partial updates).
    """

    schema: "SchemaLink" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=False)
class ProductTypeDefinitionPropertyGroups:
    """
    Mapping of property group names to property groups. Property groups represent logical groupings of schema properties that can be used for display or informational purposes.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductTypeList:
    """
    A list of Amazon product types with definitions available.
    """

    product_types: List["ProductType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductTypeVersion:
    """
    The version details for an Amazon product type.
    """

    latest: bool = attrs.field()
    """
    When true, the version indicated by the version identifier is the latest available for the Amazon product type.
    """

    release_candidate: Optional[bool] = attrs.field()
    """
    When true, the version indicated by the version identifier is the prerelease (release candidate) for the Amazon product type.
    """

    version: str = attrs.field()
    """
    Version identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PropertyGroup:
    """
    A property group represents a logical grouping of schema properties that can be used for display or informational purposes.
    """

    description: Optional[str] = attrs.field()
    """
    The description of the property group.
    """

    property_names: Optional[List[str]] = attrs.field()
    """
    The names of the schema properties for the property group.
    """

    title: Optional[str] = attrs.field()
    """
    The display label of the property group.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SchemaLink:

    checksum: str = attrs.field()
    """
    Checksum hash of the schema (Base64 MD5). Can be used to verify schema contents, identify changes between schema versions, and for caching.
    """

    link: "SchemaLinkLink" = attrs.field()
    """
    Link to retrieve the schema.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SchemaLinkLink:
    """
    Link to retrieve the schema.
    """

    resource: str = attrs.field()
    """
    URI resource for the link.
    """

    verb: Union[Literal["GET"]] = attrs.field()
    """
    HTTP method for the link operation.
    """


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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

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
        (200, "application/json"): ProductTypeDefinition,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _search_definitions_product_types_params = (  # name, param in
        ("keywords", "query"),
        ("marketplaceIds", "query"),
    )

    _search_definitions_product_types_responses = {
        (200, "application/json"): ProductTypeList,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }
