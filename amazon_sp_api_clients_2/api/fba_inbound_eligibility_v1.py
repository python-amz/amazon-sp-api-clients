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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetItemEligibilityPreviewResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B700>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ItemEligibilityPreview', 'generator': <__mp_main__.Generator object at 0x000002365F44B700>}
    pass


@attrs.define
class ItemEligibilityPreview:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'string'}
    ineligibility_reason_list: list[
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
    # {'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=['FBA_INB_0004', 'FBA_INB_0006', 'FBA_INB_0007', 'FBA_INB_0008', 'FBA_INB_0009', 'FBA_INB_0010', 'FBA_INB_0011', 'FBA_INB_0012', 'FBA_INB_0013', 'FBA_INB_0014', 'FBA_INB_0015', 'FBA_INB_0016', 'FBA_INB_0017', 'FBA_INB_0018', 'FBA_INB_0019', 'FBA_INB_0034', 'FBA_INB_0035', 'FBA_INB_0036', 'FBA_INB_0037', 'FBA_INB_0038', 'FBA_INB_0050', 'FBA_INB_0051', 'FBA_INB_0053', 'FBA_INB_0055', 'FBA_INB_0056', 'FBA_INB_0059', 'FBA_INB_0065', 'FBA_INB_0066', 'FBA_INB_0067', 'FBA_INB_0068', 'FBA_INB_0095', 'FBA_INB_0097', 'FBA_INB_0098', 'FBA_INB_0099', 'FBA_INB_0100', 'FBA_INB_0103', 'FBA_INB_0104', 'FBA_INB_0197', 'UNKNOWN_INB_ERROR_CODE'], type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Potential Ineligibility Reason Codes.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'array'}
    is_eligible_for_program: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'boolean'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'type': 'string'}
    program: Union[Literal["INBOUND"], Literal["COMMINGLING"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B700>, 'enum': ['INBOUND', 'COMMINGLING'], 'type': 'string'}

    pass


class FbaInboundEligibilityV1Client(BaseClient):
    def get_item_eligibility_preview(
        self,
        asin: str,
        program: Union[Literal["INBOUND"], Literal["COMMINGLING"]],
        marketplace_ids: list[str] = None,
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
        url = "/fba/inbound/v1/eligibility/itemPreview"
        values = (
            marketplace_ids,
            asin,
            program,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_item_eligibility_preview_params)
        return response

    _get_item_eligibility_preview_params = (  # name, param in
        ("marketplaceIds", "query"),
        ("asin", "query"),
        ("program", "query"),
    )
