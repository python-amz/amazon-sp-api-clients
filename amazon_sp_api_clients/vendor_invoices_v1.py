from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class SubmitInvoicesResponse:
    """
    The response schema for the submitInvoices operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: TransactionId = TransactionId(data["payload"])
        else:
            self.payload: TransactionId = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class TransactionId:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "transactionId" in data:
            self.transactionId: str = str(data["transactionId"])
        else:
            self.transactionId: str = None


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
        else:
            self.details: str = None


class SubmitInvoicesRequest:
    """
    The request schema for the submitInvoices operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "invoices" in data:
            self.invoices: _List[Invoice] = [Invoice(datum) for datum in data["invoices"]]
        else:
            self.invoices: _List[Invoice] = []


class Invoice:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "invoiceType" in data:
            self.invoiceType: str = str(data["invoiceType"])
        else:
            self.invoiceType: str = None
        if "id" in data:
            self.id: str = str(data["id"])
        else:
            self.id: str = None
        if "referenceNumber" in data:
            self.referenceNumber: str = str(data["referenceNumber"])
        else:
            self.referenceNumber: str = None
        if "date" in data:
            self.date: DateTime = DateTime(data["date"])
        else:
            self.date: DateTime = None
        if "remitToParty" in data:
            self.remitToParty: PartyIdentification = PartyIdentification(data["remitToParty"])
        else:
            self.remitToParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = PartyIdentification(data["shipToParty"])
        else:
            self.shipToParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = PartyIdentification(data["billToParty"])
        else:
            self.billToParty: PartyIdentification = None
        if "paymentTerms" in data:
            self.paymentTerms: PaymentTerms = PaymentTerms(data["paymentTerms"])
        else:
            self.paymentTerms: PaymentTerms = None
        if "invoiceTotal" in data:
            self.invoiceTotal: Money = Money(data["invoiceTotal"])
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


class PartyIdentification:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "partyId" in data:
            self.partyId: str = str(data["partyId"])
        else:
            self.partyId: str = None
        if "address" in data:
            self.address: Address = Address(data["address"])
        else:
            self.address: Address = None
        if "taxRegistrationDetails" in data:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = [
                TaxRegistrationDetails(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = []


class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "taxRegistrationType" in data:
            self.taxRegistrationType: str = str(data["taxRegistrationType"])
        else:
            self.taxRegistrationType: str = None
        if "taxRegistrationNumber" in data:
            self.taxRegistrationNumber: str = str(data["taxRegistrationNumber"])
        else:
            self.taxRegistrationNumber: str = None


class Address:
    """
    A physical address.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "addressLine1" in data:
            self.addressLine1: str = str(data["addressLine1"])
        else:
            self.addressLine1: str = None
        if "addressLine2" in data:
            self.addressLine2: str = str(data["addressLine2"])
        else:
            self.addressLine2: str = None
        if "addressLine3" in data:
            self.addressLine3: str = str(data["addressLine3"])
        else:
            self.addressLine3: str = None
        if "city" in data:
            self.city: str = str(data["city"])
        else:
            self.city: str = None
        if "county" in data:
            self.county: str = str(data["county"])
        else:
            self.county: str = None
        if "district" in data:
            self.district: str = str(data["district"])
        else:
            self.district: str = None
        if "stateOrRegion" in data:
            self.stateOrRegion: str = str(data["stateOrRegion"])
        else:
            self.stateOrRegion: str = None
        if "postalOrZipCode" in data:
            self.postalOrZipCode: str = str(data["postalOrZipCode"])
        else:
            self.postalOrZipCode: str = None
        if "countryCode" in data:
            self.countryCode: str = str(data["countryCode"])
        else:
            self.countryCode: str = None
        if "phone" in data:
            self.phone: str = str(data["phone"])
        else:
            self.phone: str = None


class InvoiceItem:
    """
    Details of the item being invoiced.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: int = int(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: int = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = str(data["amazonProductIdentifier"])
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "invoicedQuantity" in data:
            self.invoicedQuantity: ItemQuantity = ItemQuantity(data["invoicedQuantity"])
        else:
            self.invoicedQuantity: ItemQuantity = None
        if "netCost" in data:
            self.netCost: Money = Money(data["netCost"])
        else:
            self.netCost: Money = None
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "hsnCode" in data:
            self.hsnCode: str = str(data["hsnCode"])
        else:
            self.hsnCode: str = None
        if "creditNoteDetails" in data:
            self.creditNoteDetails: CreditNoteDetails = CreditNoteDetails(data["creditNoteDetails"])
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


class TaxDetails:
    """
    Details of tax amount applied.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "taxType" in data:
            self.taxType: str = str(data["taxType"])
        else:
            self.taxType: str = None
        if "taxRate" in data:
            self.taxRate: Decimal = Decimal(data["taxRate"])
        else:
            self.taxRate: Decimal = None
        if "taxAmount" in data:
            self.taxAmount: Money = Money(data["taxAmount"])
        else:
            self.taxAmount: Money = None
        if "taxableAmount" in data:
            self.taxableAmount: Money = Money(data["taxableAmount"])
        else:
            self.taxableAmount: Money = None


class Money:
    """
    An amount of money, including units in the form of currency.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "currencyCode" in data:
            self.currencyCode: str = str(data["currencyCode"])
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = Decimal(data["amount"])
        else:
            self.amount: Decimal = None


class AdditionalDetails:
    """
    Additional information provided by the selling party for tax-related or any other purpose.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "type" in data:
            self.type: str = str(data["type"])
        else:
            self.type: str = None
        if "detail" in data:
            self.detail: str = str(data["detail"])
        else:
            self.detail: str = None
        if "languageCode" in data:
            self.languageCode: str = str(data["languageCode"])
        else:
            self.languageCode: str = None


class ChargeDetails:
    """
    Monetary and tax details of the charge.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "type" in data:
            self.type: str = str(data["type"])
        else:
            self.type: str = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None
        if "chargeAmount" in data:
            self.chargeAmount: Money = Money(data["chargeAmount"])
        else:
            self.chargeAmount: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetails] = [TaxDetails(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetails] = []


class AllowanceDetails:
    """
    Monetary and tax details of the allowance.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "type" in data:
            self.type: str = str(data["type"])
        else:
            self.type: str = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None
        if "allowanceAmount" in data:
            self.allowanceAmount: Money = Money(data["allowanceAmount"])
        else:
            self.allowanceAmount: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetails] = [TaxDetails(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetails] = []


class PaymentTerms:
    """
    Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "type" in data:
            self.type: str = str(data["type"])
        else:
            self.type: str = None
        if "discountPercent" in data:
            self.discountPercent: Decimal = Decimal(data["discountPercent"])
        else:
            self.discountPercent: Decimal = None
        if "discountDueDays" in data:
            self.discountDueDays: float = float(data["discountDueDays"])
        else:
            self.discountDueDays: float = None
        if "netDueDays" in data:
            self.netDueDays: float = float(data["netDueDays"])
        else:
            self.netDueDays: float = None


class CreditNoteDetails:
    """
    References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "referenceInvoiceNumber" in data:
            self.referenceInvoiceNumber: str = str(data["referenceInvoiceNumber"])
        else:
            self.referenceInvoiceNumber: str = None
        if "debitNoteNumber" in data:
            self.debitNoteNumber: str = str(data["debitNoteNumber"])
        else:
            self.debitNoteNumber: str = None
        if "returnsReferenceNumber" in data:
            self.returnsReferenceNumber: str = str(data["returnsReferenceNumber"])
        else:
            self.returnsReferenceNumber: str = None
        if "goodsReturnDate" in data:
            self.goodsReturnDate: DateTime = DateTime(data["goodsReturnDate"])
        else:
            self.goodsReturnDate: DateTime = None
        if "rmaId" in data:
            self.rmaId: str = str(data["rmaId"])
        else:
            self.rmaId: str = None
        if "coopReferenceNumber" in data:
            self.coopReferenceNumber: str = str(data["coopReferenceNumber"])
        else:
            self.coopReferenceNumber: str = None
        if "consignorsReferenceNumber" in data:
            self.consignorsReferenceNumber: str = str(data["consignorsReferenceNumber"])
        else:
            self.consignorsReferenceNumber: str = None


class ItemQuantity:
    """
    Details of quantity.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "amount" in data:
            self.amount: int = int(data["amount"])
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = str(data["unitOfMeasure"])
        else:
            self.unitOfMeasure: str = None
        if "unitSize" in data:
            self.unitSize: int = int(data["unitSize"])
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
    """
        Submit new invoices to Amazon.
    **Usage Plans:**
    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |
    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def submitInvoices(
        self,
        data: SubmitInvoicesRequest,
    ):
        url = "/vendor/payments/v1/invoices".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            202: SubmitInvoicesResponse,
            400: SubmitInvoicesResponse,
            403: SubmitInvoicesResponse,
            404: SubmitInvoicesResponse,
            413: SubmitInvoicesResponse,
            415: SubmitInvoicesResponse,
            429: SubmitInvoicesResponse,
            500: SubmitInvoicesResponse,
            503: SubmitInvoicesResponse,
        }[response.status_code](self._get_response_json(response))
