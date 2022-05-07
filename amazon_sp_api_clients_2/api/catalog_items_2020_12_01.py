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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class BrandRefinement:
    """
    Description of a brand that can be used to get more fine-grained search results.
    """

    brand_name: str = attrs.field()
    """
    Brand name. For display and can be used as a search refinement.
    """

    number_of_results: int = attrs.field()
    """
    The estimated number of results that would still be returned if refinement key applied.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ClassificationRefinement:
    """
    Description of a classification that can be used to get more fine-grained search results.
    """

    classification_id: str = attrs.field()
    """
    Identifier for the classification that can be used for search refinement purposes.
    """

    display_name: str = attrs.field()
    """
    Display name for the classification.
    """

    number_of_results: int = attrs.field()
    """
    The estimated number of results that would still be returned if refinement key applied.
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
class Item:
    """
    An item in the Amazon catalog.
    """

    asin: "ItemAsin" = attrs.field()
    """
    Amazon Standard Identification Number (ASIN) is the unique identifier for an item in the Amazon catalog.
    """

    attributes: Optional["ItemAttributes"] = attrs.field()
    """
    A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.
    """

    identifiers: Optional[List["ItemIdentifiersByMarketplace"]] = attrs.field()
    """
    Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    """

    images: Optional[List["ItemImagesByMarketplace"]] = attrs.field()
    """
    Images for an item in the Amazon catalog. All image variants are provided to brand owners. Otherwise, a thumbnail of the "MAIN" image variant is provided.
    """

    product_types: Optional[List["ItemProductTypeByMarketplace"]] = attrs.field()
    """
    Product types associated with the Amazon catalog item.
    """

    sales_ranks: Optional[List["ItemSalesRanksByMarketplace"]] = attrs.field()
    """
    Sales ranks of an Amazon catalog item.
    """

    summaries: Optional[List["ItemSummaryByMarketplace"]] = attrs.field()
    """
    Summary details of an Amazon catalog item.
    """

    variations: Optional[List["ItemVariationsByMarketplace"]] = attrs.field()
    """
    Variation details by marketplace for an Amazon catalog item (variation relationships).
    """

    vendor_details: Optional[List["ItemVendorDetailsByMarketplace"]] = attrs.field()
    """
    Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemAsin:
    """
    Amazon Standard Identification Number (ASIN) is the unique identifier for an item in the Amazon catalog.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemAttributes:
    """
    A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemIdentifier:
    """
    Identifier associated with the item in the Amazon catalog, such as a UPC or EAN identifier.
    """

    identifier: str = attrs.field()
    """
    Identifier.
    """

    identifier_type: str = attrs.field()
    """
    Type of identifier, such as UPC, EAN, or ISBN.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemIdentifiersByMarketplace:
    """
    Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """

    identifiers: List["ItemIdentifier"] = attrs.field()
    """
    Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemImage:
    """
    Image for an item in the Amazon catalog.
    """

    height: int = attrs.field()
    """
    Height of the image in pixels.
    """

    link: str = attrs.field()
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
    ] = attrs.field()
    """
    Variant of the image, such as MAIN or PT01.

    Extra fields:
    {'example': 'MAIN'}
    """

    width: int = attrs.field()
    """
    Width of the image in pixels.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemImagesByMarketplace:
    """
    Images for an item in the Amazon catalog for the indicated Amazon marketplace.
    """

    images: List["ItemImage"] = attrs.field()
    """
    Images for an item in the Amazon catalog for the indicated Amazon marketplace.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemProductTypeByMarketplace:
    """
    Product type associated with the Amazon catalog item for the indicated Amazon marketplace.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    Amazon marketplace identifier.
    """

    product_type: Optional[str] = attrs.field()
    """
    Name of the product type associated with the Amazon catalog item.

    Extra fields:
    {'example': 'LUGGAGE'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemSalesRank:
    """
    Sales rank of an Amazon catalog item.
    """

    link: Optional[str] = attrs.field()
    """
    Corresponding Amazon retail website link, or URL, for the sales rank.
    """

    rank: int = attrs.field()
    """
    Sales rank value.
    """

    title: str = attrs.field()
    """
    Title, or name, of the sales rank.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemSalesRanksByMarketplace:
    """
    Sales ranks of an Amazon catalog item for the indicated Amazon marketplace.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """

    ranks: List["ItemSalesRank"] = attrs.field()
    """
    Sales ranks of an Amazon catalog item for an Amazon marketplace.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemSearchResults:
    """
    Items in the Amazon catalog and search related metadata.
    """

    items: List["Item"] = attrs.field()
    """
    A list of items from the Amazon catalog.
    """

    number_of_results: int = attrs.field()
    """
    The estimated total number of products matched by the search query (only results up to the page count limit will be returned per request regardless of the number found).
        Note: The maximum number of items (ASINs) that can be returned and paged through is 1000.
    """

    pagination: "Pagination" = attrs.field()
    """
    When a request produces a response that exceeds the pageSize, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the nextToken value or the previousToken value as the pageToken parameter in the next request. When you receive the last page, there will be no nextToken key in the pagination object.
    """

    refinements: "Refinements" = attrs.field()
    """
    Search refinements.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemSummaryByMarketplace:
    """
    Summary details of an Amazon catalog item for the indicated Amazon marketplace.
    """

    brand_name: Optional[str] = attrs.field()
    """
    Name of the brand associated with an Amazon catalog item.
    """

    browse_node: Optional[str] = attrs.field()
    """
    Identifier of the browse node associated with an Amazon catalog item.
    """

    color_name: Optional[str] = attrs.field()
    """
    Name of the color associated with an Amazon catalog item.
    """

    item_name: Optional[str] = attrs.field()
    """
    Name, or title, associated with an Amazon catalog item.
    """

    manufacturer: Optional[str] = attrs.field()
    """
    Name of the manufacturer associated with an Amazon catalog item.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """

    model_number: Optional[str] = attrs.field()
    """
    Model number associated with an Amazon catalog item.
    """

    size_name: Optional[str] = attrs.field()
    """
    Name of the size associated with an Amazon catalog item.
    """

    style_name: Optional[str] = attrs.field()
    """
    Name of the style associated with an Amazon catalog item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemVariationsByMarketplace:
    """
    Variation details for the Amazon catalog item for the indicated Amazon marketplace.
    """

    asins: List[str] = attrs.field()
    """
    Identifiers (ASINs) of the related items.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """

    variation_type: Union[Literal["PARENT"], Literal["CHILD"]] = attrs.field()
    """
    Type of variation relationship of the Amazon catalog item in the request to the related item(s): "PARENT" or "CHILD".

    Extra fields:
    {'example': 'PARENT'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemVendorDetailsByMarketplace:
    """
    Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace.
    """

    brand_code: Optional[str] = attrs.field()
    """
    Brand code associated with an Amazon catalog item.
    """

    category_code: Optional[str] = attrs.field()
    """
    Product category associated with an Amazon catalog item.
    """

    manufacturer_code: Optional[str] = attrs.field()
    """
    Manufacturer code associated with an Amazon catalog item.
    """

    manufacturer_code_parent: Optional[str] = attrs.field()
    """
    Parent vendor code of the manufacturer code.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """

    product_group: Optional[str] = attrs.field()
    """
    Product group associated with an Amazon catalog item.
    """

    replenishment_category: Optional[
        Union[
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
    ] = attrs.field()
    """
    Replenishment category associated with an Amazon catalog item.
    """

    subcategory_code: Optional[str] = attrs.field()
    """
    Product subcategory associated with an Amazon catalog item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:
    """
    When a request produces a response that exceeds the pageSize, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the nextToken value or the previousToken value as the pageToken parameter in the next request. When you receive the last page, there will be no nextToken key in the pagination object.
    """

    next_token: Optional[str] = attrs.field()
    """
    A token that can be used to fetch the next page.
    """

    previous_token: Optional[str] = attrs.field()
    """
    A token that can be used to fetch the previous page.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Refinements:
    """
    Search refinements.
    """

    brands: List["BrandRefinement"] = attrs.field()
    """
    Brand search refinements.
    """

    classifications: List["ClassificationRefinement"] = attrs.field()
    """
    Classification search refinements.
    """


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
    ) -> Union[ErrorList, Item]:
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
        ("asin", "path"),
        ("marketplaceIds", "query"),
        ("includedData", "query"),
        ("locale", "query"),
    )

    _get_catalog_item_responses = {
        (200, "application/json"): Item,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

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
    ) -> Union[ErrorList, ItemSearchResults]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._search_catalog_items_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

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

    _search_catalog_items_responses = {
        (200, "application/json"): ItemSearchResults,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }
