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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _acknowledgement_status_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return AcknowledgementStatusDetails(**data)

    accepted_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    acknowledgement_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date when the line item was confirmed by vendor. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    rejected_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    Address of the party.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Address(**data)

    address_line1: str = attrs.field(
        default=None,
    )
    """
    First line of the address.
    """

    address_line2: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field(
        default=None,
    )
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.

    Extra fields:
    {'maxLength': 2}
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field(
        default=None,
    )
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DateTimeInterval:
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _date_time_interval_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return DateTimeInterval(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _decimal_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Decimal(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPurchaseOrderResponse:
    """
    The response schema for the getPurchaseOrder operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_purchase_order_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetPurchaseOrderResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Order"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPurchaseOrdersResponse:
    """
    The response schema for the getPurchaseOrders operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_purchase_orders_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetPurchaseOrdersResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderList"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPurchaseOrdersStatusResponse:
    """
    The response schema for the getPurchaseOrdersStatus operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_purchase_orders_status_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetPurchaseOrdersStatusResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderListStatus"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImportDetails:
    """
    Import details for an import order.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _import_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ImportDetails(**data)

    import_containers: Optional[str] = attrs.field(
        default=None,
    )
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
    ] = attrs.field(
        default=None,
    )
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
    ] = attrs.field(
        default=None,
    )
    """
    If the recipient requests, contains the shipment method of payment. This is for import PO's only.
    """

    port_of_delivery: Optional[str] = attrs.field(
        default=None,
    )
    """
    The port where goods on an import purchase order must be delivered by the vendor. This should only be specified when the internationalCommercialTerms is FOB.

    Extra fields:
    {'maxLength': 64}
    """

    shipping_instructions: Optional[str] = attrs.field(
        default=None,
    )
    """
    Special instructions regarding the shipment. This field is for import purchase orders.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of quantity ordered.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_quantity_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ItemQuantity(**data)

    amount: Optional[int] = attrs.field(
        default=None,
    )
    """
    Acknowledged quantity. This value should not be zero.
    """

    unit_of_measure: Optional[Union[Literal["Cases"], Literal["Eaches"]]] = attrs.field(
        default=None,
    )
    """
    Unit of measure for the acknowledged quantity.
    """

    unit_size: Optional[int] = attrs.field(
        default=None,
    )
    """
    The case size, in the event that we ordered using cases.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Money(**data)

    amount: Optional["Decimal"] = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    currency_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    Three digit currency code in ISO 4217 format. String of length 3.

    Extra fields:
    {'maxLength': 3}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Order:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Order(**data)

    order_details: Optional["OrderDetails"] = attrs.field(
        default=None,
    )
    """
    Details of an order.
    """

    purchase_order_number: str = attrs.field(
        default=None,
    )
    """
    The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    purchase_order_state: Union[Literal["New"], Literal["Acknowledged"], Literal["Closed"]] = attrs.field(
        default=None,
    )
    """
    This field will contain the current state of the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAcknowledgement:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_acknowledgement_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderAcknowledgement(**data)

    acknowledgement_date: datetime = attrs.field(
        default=None,
    )
    """
    The date and time when the purchase order is acknowledged, in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    items: List["OrderAcknowledgementItem"] = attrs.field(
        default=None,
    )
    """
    A list of the items being acknowledged with associated details.
    """

    purchase_order_number: str = attrs.field(
        default=None,
    )
    """
    The purchase order number. Formatting Notes: 8-character alpha-numeric code.
    """

    selling_party: "PartyIdentification" = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAcknowledgementItem:
    """
    Details of the item being acknowledged.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_acknowledgement_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderAcknowledgementItem(**data)

    amazon_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    discount_multiplier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The discount multiplier that should be applied to the price if a vendor sells books with a list price. This is a multiplier factor to arrive at a final discounted price. A multiplier of .90 would be the factor if a 10% discount is given.
    """

    item_acknowledgements: List["OrderItemAcknowledgement"] = attrs.field(
        default=None,
    )
    """
    This is used to indicate acknowledged quantity.
    """

    item_sequence_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    Line item sequence number for the item.
    """

    list_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    net_cost: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: "ItemQuantity" = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderDetails:
    """
    Details of an order.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderDetails(**data)

    bill_to_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    buying_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    deal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    If requested by the recipient, this field will contain a promotional/deal number. The discount code line is optional. It is used to obtain a price discount on items on the order.
    """

    delivery_window: Optional["DateTimeInterval"] = attrs.field(
        default=None,
    )
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """

    import_details: Optional["ImportDetails"] = attrs.field(
        default=None,
    )
    """
    Import details for an import order.
    """

    items: List["OrderItem"] = attrs.field(
        default=None,
    )
    """
    A list of items in this purchase order.
    """

    payment_method: Optional[
        Union[Literal["Invoice"], Literal["Consignment"], Literal["CreditCard"], Literal["Prepaid"]]
    ] = attrs.field(
        default=None,
    )
    """
    Payment method used.
    """

    purchase_order_changed_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date when purchase order was last changed by Amazon after the order was placed. This date will be greater than 'purchaseOrderDate'. This means the PO data was changed on that date and vendors are required to fulfill the  updated PO. The PO changes can be related to Item Quantity, Ship to Location, Ship Window etc. This field will not be present in orders that have not changed after creation. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_date: datetime = attrs.field(
        default=None,
    )
    """
    The date the purchase order was placed. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_state_changed_date: datetime = attrs.field(
        default=None,
    )
    """
    The date when current purchase order state was changed. Current purchase order state is available in the field 'purchaseOrderState'. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_type: Optional[
        Union[
            Literal["RegularOrder"], Literal["ConsignedOrder"], Literal["NewProductIntroduction"], Literal["RushOrder"]
        ]
    ] = attrs.field(
        default=None,
    )
    """
    Type of purchase order.
    """

    selling_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    ship_to_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    ship_window: Optional["DateTimeInterval"] = attrs.field(
        default=None,
    )
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItem:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderItem(**data)

    amazon_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    is_back_order_allowed: bool = attrs.field(
        default=None,
    )
    """
    When true, we will accept backorder confirmations for this item.
    """

    item_sequence_number: str = attrs.field(
        default=None,
    )
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    list_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    net_cost: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: "ItemQuantity" = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemAcknowledgement:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_acknowledgement_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderItemAcknowledgement(**data)

    acknowledged_quantity: "ItemQuantity" = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    acknowledgement_code: Union[Literal["Accepted"], Literal["Backordered"], Literal["Rejected"]] = attrs.field(
        default=None,
    )
    """
    This indicates the acknowledgement code.
    """

    rejection_reason: Optional[
        Union[Literal["TemporarilyUnavailable"], Literal["InvalidProductIdentifier"], Literal["ObsoleteProduct"]]
    ] = attrs.field(
        default=None,
    )
    """
    Indicates the reason for rejection.
    """

    scheduled_delivery_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Estimated delivery date per line item. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    scheduled_ship_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Estimated ship date per line item. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatus:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderItemStatus(**data)

    acknowledgement_status: Optional["OrderItemStatusAcknowledgementStatus"] = attrs.field(
        default=None,
    )
    """
    Acknowledgement status information.
    """

    buyer_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Buyer's Standard Identification Number (ASIN) of an item.
    """

    item_sequence_number: str = attrs.field(
        default=None,
    )
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    list_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    net_cost: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: Optional["OrderItemStatusOrderedQuantity"] = attrs.field(
        default=None,
    )
    """
    Ordered quantity information.
    """

    receiving_status: Optional["OrderItemStatusReceivingStatus"] = attrs.field(
        default=None,
    )
    """
    Item receive status at the buyer's warehouse.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatusAcknowledgementStatus:
    """
    Acknowledgement status information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_status_acknowledgement_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderItemStatusAcknowledgementStatus(**data)

    accepted_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    acknowledgement_status_details: Optional[List["AcknowledgementStatusDetails"]] = attrs.field(
        default=None,
    )
    """
    Details of item quantity confirmed.
    """

    confirmation_status: Optional[
        Union[Literal["ACCEPTED"], Literal["PARTIALLY_ACCEPTED"], Literal["REJECTED"], Literal["UNCONFIRMED"]]
    ] = attrs.field(
        default=None,
    )
    """
    Confirmation status of line item.
    """

    rejected_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatusOrderedQuantity:
    """
    Ordered quantity information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_status_ordered_quantity_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderItemStatusOrderedQuantity(**data)

    ordered_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    ordered_quantity_details: Optional[List["OrderedQuantityDetails"]] = attrs.field(
        default=None,
    )
    """
    Details of item quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemStatusReceivingStatus:
    """
    Item receive status at the buyer's warehouse.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_status_receiving_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderItemStatusReceivingStatus(**data)

    last_receive_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date when the most recent item was received at the buyer's warehouse. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    receive_status: Optional[
        Union[Literal["NOT_RECEIVED"], Literal["PARTIALLY_RECEIVED"], Literal["RECEIVED"]]
    ] = attrs.field(
        default=None,
    )
    """
    Receive status of the line item.
    """

    received_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderList:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_list_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderList(**data)

    orders: Optional[List["Order"]] = attrs.field(
        default=None,
    )

    pagination: Optional["Pagination"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderListStatus:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_list_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderListStatus(**data)

    orders_status: Optional[List["OrderStatus"]] = attrs.field(
        default=None,
    )

    pagination: Optional["Pagination"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderStatus:
    """
    Current status of a purchase order.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderStatus(**data)

    item_status: List["OrderItemStatus"] = attrs.field(
        default=None,
    )
    """
    Detailed description of items order status.
    """

    last_updated_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date when the purchase order was last updated. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_date: datetime = attrs.field(
        default=None,
    )
    """
    The date the purchase order was placed. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_number: str = attrs.field(
        default=None,
    )
    """
    The buyer's purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    purchase_order_status: Union[Literal["OPEN"], Literal["CLOSED"]] = attrs.field(
        default=None,
    )
    """
    The status of the buyer's purchase order for this order.
    """

    selling_party: "PartyIdentification" = attrs.field(
        default=None,
    )

    ship_to_party: "PartyIdentification" = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderedQuantityDetails:
    """
    Details of item quantity ordered
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _ordered_quantity_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return OrderedQuantityDetails(**data)

    cancelled_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    ordered_quantity: Optional["ItemQuantity"] = attrs.field(
        default=None,
    )
    """
    Details of quantity ordered.
    """

    updated_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date when the line item quantity was updated by buyer. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _pagination_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Pagination(**data)

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more purchase order items to return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _party_identification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return PartyIdentification(**data)

    address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    Address of the party.
    """

    party_id: str = attrs.field(
        default=None,
    )
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    tax_info: Optional["TaxRegistrationDetails"] = attrs.field(
        default=None,
    )
    """
    Tax registration details of the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementRequest:
    """
    The request schema for the submitAcknowledgment operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_acknowledgement_request_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitAcknowledgementRequest(**data)

    acknowledgements: Optional[List["OrderAcknowledgement"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementResponse:
    """
    The response schema for the submitAcknowledgement operation
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_acknowledgement_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitAcknowledgementResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionId"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_registration_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TaxRegistrationDetails(**data)

    tax_registration_number: str = attrs.field(
        default=None,
    )
    """
    Tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        default=None,
    )
    """
    Tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionId:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_id_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TransactionId(**data)

    transaction_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


_acknowledgement_status_details_name_convert = {
    "acceptedQuantity": "accepted_quantity",
    "acknowledgementDate": "acknowledgement_date",
    "rejectedQuantity": "rejected_quantity",
}

_address_name_convert = {
    "addressLine1": "address_line1",
    "addressLine2": "address_line2",
    "addressLine3": "address_line3",
    "city": "city",
    "countryCode": "country_code",
    "county": "county",
    "district": "district",
    "name": "name",
    "phone": "phone",
    "postalCode": "postal_code",
    "stateOrRegion": "state_or_region",
}

_date_time_interval_name_convert = {}

_decimal_name_convert = {}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_get_purchase_order_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_purchase_orders_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_purchase_orders_status_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_import_details_name_convert = {
    "importContainers": "import_containers",
    "internationalCommercialTerms": "international_commercial_terms",
    "methodOfPayment": "method_of_payment",
    "portOfDelivery": "port_of_delivery",
    "shippingInstructions": "shipping_instructions",
}

_item_quantity_name_convert = {
    "amount": "amount",
    "unitOfMeasure": "unit_of_measure",
    "unitSize": "unit_size",
}

_money_name_convert = {
    "amount": "amount",
    "currencyCode": "currency_code",
}

_order_name_convert = {
    "orderDetails": "order_details",
    "purchaseOrderNumber": "purchase_order_number",
    "purchaseOrderState": "purchase_order_state",
}

_order_acknowledgement_name_convert = {
    "acknowledgementDate": "acknowledgement_date",
    "items": "items",
    "purchaseOrderNumber": "purchase_order_number",
    "sellingParty": "selling_party",
}

_order_acknowledgement_item_name_convert = {
    "amazonProductIdentifier": "amazon_product_identifier",
    "discountMultiplier": "discount_multiplier",
    "itemAcknowledgements": "item_acknowledgements",
    "itemSequenceNumber": "item_sequence_number",
    "listPrice": "list_price",
    "netCost": "net_cost",
    "orderedQuantity": "ordered_quantity",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_order_details_name_convert = {
    "billToParty": "bill_to_party",
    "buyingParty": "buying_party",
    "dealCode": "deal_code",
    "deliveryWindow": "delivery_window",
    "importDetails": "import_details",
    "items": "items",
    "paymentMethod": "payment_method",
    "purchaseOrderChangedDate": "purchase_order_changed_date",
    "purchaseOrderDate": "purchase_order_date",
    "purchaseOrderStateChangedDate": "purchase_order_state_changed_date",
    "purchaseOrderType": "purchase_order_type",
    "sellingParty": "selling_party",
    "shipToParty": "ship_to_party",
    "shipWindow": "ship_window",
}

_order_item_name_convert = {
    "amazonProductIdentifier": "amazon_product_identifier",
    "isBackOrderAllowed": "is_back_order_allowed",
    "itemSequenceNumber": "item_sequence_number",
    "listPrice": "list_price",
    "netCost": "net_cost",
    "orderedQuantity": "ordered_quantity",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_order_item_acknowledgement_name_convert = {
    "acknowledgedQuantity": "acknowledged_quantity",
    "acknowledgementCode": "acknowledgement_code",
    "rejectionReason": "rejection_reason",
    "scheduledDeliveryDate": "scheduled_delivery_date",
    "scheduledShipDate": "scheduled_ship_date",
}

_order_item_status_name_convert = {
    "acknowledgementStatus": "acknowledgement_status",
    "buyerProductIdentifier": "buyer_product_identifier",
    "itemSequenceNumber": "item_sequence_number",
    "listPrice": "list_price",
    "netCost": "net_cost",
    "orderedQuantity": "ordered_quantity",
    "receivingStatus": "receiving_status",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_order_item_status_acknowledgement_status_name_convert = {
    "acceptedQuantity": "accepted_quantity",
    "acknowledgementStatusDetails": "acknowledgement_status_details",
    "confirmationStatus": "confirmation_status",
    "rejectedQuantity": "rejected_quantity",
}

_order_item_status_ordered_quantity_name_convert = {
    "orderedQuantity": "ordered_quantity",
    "orderedQuantityDetails": "ordered_quantity_details",
}

_order_item_status_receiving_status_name_convert = {
    "lastReceiveDate": "last_receive_date",
    "receiveStatus": "receive_status",
    "receivedQuantity": "received_quantity",
}

_order_list_name_convert = {
    "orders": "orders",
    "pagination": "pagination",
}

_order_list_status_name_convert = {
    "ordersStatus": "orders_status",
    "pagination": "pagination",
}

_order_status_name_convert = {
    "itemStatus": "item_status",
    "lastUpdatedDate": "last_updated_date",
    "purchaseOrderDate": "purchase_order_date",
    "purchaseOrderNumber": "purchase_order_number",
    "purchaseOrderStatus": "purchase_order_status",
    "sellingParty": "selling_party",
    "shipToParty": "ship_to_party",
}

_ordered_quantity_details_name_convert = {
    "cancelledQuantity": "cancelled_quantity",
    "orderedQuantity": "ordered_quantity",
    "updatedDate": "updated_date",
}

_pagination_name_convert = {
    "nextToken": "next_token",
}

_party_identification_name_convert = {
    "address": "address",
    "partyId": "party_id",
    "taxInfo": "tax_info",
}

_submit_acknowledgement_request_name_convert = {
    "acknowledgements": "acknowledgements",
}

_submit_acknowledgement_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_tax_registration_details_name_convert = {
    "taxRegistrationNumber": "tax_registration_number",
    "taxRegistrationType": "tax_registration_type",
}

_transaction_id_name_convert = {
    "transactionId": "transaction_id",
}


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
            self._get_purchase_order_responses,
        )
        return response

    _get_purchase_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_purchase_order_responses = {
        200: GetPurchaseOrderResponse,
        400: GetPurchaseOrderResponse,
        401: GetPurchaseOrderResponse,
        403: GetPurchaseOrderResponse,
        404: GetPurchaseOrderResponse,
        415: GetPurchaseOrderResponse,
        429: GetPurchaseOrderResponse,
        500: GetPurchaseOrderResponse,
        503: GetPurchaseOrderResponse,
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
            self._get_purchase_orders_responses,
        )
        return response

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
        200: GetPurchaseOrdersResponse,
        400: GetPurchaseOrdersResponse,
        403: GetPurchaseOrdersResponse,
        404: GetPurchaseOrdersResponse,
        415: GetPurchaseOrdersResponse,
        429: GetPurchaseOrdersResponse,
        500: GetPurchaseOrdersResponse,
        503: GetPurchaseOrdersResponse,
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
            self._get_purchase_orders_status_responses,
        )
        return response

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
        200: GetPurchaseOrdersStatusResponse,
        400: GetPurchaseOrdersStatusResponse,
        403: GetPurchaseOrdersStatusResponse,
        404: GetPurchaseOrdersStatusResponse,
        415: GetPurchaseOrdersStatusResponse,
        429: GetPurchaseOrdersStatusResponse,
        500: GetPurchaseOrdersStatusResponse,
        503: GetPurchaseOrdersStatusResponse,
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
            self._submit_acknowledgement_responses,
        )
        return response

    _submit_acknowledgement_params = (("acknowledgements", "body"),)  # name, param in

    _submit_acknowledgement_responses = {
        202: SubmitAcknowledgementResponse,
        400: SubmitAcknowledgementResponse,
        403: SubmitAcknowledgementResponse,
        404: SubmitAcknowledgementResponse,
        413: SubmitAcknowledgementResponse,
        415: SubmitAcknowledgementResponse,
        429: SubmitAcknowledgementResponse,
        500: SubmitAcknowledgementResponse,
        503: SubmitAcknowledgementResponse,
    }
