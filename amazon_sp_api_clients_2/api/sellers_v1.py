"""
Selling Partner API for Sellers
=============================================================================================

The Selling Partner API for Sellers lets you retrieve information on behalf of sellers about their seller account, such as the marketplaces they participate in. Along with listing the marketplaces that a seller can sell in, the API also provides additional information about the marketplace such as the default language and the default currency. The API also provides seller-specific information such as whether the seller has suspended listings in that marketplace.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class Error:
    pass


class ErrorList:
    pass


class MarketplaceParticipation:
    pass


class MarketplaceParticipationList:
    pass


class GetMarketplaceParticipationsResponse:
    pass


class Marketplace:
    pass


class Participation:
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
