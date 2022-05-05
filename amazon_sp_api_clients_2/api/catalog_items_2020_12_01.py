"""
Selling Partner API for Catalog Items
=============================================================================================

The Selling Partner API for Catalog Items provides programmatic access to information about items in the Amazon catalog.

For more information, see the [Catalog Items API Use Case Guide](doc:catalog-items-api-v2020-12-01-use-case-guide).
API Version: 2020-12-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class BrandRefinement:

    brand_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    number_of_results: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ClassificationRefinement:

    classification_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    display_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    number_of_results: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Error'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class Item:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemAsin'}
    attributes: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemAttributes'}
    identifiers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemIdentifiers'}
    images: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemImages'}
    product_types: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemProductTypes'}
    sales_ranks: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemSalesRanks'}
    summaries: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemSummaries'}
    variations: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemVariations'}
    vendor_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/ItemVendorDetails'}
    pass


@attrs.define
class ItemAsin:

    pass


@attrs.define
class ItemAttributes:

    pass


@attrs.define
class ItemIdentifier:

    identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    identifier_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemIdentifiers:

    pass


@attrs.define
class ItemIdentifiersByMarketplace:

    identifiers: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ItemIdentifier'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemImage:

    height: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    link: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    variant: Union[
        Literal["MAIN"],
        Literal["PT01"],
        Literal["PT02"],
        Literal["PT03"],
        Literal["PT04"],
        Literal["PT05"],
        Literal["PT06"],
        Literal["PT07"],
        Literal["PT08"],
        Literal["SWCH"],
    ]
    # {'example': 'MAIN', 'enum': ['MAIN', 'PT01', 'PT02', 'PT03', 'PT04', 'PT05', 'PT06', 'PT07', 'PT08', 'SWCH'], 'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    width: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemImages:

    pass


@attrs.define
class ItemImagesByMarketplace:

    images: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ItemImage'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemProductTypeByMarketplace:

    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    product_type: str
    # {'example': 'LUGGAGE', 'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemProductTypes:

    pass


@attrs.define
class ItemSalesRank:

    link: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    rank: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    title: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemSalesRanks:

    pass


@attrs.define
class ItemSalesRanksByMarketplace:

    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    ranks: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ItemSalesRank'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemSearchResults:

    items: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Item'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    number_of_results: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pagination: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/Pagination'}
    refinements: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>, 'ref': '#/components/schemas/Refinements'}
    pass


@attrs.define
class ItemSummaries:

    pass


@attrs.define
class ItemSummaryByMarketplace:

    brand_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    browse_node: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    color_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    item_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    manufacturer: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    model_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    size_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    style_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemVariations:

    pass


@attrs.define
class ItemVariationsByMarketplace:

    asins: list[str]
    # {'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    variation_type: Union[Literal["PARENT"], Literal["CHILD"]]
    # {'example': 'PARENT', 'enum': ['PARENT', 'CHILD'], 'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class ItemVendorDetails:

    pass


@attrs.define
class ItemVendorDetailsByMarketplace:

    brand_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    category_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    manufacturer_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    manufacturer_code_parent: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    product_group: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    replenishment_category: Union[
        Literal["ALLOCATED"],
        Literal["BASIC_REPLENISHMENT"],
        Literal["IN_SEASON"],
        Literal["LIMITED_REPLENISHMENT"],
        Literal["MANUFACTURER_OUT_OF_STOCK"],
        Literal["NEW_PRODUCT"],
        Literal["NON_REPLENISHABLE"],
        Literal["NON_STOCKUPABLE"],
        Literal["OBSOLETE"],
        Literal["PLANNED_REPLENISHMENT"],
    ]
    # {'enum': ['ALLOCATED', 'BASIC_REPLENISHMENT', 'IN_SEASON', 'LIMITED_REPLENISHMENT', 'MANUFACTURER_OUT_OF_STOCK', 'NEW_PRODUCT', 'NON_REPLENISHABLE', 'NON_STOCKUPABLE', 'OBSOLETE', 'PLANNED_REPLENISHMENT'], 'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    subcategory_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class Pagination:

    next_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    previous_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


@attrs.define
class Refinements:

    brands: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/BrandRefinement'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}
    classifications: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ClassificationRefinement'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x000001C2EE8CB310>}

    pass


class CatalogItems20201201Client(BaseClient):
    def get_catalog_item(
        self,
        asin: str,
        marketplace_ids: list[str],
        included_data: list[
            Union[
                Literal["attributes"],
                Literal["identifiers"],
                Literal["images"],
                Literal["productTypes"],
                Literal["salesRanks"],
                Literal["summaries"],
                Literal["variations"],
                Literal["vendorDetails"],
            ]
        ] = None,
        locale: str = None,
    ):
        """
        Retrieves details for an item in the Amazon catalog.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 5 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers. Data sets in the response contain data only for the specified marketplaces.
            included_data: A comma-delimited list of data sets to include in the response. Default: summaries.
            locale: Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.
        """
        url = "/catalog/2020-12-01/items/{asin}"
        values = (
            asin,
            marketplace_ids,
            included_data,
            locale,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_catalog_item_params)
        return response

    _get_catalog_item_params = (  # name, param in
        ("asin", "path"),
        ("marketplaceIds", "query"),
        ("includedData", "query"),
        ("locale", "query"),
    )

    def search_catalog_items(
        self,
        keywords: list[str],
        marketplace_ids: list[str],
        included_data: list[
            Union[
                Literal["identifiers"],
                Literal["images"],
                Literal["productTypes"],
                Literal["salesRanks"],
                Literal["summaries"],
                Literal["variations"],
                Literal["vendorDetails"],
            ]
        ] = None,
        brand_names: list[str] = None,
        classification_ids: list[str] = None,
        page_size: int = None,
        page_token: str = None,
        keywords_locale: str = None,
        locale: str = None,
    ):
        """
        Search for and return a list of Amazon catalog items and associated information.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 5 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            keywords: A comma-delimited list of words or item identifiers to search the Amazon catalog for.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            included_data: A comma-delimited list of data sets to include in the response. Default: summaries.
            brand_names: A comma-delimited list of brand names to limit the search to.
            classification_ids: A comma-delimited list of classification identifiers to limit the search to.
            page_size: Number of results to be returned per page.
            page_token: A token to fetch a certain page when there are multiple pages worth of results.
            keywords_locale: The language the keywords are provided in. Defaults to the primary locale of the marketplace.
            locale: Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.
        """
        url = "/catalog/2020-12-01/items"
        values = (
            keywords,
            marketplace_ids,
            included_data,
            brand_names,
            classification_ids,
            page_size,
            page_token,
            keywords_locale,
            locale,
        )
        response = self._parse_args_and_request(url, "GET", values, self._search_catalog_items_params)
        return response

    _search_catalog_items_params = (  # name, param in
        ("keywords", "query"),
        ("marketplaceIds", "query"),
        ("includedData", "query"),
        ("brandNames", "query"),
        ("classificationIds", "query"),
        ("pageSize", "query"),
        ("pageToken", "query"),
        ("keywordsLocale", "query"),
        ("locale", "query"),
    )
