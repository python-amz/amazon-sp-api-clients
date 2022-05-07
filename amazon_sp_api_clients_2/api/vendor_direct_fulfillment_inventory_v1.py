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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InventoryUpdate:

    is_full_update: bool = attrs.field()
    """
    When true, this request contains a full feed. Otherwise, this request contains a partial feed. When sending a full feed, you must send information about all items in the warehouse. Any items not in the full feed are updated as not available. When sending a partial feed, only include the items that need an update to inventory. The status of other items will remain unchanged.
    """

    items: List["ItemDetails"] = attrs.field()
    """
    A list of inventory items with updated details, including quantity available.
    """

    selling_party: "PartyIdentification" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDetails:
    """
    Updated inventory details for an item.
    """

    available_quantity: "ItemQuantity" = attrs.field()
    """
    Details of item quantity.
    """

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    The buyer selected product identification of the item. Either buyerProductIdentifier or vendorProductIdentifier should be submitted.
    """

    is_obsolete: Optional[bool] = attrs.field()
    """
    When true, the item is permanently unavailable.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item. Either buyerProductIdentifier or vendorProductIdentifier should be submitted.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of item quantity.
    """

    amount: Optional[int] = attrs.field()
    """
    Quantity of units available for a specific item.
    """

    unit_of_measure: str = attrs.field()
    """
    Unit of measure for the available quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:

    party_id: str = attrs.field()
    """
    Assigned identification for the party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInventoryUpdateRequest:
    """
    The request body for the submitInventoryUpdate operation.
    """

    inventory: Optional["InventoryUpdate"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInventoryUpdateResponse:
    """
    The response schema for the submitInventoryUpdate operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionReference"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionReference:

    transaction_id: Optional[str] = attrs.field()
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorDirectFulfillmentInventoryV1Client(BaseClient):
    def submit_inventory_update(
        self,
        warehouse_id: str,
        inventory: Dict[str, Any] = None,
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_inventory_update_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _submit_inventory_update_params = (  # name, param in
        ("warehouseId", "path"),
        ("inventory", "body"),
    )

    _submit_inventory_update_responses = {
        (202, "application/json"): SubmitInventoryUpdateResponse,
        (400, "application/json"): SubmitInventoryUpdateResponse,
        (403, "application/json"): SubmitInventoryUpdateResponse,
        (404, "application/json"): SubmitInventoryUpdateResponse,
        (413, "application/json"): SubmitInventoryUpdateResponse,
        (415, "application/json"): SubmitInventoryUpdateResponse,
        (429, "application/json"): SubmitInventoryUpdateResponse,
        (500, "application/json"): SubmitInventoryUpdateResponse,
        (503, "application/json"): SubmitInventoryUpdateResponse,
    }
