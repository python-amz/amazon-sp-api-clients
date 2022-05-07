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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _additional_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AdditionalDetails(**data)

    detail: str = attrs.field()
    """
    The detail of the additional information provided by the selling party.
    """

    language_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The language code of the additional information detail.
    """

    type: Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]] = attrs.field()
    """
    The type of the additional information provided by the selling party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    A physical address.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Address(**data)

    address_line1: str = attrs.field()
    """
    First line of street address.
    """

    address_line2: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.

    Extra fields:
    {'maxLength': 2}
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_or_zip_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal or zip code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AllowanceDetails:
    """
    Monetary and tax details of the allowance.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _allowance_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AllowanceDetails(**data)

    allowance_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    description: Optional[str] = attrs.field(
        default=None,
    )
    """
    Description of the allowance.
    """

    tax_details: Optional[List["TaxDetails"]] = attrs.field(
        default=None,
    )
    """
    Tax amount details applied on this allowance.
    """

    type: Union[
        Literal["Discount"],
        Literal["DiscountIncentive"],
        Literal["Defective"],
        Literal["Promotional"],
        Literal["UnsaleableMerchandise"],
        Literal["Special"],
    ] = attrs.field()
    """
    Type of the allowance applied.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ChargeDetails:
    """
    Monetary and tax details of the charge.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _charge_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ChargeDetails(**data)

    charge_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    description: Optional[str] = attrs.field(
        default=None,
    )
    """
    Description of the charge.
    """

    tax_details: Optional[List["TaxDetails"]] = attrs.field(
        default=None,
    )
    """
    Tax amount details applied on this charge.
    """

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
    """
    Type of the charge applied.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreditNoteDetails:
    """
    References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _credit_note_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreditNoteDetails(**data)

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
    """
    Defines a date and time according to ISO8601.
    """

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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _date_time_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DateTime(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _decimal_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Decimal(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Invoice:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _invoice_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Invoice(**data)

    additional_details: Optional[List["AdditionalDetails"]] = attrs.field(
        default=None,
    )
    """
    Additional details provided by the selling party, for tax related or other purposes.
    """

    allowance_details: Optional[List["AllowanceDetails"]] = attrs.field(
        default=None,
    )
    """
    Total allowance amount details for all line items.
    """

    bill_to_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    charge_details: Optional[List["ChargeDetails"]] = attrs.field(
        default=None,
    )
    """
    Total charge amount details for all line items.
    """

    date: "DateTime" = attrs.field()
    """
    Defines a date and time according to ISO8601.
    """

    id: str = attrs.field()
    """
    Unique number relating to the charges defined in this document. This will be invoice number if the document type is Invoice or CreditNote number if the document type is Credit Note. Failure to provide this reference will result in a rejection.
    """

    invoice_total: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    invoice_type: Union[Literal["Invoice"], Literal["CreditNote"]] = attrs.field()
    """
    Identifies the type of invoice.
    """

    items: Optional[List["InvoiceItem"]] = attrs.field(
        default=None,
    )
    """
    The list of invoice items.
    """

    payment_terms: Optional["PaymentTerms"] = attrs.field(
        default=None,
    )
    """
    Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
    """

    reference_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    An additional unique reference number used for regulatory or other purposes.
    """

    remit_to_party: "PartyIdentification" = attrs.field()

    ship_from_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    ship_to_party: Optional["PartyIdentification"] = attrs.field(
        default=None,
    )

    tax_details: Optional[List["TaxDetails"]] = attrs.field(
        default=None,
    )
    """
    Total tax amount details for all line items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvoiceItem:
    """
    Details of the item being invoiced.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _invoice_item_name_convert
        data = {name_convert[k]: v for k, v in data}
        return InvoiceItem(**data)

    allowance_details: Optional[List["AllowanceDetails"]] = attrs.field(
        default=None,
    )
    """
    Individual allowance details per line item.
    """

    amazon_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon Standard Identification Number (ASIN) of an item.
    """

    charge_details: Optional[List["ChargeDetails"]] = attrs.field(
        default=None,
    )
    """
    Individual charge details per line item.
    """

    credit_note_details: Optional["CreditNoteDetails"] = attrs.field(
        default=None,
    )
    """
    References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
    """

    hsn_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    HSN Tax code. The HSN number cannot contain alphabets.
    """

    invoiced_quantity: "ItemQuantity" = attrs.field()
    """
    Details of quantity.
    """

    item_sequence_number: int = attrs.field()
    """
    Unique number related to this line item.
    """

    net_cost: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    purchase_order_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon purchase order number for this invoiced line item. Formatting Notes: 8-character alpha-numeric code. This value is mandatory only when invoiceType is Invoice, and is not required when invoiceType is CreditNote.
    """

    tax_details: Optional[List["TaxDetails"]] = attrs.field(
        default=None,
    )
    """
    Individual tax details per line item.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identifier of the item. Should be the same as was provided in the purchase order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of quantity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_quantity_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ItemQuantity(**data)

    amount: int = attrs.field()
    """
    Quantity of an item. This value should not be zero.
    """

    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field()
    """
    Unit of measure for the quantity.
    """

    unit_size: Optional[int] = attrs.field(
        default=None,
    )
    """
    The case size, if the unit of measure value is Cases.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Money(**data)

    amount: Optional["Decimal"] = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    currency_code: Optional[str] = attrs.field()
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _party_identification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PartyIdentification(**data)

    address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    A physical address.
    """

    party_id: str = attrs.field()
    """
    Assigned identification for the party.
    """

    tax_registration_details: Optional[List["TaxRegistrationDetails"]] = attrs.field(
        default=None,
    )
    """
    Tax registration details of the party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PaymentTerms:
    """
    Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _payment_terms_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PaymentTerms(**data)

    discount_due_days: Optional[float] = attrs.field()
    """
    The number of calendar days from the Base date (Invoice date) until the discount is no longer valid.
    """

    discount_percent: Optional["Decimal"] = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_invoices_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SubmitInvoicesRequest(**data)

    invoices: Optional[List["Invoice"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoicesResponse:
    """
    The response schema for the submitInvoices operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_invoices_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SubmitInvoicesResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxDetails:
    """
    Details of tax amount applied.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TaxDetails(**data)

    tax_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    tax_rate: Optional["Decimal"] = attrs.field(
        default=None,
    )
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

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
    """
    Type of the tax applied.
    """

    taxable_amount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_registration_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TaxRegistrationDetails(**data)

    tax_registration_number: str = attrs.field()
    """
    The tax registration number for the entity. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()
    """
    The tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionId:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TransactionId(**data)

    transaction_id: Optional[str] = attrs.field()
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


_additional_details_name_convert = {
    "detail": "detail",
    "languageCode": "language_code",
    "type": "type",
}

_address_name_convert = {
    "addressLine1": "address_line1",
    "addressLine2": "address_line2",
    "addressLine3": "address_line3",
    "city": "city",
    "countryCode": "country_code",
    "county": "county",
    "district": "district",
    "name": "name",
    "phone": "phone",
    "postalOrZipCode": "postal_or_zip_code",
    "stateOrRegion": "state_or_region",
}

_allowance_details_name_convert = {
    "allowanceAmount": "allowance_amount",
    "description": "description",
    "taxDetails": "tax_details",
    "type": "type",
}

_charge_details_name_convert = {
    "chargeAmount": "charge_amount",
    "description": "description",
    "taxDetails": "tax_details",
    "type": "type",
}

_credit_note_details_name_convert = {
    "consignorsReferenceNumber": "consignors_reference_number",
    "coopReferenceNumber": "coop_reference_number",
    "debitNoteNumber": "debit_note_number",
    "goodsReturnDate": "goods_return_date",
    "referenceInvoiceNumber": "reference_invoice_number",
    "returnsReferenceNumber": "returns_reference_number",
    "rmaId": "rma_id",
}

_date_time_name_convert = {}

_decimal_name_convert = {}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_invoice_name_convert = {
    "additionalDetails": "additional_details",
    "allowanceDetails": "allowance_details",
    "billToParty": "bill_to_party",
    "chargeDetails": "charge_details",
    "date": "date",
    "id": "id",
    "invoiceTotal": "invoice_total",
    "invoiceType": "invoice_type",
    "items": "items",
    "paymentTerms": "payment_terms",
    "referenceNumber": "reference_number",
    "remitToParty": "remit_to_party",
    "shipFromParty": "ship_from_party",
    "shipToParty": "ship_to_party",
    "taxDetails": "tax_details",
}

_invoice_item_name_convert = {
    "allowanceDetails": "allowance_details",
    "amazonProductIdentifier": "amazon_product_identifier",
    "chargeDetails": "charge_details",
    "creditNoteDetails": "credit_note_details",
    "hsnCode": "hsn_code",
    "invoicedQuantity": "invoiced_quantity",
    "itemSequenceNumber": "item_sequence_number",
    "netCost": "net_cost",
    "purchaseOrderNumber": "purchase_order_number",
    "taxDetails": "tax_details",
    "vendorProductIdentifier": "vendor_product_identifier",
}

_item_quantity_name_convert = {
    "amount": "amount",
    "unitOfMeasure": "unit_of_measure",
    "unitSize": "unit_size",
}

_money_name_convert = {
    "amount": "amount",
    "currencyCode": "currency_code",
}

_party_identification_name_convert = {
    "address": "address",
    "partyId": "party_id",
    "taxRegistrationDetails": "tax_registration_details",
}

_payment_terms_name_convert = {
    "discountDueDays": "discount_due_days",
    "discountPercent": "discount_percent",
    "netDueDays": "net_due_days",
    "type": "type",
}

_submit_invoices_request_name_convert = {
    "invoices": "invoices",
}

_submit_invoices_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_tax_details_name_convert = {
    "taxAmount": "tax_amount",
    "taxRate": "tax_rate",
    "taxType": "tax_type",
    "taxableAmount": "taxable_amount",
}

_tax_registration_details_name_convert = {
    "taxRegistrationNumber": "tax_registration_number",
    "taxRegistrationType": "tax_registration_type",
}

_transaction_id_name_convert = {
    "transactionId": "transaction_id",
}


class VendorInvoicesV1Client(BaseClient):
    def submit_invoices(
        self,
        invoices: List["Invoice"] = None,
    ) -> Union[SubmitInvoicesResponse]:
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_invoices_params,
            self._submit_invoices_responses,
        )
        return response

    _submit_invoices_params = (("invoices", "body"),)  # name, param in

    _submit_invoices_responses = {
        202: SubmitInvoicesResponse,
        400: SubmitInvoicesResponse,
        403: SubmitInvoicesResponse,
        404: SubmitInvoicesResponse,
        413: SubmitInvoicesResponse,
        415: SubmitInvoicesResponse,
        429: SubmitInvoicesResponse,
        500: SubmitInvoicesResponse,
        503: SubmitInvoicesResponse,
    }
