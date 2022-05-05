"""
Selling Partner API for Direct Fulfillment Inventory Updates
=============================================================================================

The Selling Partner API for Direct Fulfillment Inventory Updates provides programmatic access to a direct fulfillment vendor's inventory updates.
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
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class InventoryUpdate:

    is_full_update: bool
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'boolean'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/ItemDetails')}

    selling_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'ref': '#/components/schemas/PartyIdentification'}
    pass


@attrs.define
class ItemDetails:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}
    is_obsolete: bool
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'boolean'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}

    available_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'ref': '#/components/schemas/ItemQuantity'}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'integer'}
    unit_of_measure: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}

    pass


@attrs.define
class SubmitInventoryUpdateRequest:

    inventory: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'ref': '#/components/schemas/InventoryUpdate'}
    pass


@attrs.define
class SubmitInventoryUpdateResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'ref': '#/components/schemas/TransactionReference'}
    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB700>, 'type': 'string'}

    pass


class VendorDirectFulfillmentInventoryV1Client(BaseClient):
    def submit_inventory_update(
        self,
        warehouse_id: str,
        inventory: dict[str, Any] = None,
    ):
        """
        Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            warehouse_id: Identifier for the warehouse for which to update inventory.
            inventory: no description.
        """
        url = "/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items"
        values = (
            warehouse_id,
            inventory,
        )
        response = self._parse_args_and_request(url, "POST", values, self._submit_inventory_update_params)
        return response

    _submit_inventory_update_params = (  # name, param in
        ("warehouseId", "path"),
        ("inventory", "body"),
    )
