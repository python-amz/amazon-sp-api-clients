"""
Selling Partner API for FBA Inbound Eligibilty
=============================================================================================

With the FBA Inbound Eligibility API, you can build applications that let sellers get eligibility previews for items before shipping them to Amazon's fulfillment centers. With this API you can find out if an item is eligible for inbound shipment to Amazon's fulfillment centers in a specific marketplace. You can also find out if an item is eligible for using the manufacturer barcode for FBA inventory tracking. Sellers can use this information to inform their decisions about which items to ship Amazon's fulfillment centers.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime
import cattrs


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetItemEligibilityPreviewResponse:
    """
    The response schema for the getItemEligibilityPreview operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ItemEligibilityPreview"] = attrs.field()
    """
    The response object which contains the ASIN, marketplaceId if required, eligibility program, the eligibility status (boolean), and a list of ineligibility reason codes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemEligibilityPreview:
    """
    The response object which contains the ASIN, marketplaceId if required, eligibility program, the eligibility status (boolean), and a list of ineligibility reason codes.
    """

    asin: str = attrs.field()
    """
    The ASIN for which eligibility was determined.
    """

    ineligibility_reason_list: Optional[
        List[
            Union[
                Literal["FBA_INB_0004"],
                Literal["FBA_INB_0006"],
                Literal["FBA_INB_0007"],
                Literal["FBA_INB_0008"],
                Literal["FBA_INB_0009"],
                Literal["FBA_INB_0010"],
                Literal["FBA_INB_0011"],
                Literal["FBA_INB_0012"],
                Literal["FBA_INB_0013"],
                Literal["FBA_INB_0014"],
                Literal["FBA_INB_0015"],
                Literal["FBA_INB_0016"],
                Literal["FBA_INB_0017"],
                Literal["FBA_INB_0018"],
                Literal["FBA_INB_0019"],
                Literal["FBA_INB_0034"],
                Literal["FBA_INB_0035"],
                Literal["FBA_INB_0036"],
                Literal["FBA_INB_0037"],
                Literal["FBA_INB_0038"],
                Literal["FBA_INB_0050"],
                Literal["FBA_INB_0051"],
                Literal["FBA_INB_0053"],
                Literal["FBA_INB_0055"],
                Literal["FBA_INB_0056"],
                Literal["FBA_INB_0059"],
                Literal["FBA_INB_0065"],
                Literal["FBA_INB_0066"],
                Literal["FBA_INB_0067"],
                Literal["FBA_INB_0068"],
                Literal["FBA_INB_0095"],
                Literal["FBA_INB_0097"],
                Literal["FBA_INB_0098"],
                Literal["FBA_INB_0099"],
                Literal["FBA_INB_0100"],
                Literal["FBA_INB_0103"],
                Literal["FBA_INB_0104"],
                Literal["FBA_INB_0197"],
                Literal["UNKNOWN_INB_ERROR_CODE"],
            ]
        ]
    ] = attrs.field(
        default=None,
    )
    """
    Potential Ineligibility Reason Codes.
    """

    is_eligible_for_program: bool = attrs.field()
    """
    Indicates if the item is eligible for the program.
    """

    marketplace_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The marketplace for which eligibility was determined.
    """

    program: Union[Literal["INBOUND"], Literal["COMMINGLING"]] = attrs.field()
    """
    The program for which eligibility was determined.
    """


class FbaInboundEligibilityV1Client(BaseClient):
    def get_item_eligibility_preview(
        self,
        asin: str,
        program: Union[Literal["INBOUND"], Literal["COMMINGLING"]],
        marketplace_ids: List[str] = None,
    ) -> Union[GetItemEligibilityPreviewResponse]:
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
        url = "/fba/inbound/v1/eligibility/itemPreview"
        values = (
            marketplace_ids,
            asin,
            program,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_item_eligibility_preview_params,
        )
        klass = self._get_item_eligibility_preview_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_item_eligibility_preview_params = (  # name, param in
        ("marketplaceIds", "query"),
        ("asin", "query"),
        ("program", "query"),
    )

    _get_item_eligibility_preview_responses = {
        200: GetItemEligibilityPreviewResponse,
        400: GetItemEligibilityPreviewResponse,
        401: GetItemEligibilityPreviewResponse,
        403: GetItemEligibilityPreviewResponse,
        404: GetItemEligibilityPreviewResponse,
        429: GetItemEligibilityPreviewResponse,
        500: GetItemEligibilityPreviewResponse,
        503: GetItemEligibilityPreviewResponse,
    }
