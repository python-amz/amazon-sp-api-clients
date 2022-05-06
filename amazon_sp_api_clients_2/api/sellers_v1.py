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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMarketplaceParticipationsResponse:
    """
    The response schema for the getMarketplaceParticipations operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["MarketplaceParticipationList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Marketplace:
    """
    Detailed information about an Amazon market where a seller can list items for sale and customers can view and purchase items.
    """

    country_code: Optional[str] = attrs.field()
    """
    The ISO 3166-1 alpha-2 format country code of the marketplace.

    Extra fields:
    {'pattern': '^([A-Z]{2})$'}
    """

    default_currency_code: Optional[str] = attrs.field()
    """
    The ISO 4217 format currency code of the marketplace.
    """

    default_language_code: Optional[str] = attrs.field()
    """
    The ISO 639-1 format language code of the marketplace.
    """

    domain_name: Optional[str] = attrs.field()
    """
    The domain name of the marketplace.
    """

    id: Optional[str] = attrs.field()
    """
    The encrypted marketplace value.
    """

    name: Optional[str] = attrs.field()
    """
    Marketplace name.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceParticipation:

    marketplace: Optional["Marketplace"] = attrs.field()

    participation: Optional["Participation"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceParticipationList:
    """
    List of marketplace participations.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Participation:
    """
    Detailed information that is specific to a seller in a Marketplace.
    """

    has_suspended_listings: Optional[bool] = attrs.field()
    """
    Specifies if the seller has suspended listings. True if the seller Listing Status is set to Inactive, otherwise False.
    """

    is_participating: Optional[bool] = attrs.field()


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
