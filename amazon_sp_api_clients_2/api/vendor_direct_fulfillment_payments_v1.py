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
from datetime import date, datetime


@attrs.define
class AdditionalDetails:
    """
    A field where selling party can provide additional information for tax related or any other purposes.
    """

    detail: str = attrs.field(
        kw_only=True,
    )
    """
    The detail of the additional information provided by the selling party.
    """

    language_code: str = attrs.field(
        kw_only=True,
    )
    """
    The language code of the additional information detail.
    """

    type: Union[Literal["SUR"], Literal["OCR"]] = attrs.field(
        kw_only=True,
    )
    """
    The type of the additional information provided by the selling party.
    """


@attrs.define
class Address:
    """
    Address of the party.
    """

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    First line of the address.
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.
    """

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two digit country code in ISO 3166-1 alpha-2 format.
    """

    county: str = attrs.field(
        kw_only=True,
    )
    """
    The county where person, business or institution is located.
    """

    district: str = attrs.field(
        kw_only=True,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person, business or institution at that address.
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: str = attrs.field(
        kw_only=True,
    )
    """
    The state or region where person, business or institution is located.
    """


@attrs.define
class ChargeDetails:
    """
    Monetary and tax details of the charge.
    """

    charge_amount: "Money" = attrs.field(
        kw_only=True,
    )

    tax_details: List["TaxDetail"] = attrs.field(
        kw_only=True,
    )
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
    ] = attrs.field(
        kw_only=True,
    )
    """
    Type of charge applied.
    """


@attrs.define
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    pass


@attrs.define
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class InvoiceDetail:

    additional_details: List["AdditionalDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Additional details provided by the selling party, for tax related or other purposes.
    """

    bill_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    charge_details: List["ChargeDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Total charge amount details for all line items.
    """

    invoice_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    Invoice date.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    invoice_number: str = attrs.field(
        kw_only=True,
    )
    """
    The unique invoice number.
    """

    invoice_total: "Money" = attrs.field(
        kw_only=True,
    )

    items: List["InvoiceItem"] = attrs.field(
        kw_only=True,
    )
    """
    Provides the details of the items in this invoice.
    """

    payment_terms_code: str = attrs.field(
        kw_only=True,
    )
    """
    The payment terms for the invoice.
    """

    reference_number: str = attrs.field(
        kw_only=True,
    )
    """
    An additional unique reference number used for regulatory or other purposes.
    """

    remit_to_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )

    ship_to_country_code: str = attrs.field(
        kw_only=True,
    )
    """
    Ship-to country code.
    """

    tax_totals: List["TaxDetail"] = attrs.field(
        kw_only=True,
    )
    """
    Individual tax details per line item.
    """


@attrs.define
class InvoiceItem:

    buyer_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    Buyer's standard identification number (ASIN) of an item.
    """

    charge_details: List["ChargeDetails"] = attrs.field(
        kw_only=True,
    )
    """
    Individual charge details per line item.
    """

    hsn_code: str = attrs.field(
        kw_only=True,
    )
    """
    HSN tax code. The HSN number cannot contain alphabets.
    """

    invoiced_quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )

    item_sequence_number: str = attrs.field(
        kw_only=True,
    )
    """
    Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.
    """

    net_cost: "Money" = attrs.field(
        kw_only=True,
    )

    purchase_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.
    """

    tax_details: List["TaxDetail"] = attrs.field(
        kw_only=True,
    )
    """
    Individual tax details per line item.
    """

    vendor_order_number: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor's order number for this order.
    """

    vendor_product_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    The vendor selected product identification of the item.
    """


@attrs.define
class ItemQuantity:
    """
    Details of item quantity.
    """

    amount: int = attrs.field(
        kw_only=True,
    )
    """
    Quantity of units available for a specific item.
    """

    unit_of_measure: str = attrs.field(
        kw_only=True,
    )
    """
    Unit of measure for the available quantity.
    """


@attrs.define
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    amount: "Decimal" = attrs.field(
        kw_only=True,
    )

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three digit currency code in ISO 4217 format.
    """


@attrs.define
class PartyIdentification:

    address: "Address" = attrs.field(
        kw_only=True,
    )

    party_id: str = attrs.field(
        kw_only=True,
    )
    """
    Assigned Identification for the party.
    """

    tax_registration_details: List["TaxRegistrationDetail"] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration details of the entity.
    """


@attrs.define
class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    invoices: List["InvoiceDetail"] = attrs.field(
        kw_only=True,
    )


@attrs.define
class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "TransactionReference" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TaxDetail:
    """
    Details of tax amount applied.
    """

    tax_amount: "Money" = attrs.field(
        kw_only=True,
    )

    tax_rate: "Decimal" = attrs.field(
        kw_only=True,
    )

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
    ] = attrs.field(
        kw_only=True,
    )
    """
    Type of the tax applied.
    """

    taxable_amount: "Money" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TaxRegistrationDetail:
    """
    Tax registration details of the entity.
    """

    tax_registration_address: "Address" = attrs.field(
        kw_only=True,
    )

    tax_registration_message: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field(
        kw_only=True,
    )
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field(
        kw_only=True,
    )
    """
    Tax registration type for the entity.
    """


@attrs.define
class TransactionReference:

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


class VendorDirectFulfillmentPaymentsV1Client(BaseClient):
    def submit_invoice(
        self,
        invoices: List["InvoiceDetail"] = None,
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
            invoices: no description.
        """
        url = "/vendor/directFulfillment/payments/v1/invoices"
        values = (invoices,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoice_params)
        return response

    _submit_invoice_params = (("invoices", "body"),)  # name, param in
