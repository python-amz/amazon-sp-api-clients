"""
Selling Partner API for Listings Restrictions
=============================================================================================

The Selling Partner API for Listings Restrictions provides programmatic access to restrictions on Amazon catalog listings.

For more information, see the [Listings Restrictions API Use Case Guide](doc:listings-restrictions-api-v2021-08-01-use-case-guide).
API Version: 2021-08-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class Link:

    resource: str = attrs.field()
    # {'schema_format': 'uri'}
    title: str = attrs.field()
    type: str = attrs.field()
    verb: Union[Literal["GET"]] = attrs.field()

    pass


@attrs.define
class Reason:

    links: list["Link"] = attrs.field()
    message: str = attrs.field()
    reason_code: Union[Literal["APPROVAL_REQUIRED"], Literal["ASIN_NOT_FOUND"], Literal["NOT_ELIGIBLE"]] = attrs.field()

    pass


@attrs.define
class Restriction:

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
    marketplace_id: str = attrs.field()
    reasons: list["Reason"] = attrs.field()

    pass


@attrs.define
class RestrictionList:

    restrictions: list["Restriction"] = attrs.field()

    pass


class ListingsRestrictions20210801Client(BaseClient):
    def get_listings_restrictions(
        self,
        asin: str,
        seller_id: str,
        marketplace_ids: list[str],
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
        ] = None,
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
        url = "/listings/2021-08-01/restrictions"
        values = (
            asin,
            condition_type,
            seller_id,
            marketplace_ids,
            reason_locale,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_listings_restrictions_params)
        return response

    _get_listings_restrictions_params = (  # name, param in
        ("asin", "query"),
        ("conditionType", "query"),
        ("sellerId", "query"),
        ("marketplaceIds", "query"),
        ("reasonLocale", "query"),
    )
