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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    address_line2: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    address_line3: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    city: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    country_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    county: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    district: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    phone: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    postal_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    state_or_region: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    pass


@attrs.define
class Container:

    carrier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    container_identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    container_sequence_number: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    container_type: Union[Literal["Carton"], Literal["Pallet"]]
    # {'type': 'string', 'enum': ['Carton', 'Pallet'], 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    manifest_date: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    manifest_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    packed_items: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/PackedItem')}
    scac_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    ship_method: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    tracking_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    dimensions: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Dimensions'}
    weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Weight'}
    pass


@attrs.define
class CustomerInvoice:

    content: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    purchase_order_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'pattern': '^[a-zA-Z0-9]+$'}

    pass


@attrs.define
class CustomerInvoiceList:

    customer_invoices: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/CustomerInvoice')}

    pagination: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Pagination'}
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Dimensions:

    unit_of_measure: Union[Literal["IN"], Literal["CM"]]
    # {'type': 'string', 'enum': ['IN', 'CM'], 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    height: str
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Decimal'}
    length: str
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Decimal'}
    width: str
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/Error')}

    pass


@attrs.define
class GetCustomerInvoiceResponse:

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/CustomerInvoice'}
    pass


@attrs.define
class GetCustomerInvoicesResponse:

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/CustomerInvoiceList'}
    pass


@attrs.define
class GetShippingLabelListResponse:

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ShippingLabelList'}
    pass


@attrs.define
class GetShippingLabelResponse:

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ShippingLabel'}
    pass


@attrs.define
class Item:

    buyer_product_identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    item_sequence_number: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    vendor_product_identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    shipped_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ItemQuantity'}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    unit_of_measure: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    pass


@attrs.define
class LabelData:

    content: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    package_identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    ship_method: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    ship_method_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    tracking_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    pass


@attrs.define
class PackedItem:

    buyer_product_identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    item_sequence_number: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    vendor_product_identifier: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    packed_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ItemQuantity'}
    pass


@attrs.define
class Pagination:

    next_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    tax_registration_details: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/TaxRegistrationDetails')}

    address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class ShippingLabel:

    label_data: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/LabelData')}
    label_format: Union[Literal["PNG"], Literal["ZPL"]]
    # {'type': 'string', 'enum': ['PNG', 'ZPL'], 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    purchase_order_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'pattern': '^[a-zA-Z0-9]+$'}

    selling_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/PartyIdentification'}
    pass


@attrs.define
class ShippingLabelList:

    shipping_labels: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/ShippingLabel')}

    pagination: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Pagination'}
    pass


@attrs.define
class ShippingLabelRequest:

    containers: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/Container')}
    purchase_order_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'pattern': '^[a-zA-Z0-9]+$'}

    selling_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/PartyIdentification'}
    pass


@attrs.define
class SubmitShippingLabelsRequest:

    shipping_label_requests: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'items': Reference(ref='#/components/schemas/ShippingLabelRequest')}

    pass


@attrs.define
class SubmitShippingLabelsResponse:

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/TransactionReference'}
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_messages: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    tax_registration_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'type': 'string', 'enum': ['VAT', 'GST'], 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    tax_registration_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    pass


@attrs.define
class Weight:

    unit_of_measure: Union[Literal["KG"], Literal["LB"]]
    # {'type': 'string', 'enum': ['KG', 'LB'], 'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>}

    value: str
    # {'generator': <__mp_main__.Generator object at 0x0000024D5CC7B700>, 'ref': '#/components/schemas/Decimal'}
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
