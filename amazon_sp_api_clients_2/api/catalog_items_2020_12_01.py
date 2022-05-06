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
from datetime import date, datetime


@attrs.define
class BrandRefinement:

    brand_name: str = attrs.field(
        kw_only=True,
    )
    """
    Brand name. For display and can be used as a search refinement.
    """

    number_of_results: int = attrs.field(
        kw_only=True,
    )
    """
    The estimated number of results that would still be returned if refinement key applied.
    """

    pass


@attrs.define
class ClassificationRefinement:

    classification_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifier for the classification that can be used for search refinement purposes.
    """

    display_name: str = attrs.field(
        kw_only=True,
    )
    """
    Display name for the classification.
    """

    number_of_results: int = attrs.field(
        kw_only=True,
    )
    """
    The estimated number of results that would still be returned if refinement key applied.
    """

    pass


@attrs.define
class Error:

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
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """

    pass


@attrs.define
class ErrorList:

    errors: List["Error"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Item:

    asin: "ItemAsin" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    attributes: "ItemAttributes" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    identifiers: "ItemIdentifiers" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    images: "ItemImages" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    product_types: "ItemProductTypes" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    sales_ranks: "ItemSalesRanks" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    summaries: "ItemSummaries" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    variations: "ItemVariations" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    vendor_details: "ItemVendorDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ItemAsin:

    pass


@attrs.define
class ItemAttributes:

    pass


@attrs.define
class ItemIdentifier:

    identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Identifier.
    """

    identifier_type: str = attrs.field(
        kw_only=True,
    )
    """
    Type of identifier, such as UPC, EAN, or ISBN.
    """

    pass


@attrs.define
class ItemIdentifiers:

    pass


@attrs.define
class ItemIdentifiersByMarketplace:

    identifiers: List["ItemIdentifier"] = attrs.field(
        kw_only=True,
    )
    """
    Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    pass


@attrs.define
class ItemImage:

    height: int = attrs.field(
        kw_only=True,
    )
    """
    Height of the image in pixels.
    """

    link: str = attrs.field(
        kw_only=True,
    )
    """
    Link, or URL, for the image.
    """

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
    ] = attrs.field(
        kw_only=True,
    )
    """
    Variant of the image, such as MAIN or PT01.

    Extra fields:
    {'example': 'MAIN'}
    """

    width: int = attrs.field(
        kw_only=True,
    )
    """
    Width of the image in pixels.
    """

    pass


@attrs.define
class ItemImages:

    pass


@attrs.define
class ItemImagesByMarketplace:

    images: List["ItemImage"] = attrs.field(
        kw_only=True,
    )
    """
    Images for an item in the Amazon catalog for the indicated Amazon marketplace.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    pass


@attrs.define
class ItemProductTypeByMarketplace:

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    product_type: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the product type associated with the Amazon catalog item.

    Extra fields:
    {'example': 'LUGGAGE'}
    """

    pass


@attrs.define
class ItemProductTypes:

    pass


@attrs.define
class ItemSalesRank:

    link: str = attrs.field(
        kw_only=True,
    )
    """
    Corresponding Amazon retail website link, or URL, for the sales rank.
    """

    rank: int = attrs.field(
        kw_only=True,
    )
    """
    Sales rank value.
    """

    title: str = attrs.field(
        kw_only=True,
    )
    """
    Title, or name, of the sales rank.
    """

    pass


@attrs.define
class ItemSalesRanks:

    pass


@attrs.define
class ItemSalesRanksByMarketplace:

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    ranks: List["ItemSalesRank"] = attrs.field(
        kw_only=True,
    )
    """
    Sales ranks of an Amazon catalog item for an Amazon marketplace.
    """

    pass


@attrs.define
class ItemSearchResults:

    items: List["Item"] = attrs.field(
        kw_only=True,
    )
    """
    A list of items from the Amazon catalog.
    """

    number_of_results: int = attrs.field(
        kw_only=True,
    )
    """
    The estimated total number of products matched by the search query (only results up to the page count limit will be returned per request regardless of the number found).
        Note: The maximum number of items (ASINs) that can be returned and paged through is 1000.
    """

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    refinements: "Refinements" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ItemSummaries:

    pass


@attrs.define
class ItemSummaryByMarketplace:

    brand_name: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the brand associated with an Amazon catalog item.
    """

    browse_node: str = attrs.field(
        kw_only=True,
    )
    """
    Identifier of the browse node associated with an Amazon catalog item.
    """

    color_name: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the color associated with an Amazon catalog item.
    """

    item_name: str = attrs.field(
        kw_only=True,
    )
    """
    Name, or title, associated with an Amazon catalog item.
    """

    manufacturer: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the manufacturer associated with an Amazon catalog item.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    model_number: str = attrs.field(
        kw_only=True,
    )
    """
    Model number associated with an Amazon catalog item.
    """

    size_name: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the size associated with an Amazon catalog item.
    """

    style_name: str = attrs.field(
        kw_only=True,
    )
    """
    Name of the style associated with an Amazon catalog item.
    """

    pass


@attrs.define
class ItemVariations:

    pass


@attrs.define
class ItemVariationsByMarketplace:

    asins: List[str] = attrs.field(
        kw_only=True,
    )
    """
    Identifiers (ASINs) of the related items.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    variation_type: Union[Literal["PARENT"], Literal["CHILD"]] = attrs.field(
        kw_only=True,
    )
    """
    Type of variation relationship of the Amazon catalog item in the request to the related item(s): "PARENT" or "CHILD".

    Extra fields:
    {'example': 'PARENT'}
    """

    pass


@attrs.define
class ItemVendorDetails:

    pass


@attrs.define
class ItemVendorDetailsByMarketplace:

    brand_code: str = attrs.field(
        kw_only=True,
    )
    """
    Brand code associated with an Amazon catalog item.
    """

    category_code: str = attrs.field(
        kw_only=True,
    )
    """
    Product category associated with an Amazon catalog item.
    """

    manufacturer_code: str = attrs.field(
        kw_only=True,
    )
    """
    Manufacturer code associated with an Amazon catalog item.
    """

    manufacturer_code_parent: str = attrs.field(
        kw_only=True,
    )
    """
    Parent vendor code of the manufacturer code.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    product_group: str = attrs.field(
        kw_only=True,
    )
    """
    Product group associated with an Amazon catalog item.
    """

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
    ] = attrs.field(
        kw_only=True,
    )
    """
    Replenishment category associated with an Amazon catalog item.
    """

    subcategory_code: str = attrs.field(
        kw_only=True,
    )
    """
    Product subcategory associated with an Amazon catalog item.
    """

    pass


@attrs.define
class Pagination:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    A token that can be used to fetch the next page.
    """

    previous_token: str = attrs.field(
        kw_only=True,
    )
    """
    A token that can be used to fetch the previous page.
    """

    pass


@attrs.define
class Refinements:

    brands: List["BrandRefinement"] = attrs.field(
        kw_only=True,
    )
    """
    Brand search refinements.
    """

    classifications: List["ClassificationRefinement"] = attrs.field(
        kw_only=True,
    )
    """
    Classification search refinements.
    """

    pass


class CatalogItems20201201Client(BaseClient):
    def get_catalog_item(
        self,
        asin: str,
        marketplace_ids: List[str],
        included_data: List[
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
        keywords: List[str],
        marketplace_ids: List[str],
        included_data: List[
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
        brand_names: List[str] = None,
        classification_ids: List[str] = None,
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
