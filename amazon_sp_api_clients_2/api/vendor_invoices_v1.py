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
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    language_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    type: Union[Literal["SUR"], Literal["OCR"], Literal["CartonCount"]]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['SUR', 'OCR', 'CartonCount'], 'type': 'string'}

    pass


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'maxLength': 2, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    postal_or_zip_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}

    pass


@attrs.define
class AllowanceDetails:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    type: Union[
        Literal["Discount"],
        Literal["DiscountIncentive"],
        Literal["Defective"],
        Literal["Promotional"],
        Literal["UnsaleableMerchandise"],
        Literal["Special"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['Discount', 'DiscountIncentive', 'Defective', 'Promotional', 'UnsaleableMerchandise', 'Special'], 'type': 'string'}

    allowance_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class ChargeDetails:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
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
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['Freight', 'Packing', 'Duty', 'Service', 'SmallOrder', 'InsurancePlacementCost', 'InsuranceFee', 'SpecialHandlingService', 'CollectionAndRecyclingService', 'EnvironmentalProtectionService', 'TaxCollectedAtSource'], 'type': 'string'}

    charge_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class CreditNoteDetails:

    consignors_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    coop_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    debit_note_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    reference_invoice_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    returns_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    rma_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}

    goods_return_date: str
    # {'ref': '#/components/schemas/DateTime', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
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
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class Invoice:

    additional_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/AdditionalDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    allowance_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/AllowanceDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    charge_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ChargeDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    invoice_type: Union[Literal["Invoice"], Literal["CreditNote"]]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['Invoice', 'CreditNote'], 'type': 'string'}
    items: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/InvoiceItem'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}

    bill_to_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    date: str
    # {'ref': '#/components/schemas/DateTime', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    invoice_total: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    payment_terms: dict[str, Any]
    # {'ref': '#/components/schemas/PaymentTerms', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    remit_to_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    ship_from_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    ship_to_party: dict[str, Any]
    # {'ref': '#/components/schemas/PartyIdentification', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class InvoiceItem:

    allowance_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/AllowanceDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    amazon_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    charge_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ChargeDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    hsn_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    item_sequence_number: int
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'integer'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    tax_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}

    credit_note_details: dict[str, Any]
    # {'ref': '#/components/schemas/CreditNoteDetails', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    invoiced_quantity: dict[str, Any]
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    net_cost: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'integer'}
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['Cases', 'Eaches'], 'type': 'string'}
    unit_size: int
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'integer'}

    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}

    amount: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    tax_registration_details: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxRegistrationDetails'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}

    address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class PaymentTerms:

    discount_due_days: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'number'}
    net_due_days: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'number'}
    type: Union[
        Literal["Basic"],
        Literal["EndOfMonth"],
        Literal["FixedDate"],
        Literal["Proximo"],
        Literal["PaymentDueUponReceiptOfInvoice"],
        Literal["LetterofCredit"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['Basic', 'EndOfMonth', 'FixedDate', 'Proximo', 'PaymentDueUponReceiptOfInvoice', 'LetterofCredit'], 'type': 'string'}

    discount_percent: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class SubmitInvoicesRequest:

    invoices: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Invoice'), 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'array'}

    pass


@attrs.define
class SubmitInvoicesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TransactionId', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
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
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['CGST', 'SGST', 'CESS', 'UTGST', 'IGST', 'MwSt.', 'PST', 'TVA', 'VAT', 'GST', 'ST', 'Consumption', 'MutuallyDefined', 'DomesticVAT'], 'type': 'string'}

    tax_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    tax_rate: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    taxable_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>}
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'enum': ['VAT', 'GST'], 'type': 'string'}

    pass


@attrs.define
class TransactionId:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001B4ECFF1660>, 'type': 'string'}

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
