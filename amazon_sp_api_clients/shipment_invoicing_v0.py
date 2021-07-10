from .base import BaseClient as __BaseClient
from typing import List as _List


class GetShipmentDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ShipmentDetail = ShipmentDetail(data["payload"])
        else:
            self.payload: ShipmentDetail = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ShipmentDetail:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "WarehouseId" in data:
            self.WarehouseId: str = str(data["WarehouseId"])
        else:
            self.WarehouseId: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "AmazonShipmentId" in data:
            self.AmazonShipmentId: str = str(data["AmazonShipmentId"])
        else:
            self.AmazonShipmentId: str = None
        if "PurchaseDate" in data:
            self.PurchaseDate: str = str(data["PurchaseDate"])
        else:
            self.PurchaseDate: str = None
        if "ShippingAddress" in data:
            self.ShippingAddress: Address = Address(data["ShippingAddress"])
        else:
            self.ShippingAddress: Address = None
        if "PaymentMethodDetails" in data:
            self.PaymentMethodDetails: PaymentMethodDetailItemList = PaymentMethodDetailItemList(
                data["PaymentMethodDetails"]
            )
        else:
            self.PaymentMethodDetails: PaymentMethodDetailItemList = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "BuyerName" in data:
            self.BuyerName: str = str(data["BuyerName"])
        else:
            self.BuyerName: str = None
        if "BuyerCounty" in data:
            self.BuyerCounty: str = str(data["BuyerCounty"])
        else:
            self.BuyerCounty: str = None
        if "BuyerTaxInfo" in data:
            self.BuyerTaxInfo: BuyerTaxInfo = BuyerTaxInfo(data["BuyerTaxInfo"])
        else:
            self.BuyerTaxInfo: BuyerTaxInfo = None
        if "MarketplaceTaxInfo" in data:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = MarketplaceTaxInfo(data["MarketplaceTaxInfo"])
        else:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = None
        if "SellerDisplayName" in data:
            self.SellerDisplayName: str = str(data["SellerDisplayName"])
        else:
            self.SellerDisplayName: str = None
        if "ShipmentItems" in data:
            self.ShipmentItems: ShipmentItems = ShipmentItems(data["ShipmentItems"])
        else:
            self.ShipmentItems: ShipmentItems = None


class Address:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Name" in data:
            self.Name: str = str(data["Name"])
        else:
            self.Name: str = None
        if "AddressLine1" in data:
            self.AddressLine1: str = str(data["AddressLine1"])
        else:
            self.AddressLine1: str = None
        if "AddressLine2" in data:
            self.AddressLine2: str = str(data["AddressLine2"])
        else:
            self.AddressLine2: str = None
        if "AddressLine3" in data:
            self.AddressLine3: str = str(data["AddressLine3"])
        else:
            self.AddressLine3: str = None
        if "City" in data:
            self.City: str = str(data["City"])
        else:
            self.City: str = None
        if "County" in data:
            self.County: str = str(data["County"])
        else:
            self.County: str = None
        if "District" in data:
            self.District: str = str(data["District"])
        else:
            self.District: str = None
        if "StateOrRegion" in data:
            self.StateOrRegion: str = str(data["StateOrRegion"])
        else:
            self.StateOrRegion: str = None
        if "PostalCode" in data:
            self.PostalCode: str = str(data["PostalCode"])
        else:
            self.PostalCode: str = None
        if "CountryCode" in data:
            self.CountryCode: str = str(data["CountryCode"])
        else:
            self.CountryCode: str = None
        if "Phone" in data:
            self.Phone: str = str(data["Phone"])
        else:
            self.Phone: str = None
        if "AddressType" in data:
            self.AddressType: AddressTypeEnum = AddressTypeEnum(data["AddressType"])
        else:
            self.AddressType: AddressTypeEnum = None


class BuyerTaxInfo:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CompanyLegalName" in data:
            self.CompanyLegalName: str = str(data["CompanyLegalName"])
        else:
            self.CompanyLegalName: str = None
        if "TaxingRegion" in data:
            self.TaxingRegion: str = str(data["TaxingRegion"])
        else:
            self.TaxingRegion: str = None
        if "TaxClassifications" in data:
            self.TaxClassifications: TaxClassificationList = TaxClassificationList(data["TaxClassifications"])
        else:
            self.TaxClassifications: TaxClassificationList = None


class MarketplaceTaxInfo:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CompanyLegalName" in data:
            self.CompanyLegalName: str = str(data["CompanyLegalName"])
        else:
            self.CompanyLegalName: str = None
        if "TaxingRegion" in data:
            self.TaxingRegion: str = str(data["TaxingRegion"])
        else:
            self.TaxingRegion: str = None
        if "TaxClassifications" in data:
            self.TaxClassifications: TaxClassificationList = TaxClassificationList(data["TaxClassifications"])
        else:
            self.TaxClassifications: TaxClassificationList = None


class TaxClassification:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Name" in data:
            self.Name: str = str(data["Name"])
        else:
            self.Name: str = None
        if "Value" in data:
            self.Value: str = str(data["Value"])
        else:
            self.Value: str = None


class ShipmentItem:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "OrderItemId" in data:
            self.OrderItemId: str = str(data["OrderItemId"])
        else:
            self.OrderItemId: str = None
        if "Title" in data:
            self.Title: str = str(data["Title"])
        else:
            self.Title: str = None
        if "QuantityOrdered" in data:
            self.QuantityOrdered: float = float(data["QuantityOrdered"])
        else:
            self.QuantityOrdered: float = None
        if "ItemPrice" in data:
            self.ItemPrice: Money = Money(data["ItemPrice"])
        else:
            self.ItemPrice: Money = None
        if "ShippingPrice" in data:
            self.ShippingPrice: Money = Money(data["ShippingPrice"])
        else:
            self.ShippingPrice: Money = None
        if "GiftWrapPrice" in data:
            self.GiftWrapPrice: Money = Money(data["GiftWrapPrice"])
        else:
            self.GiftWrapPrice: Money = None
        if "ShippingDiscount" in data:
            self.ShippingDiscount: Money = Money(data["ShippingDiscount"])
        else:
            self.ShippingDiscount: Money = None
        if "PromotionDiscount" in data:
            self.PromotionDiscount: Money = Money(data["PromotionDiscount"])
        else:
            self.PromotionDiscount: Money = None
        if "SerialNumbers" in data:
            self.SerialNumbers: SerialNumbersList = SerialNumbersList(data["SerialNumbers"])
        else:
            self.SerialNumbers: SerialNumbersList = None


class Money:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: str = str(data["Amount"])
        else:
            self.Amount: str = None


class Error:
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


class SubmitInvoiceRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "InvoiceContent" in data:
            self.InvoiceContent: Blob = Blob(data["InvoiceContent"])
        else:
            self.InvoiceContent: Blob = None
        if "ContentMD5Value" in data:
            self.ContentMD5Value: str = str(data["ContentMD5Value"])
        else:
            self.ContentMD5Value: str = None


class SubmitInvoiceResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ShipmentInvoiceStatusInfo:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonShipmentId" in data:
            self.AmazonShipmentId: str = str(data["AmazonShipmentId"])
        else:
            self.AmazonShipmentId: str = None
        if "InvoiceStatus" in data:
            self.InvoiceStatus: ShipmentInvoiceStatus = ShipmentInvoiceStatus(data["InvoiceStatus"])
        else:
            self.InvoiceStatus: ShipmentInvoiceStatus = None


class ShipmentInvoiceStatusResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Shipments" in data:
            self.Shipments: ShipmentInvoiceStatusInfo = ShipmentInvoiceStatusInfo(data["Shipments"])
        else:
            self.Shipments: ShipmentInvoiceStatusInfo = None


class GetInvoiceStatusResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ShipmentInvoiceStatusResponse = ShipmentInvoiceStatusResponse(data["payload"])
        else:
            self.payload: ShipmentInvoiceStatusResponse = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class PaymentMethodDetailItemList(list, _List["str"]):
    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class TaxClassificationList(list, _List["TaxClassification"]):
    def __init__(self, data):
        super().__init__([TaxClassification(datum) for datum in data])
        self.data = data


class ShipmentItems(list, _List["ShipmentItem"]):
    def __init__(self, data):
        super().__init__([ShipmentItem(datum) for datum in data])
        self.data = data


class SerialNumbersList(list, _List["str"]):
    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class AddressTypeEnum(str):
    pass


class Blob(str):
    pass


class ShipmentInvoiceStatus(str):
    pass


class ShipmentInvoicingV0Client(__BaseClient):
    def getShipmentDetails(
        self,
        shipmentId: str,
    ):
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShipmentDetailsResponse,
            400: GetShipmentDetailsResponse,
            401: GetShipmentDetailsResponse,
            403: GetShipmentDetailsResponse,
            404: GetShipmentDetailsResponse,
            415: GetShipmentDetailsResponse,
            429: GetShipmentDetailsResponse,
            500: GetShipmentDetailsResponse,
            503: GetShipmentDetailsResponse,
        }[response.status_code](response.json())

    def submitInvoice(
        self,
        data: SubmitInvoiceRequest,
        shipmentId: str,
    ):
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            200: SubmitInvoiceResponse,
            400: SubmitInvoiceResponse,
            401: SubmitInvoiceResponse,
            403: SubmitInvoiceResponse,
            404: SubmitInvoiceResponse,
            415: SubmitInvoiceResponse,
            429: SubmitInvoiceResponse,
            500: SubmitInvoiceResponse,
            503: SubmitInvoiceResponse,
        }[response.status_code](response.json())

    def getInvoiceStatus(
        self,
        shipmentId: str,
    ):
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetInvoiceStatusResponse,
            400: GetInvoiceStatusResponse,
            401: GetInvoiceStatusResponse,
            403: GetInvoiceStatusResponse,
            404: GetInvoiceStatusResponse,
            415: GetInvoiceStatusResponse,
            429: GetInvoiceStatusResponse,
            500: GetInvoiceStatusResponse,
            503: GetInvoiceStatusResponse,
        }[response.status_code](response.json())
