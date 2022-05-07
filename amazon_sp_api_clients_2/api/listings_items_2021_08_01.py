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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """

    pass


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
class FulfillmentAvailability:
    """
    Fulfillment availability details for the listings item.
    """

    fulfillment_channel_code: str = attrs.field()
    """
    Designates which fulfillment network will be used.
    """

    quantity: Optional[int] = attrs.field()
    """
    The quantity of the item you are making available for sale.

    Extra fields:
    {'minimum': 0.0}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Issue:
    """
    An issue with a listings item.
    """

    attribute_names: Optional[List[str]] = attrs.field()
    """
    Names of the attributes associated with the issue, if applicable.
    """

    code: str = attrs.field()
    """
    An issue code that identifies the type of issue.
    """

    message: str = attrs.field()
    """
    A message that describes the issue.
    """

    severity: Union[Literal["ERROR"], Literal["WARNING"], Literal["INFO"]] = attrs.field()
    """
    The severity of the issue.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    A listings item.
    """

    attributes: Optional["ItemAttributes"] = attrs.field()
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    fulfillment_availability: Optional[List["FulfillmentAvailability"]] = attrs.field()
    """
    Fulfillment availability for the listings item.
    """

    issues: Optional[List["Issue"]] = attrs.field()
    """
    Issues associated with the listings item.
    """

    offers: Optional[List["ItemOfferByMarketplace"]] = attrs.field()
    """
    Offer details for the listings item.
    """

    procurement: Optional["ItemProcurement"] = attrs.field()
    """
    Vendor procurement information for the listings item.
    """

    sku: str = attrs.field()
    """
    A selling partner provided identifier for an Amazon listing.
    """

    summaries: Optional[List["ItemSummaryByMarketplace"]] = attrs.field()
    """
    Summary details of a listings item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemAttributes:
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemImage:
    """
    Image for the listings item.
    """

    height: int = attrs.field()
    """
    Height of the image in pixels.
    """

    link: str = attrs.field()
    """
    Link, or URL, for the image.
    """

    width: int = attrs.field()
    """
    Width of the image in pixels.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemOfferByMarketplace:
    """
    Offer details of a listings item for an Amazon marketplace.
    """

    marketplace_id: str = attrs.field()
    """
    Amazon marketplace identifier.
    """

    offer_type: Union[Literal["B2C"], Literal["B2B"]] = attrs.field()
    """
    Type of offer for the listings item.
    """

    points: Optional["Points"] = attrs.field()
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points element is only returned in Japan (JP).
    """

    price: "Money" = attrs.field()
    """
    The currency type and the amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemProcurement:
    """
    Vendor procurement information for the listings item.
    """

    cost_price: "Money" = attrs.field()
    """
    The currency type and the amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemSummaryByMarketplace:
    """
    Summary details of a listings item for an Amazon marketplace.
    """

    asin: str = attrs.field()
    """
    Amazon Standard Identification Number (ASIN) of the listings item.
    """

    condition_type: Optional[
        Union[
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
        ]
    ] = attrs.field()
    """
    Identifies the condition of the listings item.
    """

    created_date: datetime = attrs.field()
    """
    Date the listings item was created, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    fn_sku: Optional[str] = attrs.field()
    """
    Fulfillment network stock keeping unit is an identifier used by Amazon fulfillment centers to identify each unique item.
    """

    item_name: str = attrs.field()
    """
    Name, or title, associated with an Amazon catalog item.
    """

    last_updated_date: datetime = attrs.field()
    """
    Date the listings item was last updated, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    main_image: Optional["ItemImage"] = attrs.field()
    """
    Image for the listings item.
    """

    marketplace_id: str = attrs.field()
    """
    A marketplace identifier. Identifies the Amazon marketplace for the listings item.
    """

    product_type: str = attrs.field()
    """
    The Amazon product type of the listings item.
    """

    status: List[Union[Literal["BUYABLE"], Literal["DISCOVERABLE"]]] = attrs.field()
    """
    Statuses that apply to the listings item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemPatchRequest:
    """
    The request body schema for the patchListingsItem operation.
    """

    patches: List["PatchOperation"] = attrs.field()
    """
    One or more JSON Patch operations to perform on the listings item.

    Extra fields:
    {'minItems': 1}
    """

    product_type: str = attrs.field()
    """
    The Amazon product type of the listings item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemPutRequest:
    """
    The request body schema for the putListingsItem operation.
    """

    attributes: "ListingsItemPutRequestAttributes" = attrs.field()
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    product_type: str = attrs.field()
    """
    The Amazon product type of the listings item.
    """

    requirements: Optional[
        Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]]
    ] = attrs.field()
    """
    The name of the requirements set for the provided data.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemPutRequestAttributes:
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemSubmissionResponse:
    """
    Response containing the results of a submission to the Selling Partner API for Listings Items.
    """

    issues: Optional[List["Issue"]] = attrs.field()
    """
    Listings item issues related to the listings item submission.
    """

    sku: str = attrs.field()
    """
    A selling partner provided identifier for an Amazon listing.
    """

    status: Union[Literal["ACCEPTED"], Literal["INVALID"]] = attrs.field()
    """
    The status of the listings item submission.
    """

    submission_id: str = attrs.field()
    """
    The unique identifier of the listings item submission.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    The currency type and the amount.
    """

    amount: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """

    currency_code: str = attrs.field()
    """
    Three-digit currency code. In ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PatchOperation:
    """
    Individual JSON Patch operation for an HTTP PATCH request.
    """

    op: Union[Literal["add"], Literal["replace"], Literal["delete"]] = attrs.field()
    """
    Type of JSON Patch operation. Supported JSON Patch operations include add, replace, and delete. See <https://tools.ietf.org/html/rfc6902>.
    """

    path: str = attrs.field()
    """
    JSON Pointer path of the element to patch. See <https://tools.ietf.org/html/rfc6902>.
    """

    value: Optional[List["PatchOperationValueItem"]] = attrs.field()
    """
    JSON value to add, replace, or delete.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PatchOperationValueItem:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Points:
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points element is only returned in Japan (JP).
    """

    points_number: int = attrs.field()


class ListingsItems20210801Client(BaseClient):
    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._delete_listings_item_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _delete_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
    )

    _delete_listings_item_responses = {
        (200, "application/json"): ListingsItemSubmissionResponse,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

    def get_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: List[str],
        issue_locale: str = None,
        included_data: List[
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_listings_item_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("includedData", "query"),
    )

    _get_listings_item_responses = {
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

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: List[str],
        patches: List["PatchOperation"],
        product_type: str,
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
            patches: One or more JSON Patch operations to perform on the listings item.
            product_type: The Amazon product type of the listings item.
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            patches,
            product_type,
        )
        response = self._parse_args_and_request(
            url,
            "PATCH",
            values,
            self._patch_listings_item_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _patch_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("patches", "body"),
        ("productType", "body"),
    )

    _patch_listings_item_responses = {
        (200, "application/json"): ListingsItemSubmissionResponse,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: List[str],
        attributes: Dict[str, Any],
        product_type: str,
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
            attributes: JSON object containing structured listings item attribute data keyed by attribute name.
            product_type: The Amazon product type of the listings item.
            requirements: The name of the requirements set for the provided data.
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            attributes,
            product_type,
            requirements,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._put_listings_item_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _put_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("attributes", "body"),
        ("productType", "body"),
        ("requirements", "body"),
    )

    _put_listings_item_responses = {
        (200, "application/json"): ListingsItemSubmissionResponse,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }
