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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AcknowledgementStatus:
    """
    Status of acknowledgement.
    """

    code: Optional[str] = attrs.field()
    """
    Acknowledgement code is a unique two digit value which indicates the status of the acknowledgement. For a list of acknowledgement codes that Amazon supports, see the Vendor Direct Fulfillment APIs Use Case Guide.
    """

    description: Optional[str] = attrs.field()
    """
    Reason for the acknowledgement code.
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

    attention: Optional[str] = attrs.field()
    """
    The attention name of the person at that address.
    """

    city: Optional[str] = attrs.field()
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
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

    state_or_region: str = attrs.field()
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
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
class GetOrderResponse:
    """
    The response schema for the getOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Order"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrdersResponse:
    """
    The response schema for the getOrders operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["OrderList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GiftDetails:
    """
    Gift details for the item.
    """

    gift_message: Optional[str] = attrs.field()
    """
    Gift message to be printed in shipment.
    """

    gift_wrap_id: Optional[str] = attrs.field()
    """
    Gift wrap identifier for the gift wrapping, if any.
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

    unit_of_measure: Optional[Union[Literal["Each"]]] = attrs.field()
    """
    Unit of measure for the acknowledged quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: Optional["Decimal"] = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """

    currency_code: Optional[str] = attrs.field()
    """
    Three digit currency code in ISO 4217 format. String of length 3.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Order:

    order_details: Optional["OrderDetails"] = attrs.field()
    """
    Details of an order.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order. Formatting Notes: alpha-numeric code.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderAcknowledgementItem:
    """
    Details of an individual order being acknowledged.
    """

    acknowledgement_date: datetime = attrs.field()
    """
    The date and time when the order is acknowledged, in ISO-8601 date/time format. For example: 2018-07-16T23:00:00Z / 2018-07-16T23:00:00-05:00 / 2018-07-16T23:00:00-08:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    acknowledgement_status: "AcknowledgementStatus" = attrs.field()
    """
    Status of acknowledgement.
    """

    item_acknowledgements: List["OrderItemAcknowledgement"] = attrs.field()
    """
    Item details including acknowledged quantity.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order. Formatting Notes: alpha-numeric code.
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    vendor_order_number: str = attrs.field()
    """
    The vendor's order number for this order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderDetails:
    """
    Details of an order.
    """

    bill_to_party: "PartyIdentification" = attrs.field()

    customer_order_number: str = attrs.field()
    """
    The customer order number.
    """

    items: List["OrderItem"] = attrs.field()
    """
    A list of items in this purchase order.
    """

    order_date: datetime = attrs.field()
    """
    The date the order was placed. This field is expected to be in ISO-8601 date/time format, for example:2018-07-16T23:00:00Z/ 2018-07-16T23:00:00-05:00 /2018-07-16T23:00:00-08:00. If no time zone is specified, UTC should be assumed.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    order_status: Optional[
        Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]]
    ] = attrs.field()
    """
    Current status of the order.
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    ship_to_party: "Address" = attrs.field()
    """
    Address of the party.
    """

    shipment_details: "ShipmentDetails" = attrs.field()
    """
    Shipment details required for the shipment.
    """

    tax_total: Optional["OrderDetailsTaxTotal"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderDetailsTaxTotal:

    tax_line_item: Optional[List["TaxDetails"]] = attrs.field()
    """
    A list of tax line items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItem:

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    gift_details: Optional["GiftDetails"] = attrs.field()
    """
    Gift details for the item.
    """

    item_sequence_number: str = attrs.field()
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    net_price: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    ordered_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity ordered.
    """

    scheduled_delivery_shipment: Optional["ScheduledDeliveryShipment"] = attrs.field()
    """
    Dates for the scheduled delivery shipments.
    """

    tax_details: Optional["OrderItemTaxDetails"] = attrs.field()
    """
    Total tax details for the line item.
    """

    title: Optional[str] = attrs.field()
    """
    Title for the item.
    """

    total_price: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
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

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    item_sequence_number: str = attrs.field()
    """
    Line item sequence number for the item.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item. Should be the same as was provided in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemTaxDetails:
    """
    Total tax details for the line item.
    """

    tax_line_item: Optional[List["TaxDetails"]] = attrs.field()
    """
    A list of tax line items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderList:

    orders: Optional[List["Order"]] = attrs.field()

    pagination: Optional["Pagination"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:

    next_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
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
class ScheduledDeliveryShipment:
    """
    Dates for the scheduled delivery shipments.
    """

    earliest_nominated_delivery_date: Optional[datetime] = attrs.field()
    """
    Earliest nominated delivery date for the scheduled delivery.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    latest_nominated_delivery_date: Optional[datetime] = attrs.field()
    """
    Latest nominated delivery date for the scheduled delivery.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    scheduled_delivery_service_type: Optional[str] = attrs.field()
    """
    Scheduled delivery service type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDates:
    """
    Shipment dates.
    """

    promised_delivery_date: Optional[datetime] = attrs.field()
    """
    Delivery date promised to the Amazon customer.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    required_ship_date: datetime = attrs.field()
    """
    Time by which the vendor is required to ship the order.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDetails:
    """
    Shipment details required for the shipment.
    """

    is_gift: Optional[bool] = attrs.field()
    """
    When true, the order contain a gift. Include the gift message and gift wrap information.
    """

    is_priority_shipment: bool = attrs.field()
    """
    When true, this is a priority shipment.
    """

    is_pslip_required: bool = attrs.field()
    """
    When true, a packing slip is required to be sent to the customer.
    """

    is_scheduled_delivery_shipment: Optional[bool] = attrs.field()
    """
    When true, this order is part of a scheduled delivery program.
    """

    message_to_customer: str = attrs.field()
    """
    Message to customer for order status.
    """

    ship_method: str = attrs.field()
    """
    Ship method to be used for shipping the order. Amazon defines ship method codes indicating the shipping carrier and shipment service level. To see the full list of ship methods in use, including both the code and the friendly name, search the 'Help' section on Vendor Central for 'ship methods'.
    """

    shipment_dates: "ShipmentDates" = attrs.field()
    """
    Shipment dates.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementRequest:
    """
    The request schema for the submitAcknowledgement operation.
    """

    order_acknowledgements: Optional[List["OrderAcknowledgementItem"]] = attrs.field()
    """
    A list of one or more purchase orders.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitAcknowledgementResponse:
    """
    The response schema for the submitAcknowledgement operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxDetails:

    tax_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    tax_rate: Optional["Decimal"] = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """

    taxable_amount: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    type: Optional[
        Union[
            Literal["CONSUMPTION"],
            Literal["GST"],
            Literal["MwSt."],
            Literal["PST"],
            Literal["TOTAL"],
            Literal["TVA"],
            Literal["VAT"],
        ]
    ] = attrs.field()
    """
    Tax type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_address: Optional["Address"] = attrs.field()
    """
    Address of the party.
    """

    tax_registration_messages: Optional[str] = attrs.field()
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field()
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Optional[Union[Literal["VAT"], Literal["GST"]]] = attrs.field()
    """
    Tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionId:

    transaction_id: Optional[str] = attrs.field()
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_order_responses = {
        (200, "application/json"): GetOrderResponse,
        (400, "application/json"): GetOrderResponse,
        (401, "application/json"): GetOrderResponse,
        (403, "application/json"): GetOrderResponse,
        (404, "application/json"): GetOrderResponse,
        (415, "application/json"): GetOrderResponse,
        (429, "application/json"): GetOrderResponse,
        (500, "application/json"): GetOrderResponse,
        (503, "application/json"): GetOrderResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_orders_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

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

    _get_orders_responses = {
        (200, "application/json"): GetOrdersResponse,
        (400, "application/json"): GetOrdersResponse,
        (403, "application/json"): GetOrdersResponse,
        (404, "application/json"): GetOrdersResponse,
        (415, "application/json"): GetOrdersResponse,
        (429, "application/json"): GetOrdersResponse,
        (500, "application/json"): GetOrdersResponse,
        (503, "application/json"): GetOrdersResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_acknowledgement_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _submit_acknowledgement_params = (("orderAcknowledgements", "body"),)  # name, param in

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
