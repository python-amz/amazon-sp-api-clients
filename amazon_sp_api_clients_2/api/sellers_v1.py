"""
Selling Partner API for Sellers
=============================================================================================

The Selling Partner API for Sellers lets you retrieve information on behalf of sellers about their seller account, such as the marketplaces they participate in. Along with listing the marketplaces that a seller can sell in, the API also provides additional information about the marketplace such as the default language and the default currency. The API also provides seller-specific information such as whether the seller has suspended listings in that marketplace.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occured.
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
    A message that describes the error condition in a human-readable form.
    """

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetMarketplaceParticipationsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "MarketplaceParticipationList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Marketplace:

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The ISO 3166-1 alpha-2 format country code of the marketplace.

    Extra fields:
    {'pattern': '^([A-Z]{2})$'}
    """

    default_currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    The ISO 4217 format currency code of the marketplace.
    """

    default_language_code: str = attrs.field(
        kw_only=True,
    )
    """
    The ISO 639-1 format language code of the marketplace.
    """

    domain_name: str = attrs.field(
        kw_only=True,
    )
    """
    The domain name of the marketplace.
    """

    id: str = attrs.field(
        kw_only=True,
    )
    """
    The encrypted marketplace value.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    Marketplace name.
    """

    pass


@attrs.define
class MarketplaceParticipation:

    marketplace: "Marketplace" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    participation: "Participation" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class MarketplaceParticipationList:

    pass


@attrs.define
class Participation:

    has_suspended_listings: bool = attrs.field(
        kw_only=True,
    )
    """
    Specifies if the seller has suspended listings. True if the seller Listing Status is set to Inactive, otherwise False.
    """

    is_participating: bool = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


class SellersV1Client(BaseClient):
    def get_marketplace_participations(
        self,
    ):
        """
        Returns a list of marketplaces that the seller submitting the request can sell in and information about the seller's participation in those marketplaces.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .016 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/sellers/v1/marketplaceParticipations"
        values = ()
        response = self._parse_args_and_request(url, "GET", values, self._get_marketplace_participations_params)
        return response

    _get_marketplace_participations_params = ()  # name, param in
