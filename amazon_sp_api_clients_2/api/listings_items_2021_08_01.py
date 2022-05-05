"""
Selling Partner API for Listings Items
=============================================================================================

The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

For more information, see the [Listings Items API Use Case Guide](doc:listings-items-api-v2021-08-01-use-case-guide).
API Version: 2021-08-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Any, Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class Decimal:
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
class FulfillmentAvailability:
    fulfillment_channel_code: str = attrs.field()
    quantity: int = attrs.field()
    # {'minimum': 0.0}

    pass


@attrs.define
class Issue:
    attribute_names: list[str] = attrs.field()
    code: str = attrs.field()
    message: str = attrs.field()
    severity: Union[Literal["ERROR"], Literal["WARNING"], Literal["INFO"]] = attrs.field()

    pass


@attrs.define
class Item:
    fulfillment_availability: list["FulfillmentAvailability"] = attrs.field()
    sku: str = attrs.field()

    attributes: "ItemAttributes" = attrs.field()
    issues: "ItemIssues" = attrs.field()
    offers: "ItemOffers" = attrs.field()
    procurement: "ItemProcurement" = attrs.field()
    summaries: "ItemSummaries" = attrs.field()
    pass


@attrs.define
class ItemAttributes:
    pass


@attrs.define
class ItemImage:
    height: int = attrs.field()
    link: str = attrs.field()
    width: int = attrs.field()

    pass


@attrs.define
class ItemIssues:
    pass


@attrs.define
class ItemOfferByMarketplace:
    marketplace_id: str = attrs.field()
    offer_type: Union[Literal["B2C"], Literal["B2B"]] = attrs.field()

    points: "Points" = attrs.field()
    price: "Money" = attrs.field()
    pass


@attrs.define
class ItemOffers:
    pass


@attrs.define
class ItemProcurement:
    cost_price: "Money" = attrs.field()
    pass


@attrs.define
class ItemSummaries:
    pass


@attrs.define
class ItemSummaryByMarketplace:
    asin: str = attrs.field()
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
    ] = attrs.field()
    created_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    fn_sku: str = attrs.field()
    item_name: str = attrs.field()
    last_updated_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    marketplace_id: str = attrs.field()
    product_type: str = attrs.field()
    status: list[Union[Literal["BUYABLE"], Literal["DISCOVERABLE"]]] = attrs.field()

    main_image: "ItemImage" = attrs.field()
    pass


@attrs.define
class ListingsItemPatchRequest:
    patches: list["PatchOperation"] = attrs.field()
    # {'minItems': 1}
    product_type: str = attrs.field()

    pass


@attrs.define
class ListingsItemPutRequest:
    attributes: dict[str, Any] = attrs.field()
    # {'properties': {}}
    product_type: str = attrs.field()
    requirements: Union[
        Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]
    ] = attrs.field()

    pass


@attrs.define
class ListingsItemSubmissionResponse:
    issues: list["Issue"] = attrs.field()
    sku: str = attrs.field()
    status: Union[Literal["ACCEPTED"], Literal["INVALID"]] = attrs.field()
    submission_id: str = attrs.field()

    pass


@attrs.define
class Money:
    currency_code: str = attrs.field()

    amount: "Decimal" = attrs.field()
    pass


@attrs.define
class PatchOperation:
    op: Union[Literal["add"], Literal["replace"], Literal["delete"]] = attrs.field()
    path: str = attrs.field()
    value: list[dict[str, Any]] = attrs.field()

    pass


@attrs.define
class Points:
    points_number: int = attrs.field()

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
            requirements: Union[
                Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]] = None,
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
