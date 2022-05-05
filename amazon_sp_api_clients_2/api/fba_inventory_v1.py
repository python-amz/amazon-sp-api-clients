"""
Selling Partner API for FBA Inventory
=============================================================================================

The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class GetInventorySummariesResponse:
    errors: "ErrorList" = attrs.field()
    pagination: "Pagination" = attrs.field()
    payload: "GetInventorySummariesResult" = attrs.field()
    pass


@attrs.define
class GetInventorySummariesResult:
    granularity: "Granularity" = attrs.field()
    inventory_summaries: "InventorySummaries" = attrs.field()
    pass


@attrs.define
class Granularity:
    granularity_id: str = attrs.field()
    granularity_type: str = attrs.field()

    pass


@attrs.define
class InventoryDetails:
    fulfillable_quantity: int = attrs.field()
    inbound_receiving_quantity: int = attrs.field()
    inbound_shipped_quantity: int = attrs.field()
    inbound_working_quantity: int = attrs.field()

    researching_quantity: "ResearchingQuantity" = attrs.field()
    reserved_quantity: "ReservedQuantity" = attrs.field()
    unfulfillable_quantity: "UnfulfillableQuantity" = attrs.field()
    pass


@attrs.define
class InventorySummaries:
    pass


@attrs.define
class InventorySummary:
    asin: str = attrs.field()
    condition: str = attrs.field()
    fn_sku: str = attrs.field()
    last_updated_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    product_name: str = attrs.field()
    seller_sku: str = attrs.field()
    total_quantity: int = attrs.field()

    inventory_details: "InventoryDetails" = attrs.field()
    pass


@attrs.define
class Pagination:
    next_token: str = attrs.field()

    pass


@attrs.define
class ResearchingQuantity:
    researching_quantity_breakdown: list["ResearchingQuantityEntry"] = attrs.field()
    total_researching_quantity: int = attrs.field()

    pass


@attrs.define
class ResearchingQuantityEntry:
    name: Union[
        Literal["researchingQuantityInShortTerm"],
        Literal["researchingQuantityInMidTerm"],
        Literal["researchingQuantityInLongTerm"],
    ] = attrs.field()
    quantity: int = attrs.field()

    pass


@attrs.define
class ReservedQuantity:
    fc_processing_quantity: int = attrs.field()
    pending_customer_order_quantity: int = attrs.field()
    pending_transshipment_quantity: int = attrs.field()
    total_reserved_quantity: int = attrs.field()

    pass


@attrs.define
class UnfulfillableQuantity:
    carrier_damaged_quantity: int = attrs.field()
    customer_damaged_quantity: int = attrs.field()
    defective_quantity: int = attrs.field()
    distributor_damaged_quantity: int = attrs.field()
    expired_quantity: int = attrs.field()
    total_unfulfillable_quantity: int = attrs.field()
    warehouse_damaged_quantity: int = attrs.field()

    pass


class FbaInventoryV1Client(BaseClient):
    def get_inventory_summaries(
            self,
            granularity_type: Union[Literal["Marketplace"]],
            granularity_id: str,
            marketplace_ids: list[str],
            details: bool = None,
            start_date_time: str = None,
            seller_skus: list[str] = None,
            next_token: str = None,
    ):
        """
        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime and sellerSkus parameters:

        - All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted.
        - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored.
        - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            details: true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value).
            granularity_type: The granularity type for the inventory aggregation level.
            granularity_id: The granularity ID for the inventory aggregation level.
            start_date_time: A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected.
            seller_skus: A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs.
            next_token: String token returned in the response of your previous request.
            marketplace_ids: The marketplace ID for the marketplace for which to return inventory summaries.
        """
        url = "/fba/inventory/v1/summaries"
        values = (
            details,
            granularity_type,
            granularity_id,
            start_date_time,
            seller_skus,
            next_token,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_inventory_summaries_params)
        return response

    _get_inventory_summaries_params = (  # name, param in
        ("details", "query"),
        ("granularityType", "query"),
        ("granularityId", "query"),
        ("startDateTime", "query"),
        ("sellerSkus", "query"),
        ("nextToken", "query"),
        ("marketplaceIds", "query"),
    )
