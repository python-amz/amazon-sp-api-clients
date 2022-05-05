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

    brand_name: str = attrs.field()
    number_of_results: int = attrs.field()

    pass


@attrs.define
class ClassificationRefinement:

    classification_id: str = attrs.field()
    display_name: str = attrs.field()
    number_of_results: int = attrs.field()

    pass


@attrs.define
class Error:

    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:

    errors: list["Error"] = attrs.field()

    pass


@attrs.define
class Item:

    asin: "ItemAsin" = attrs.field()
    attributes: "ItemAttributes" = attrs.field()
    identifiers: "ItemIdentifiers" = attrs.field()
    images: "ItemImages" = attrs.field()
    product_types: "ItemProductTypes" = attrs.field()
    sales_ranks: "ItemSalesRanks" = attrs.field()
    summaries: "ItemSummaries" = attrs.field()
    variations: "ItemVariations" = attrs.field()
    vendor_details: "ItemVendorDetails" = attrs.field()
    pass


@attrs.define
class ItemAsin:

    pass


@attrs.define
class ItemAttributes:

    pass


@attrs.define
class ItemIdentifier:

    identifier: str = attrs.field()
    identifier_type: str = attrs.field()

    pass


@attrs.define
class ItemIdentifiers:

    pass


@attrs.define
class ItemIdentifiersByMarketplace:

    identifiers: list["ItemIdentifier"] = attrs.field()
    marketplace_id: str = attrs.field()

    pass


@attrs.define
class ItemImage:

    height: int = attrs.field()
    link: str = attrs.field()
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
    ] = attrs.field()
    # {'example': 'MAIN'}
    width: int = attrs.field()

    pass


@attrs.define
class ItemImages:

    pass


@attrs.define
class ItemImagesByMarketplace:

    images: list["ItemImage"] = attrs.field()
    marketplace_id: str = attrs.field()

    pass


@attrs.define
class ItemProductTypeByMarketplace:

    marketplace_id: str = attrs.field()
    product_type: str = attrs.field()
    # {'example': 'LUGGAGE'}

    pass


@attrs.define
class ItemProductTypes:

    pass


@attrs.define
class ItemSalesRank:

    link: str = attrs.field()
    rank: int = attrs.field()
    title: str = attrs.field()

    pass


@attrs.define
class ItemSalesRanks:

    pass


@attrs.define
class ItemSalesRanksByMarketplace:

    marketplace_id: str = attrs.field()
    ranks: list["ItemSalesRank"] = attrs.field()

    pass


@attrs.define
class ItemSearchResults:

    items: list["Item"] = attrs.field()
    number_of_results: int = attrs.field()

    pagination: "Pagination" = attrs.field()
    refinements: "Refinements" = attrs.field()
    pass


@attrs.define
class ItemSummaries:

    pass


@attrs.define
class ItemSummaryByMarketplace:

    brand_name: str = attrs.field()
    browse_node: str = attrs.field()
    color_name: str = attrs.field()
    item_name: str = attrs.field()
    manufacturer: str = attrs.field()
    marketplace_id: str = attrs.field()
    model_number: str = attrs.field()
    size_name: str = attrs.field()
    style_name: str = attrs.field()

    pass


@attrs.define
class ItemVariations:

    pass


@attrs.define
class ItemVariationsByMarketplace:

    asins: list[str] = attrs.field()
    marketplace_id: str = attrs.field()
    variation_type: Union[Literal["PARENT"], Literal["CHILD"]] = attrs.field()
    # {'example': 'PARENT'}

    pass


@attrs.define
class ItemVendorDetails:

    pass


@attrs.define
class ItemVendorDetailsByMarketplace:

    brand_code: str = attrs.field()
    category_code: str = attrs.field()
    manufacturer_code: str = attrs.field()
    manufacturer_code_parent: str = attrs.field()
    marketplace_id: str = attrs.field()
    product_group: str = attrs.field()
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
    ] = attrs.field()
    subcategory_code: str = attrs.field()

    pass


@attrs.define
class Pagination:

    next_token: str = attrs.field()
    previous_token: str = attrs.field()

    pass


@attrs.define
class Refinements:

    brands: list["BrandRefinement"] = attrs.field()
    classifications: list["ClassificationRefinement"] = attrs.field()

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
