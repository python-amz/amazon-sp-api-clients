"""
Selling Partner API for Retail Procurement Orders
=============================================================================================

The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AcknowledgementStatusDetails:
    """
    Details of item quantity ordered
    """

    accepted_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """

    acknowledgement_date: Optional[datetime] = attrs.field()
    """
    The date when the line item was confirmed by vendor. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    rejected_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    Address of the party.
    """

    address_line1: str = attrs.field()
    """
    First line of the address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional address information, if required.
    """

    city: Optional[str] = attrs.field()
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.

    Extra fields:
    {'maxLength': 2}
    """

    county: Optional[str] = attrs.field()
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field()
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: Optional[str] = attrs.field()
    """
    The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field()
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DateTimeInterval:
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    pass


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
class GetPurchaseOrderResponse:
    """
    The response schema for the getPurchaseOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Order"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPurchaseOrdersResponse:
    """
    The response schema for the getPurchaseOrders operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPurchaseOrdersStatusResponse:
    """
    The response schema for the getPurchaseOrdersStatus operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderListStatus"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImportDetails:
    """
    Import details for an import order.
    """

    import_containers: Optional[str] = attrs.field()
    """
    Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if the shipment has multiple containers. HC signifies a high-capacity container. Free-text field, limited to 64 characters. The format will be a comma-delimited list containing values of the type: $NUMBER_OF_CONTAINERS_OF_THIS_TYPE-$CONTAINER_TYPE. The list of values for the container type is: 40'(40-foot container), 40'HC (40-foot high-capacity container), 45', 45'HC, 30', 30'HC, 20', 20'HC.

    Extra fields:
    {'maxLength': 64}
    """

    international_commercial_terms: Optional[
        Union[
            Literal["ExWorks"],
            Literal["FreeCarrier"],
            Literal["FreeOnBoard"],
            Literal["FreeAlongSideShip"],
            Literal["CarriagePaidTo"],
            Literal["CostAndFreight"],
            Literal["CarriageAndInsurancePaidTo"],
            Literal["CostInsuranceAndFreight"],
            Literal["DeliveredAtTerminal"],
            Literal["DeliveredAtPlace"],
            Literal["DeliverDutyPaid"],
        ]
    ] = attrs.field()
    """
    Incoterms (International Commercial Terms) are used to divide transaction costs and responsibilities between buyer and seller and reflect state-of-the-art transportation practices. This is for import purchase orders only.
    """

    method_of_payment: Optional[
        Union[
            Literal["PaidByBuyer"],
            Literal["CollectOnDelivery"],
            Literal["DefinedByBuyerAndSeller"],
            Literal["FOBPortOfCall"],
            Literal["PrepaidBySeller"],
            Literal["PaidBySeller"],
        ]
    ] = attrs.field()
    """
    If the recipient requests, contains the shipment method of payment. This is for import PO's only.
    """

    port_of_delivery: Optional[str] = attrs.field()
    """
    The port where goods on an import purchase order must be delivered by the vendor. This should only be specified when the internationalCommercialTerms is FOB.

    Extra fields:
    {'maxLength': 64}
    """

    shipping_instructions: Optional[str] = attrs.field()
    """
    Special instructions regarding the shipment. This field is for import purchase orders.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of quantity ordered.
    """

    amount: Optional[int] = attrs.field()
    """
    Acknowledged quantity. This value should not be zero.
    """

    unit_of_measure: Optional[Union[Literal["Cases"], Literal["Eaches"]]] = attrs.field()
    """
    Unit of measure for the acknowledged quantity.
    """

    unit_size: Optional[int] = attrs.field()
    """
    The case size, in the event that we ordered using cases.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: Optional["Decimal"] = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    currency_code: Optional[str] = attrs.field()
    """
    Three digit currency code in ISO 4217 format. String of length 3.

    Extra fields:
    {'maxLength': 3}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Order:

    order_details: Optional["OrderDetails"] = attrs.field()
    """
    Details of an order.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    purchase_order_state: Union[Literal["New"], Literal["Acknowledged"], Literal["Closed"]] = attrs.field()
    """
    This field will contain the current state of the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAcknowledgement:

    acknowledgement_date: datetime = attrs.field()
    """
    The date and time when the purchase order is acknowledged, in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    items: List["OrderAcknowledgementItem"] = attrs.field()
    """
    A list of the items being acknowledged with associated details.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number. Formatting Notes: 8-character alpha-numeric code.
    """

    selling_party: "PartyIdentification" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAcknowledgementItem:
    """
    Details of the item being acknowledged.
    """

    amazon_product_identifier: Optional[str] = attrs.field()
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    discount_multiplier: Optional[str] = attrs.field()
    """
    The discount multiplier that should be applied to the price if a vendor sells books with a list price. This is a multiplier factor to arrive at a final discounted price. A multiplier of .90 would be the factor if a 10% discount is given.
    """

    item_acknowledgements: List["OrderItemAcknowledgement"] = attrs.field()
    """
    This is used to indicate acknowledged quantity.
    """

    item_sequence_number: Optional[str] = attrs.field()
    """
    Line item sequence number for the item.
    """

    list_price: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    net_cost: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity ordered.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item. Should be the same as was sent in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderDetails:
    """
    Details of an order.
    """

    bill_to_party: Optional["PartyIdentification"] = attrs.field()

    buying_party: Optional["PartyIdentification"] = attrs.field()

    deal_code: Optional[str] = attrs.field()
    """
    If requested by the recipient, this field will contain a promotional/deal number. The discount code line is optional. It is used to obtain a price discount on items on the order.
    """

    delivery_window: Optional["DateTimeInterval"] = attrs.field()
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """

    import_details: Optional["ImportDetails"] = attrs.field()
    """
    Import details for an import order.
    """

    items: List["OrderItem"] = attrs.field()
    """
    A list of items in this purchase order.
    """

    payment_method: Optional[
        Union[Literal["Invoice"], Literal["Consignment"], Literal["CreditCard"], Literal["Prepaid"]]
    ] = attrs.field()
    """
    Payment method used.
    """

    purchase_order_changed_date: Optional[datetime] = attrs.field()
    """
    The date when purchase order was last changed by Amazon after the order was placed. This date will be greater than 'purchaseOrderDate'. This means the PO data was changed on that date and vendors are required to fulfill the  updated PO. The PO changes can be related to Item Quantity, Ship to Location, Ship Window etc. This field will not be present in orders that have not changed after creation. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_date: datetime = attrs.field()
    """
    The date the purchase order was placed. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_state_changed_date: datetime = attrs.field()
    """
    The date when current purchase order state was changed. Current purchase order state is available in the field 'purchaseOrderState'. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_type: Optional[
        Union[
            Literal["RegularOrder"], Literal["ConsignedOrder"], Literal["NewProductIntroduction"], Literal["RushOrder"]
        ]
    ] = attrs.field()
    """
    Type of purchase order.
    """

    selling_party: Optional["PartyIdentification"] = attrs.field()

    ship_to_party: Optional["PartyIdentification"] = attrs.field()

    ship_window: Optional["DateTimeInterval"] = attrs.field()
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItem:

    amazon_product_identifier: Optional[str] = attrs.field()
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    is_back_order_allowed: bool = attrs.field()
    """
    When true, we will accept backorder confirmations for this item.
    """

    item_sequence_number: str = attrs.field()
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    list_price: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    net_cost: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity ordered.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemAcknowledgement:

    acknowledged_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity ordered.
    """

    acknowledgement_code: Union[Literal["Accepted"], Literal["Backordered"], Literal["Rejected"]] = attrs.field()
    """
    This indicates the acknowledgement code.
    """

    rejection_reason: Optional[
        Union[Literal["TemporarilyUnavailable"], Literal["InvalidProductIdentifier"], Literal["ObsoleteProduct"]]
    ] = attrs.field()
    """
    Indicates the reason for rejection.
    """

    scheduled_delivery_date: Optional[datetime] = attrs.field()
    """
    Estimated delivery date per line item. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    scheduled_ship_date: Optional[datetime] = attrs.field()
    """
    Estimated ship date per line item. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatus:

    acknowledgement_status: Optional["OrderItemStatusAcknowledgementStatus"] = attrs.field()
    """
    Acknowledgement status information.
    """

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    Buyer's Standard Identification Number (ASIN) of an item.
    """

    item_sequence_number: str = attrs.field()
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    list_price: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    net_cost: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: Optional["OrderItemStatusOrderedQuantity"] = attrs.field()
    """
    Ordered quantity information.
    """

    receiving_status: Optional["OrderItemStatusReceivingStatus"] = attrs.field()
    """
    Item receive status at the buyer's warehouse.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatusAcknowledgementStatus:
    """
    Acknowledgement status information.
    """

    accepted_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """

    acknowledgement_status_details: Optional[List["AcknowledgementStatusDetails"]] = attrs.field()
    """
    Details of item quantity confirmed.
    """

    confirmation_status: Optional[
        Union[Literal["ACCEPTED"], Literal["PARTIALLY_ACCEPTED"], Literal["REJECTED"], Literal["UNCONFIRMED"]]
    ] = attrs.field()
    """
    Confirmation status of line item.
    """

    rejected_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatusOrderedQuantity:
    """
    Ordered quantity information.
    """

    ordered_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """

    ordered_quantity_details: Optional[List["OrderedQuantityDetails"]] = attrs.field()
    """
    Details of item quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatusReceivingStatus:
    """
    Item receive status at the buyer's warehouse.
    """

    last_receive_date: Optional[datetime] = attrs.field()
    """
    The date when the most recent item was received at the buyer's warehouse. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    receive_status: Optional[
        Union[Literal["NOT_RECEIVED"], Literal["PARTIALLY_RECEIVED"], Literal["RECEIVED"]]
    ] = attrs.field()
    """
    Receive status of the line item.
    """

    received_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderList:

    orders: Optional[List["Order"]] = attrs.field()

    pagination: Optional["Pagination"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderListStatus:

    orders_status: Optional[List["OrderStatus"]] = attrs.field()

    pagination: Optional["Pagination"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderStatus:
    """
    Current status of a purchase order.
    """

    item_status: List["OrderItemStatus"] = attrs.field()
    """
    Detailed description of items order status.
    """

    last_updated_date: Optional[datetime] = attrs.field()
    """
    The date when the purchase order was last updated. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_date: datetime = attrs.field()
    """
    The date the purchase order was placed. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_number: str = attrs.field()
    """
    The buyer's purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    purchase_order_status: Union[Literal["OPEN"], Literal["CLOSED"]] = attrs.field()
    """
    The status of the buyer's purchase order for this order.
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_to_party: "PartyIdentification" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderedQuantityDetails:
    """
    Details of item quantity ordered
    """

    cancelled_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """

    ordered_quantity: Optional["ItemQuantity"] = attrs.field()
    """
    Details of quantity ordered.
    """

    updated_date: Optional[datetime] = attrs.field()
    """
    The date when the line item quantity was updated by buyer. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:

    next_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more purchase order items to return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:

    address: Optional["Address"] = attrs.field()
    """
    Address of the party.
    """

    party_id: str = attrs.field()
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    tax_info: Optional["TaxRegistrationDetails"] = attrs.field()
    """
    Tax registration details of the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementRequest:
    """
    The request schema for the submitAcknowledgment operation.
    """

    acknowledgements: Optional[List["OrderAcknowledgement"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementResponse:
    """
    The response schema for the submitAcknowledgement operation
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_number: str = attrs.field()
    """
    Tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()
    """
    Tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionId:

    transaction_id: Optional[str] = attrs.field()
    """
    GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorOrdersV1Client(BaseClient):
    def get_purchase_order(
        self,
        purchase_order_number: str,
    ) -> Union[GetPurchaseOrderResponse]:
        """
        Returns a purchase order based on the purchaseOrderNumber value that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchase order identifier for the order that you want. Formatting Notes: 8-character alpha-numeric code.
        """
        url = "/vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_purchase_order_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_purchase_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_purchase_order_responses = {
        (200, "application/json"): GetPurchaseOrderResponse,
        (400, "application/json"): GetPurchaseOrderResponse,
        (401, "application/json"): GetPurchaseOrderResponse,
        (403, "application/json"): GetPurchaseOrderResponse,
        (404, "application/json"): GetPurchaseOrderResponse,
        (415, "application/json"): GetPurchaseOrderResponse,
        (429, "application/json"): GetPurchaseOrderResponse,
        (500, "application/json"): GetPurchaseOrderResponse,
        (503, "application/json"): GetPurchaseOrderResponse,
    }

    def get_purchase_orders(
        self,
        limit: int = None,
        created_after: datetime = None,
        created_before: datetime = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
        include_details: bool = None,
        changed_after: datetime = None,
        changed_before: datetime = None,
        po_item_state: Union[Literal["Cancelled"]] = None,
        is_pochanged: bool = None,
        purchase_order_state: Union[Literal["New"], Literal["Acknowledged"], Literal["Closed"]] = None,
        ordering_vendor_code: str = None,
    ) -> Union[GetPurchaseOrdersResponse]:
        """
        Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder operation to receive details for a specific purchase order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            limit: The limit to the number of records returned. Default value is 100 records.
            created_after: Purchase orders that became available after this time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort in ascending or descending order by purchase order creation date.
            next_token: Used for pagination when there is more purchase orders than the specified result size limit. The token value is returned in the previous API call
            include_details: When true, returns purchase orders with complete details. Otherwise, only purchase order numbers are returned. Default value is true.
            changed_after: Purchase orders that changed after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            changed_before: Purchase orders that changed before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            po_item_state: Current state of the purchase order item. If this value is Cancelled, this API will return purchase orders which have one or more items cancelled by Amazon with updated item quantity as zero.
            is_pochanged: When true, returns purchase orders which were modified after the order was placed. Vendors are required to pull the changed purchase order and fulfill the updated purchase order and not the original one. Default value is false.
            purchase_order_state: Filters purchase orders based on the purchase order state.
            ordering_vendor_code: Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in the filter, all purchase orders for all of the vendor codes that exist in the vendor group used to authorize the API client application are returned.
        """
        url = "/vendor/orders/v1/purchaseOrders"
        values = (
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
            include_details,
            changed_after,
            changed_before,
            po_item_state,
            is_pochanged,
            purchase_order_state,
            ordering_vendor_code,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_purchase_orders_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_purchase_orders_params = (  # name, param in
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
        ("includeDetails", "query"),
        ("changedAfter", "query"),
        ("changedBefore", "query"),
        ("poItemState", "query"),
        ("isPOChanged", "query"),
        ("purchaseOrderState", "query"),
        ("orderingVendorCode", "query"),
    )

    _get_purchase_orders_responses = {
        (200, "application/json"): GetPurchaseOrdersResponse,
        (400, "application/json"): GetPurchaseOrdersResponse,
        (403, "application/json"): GetPurchaseOrdersResponse,
        (404, "application/json"): GetPurchaseOrdersResponse,
        (415, "application/json"): GetPurchaseOrdersResponse,
        (429, "application/json"): GetPurchaseOrdersResponse,
        (500, "application/json"): GetPurchaseOrdersResponse,
        (503, "application/json"): GetPurchaseOrdersResponse,
    }

    def get_purchase_orders_status(
        self,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
        created_after: datetime = None,
        created_before: datetime = None,
        updated_after: datetime = None,
        updated_before: datetime = None,
        purchase_order_number: str = None,
        purchase_order_status: Union[Literal["OPEN"], Literal["CLOSED"]] = None,
        item_confirmation_status: Union[
            Literal["ACCEPTED"], Literal["PARTIALLY_ACCEPTED"], Literal["REJECTED"], Literal["UNCONFIRMED"]
        ] = None,
        item_receive_status: Union[Literal["NOT_RECEIVED"], Literal["PARTIALLY_RECEIVED"], Literal["RECEIVED"]] = None,
        ordering_vendor_code: str = None,
        ship_to_party_id: str = None,
    ) -> Union[GetPurchaseOrdersStatusResponse]:
        """
        Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            limit: The limit to the number of records returned. Default value is 100 records.
            sort_order: Sort in ascending or descending order by purchase order creation date.
            next_token: Used for pagination when there are more purchase orders than the specified result size limit.
            created_after: Purchase orders that became available after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            updated_after: Purchase orders for which the last purchase order update happened after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            updated_before: Purchase orders for which the last purchase order update happened before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            purchase_order_number: Provides purchase order status for the specified purchase order number.
            purchase_order_status: Filters purchase orders based on the specified purchase order status. If not included in filter, this will return purchase orders for all statuses.
            item_confirmation_status: Filters purchase orders based on their item confirmation status. If the item confirmation status is not included in the filter, purchase orders for all confirmation statuses are included.
            item_receive_status: Filters purchase orders based on the purchase order's item receive status. If the item receive status is not included in the filter, purchase orders for all receive statuses are included.
            ordering_vendor_code: Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in filter, all purchase orders for all the vendor codes that exist in the vendor group used to authorize API client application are returned.
            ship_to_party_id: Filters purchase orders for a specific buyer's Fulfillment Center/warehouse by providing ship to location id here. This value should be same as 'shipToParty.partyId' in the purchase order. If not included in filter, this will return purchase orders for all the buyer's warehouses used for vendor group purchase orders.
        """
        url = "/vendor/orders/v1/purchaseOrdersStatus"
        values = (
            limit,
            sort_order,
            next_token,
            created_after,
            created_before,
            updated_after,
            updated_before,
            purchase_order_number,
            purchase_order_status,
            item_confirmation_status,
            item_receive_status,
            ordering_vendor_code,
            ship_to_party_id,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_purchase_orders_status_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_purchase_orders_status_params = (  # name, param in
        ("limit", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("updatedAfter", "query"),
        ("updatedBefore", "query"),
        ("purchaseOrderNumber", "query"),
        ("purchaseOrderStatus", "query"),
        ("itemConfirmationStatus", "query"),
        ("itemReceiveStatus", "query"),
        ("orderingVendorCode", "query"),
        ("shipToPartyId", "query"),
    )

    _get_purchase_orders_status_responses = {
        (200, "application/json"): GetPurchaseOrdersStatusResponse,
        (400, "application/json"): GetPurchaseOrdersStatusResponse,
        (403, "application/json"): GetPurchaseOrdersStatusResponse,
        (404, "application/json"): GetPurchaseOrdersStatusResponse,
        (415, "application/json"): GetPurchaseOrdersStatusResponse,
        (429, "application/json"): GetPurchaseOrdersStatusResponse,
        (500, "application/json"): GetPurchaseOrdersStatusResponse,
        (503, "application/json"): GetPurchaseOrdersStatusResponse,
    }

    def submit_acknowledgement(
        self,
        acknowledgements: List["OrderAcknowledgement"] = None,
    ) -> Union[SubmitAcknowledgementResponse]:
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            acknowledgements: no description.
        """
        url = "/vendor/orders/v1/acknowledgements"
        values = (acknowledgements,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_acknowledgement_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _submit_acknowledgement_params = (("acknowledgements", "body"),)  # name, param in

    _submit_acknowledgement_responses = {
        (202, "application/json"): SubmitAcknowledgementResponse,
        (400, "application/json"): SubmitAcknowledgementResponse,
        (403, "application/json"): SubmitAcknowledgementResponse,
        (404, "application/json"): SubmitAcknowledgementResponse,
        (413, "application/json"): SubmitAcknowledgementResponse,
        (415, "application/json"): SubmitAcknowledgementResponse,
        (429, "application/json"): SubmitAcknowledgementResponse,
        (500, "application/json"): SubmitAcknowledgementResponse,
        (503, "application/json"): SubmitAcknowledgementResponse,
    }
