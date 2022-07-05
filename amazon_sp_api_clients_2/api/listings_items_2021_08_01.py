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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _decimal_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Decimal(**data)

    pass


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
class FulfillmentAvailability:
    """
    Fulfillment availability details for the listings item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _fulfillment_availability_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return FulfillmentAvailability(**data)

    fulfillment_channel_code: str = attrs.field(
        default=None,
    )
    """
    Designates which fulfillment network will be used.
    """

    quantity: Optional[int] = attrs.field(
        default=None,
    )
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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _issue_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Issue(**data)

    attribute_names: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    Names of the attributes associated with the issue, if applicable.
    """

    code: str = attrs.field(
        default=None,
    )
    """
    An issue code that identifies the type of issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the issue.
    """

    severity: Union[Literal["ERROR"], Literal["WARNING"], Literal["INFO"]] = attrs.field(
        default=None,
    )
    """
    The severity of the issue.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    A listings item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Item(**data)

    attributes: Optional["ItemAttributes"] = attrs.field(
        default=None,
    )
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    fulfillment_availability: Optional[List["FulfillmentAvailability"]] = attrs.field(
        default=None,
    )
    """
    Fulfillment availability for the listings item.
    """

    issues: Optional[List["Issue"]] = attrs.field(
        default=None,
    )
    """
    Issues associated with the listings item.
    """

    offers: Optional[List["ItemOfferByMarketplace"]] = attrs.field(
        default=None,
    )
    """
    Offer details for the listings item.
    """

    procurement: Optional["ItemProcurement"] = attrs.field(
        default=None,
    )
    """
    Vendor procurement information for the listings item.
    """

    sku: str = attrs.field(
        default=None,
    )
    """
    A selling partner provided identifier for an Amazon listing.
    """

    summaries: Optional[List["ItemSummaryByMarketplace"]] = attrs.field(
        default=None,
    )
    """
    Summary details of a listings item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemAttributes:
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_attributes_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemAttributes(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemImage:
    """
    Image for the listings item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_image_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemImage(**data)

    height: int = attrs.field(
        default=None,
    )
    """
    Height of the image in pixels.
    """

    link: str = attrs.field(
        default=None,
    )
    """
    Link, or URL, for the image.
    """

    width: int = attrs.field(
        default=None,
    )
    """
    Width of the image in pixels.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemOfferByMarketplace:
    """
    Offer details of a listings item for an Amazon marketplace.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_offer_by_marketplace_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemOfferByMarketplace(**data)

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    Amazon marketplace identifier.
    """

    offer_type: Union[Literal["B2C"], Literal["B2B"]] = attrs.field(
        default=None,
    )
    """
    Type of offer for the listings item.
    """

    points: Optional["Points"] = attrs.field(
        default=None,
    )
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points element is only returned in Japan (JP).
    """

    price: "Money" = attrs.field(
        default=None,
    )
    """
    The currency type and the amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemProcurement:
    """
    Vendor procurement information for the listings item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_procurement_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemProcurement(**data)

    cost_price: "Money" = attrs.field(
        default=None,
    )
    """
    The currency type and the amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemSummaryByMarketplace:
    """
    Summary details of a listings item for an Amazon marketplace.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_summary_by_marketplace_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemSummaryByMarketplace(**data)

    asin: str = attrs.field(
        default=None,
    )
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
    ] = attrs.field(
        default=None,
    )
    """
    Identifies the condition of the listings item.
    """

    created_date: datetime = attrs.field(
        default=None,
    )
    """
    Date the listings item was created, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    fn_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    Fulfillment network stock keeping unit is an identifier used by Amazon fulfillment centers to identify each unique item.
    """

    item_name: str = attrs.field(
        default=None,
    )
    """
    Name, or title, associated with an Amazon catalog item.
    """

    last_updated_date: datetime = attrs.field(
        default=None,
    )
    """
    Date the listings item was last updated, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    main_image: Optional["ItemImage"] = attrs.field(
        default=None,
    )
    """
    Image for the listings item.
    """

    marketplace_id: str = attrs.field(
        default=None,
    )
    """
    A marketplace identifier. Identifies the Amazon marketplace for the listings item.
    """

    product_type: str = attrs.field(
        default=None,
    )
    """
    The Amazon product type of the listings item.
    """

    status: List[Union[Literal["BUYABLE"], Literal["DISCOVERABLE"]]] = attrs.field(
        default=None,
    )
    """
    Statuses that apply to the listings item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemPatchRequest:
    """
    The request body schema for the patchListingsItem operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _listings_item_patch_request_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListingsItemPatchRequest(**data)

    patches: List["PatchOperation"] = attrs.field(
        default=None,
    )
    """
    One or more JSON Patch operations to perform on the listings item.

    Extra fields:
    {'minItems': 1}
    """

    product_type: str = attrs.field(
        default=None,
    )
    """
    The Amazon product type of the listings item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemPutRequest:
    """
    The request body schema for the putListingsItem operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _listings_item_put_request_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListingsItemPutRequest(**data)

    attributes: "ListingsItemPutRequestAttributes" = attrs.field(
        default=None,
    )
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    product_type: str = attrs.field(
        default=None,
    )
    """
    The Amazon product type of the listings item.
    """

    requirements: Optional[
        Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]]
    ] = attrs.field(
        default=None,
    )
    """
    The name of the requirements set for the provided data.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemPutRequestAttributes:
    """
    JSON object containing structured listings item attribute data keyed by attribute name.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _listings_item_put_request_attributes_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListingsItemPutRequestAttributes(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListingsItemSubmissionResponse:
    """
    Response containing the results of a submission to the Selling Partner API for Listings Items.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _listings_item_submission_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ListingsItemSubmissionResponse(**data)

    issues: Optional[List["Issue"]] = attrs.field(
        default=None,
    )
    """
    Listings item issues related to the listings item submission.
    """

    sku: str = attrs.field(
        default=None,
    )
    """
    A selling partner provided identifier for an Amazon listing.
    """

    status: Union[Literal["ACCEPTED"], Literal["INVALID"]] = attrs.field(
        default=None,
    )
    """
    The status of the listings item submission.
    """

    submission_id: str = attrs.field(
        default=None,
    )
    """
    The unique identifier of the listings item submission.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    The currency type and the amount.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Money(**data)

    amount: "Decimal" = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """

    currency_code: str = attrs.field(
        default=None,
    )
    """
    Three-digit currency code. In ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PatchOperation:
    """
    Individual JSON Patch operation for an HTTP PATCH request.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _patch_operation_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PatchOperation(**data)

    op: Union[Literal["add"], Literal["replace"], Literal["delete"]] = attrs.field(
        default=None,
    )
    """
    Type of JSON Patch operation. Supported JSON Patch operations include add, replace, and delete. See <https://tools.ietf.org/html/rfc6902>.
    """

    path: str = attrs.field(
        default=None,
    )
    """
    JSON Pointer path of the element to patch. See <https://tools.ietf.org/html/rfc6902>.
    """

    value: Optional[List["PatchOperationValueItem"]] = attrs.field(
        default=None,
    )
    """
    JSON value to add, replace, or delete.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PatchOperationValueItem:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _patch_operation_value_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PatchOperationValueItem(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Points:
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the Points element is only returned in Japan (JP).
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _points_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Points(**data)

    points_number: int = attrs.field(
        default=None,
    )


_decimal_name_convert = {}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_fulfillment_availability_name_convert = {
    "fulfillmentChannelCode": "fulfillment_channel_code",
    "quantity": "quantity",
}

_issue_name_convert = {
    "attributeNames": "attribute_names",
    "code": "code",
    "message": "message",
    "severity": "severity",
}

_item_name_convert = {
    "attributes": "attributes",
    "fulfillmentAvailability": "fulfillment_availability",
    "issues": "issues",
    "offers": "offers",
    "procurement": "procurement",
    "sku": "sku",
    "summaries": "summaries",
}

_item_attributes_name_convert = {}

_item_image_name_convert = {
    "height": "height",
    "link": "link",
    "width": "width",
}

_item_offer_by_marketplace_name_convert = {
    "marketplaceId": "marketplace_id",
    "offerType": "offer_type",
    "points": "points",
    "price": "price",
}

_item_procurement_name_convert = {
    "costPrice": "cost_price",
}

_item_summary_by_marketplace_name_convert = {
    "asin": "asin",
    "conditionType": "condition_type",
    "createdDate": "created_date",
    "fnSku": "fn_sku",
    "itemName": "item_name",
    "lastUpdatedDate": "last_updated_date",
    "mainImage": "main_image",
    "marketplaceId": "marketplace_id",
    "productType": "product_type",
    "status": "status",
}

_listings_item_patch_request_name_convert = {
    "patches": "patches",
    "productType": "product_type",
}

_listings_item_put_request_name_convert = {
    "attributes": "attributes",
    "productType": "product_type",
    "requirements": "requirements",
}

_listings_item_put_request_attributes_name_convert = {}

_listings_item_submission_response_name_convert = {
    "issues": "issues",
    "sku": "sku",
    "status": "status",
    "submissionId": "submission_id",
}

_money_name_convert = {
    "amount": "amount",
    "currencyCode": "currency_code",
}

_patch_operation_name_convert = {
    "op": "op",
    "path": "path",
    "value": "value",
}

_patch_operation_value_item_name_convert = {}

_points_name_convert = {
    "pointsNumber": "points_number",
}


class ListingsItems20210801Client(BaseClient):
    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: List[str],
        issue_locale: str = None,
    ) -> Union[ErrorList, ListingsItemSubmissionResponse]:
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
            self._delete_listings_item_responses,
        )
        return response

    _delete_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
    )

    _delete_listings_item_responses = {
        200: ListingsItemSubmissionResponse,
        400: ErrorList,
        403: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
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
    ) -> Union[ErrorList, Item]:
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
            self._get_listings_item_responses,
        )
        return response

    _get_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("includedData", "query"),
    )

    _get_listings_item_responses = {
        200: Item,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: List[str],
        patches: List["PatchOperation"],
        product_type: str,
        issue_locale: str = None,
    ) -> Union[ErrorList, ListingsItemSubmissionResponse]:
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
            self._patch_listings_item_responses,
        )
        return response

    _patch_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("patches", "body"),
        ("productType", "body"),
    )

    _patch_listings_item_responses = {
        200: ListingsItemSubmissionResponse,
        400: ErrorList,
        403: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
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
    ) -> Union[ErrorList, ListingsItemSubmissionResponse]:
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
            self._put_listings_item_responses,
        )
        return response

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
        200: ListingsItemSubmissionResponse,
        400: ErrorList,
        403: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
