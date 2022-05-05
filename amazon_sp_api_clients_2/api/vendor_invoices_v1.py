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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    language_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    type: Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['SUR', 'OCR', 'CartonCount']}

    pass


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'maxLength': 2}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    postal_or_zip_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}

    pass


@attrs.define
class AllowanceDetails:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetails')}
    type: Union[
        Literal["Discount"],
        Literal["DiscountIncentive"],
        Literal["Defective"],
        Literal["Promotional"],
        Literal["UnsaleableMerchandise"],
        Literal["Special"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['Discount', 'DiscountIncentive', 'Defective', 'Promotional', 'UnsaleableMerchandise', 'Special']}

    allowance_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class ChargeDetails:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetails')}
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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['Freight', 'Packing', 'Duty', 'Service', 'SmallOrder', 'InsurancePlacementCost', 'InsuranceFee', 'SpecialHandlingService', 'CollectionAndRecyclingService', 'EnvironmentalProtectionService', 'TaxCollectedAtSource']}

    charge_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class CreditNoteDetails:

    consignors_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    coop_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    debit_note_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    reference_invoice_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    returns_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    rma_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}

    goods_return_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/DateTime'}
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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class Invoice:

    additional_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/AdditionalDetails')}
    allowance_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/AllowanceDetails')}
    charge_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/ChargeDetails')}
    id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    invoice_type: Union[Literal["Invoice"], Literal["CreditNote"]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['Invoice', 'CreditNote']}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/InvoiceItem')}
    reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetails')}

    bill_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/PartyIdentification'}
    date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/DateTime'}
    invoice_total: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Money'}
    payment_terms: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/PaymentTerms'}
    remit_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/PartyIdentification'}
    pass


@attrs.define
class InvoiceItem:

    allowance_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/AllowanceDetails')}
    amazon_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    charge_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/ChargeDetails')}
    hsn_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    item_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'integer'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxDetails')}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}

    credit_note_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/CreditNoteDetails'}
    invoiced_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/ItemQuantity'}
    net_cost: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'integer'}
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['Cases', 'Eaches']}
    unit_size: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'integer'}

    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    tax_registration_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/TaxRegistrationDetails')}

    address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class PaymentTerms:

    discount_due_days: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'number'}
    net_due_days: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'number'}
    type: Union[
        Literal["Basic"],
        Literal["EndOfMonth"],
        Literal["FixedDate"],
        Literal["Proximo"],
        Literal["PaymentDueUponReceiptOfInvoice"],
        Literal["LetterofCredit"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['Basic', 'EndOfMonth', 'FixedDate', 'Proximo', 'PaymentDueUponReceiptOfInvoice', 'LetterofCredit']}

    discount_percent: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class SubmitInvoicesRequest:

    invoices: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'array', 'items': Reference(ref='#/components/schemas/Invoice')}

    pass


@attrs.define
class SubmitInvoicesResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/TransactionId'}
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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['CGST', 'SGST', 'CESS', 'UTGST', 'IGST', 'MwSt.', 'PST', 'TVA', 'VAT', 'GST', 'ST', 'Consumption', 'MutuallyDefined', 'DomesticVAT']}

    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Money'}
    tax_rate: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Decimal'}
    taxable_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string', 'enum': ['VAT', 'GST']}

    pass


@attrs.define
class TransactionId:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB700>, 'type': 'string'}

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
