"""
Selling Partner API for Retail Procurement Payments
=============================================================================================

The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
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
    type: Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]]

    pass


@attrs.define
class Address:

    address_line1: str
    address_line2: str
    address_line3: str
    city: str
    country_code: str
    # {'maxLength': 2}
    county: str
    district: str
    name: str
    phone: str
    postal_or_zip_code: str
    state_or_region: str

    pass


@attrs.define
class AllowanceDetails:

    description: str
    tax_details: list["TaxDetails"]
    type: Union[
        Literal["Discount"],
        Literal["DiscountIncentive"],
        Literal["Defective"],
        Literal["Promotional"],
        Literal["UnsaleableMerchandise"],
        Literal["Special"],
    ]

    allowance_amount: "Money"
    pass


@attrs.define
class ChargeDetails:

    description: str
    tax_details: list["TaxDetails"]
    type: Union[
        Literal["Freight"],
        Literal["Packing"],
        Literal["Duty"],
        Literal["Service"],
        Literal["SmallOrder"],
        Literal["InsurancePlacementCost"],
        Literal["InsuranceFee"],
        Literal["SpecialHandlingService"],
        Literal["CollectionAndRecyclingService"],
        Literal["EnvironmentalProtectionService"],
        Literal["TaxCollectedAtSource"],
    ]

    charge_amount: "Money"
    pass


@attrs.define
class CreditNoteDetails:

    consignors_reference_number: str
    coop_reference_number: str
    debit_note_number: str
    reference_invoice_number: str
    returns_reference_number: str
    rma_id: str

    goods_return_date: "DateTime"
    pass


@attrs.define
class DateTime:

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
class Invoice:

    additional_details: list["AdditionalDetails"]
    allowance_details: list["AllowanceDetails"]
    charge_details: list["ChargeDetails"]
    id: str
    invoice_type: Union[Literal["Invoice"], Literal["CreditNote"]]
    items: list["InvoiceItem"]
    reference_number: str
    tax_details: list["TaxDetails"]

    bill_to_party: "PartyIdentification"
    date: "DateTime"
    invoice_total: "Money"
    payment_terms: "PaymentTerms"
    remit_to_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    ship_to_party: "PartyIdentification"
    pass


@attrs.define
class InvoiceItem:

    allowance_details: list["AllowanceDetails"]
    amazon_product_identifier: str
    charge_details: list["ChargeDetails"]
    hsn_code: str
    item_sequence_number: int
    purchase_order_number: str
    tax_details: list["TaxDetails"]
    vendor_product_identifier: str

    credit_note_details: "CreditNoteDetails"
    invoiced_quantity: "ItemQuantity"
    net_cost: "Money"
    pass


@attrs.define
class ItemQuantity:

    amount: int
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]]
    unit_size: int

    pass


@attrs.define
class Money:

    currency_code: str

    amount: "Decimal"
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    tax_registration_details: list["TaxRegistrationDetails"]

    address: "Address"
    pass


@attrs.define
class PaymentTerms:

    discount_due_days: Union[float, int]
    net_due_days: Union[float, int]
    type: Union[
        Literal["Basic"],
        Literal["EndOfMonth"],
        Literal["FixedDate"],
        Literal["Proximo"],
        Literal["PaymentDueUponReceiptOfInvoice"],
        Literal["LetterofCredit"],
    ]

    discount_percent: "Decimal"
    pass


@attrs.define
class SubmitInvoicesRequest:

    invoices: list["Invoice"]

    pass


@attrs.define
class SubmitInvoicesResponse:

    errors: "ErrorList"
    payload: "TransactionId"
    pass


@attrs.define
class TaxDetails:

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
class TaxRegistrationDetails:

    tax_registration_number: str
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]

    pass


@attrs.define
class TransactionId:

    transaction_id: str

    pass


class VendorInvoicesV1Client(BaseClient):
    def submit_invoices(
        self,
    ):
        """
        Submit new invoices to Amazon.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/payments/v1/invoices"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoices_params)
        return response

    _submit_invoices_params = ()  # name, param in
