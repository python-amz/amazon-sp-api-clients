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
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class AcknowledgementStatusDetails:

    """
    Details of item quantity ordered
    """

    acknowledgement_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date when the line item was confirmed by vendor. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    accepted_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rejected_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Address:

    """
    Address of the party.
    """

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    First line of the address.
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.
    """

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.

    Extra fields:
    {'maxLength': 2}
    """

    county: str = attrs.field(
        kw_only=True,
    )
    """
    The county where person, business or institution is located.
    """

    district: str = attrs.field(
        kw_only=True,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person, business or institution at that address.
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: str = attrs.field(
        kw_only=True,
    )
    """
    The state or region where person, business or institution is located.
    """

    pass


@attrs.define
class DateTimeInterval:

    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """

    pass


@attrs.define
class Decimal:

    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    pass


@attrs.define
class Error:

    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """

    pass


@attrs.define
class ErrorList:

    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class GetPurchaseOrderResponse:

    """
    The response schema for the getPurchaseOrder operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Order" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPurchaseOrdersResponse:

    """
    The response schema for the getPurchaseOrders operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "OrderList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPurchaseOrdersStatusResponse:

    """
    The response schema for the getPurchaseOrdersStatus operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "OrderListStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ImportDetails:

    """
    Import details for an import order.
    """

    import_containers: str = attrs.field(
        kw_only=True,
    )
    """
    Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if the shipment has multiple containers. HC signifies a high-capacity container. Free-text field, limited to 64 characters. The format will be a comma-delimited list containing values of the type: $NUMBER_OF_CONTAINERS_OF_THIS_TYPE-$CONTAINER_TYPE. The list of values for the container type is: 40'(40-foot container), 40'HC (40-foot high-capacity container), 45', 45'HC, 30', 30'HC, 20', 20'HC.

    Extra fields:
    {'maxLength': 64}
    """

    international_commercial_terms: Union[
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
    ] = attrs.field(
        kw_only=True,
    )
    """
    Incoterms (International Commercial Terms) are used to divide transaction costs and responsibilities between buyer and seller and reflect state-of-the-art transportation practices. This is for import purchase orders only.
    """

    method_of_payment: Union[
        Literal["PaidByBuyer"],
        Literal["CollectOnDelivery"],
        Literal["DefinedByBuyerAndSeller"],
        Literal["FOBPortOfCall"],
        Literal["PrepaidBySeller"],
        Literal["PaidBySeller"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    If the recipient requests, contains the shipment method of payment. This is for import PO's only.
    """

    port_of_delivery: str = attrs.field(
        kw_only=True,
    )
    """
    The port where goods on an import purchase order must be delivered by the vendor. This should only be specified when the internationalCommercialTerms is FOB.

    Extra fields:
    {'maxLength': 64}
    """

    shipping_instructions: str = attrs.field(
        kw_only=True,
    )
    """
    Special instructions regarding the shipment. This field is for import purchase orders.
    """

    pass


@attrs.define
class ItemQuantity:

    """
    Details of quantity ordered.
    """

    amount: int = attrs.field(
        kw_only=True,
    )
    """
    Acknowledged quantity. This value should not be zero.
    """

    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field(
        kw_only=True,
    )
    """
    Unit of measure for the acknowledged quantity.
    """

    unit_size: int = attrs.field(
        kw_only=True,
    )
    """
    The case size, in the event that we ordered using cases.
    """

    pass


@attrs.define
class ItemStatus:

    """
    Detailed description of items order status.
    """

    pass


@attrs.define
class Money:

    """
    An amount of money, including units in the form of currency.
    """

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three digit currency code in ISO 4217 format. String of length 3.

    Extra fields:
    {'maxLength': 3}
    """

    amount: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Order:

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    purchase_order_state: Union[Literal["New"], Literal["Acknowledged"], Literal["Closed"]] = attrs.field(
        kw_only=True,
    )
    """
    This field will contain the current state of the purchase order.
    """

    order_details: "OrderDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderAcknowledgement:

    acknowledgement_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time when the purchase order is acknowledged, in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    items: List["OrderAcknowledgementItem"] = attrs.field(
        kw_only=True,
    )
    """
    A list of the items being acknowledged with associated details.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The purchase order number. Formatting Notes: 8-character alpha-numeric code.
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderAcknowledgementItem:

    """
    Details of the item being acknowledged.
    """

    amazon_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    discount_multiplier: str = attrs.field(
        kw_only=True,
    )
    """
    The discount multiplier that should be applied to the price if a vendor sells books with a list price. This is a multiplier factor to arrive at a final discounted price. A multiplier of .90 would be the factor if a 10% discount is given.
    """

    item_acknowledgements: List["OrderItemAcknowledgement"] = attrs.field(
        kw_only=True,
    )
    """
    This is used to indicate acknowledged quantity.
    """

    item_sequence_number: str = attrs.field(
        kw_only=True,
    )
    """
    Line item sequence number for the item.
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the purchase order.
    """

    list_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    net_cost: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ordered_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderDetails:

    """
    Details of an order.
    """

    deal_code: str = attrs.field(
        kw_only=True,
    )
    """
    If requested by the recipient, this field will contain a promotional/deal number. The discount code line is optional. It is used to obtain a price discount on items on the order.
    """

    items: List["OrderItem"] = attrs.field(
        kw_only=True,
    )
    """
    A list of items in this purchase order.
    """

    payment_method: Union[
        Literal["Invoice"], Literal["Consignment"], Literal["CreditCard"], Literal["Prepaid"]
    ] = attrs.field(
        kw_only=True,
    )
    """
    Payment method used.
    """

    purchase_order_changed_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date when purchase order was last changed by Amazon after the order was placed. This date will be greater than 'purchaseOrderDate'. This means the PO data was changed on that date and vendors are required to fulfill the  updated PO. The PO changes can be related to Item Quantity, Ship to Location, Ship Window etc. This field will not be present in orders that have not changed after creation. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date the purchase order was placed. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_state_changed_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date when current purchase order state was changed. Current purchase order state is available in the field 'purchaseOrderState'. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_type: Union[
        Literal["RegularOrder"], Literal["ConsignedOrder"], Literal["NewProductIntroduction"], Literal["RushOrder"]
    ] = attrs.field(
        kw_only=True,
    )
    """
    Type of purchase order.
    """

    bill_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    buying_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    delivery_window: "DateTimeInterval" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    import_details: "ImportDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_window: "DateTimeInterval" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderItem:

    amazon_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    is_back_order_allowed: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, we will accept backorder confirmations for this item.
    """

    item_sequence_number: str = attrs.field(
        kw_only=True,
    )
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item.
    """

    list_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    net_cost: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ordered_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderItemAcknowledgement:

    acknowledgement_code: Union[Literal["Accepted"], Literal["Backordered"], Literal["Rejected"]] = attrs.field(
        kw_only=True,
    )
    """
    This indicates the acknowledgement code.
    """

    rejection_reason: Union[
        Literal["TemporarilyUnavailable"], Literal["InvalidProductIdentifier"], Literal["ObsoleteProduct"]
    ] = attrs.field(
        kw_only=True,
    )
    """
    Indicates the reason for rejection.
    """

    scheduled_delivery_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Estimated delivery date per line item. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    scheduled_ship_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Estimated ship date per line item. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    acknowledged_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderItemStatus:

    acknowledgement_status: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    Acknowledgement status information.

    Extra fields:
    {'properties': {'confirmationStatus': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=['ACCEPTED', 'PARTIALLY_ACCEPTED', 'REJECTED', 'UNCONFIRMED'], type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Confirmation status of line item.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'acceptedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'rejectedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'acknowledgementStatusDetails': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/AcknowledgementStatusDetails'), properties=None, additionalProperties=None, description='Details of item quantity confirmed.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    """

    buyer_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Buyer's Standard Identification Number (ASIN) of an item.
    """

    item_sequence_number: str = attrs.field(
        kw_only=True,
    )
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    ordered_quantity: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    Ordered quantity information.

    Extra fields:
    {'properties': {'orderedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'orderedQuantityDetails': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/OrderedQuantityDetails'), properties=None, additionalProperties=None, description='Details of item quantity ordered.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    """

    receiving_status: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    Item receive status at the buyer's warehouse.

    Extra fields:
    {'properties': {'receiveStatus': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=['NOT_RECEIVED', 'PARTIALLY_RECEIVED', 'RECEIVED'], type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Receive status of the line item.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'receivedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'lastReceiveDate': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description="The date when the most recent item was received at the buyer's warehouse. Must be in ISO-8601 date/time format.", schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item.
    """

    list_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    net_cost: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderList:

    orders: List["Order"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderListStatus:

    orders_status: List["OrderStatus"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderStatus:

    """
    Current status of a purchase order.
    """

    last_updated_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date when the purchase order was last updated. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date the purchase order was placed. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The buyer's purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    purchase_order_status: Union[Literal["OPEN"], Literal["CLOSED"]] = attrs.field(
        kw_only=True,
    )
    """
    The status of the buyer's purchase order for this order.
    """

    item_status: "ItemStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderedQuantityDetails:

    """
    Details of item quantity ordered
    """

    updated_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date when the line item quantity was updated by buyer. Must be in ISO-8601 date/time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    cancelled_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ordered_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Pagination:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more purchase order items to return.
    """

    pass


@attrs.define
class PartyIdentification:

    party_id: str = attrs.field(
        kw_only=True,
    )
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_info: "TaxRegistrationDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitAcknowledgementRequest:

    """
    The request schema for the submitAcknowledgment operation.
    """

    acknowledgements: List["OrderAcknowledgement"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitAcknowledgementResponse:

    """
    The response schema for the submitAcknowledgement operation
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "TransactionId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TaxRegistrationDetails:

    """
    Tax registration details of the entity.
    """

    tax_registration_number: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration type for the entity.
    """

    pass


@attrs.define
class TransactionId:

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """

    pass


class VendorOrdersV1Client(BaseClient):
    def get_purchase_order(
        self,
        purchase_order_number: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_purchase_order_params)
        return response

    _get_purchase_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

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
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_purchase_orders_params)
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
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_purchase_orders_status_params)
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

    def submit_acknowledgement(
        self,
        acknowledgements: List["OrderAcknowledgement"] = None,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._submit_acknowledgement_params)
        return response

    _submit_acknowledgement_params = (("acknowledgements", "body"),)  # name, param in
