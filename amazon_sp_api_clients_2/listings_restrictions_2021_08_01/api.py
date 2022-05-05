"""
Selling Partner API for Listings Restrictions
=============================================================================================
The Selling Partner API for Listings Restrictions provides programmatic access to restrictions on Amazon catalog listings.

For more information, see the [Listings Restrictions API Use Case Guide](doc:listings-restrictions-api-v2021-08-01-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-08-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ListingsRestrictions20210801Client(BaseClient):
    def get_listings_restrictions(
        self,
        asin: str,
        condition_type: str = None,
        seller_id: str,
        marketplace_ids: list[str],
        reason_locale: str = None,
    ):
        """
        Returns listing restrictions for an item in the Amazon Catalog.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            condition_type: The condition used to filter restrictions.
            seller_id: A selling partner identifier, such as a merchant account.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            reason_locale: A locale for reason text localization. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        """
        path_parameters = {}

        url = "/listings/2021-08-01/restrictions".format(**path_parameters)

        query_parameters = {}

        query_parameters["asin"] = asin

        if condition_type is not None:
            query_parameters["conditionType"] = condition_type

        query_parameters["sellerId"] = seller_id

        query_parameters["marketplaceIds"] = marketplace_ids

        if reason_locale is not None:
            query_parameters["reasonLocale"] = reason_locale
