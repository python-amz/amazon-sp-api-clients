from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "invoices" in data:
            self.invoices: _List[InvoiceDetail] = [InvoiceDetail(datum) for datum in data["invoices"]]
        else:
            self.invoices: _List[InvoiceDetail] = []


class InvoiceDetail:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "invoiceNumber" in data:
            self.invoiceNumber: str = str(data["invoiceNumber"])
        else:
            self.invoiceNumber: str = None
        if "invoiceDate" in data:
            self.invoiceDate: str = str(data["invoiceDate"])
        else:
            self.invoiceDate: str = None
        if "referenceNumber" in data:
            self.referenceNumber: str = str(data["referenceNumber"])
        else:
            self.referenceNumber: str = None
        if "remitToParty" in data:
            self.remitToParty: PartyIdentification = PartyIdentification(data["remitToParty"])
        else:
            self.remitToParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = PartyIdentification(data["billToParty"])
        else:
            self.billToParty: PartyIdentification = None
        if "shipToCountryCode" in data:
            self.shipToCountryCode: str = str(data["shipToCountryCode"])
        else:
            self.shipToCountryCode: str = None
        if "paymentTermsCode" in data:
            self.paymentTermsCode: str = str(data["paymentTermsCode"])
        else:
            self.paymentTermsCode: str = None
        if "invoiceTotal" in data:
            self.invoiceTotal: Money = Money(data["invoiceTotal"])
        else:
            self.invoiceTotal: Money = None
        if "taxTotals" in data:
            self.taxTotals: _List[TaxDetail] = [TaxDetail(datum) for datum in data["taxTotals"]]
        else:
            self.taxTotals: _List[TaxDetail] = []
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
        if "items" in data:
            self.items: _List[InvoiceItem] = [InvoiceItem(datum) for datum in data["items"]]
        else:
            self.items: _List[InvoiceItem] = []


class InvoiceItem:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = str(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: str = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = str(data["buyerProductIdentifier"])
        else:
            self.buyerProductIdentifier: str = None
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
        if "vendorOrderNumber" in data:
            self.vendorOrderNumber: str = str(data["vendorOrderNumber"])
        else:
            self.vendorOrderNumber: str = None
        if "hsnCode" in data:
            self.hsnCode: str = str(data["hsnCode"])
        else:
            self.hsnCode: str = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetail] = [TaxDetail(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetail] = []
        if "chargeDetails" in data:
            self.chargeDetails: _List[ChargeDetails] = [ChargeDetails(datum) for datum in data["chargeDetails"]]
        else:
            self.chargeDetails: _List[ChargeDetails] = []


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
            self.taxRegistrationDetails: _List[TaxRegistrationDetail] = [
                TaxRegistrationDetail(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetail] = []


class TaxRegistrationDetail:
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
        if "taxRegistrationAddress" in data:
            self.taxRegistrationAddress: Address = Address(data["taxRegistrationAddress"])
        else:
            self.taxRegistrationAddress: Address = None
        if "taxRegistrationMessage" in data:
            self.taxRegistrationMessage: str = str(data["taxRegistrationMessage"])
        else:
            self.taxRegistrationMessage: str = None


class Address:
    """
    Address of the party.
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
        if "postalCode" in data:
            self.postalCode: str = str(data["postalCode"])
        else:
            self.postalCode: str = None
        if "countryCode" in data:
            self.countryCode: str = str(data["countryCode"])
        else:
            self.countryCode: str = None
        if "phone" in data:
            self.phone: str = str(data["phone"])
        else:
            self.phone: str = None


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


class TaxDetail:
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
        if "chargeAmount" in data:
            self.chargeAmount: Money = Money(data["chargeAmount"])
        else:
            self.chargeAmount: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetail] = [TaxDetail(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetail] = []


class AdditionalDetails:
    """
    A field where selling party can provide additional information for tax related or any other purposes.
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


class ItemQuantity:
    """
    Details of item quantity.
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


class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: TransactionReference = TransactionReference(data["payload"])
        else:
            self.payload: TransactionReference = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class TransactionReference:
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


class VendorDirectFulfillmentPaymentsV1Client(__BaseClient):
    """
        Submits one or more invoices for a vendor's direct fulfillment orders.
    **Usage Plans:**
    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |
    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def submitInvoice(
        self,
        data: SubmitInvoiceRequest,
    ):
        url = "/vendor/directFulfillment/payments/v1/invoices".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: SubmitInvoiceResponse,
            400: SubmitInvoiceResponse,
            403: SubmitInvoiceResponse,
            404: SubmitInvoiceResponse,
            413: SubmitInvoiceResponse,
            415: SubmitInvoiceResponse,
            429: SubmitInvoiceResponse,
            500: SubmitInvoiceResponse,
            503: SubmitInvoiceResponse,
        }[response.status_code](self._get_response_json(response))
