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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalDetails:
    """
    A field where selling party can provide additional information for tax related or any other purposes.
    """

    detail: str = attrs.field()
    """
    The detail of the additional information provided by the selling party.
    """

    language_code: Optional[str] = attrs.field()
    """
    The language code of the additional information detail.
    """

    type: Union[Literal["SUR"], Literal["OCR"]] = attrs.field()
    """
    The type of the additional information provided by the selling party.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    Address of the party.
    """

    address_line1: str = attrs.field()
    """
    First line of the address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    city: str = attrs.field()
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code in ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field()
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field()
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: str = attrs.field()
    """
    The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: str = attrs.field()
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ChargeDetails:
    """
    Monetary and tax details of the charge.
    """

    charge_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    tax_details: Optional[List["TaxDetail"]] = attrs.field()
    """
    Individual tax details per line item.
    """

    type: Union[
        Literal["GIFTWRAP"],
        Literal["FULFILLMENT"],
        Literal["MARKETINGINSERT"],
        Literal["PACKAGING"],
        Literal["LOADING"],
        Literal["FREIGHTOUT"],
        Literal["TAX_COLLECTED_AT_SOURCE"],
    ] = attrs.field()
    """
    Type of charge applied.
    """


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

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvoiceDetail:

    additional_details: Optional[List["AdditionalDetails"]] = attrs.field()
    """
    Additional details provided by the selling party, for tax related or other purposes.
    """

    bill_to_party: Optional["PartyIdentification"] = attrs.field()

    charge_details: Optional[List["ChargeDetails"]] = attrs.field()
    """
    Total charge amount details for all line items.
    """

    invoice_date: datetime = attrs.field()
    """
    Invoice date.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    invoice_number: str = attrs.field()
    """
    The unique invoice number.
    """

    invoice_total: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    items: List["InvoiceItem"] = attrs.field()
    """
    Provides the details of the items in this invoice.
    """

    payment_terms_code: Optional[str] = attrs.field()
    """
    The payment terms for the invoice.
    """

    reference_number: Optional[str] = attrs.field()
    """
    An additional unique reference number used for regulatory or other purposes.
    """

    remit_to_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    ship_to_country_code: Optional[str] = attrs.field()
    """
    Ship-to country code.
    """

    tax_totals: Optional[List["TaxDetail"]] = attrs.field()
    """
    Individual tax details per line item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvoiceItem:

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    charge_details: Optional[List["ChargeDetails"]] = attrs.field()
    """
    Individual charge details per line item.
    """

    hsn_code: Optional[str] = attrs.field()
    """
    HSN tax code. The HSN number cannot contain alphabets.
    """

    invoiced_quantity: "ItemQuantity" = attrs.field()
    """
    Details of item quantity.
    """

    item_sequence_number: str = attrs.field()
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    net_cost: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    tax_details: Optional[List["TaxDetail"]] = attrs.field()
    """
    Individual tax details per line item.
    """

    vendor_order_number: Optional[str] = attrs.field()
    """
    The vendor's order number for this order.
    """

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of item quantity.
    """

    amount: int = attrs.field()
    """
    Quantity of units available for a specific item.
    """

    unit_of_measure: str = attrs.field()
    """
    Unit of measure for the available quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    currency_code: str = attrs.field()
    """
    Three digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:

    address: Optional["Address"] = attrs.field()
    """
    Address of the party.
    """

    party_id: str = attrs.field()
    """
    Assigned Identification for the party.
    """

    tax_registration_details: Optional[List["TaxRegistrationDetail"]] = attrs.field()
    """
    Tax registration details of the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    invoices: Optional[List["InvoiceDetail"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionReference"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxDetail:
    """
    Details of tax amount applied.
    """

    tax_amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    tax_rate: Optional["Decimal"] = attrs.field()
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

    taxable_amount: Optional["Money"] = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetail:
    """
    Tax registration details of the entity.
    """

    tax_registration_address: Optional["Address"] = attrs.field()
    """
    Address of the party.
    """

    tax_registration_message: Optional[str] = attrs.field()
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field()
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Optional[Union[Literal["VAT"], Literal["GST"]]] = attrs.field()
    """
    Tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionReference:

    transaction_id: Optional[str] = attrs.field()
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorDirectFulfillmentPaymentsV1Client(BaseClient):
    def submit_invoice(
        self,
        invoices: List["InvoiceDetail"] = None,
    ) -> Union[SubmitInvoiceResponse]:
        """
        Submits one or more invoices for a vendor's direct fulfillment orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            invoices: no description.
        """
        url = "/vendor/directFulfillment/payments/v1/invoices"
        values = (invoices,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_invoice_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _submit_invoice_params = (("invoices", "body"),)  # name, param in

    _submit_invoice_responses = {
        (202, "application/json"): SubmitInvoiceResponse,
        (400, "application/json"): SubmitInvoiceResponse,
        (403, "application/json"): SubmitInvoiceResponse,
        (404, "application/json"): SubmitInvoiceResponse,
        (413, "application/json"): SubmitInvoiceResponse,
        (415, "application/json"): SubmitInvoiceResponse,
        (429, "application/json"): SubmitInvoiceResponse,
        (500, "application/json"): SubmitInvoiceResponse,
        (503, "application/json"): SubmitInvoiceResponse,
    }
