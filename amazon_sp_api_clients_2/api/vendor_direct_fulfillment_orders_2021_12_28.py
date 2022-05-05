"""
Selling Partner API for Direct Fulfillment Orders
=============================================================================================

The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.
API Version: 2021-12-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AcknowledgementStatus:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    description: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    attention: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'array', 'items': Reference(ref='#/components/schemas/Error')}

    pass


@attrs.define
class GiftDetails:

    gift_message: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    gift_wrap_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'integer'}
    unit_of_measure: Union[Literal["Each"]]
    # {'enum': ['Each'], 'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class Order:

    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    order_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/OrderDetails'}
    pass


@attrs.define
class OrderAcknowledgementItem:

    acknowledgement_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string', 'schema_format': 'date-time'}
    item_acknowledgements: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'array', 'items': Reference(ref='#/components/schemas/OrderItemAcknowledgement')}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    vendor_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    acknowledgement_status: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/AcknowledgementStatus'}
    selling_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/PartyIdentification'}
    pass


@attrs.define
class OrderDetails:

    customer_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'array', 'items': Reference(ref='#/components/schemas/OrderItem')}
    order_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string', 'schema_format': 'date-time'}
    order_status: Union[Literal["NEW"], Literal["SHIPPED"], Literal["ACCEPTED"], Literal["CANCELLED"]]
    # {'enum': ['NEW', 'SHIPPED', 'ACCEPTED', 'CANCELLED'], 'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    bill_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/PartyIdentification'}
    selling_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Address'}
    shipment_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/ShipmentDetails'}
    tax_total: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/TaxItemDetails'}
    pass


@attrs.define
class OrderItem:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    item_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    gift_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/GiftDetails'}
    net_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Money'}
    ordered_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/ItemQuantity'}
    scheduled_delivery_shipment: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/ScheduledDeliveryShipment'}
    tax_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/TaxItemDetails'}
    total_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class OrderItemAcknowledgement:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    item_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    acknowledged_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/ItemQuantity'}
    pass


@attrs.define
class OrderList:

    orders: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'array', 'items': Reference(ref='#/components/schemas/Order')}

    pagination: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Pagination'}
    pass


@attrs.define
class Pagination:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Address'}
    tax_info: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/TaxRegistrationDetails'}
    pass


@attrs.define
class ScheduledDeliveryShipment:

    earliest_nominated_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string', 'schema_format': 'date-time'}
    latest_nominated_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string', 'schema_format': 'date-time'}
    scheduled_delivery_service_type: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


@attrs.define
class ShipmentDates:

    promised_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string', 'schema_format': 'date-time'}
    required_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string', 'schema_format': 'date-time'}

    pass


@attrs.define
class ShipmentDetails:

    is_gift: bool
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'boolean'}
    is_priority_shipment: bool
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'boolean'}
    is_pslip_required: bool
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'boolean'}
    is_scheduled_delivery_shipment: bool
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'boolean'}
    message_to_customer: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    shipment_dates: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/ShipmentDates'}
    pass


@attrs.define
class SubmitAcknowledgementRequest:

    order_acknowledgements: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'array', 'items': Reference(ref='#/components/schemas/OrderAcknowledgementItem')}

    pass


@attrs.define
class SubmitAcknowledgementResponse:

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/TransactionId'}
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
    # {'enum': ['CONSUMPTION', 'GST', 'MwSt.', 'PST', 'TOTAL', 'TVA', 'VAT'], 'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Money'}
    tax_rate: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Decimal'}
    taxable_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class TaxItemDetails:

    tax_line_item: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/TaxLineItem'}
    pass


@attrs.define
class TaxLineItem:

    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'enum': ['VAT', 'GST'], 'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    tax_registration_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class TransactionId:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002544D19B880>, 'type': 'string'}

    pass


class VendorDirectFulfillmentOrders20211228Client(BaseClient):
    def get_order(
        self,
        purchase_order_number: str,
    ):
        """
        Returns purchase order information for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            purchase_order_number: The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.
        """
        url = "/vendor/directFulfillment/orders/2021-12-28/purchaseOrders/{purchaseOrderNumber}"
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

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

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
        url = "/vendor/directFulfillment/orders/2021-12-28/purchaseOrders"
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

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        """
        url = "/vendor/directFulfillment/orders/2021-12-28/acknowledgements"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_acknowledgement_params)
        return response

    _submit_acknowledgement_params = ()  # name, param in
