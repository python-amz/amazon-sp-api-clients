"""
Selling Partner API for Sellers
=============================================================================================
The Selling Partner API for Sellers lets you retrieve information on behalf of sellers about their seller account, such as the marketplaces they participate in. Along with listing the marketplaces that a seller can sell in, the API also provides additional information about the marketplace such as the default language and the default currency. The API also provides seller-specific information such as whether the seller has suspended listings in that marketplace.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


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
        path_parameters = {}

        url = "/sellers/v1/marketplaceParticipations".format(**path_parameters)

        query_parameters = {}
