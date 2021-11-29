from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class SubmitInvoiceRequest(__BaseDictObject):
    """
    The request schema for the submitInvoice operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "invoices" in data:
            self.invoices: _List[InvoiceDetail] = [InvoiceDetail(datum) for datum in data["invoices"]]
        else:
            self.invoices: _List[InvoiceDetail] = []


class InvoiceDetail(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "invoiceNumber" in data:
            self.invoiceNumber: str = self._get_value(str, "invoiceNumber")
        else:
            self.invoiceNumber: str = None
        if "invoiceDate" in data:
            self.invoiceDate: str = self._get_value(str, "invoiceDate")
        else:
            self.invoiceDate: str = None
        if "referenceNumber" in data:
            self.referenceNumber: str = self._get_value(str, "referenceNumber")
        else:
            self.referenceNumber: str = None
        if "remitToParty" in data:
            self.remitToParty: PartyIdentification = self._get_value(PartyIdentification, "remitToParty")
        else:
            self.remitToParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = self._get_value(PartyIdentification, "billToParty")
        else:
            self.billToParty: PartyIdentification = None
        if "shipToCountryCode" in data:
            self.shipToCountryCode: str = self._get_value(str, "shipToCountryCode")
        else:
            self.shipToCountryCode: str = None
        if "paymentTermsCode" in data:
            self.paymentTermsCode: str = self._get_value(str, "paymentTermsCode")
        else:
            self.paymentTermsCode: str = None
        if "invoiceTotal" in data:
            self.invoiceTotal: Money = self._get_value(Money, "invoiceTotal")
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


class InvoiceItem(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = self._get_value(str, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: str = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = self._get_value(str, "buyerProductIdentifier")
        else:
            self.buyerProductIdentifier: str = None
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
        if "vendorOrderNumber" in data:
            self.vendorOrderNumber: str = self._get_value(str, "vendorOrderNumber")
        else:
            self.vendorOrderNumber: str = None
        if "hsnCode" in data:
            self.hsnCode: str = self._get_value(str, "hsnCode")
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
            self.taxRegistrationDetails: _List[TaxRegistrationDetail] = [
                TaxRegistrationDetail(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetail] = []


class TaxRegistrationDetail(__BaseDictObject):
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
        if "taxRegistrationAddress" in data:
            self.taxRegistrationAddress: Address = self._get_value(Address, "taxRegistrationAddress")
        else:
            self.taxRegistrationAddress: Address = None
        if "taxRegistrationMessage" in data:
            self.taxRegistrationMessage: str = self._get_value(str, "taxRegistrationMessage")
        else:
            self.taxRegistrationMessage: str = None


class Address(__BaseDictObject):
    """
    Address of the party.
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
        if "postalCode" in data:
            self.postalCode: str = self._get_value(str, "postalCode")
        else:
            self.postalCode: str = None
        if "countryCode" in data:
            self.countryCode: str = self._get_value(str, "countryCode")
        else:
            self.countryCode: str = None
        if "phone" in data:
            self.phone: str = self._get_value(str, "phone")
        else:
            self.phone: str = None


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


class TaxDetail(__BaseDictObject):
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
        if "chargeAmount" in data:
            self.chargeAmount: Money = self._get_value(Money, "chargeAmount")
        else:
            self.chargeAmount: Money = None
        if "taxDetails" in data:
            self.taxDetails: _List[TaxDetail] = [TaxDetail(datum) for datum in data["taxDetails"]]
        else:
            self.taxDetails: _List[TaxDetail] = []


class AdditionalDetails(__BaseDictObject):
    """
    A field where selling party can provide additional information for tax related or any other purposes.
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


class ItemQuantity(__BaseDictObject):
    """
    Details of item quantity.
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


class SubmitInvoiceResponse(__BaseDictObject):
    """
    The response schema for the submitInvoice operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: TransactionReference = self._get_value(TransactionReference, "payload")
        else:
            self.payload: TransactionReference = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class TransactionReference(__BaseDictObject):
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
    def submitInvoice(
        self,
        data: SubmitInvoiceRequest,
    ):
        """
                Submits one or more invoices for a vendor's direct fulfillment orders.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/vendor/directFulfillment/payments/v1/invoices"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: SubmitInvoiceResponse,
            400: SubmitInvoiceResponse,
            403: SubmitInvoiceResponse,
            404: SubmitInvoiceResponse,
            413: SubmitInvoiceResponse,
            415: SubmitInvoiceResponse,
            429: SubmitInvoiceResponse,
            500: SubmitInvoiceResponse,
            503: SubmitInvoiceResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
