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
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class InventoryUpdate:

    is_full_update: bool
    items: list["ItemDetails"]

    selling_party: "PartyIdentification"
    pass


@attrs.define
class ItemDetails:

    buyer_product_identifier: str
    is_obsolete: bool
    vendor_product_identifier: str

    available_quantity: "ItemQuantity"
    pass


@attrs.define
class ItemQuantity:

    amount: int
    unit_of_measure: str

    pass


@attrs.define
class PartyIdentification:

    party_id: str

    pass


@attrs.define
class SubmitInventoryUpdateRequest:

    inventory: "InventoryUpdate"
    pass


@attrs.define
class SubmitInventoryUpdateResponse:

    errors: "ErrorList"
    payload: "TransactionReference"
    pass


@attrs.define
class TransactionReference:

    transaction_id: str

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
