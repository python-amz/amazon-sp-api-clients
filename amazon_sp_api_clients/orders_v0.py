from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class UpdateShipmentStatusRequest(__BaseDictObject):
    """
    The request body for the updateShipmentStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "shipmentStatus" in data:
            self.shipmentStatus: ShipmentStatus = self._get_value(ShipmentStatus, "shipmentStatus")
        else:
            self.shipmentStatus: ShipmentStatus = None
        if "orderItems" in data:
            self.orderItems: OrderItems = self._get_value(OrderItems, "orderItems")
        else:
            self.orderItems: OrderItems = None


class UpdateVerificationStatusRequest(__BaseDictObject):
    """
    The request body for the updateVerificationStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "regulatedOrderVerificationStatus" in data:
            self.regulatedOrderVerificationStatus: UpdateVerificationStatusRequestBody = self._get_value(
                UpdateVerificationStatusRequestBody, "regulatedOrderVerificationStatus"
            )
        else:
            self.regulatedOrderVerificationStatus: UpdateVerificationStatusRequestBody = None


class UpdateVerificationStatusRequestBody(__BaseDictObject):
    """
    The updated values of the VerificationStatus field.
    """

    def __init__(self, data):
        super().__init__(data)
        if "status" in data:
            self.status: VerificationStatus = self._get_value(VerificationStatus, "status")
        else:
            self.status: VerificationStatus = None
        if "externalReviewerId" in data:
            self.externalReviewerId: str = self._get_value(str, "externalReviewerId")
        else:
            self.externalReviewerId: str = None
        if "rejectionReasonId" in data:
            self.rejectionReasonId: str = self._get_value(str, "rejectionReasonId")
        else:
            self.rejectionReasonId: str = None


class UpdateShipmentStatusErrorResponse(__BaseDictObject):
    """
    The error response schema for the UpdateShipmentStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class UpdateVerificationStatusErrorResponse(__BaseDictObject):
    """
    The error response schema for the UpdateVerificationStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrdersResponse(__BaseDictObject):
    """
    The response schema for the getOrders operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrdersList = self._get_value(OrdersList, "payload")
        else:
            self.payload: OrdersList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderResponse(__BaseDictObject):
    """
    The response schema for the getOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Order = self._get_value(Order, "payload")
        else:
            self.payload: Order = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderBuyerInfoResponse(__BaseDictObject):
    """
    The response schema for the getOrderBuyerInfo operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderBuyerInfo = self._get_value(OrderBuyerInfo, "payload")
        else:
            self.payload: OrderBuyerInfo = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderRegulatedInfoResponse(__BaseDictObject):
    """
    The response schema for the getOrderRegulatedInfo operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderRegulatedInfo = self._get_value(OrderRegulatedInfo, "payload")
        else:
            self.payload: OrderRegulatedInfo = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderAddressResponse(__BaseDictObject):
    """
    The response schema for the getOrderAddress operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderAddress = self._get_value(OrderAddress, "payload")
        else:
            self.payload: OrderAddress = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderItemsResponse(__BaseDictObject):
    """
    The response schema for the getOrderItems operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderItemsList = self._get_value(OrderItemsList, "payload")
        else:
            self.payload: OrderItemsList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderItemsBuyerInfoResponse(__BaseDictObject):
    """
    The response schema for the getOrderItemsBuyerInfo operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderItemsBuyerInfoList = self._get_value(OrderItemsBuyerInfoList, "payload")
        else:
            self.payload: OrderItemsBuyerInfoList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class OrdersList(__BaseDictObject):
    """
    A list of orders along with additional information to make subsequent API calls.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Orders" in data:
            self.Orders: OrderList = self._get_value(OrderList, "Orders")
        else:
            self.Orders: OrderList = None
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "LastUpdatedBefore" in data:
            self.LastUpdatedBefore: str = self._get_value(str, "LastUpdatedBefore")
        else:
            self.LastUpdatedBefore: str = None
        if "CreatedBefore" in data:
            self.CreatedBefore: str = self._get_value(str, "CreatedBefore")
        else:
            self.CreatedBefore: str = None


class Order(__BaseDictObject):
    """
    Order information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "SellerOrderId" in data:
            self.SellerOrderId: str = self._get_value(str, "SellerOrderId")
        else:
            self.SellerOrderId: str = None
        if "PurchaseDate" in data:
            self.PurchaseDate: str = self._get_value(str, "PurchaseDate")
        else:
            self.PurchaseDate: str = None
        if "LastUpdateDate" in data:
            self.LastUpdateDate: str = self._get_value(str, "LastUpdateDate")
        else:
            self.LastUpdateDate: str = None
        if "OrderStatus" in data:
            self.OrderStatus: str = self._get_value(str, "OrderStatus")
        else:
            self.OrderStatus: str = None
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = self._get_value(str, "FulfillmentChannel")
        else:
            self.FulfillmentChannel: str = None
        if "SalesChannel" in data:
            self.SalesChannel: str = self._get_value(str, "SalesChannel")
        else:
            self.SalesChannel: str = None
        if "OrderChannel" in data:
            self.OrderChannel: str = self._get_value(str, "OrderChannel")
        else:
            self.OrderChannel: str = None
        if "ShipServiceLevel" in data:
            self.ShipServiceLevel: str = self._get_value(str, "ShipServiceLevel")
        else:
            self.ShipServiceLevel: str = None
        if "OrderTotal" in data:
            self.OrderTotal: Money = self._get_value(Money, "OrderTotal")
        else:
            self.OrderTotal: Money = None
        if "NumberOfItemsShipped" in data:
            self.NumberOfItemsShipped: int = self._get_value(int, "NumberOfItemsShipped")
        else:
            self.NumberOfItemsShipped: int = None
        if "NumberOfItemsUnshipped" in data:
            self.NumberOfItemsUnshipped: int = self._get_value(int, "NumberOfItemsUnshipped")
        else:
            self.NumberOfItemsUnshipped: int = None
        if "PaymentExecutionDetail" in data:
            self.PaymentExecutionDetail: PaymentExecutionDetailItemList = self._get_value(
                PaymentExecutionDetailItemList, "PaymentExecutionDetail"
            )
        else:
            self.PaymentExecutionDetail: PaymentExecutionDetailItemList = None
        if "PaymentMethod" in data:
            self.PaymentMethod: str = self._get_value(str, "PaymentMethod")
        else:
            self.PaymentMethod: str = None
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
        if "ShipmentServiceLevelCategory" in data:
            self.ShipmentServiceLevelCategory: str = self._get_value(str, "ShipmentServiceLevelCategory")
        else:
            self.ShipmentServiceLevelCategory: str = None
        if "EasyShipShipmentStatus" in data:
            self.EasyShipShipmentStatus: EasyShipShipmentStatus = self._get_value(
                EasyShipShipmentStatus, "EasyShipShipmentStatus"
            )
        else:
            self.EasyShipShipmentStatus: EasyShipShipmentStatus = None
        if "CbaDisplayableShippingLabel" in data:
            self.CbaDisplayableShippingLabel: str = self._get_value(str, "CbaDisplayableShippingLabel")
        else:
            self.CbaDisplayableShippingLabel: str = None
        if "OrderType" in data:
            self.OrderType: str = self._get_value(str, "OrderType")
        else:
            self.OrderType: str = None
        if "EarliestShipDate" in data:
            self.EarliestShipDate: str = self._get_value(str, "EarliestShipDate")
        else:
            self.EarliestShipDate: str = None
        if "LatestShipDate" in data:
            self.LatestShipDate: str = self._get_value(str, "LatestShipDate")
        else:
            self.LatestShipDate: str = None
        if "EarliestDeliveryDate" in data:
            self.EarliestDeliveryDate: str = self._get_value(str, "EarliestDeliveryDate")
        else:
            self.EarliestDeliveryDate: str = None
        if "LatestDeliveryDate" in data:
            self.LatestDeliveryDate: str = self._get_value(str, "LatestDeliveryDate")
        else:
            self.LatestDeliveryDate: str = None
        if "IsBusinessOrder" in data:
            self.IsBusinessOrder: bool = self._get_value(convert_bool, "IsBusinessOrder")
        else:
            self.IsBusinessOrder: bool = None
        if "IsPrime" in data:
            self.IsPrime: bool = self._get_value(convert_bool, "IsPrime")
        else:
            self.IsPrime: bool = None
        if "IsPremiumOrder" in data:
            self.IsPremiumOrder: bool = self._get_value(convert_bool, "IsPremiumOrder")
        else:
            self.IsPremiumOrder: bool = None
        if "IsGlobalExpressEnabled" in data:
            self.IsGlobalExpressEnabled: bool = self._get_value(convert_bool, "IsGlobalExpressEnabled")
        else:
            self.IsGlobalExpressEnabled: bool = None
        if "ReplacedOrderId" in data:
            self.ReplacedOrderId: str = self._get_value(str, "ReplacedOrderId")
        else:
            self.ReplacedOrderId: str = None
        if "IsReplacementOrder" in data:
            self.IsReplacementOrder: bool = self._get_value(convert_bool, "IsReplacementOrder")
        else:
            self.IsReplacementOrder: bool = None
        if "PromiseResponseDueDate" in data:
            self.PromiseResponseDueDate: str = self._get_value(str, "PromiseResponseDueDate")
        else:
            self.PromiseResponseDueDate: str = None
        if "IsEstimatedShipDateSet" in data:
            self.IsEstimatedShipDateSet: bool = self._get_value(convert_bool, "IsEstimatedShipDateSet")
        else:
            self.IsEstimatedShipDateSet: bool = None
        if "IsSoldByAB" in data:
            self.IsSoldByAB: bool = self._get_value(convert_bool, "IsSoldByAB")
        else:
            self.IsSoldByAB: bool = None
        if "IsIBA" in data:
            self.IsIBA: bool = self._get_value(convert_bool, "IsIBA")
        else:
            self.IsIBA: bool = None
        if "DefaultShipFromLocationAddress" in data:
            self.DefaultShipFromLocationAddress: Address = self._get_value(Address, "DefaultShipFromLocationAddress")
        else:
            self.DefaultShipFromLocationAddress: Address = None
        if "BuyerInvoicePreference" in data:
            self.BuyerInvoicePreference: str = self._get_value(str, "BuyerInvoicePreference")
        else:
            self.BuyerInvoicePreference: str = None
        if "BuyerTaxInformation" in data:
            self.BuyerTaxInformation: BuyerTaxInformation = self._get_value(BuyerTaxInformation, "BuyerTaxInformation")
        else:
            self.BuyerTaxInformation: BuyerTaxInformation = None
        if "FulfillmentInstruction" in data:
            self.FulfillmentInstruction: FulfillmentInstruction = self._get_value(
                FulfillmentInstruction, "FulfillmentInstruction"
            )
        else:
            self.FulfillmentInstruction: FulfillmentInstruction = None
        if "IsISPU" in data:
            self.IsISPU: bool = self._get_value(convert_bool, "IsISPU")
        else:
            self.IsISPU: bool = None
        if "IsAccessPointOrder" in data:
            self.IsAccessPointOrder: bool = self._get_value(convert_bool, "IsAccessPointOrder")
        else:
            self.IsAccessPointOrder: bool = None
        if "MarketplaceTaxInfo" in data:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = self._get_value(MarketplaceTaxInfo, "MarketplaceTaxInfo")
        else:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = None
        if "SellerDisplayName" in data:
            self.SellerDisplayName: str = self._get_value(str, "SellerDisplayName")
        else:
            self.SellerDisplayName: str = None
        if "ShippingAddress" in data:
            self.ShippingAddress: Address = self._get_value(Address, "ShippingAddress")
        else:
            self.ShippingAddress: Address = None
        if "BuyerInfo" in data:
            self.BuyerInfo: BuyerInfo = self._get_value(BuyerInfo, "BuyerInfo")
        else:
            self.BuyerInfo: BuyerInfo = None
        if "AutomatedShippingSettings" in data:
            self.AutomatedShippingSettings: AutomatedShippingSettings = self._get_value(
                AutomatedShippingSettings, "AutomatedShippingSettings"
            )
        else:
            self.AutomatedShippingSettings: AutomatedShippingSettings = None
        if "HasRegulatedItems" in data:
            self.HasRegulatedItems: bool = self._get_value(convert_bool, "HasRegulatedItems")
        else:
            self.HasRegulatedItems: bool = None
        if "ElectronicInvoiceStatus" in data:
            self.ElectronicInvoiceStatus: ElectronicInvoiceStatus = self._get_value(
                ElectronicInvoiceStatus, "ElectronicInvoiceStatus"
            )
        else:
            self.ElectronicInvoiceStatus: ElectronicInvoiceStatus = None


class OrderBuyerInfo(__BaseDictObject):
    """
    Buyer information for an order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "BuyerEmail" in data:
            self.BuyerEmail: str = self._get_value(str, "BuyerEmail")
        else:
            self.BuyerEmail: str = None
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
        if "PurchaseOrderNumber" in data:
            self.PurchaseOrderNumber: str = self._get_value(str, "PurchaseOrderNumber")
        else:
            self.PurchaseOrderNumber: str = None


class OrderRegulatedInfo(__BaseDictObject):
    """
    The order's regulated information along with its verification status.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "RegulatedInformation" in data:
            self.RegulatedInformation: RegulatedInformation = self._get_value(
                RegulatedInformation, "RegulatedInformation"
            )
        else:
            self.RegulatedInformation: RegulatedInformation = None
        if "RequiresDosageLabel" in data:
            self.RequiresDosageLabel: bool = self._get_value(convert_bool, "RequiresDosageLabel")
        else:
            self.RequiresDosageLabel: bool = None
        if "RegulatedOrderVerificationStatus" in data:
            self.RegulatedOrderVerificationStatus: RegulatedOrderVerificationStatus = self._get_value(
                RegulatedOrderVerificationStatus, "RegulatedOrderVerificationStatus"
            )
        else:
            self.RegulatedOrderVerificationStatus: RegulatedOrderVerificationStatus = None


class RegulatedOrderVerificationStatus(__BaseDictObject):
    """
    The verification status of the order along with associated approval or rejection metadata.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Status" in data:
            self.Status: VerificationStatus = self._get_value(VerificationStatus, "Status")
        else:
            self.Status: VerificationStatus = None
        if "RequiresMerchantAction" in data:
            self.RequiresMerchantAction: bool = self._get_value(convert_bool, "RequiresMerchantAction")
        else:
            self.RequiresMerchantAction: bool = None
        if "ValidRejectionReasons" in data:
            self.ValidRejectionReasons: _List[RejectionReason] = [
                RejectionReason(datum) for datum in data["ValidRejectionReasons"]
            ]
        else:
            self.ValidRejectionReasons: _List[RejectionReason] = []
        if "RejectionReason" in data:
            self.RejectionReason: RejectionReason = self._get_value(RejectionReason, "RejectionReason")
        else:
            self.RejectionReason: RejectionReason = None
        if "ReviewDate" in data:
            self.ReviewDate: str = self._get_value(str, "ReviewDate")
        else:
            self.ReviewDate: str = None
        if "ExternalReviewerId" in data:
            self.ExternalReviewerId: str = self._get_value(str, "ExternalReviewerId")
        else:
            self.ExternalReviewerId: str = None


class RejectionReason(__BaseDictObject):
    """
    The reason for rejecting the order's regulated information. Not present if the order isn't rejected.
    """

    def __init__(self, data):
        super().__init__(data)
        if "RejectionReasonId" in data:
            self.RejectionReasonId: str = self._get_value(str, "RejectionReasonId")
        else:
            self.RejectionReasonId: str = None
        if "RejectionReasonDescription" in data:
            self.RejectionReasonDescription: str = self._get_value(str, "RejectionReasonDescription")
        else:
            self.RejectionReasonDescription: str = None


class RegulatedInformation(__BaseDictObject):
    """
    The regulated information collected during purchase and used to verify the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Fields" in data:
            self.Fields: _List[RegulatedInformationField] = [
                RegulatedInformationField(datum) for datum in data["Fields"]
            ]
        else:
            self.Fields: _List[RegulatedInformationField] = []


class RegulatedInformationField(__BaseDictObject):
    """
    A field collected from the regulatory form.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FieldId" in data:
            self.FieldId: str = self._get_value(str, "FieldId")
        else:
            self.FieldId: str = None
        if "FieldLabel" in data:
            self.FieldLabel: str = self._get_value(str, "FieldLabel")
        else:
            self.FieldLabel: str = None
        if "FieldType" in data:
            self.FieldType: str = self._get_value(str, "FieldType")
        else:
            self.FieldType: str = None
        if "FieldValue" in data:
            self.FieldValue: str = self._get_value(str, "FieldValue")
        else:
            self.FieldValue: str = None


class OrderAddress(__BaseDictObject):
    """
    The shipping address for the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "BuyerCompanyName" in data:
            self.BuyerCompanyName: str = self._get_value(str, "BuyerCompanyName")
        else:
            self.BuyerCompanyName: str = None
        if "ShippingAddress" in data:
            self.ShippingAddress: Address = self._get_value(Address, "ShippingAddress")
        else:
            self.ShippingAddress: Address = None
        if "DeliveryPreferences" in data:
            self.DeliveryPreferences: DeliveryPreferences = self._get_value(DeliveryPreferences, "DeliveryPreferences")
        else:
            self.DeliveryPreferences: DeliveryPreferences = None


class Address(__BaseDictObject):
    """
    The shipping address for the order.
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
        if "Municipality" in data:
            self.Municipality: str = self._get_value(str, "Municipality")
        else:
            self.Municipality: str = None
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
            self.AddressType: str = self._get_value(str, "AddressType")
        else:
            self.AddressType: str = None


class DeliveryPreferences(__BaseDictObject):
    """
    Contains all of the delivery instructions provided by the customer for the shipping address.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DropOffLocation" in data:
            self.DropOffLocation: str = self._get_value(str, "DropOffLocation")
        else:
            self.DropOffLocation: str = None
        if "PreferredDeliveryTime" in data:
            self.PreferredDeliveryTime: PreferredDeliveryTime = self._get_value(
                PreferredDeliveryTime, "PreferredDeliveryTime"
            )
        else:
            self.PreferredDeliveryTime: PreferredDeliveryTime = None
        if "OtherAttributes" in data:
            self.OtherAttributes: _List[OtherDeliveryAttributes] = [
                OtherDeliveryAttributes(datum) for datum in data["OtherAttributes"]
            ]
        else:
            self.OtherAttributes: _List[OtherDeliveryAttributes] = []
        if "AddressInstructions" in data:
            self.AddressInstructions: str = self._get_value(str, "AddressInstructions")
        else:
            self.AddressInstructions: str = None


class PreferredDeliveryTime(__BaseDictObject):
    """
    The time window when the delivery is preferred.
    """

    def __init__(self, data):
        super().__init__(data)
        if "BusinessHours" in data:
            self.BusinessHours: _List[BusinessHours] = [BusinessHours(datum) for datum in data["BusinessHours"]]
        else:
            self.BusinessHours: _List[BusinessHours] = []
        if "ExceptionDates" in data:
            self.ExceptionDates: _List[ExceptionDates] = [ExceptionDates(datum) for datum in data["ExceptionDates"]]
        else:
            self.ExceptionDates: _List[ExceptionDates] = []


class BusinessHours(__BaseDictObject):
    """
    Business days and hours when the destination is open for deliveries.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DayOfWeek" in data:
            self.DayOfWeek: str = self._get_value(str, "DayOfWeek")
        else:
            self.DayOfWeek: str = None
        if "OpenIntervals" in data:
            self.OpenIntervals: _List[OpenInterval] = [OpenInterval(datum) for datum in data["OpenIntervals"]]
        else:
            self.OpenIntervals: _List[OpenInterval] = []


class ExceptionDates(__BaseDictObject):
    """
    Dates when the business is closed or open with a different time window.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ExceptionDate" in data:
            self.ExceptionDate: str = self._get_value(str, "ExceptionDate")
        else:
            self.ExceptionDate: str = None
        if "IsOpen" in data:
            self.IsOpen: bool = self._get_value(convert_bool, "IsOpen")
        else:
            self.IsOpen: bool = None
        if "OpenIntervals" in data:
            self.OpenIntervals: _List[OpenInterval] = [OpenInterval(datum) for datum in data["OpenIntervals"]]
        else:
            self.OpenIntervals: _List[OpenInterval] = []


class OpenInterval(__BaseDictObject):
    """
    The time interval for which the business is open.
    """

    def __init__(self, data):
        super().__init__(data)
        if "StartTime" in data:
            self.StartTime: OpenTimeInterval = self._get_value(OpenTimeInterval, "StartTime")
        else:
            self.StartTime: OpenTimeInterval = None
        if "EndTime" in data:
            self.EndTime: OpenTimeInterval = self._get_value(OpenTimeInterval, "EndTime")
        else:
            self.EndTime: OpenTimeInterval = None


class OpenTimeInterval(__BaseDictObject):
    """
    The time when the business opens or closes.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Hour" in data:
            self.Hour: int = self._get_value(int, "Hour")
        else:
            self.Hour: int = None
        if "Minute" in data:
            self.Minute: int = self._get_value(int, "Minute")
        else:
            self.Minute: int = None


class Money(__BaseDictObject):
    """
    The monetary value of the order.
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


class PaymentExecutionDetailItem(__BaseDictObject):
    """
    Information about a sub-payment method used to pay for a COD order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Payment" in data:
            self.Payment: Money = self._get_value(Money, "Payment")
        else:
            self.Payment: Money = None
        if "PaymentMethod" in data:
            self.PaymentMethod: str = self._get_value(str, "PaymentMethod")
        else:
            self.PaymentMethod: str = None


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
            self.TaxClassifications: _List[TaxClassification] = [
                TaxClassification(datum) for datum in data["TaxClassifications"]
            ]
        else:
            self.TaxClassifications: _List[TaxClassification] = []


class MarketplaceTaxInfo(__BaseDictObject):
    """
    Tax information about the marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "TaxClassifications" in data:
            self.TaxClassifications: _List[TaxClassification] = [
                TaxClassification(datum) for datum in data["TaxClassifications"]
            ]
        else:
            self.TaxClassifications: _List[TaxClassification] = []


class TaxClassification(__BaseDictObject):
    """
    The tax classification for the order.
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


class OrderItemsList(__BaseDictObject):
    """
    The order items list along with the order ID.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItems" in data:
            self.OrderItems: OrderItemList = self._get_value(OrderItemList, "OrderItems")
        else:
            self.OrderItems: OrderItemList = None
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None


class OrderItem(__BaseDictObject):
    """
    A single order item.
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
        if "AssociatedItems" in data:
            self.AssociatedItems: _List[AssociatedItem] = [AssociatedItem(datum) for datum in data["AssociatedItems"]]
        else:
            self.AssociatedItems: _List[AssociatedItem] = []
        if "Title" in data:
            self.Title: str = self._get_value(str, "Title")
        else:
            self.Title: str = None
        if "QuantityOrdered" in data:
            self.QuantityOrdered: int = self._get_value(int, "QuantityOrdered")
        else:
            self.QuantityOrdered: int = None
        if "QuantityShipped" in data:
            self.QuantityShipped: int = self._get_value(int, "QuantityShipped")
        else:
            self.QuantityShipped: int = None
        if "ProductInfo" in data:
            self.ProductInfo: ProductInfoDetail = self._get_value(ProductInfoDetail, "ProductInfo")
        else:
            self.ProductInfo: ProductInfoDetail = None
        if "PointsGranted" in data:
            self.PointsGranted: PointsGrantedDetail = self._get_value(PointsGrantedDetail, "PointsGranted")
        else:
            self.PointsGranted: PointsGrantedDetail = None
        if "ItemPrice" in data:
            self.ItemPrice: Money = self._get_value(Money, "ItemPrice")
        else:
            self.ItemPrice: Money = None
        if "ShippingPrice" in data:
            self.ShippingPrice: Money = self._get_value(Money, "ShippingPrice")
        else:
            self.ShippingPrice: Money = None
        if "ItemTax" in data:
            self.ItemTax: Money = self._get_value(Money, "ItemTax")
        else:
            self.ItemTax: Money = None
        if "ShippingTax" in data:
            self.ShippingTax: Money = self._get_value(Money, "ShippingTax")
        else:
            self.ShippingTax: Money = None
        if "ShippingDiscount" in data:
            self.ShippingDiscount: Money = self._get_value(Money, "ShippingDiscount")
        else:
            self.ShippingDiscount: Money = None
        if "ShippingDiscountTax" in data:
            self.ShippingDiscountTax: Money = self._get_value(Money, "ShippingDiscountTax")
        else:
            self.ShippingDiscountTax: Money = None
        if "PromotionDiscount" in data:
            self.PromotionDiscount: Money = self._get_value(Money, "PromotionDiscount")
        else:
            self.PromotionDiscount: Money = None
        if "PromotionDiscountTax" in data:
            self.PromotionDiscountTax: Money = self._get_value(Money, "PromotionDiscountTax")
        else:
            self.PromotionDiscountTax: Money = None
        if "PromotionIds" in data:
            self.PromotionIds: PromotionIdList = self._get_value(PromotionIdList, "PromotionIds")
        else:
            self.PromotionIds: PromotionIdList = None
        if "CODFee" in data:
            self.CODFee: Money = self._get_value(Money, "CODFee")
        else:
            self.CODFee: Money = None
        if "CODFeeDiscount" in data:
            self.CODFeeDiscount: Money = self._get_value(Money, "CODFeeDiscount")
        else:
            self.CODFeeDiscount: Money = None
        if "IsGift" in data:
            self.IsGift: bool = self._get_value(convert_bool, "IsGift")
        else:
            self.IsGift: bool = None
        if "ConditionNote" in data:
            self.ConditionNote: str = self._get_value(str, "ConditionNote")
        else:
            self.ConditionNote: str = None
        if "ConditionId" in data:
            self.ConditionId: str = self._get_value(str, "ConditionId")
        else:
            self.ConditionId: str = None
        if "ConditionSubtypeId" in data:
            self.ConditionSubtypeId: str = self._get_value(str, "ConditionSubtypeId")
        else:
            self.ConditionSubtypeId: str = None
        if "ScheduledDeliveryStartDate" in data:
            self.ScheduledDeliveryStartDate: str = self._get_value(str, "ScheduledDeliveryStartDate")
        else:
            self.ScheduledDeliveryStartDate: str = None
        if "ScheduledDeliveryEndDate" in data:
            self.ScheduledDeliveryEndDate: str = self._get_value(str, "ScheduledDeliveryEndDate")
        else:
            self.ScheduledDeliveryEndDate: str = None
        if "PriceDesignation" in data:
            self.PriceDesignation: str = self._get_value(str, "PriceDesignation")
        else:
            self.PriceDesignation: str = None
        if "TaxCollection" in data:
            self.TaxCollection: TaxCollection = self._get_value(TaxCollection, "TaxCollection")
        else:
            self.TaxCollection: TaxCollection = None
        if "SerialNumberRequired" in data:
            self.SerialNumberRequired: bool = self._get_value(convert_bool, "SerialNumberRequired")
        else:
            self.SerialNumberRequired: bool = None
        if "IsTransparency" in data:
            self.IsTransparency: bool = self._get_value(convert_bool, "IsTransparency")
        else:
            self.IsTransparency: bool = None
        if "IossNumber" in data:
            self.IossNumber: str = self._get_value(str, "IossNumber")
        else:
            self.IossNumber: str = None
        if "StoreChainStoreId" in data:
            self.StoreChainStoreId: str = self._get_value(str, "StoreChainStoreId")
        else:
            self.StoreChainStoreId: str = None
        if "DeemedResellerCategory" in data:
            self.DeemedResellerCategory: str = self._get_value(str, "DeemedResellerCategory")
        else:
            self.DeemedResellerCategory: str = None
        if "BuyerInfo" in data:
            self.BuyerInfo: ItemBuyerInfo = self._get_value(ItemBuyerInfo, "BuyerInfo")
        else:
            self.BuyerInfo: ItemBuyerInfo = None
        if "BuyerRequestedCancel" in data:
            self.BuyerRequestedCancel: BuyerRequestedCancel = self._get_value(
                BuyerRequestedCancel, "BuyerRequestedCancel"
            )
        else:
            self.BuyerRequestedCancel: BuyerRequestedCancel = None
        if "SerialNumbers" in data:
            self.SerialNumbers: _List[str] = [str(datum) for datum in data["SerialNumbers"]]
        else:
            self.SerialNumbers: _List[str] = []
        if "SubstitutionPreferences" in data:
            self.SubstitutionPreferences: SubstitutionPreferences = self._get_value(
                SubstitutionPreferences, "SubstitutionPreferences"
            )
        else:
            self.SubstitutionPreferences: SubstitutionPreferences = None
        if "Measurement" in data:
            self.Measurement: Measurement = self._get_value(Measurement, "Measurement")
        else:
            self.Measurement: Measurement = None


class SubstitutionPreferences(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "SubstitutionType" in data:
            self.SubstitutionType: str = self._get_value(str, "SubstitutionType")
        else:
            self.SubstitutionType: str = None
        if "SubstitutionOptions" in data:
            self.SubstitutionOptions: SubstitutionOptionList = self._get_value(
                SubstitutionOptionList, "SubstitutionOptions"
            )
        else:
            self.SubstitutionOptions: SubstitutionOptionList = None


class SubstitutionOption(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "QuantityOrdered" in data:
            self.QuantityOrdered: int = self._get_value(int, "QuantityOrdered")
        else:
            self.QuantityOrdered: int = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "Title" in data:
            self.Title: str = self._get_value(str, "Title")
        else:
            self.Title: str = None
        if "Measurement" in data:
            self.Measurement: Measurement = self._get_value(Measurement, "Measurement")
        else:
            self.Measurement: Measurement = None


class Measurement(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "Unit" in data:
            self.Unit: str = self._get_value(str, "Unit")
        else:
            self.Unit: str = None
        if "Value" in data:
            self.Value: float = self._get_value(float, "Value")
        else:
            self.Value: float = None


class AssociatedItem(__BaseDictObject):
    """
    An item associated with an order item. For example, a tire installation service purchased with tires.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderId" in data:
            self.OrderId: str = self._get_value(str, "OrderId")
        else:
            self.OrderId: str = None
        if "OrderItemId" in data:
            self.OrderItemId: str = self._get_value(str, "OrderItemId")
        else:
            self.OrderItemId: str = None
        if "AssociationType" in data:
            self.AssociationType: AssociationType = self._get_value(AssociationType, "AssociationType")
        else:
            self.AssociationType: AssociationType = None


class OrderItemsBuyerInfoList(__BaseDictObject):
    """
    A single order item's buyer information list with the order ID.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItems" in data:
            self.OrderItems: OrderItemBuyerInfoList = self._get_value(OrderItemBuyerInfoList, "OrderItems")
        else:
            self.OrderItems: OrderItemBuyerInfoList = None
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None


class OrderItemBuyerInfo(__BaseDictObject):
    """
    A single order item's buyer information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItemId" in data:
            self.OrderItemId: str = self._get_value(str, "OrderItemId")
        else:
            self.OrderItemId: str = None
        if "BuyerCustomizedInfo" in data:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = self._get_value(
                BuyerCustomizedInfoDetail, "BuyerCustomizedInfo"
            )
        else:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = None
        if "GiftWrapPrice" in data:
            self.GiftWrapPrice: Money = self._get_value(Money, "GiftWrapPrice")
        else:
            self.GiftWrapPrice: Money = None
        if "GiftWrapTax" in data:
            self.GiftWrapTax: Money = self._get_value(Money, "GiftWrapTax")
        else:
            self.GiftWrapTax: Money = None
        if "GiftMessageText" in data:
            self.GiftMessageText: str = self._get_value(str, "GiftMessageText")
        else:
            self.GiftMessageText: str = None
        if "GiftWrapLevel" in data:
            self.GiftWrapLevel: str = self._get_value(str, "GiftWrapLevel")
        else:
            self.GiftWrapLevel: str = None


class PointsGrantedDetail(__BaseDictObject):
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PointsNumber" in data:
            self.PointsNumber: int = self._get_value(int, "PointsNumber")
        else:
            self.PointsNumber: int = None
        if "PointsMonetaryValue" in data:
            self.PointsMonetaryValue: Money = self._get_value(Money, "PointsMonetaryValue")
        else:
            self.PointsMonetaryValue: Money = None


class ProductInfoDetail(__BaseDictObject):
    """
    Product information on the number of items.
    """

    def __init__(self, data):
        super().__init__(data)
        if "NumberOfItems" in data:
            self.NumberOfItems: int = self._get_value(int, "NumberOfItems")
        else:
            self.NumberOfItems: int = None


class BuyerCustomizedInfoDetail(__BaseDictObject):
    """
    Buyer information for custom orders from the Amazon Custom program.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CustomizedURL" in data:
            self.CustomizedURL: str = self._get_value(str, "CustomizedURL")
        else:
            self.CustomizedURL: str = None


class TaxCollection(__BaseDictObject):
    """
    Information about withheld taxes.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Model" in data:
            self.Model: str = self._get_value(str, "Model")
        else:
            self.Model: str = None
        if "ResponsibleParty" in data:
            self.ResponsibleParty: str = self._get_value(str, "ResponsibleParty")
        else:
            self.ResponsibleParty: str = None


class BuyerTaxInformation(__BaseDictObject):
    """
    Contains the business invoice tax information. Available only in the TR marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "BuyerLegalCompanyName" in data:
            self.BuyerLegalCompanyName: str = self._get_value(str, "BuyerLegalCompanyName")
        else:
            self.BuyerLegalCompanyName: str = None
        if "BuyerBusinessAddress" in data:
            self.BuyerBusinessAddress: str = self._get_value(str, "BuyerBusinessAddress")
        else:
            self.BuyerBusinessAddress: str = None
        if "BuyerTaxRegistrationId" in data:
            self.BuyerTaxRegistrationId: str = self._get_value(str, "BuyerTaxRegistrationId")
        else:
            self.BuyerTaxRegistrationId: str = None
        if "BuyerTaxOffice" in data:
            self.BuyerTaxOffice: str = self._get_value(str, "BuyerTaxOffice")
        else:
            self.BuyerTaxOffice: str = None


class FulfillmentInstruction(__BaseDictObject):
    """
    Contains the instructions about the fulfillment like where should it be fulfilled from.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FulfillmentSupplySourceId" in data:
            self.FulfillmentSupplySourceId: str = self._get_value(str, "FulfillmentSupplySourceId")
        else:
            self.FulfillmentSupplySourceId: str = None


class BuyerInfo(__BaseDictObject):
    """
    Buyer information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "BuyerEmail" in data:
            self.BuyerEmail: str = self._get_value(str, "BuyerEmail")
        else:
            self.BuyerEmail: str = None
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
        if "PurchaseOrderNumber" in data:
            self.PurchaseOrderNumber: str = self._get_value(str, "PurchaseOrderNumber")
        else:
            self.PurchaseOrderNumber: str = None


class ItemBuyerInfo(__BaseDictObject):
    """
    A single item's buyer information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "BuyerCustomizedInfo" in data:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = self._get_value(
                BuyerCustomizedInfoDetail, "BuyerCustomizedInfo"
            )
        else:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = None
        if "GiftWrapPrice" in data:
            self.GiftWrapPrice: Money = self._get_value(Money, "GiftWrapPrice")
        else:
            self.GiftWrapPrice: Money = None
        if "GiftWrapTax" in data:
            self.GiftWrapTax: Money = self._get_value(Money, "GiftWrapTax")
        else:
            self.GiftWrapTax: Money = None
        if "GiftMessageText" in data:
            self.GiftMessageText: str = self._get_value(str, "GiftMessageText")
        else:
            self.GiftMessageText: str = None
        if "GiftWrapLevel" in data:
            self.GiftWrapLevel: str = self._get_value(str, "GiftWrapLevel")
        else:
            self.GiftWrapLevel: str = None


class AutomatedShippingSettings(__BaseDictObject):
    """
    Contains information regarding the Shipping Settings Automation program, such as whether the order's shipping settings were generated automatically, and what those settings are.
    """

    def __init__(self, data):
        super().__init__(data)
        if "HasAutomatedShippingSettings" in data:
            self.HasAutomatedShippingSettings: bool = self._get_value(convert_bool, "HasAutomatedShippingSettings")
        else:
            self.HasAutomatedShippingSettings: bool = None
        if "AutomatedCarrier" in data:
            self.AutomatedCarrier: str = self._get_value(str, "AutomatedCarrier")
        else:
            self.AutomatedCarrier: str = None
        if "AutomatedShipMethod" in data:
            self.AutomatedShipMethod: str = self._get_value(str, "AutomatedShipMethod")
        else:
            self.AutomatedShipMethod: str = None


class BuyerRequestedCancel(__BaseDictObject):
    """
    Information about whether or not a buyer requested cancellation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "IsBuyerRequestedCancel" in data:
            self.IsBuyerRequestedCancel: bool = self._get_value(convert_bool, "IsBuyerRequestedCancel")
        else:
            self.IsBuyerRequestedCancel: bool = None
        if "BuyerCancelReason" in data:
            self.BuyerCancelReason: str = self._get_value(str, "BuyerCancelReason")
        else:
            self.BuyerCancelReason: str = None


class ConfirmShipmentRequest(__BaseDictObject):
    """
    The request schema for an shipment confirmation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "packageDetail" in data:
            self.packageDetail: PackageDetail = self._get_value(PackageDetail, "packageDetail")
        else:
            self.packageDetail: PackageDetail = None
        if "codCollectionMethod" in data:
            self.codCollectionMethod: str = self._get_value(str, "codCollectionMethod")
        else:
            self.codCollectionMethod: str = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None


class ConfirmShipmentErrorResponse(__BaseDictObject):
    """
    The error response schema for an shipment confirmation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class PackageDetail(__BaseDictObject):
    """
    Properties of packages
    """

    def __init__(self, data):
        super().__init__(data)
        if "packageReferenceId" in data:
            self.packageReferenceId: PackageReferenceId = self._get_value(PackageReferenceId, "packageReferenceId")
        else:
            self.packageReferenceId: PackageReferenceId = None
        if "carrierCode" in data:
            self.carrierCode: str = self._get_value(str, "carrierCode")
        else:
            self.carrierCode: str = None
        if "carrierName" in data:
            self.carrierName: str = self._get_value(str, "carrierName")
        else:
            self.carrierName: str = None
        if "shippingMethod" in data:
            self.shippingMethod: str = self._get_value(str, "shippingMethod")
        else:
            self.shippingMethod: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "shipDate" in data:
            self.shipDate: str = self._get_value(str, "shipDate")
        else:
            self.shipDate: str = None
        if "shipFromSupplySourceId" in data:
            self.shipFromSupplySourceId: str = self._get_value(str, "shipFromSupplySourceId")
        else:
            self.shipFromSupplySourceId: str = None
        if "orderItems" in data:
            self.orderItems: ConfirmShipmentOrderItemsList = self._get_value(
                ConfirmShipmentOrderItemsList, "orderItems"
            )
        else:
            self.orderItems: ConfirmShipmentOrderItemsList = None


class ConfirmShipmentOrderItem(__BaseDictObject):
    """
    A single order item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "orderItemId" in data:
            self.orderItemId: str = self._get_value(str, "orderItemId")
        else:
            self.orderItemId: str = None
        if "quantity" in data:
            self.quantity: int = self._get_value(int, "quantity")
        else:
            self.quantity: int = None
        if "transparencyCodes" in data:
            self.transparencyCodes: TransparencyCodeList = self._get_value(TransparencyCodeList, "transparencyCodes")
        else:
            self.transparencyCodes: TransparencyCodeList = None


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


class OrderItems(list, _List["dict"]):
    """
    For partial shipment status updates, the list of order items and quantities to be updated.
    """

    def __init__(self, data):
        super().__init__([dict(datum) for datum in data])
        self.data = data


class OrderList(list, _List["Order"]):
    """
    A list of orders.
    """

    def __init__(self, data):
        super().__init__([Order(datum) for datum in data])
        self.data = data


class PaymentMethodDetailItemList(list, _List["str"]):
    """
    A list of payment method detail items.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class PaymentExecutionDetailItemList(list, _List["PaymentExecutionDetailItem"]):
    """
    A list of payment execution detail items.
    """

    def __init__(self, data):
        super().__init__([PaymentExecutionDetailItem(datum) for datum in data])
        self.data = data


class OrderItemList(list, _List["OrderItem"]):
    """
    A list of order items.
    """

    def __init__(self, data):
        super().__init__([OrderItem(datum) for datum in data])
        self.data = data


class SubstitutionOptionList(list, _List["SubstitutionOption"]):
    """
    A collection of substitution options.
    """

    def __init__(self, data):
        super().__init__([SubstitutionOption(datum) for datum in data])
        self.data = data


class OrderItemBuyerInfoList(list, _List["OrderItemBuyerInfo"]):
    """
    A single order item's buyer information list.
    """

    def __init__(self, data):
        super().__init__([OrderItemBuyerInfo(datum) for datum in data])
        self.data = data


class PromotionIdList(list, _List["str"]):
    """
    A list of promotion identifiers provided by the seller when the promotions were created.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ConfirmShipmentOrderItemsList(list, _List["ConfirmShipmentOrderItem"]):
    """
    A list of order items.
    """

    def __init__(self, data):
        super().__init__([ConfirmShipmentOrderItem(datum) for datum in data])
        self.data = data


class TransparencyCodeList(list, _List["TransparencyCode"]):
    """
    A list of order items.
    """

    def __init__(self, data):
        super().__init__([TransparencyCode(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class MarketplaceId(str):
    """
    The unobfuscated marketplace identifier.
    """


class ShipmentStatus(str):
    """
    The shipment status to apply.
    """


class VerificationStatus(str):
    """
    The verification status of the order.
    """


class OtherDeliveryAttributes(str):
    """
    Miscellaneous delivery attributes associated with the shipping address.
    """


class AssociationType(str):
    """
    The type of association an item has with an order item.
    """


class EasyShipShipmentStatus(str):
    """
    The status of the Amazon Easy Ship order. This property is included only for Amazon Easy Ship orders.
    """


class ElectronicInvoiceStatus(str):
    """
    The status of the electronic invoice.
    """


class TransparencyCode(str):
    """
    The Transparency code associated with the item.
    """


class PackageReferenceId(str):
    """
    A seller-supplied identifier that uniquely identifies a package within the scope of an order. Only positive numeric values are supported.
    """


class OrdersV0Client(__BaseClient):
    def getOrders(
        self,
        MarketplaceIds: _List[str],
        CreatedAfter: str = None,
        CreatedBefore: str = None,
        LastUpdatedAfter: str = None,
        LastUpdatedBefore: str = None,
        OrderStatuses: _List[str] = None,
        FulfillmentChannels: _List[str] = None,
        PaymentMethods: _List[str] = None,
        BuyerEmail: str = None,
        SellerOrderId: str = None,
        MaxResultsPerPage: int = None,
        EasyShipShipmentStatuses: _List[str] = None,
        ElectronicInvoiceStatuses: _List[str] = None,
        NextToken: str = None,
        AmazonOrderIds: _List[str] = None,
        ActualFulfillmentSupplySourceId: str = None,
        IsISPU: bool = None,
        StoreChainStoreId: str = None,
        EarliestDeliveryDateBefore: str = None,
        EarliestDeliveryDateAfter: str = None,
        LatestDeliveryDateBefore: str = None,
        LatestDeliveryDateAfter: str = None,
    ):
        """
                Returns orders created or updated during the time frame indicated by the specified parameters. You can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is present, that will be used to retrieve the orders instead of other criteria.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders"
        params = {}
        if CreatedAfter is not None:
            params["CreatedAfter"] = CreatedAfter
        if CreatedBefore is not None:
            params["CreatedBefore"] = CreatedBefore
        if LastUpdatedAfter is not None:
            params["LastUpdatedAfter"] = LastUpdatedAfter
        if LastUpdatedBefore is not None:
            params["LastUpdatedBefore"] = LastUpdatedBefore
        if OrderStatuses is not None:
            params["OrderStatuses"] = ",".join(map(str, OrderStatuses))
        if MarketplaceIds is not None:
            params["MarketplaceIds"] = ",".join(map(str, MarketplaceIds))
        if FulfillmentChannels is not None:
            params["FulfillmentChannels"] = ",".join(map(str, FulfillmentChannels))
        if PaymentMethods is not None:
            params["PaymentMethods"] = ",".join(map(str, PaymentMethods))
        if BuyerEmail is not None:
            params["BuyerEmail"] = BuyerEmail
        if SellerOrderId is not None:
            params["SellerOrderId"] = SellerOrderId
        if MaxResultsPerPage is not None:
            params["MaxResultsPerPage"] = MaxResultsPerPage
        if EasyShipShipmentStatuses is not None:
            params["EasyShipShipmentStatuses"] = ",".join(map(str, EasyShipShipmentStatuses))
        if ElectronicInvoiceStatuses is not None:
            params["ElectronicInvoiceStatuses"] = ",".join(map(str, ElectronicInvoiceStatuses))
        if NextToken is not None:
            params["NextToken"] = NextToken
        if AmazonOrderIds is not None:
            params["AmazonOrderIds"] = ",".join(map(str, AmazonOrderIds))
        if ActualFulfillmentSupplySourceId is not None:
            params["ActualFulfillmentSupplySourceId"] = ActualFulfillmentSupplySourceId
        if IsISPU is not None:
            params["IsISPU"] = IsISPU
        if StoreChainStoreId is not None:
            params["StoreChainStoreId"] = StoreChainStoreId
        if EarliestDeliveryDateBefore is not None:
            params["EarliestDeliveryDateBefore"] = EarliestDeliveryDateBefore
        if EarliestDeliveryDateAfter is not None:
            params["EarliestDeliveryDateAfter"] = EarliestDeliveryDateAfter
        if LatestDeliveryDateBefore is not None:
            params["LatestDeliveryDateBefore"] = LatestDeliveryDateBefore
        if LatestDeliveryDateAfter is not None:
            params["LatestDeliveryDateAfter"] = LatestDeliveryDateAfter
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrdersResponse,
            400: GetOrdersResponse,
            403: GetOrdersResponse,
            404: GetOrdersResponse,
            429: GetOrdersResponse,
            500: GetOrdersResponse,
            503: GetOrdersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrder(
        self,
        orderId: str,
    ):
        """
                Returns the order that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderResponse,
            400: GetOrderResponse,
            403: GetOrderResponse,
            404: GetOrderResponse,
            429: GetOrderResponse,
            500: GetOrderResponse,
            503: GetOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderBuyerInfo(
        self,
        orderId: str,
    ):
        """
                Returns buyer information for the order that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/buyerInfo"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderBuyerInfoResponse,
            400: GetOrderBuyerInfoResponse,
            403: GetOrderBuyerInfoResponse,
            404: GetOrderBuyerInfoResponse,
            429: GetOrderBuyerInfoResponse,
            500: GetOrderBuyerInfoResponse,
            503: GetOrderBuyerInfoResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderAddress(
        self,
        orderId: str,
    ):
        """
                Returns the shipping address for the order that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/address"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderAddressResponse,
            400: GetOrderAddressResponse,
            403: GetOrderAddressResponse,
            404: GetOrderAddressResponse,
            429: GetOrderAddressResponse,
            500: GetOrderAddressResponse,
            503: GetOrderAddressResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderItems(
        self,
        orderId: str,
        NextToken: str = None,
    ):
        """
                Returns detailed order item information for the order that you specify. If NextToken is provided, it's used to retrieve the next page of order items.
        __Note__: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/orderItems"
        params = {}
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderItemsResponse,
            400: GetOrderItemsResponse,
            403: GetOrderItemsResponse,
            404: GetOrderItemsResponse,
            429: GetOrderItemsResponse,
            500: GetOrderItemsResponse,
            503: GetOrderItemsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderItemsBuyerInfo(
        self,
        orderId: str,
        NextToken: str = None,
    ):
        """
                Returns buyer information for the order items in the order that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/orderItems/buyerInfo"
        params = {}
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderItemsBuyerInfoResponse,
            400: GetOrderItemsBuyerInfoResponse,
            403: GetOrderItemsBuyerInfoResponse,
            404: GetOrderItemsBuyerInfoResponse,
            429: GetOrderItemsBuyerInfoResponse,
            500: GetOrderItemsBuyerInfoResponse,
            503: GetOrderItemsBuyerInfoResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateShipmentStatus(
        self,
        data: UpdateShipmentStatusRequest,
        orderId: str,
    ):
        """
                Update the shipment status for an order that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/shipment"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            204: None,
            400: UpdateShipmentStatusErrorResponse,
            403: UpdateShipmentStatusErrorResponse,
            404: UpdateShipmentStatusErrorResponse,
            413: UpdateShipmentStatusErrorResponse,
            415: UpdateShipmentStatusErrorResponse,
            429: UpdateShipmentStatusErrorResponse,
            500: UpdateShipmentStatusErrorResponse,
            503: UpdateShipmentStatusErrorResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderRegulatedInfo(
        self,
        orderId: str,
    ):
        """
                Returns regulated information for the order that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/regulatedInfo"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderRegulatedInfoResponse,
            400: GetOrderRegulatedInfoResponse,
            403: GetOrderRegulatedInfoResponse,
            404: GetOrderRegulatedInfoResponse,
            429: GetOrderRegulatedInfoResponse,
            500: GetOrderRegulatedInfoResponse,
            503: GetOrderRegulatedInfoResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateVerificationStatus(
        self,
        data: UpdateVerificationStatusRequest,
        orderId: str,
    ):
        """
                Updates (approves or rejects) the verification status of an order containing regulated products.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/regulatedInfo"
        params = {}
        response = self.request(
            path=url,
            method="PATCH",
            params=params,
            data=data.data,
        )
        response_type = {
            204: None,
            400: UpdateVerificationStatusErrorResponse,
            403: UpdateVerificationStatusErrorResponse,
            404: UpdateVerificationStatusErrorResponse,
            413: UpdateVerificationStatusErrorResponse,
            415: UpdateVerificationStatusErrorResponse,
            429: UpdateVerificationStatusErrorResponse,
            500: UpdateVerificationStatusErrorResponse,
            503: UpdateVerificationStatusErrorResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def confirmShipment(
        self,
        data: ConfirmShipmentRequest,
        orderId: str,
    ):
        """
                Updates the shipment confirmation status for a specified order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/orders/v0/orders/{orderId}/shipmentConfirmation"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            204: None,
            400: ConfirmShipmentErrorResponse,
            401: ConfirmShipmentErrorResponse,
            403: ConfirmShipmentErrorResponse,
            404: ConfirmShipmentErrorResponse,
            429: ConfirmShipmentErrorResponse,
            500: ConfirmShipmentErrorResponse,
            503: ConfirmShipmentErrorResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
