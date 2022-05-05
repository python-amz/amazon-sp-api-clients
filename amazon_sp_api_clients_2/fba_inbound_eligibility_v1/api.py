"""
Selling Partner API for FBA Inbound Eligibilty
=============================================================================================
With the FBA Inbound Eligibility API, you can build applications that let sellers get eligibility previews for items before shipping them to Amazon's fulfillment centers. With this API you can find out if an item is eligible for inbound shipment to Amazon's fulfillment centers in a specific marketplace. You can also find out if an item is eligible for using the manufacturer barcode for FBA inventory tracking. Sellers can use this information to inform their decisions about which items to ship Amazon's fulfillment centers.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class FbaInboundEligibilityV1Client(BaseClient):
    def get_item_eligibility_preview(
        self,
        marketplace_ids: list[str] = None,
        asin: str,
        program: str,
    ):
        """
        This operation gets an eligibility preview for an item that you specify. You can specify the type of eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify the marketplace in which you want to determine the item's eligibility.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_ids: The identifier for the marketplace in which you want to determine eligibility. Required only when program=INBOUND.
            asin: The ASIN of the item for which you want an eligibility preview.
            program: The program that you want to check eligibility against.
        """
        path_parameters = {}

        url = "/fba/inbound/v1/eligibility/itemPreview".format(**path_parameters)

        query_parameters = {}

        if marketplace_ids is not None:
            query_parameters["marketplaceIds"] = marketplace_ids

        query_parameters["asin"] = asin

        query_parameters["program"] = program
