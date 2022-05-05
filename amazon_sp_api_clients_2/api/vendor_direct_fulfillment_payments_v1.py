"""
Selling Partner API for Direct Fulfillment Payments
=============================================================================================

The Selling Partner API for Direct Fulfillment Payments provides programmatic access to a direct fulfillment vendor's invoice data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AdditionalDetails:
    detail: str = attrs.field()
    language_code: str = attrs.field()
    type: Union[Literal["SUR"], Literal["OCR"]] = attrs.field()

    pass


@attrs.define
class Address:
    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class ChargeDetails:
    tax_details: list["TaxDetail"] = attrs.field()
    type: Union[
        Literal["GIFTWRAP"],
        Literal["FULFILLMENT"],
        Literal["MARKETINGINSERT"],
        Literal["PACKAGING"],
        Literal["LOADING"],
        Literal["FREIGHTOUT"],
        Literal["TAX_COLLECTED_AT_SOURCE"],
    ] = attrs.field()

    charge_amount: "Money" = attrs.field()
    pass


@attrs.define
class Decimal:
    pass


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class InvoiceDetail:
    additional_details: list["AdditionalDetails"] = attrs.field()
    charge_details: list["ChargeDetails"] = attrs.field()
    invoice_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    invoice_number: str = attrs.field()
    items: list["InvoiceItem"] = attrs.field()
    payment_terms_code: str = attrs.field()
    reference_number: str = attrs.field()
    ship_to_country_code: str = attrs.field()
    tax_totals: list["TaxDetail"] = attrs.field()

    bill_to_party: "PartyIdentification" = attrs.field()
    invoice_total: "Money" = attrs.field()
    remit_to_party: "PartyIdentification" = attrs.field()
    ship_from_party: "PartyIdentification" = attrs.field()
    pass


@attrs.define
class InvoiceItem:
    buyer_product_identifier: str = attrs.field()
    charge_details: list["ChargeDetails"] = attrs.field()
    hsn_code: str = attrs.field()
    item_sequence_number: str = attrs.field()
    purchase_order_number: str = attrs.field()
    tax_details: list["TaxDetail"] = attrs.field()
    vendor_order_number: str = attrs.field()
    vendor_product_identifier: str = attrs.field()

    invoiced_quantity: "ItemQuantity" = attrs.field()
    net_cost: "Money" = attrs.field()
    pass


@attrs.define
class ItemQuantity:
    amount: int = attrs.field()
    unit_of_measure: str = attrs.field()

    pass


@attrs.define
class Money:
    currency_code: str = attrs.field()

    amount: "Decimal" = attrs.field()
    pass


@attrs.define
class PartyIdentification:
    party_id: str = attrs.field()
    tax_registration_details: list["TaxRegistrationDetail"] = attrs.field()

    address: "Address" = attrs.field()
    pass


@attrs.define
class SubmitInvoiceRequest:
    invoices: list["InvoiceDetail"] = attrs.field()

    pass


@attrs.define
class SubmitInvoiceResponse:
    errors: "ErrorList" = attrs.field()
    payload: "TransactionReference" = attrs.field()
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
    ] = attrs.field()

    tax_amount: "Money" = attrs.field()
    tax_rate: "Decimal" = attrs.field()
    taxable_amount: "Money" = attrs.field()
    pass


@attrs.define
class TaxRegistrationDetail:
    tax_registration_message: str = attrs.field()
    tax_registration_number: str = attrs.field()
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()

    tax_registration_address: "Address" = attrs.field()
    pass


@attrs.define
class TransactionReference:
    transaction_id: str = attrs.field()

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
