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


@attrs.define
class AcknowledgementStatus:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    attention: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetOrderResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Order', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class GetOrdersResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrderList', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class GiftDetails:

    gift_message: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    gift_wrap_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'integer'}
    unit_of_measure: Union[Literal["Each"]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'enum': ['Each'], 'type': 'string'}

    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    amount: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class Order:

    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    order_details: dict[str, Any]
    # {'ref': '#/components/schemas/OrderDetails', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class OrderAcknowledgementItem:

    acknowledgement_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'schema_format': 'date-time', 'type': 'string'}
    item_acknowledgements: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'items': Reference(ref='#/components/schemas/OrderItemAcknowledgement'), 'type': 'array'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    vendor_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    acknowledgement_status: dict[str, Any]
    # {'ref': '#/components/schemas/AcknowledgementStatus', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class OrderDetails:

    customer_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'items': Reference(ref='#/components/schemas/OrderItem'), 'type': 'array'}
    order_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'schema_format': 'date-time', 'type': 'string'}
    order_status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'enum': ['NEW', 'SHIPPED', 'ACCEPTED', 'CANCELLED'], 'type': 'string'}
    tax_total: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'properties': {'taxLineItem': Reference(ref='#/components/schemas/TaxLineItem')}, 'type': 'object'}

    bill_to_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    ship_to_party: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    shipment_details: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentDetails', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class OrderItem:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    item_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    tax_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'properties': {'taxLineItem': Reference(ref='#/components/schemas/TaxLineItem')}, 'type': 'object'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    gift_details: dict[str, Any]
    # {'ref': '#/components/schemas/GiftDetails', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    net_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    ordered_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    scheduled_delivery_shipment: dict[str, Any]
    # {'ref': '#/components/schemas/ScheduledDeliveryShipment', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    total_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class OrderItemAcknowledgement:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    item_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    acknowledged_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class OrderList:

    orders: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'items': Reference(ref='#/components/schemas/Order'), 'type': 'array'}

    pagination: dict[str, Any]
    # {'ref': '#/components/schemas/Pagination', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class Pagination:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    tax_info: dict[str, Any]
    # {'ref': '#/components/schemas/TaxRegistrationDetails', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class ScheduledDeliveryShipment:

    earliest_nominated_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'schema_format': 'date-time', 'type': 'string'}
    latest_nominated_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'schema_format': 'date-time', 'type': 'string'}
    scheduled_delivery_service_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


@attrs.define
class ShipmentDates:

    promised_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'schema_format': 'date-time', 'type': 'string'}
    required_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'schema_format': 'date-time', 'type': 'string'}

    pass


@attrs.define
class ShipmentDetails:

    is_gift: bool
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'boolean'}
    is_priority_shipment: bool
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'boolean'}
    is_pslip_required: bool
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'boolean'}
    is_scheduled_delivery_shipment: bool
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'boolean'}
    message_to_customer: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    shipment_dates: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentDates', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class SubmitAcknowledgementRequest:

    order_acknowledgements: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'items': Reference(ref='#/components/schemas/OrderAcknowledgementItem'), 'type': 'array'}

    pass


@attrs.define
class SubmitAcknowledgementResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TransactionId', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class TaxDetails:

    type: Union[
        Literal["CONSUMPTION"],
        Literal["GST"],
        Literal["MwSt."],
        Literal["PST"],
        Literal["TOTAL"],
        Literal["TVA"],
        Literal["VAT"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'enum': ['CONSUMPTION', 'GST', 'MwSt.', 'PST', 'TOTAL', 'TVA', 'VAT'], 'type': 'string'}

    tax_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    tax_rate: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    taxable_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class TaxLineItem:

    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'enum': ['VAT', 'GST'], 'type': 'string'}

    tax_registration_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>}
    pass


@attrs.define
class TransactionId:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000021B3C750AF0>, 'type': 'string'}

    pass


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
        created_after: str,
        created_before: str,
        ship_from_party_id: str = None,
        status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]] = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
        include_details: str = None,
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
        """
        url = "/vendor/directFulfillment/orders/v1/acknowledgements"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_acknowledgement_params)
        return response

    _submit_acknowledgement_params = ()  # name, param in
