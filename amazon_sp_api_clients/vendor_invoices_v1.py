from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class SubmitInvoicesResponse(__BaseDictObject):
    """
    The response schema for the submitInvoices operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: TransactionId = self._get_value(TransactionId, "payload")
        else:
            self.payload: TransactionId = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class TransactionId(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "transactionId" in data:
            self.transactionId: str = self._get_value(str, "transactionId")
        else:
            self.transactionId: str = None


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class SubmitInvoicesRequest(__BaseDictObject):
    """
    The request schema for the submitInvoices operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "invoices" in data:
            self.invoices: _List[Invoice] = [Invoice(datum) for datum in data["invoices"]]
        else:
            self.invoices: _List[Invoice] = []


class Invoice(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "invoiceType" in data:
            self.invoiceType: str = self._get_value(str, "invoiceType")
        else:
            self.invoiceType: str = None
        if "id" in data:
            self.id: str = self._get_value(str, "id")
        else:
            self.id: str = None
        if "referenceNumber" in data:
            self.referenceNumber: str = self._get_value(str, "referenceNumber")
        else:
            self.referenceNumber: str = None
        if "date" in data:
            self.date: DateTime = self._get_value(DateTime, "date")
        else:
            self.date: DateTime = None
        if "remitToParty" in data:
            self.remitToParty: PartyIdentification = self._get_value(PartyIdentification, "remitToParty")
        else:
            self.remitToParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = self._get_value(PartyIdentification, "shipToParty")
        else:
            self.shipToParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = self._get_value(PartyIdentification, "billToParty")
        else:
            self.billToParty: PartyIdentification = None
        if "paymentTerms" in data:
            self.paymentTerms: PaymentTerms = self._get_value(PaymentTerms, "paymentTerms")
        else:
            self.paymentTerms: PaymentTerms = None
        if "invoiceTotal" in data:
            self.invoiceTotal: Money = self._get_value(Money, "invoiceTotal")
        else:
            self.invoiceTotal: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetails] = [TaxDetails(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetails] = []
        if "additionalDetails" in data:
            self.additionalDetails: _List[AdditionalDetails] = [
                AdditionalDetails(datum) for datum in data["additionalDetails"]
            ]
        else:
            self.additionalDetails: _List[AdditionalDetails] = []
        if "chargeDetails" in data:
            self.chargeDetails: _List[ChargeDetails] = [ChargeDetails(datum) for datum in data["chargeDetails"]]
        else:
            self.chargeDetails: _List[ChargeDetails] = []
        if "allowanceDetails" in data:
            self.allowanceDetails: _List[AllowanceDetails] = [
                AllowanceDetails(datum) for datum in data["allowanceDetails"]
            ]
        else:
            self.allowanceDetails: _List[AllowanceDetails] = []
        if "items" in data:
            self.items: _List[InvoiceItem] = [InvoiceItem(datum) for datum in data["items"]]
        else:
            self.items: _List[InvoiceItem] = []


class PartyIdentification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "partyId" in data:
            self.partyId: str = self._get_value(str, "partyId")
        else:
            self.partyId: str = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None
        if "taxRegistrationDetails" in data:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = [
                TaxRegistrationDetails(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = []


class TaxRegistrationDetails(__BaseDictObject):
    """
    Tax registration details of the entity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "taxRegistrationType" in data:
            self.taxRegistrationType: str = self._get_value(str, "taxRegistrationType")
        else:
            self.taxRegistrationType: str = None
        if "taxRegistrationNumber" in data:
            self.taxRegistrationNumber: str = self._get_value(str, "taxRegistrationNumber")
        else:
            self.taxRegistrationNumber: str = None


class Address(__BaseDictObject):
    """
    A physical address.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "addressLine1" in data:
            self.addressLine1: str = self._get_value(str, "addressLine1")
        else:
            self.addressLine1: str = None
        if "addressLine2" in data:
            self.addressLine2: str = self._get_value(str, "addressLine2")
        else:
            self.addressLine2: str = None
        if "addressLine3" in data:
            self.addressLine3: str = self._get_value(str, "addressLine3")
        else:
            self.addressLine3: str = None
        if "city" in data:
            self.city: str = self._get_value(str, "city")
        else:
            self.city: str = None
        if "county" in data:
            self.county: str = self._get_value(str, "county")
        else:
            self.county: str = None
        if "district" in data:
            self.district: str = self._get_value(str, "district")
        else:
            self.district: str = None
        if "stateOrRegion" in data:
            self.stateOrRegion: str = self._get_value(str, "stateOrRegion")
        else:
            self.stateOrRegion: str = None
        if "postalOrZipCode" in data:
            self.postalOrZipCode: str = self._get_value(str, "postalOrZipCode")
        else:
            self.postalOrZipCode: str = None
        if "countryCode" in data:
            self.countryCode: str = self._get_value(str, "countryCode")
        else:
            self.countryCode: str = None
        if "phone" in data:
            self.phone: str = self._get_value(str, "phone")
        else:
            self.phone: str = None


class InvoiceItem(__BaseDictObject):
    """
    Details of the item being invoiced.
    """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: int = self._get_value(int, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: int = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = self._get_value(str, "amazonProductIdentifier")
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "invoicedQuantity" in data:
            self.invoicedQuantity: ItemQuantity = self._get_value(ItemQuantity, "invoicedQuantity")
        else:
            self.invoicedQuantity: ItemQuantity = None
        if "netCost" in data:
            self.netCost: Money = self._get_value(Money, "netCost")
        else:
            self.netCost: Money = None
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "hsnCode" in data:
            self.hsnCode: str = self._get_value(str, "hsnCode")
        else:
            self.hsnCode: str = None
        if "creditNoteDetails" in data:
            self.creditNoteDetails: CreditNoteDetails = self._get_value(CreditNoteDetails, "creditNoteDetails")
        else:
            self.creditNoteDetails: CreditNoteDetails = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetails] = [TaxDetails(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetails] = []
        if "chargeDetails" in data:
            self.chargeDetails: _List[ChargeDetails] = [ChargeDetails(datum) for datum in data["chargeDetails"]]
        else:
            self.chargeDetails: _List[ChargeDetails] = []
        if "allowanceDetails" in data:
            self.allowanceDetails: _List[AllowanceDetails] = [
                AllowanceDetails(datum) for datum in data["allowanceDetails"]
            ]
        else:
            self.allowanceDetails: _List[AllowanceDetails] = []


class TaxDetails(__BaseDictObject):
    """
    Details of tax amount applied.
    """

    def __init__(self, data):
        super().__init__(data)
        if "taxType" in data:
            self.taxType: str = self._get_value(str, "taxType")
        else:
            self.taxType: str = None
        if "taxRate" in data:
            self.taxRate: Decimal = self._get_value(Decimal, "taxRate")
        else:
            self.taxRate: Decimal = None
        if "taxAmount" in data:
            self.taxAmount: Money = self._get_value(Money, "taxAmount")
        else:
            self.taxAmount: Money = None
        if "taxableAmount" in data:
            self.taxableAmount: Money = self._get_value(Money, "taxableAmount")
        else:
            self.taxableAmount: Money = None


class Money(__BaseDictObject):
    """
    An amount of money, including units in the form of currency.
    """

    def __init__(self, data):
        super().__init__(data)
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = self._get_value(Decimal, "amount")
        else:
            self.amount: Decimal = None


class AdditionalDetails(__BaseDictObject):
    """
    Additional information provided by the selling party for tax-related or any other purpose.
    """

    def __init__(self, data):
        super().__init__(data)
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None
        if "detail" in data:
            self.detail: str = self._get_value(str, "detail")
        else:
            self.detail: str = None
        if "languageCode" in data:
            self.languageCode: str = self._get_value(str, "languageCode")
        else:
            self.languageCode: str = None


class ChargeDetails(__BaseDictObject):
    """
    Monetary and tax details of the charge.
    """

    def __init__(self, data):
        super().__init__(data)
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None
        if "description" in data:
            self.description: str = self._get_value(str, "description")
        else:
            self.description: str = None
        if "chargeAmount" in data:
            self.chargeAmount: Money = self._get_value(Money, "chargeAmount")
        else:
            self.chargeAmount: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetails] = [TaxDetails(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetails] = []


class AllowanceDetails(__BaseDictObject):
    """
    Monetary and tax details of the allowance.
    """

    def __init__(self, data):
        super().__init__(data)
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None
        if "description" in data:
            self.description: str = self._get_value(str, "description")
        else:
            self.description: str = None
        if "allowanceAmount" in data:
            self.allowanceAmount: Money = self._get_value(Money, "allowanceAmount")
        else:
            self.allowanceAmount: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetails] = [TaxDetails(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetails] = []


class PaymentTerms(__BaseDictObject):
    """
    Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
    """

    def __init__(self, data):
        super().__init__(data)
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None
        if "discountPercent" in data:
            self.discountPercent: Decimal = self._get_value(Decimal, "discountPercent")
        else:
            self.discountPercent: Decimal = None
        if "discountDueDays" in data:
            self.discountDueDays: float = self._get_value(float, "discountDueDays")
        else:
            self.discountDueDays: float = None
        if "netDueDays" in data:
            self.netDueDays: float = self._get_value(float, "netDueDays")
        else:
            self.netDueDays: float = None


class CreditNoteDetails(__BaseDictObject):
    """
    References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
    """

    def __init__(self, data):
        super().__init__(data)
        if "referenceInvoiceNumber" in data:
            self.referenceInvoiceNumber: str = self._get_value(str, "referenceInvoiceNumber")
        else:
            self.referenceInvoiceNumber: str = None
        if "debitNoteNumber" in data:
            self.debitNoteNumber: str = self._get_value(str, "debitNoteNumber")
        else:
            self.debitNoteNumber: str = None
        if "returnsReferenceNumber" in data:
            self.returnsReferenceNumber: str = self._get_value(str, "returnsReferenceNumber")
        else:
            self.returnsReferenceNumber: str = None
        if "goodsReturnDate" in data:
            self.goodsReturnDate: DateTime = self._get_value(DateTime, "goodsReturnDate")
        else:
            self.goodsReturnDate: DateTime = None
        if "rmaId" in data:
            self.rmaId: str = self._get_value(str, "rmaId")
        else:
            self.rmaId: str = None
        if "coopReferenceNumber" in data:
            self.coopReferenceNumber: str = self._get_value(str, "coopReferenceNumber")
        else:
            self.coopReferenceNumber: str = None
        if "consignorsReferenceNumber" in data:
            self.consignorsReferenceNumber: str = self._get_value(str, "consignorsReferenceNumber")
        else:
            self.consignorsReferenceNumber: str = None


class ItemQuantity(__BaseDictObject):
    """
    Details of quantity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "amount" in data:
            self.amount: int = self._get_value(int, "amount")
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None
        if "unitSize" in data:
            self.unitSize: int = self._get_value(int, "unitSize")
        else:
            self.unitSize: int = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """


class DateTime(str):
    """
    Defines a date and time according to ISO8601.
    """


class VendorInvoicesV1Client(__BaseClient):
    def submitInvoices(
        self,
        data: SubmitInvoicesRequest,
    ):
        """
                Submit new invoices to Amazon.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/payments/v1/invoices"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: SubmitInvoicesResponse,
            400: SubmitInvoicesResponse,
            403: SubmitInvoicesResponse,
            404: SubmitInvoicesResponse,
            413: SubmitInvoicesResponse,
            415: SubmitInvoicesResponse,
            429: SubmitInvoicesResponse,
            500: SubmitInvoicesResponse,
            503: SubmitInvoicesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
