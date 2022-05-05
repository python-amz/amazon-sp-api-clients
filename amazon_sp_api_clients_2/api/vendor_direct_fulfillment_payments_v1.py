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
    language_code: str
    type: Union[Literal["SUR"], Literal["OCR"]]

    pass


@attrs.define
class Address:

    address_line1: str
    address_line2: str
    address_line3: str
    city: str
    country_code: str
    county: str
    district: str
    name: str
    phone: str
    postal_code: str
    state_or_region: str

    pass


@attrs.define
class ChargeDetails:

    tax_details: list["TaxDetail"]
    type: Union[
        Literal["GIFTWRAP"],
        Literal["FULFILLMENT"],
        Literal["MARKETINGINSERT"],
        Literal["PACKAGING"],
        Literal["LOADING"],
        Literal["FREIGHTOUT"],
        Literal["TAX_COLLECTED_AT_SOURCE"],
    ]

    charge_amount: "Money"
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Error:

    code: str
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class InvoiceDetail:

    additional_details: list["AdditionalDetails"]
    charge_details: list["ChargeDetails"]
    invoice_date: str
    # {'schema_format': 'date-time'}
    invoice_number: str
    items: list["InvoiceItem"]
    payment_terms_code: str
    reference_number: str
    ship_to_country_code: str
    tax_totals: list["TaxDetail"]

    bill_to_party: "PartyIdentification"
    invoice_total: "Money"
    remit_to_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    pass


@attrs.define
class InvoiceItem:

    buyer_product_identifier: str
    charge_details: list["ChargeDetails"]
    hsn_code: str
    item_sequence_number: str
    purchase_order_number: str
    tax_details: list["TaxDetail"]
    vendor_order_number: str
    vendor_product_identifier: str

    invoiced_quantity: "ItemQuantity"
    net_cost: "Money"
    pass


@attrs.define
class ItemQuantity:

    amount: int
    unit_of_measure: str

    pass


@attrs.define
class Money:

    currency_code: str

    amount: "Decimal"
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    tax_registration_details: list["TaxRegistrationDetail"]

    address: "Address"
    pass


@attrs.define
class SubmitInvoiceRequest:

    invoices: list["InvoiceDetail"]

    pass


@attrs.define
class SubmitInvoiceResponse:

    errors: "ErrorList"
    payload: "TransactionReference"
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

    tax_amount: "Money"
    tax_rate: "Decimal"
    taxable_amount: "Money"
    pass


@attrs.define
class TaxRegistrationDetail:

    tax_registration_message: str
    tax_registration_number: str
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]

    tax_registration_address: "Address"
    pass


@attrs.define
class TransactionReference:

    transaction_id: str

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
