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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalDetails:
    """
    Additional information provided by the selling party for tax-related or any other purpose.
    """

    detail: Optional[str] = attrs.field()
    """
    The detail of the additional information provided by the selling party.
    """

    language_code: Optional[str] = attrs.field()
    """
    The language code of the additional information detail.
    """

    type: Optional[Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]]] = attrs.field()
    """
    The type of the additional information provided by the selling party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    A physical address.
    """

    address_line1: Optional[str] = attrs.field()
    """
    First line of street address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional address information, if required.
    """

    city: Optional[str] = attrs.field()
    """
    The city where the person, business or institution is located.
    """

    country_code: Optional[str] = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.

    Extra fields:
    {'maxLength': 2}
    """

    county: Optional[str] = attrs.field()
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field()
    """
    The district where person, business or institution is located.
    """

    name: Optional[str] = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_or_zip_code: Optional[str] = attrs.field()
    """
    The postal or zip code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field()
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AllowanceDetails:
    """
    Monetary and tax details of the allowance.
    """

    allowance_amount: Optional["Money"] = attrs.field()

    description: Optional[str] = attrs.field()
    """
    Description of the allowance.
    """

    tax_details: Optional[List["TaxDetails"]] = attrs.field()
    """
    Tax amount details applied on this allowance.
    """

    type: Optional[
        Union[
            Literal["Discount"],
            Literal["DiscountIncentive"],
            Literal["Defective"],
            Literal["Promotional"],
            Literal["UnsaleableMerchandise"],
            Literal["Special"],
        ]
    ] = attrs.field()
    """
    Type of the allowance applied.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ChargeDetails:
    """
    Monetary and tax details of the charge.
    """

    charge_amount: Optional["Money"] = attrs.field()

    description: Optional[str] = attrs.field()
    """
    Description of the charge.
    """

    tax_details: Optional[List["TaxDetails"]] = attrs.field()
    """
    Tax amount details applied on this charge.
    """

    type: Optional[
        Union[
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
    ] = attrs.field()
    """
    Type of the charge applied.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreditNoteDetails:
    """
    References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
    """

    consignors_reference_number: Optional[str] = attrs.field()
    """
    Identifies the consignor reference number (VRET number), if generated by Amazon.
    """

    coop_reference_number: Optional[str] = attrs.field()
    """
    Identifies the COOP reference used for COOP agreement. Failure to provide the COOP reference number or the Debit Note number may lead to a rejection of the Credit Note.
    """

    debit_note_number: Optional[str] = attrs.field()
    """
    Debit Note Number as generated by Amazon. Recommended for Returns and COOP Credit Notes.
    """

    goods_return_date: Optional["DateTime"] = attrs.field()

    reference_invoice_number: Optional[str] = attrs.field()
    """
    Original Invoice Number when sending a credit note relating to an existing invoice. One Invoice only to be processed per Credit Note. This is mandatory for AP Credit Notes.
    """

    returns_reference_number: Optional[str] = attrs.field()
    """
    Identifies the Returns Notice Number. Mandatory for all Returns Credit Notes.
    """

    rma_id: Optional[str] = attrs.field()
    """
    Identifies the Returned Merchandise Authorization ID, if generated.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DateTime:
    """
    Defines a date and time according to ISO8601.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Invoice:

    additional_details: Optional[List["AdditionalDetails"]] = attrs.field()
    """
    Additional details provided by the selling party, for tax related or other purposes.
    """

    allowance_details: Optional[List["AllowanceDetails"]] = attrs.field()
    """
    Total allowance amount details for all line items.
    """

    bill_to_party: Optional["PartyIdentification"] = attrs.field()

    charge_details: Optional[List["ChargeDetails"]] = attrs.field()
    """
    Total charge amount details for all line items.
    """

    date: Optional["DateTime"] = attrs.field()

    id: Optional[str] = attrs.field()
    """
    Unique number relating to the charges defined in this document. This will be invoice number if the document type is Invoice or CreditNote number if the document type is Credit Note. Failure to provide this reference will result in a rejection.
    """

    invoice_total: Optional["Money"] = attrs.field()

    invoice_type: Optional[Union[Literal["Invoice"], Literal["CreditNote"]]] = attrs.field()
    """
    Identifies the type of invoice.
    """

    items: Optional[List["InvoiceItem"]] = attrs.field()
    """
    The list of invoice items.
    """

    payment_terms: Optional["PaymentTerms"] = attrs.field()

    reference_number: Optional[str] = attrs.field()
    """
    An additional unique reference number used for regulatory or other purposes.
    """

    remit_to_party: Optional["PartyIdentification"] = attrs.field()

    ship_from_party: Optional["PartyIdentification"] = attrs.field()

    ship_to_party: Optional["PartyIdentification"] = attrs.field()

    tax_details: Optional[List["TaxDetails"]] = attrs.field()
    """
    Total tax amount details for all line items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvoiceItem:
    """
    Details of the item being invoiced.
    """

    allowance_details: Optional[List["AllowanceDetails"]] = attrs.field()
    """
    Individual allowance details per line item.
    """

    amazon_product_identifier: Optional[str] = attrs.field()
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    charge_details: Optional[List["ChargeDetails"]] = attrs.field()
    """
    Individual charge details per line item.
    """

    credit_note_details: Optional["CreditNoteDetails"] = attrs.field()

    hsn_code: Optional[str] = attrs.field()
    """
    HSN Tax code. The HSN number cannot contain alphabets.
    """

    invoiced_quantity: Optional["ItemQuantity"] = attrs.field()

    item_sequence_number: Optional[int] = attrs.field()
    """
    Unique number related to this line item.
    """

    net_cost: Optional["Money"] = attrs.field()

    purchase_order_number: Optional[str] = attrs.field()
    """
    The Amazon purchase order number for this invoiced line item. Formatting Notes: 8-character alpha-numeric code. This value is mandatory only when invoiceType is Invoice, and is not required when invoiceType is CreditNote.
    """

    tax_details: Optional[List["TaxDetails"]] = attrs.field()
    """
    Individual tax details per line item.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identifier of the item. Should be the same as was provided in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of quantity.
    """

    amount: Optional[int] = attrs.field()
    """
    Quantity of an item. This value should not be zero.
    """

    unit_of_measure: Optional[Union[Literal["Cases"], Literal["Eaches"]]] = attrs.field()
    """
    Unit of measure for the quantity.
    """

    unit_size: Optional[int] = attrs.field()
    """
    The case size, if the unit of measure value is Cases.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: Optional["Decimal"] = attrs.field()

    currency_code: Optional[str] = attrs.field()
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:

    address: Optional["Address"] = attrs.field()

    party_id: Optional[str] = attrs.field()
    """
    Assigned identification for the party.
    """

    tax_registration_details: Optional[List["TaxRegistrationDetails"]] = attrs.field()
    """
    Tax registration details of the party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PaymentTerms:
    """
    Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
    """

    discount_due_days: Optional[float] = attrs.field()
    """
    The number of calendar days from the Base date (Invoice date) until the discount is no longer valid.
    """

    discount_percent: Optional["Decimal"] = attrs.field()

    net_due_days: Optional[float] = attrs.field()
    """
    The number of calendar days from the base date (invoice date) until the total amount on the invoice is due.
    """

    type: Optional[
        Union[
            Literal["Basic"],
            Literal["EndOfMonth"],
            Literal["FixedDate"],
            Literal["Proximo"],
            Literal["PaymentDueUponReceiptOfInvoice"],
            Literal["LetterofCredit"],
        ]
    ] = attrs.field()
    """
    The payment term type for the invoice.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoicesRequest:
    """
    The request schema for the submitInvoices operation.
    """

    invoices: Optional[List["Invoice"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoicesResponse:
    """
    The response schema for the submitInvoices operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["TransactionId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxDetails:
    """
    Details of tax amount applied.
    """

    tax_amount: Optional["Money"] = attrs.field()

    tax_rate: Optional["Decimal"] = attrs.field()

    tax_type: Optional[
        Union[
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
    ] = attrs.field()
    """
    Type of the tax applied.
    """

    taxable_amount: Optional["Money"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_number: Optional[str] = attrs.field()
    """
    The tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Optional[Union[Literal["VAT"], Literal["GST"]]] = attrs.field()
    """
    The tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionId:

    transaction_id: Optional[str] = attrs.field()
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorInvoicesV1Client(BaseClient):
    def submit_invoices(
        self,
        invoices: List["Invoice"] = None,
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
            invoices: no description.
        """
        url = "/vendor/payments/v1/invoices"
        values = (invoices,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoices_params)
        return response

    _submit_invoices_params = (("invoices", "body"),)  # name, param in
