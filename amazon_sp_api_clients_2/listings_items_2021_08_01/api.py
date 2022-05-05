"""
Selling Partner API for Listings Items
=============================================================================================
The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

For more information, see the [Listings Items API Use Case Guide](doc:listings-items-api-v2021-08-01-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-08-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


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

    _delete_listings_item_params = (  # name, param in, required
        ("sellerId", "path", True),
        ("sku", "path", True),
        ("marketplaceIds", "query", True),
        ("issueLocale", "query", False),
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

    _get_listings_item_params = (  # name, param in, required
        ("sellerId", "path", True),
        ("sku", "path", True),
        ("marketplaceIds", "query", True),
        ("issueLocale", "query", False),
        ("includedData", "query", False),
    )

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
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
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
        )

    _patch_listings_item_params = (  # name, param in, required
        ("sellerId", "path", True),
        ("sku", "path", True),
        ("marketplaceIds", "query", True),
        ("issueLocale", "query", False),
    )

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
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
        """
        url = "/listings/2021-08-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
        )

    _put_listings_item_params = (  # name, param in, required
        ("sellerId", "path", True),
        ("sku", "path", True),
        ("marketplaceIds", "query", True),
        ("issueLocale", "query", False),
    )
