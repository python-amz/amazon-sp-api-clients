"""
Selling Partner API for Retail Procurement Payments
=============================================================================================

The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
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
    type: Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]] = attrs.field()

    pass


@attrs.define
class Address:
    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    # {'maxLength': 2}
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_or_zip_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class AllowanceDetails:
    description: str = attrs.field()
    tax_details: list["TaxDetails"] = attrs.field()
    type: Union[
        Literal["Discount"],
        Literal["DiscountIncentive"],
        Literal["Defective"],
        Literal["Promotional"],
        Literal["UnsaleableMerchandise"],
        Literal["Special"],
    ] = attrs.field()

    allowance_amount: "Money" = attrs.field()
    pass


@attrs.define
class ChargeDetails:
    description: str = attrs.field()
    tax_details: list["TaxDetails"] = attrs.field()
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
    ] = attrs.field()

    charge_amount: "Money" = attrs.field()
    pass


@attrs.define
class CreditNoteDetails:
    consignors_reference_number: str = attrs.field()
    coop_reference_number: str = attrs.field()
    debit_note_number: str = attrs.field()
    reference_invoice_number: str = attrs.field()
    returns_reference_number: str = attrs.field()
    rma_id: str = attrs.field()

    goods_return_date: "DateTime" = attrs.field()
    pass


@attrs.define
class DateTime:
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
class Invoice:
    additional_details: list["AdditionalDetails"] = attrs.field()
    allowance_details: list["AllowanceDetails"] = attrs.field()
    charge_details: list["ChargeDetails"] = attrs.field()
    id: str = attrs.field()
    invoice_type: Union[Literal["Invoice"], Literal["CreditNote"]] = attrs.field()
    items: list["InvoiceItem"] = attrs.field()
    reference_number: str = attrs.field()
    tax_details: list["TaxDetails"] = attrs.field()

    bill_to_party: "PartyIdentification" = attrs.field()
    date: "DateTime" = attrs.field()
    invoice_total: "Money" = attrs.field()
    payment_terms: "PaymentTerms" = attrs.field()
    remit_to_party: "PartyIdentification" = attrs.field()
    ship_from_party: "PartyIdentification" = attrs.field()
    ship_to_party: "PartyIdentification" = attrs.field()
    pass


@attrs.define
class InvoiceItem:
    allowance_details: list["AllowanceDetails"] = attrs.field()
    amazon_product_identifier: str = attrs.field()
    charge_details: list["ChargeDetails"] = attrs.field()
    hsn_code: str = attrs.field()
    item_sequence_number: int = attrs.field()
    purchase_order_number: str = attrs.field()
    tax_details: list["TaxDetails"] = attrs.field()
    vendor_product_identifier: str = attrs.field()

    credit_note_details: "CreditNoteDetails" = attrs.field()
    invoiced_quantity: "ItemQuantity" = attrs.field()
    net_cost: "Money" = attrs.field()
    pass


@attrs.define
class ItemQuantity:
    amount: int = attrs.field()
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field()
    unit_size: int = attrs.field()

    pass


@attrs.define
class Money:
    currency_code: str = attrs.field()

    amount: "Decimal" = attrs.field()
    pass


@attrs.define
class PartyIdentification:
    party_id: str = attrs.field()
    tax_registration_details: list["TaxRegistrationDetails"] = attrs.field()

    address: "Address" = attrs.field()
    pass


@attrs.define
class PaymentTerms:
    discount_due_days: Union[float, int] = attrs.field()
    net_due_days: Union[float, int] = attrs.field()
    type: Union[
        Literal["Basic"],
        Literal["EndOfMonth"],
        Literal["FixedDate"],
        Literal["Proximo"],
        Literal["PaymentDueUponReceiptOfInvoice"],
        Literal["LetterofCredit"],
    ] = attrs.field()

    discount_percent: "Decimal" = attrs.field()
    pass


@attrs.define
class SubmitInvoicesRequest:
    invoices: list["Invoice"] = attrs.field()

    pass


@attrs.define
class SubmitInvoicesResponse:
    errors: "ErrorList" = attrs.field()
    payload: "TransactionId" = attrs.field()
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
    ] = attrs.field()

    tax_amount: "Money" = attrs.field()
    tax_rate: "Decimal" = attrs.field()
    taxable_amount: "Money" = attrs.field()
    pass


@attrs.define
class TaxRegistrationDetails:
    tax_registration_number: str = attrs.field()
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()

    pass


@attrs.define
class TransactionId:
    transaction_id: str = attrs.field()

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
