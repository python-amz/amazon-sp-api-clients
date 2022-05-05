"""
Selling Partner API for Listings Items
=============================================================================================
The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

For more information, see the [Listing Items API Use Case Guide](doc:listings-items-api-v2020-09-01-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-09-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ListingsItems20200901Client(BaseClient):
    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
    ):
        """
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        """
        path_parameters = {}

        path_parameters["sellerId"] = seller_id

        path_parameters["sku"] = sku

        url = "/listings/2020-09-01/items/{sellerId}/{sku}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

        if issue_locale is not None:
            query_parameters["issueLocale"] = issue_locale

    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
    ):
        """
        Delete a listings item for a selling partner.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        """
        path_parameters = {}

        path_parameters["sellerId"] = seller_id

        path_parameters["sku"] = sku

        url = "/listings/2020-09-01/items/{sellerId}/{sku}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

        if issue_locale is not None:
            query_parameters["issueLocale"] = issue_locale

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
    ):
        """
        Creates a new or fully-updates an existing listings item for a selling partner.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        """
        path_parameters = {}

        path_parameters["sellerId"] = seller_id

        path_parameters["sku"] = sku

        url = "/listings/2020-09-01/items/{sellerId}/{sku}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

        if issue_locale is not None:
            query_parameters["issueLocale"] = issue_locale
