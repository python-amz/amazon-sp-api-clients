"""
Selling Partner API for FBA Inventory
=============================================================================================

The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network.
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
    An error response returned when the request is unsuccessful.
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
class GetInventorySummariesResponse:
    """
    The Response schema.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pagination: Optional["Pagination"] = attrs.field()
    """
    The process of returning the results to a request in batches of a defined size called pages. This is done to exercise some control over result size and overall throughput. It's a form of traffic management.
    """

    payload: Optional["GetInventorySummariesResult"] = attrs.field()
    """
    The payload schema for the getInventorySummaries operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetInventorySummariesResult:
    """
    The payload schema for the getInventorySummaries operation.
    """

    granularity: "Granularity" = attrs.field()
    """
    Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace.
    """

    inventory_summaries: List["InventorySummary"] = attrs.field()
    """
    A list of inventory summaries.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Granularity:
    """
    Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace.
    """

    granularity_id: Optional[str] = attrs.field()
    """
    The granularity ID for the specified granularity type. When granularityType is Marketplace, specify the marketplaceId.
    """

    granularity_type: Optional[str] = attrs.field()
    """
    The granularity type for the inventory aggregation level.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InventoryDetails:
    """
    Summarized inventory details. This object will not appear if the details parameter in the request is false.
    """

    fulfillable_quantity: Optional[int] = attrs.field()
    """
    The item quantity that can be picked, packed, and shipped.
    """

    inbound_receiving_quantity: Optional[int] = attrs.field()
    """
    The number of units that have not yet been received at an Amazon fulfillment center for processing, but are part of an inbound shipment with some units that have already been received and processed.
    """

    inbound_shipped_quantity: Optional[int] = attrs.field()
    """
    The number of units in an inbound shipment that you have notified Amazon about and have provided a tracking number.
    """

    inbound_working_quantity: Optional[int] = attrs.field()
    """
    The number of units in an inbound shipment for which you have notified Amazon.
    """

    researching_quantity: Optional["ResearchingQuantity"] = attrs.field()
    """
    The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers.
    """

    reserved_quantity: Optional["ReservedQuantity"] = attrs.field()
    """
    The quantity of reserved inventory.
    """

    unfulfillable_quantity: Optional["UnfulfillableQuantity"] = attrs.field()
    """
    The quantity of unfulfillable inventory.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InventorySummary:
    """
    Inventory summary for a specific item.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of an item.
    """

    condition: Optional[str] = attrs.field()
    """
    The condition of the item as described by the seller (for example, New Item).
    """

    fn_sku: Optional[str] = attrs.field()
    """
    Amazon's fulfillment network SKU identifier.
    """

    inventory_details: Optional["InventoryDetails"] = attrs.field()
    """
    Summarized inventory details. This object will not appear if the details parameter in the request is false.
    """

    last_updated_time: Optional[datetime] = attrs.field()
    """
    The date and time that any quantity was last updated.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    product_name: Optional[str] = attrs.field()
    """
    The localized language product title of the item within the specific marketplace.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item.
    """

    total_quantity: Optional[int] = attrs.field()
    """
    The total number of units in an inbound shipment or in Amazon fulfillment centers.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:
    """
    The process of returning the results to a request in batches of a defined size called pages. This is done to exercise some control over result size and overall throughput. It's a form of traffic management.
    """

    next_token: Optional[str] = attrs.field()
    """
    A generated string used to retrieve the next page of the result. If nextToken is returned, pass the value of nextToken to the next request. If nextToken is not returned, there are no more items to return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ResearchingQuantity:
    """
    The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers.
    """

    researching_quantity_breakdown: Optional[List["ResearchingQuantityEntry"]] = attrs.field()
    """
    A list of quantity details for items currently being researched.
    """

    total_researching_quantity: Optional[int] = attrs.field()
    """
    The total number of units currently being researched in Amazon's fulfillment network.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ResearchingQuantityEntry:
    """
    The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers.
    """

    name: Union[
        Literal["researchingQuantityInShortTerm"],
        Literal["researchingQuantityInMidTerm"],
        Literal["researchingQuantityInLongTerm"],
    ] = attrs.field()
    """
    The duration of the research.
    """

    quantity: int = attrs.field()
    """
    The number of units.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReservedQuantity:
    """
    The quantity of reserved inventory.
    """

    fc_processing_quantity: Optional[int] = attrs.field()
    """
    The number of units that have been sidelined at the fulfillment center for additional processing.
    """

    pending_customer_order_quantity: Optional[int] = attrs.field()
    """
    The number of units reserved for customer orders.
    """

    pending_transshipment_quantity: Optional[int] = attrs.field()
    """
    The number of units being transferred from one fulfillment center to another.
    """

    total_reserved_quantity: Optional[int] = attrs.field()
    """
    The total number of units in Amazon's fulfillment network that are currently being picked, packed, and shipped; or are sidelined for measurement, sampling, or other internal processes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnfulfillableQuantity:
    """
    The quantity of unfulfillable inventory.
    """

    carrier_damaged_quantity: Optional[int] = attrs.field()
    """
    The number of units in carrier damaged disposition.
    """

    customer_damaged_quantity: Optional[int] = attrs.field()
    """
    The number of units in customer damaged disposition.
    """

    defective_quantity: Optional[int] = attrs.field()
    """
    The number of units in defective disposition.
    """

    distributor_damaged_quantity: Optional[int] = attrs.field()
    """
    The number of units in distributor damaged disposition.
    """

    expired_quantity: Optional[int] = attrs.field()
    """
    The number of units in expired disposition.
    """

    total_unfulfillable_quantity: Optional[int] = attrs.field()
    """
    The total number of units in Amazon's fulfillment network in unsellable condition.
    """

    warehouse_damaged_quantity: Optional[int] = attrs.field()
    """
    The number of units in warehouse damaged disposition.
    """


class FbaInventoryV1Client(BaseClient):
    def get_inventory_summaries(
        self,
        granularity_type: Union[Literal["Marketplace"]],
        granularity_id: str,
        marketplace_ids: List[str],
        details: bool = None,
        start_date_time: datetime = None,
        seller_skus: List[str] = None,
        next_token: str = None,
    ) -> Union[GetInventorySummariesResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_inventory_summaries_params,
        )
        klass = self._get_inventory_summaries_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_inventory_summaries_params = (  # name, param in
        ("details", "query"),
        ("granularityType", "query"),
        ("granularityId", "query"),
        ("startDateTime", "query"),
        ("sellerSkus", "query"),
        ("nextToken", "query"),
        ("marketplaceIds", "query"),
    )

    _get_inventory_summaries_responses = {
        200: GetInventorySummariesResponse,
        400: GetInventorySummariesResponse,
        403: GetInventorySummariesResponse,
        404: GetInventorySummariesResponse,
        429: GetInventorySummariesResponse,
        500: GetInventorySummariesResponse,
        503: GetInventorySummariesResponse,
    }
