from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetShipmentDetailsResponse(__BaseDictObject):
    """
    The response schema for the getShipmentDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ShipmentDetail = self._get_value(ShipmentDetail, "payload")
        else:
            self.payload: ShipmentDetail = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ShipmentDetail(__BaseDictObject):
    """
    The information required by a selling partner to issue a shipment invoice.
    """

    def __init__(self, data):
        super().__init__(data)
        if "WarehouseId" in data:
            self.WarehouseId: str = self._get_value(str, "WarehouseId")
        else:
            self.WarehouseId: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "AmazonShipmentId" in data:
            self.AmazonShipmentId: str = self._get_value(str, "AmazonShipmentId")
        else:
            self.AmazonShipmentId: str = None
        if "PurchaseDate" in data:
            self.PurchaseDate: str = self._get_value(str, "PurchaseDate")
        else:
            self.PurchaseDate: str = None
        if "ShippingAddress" in data:
            self.ShippingAddress: Address = self._get_value(Address, "ShippingAddress")
        else:
            self.ShippingAddress: Address = None
        if "PaymentMethodDetails" in data:
            self.PaymentMethodDetails: PaymentMethodDetailItemList = self._get_value(
                PaymentMethodDetailItemList, "PaymentMethodDetails"
            )
        else:
            self.PaymentMethodDetails: PaymentMethodDetailItemList = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = self._get_value(str, "SellerId")
        else:
            self.SellerId: str = None
        if "BuyerName" in data:
            self.BuyerName: str = self._get_value(str, "BuyerName")
        else:
            self.BuyerName: str = None
        if "BuyerCounty" in data:
            self.BuyerCounty: str = self._get_value(str, "BuyerCounty")
        else:
            self.BuyerCounty: str = None
        if "BuyerTaxInfo" in data:
            self.BuyerTaxInfo: BuyerTaxInfo = self._get_value(BuyerTaxInfo, "BuyerTaxInfo")
        else:
            self.BuyerTaxInfo: BuyerTaxInfo = None
        if "MarketplaceTaxInfo" in data:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = self._get_value(MarketplaceTaxInfo, "MarketplaceTaxInfo")
        else:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = None
        if "SellerDisplayName" in data:
            self.SellerDisplayName: str = self._get_value(str, "SellerDisplayName")
        else:
            self.SellerDisplayName: str = None
        if "ShipmentItems" in data:
            self.ShipmentItems: ShipmentItems = self._get_value(ShipmentItems, "ShipmentItems")
        else:
            self.ShipmentItems: ShipmentItems = None


class Address(__BaseDictObject):
    """
    The shipping address details of the shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Name" in data:
            self.Name: str = self._get_value(str, "Name")
        else:
            self.Name: str = None
        if "AddressLine1" in data:
            self.AddressLine1: str = self._get_value(str, "AddressLine1")
        else:
            self.AddressLine1: str = None
        if "AddressLine2" in data:
            self.AddressLine2: str = self._get_value(str, "AddressLine2")
        else:
            self.AddressLine2: str = None
        if "AddressLine3" in data:
            self.AddressLine3: str = self._get_value(str, "AddressLine3")
        else:
            self.AddressLine3: str = None
        if "City" in data:
            self.City: str = self._get_value(str, "City")
        else:
            self.City: str = None
        if "County" in data:
            self.County: str = self._get_value(str, "County")
        else:
            self.County: str = None
        if "District" in data:
            self.District: str = self._get_value(str, "District")
        else:
            self.District: str = None
        if "StateOrRegion" in data:
            self.StateOrRegion: str = self._get_value(str, "StateOrRegion")
        else:
            self.StateOrRegion: str = None
        if "PostalCode" in data:
            self.PostalCode: str = self._get_value(str, "PostalCode")
        else:
            self.PostalCode: str = None
        if "CountryCode" in data:
            self.CountryCode: str = self._get_value(str, "CountryCode")
        else:
            self.CountryCode: str = None
        if "Phone" in data:
            self.Phone: str = self._get_value(str, "Phone")
        else:
            self.Phone: str = None
        if "AddressType" in data:
            self.AddressType: AddressTypeEnum = self._get_value(AddressTypeEnum, "AddressType")
        else:
            self.AddressType: AddressTypeEnum = None


class BuyerTaxInfo(__BaseDictObject):
    """
    Tax information about the buyer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CompanyLegalName" in data:
            self.CompanyLegalName: str = self._get_value(str, "CompanyLegalName")
        else:
            self.CompanyLegalName: str = None
        if "TaxingRegion" in data:
            self.TaxingRegion: str = self._get_value(str, "TaxingRegion")
        else:
            self.TaxingRegion: str = None
        if "TaxClassifications" in data:
            self.TaxClassifications: TaxClassificationList = self._get_value(
                TaxClassificationList, "TaxClassifications"
            )
        else:
            self.TaxClassifications: TaxClassificationList = None


class MarketplaceTaxInfo(__BaseDictObject):
    """
    Tax information about the marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CompanyLegalName" in data:
            self.CompanyLegalName: str = self._get_value(str, "CompanyLegalName")
        else:
            self.CompanyLegalName: str = None
        if "TaxingRegion" in data:
            self.TaxingRegion: str = self._get_value(str, "TaxingRegion")
        else:
            self.TaxingRegion: str = None
        if "TaxClassifications" in data:
            self.TaxClassifications: TaxClassificationList = self._get_value(
                TaxClassificationList, "TaxClassifications"
            )
        else:
            self.TaxClassifications: TaxClassificationList = None


class TaxClassification(__BaseDictObject):
    """
    The tax classification for the entity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Name" in data:
            self.Name: str = self._get_value(str, "Name")
        else:
            self.Name: str = None
        if "Value" in data:
            self.Value: str = self._get_value(str, "Value")
        else:
            self.Value: str = None


class ShipmentItem(__BaseDictObject):
    """
    The shipment item information required by a seller to issue a shipment invoice.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "OrderItemId" in data:
            self.OrderItemId: str = self._get_value(str, "OrderItemId")
        else:
            self.OrderItemId: str = None
        if "Title" in data:
            self.Title: str = self._get_value(str, "Title")
        else:
            self.Title: str = None
        if "QuantityOrdered" in data:
            self.QuantityOrdered: float = self._get_value(float, "QuantityOrdered")
        else:
            self.QuantityOrdered: float = None
        if "ItemPrice" in data:
            self.ItemPrice: Money = self._get_value(Money, "ItemPrice")
        else:
            self.ItemPrice: Money = None
        if "ShippingPrice" in data:
            self.ShippingPrice: Money = self._get_value(Money, "ShippingPrice")
        else:
            self.ShippingPrice: Money = None
        if "GiftWrapPrice" in data:
            self.GiftWrapPrice: Money = self._get_value(Money, "GiftWrapPrice")
        else:
            self.GiftWrapPrice: Money = None
        if "ShippingDiscount" in data:
            self.ShippingDiscount: Money = self._get_value(Money, "ShippingDiscount")
        else:
            self.ShippingDiscount: Money = None
        if "PromotionDiscount" in data:
            self.PromotionDiscount: Money = self._get_value(Money, "PromotionDiscount")
        else:
            self.PromotionDiscount: Money = None
        if "SerialNumbers" in data:
            self.SerialNumbers: SerialNumbersList = self._get_value(SerialNumbersList, "SerialNumbers")
        else:
            self.SerialNumbers: SerialNumbersList = None


class Money(__BaseDictObject):
    """
    The currency type and amount.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: str = self._get_value(str, "Amount")
        else:
            self.Amount: str = None


class Error(__BaseDictObject):
    """
    An error response returned when the request is unsuccessful.
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


class SubmitInvoiceRequest(__BaseDictObject):
    """
    The request schema for the submitInvoice operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "InvoiceContent" in data:
            self.InvoiceContent: Blob = self._get_value(Blob, "InvoiceContent")
        else:
            self.InvoiceContent: Blob = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "ContentMD5Value" in data:
            self.ContentMD5Value: str = self._get_value(str, "ContentMD5Value")
        else:
            self.ContentMD5Value: str = None


class SubmitInvoiceResponse(__BaseDictObject):
    """
    The response schema for the submitInvoice operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ShipmentInvoiceStatusInfo(__BaseDictObject):
    """
    The shipment invoice status information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonShipmentId" in data:
            self.AmazonShipmentId: str = self._get_value(str, "AmazonShipmentId")
        else:
            self.AmazonShipmentId: str = None
        if "InvoiceStatus" in data:
            self.InvoiceStatus: ShipmentInvoiceStatus = self._get_value(ShipmentInvoiceStatus, "InvoiceStatus")
        else:
            self.InvoiceStatus: ShipmentInvoiceStatus = None


class ShipmentInvoiceStatusResponse(__BaseDictObject):
    """
    The shipment invoice status response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Shipments" in data:
            self.Shipments: ShipmentInvoiceStatusInfo = self._get_value(ShipmentInvoiceStatusInfo, "Shipments")
        else:
            self.Shipments: ShipmentInvoiceStatusInfo = None


class GetInvoiceStatusResponse(__BaseDictObject):
    """
    The response schema for the getInvoiceStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ShipmentInvoiceStatusResponse = self._get_value(ShipmentInvoiceStatusResponse, "payload")
        else:
            self.payload: ShipmentInvoiceStatusResponse = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class PaymentMethodDetailItemList(list, _List["str"]):
    """
    The list of payment method details.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class TaxClassificationList(list, _List["TaxClassification"]):
    """
    The list of tax classifications.
    """

    def __init__(self, data):
        super().__init__([TaxClassification(datum) for datum in data])
        self.data = data


class ShipmentItems(list, _List["ShipmentItem"]):
    """
    A list of shipment items.
    """

    def __init__(self, data):
        super().__init__([ShipmentItem(datum) for datum in data])
        self.data = data


class SerialNumbersList(list, _List["str"]):
    """
    The list of serial numbers.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class AddressTypeEnum(str):
    """
    The shipping address type.
    """


class Blob(str):
    """
    Shipment invoice document content.
    """


class ShipmentInvoiceStatus(str):
    """
    The shipment invoice status.
    """


class ShipmentInvoicingV0Client(__BaseClient):
    def getShipmentDetails(
        self,
        shipmentId: str,
    ):
        """
                Returns the shipment details required to issue an invoice for the specified shipment.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/outbound/brazil/v0/shipments/{shipmentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetShipmentDetailsResponse,
            400: GetShipmentDetailsResponse,
            401: GetShipmentDetailsResponse,
            403: GetShipmentDetailsResponse,
            404: GetShipmentDetailsResponse,
            415: GetShipmentDetailsResponse,
            429: GetShipmentDetailsResponse,
            500: GetShipmentDetailsResponse,
            503: GetShipmentDetailsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def submitInvoice(
        self,
        data: SubmitInvoiceRequest,
        shipmentId: str,
    ):
        """
                Submits a shipment invoice document for a given shipment.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: SubmitInvoiceResponse,
            400: SubmitInvoiceResponse,
            401: SubmitInvoiceResponse,
            403: SubmitInvoiceResponse,
            404: SubmitInvoiceResponse,
            415: SubmitInvoiceResponse,
            429: SubmitInvoiceResponse,
            500: SubmitInvoiceResponse,
            503: SubmitInvoiceResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getInvoiceStatus(
        self,
        shipmentId: str,
    ):
        """
                Returns the invoice status for the shipment you specify.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetInvoiceStatusResponse,
            400: GetInvoiceStatusResponse,
            401: GetInvoiceStatusResponse,
            403: GetInvoiceStatusResponse,
            404: GetInvoiceStatusResponse,
            415: GetInvoiceStatusResponse,
            429: GetInvoiceStatusResponse,
            500: GetInvoiceStatusResponse,
            503: GetInvoiceStatusResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
