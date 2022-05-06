"""
Selling Partner API for Listings Items
=============================================================================================

The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

For more information, see the [Listings Items API Use Case Guide](doc:listings-items-api-v2021-08-01-use-case-guide).
API Version: 2021-08-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Decimal:

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

    errors: list["Error"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentAvailability:

    fulfillment_channel_code: str = attrs.field(
        kw_only=True,
    )
    """
    Designates which fulfillment network will be used.
    """

    quantity: int = attrs.field(
        kw_only=True,
    )
    """
    The quantity of the item you are making available for sale.

    Extra fields:
    {'minimum': 0.0}
    """

    pass


@attrs.define
class Issue:

    attribute_names: list[str] = attrs.field(
        kw_only=True,
    )
    """
    Names of the attributes associated with the issue, if applicable.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An issue code that identifies the type of issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the issue.
    """

    severity: Union[Literal["ERROR"], Literal["WARNING"], Literal["INFO"]] = attrs.field(
        kw_only=True,
    )
    """
    The severity of the issue.
    """

    pass


@attrs.define
class Item:

    fulfillment_availability: list["FulfillmentAvailability"] = attrs.field(
        kw_only=True,
    )
    """
    Fulfillment availability for the listings item.
    """

    sku: str = attrs.field(
        kw_only=True,
    )
    """
    A selling partner provided identifier for an Amazon listing.
    """

    attributes: "ItemAttributes" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    issues: "ItemIssues" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    offers: "ItemOffers" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    procurement: "ItemProcurement" = attrs.field(
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

    pass


@attrs.define
class ItemAttributes:

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

    width: int = attrs.field(
        kw_only=True,
    )
    """
    Width of the image in pixels.
    """

    pass


@attrs.define
class ItemIssues:

    pass


@attrs.define
class ItemOfferByMarketplace:

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon marketplace identifier.
    """

    offer_type: Union[Literal["B2C"], Literal["B2B"]] = attrs.field(
        kw_only=True,
    )
    """
    Type of offer for the listings item.
    """

    points: "Points" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ItemOffers:

    pass


@attrs.define
class ItemProcurement:

    cost_price: "Money" = attrs.field(
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

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon Standard Identification Number (ASIN) of the listings item.
    """

    condition_type: Union[
        Literal["new_new"],
        Literal["new_open_box"],
        Literal["new_oem"],
        Literal["refurbished_refurbished"],
        Literal["used_like_new"],
        Literal["used_very_good"],
        Literal["used_good"],
        Literal["used_acceptable"],
        Literal["collectible_like_new"],
        Literal["collectible_very_good"],
        Literal["collectible_good"],
        Literal["collectible_acceptable"],
        Literal["club_club"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    Identifies the condition of the listings item.
    """

    created_date: str = attrs.field(
        kw_only=True,
    )
    """
    Date the listings item was created, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    fn_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Fulfillment network stock keeping unit is an identifier used by Amazon fulfillment centers to identify each unique item.
    """

    item_name: str = attrs.field(
        kw_only=True,
    )
    """
    Name, or title, associated with an Amazon catalog item.
    """

    last_updated_date: str = attrs.field(
        kw_only=True,
    )
    """
    Date the listings item was last updated, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier. Identifies the Amazon marketplace for the listings item.
    """

    product_type: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon product type of the listings item.
    """

    status: list[Union[Literal["BUYABLE"], Literal["DISCOVERABLE"]]] = attrs.field(
        kw_only=True,
    )
    """
    Statuses that apply to the listings item.
    """

    main_image: "ItemImage" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ListingsItemPatchRequest:

    patches: list["PatchOperation"] = attrs.field(
        kw_only=True,
    )
    """
    One or more JSON Patch operations to perform on the listings item.

    Extra fields:
    {'minItems': 1}
    """

    product_type: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon product type of the listings item.
    """

    pass


@attrs.define
class ListingsItemPutRequest:

    attributes: dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    JSON object containing structured listings item attribute data keyed by attribute name.

    Extra fields:
    {'properties': {}}
    """

    product_type: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon product type of the listings item.
    """

    requirements: Union[
        Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]
    ] = attrs.field(
        kw_only=True,
    )
    """
    The name of the requirements set for the provided data.
    """

    pass


@attrs.define
class ListingsItemSubmissionResponse:

    issues: list["Issue"] = attrs.field(
        kw_only=True,
    )
    """
    Listings item issues related to the listings item submission.
    """

    sku: str = attrs.field(
        kw_only=True,
    )
    """
    A selling partner provided identifier for an Amazon listing.
    """

    status: Union[Literal["ACCEPTED"], Literal["INVALID"]] = attrs.field(
        kw_only=True,
    )
    """
    The status of the listings item submission.
    """

    submission_id: str = attrs.field(
        kw_only=True,
    )
    """
    The unique identifier of the listings item submission.
    """

    pass


@attrs.define
class Money:

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three-digit currency code. In ISO 4217 format.
    """

    amount: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PatchOperation:

    op: Union[Literal["add"], Literal["replace"], Literal["delete"]] = attrs.field(
        kw_only=True,
    )
    """
    Type of JSON Patch operation. Supported JSON Patch operations include add, replace, and delete. See <https://tools.ietf.org/html/rfc6902>.
    """

    path: str = attrs.field(
        kw_only=True,
    )
    """
    JSON Pointer path of the element to patch. See <https://tools.ietf.org/html/rfc6902>.
    """

    value: list[dict[str, Any]] = attrs.field(
        kw_only=True,
    )
    """
    JSON value to add, replace, or delete.
    """

    pass


@attrs.define
class Points:

    points_number: int = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


class ListingsItems20210801Client(BaseClient):
    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
    ):
        """
        Delete a listings item for a selling partner.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
        )
        response = self._parse_args_and_request(url, "DELETE", values, self._delete_listings_item_params)
        return response

    _delete_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
    )

    def get_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
        included_data: list[
            Union[
                Literal["summaries"],
                Literal["attributes"],
                Literal["issues"],
                Literal["offers"],
                Literal["fulfillmentAvailability"],
                Literal["procurement"],
            ]
        ] = None,
    ):
        """
        Returns details about a listings item for a selling partner.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            included_data: A comma-delimited list of data sets to include in the response. Default: summaries.
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            included_data,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_listings_item_params)
        return response

    _get_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("includedData", "query"),
    )

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        product_type: str,
        patches: list["PatchOperation"],
        issue_locale: str = None,
    ):
        """
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            product_type: The Amazon product type of the listings item.
            patches: One or more JSON Patch operations to perform on the listings item.
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            product_type,
            patches,
        )
        response = self._parse_args_and_request(url, "PATCH", values, self._patch_listings_item_params)
        return response

    _patch_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("productType", "body"),
        ("patches", "body"),
    )

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        product_type: str,
        attributes: dict[str, Any],
        issue_locale: str = None,
        requirements: Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]] = None,
    ):
        """
        Creates a new or fully-updates an existing listings item for a selling partner.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            product_type: The Amazon product type of the listings item.
            requirements: The name of the requirements set for the provided data.
            attributes: JSON object containing structured listings item attribute data keyed by attribute name.
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            product_type,
            requirements,
            attributes,
        )
        response = self._parse_args_and_request(url, "PUT", values, self._put_listings_item_params)
        return response

    _put_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("productType", "body"),
        ("requirements", "body"),
        ("attributes", "body"),
    )
