"""
Selling Partner API for Direct Fulfillment Orders
=============================================================================================

The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class AcknowledgementStatus:
    """
    Status of acknowledgement.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    Acknowledgement code is a unique two digit value which indicates the status of the acknowledgement. For a list of acknowledgement codes that Amazon supports, see the Vendor Direct Fulfillment APIs Use Case Guide.
    """

    description: str = attrs.field(
        kw_only=True,
    )
    """
    Reason for the acknowledgement code.
    """


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

    attention: str = attrs.field(
        kw_only=True,
    )
    """
    The attention name of the person at that address.
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


@attrs.define
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
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


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class GetOrderResponse:
    """
    The response schema for the getOrder operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Order" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetOrdersResponse:
    """
    The response schema for the getOrders operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "OrderList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GiftDetails:
    """
    Gift details for the item.
    """

    gift_message: str = attrs.field(
        kw_only=True,
    )
    """
    Gift message to be printed in shipment.
    """

    gift_wrap_id: str = attrs.field(
        kw_only=True,
    )
    """
    Gift wrap identifier for the gift wrapping, if any.
    """


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

    unit_of_measure: Union[Literal["Each"]] = attrs.field(
        kw_only=True,
    )
    """
    Unit of measure for the acknowledged quantity.
    """


@attrs.define
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: "Decimal" = attrs.field(
        kw_only=True,
    )

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three digit currency code in ISO 4217 format. String of length 3.
    """


@attrs.define
class Order:

    order_details: "OrderDetails" = attrs.field(
        kw_only=True,
    )

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The purchase order number for this order. Formatting Notes: alpha-numeric code.
    """


@attrs.define
class OrderAcknowledgementItem:
    """
    Details of an individual order being acknowledged.
    """

    acknowledgement_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time when the order is acknowledged, in ISO-8601 date/time format. For example: 2018-07-16T23:00:00Z / 2018-07-16T23:00:00-05:00 / 2018-07-16T23:00:00-08:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    acknowledgement_status: "AcknowledgementStatus" = attrs.field(
        kw_only=True,
    )

    item_acknowledgements: List["OrderItemAcknowledgement"] = attrs.field(
        kw_only=True,
    )
    """
    Item details including acknowledged quantity.
    """

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The purchase order number for this order. Formatting Notes: alpha-numeric code.
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    vendor_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor's order number for this order.
    """


@attrs.define
class OrderDetails:
    """
    Details of an order.
    """

    bill_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    customer_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The customer order number.
    """

    items: List["OrderItem"] = attrs.field(
        kw_only=True,
    )
    """
    A list of items in this purchase order.
    """

    order_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date the order was placed. This field is expected to be in ISO-8601 date/time format, for example:2018-07-16T23:00:00Z/ 2018-07-16T23:00:00-05:00 /2018-07-16T23:00:00-08:00. If no time zone is specified, UTC should be assumed.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    order_status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]] = attrs.field(
        kw_only=True,
    )
    """
    Current status of the order.
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_to_party: "Address" = attrs.field(
        kw_only=True,
    )

    shipment_details: "ShipmentDetails" = attrs.field(
        kw_only=True,
    )

    tax_total: "OrderDetailsTaxTotal" = attrs.field(
        kw_only=True,
    )


@attrs.define
class OrderDetailsTaxTotal:

    tax_line_item: "TaxLineItem" = attrs.field(
        kw_only=True,
    )


@attrs.define
class OrderItem:

    buyer_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    gift_details: "GiftDetails" = attrs.field(
        kw_only=True,
    )

    item_sequence_number: str = attrs.field(
        kw_only=True,
    )
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    net_price: "Money" = attrs.field(
        kw_only=True,
    )

    ordered_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )

    scheduled_delivery_shipment: "ScheduledDeliveryShipment" = attrs.field(
        kw_only=True,
    )

    tax_details: "OrderItemTaxDetails" = attrs.field(
        kw_only=True,
    )

    title: str = attrs.field(
        kw_only=True,
    )
    """
    Title for the item.
    """

    total_price: "Money" = attrs.field(
        kw_only=True,
    )

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item.
    """


@attrs.define
class OrderItemAcknowledgement:

    acknowledged_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )

    buyer_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Buyer's standard identification number (ASIN) of an item.
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
    The vendor selected product identification of the item. Should be the same as was provided in the purchase order.
    """


@attrs.define
class OrderItemTaxDetails:
    """
    Total tax details for the line item.
    """

    tax_line_item: "TaxLineItem" = attrs.field(
        kw_only=True,
    )


@attrs.define
class OrderList:

    orders: List["Order"] = attrs.field(
        kw_only=True,
    )

    pagination: "Pagination" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Pagination:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """


@attrs.define
class PartyIdentification:

    address: "Address" = attrs.field(
        kw_only=True,
    )

    party_id: str = attrs.field(
        kw_only=True,
    )
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    tax_info: "TaxRegistrationDetails" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ScheduledDeliveryShipment:
    """
    Dates for the scheduled delivery shipments.
    """

    earliest_nominated_delivery_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Earliest nominated delivery date for the scheduled delivery.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    latest_nominated_delivery_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Latest nominated delivery date for the scheduled delivery.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    scheduled_delivery_service_type: str = attrs.field(
        kw_only=True,
    )
    """
    Scheduled delivery service type.
    """


@attrs.define
class ShipmentDates:
    """
    Shipment dates.
    """

    promised_delivery_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Delivery date promised to the Amazon customer.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    required_ship_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Time by which the vendor is required to ship the order.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define
class ShipmentDetails:
    """
    Shipment details required for the shipment.
    """

    is_gift: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the order contain a gift. Include the gift message and gift wrap information.
    """

    is_priority_shipment: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, this is a priority shipment.
    """

    is_pslip_required: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, a packing slip is required to be sent to the customer.
    """

    is_scheduled_delivery_shipment: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, this order is part of a scheduled delivery program.
    """

    message_to_customer: str = attrs.field(
        kw_only=True,
    )
    """
    Message to customer for order status.
    """

    ship_method: str = attrs.field(
        kw_only=True,
    )
    """
    Ship method to be used for shipping the order. Amazon defines ship method codes indicating the shipping carrier and shipment service level. To see the full list of ship methods in use, including both the code and the friendly name, search the 'Help' section on Vendor Central for 'ship methods'.
    """

    shipment_dates: "ShipmentDates" = attrs.field(
        kw_only=True,
    )


@attrs.define
class SubmitAcknowledgementRequest:
    """
    The request schema for the submitAcknowledgement operation.
    """

    order_acknowledgements: List["OrderAcknowledgementItem"] = attrs.field(
        kw_only=True,
    )
    """
    A list of one or more purchase orders.
    """


@attrs.define
class SubmitAcknowledgementResponse:
    """
    The response schema for the submitAcknowledgement operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "TransactionId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TaxDetails:

    tax_amount: "Money" = attrs.field(
        kw_only=True,
    )

    tax_rate: "Decimal" = attrs.field(
        kw_only=True,
    )

    taxable_amount: "Money" = attrs.field(
        kw_only=True,
    )

    type: Union[
        Literal["CONSUMPTION"],
        Literal["GST"],
        Literal["MwSt."],
        Literal["PST"],
        Literal["TOTAL"],
        Literal["TVA"],
        Literal["VAT"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    Tax type.
    """


@attrs.define
class TaxLineItem:
    """
    A list of tax line items.
    """

    pass


@attrs.define
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_address: "Address" = attrs.field(
        kw_only=True,
    )

    tax_registration_messages: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration type for the entity.
    """


@attrs.define
class TransactionId:

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorDirectFulfillmentOrdersV1Client(BaseClient):
    def get_order(
        self,
        purchase_order_number: str,
    ):
        """
        Returns purchase order information for the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.
        """
        url = "/vendor/directFulfillment/orders/v1/purchaseOrders/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_params)
        return response

    _get_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_orders(
        self,
        created_after: datetime,
        created_before: datetime,
        ship_from_party_id: str = None,
        status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]] = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
        include_details: bool = None,
    ):
        """
        Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses.
            status: Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status.
            limit: The limit to the number of purchase orders returned.
            created_after: Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort the list in ascending or descending order by order creation date.
            next_token: Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
            include_details: When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned.
        """
        url = "/vendor/directFulfillment/orders/v1/purchaseOrders"
        values = (
            ship_from_party_id,
            status,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
            include_details,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_orders_params)
        return response

    _get_orders_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("status", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
        ("includeDetails", "query"),
    )

    def submit_acknowledgement(
        self,
        order_acknowledgements: List["OrderAcknowledgementItem"] = None,
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
            order_acknowledgements: A list of one or more purchase orders.
        """
        url = "/vendor/directFulfillment/orders/v1/acknowledgements"
        values = (order_acknowledgements,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_acknowledgement_params)
        return response

    _submit_acknowledgement_params = (("orderAcknowledgements", "body"),)  # name, param in
