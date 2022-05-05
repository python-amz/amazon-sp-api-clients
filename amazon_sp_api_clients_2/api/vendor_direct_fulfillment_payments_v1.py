"""
Selling Partner API for Direct Fulfillment Payments
=============================================================================================

The Selling Partner API for Direct Fulfillment Payments provides programmatic access to a direct fulfillment vendor's invoice data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AdditionalDetails:

    detail: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    language_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    type: Union[Literal["SUR"], Literal["OCR"]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string', 'enum': ['SUR', 'OCR']}

    pass


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}

    pass


@attrs.define
class ChargeDetails:

    tax_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetail')}
    type: Union[
        Literal["GIFTWRAP"],
        Literal["FULFILLMENT"],
        Literal["MARKETINGINSERT"],
        Literal["PACKAGING"],
        Literal["LOADING"],
        Literal["FREIGHTOUT"],
        Literal["TAX_COLLECTED_AT_SOURCE"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string', 'enum': ['GIFTWRAP', 'FULFILLMENT', 'MARKETINGINSERT', 'PACKAGING', 'LOADING', 'FREIGHTOUT', 'TAX_COLLECTED_AT_SOURCE']}

    charge_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class InvoiceDetail:

    additional_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/AdditionalDetails')}
    charge_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/ChargeDetails')}
    invoice_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string', 'schema_format': 'date-time'}
    invoice_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/InvoiceItem')}
    payment_terms_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    ship_to_country_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    tax_totals: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetail')}

    bill_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/PartyIdentification'}
    invoice_total: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Money'}
    remit_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/PartyIdentification'}
    pass


@attrs.define
class InvoiceItem:

    buyer_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    charge_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/ChargeDetails')}
    hsn_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    item_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetail')}
    vendor_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}

    invoiced_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/ItemQuantity'}
    net_cost: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'integer'}
    unit_of_measure: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}

    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    tax_registration_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxRegistrationDetail')}

    address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class SubmitInvoiceRequest:

    invoices: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'array', 'items': Reference(ref='#/components/schemas/InvoiceDetail')}

    pass


@attrs.define
class SubmitInvoiceResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/TransactionReference'}
    pass


@attrs.define
class TaxDetail:

    tax_type: Union[
        Literal["CGST"],
        Literal["SGST"],
        Literal["CESS"],
        Literal["UTGST"],
        Literal["IGST"],
        Literal["MwSt."],
        Literal["PST"],
        Literal["TVA"],
        Literal["VAT"],
        Literal["GST"],
        Literal["ST"],
        Literal["Consumption"],
        Literal["MutuallyDefined"],
        Literal["DomesticVAT"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string', 'enum': ['CGST', 'SGST', 'CESS', 'UTGST', 'IGST', 'MwSt.', 'PST', 'TVA', 'VAT', 'GST', 'ST', 'Consumption', 'MutuallyDefined', 'DomesticVAT']}

    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Money'}
    tax_rate: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Decimal'}
    taxable_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class TaxRegistrationDetail:

    tax_registration_message: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string', 'enum': ['VAT', 'GST']}

    tax_registration_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002161E6FB970>, 'type': 'string'}

    pass


class VendorDirectFulfillmentPaymentsV1Client(BaseClient):
    def submit_invoice(
        self,
    ):
        """
        Submits one or more invoices for a vendor's direct fulfillment orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/directFulfillment/payments/v1/invoices"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoice_params)
        return response

    _submit_invoice_params = ()  # name, param in
