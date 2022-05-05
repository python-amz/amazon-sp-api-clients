"""
Selling Partner API for Direct Fulfillment Shipping
=============================================================================================

The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
API Version: 2021-12-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    pass


@attrs.define
class Container:

    carrier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    container_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    container_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'integer'}
    container_type: Union[Literal["Carton"], Literal["Pallet"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'enum': ['Carton', 'Pallet'], 'type': 'string'}
    manifest_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    manifest_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    packed_items: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/PackedItem'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}
    scac_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/Dimensions', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class CustomerInvoice:

    content: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'pattern': '^[a-zA-Z0-9]+$', 'type': 'string'}

    pass


@attrs.define
class CustomerInvoiceList:

    customer_invoices: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/CustomerInvoice'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}

    pagination: dict[str, Any]
    # {'ref': '#/components/schemas/Pagination', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Dimensions:

    unit_of_measure: Union[Literal["IN"], Literal["CM"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'enum': ['IN', 'CM'], 'type': 'string'}

    height: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    length: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    width: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Error'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}

    pass


@attrs.define
class GetCustomerInvoiceResponse:

    errors: dict[str, Any]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/CustomerInvoice', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class GetCustomerInvoicesResponse:

    errors: dict[str, Any]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/CustomerInvoiceList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class GetShippingLabelListResponse:

    errors: dict[str, Any]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingLabelList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class GetShippingLabelResponse:

    errors: dict[str, Any]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingLabel', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class Item:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    item_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'integer'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    shipped_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'integer'}
    unit_of_measure: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    pass


@attrs.define
class LabelData:

    content: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    package_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    ship_method_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    pass


@attrs.define
class PackedItem:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    item_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'integer'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    packed_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class Pagination:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    tax_registration_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxRegistrationDetails'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}

    address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class ShippingLabel:

    label_data: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/LabelData'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}
    label_format: Union[Literal["PNG"], Literal["ZPL"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'enum': ['PNG', 'ZPL'], 'type': 'string'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'pattern': '^[a-zA-Z0-9]+$', 'type': 'string'}

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class ShippingLabelList:

    shipping_labels: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ShippingLabel'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}

    pagination: dict[str, Any]
    # {'ref': '#/components/schemas/Pagination', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class ShippingLabelRequest:

    containers: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Container'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'pattern': '^[a-zA-Z0-9]+$', 'type': 'string'}

    selling_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class SubmitShippingLabelsRequest:

    shipping_label_requests: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ShippingLabelRequest'), 'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'array'}

    pass


@attrs.define
class SubmitShippingLabelsResponse:

    errors: dict[str, Any]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TransactionReference', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'enum': ['VAT', 'GST'], 'type': 'string'}

    tax_registration_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'type': 'string'}

    pass


@attrs.define
class Weight:

    unit_of_measure: Union[Literal["KG"], Literal["LB"]]
    # {'generator': <__mp_main__.Generator object at 0x0000019021F13550>, 'enum': ['KG', 'LB'], 'type': 'string'}

    value: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000019021F13550>}
    pass


class VendorDirectFulfillmentShipping20211228Client(BaseClient):
    def get_shipping_label(
        self,
        purchase_order_number: str,
    ):
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            purchase_order_number: The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.
        """
        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipping_label_params)
        return response

    _get_shipping_label_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_shipping_labels(
        self,
        created_after: str,
        created_before: str,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ):
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned.
            created_after: Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_shipping_labels_params)
        return response

    _get_shipping_labels_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    def submit_shipping_label_request(
        self,
    ):
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        """
        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipping_label_request_params)
        return response

    _submit_shipping_label_request_params = ()  # name, param in
