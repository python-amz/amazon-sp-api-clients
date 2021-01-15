from .base import BaseClient as __BaseClient
from typing import List as _List


class Error:
    def __init__(self, data):
        super().__init__()
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


class Address:
    def __init__(self, data):
        super().__init__()
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
        if "districtOrCounty" in data:
            self.districtOrCounty: str = str(data["districtOrCounty"])
        else:
            self.districtOrCounty: str = None
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


class CODSettings:
    def __init__(self, data):
        super().__init__()
        if "isCodRequired" in data:
            self.isCodRequired: bool = bool(data["isCodRequired"])
        else:
            self.isCodRequired: bool = None
        if "codCharge" in data:
            self.codCharge: Money = Money(data["codCharge"])
        else:
            self.codCharge: Money = None
        if "codChargeTax" in data:
            self.codChargeTax: Money = Money(data["codChargeTax"])
        else:
            self.codChargeTax: Money = None
        if "shippingCharge" in data:
            self.shippingCharge: Money = Money(data["shippingCharge"])
        else:
            self.shippingCharge: Money = None
        if "shippingChargeTax" in data:
            self.shippingChargeTax: Money = Money(data["shippingChargeTax"])
        else:
            self.shippingChargeTax: Money = None


class CreateFulfillmentOrderItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "giftMessage" in data:
            self.giftMessage: str = str(data["giftMessage"])
        else:
            self.giftMessage: str = None
        if "displayableComment" in data:
            self.displayableComment: str = str(data["displayableComment"])
        else:
            self.displayableComment: str = None
        if "fulfillmentNetworkSku" in data:
            self.fulfillmentNetworkSku: str = str(data["fulfillmentNetworkSku"])
        else:
            self.fulfillmentNetworkSku: str = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = Money(data["perUnitDeclaredValue"])
        else:
            self.perUnitDeclaredValue: Money = None
        if "perUnitPrice" in data:
            self.perUnitPrice: Money = Money(data["perUnitPrice"])
        else:
            self.perUnitPrice: Money = None
        if "perUnitTax" in data:
            self.perUnitTax: Money = Money(data["perUnitTax"])
        else:
            self.perUnitTax: Money = None


class CreateFulfillmentOrderRequest:
    def __init__(self, data):
        super().__init__()
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "sellerFulfillmentOrderId" in data:
            self.sellerFulfillmentOrderId: str = str(data["sellerFulfillmentOrderId"])
        else:
            self.sellerFulfillmentOrderId: str = None
        if "displayableOrderId" in data:
            self.displayableOrderId: str = str(data["displayableOrderId"])
        else:
            self.displayableOrderId: str = None
        if "displayableOrderDate" in data:
            self.displayableOrderDate: Timestamp = Timestamp(data["displayableOrderDate"])
        else:
            self.displayableOrderDate: Timestamp = None
        if "displayableOrderComment" in data:
            self.displayableOrderComment: str = str(data["displayableOrderComment"])
        else:
            self.displayableOrderComment: str = None
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = ShippingSpeedCategory(data["shippingSpeedCategory"])
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "deliveryWindow" in data:
            self.deliveryWindow: DeliveryWindow = DeliveryWindow(data["deliveryWindow"])
        else:
            self.deliveryWindow: DeliveryWindow = None
        if "destinationAddress" in data:
            self.destinationAddress: Address = Address(data["destinationAddress"])
        else:
            self.destinationAddress: Address = None
        if "fulfillmentAction" in data:
            self.fulfillmentAction: FulfillmentAction = FulfillmentAction(data["fulfillmentAction"])
        else:
            self.fulfillmentAction: FulfillmentAction = None
        if "fulfillmentPolicy" in data:
            self.fulfillmentPolicy: FulfillmentPolicy = FulfillmentPolicy(data["fulfillmentPolicy"])
        else:
            self.fulfillmentPolicy: FulfillmentPolicy = None
        if "codSettings" in data:
            self.codSettings: CODSettings = CODSettings(data["codSettings"])
        else:
            self.codSettings: CODSettings = None
        if "shipFromCountryCode" in data:
            self.shipFromCountryCode: str = str(data["shipFromCountryCode"])
        else:
            self.shipFromCountryCode: str = None
        if "notificationEmails" in data:
            self.notificationEmails: NotificationEmailList = NotificationEmailList(data["notificationEmails"])
        else:
            self.notificationEmails: NotificationEmailList = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []
        if "items" in data:
            self.items: CreateFulfillmentOrderItemList = CreateFulfillmentOrderItemList(data["items"])
        else:
            self.items: CreateFulfillmentOrderItemList = None


class CreateFulfillmentReturnRequest:
    def __init__(self, data):
        super().__init__()
        if "items" in data:
            self.items: CreateReturnItemList = CreateReturnItemList(data["items"])
        else:
            self.items: CreateReturnItemList = None


class CreateFulfillmentReturnResult:
    def __init__(self, data):
        super().__init__()
        if "returnItems" in data:
            self.returnItems: ReturnItemList = ReturnItemList(data["returnItems"])
        else:
            self.returnItems: ReturnItemList = None
        if "invalidReturnItems" in data:
            self.invalidReturnItems: InvalidReturnItemList = InvalidReturnItemList(data["invalidReturnItems"])
        else:
            self.invalidReturnItems: InvalidReturnItemList = None
        if "returnAuthorizations" in data:
            self.returnAuthorizations: ReturnAuthorizationList = ReturnAuthorizationList(data["returnAuthorizations"])
        else:
            self.returnAuthorizations: ReturnAuthorizationList = None


class CreateFulfillmentReturnResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: CreateFulfillmentReturnResult = CreateFulfillmentReturnResult(data["payload"])
        else:
            self.payload: CreateFulfillmentReturnResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateReturnItem:
    def __init__(self, data):
        super().__init__()
        if "sellerReturnItemId" in data:
            self.sellerReturnItemId: str = str(data["sellerReturnItemId"])
        else:
            self.sellerReturnItemId: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "amazonShipmentId" in data:
            self.amazonShipmentId: str = str(data["amazonShipmentId"])
        else:
            self.amazonShipmentId: str = None
        if "returnReasonCode" in data:
            self.returnReasonCode: str = str(data["returnReasonCode"])
        else:
            self.returnReasonCode: str = None
        if "returnComment" in data:
            self.returnComment: str = str(data["returnComment"])
        else:
            self.returnComment: str = None


class Money:
    def __init__(self, data):
        super().__init__()
        if "currencyCode" in data:
            self.currencyCode: str = str(data["currencyCode"])
        else:
            self.currencyCode: str = None
        if "value" in data:
            self.value: Decimal = Decimal(data["value"])
        else:
            self.value: Decimal = None


class DeliveryWindow:
    def __init__(self, data):
        super().__init__()
        if "startDate" in data:
            self.startDate: Timestamp = Timestamp(data["startDate"])
        else:
            self.startDate: Timestamp = None
        if "endDate" in data:
            self.endDate: Timestamp = Timestamp(data["endDate"])
        else:
            self.endDate: Timestamp = None


class Fee:
    def __init__(self, data):
        super().__init__()
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "amount" in data:
            self.amount: Money = Money(data["amount"])
        else:
            self.amount: Money = None


class FulfillmentOrder:
    def __init__(self, data):
        super().__init__()
        if "sellerFulfillmentOrderId" in data:
            self.sellerFulfillmentOrderId: str = str(data["sellerFulfillmentOrderId"])
        else:
            self.sellerFulfillmentOrderId: str = None
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "displayableOrderId" in data:
            self.displayableOrderId: str = str(data["displayableOrderId"])
        else:
            self.displayableOrderId: str = None
        if "displayableOrderDate" in data:
            self.displayableOrderDate: Timestamp = Timestamp(data["displayableOrderDate"])
        else:
            self.displayableOrderDate: Timestamp = None
        if "displayableOrderComment" in data:
            self.displayableOrderComment: str = str(data["displayableOrderComment"])
        else:
            self.displayableOrderComment: str = None
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = ShippingSpeedCategory(data["shippingSpeedCategory"])
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "deliveryWindow" in data:
            self.deliveryWindow: DeliveryWindow = DeliveryWindow(data["deliveryWindow"])
        else:
            self.deliveryWindow: DeliveryWindow = None
        if "destinationAddress" in data:
            self.destinationAddress: Address = Address(data["destinationAddress"])
        else:
            self.destinationAddress: Address = None
        if "fulfillmentAction" in data:
            self.fulfillmentAction: FulfillmentAction = FulfillmentAction(data["fulfillmentAction"])
        else:
            self.fulfillmentAction: FulfillmentAction = None
        if "fulfillmentPolicy" in data:
            self.fulfillmentPolicy: FulfillmentPolicy = FulfillmentPolicy(data["fulfillmentPolicy"])
        else:
            self.fulfillmentPolicy: FulfillmentPolicy = None
        if "codSettings" in data:
            self.codSettings: CODSettings = CODSettings(data["codSettings"])
        else:
            self.codSettings: CODSettings = None
        if "receivedDate" in data:
            self.receivedDate: Timestamp = Timestamp(data["receivedDate"])
        else:
            self.receivedDate: Timestamp = None
        if "fulfillmentOrderStatus" in data:
            self.fulfillmentOrderStatus: FulfillmentOrderStatus = FulfillmentOrderStatus(data["fulfillmentOrderStatus"])
        else:
            self.fulfillmentOrderStatus: FulfillmentOrderStatus = None
        if "statusUpdatedDate" in data:
            self.statusUpdatedDate: Timestamp = Timestamp(data["statusUpdatedDate"])
        else:
            self.statusUpdatedDate: Timestamp = None
        if "notificationEmails" in data:
            self.notificationEmails: NotificationEmailList = NotificationEmailList(data["notificationEmails"])
        else:
            self.notificationEmails: NotificationEmailList = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class FulfillmentOrderItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "giftMessage" in data:
            self.giftMessage: str = str(data["giftMessage"])
        else:
            self.giftMessage: str = None
        if "displayableComment" in data:
            self.displayableComment: str = str(data["displayableComment"])
        else:
            self.displayableComment: str = None
        if "fulfillmentNetworkSku" in data:
            self.fulfillmentNetworkSku: str = str(data["fulfillmentNetworkSku"])
        else:
            self.fulfillmentNetworkSku: str = None
        if "orderItemDisposition" in data:
            self.orderItemDisposition: str = str(data["orderItemDisposition"])
        else:
            self.orderItemDisposition: str = None
        if "cancelledQuantity" in data:
            self.cancelledQuantity: Quantity = Quantity(data["cancelledQuantity"])
        else:
            self.cancelledQuantity: Quantity = None
        if "unfulfillableQuantity" in data:
            self.unfulfillableQuantity: Quantity = Quantity(data["unfulfillableQuantity"])
        else:
            self.unfulfillableQuantity: Quantity = None
        if "estimatedShipDate" in data:
            self.estimatedShipDate: Timestamp = Timestamp(data["estimatedShipDate"])
        else:
            self.estimatedShipDate: Timestamp = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = Timestamp(data["estimatedArrivalDate"])
        else:
            self.estimatedArrivalDate: Timestamp = None
        if "perUnitPrice" in data:
            self.perUnitPrice: Money = Money(data["perUnitPrice"])
        else:
            self.perUnitPrice: Money = None
        if "perUnitTax" in data:
            self.perUnitTax: Money = Money(data["perUnitTax"])
        else:
            self.perUnitTax: Money = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = Money(data["perUnitDeclaredValue"])
        else:
            self.perUnitDeclaredValue: Money = None


class FulfillmentPreview:
    def __init__(self, data):
        super().__init__()
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = ShippingSpeedCategory(data["shippingSpeedCategory"])
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "scheduledDeliveryInfo" in data:
            self.scheduledDeliveryInfo: ScheduledDeliveryInfo = ScheduledDeliveryInfo(data["scheduledDeliveryInfo"])
        else:
            self.scheduledDeliveryInfo: ScheduledDeliveryInfo = None
        if "isFulfillable" in data:
            self.isFulfillable: bool = bool(data["isFulfillable"])
        else:
            self.isFulfillable: bool = None
        if "isCODCapable" in data:
            self.isCODCapable: bool = bool(data["isCODCapable"])
        else:
            self.isCODCapable: bool = None
        if "estimatedShippingWeight" in data:
            self.estimatedShippingWeight: Weight = Weight(data["estimatedShippingWeight"])
        else:
            self.estimatedShippingWeight: Weight = None
        if "estimatedFees" in data:
            self.estimatedFees: FeeList = FeeList(data["estimatedFees"])
        else:
            self.estimatedFees: FeeList = None
        if "fulfillmentPreviewShipments" in data:
            self.fulfillmentPreviewShipments: FulfillmentPreviewShipmentList = FulfillmentPreviewShipmentList(
                data["fulfillmentPreviewShipments"]
            )
        else:
            self.fulfillmentPreviewShipments: FulfillmentPreviewShipmentList = None
        if "unfulfillablePreviewItems" in data:
            self.unfulfillablePreviewItems: UnfulfillablePreviewItemList = UnfulfillablePreviewItemList(
                data["unfulfillablePreviewItems"]
            )
        else:
            self.unfulfillablePreviewItems: UnfulfillablePreviewItemList = None
        if "orderUnfulfillableReasons" in data:
            self.orderUnfulfillableReasons: StringList = StringList(data["orderUnfulfillableReasons"])
        else:
            self.orderUnfulfillableReasons: StringList = None
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class FulfillmentPreviewItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "estimatedShippingWeight" in data:
            self.estimatedShippingWeight: Weight = Weight(data["estimatedShippingWeight"])
        else:
            self.estimatedShippingWeight: Weight = None
        if "shippingWeightCalculationMethod" in data:
            self.shippingWeightCalculationMethod: str = str(data["shippingWeightCalculationMethod"])
        else:
            self.shippingWeightCalculationMethod: str = None


class FulfillmentPreviewShipment:
    def __init__(self, data):
        super().__init__()
        if "earliestShipDate" in data:
            self.earliestShipDate: Timestamp = Timestamp(data["earliestShipDate"])
        else:
            self.earliestShipDate: Timestamp = None
        if "latestShipDate" in data:
            self.latestShipDate: Timestamp = Timestamp(data["latestShipDate"])
        else:
            self.latestShipDate: Timestamp = None
        if "earliestArrivalDate" in data:
            self.earliestArrivalDate: Timestamp = Timestamp(data["earliestArrivalDate"])
        else:
            self.earliestArrivalDate: Timestamp = None
        if "latestArrivalDate" in data:
            self.latestArrivalDate: Timestamp = Timestamp(data["latestArrivalDate"])
        else:
            self.latestArrivalDate: Timestamp = None
        if "shippingNotes" in data:
            self.shippingNotes: _List[str] = [str(datum) for datum in data["shippingNotes"]]
        else:
            self.shippingNotes: _List[str] = []
        if "fulfillmentPreviewItems" in data:
            self.fulfillmentPreviewItems: FulfillmentPreviewItemList = FulfillmentPreviewItemList(
                data["fulfillmentPreviewItems"]
            )
        else:
            self.fulfillmentPreviewItems: FulfillmentPreviewItemList = None


class FulfillmentShipment:
    def __init__(self, data):
        super().__init__()
        if "amazonShipmentId" in data:
            self.amazonShipmentId: str = str(data["amazonShipmentId"])
        else:
            self.amazonShipmentId: str = None
        if "fulfillmentCenterId" in data:
            self.fulfillmentCenterId: str = str(data["fulfillmentCenterId"])
        else:
            self.fulfillmentCenterId: str = None
        if "fulfillmentShipmentStatus" in data:
            self.fulfillmentShipmentStatus: str = str(data["fulfillmentShipmentStatus"])
        else:
            self.fulfillmentShipmentStatus: str = None
        if "shippingDate" in data:
            self.shippingDate: Timestamp = Timestamp(data["shippingDate"])
        else:
            self.shippingDate: Timestamp = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = Timestamp(data["estimatedArrivalDate"])
        else:
            self.estimatedArrivalDate: Timestamp = None
        if "shippingNotes" in data:
            self.shippingNotes: _List[str] = [str(datum) for datum in data["shippingNotes"]]
        else:
            self.shippingNotes: _List[str] = []
        if "fulfillmentShipmentItem" in data:
            self.fulfillmentShipmentItem: FulfillmentShipmentItemList = FulfillmentShipmentItemList(
                data["fulfillmentShipmentItem"]
            )
        else:
            self.fulfillmentShipmentItem: FulfillmentShipmentItemList = None
        if "fulfillmentShipmentPackage" in data:
            self.fulfillmentShipmentPackage: FulfillmentShipmentPackageList = FulfillmentShipmentPackageList(
                data["fulfillmentShipmentPackage"]
            )
        else:
            self.fulfillmentShipmentPackage: FulfillmentShipmentPackageList = None


class FulfillmentShipmentItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "packageNumber" in data:
            self.packageNumber: int = int(data["packageNumber"])
        else:
            self.packageNumber: int = None
        if "serialNumber" in data:
            self.serialNumber: str = str(data["serialNumber"])
        else:
            self.serialNumber: str = None


class FulfillmentShipmentPackage:
    def __init__(self, data):
        super().__init__()
        if "packageNumber" in data:
            self.packageNumber: int = int(data["packageNumber"])
        else:
            self.packageNumber: int = None
        if "carrierCode" in data:
            self.carrierCode: str = str(data["carrierCode"])
        else:
            self.carrierCode: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = Timestamp(data["estimatedArrivalDate"])
        else:
            self.estimatedArrivalDate: Timestamp = None


class GetFulfillmentOrderResult:
    def __init__(self, data):
        super().__init__()
        if "fulfillmentOrder" in data:
            self.fulfillmentOrder: FulfillmentOrder = FulfillmentOrder(data["fulfillmentOrder"])
        else:
            self.fulfillmentOrder: FulfillmentOrder = None
        if "fulfillmentOrderItems" in data:
            self.fulfillmentOrderItems: FulfillmentOrderItemList = FulfillmentOrderItemList(
                data["fulfillmentOrderItems"]
            )
        else:
            self.fulfillmentOrderItems: FulfillmentOrderItemList = None
        if "fulfillmentShipments" in data:
            self.fulfillmentShipments: FulfillmentShipmentList = FulfillmentShipmentList(data["fulfillmentShipments"])
        else:
            self.fulfillmentShipments: FulfillmentShipmentList = None
        if "returnItems" in data:
            self.returnItems: ReturnItemList = ReturnItemList(data["returnItems"])
        else:
            self.returnItems: ReturnItemList = None
        if "returnAuthorizations" in data:
            self.returnAuthorizations: ReturnAuthorizationList = ReturnAuthorizationList(data["returnAuthorizations"])
        else:
            self.returnAuthorizations: ReturnAuthorizationList = None


class GetFulfillmentOrderResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: GetFulfillmentOrderResult = GetFulfillmentOrderResult(data["payload"])
        else:
            self.payload: GetFulfillmentOrderResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFulfillmentPreviewItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = Money(data["perUnitDeclaredValue"])
        else:
            self.perUnitDeclaredValue: Money = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None


class GetFulfillmentPreviewRequest:
    def __init__(self, data):
        super().__init__()
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "address" in data:
            self.address: Address = Address(data["address"])
        else:
            self.address: Address = None
        if "items" in data:
            self.items: GetFulfillmentPreviewItemList = GetFulfillmentPreviewItemList(data["items"])
        else:
            self.items: GetFulfillmentPreviewItemList = None
        if "shippingSpeedCategories" in data:
            self.shippingSpeedCategories: ShippingSpeedCategoryList = ShippingSpeedCategoryList(
                data["shippingSpeedCategories"]
            )
        else:
            self.shippingSpeedCategories: ShippingSpeedCategoryList = None
        if "includeCODFulfillmentPreview" in data:
            self.includeCODFulfillmentPreview: bool = bool(data["includeCODFulfillmentPreview"])
        else:
            self.includeCODFulfillmentPreview: bool = None
        if "includeDeliveryWindows" in data:
            self.includeDeliveryWindows: bool = bool(data["includeDeliveryWindows"])
        else:
            self.includeDeliveryWindows: bool = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class GetFulfillmentPreviewResult:
    def __init__(self, data):
        super().__init__()
        if "fulfillmentPreviews" in data:
            self.fulfillmentPreviews: FulfillmentPreviewList = FulfillmentPreviewList(data["fulfillmentPreviews"])
        else:
            self.fulfillmentPreviews: FulfillmentPreviewList = None


class GetFulfillmentPreviewResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: GetFulfillmentPreviewResult = GetFulfillmentPreviewResult(data["payload"])
        else:
            self.payload: GetFulfillmentPreviewResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class InvalidItemReason:
    def __init__(self, data):
        super().__init__()
        if "invalidItemReasonCode" in data:
            self.invalidItemReasonCode: InvalidItemReasonCode = InvalidItemReasonCode(data["invalidItemReasonCode"])
        else:
            self.invalidItemReasonCode: InvalidItemReasonCode = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None


class InvalidReturnItem:
    def __init__(self, data):
        super().__init__()
        if "sellerReturnItemId" in data:
            self.sellerReturnItemId: str = str(data["sellerReturnItemId"])
        else:
            self.sellerReturnItemId: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "invalidItemReason" in data:
            self.invalidItemReason: InvalidItemReason = InvalidItemReason(data["invalidItemReason"])
        else:
            self.invalidItemReason: InvalidItemReason = None


class ListAllFulfillmentOrdersResult:
    def __init__(self, data):
        super().__init__()
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None
        if "fulfillmentOrders" in data:
            self.fulfillmentOrders: _List[FulfillmentOrder] = [
                FulfillmentOrder(datum) for datum in data["fulfillmentOrders"]
            ]
        else:
            self.fulfillmentOrders: _List[FulfillmentOrder] = []


class ListAllFulfillmentOrdersResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: ListAllFulfillmentOrdersResult = ListAllFulfillmentOrdersResult(data["payload"])
        else:
            self.payload: ListAllFulfillmentOrdersResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ListReturnReasonCodesResult:
    def __init__(self, data):
        super().__init__()
        if "reasonCodeDetails" in data:
            self.reasonCodeDetails: ReasonCodeDetailsList = ReasonCodeDetailsList(data["reasonCodeDetails"])
        else:
            self.reasonCodeDetails: ReasonCodeDetailsList = None


class ListReturnReasonCodesResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: ListReturnReasonCodesResult = ListReturnReasonCodesResult(data["payload"])
        else:
            self.payload: ListReturnReasonCodesResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class PackageTrackingDetails:
    def __init__(self, data):
        super().__init__()
        if "packageNumber" in data:
            self.packageNumber: int = int(data["packageNumber"])
        else:
            self.packageNumber: int = None
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "customerTrackingLink" in data:
            self.customerTrackingLink: str = str(data["customerTrackingLink"])
        else:
            self.customerTrackingLink: str = None
        if "carrierCode" in data:
            self.carrierCode: str = str(data["carrierCode"])
        else:
            self.carrierCode: str = None
        if "carrierPhoneNumber" in data:
            self.carrierPhoneNumber: str = str(data["carrierPhoneNumber"])
        else:
            self.carrierPhoneNumber: str = None
        if "carrierURL" in data:
            self.carrierURL: str = str(data["carrierURL"])
        else:
            self.carrierURL: str = None
        if "shipDate" in data:
            self.shipDate: Timestamp = Timestamp(data["shipDate"])
        else:
            self.shipDate: Timestamp = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = Timestamp(data["estimatedArrivalDate"])
        else:
            self.estimatedArrivalDate: Timestamp = None
        if "shipToAddress" in data:
            self.shipToAddress: TrackingAddress = TrackingAddress(data["shipToAddress"])
        else:
            self.shipToAddress: TrackingAddress = None
        if "currentStatus" in data:
            self.currentStatus: CurrentStatus = CurrentStatus(data["currentStatus"])
        else:
            self.currentStatus: CurrentStatus = None
        if "currentStatusDescription" in data:
            self.currentStatusDescription: str = str(data["currentStatusDescription"])
        else:
            self.currentStatusDescription: str = None
        if "signedForBy" in data:
            self.signedForBy: str = str(data["signedForBy"])
        else:
            self.signedForBy: str = None
        if "additionalLocationInfo" in data:
            self.additionalLocationInfo: AdditionalLocationInfo = AdditionalLocationInfo(data["additionalLocationInfo"])
        else:
            self.additionalLocationInfo: AdditionalLocationInfo = None
        if "trackingEvents" in data:
            self.trackingEvents: TrackingEventList = TrackingEventList(data["trackingEvents"])
        else:
            self.trackingEvents: TrackingEventList = None


class GetPackageTrackingDetailsResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: PackageTrackingDetails = PackageTrackingDetails(data["payload"])
        else:
            self.payload: PackageTrackingDetails = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ReasonCodeDetails:
    def __init__(self, data):
        super().__init__()
        if "returnReasonCode" in data:
            self.returnReasonCode: str = str(data["returnReasonCode"])
        else:
            self.returnReasonCode: str = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None
        if "translatedDescription" in data:
            self.translatedDescription: str = str(data["translatedDescription"])
        else:
            self.translatedDescription: str = None


class ReturnAuthorization:
    def __init__(self, data):
        super().__init__()
        if "returnAuthorizationId" in data:
            self.returnAuthorizationId: str = str(data["returnAuthorizationId"])
        else:
            self.returnAuthorizationId: str = None
        if "fulfillmentCenterId" in data:
            self.fulfillmentCenterId: str = str(data["fulfillmentCenterId"])
        else:
            self.fulfillmentCenterId: str = None
        if "returnToAddress" in data:
            self.returnToAddress: Address = Address(data["returnToAddress"])
        else:
            self.returnToAddress: Address = None
        if "amazonRmaId" in data:
            self.amazonRmaId: str = str(data["amazonRmaId"])
        else:
            self.amazonRmaId: str = None
        if "rmaPageURL" in data:
            self.rmaPageURL: str = str(data["rmaPageURL"])
        else:
            self.rmaPageURL: str = None


class ReturnItem:
    def __init__(self, data):
        super().__init__()
        if "sellerReturnItemId" in data:
            self.sellerReturnItemId: str = str(data["sellerReturnItemId"])
        else:
            self.sellerReturnItemId: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "amazonShipmentId" in data:
            self.amazonShipmentId: str = str(data["amazonShipmentId"])
        else:
            self.amazonShipmentId: str = None
        if "sellerReturnReasonCode" in data:
            self.sellerReturnReasonCode: str = str(data["sellerReturnReasonCode"])
        else:
            self.sellerReturnReasonCode: str = None
        if "returnComment" in data:
            self.returnComment: str = str(data["returnComment"])
        else:
            self.returnComment: str = None
        if "amazonReturnReasonCode" in data:
            self.amazonReturnReasonCode: str = str(data["amazonReturnReasonCode"])
        else:
            self.amazonReturnReasonCode: str = None
        if "status" in data:
            self.status: FulfillmentReturnItemStatus = FulfillmentReturnItemStatus(data["status"])
        else:
            self.status: FulfillmentReturnItemStatus = None
        if "statusChangedDate" in data:
            self.statusChangedDate: Timestamp = Timestamp(data["statusChangedDate"])
        else:
            self.statusChangedDate: Timestamp = None
        if "returnAuthorizationId" in data:
            self.returnAuthorizationId: str = str(data["returnAuthorizationId"])
        else:
            self.returnAuthorizationId: str = None
        if "returnReceivedCondition" in data:
            self.returnReceivedCondition: ReturnItemDisposition = ReturnItemDisposition(data["returnReceivedCondition"])
        else:
            self.returnReceivedCondition: ReturnItemDisposition = None
        if "fulfillmentCenterId" in data:
            self.fulfillmentCenterId: str = str(data["fulfillmentCenterId"])
        else:
            self.fulfillmentCenterId: str = None


class ScheduledDeliveryInfo:
    def __init__(self, data):
        super().__init__()
        if "deliveryTimeZone" in data:
            self.deliveryTimeZone: str = str(data["deliveryTimeZone"])
        else:
            self.deliveryTimeZone: str = None
        if "deliveryWindows" in data:
            self.deliveryWindows: DeliveryWindowList = DeliveryWindowList(data["deliveryWindows"])
        else:
            self.deliveryWindows: DeliveryWindowList = None


class TrackingAddress:
    def __init__(self, data):
        super().__init__()
        if "city" in data:
            self.city: str = str(data["city"])
        else:
            self.city: str = None
        if "state" in data:
            self.state: str = str(data["state"])
        else:
            self.state: str = None
        if "country" in data:
            self.country: str = str(data["country"])
        else:
            self.country: str = None


class TrackingEvent:
    def __init__(self, data):
        super().__init__()
        if "eventDate" in data:
            self.eventDate: Timestamp = Timestamp(data["eventDate"])
        else:
            self.eventDate: Timestamp = None
        if "eventAddress" in data:
            self.eventAddress: TrackingAddress = TrackingAddress(data["eventAddress"])
        else:
            self.eventAddress: TrackingAddress = None
        if "eventCode" in data:
            self.eventCode: EventCode = EventCode(data["eventCode"])
        else:
            self.eventCode: EventCode = None
        if "eventDescription" in data:
            self.eventDescription: str = str(data["eventDescription"])
        else:
            self.eventDescription: str = None


class UnfulfillablePreviewItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "itemUnfulfillableReasons" in data:
            self.itemUnfulfillableReasons: StringList = StringList(data["itemUnfulfillableReasons"])
        else:
            self.itemUnfulfillableReasons: StringList = None


class UpdateFulfillmentOrderItem:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = str(data["sellerFulfillmentOrderItemId"])
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = Quantity(data["quantity"])
        else:
            self.quantity: Quantity = None
        if "giftMessage" in data:
            self.giftMessage: str = str(data["giftMessage"])
        else:
            self.giftMessage: str = None
        if "displayableComment" in data:
            self.displayableComment: str = str(data["displayableComment"])
        else:
            self.displayableComment: str = None
        if "fulfillmentNetworkSku" in data:
            self.fulfillmentNetworkSku: str = str(data["fulfillmentNetworkSku"])
        else:
            self.fulfillmentNetworkSku: str = None
        if "orderItemDisposition" in data:
            self.orderItemDisposition: str = str(data["orderItemDisposition"])
        else:
            self.orderItemDisposition: str = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = Money(data["perUnitDeclaredValue"])
        else:
            self.perUnitDeclaredValue: Money = None
        if "perUnitPrice" in data:
            self.perUnitPrice: Money = Money(data["perUnitPrice"])
        else:
            self.perUnitPrice: Money = None
        if "perUnitTax" in data:
            self.perUnitTax: Money = Money(data["perUnitTax"])
        else:
            self.perUnitTax: Money = None


class UpdateFulfillmentOrderRequest:
    def __init__(self, data):
        super().__init__()
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "displayableOrderId" in data:
            self.displayableOrderId: str = str(data["displayableOrderId"])
        else:
            self.displayableOrderId: str = None
        if "displayableOrderDate" in data:
            self.displayableOrderDate: Timestamp = Timestamp(data["displayableOrderDate"])
        else:
            self.displayableOrderDate: Timestamp = None
        if "displayableOrderComment" in data:
            self.displayableOrderComment: str = str(data["displayableOrderComment"])
        else:
            self.displayableOrderComment: str = None
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = ShippingSpeedCategory(data["shippingSpeedCategory"])
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "destinationAddress" in data:
            self.destinationAddress: Address = Address(data["destinationAddress"])
        else:
            self.destinationAddress: Address = None
        if "fulfillmentAction" in data:
            self.fulfillmentAction: FulfillmentAction = FulfillmentAction(data["fulfillmentAction"])
        else:
            self.fulfillmentAction: FulfillmentAction = None
        if "fulfillmentPolicy" in data:
            self.fulfillmentPolicy: FulfillmentPolicy = FulfillmentPolicy(data["fulfillmentPolicy"])
        else:
            self.fulfillmentPolicy: FulfillmentPolicy = None
        if "shipFromCountryCode" in data:
            self.shipFromCountryCode: str = str(data["shipFromCountryCode"])
        else:
            self.shipFromCountryCode: str = None
        if "notificationEmails" in data:
            self.notificationEmails: NotificationEmailList = NotificationEmailList(data["notificationEmails"])
        else:
            self.notificationEmails: NotificationEmailList = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []
        if "items" in data:
            self.items: UpdateFulfillmentOrderItemList = UpdateFulfillmentOrderItemList(data["items"])
        else:
            self.items: UpdateFulfillmentOrderItemList = None


class UpdateFulfillmentOrderResponse:
    def __init__(self, data):
        super().__init__()
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateFulfillmentOrderResponse:
    def __init__(self, data):
        super().__init__()
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CancelFulfillmentOrderResponse:
    def __init__(self, data):
        super().__init__()
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Weight:
    def __init__(self, data):
        super().__init__()
        if "unit" in data:
            self.unit: str = str(data["unit"])
        else:
            self.unit: str = None
        if "value" in data:
            self.value: str = str(data["value"])
        else:
            self.value: str = None


class GetFeatureInventoryResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: GetFeatureInventoryResult = GetFeatureInventoryResult(data["payload"])
        else:
            self.payload: GetFeatureInventoryResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeatureInventoryResult:
    def __init__(self, data):
        super().__init__()
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None
        if "featureSkus" in data:
            self.featureSkus: _List[FeatureSku] = [FeatureSku(datum) for datum in data["featureSkus"]]
        else:
            self.featureSkus: _List[FeatureSku] = []


class FeatureSku:
    def __init__(self, data):
        super().__init__()
        if "sellerSku" in data:
            self.sellerSku: str = str(data["sellerSku"])
        else:
            self.sellerSku: str = None
        if "fnSku" in data:
            self.fnSku: str = str(data["fnSku"])
        else:
            self.fnSku: str = None
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "skuCount" in data:
            self.skuCount: float = float(data["skuCount"])
        else:
            self.skuCount: float = None
        if "overlappingSkus" in data:
            self.overlappingSkus: _List[str] = [str(datum) for datum in data["overlappingSkus"]]
        else:
            self.overlappingSkus: _List[str] = []


class GetFeaturesResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: GetFeaturesResult = GetFeaturesResult(data["payload"])
        else:
            self.payload: GetFeaturesResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeaturesResult:
    def __init__(self, data):
        super().__init__()
        if "features" in data:
            self.features: Features = Features(data["features"])
        else:
            self.features: Features = None


class Feature:
    def __init__(self, data):
        super().__init__()
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "featureDescription" in data:
            self.featureDescription: str = str(data["featureDescription"])
        else:
            self.featureDescription: str = None
        if "sellerEligible" in data:
            self.sellerEligible: bool = bool(data["sellerEligible"])
        else:
            self.sellerEligible: bool = None


class GetFeatureSkuResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: GetFeatureSkuResult = GetFeatureSkuResult(data["payload"])
        else:
            self.payload: GetFeatureSkuResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeatureSkuResult:
    def __init__(self, data):
        super().__init__()
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "isEligible" in data:
            self.isEligible: bool = bool(data["isEligible"])
        else:
            self.isEligible: bool = None
        if "ineligibleReasons" in data:
            self.ineligibleReasons: _List[str] = [str(datum) for datum in data["ineligibleReasons"]]
        else:
            self.ineligibleReasons: _List[str] = []
        if "skuInfo" in data:
            self.skuInfo: FeatureSku = FeatureSku(data["skuInfo"])
        else:
            self.skuInfo: FeatureSku = None


class FeatureSettings:
    def __init__(self, data):
        super().__init__()
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "featureFulfillmentPolicy" in data:
            self.featureFulfillmentPolicy: str = str(data["featureFulfillmentPolicy"])
        else:
            self.featureFulfillmentPolicy: str = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])


class CreateFulfillmentOrderItemList(list, _List["CreateFulfillmentOrderItem"]):
    def __init__(self, data):
        super().__init__([CreateFulfillmentOrderItem(datum) for datum in data])


class CreateReturnItemList(list, _List["CreateReturnItem"]):
    def __init__(self, data):
        super().__init__([CreateReturnItem(datum) for datum in data])


class DeliveryWindowList(list, _List["DeliveryWindow"]):
    def __init__(self, data):
        super().__init__([DeliveryWindow(datum) for datum in data])


class FeeList(list, _List["Fee"]):
    def __init__(self, data):
        super().__init__([Fee(datum) for datum in data])


class FulfillmentOrderItemList(list, _List["FulfillmentOrderItem"]):
    def __init__(self, data):
        super().__init__([FulfillmentOrderItem(datum) for datum in data])


class FulfillmentPreviewItemList(list, _List["FulfillmentPreviewItem"]):
    def __init__(self, data):
        super().__init__([FulfillmentPreviewItem(datum) for datum in data])


class FulfillmentPreviewList(list, _List["FulfillmentPreview"]):
    def __init__(self, data):
        super().__init__([FulfillmentPreview(datum) for datum in data])


class FulfillmentPreviewShipmentList(list, _List["FulfillmentPreviewShipment"]):
    def __init__(self, data):
        super().__init__([FulfillmentPreviewShipment(datum) for datum in data])


class FulfillmentShipmentItemList(list, _List["FulfillmentShipmentItem"]):
    def __init__(self, data):
        super().__init__([FulfillmentShipmentItem(datum) for datum in data])


class FulfillmentShipmentList(list, _List["FulfillmentShipment"]):
    def __init__(self, data):
        super().__init__([FulfillmentShipment(datum) for datum in data])


class FulfillmentShipmentPackageList(list, _List["FulfillmentShipmentPackage"]):
    def __init__(self, data):
        super().__init__([FulfillmentShipmentPackage(datum) for datum in data])


class GetFulfillmentPreviewItemList(list, _List["GetFulfillmentPreviewItem"]):
    def __init__(self, data):
        super().__init__([GetFulfillmentPreviewItem(datum) for datum in data])


class InvalidReturnItemList(list, _List["InvalidReturnItem"]):
    def __init__(self, data):
        super().__init__([InvalidReturnItem(datum) for datum in data])


class NotificationEmailList(list, _List["str"]):
    def __init__(self, data):
        super().__init__([str(datum) for datum in data])


class ReasonCodeDetailsList(list, _List["ReasonCodeDetails"]):
    def __init__(self, data):
        super().__init__([ReasonCodeDetails(datum) for datum in data])


class ReturnAuthorizationList(list, _List["ReturnAuthorization"]):
    def __init__(self, data):
        super().__init__([ReturnAuthorization(datum) for datum in data])


class ReturnItemList(list, _List["ReturnItem"]):
    def __init__(self, data):
        super().__init__([ReturnItem(datum) for datum in data])


class ShippingSpeedCategoryList(list, _List["ShippingSpeedCategory"]):
    def __init__(self, data):
        super().__init__([ShippingSpeedCategory(datum) for datum in data])


class StringList(list, _List["str"]):
    def __init__(self, data):
        super().__init__([str(datum) for datum in data])


class TrackingEventList(list, _List["TrackingEvent"]):
    def __init__(self, data):
        super().__init__([TrackingEvent(datum) for datum in data])


class UnfulfillablePreviewItemList(list, _List["UnfulfillablePreviewItem"]):
    def __init__(self, data):
        super().__init__([UnfulfillablePreviewItem(datum) for datum in data])


class UpdateFulfillmentOrderItemList(list, _List["UpdateFulfillmentOrderItem"]):
    def __init__(self, data):
        super().__init__([UpdateFulfillmentOrderItem(datum) for datum in data])


class Features(list, _List["Feature"]):
    def __init__(self, data):
        super().__init__([Feature(datum) for datum in data])


FulfillmentPolicy = str
FulfillmentOrderStatus = str
Decimal = str
FulfillmentAction = str
FulfillmentReturnItemStatus = str
InvalidItemReasonCode = str
CurrentStatus = str
AdditionalLocationInfo = str
ReturnItemDisposition = str
Timestamp = str
EventCode = str
Quantity = int
ShippingSpeedCategory = str


class FulfillmentOutboundClient(__BaseClient):
    def getFulfillmentPreview(
        self,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/preview".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetFulfillmentPreviewResponse,
            400: GetFulfillmentPreviewResponse,
            401: GetFulfillmentPreviewResponse,
            403: GetFulfillmentPreviewResponse,
            404: GetFulfillmentPreviewResponse,
            429: GetFulfillmentPreviewResponse,
            500: GetFulfillmentPreviewResponse,
            503: GetFulfillmentPreviewResponse,
        }[response.status_code](response.json())

    def listAllFulfillmentOrders(
        self,
        queryStartDate: str = None,
        nextToken: str = None,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders".format()
        data = {}
        if queryStartDate is not None:
            data["queryStartDate"] = (queryStartDate,)
        if nextToken is not None:
            data["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=data)
        return {
            200: ListAllFulfillmentOrdersResponse,
            400: ListAllFulfillmentOrdersResponse,
            401: ListAllFulfillmentOrdersResponse,
            403: ListAllFulfillmentOrdersResponse,
            404: ListAllFulfillmentOrdersResponse,
            429: ListAllFulfillmentOrdersResponse,
            500: ListAllFulfillmentOrdersResponse,
            503: ListAllFulfillmentOrdersResponse,
        }[response.status_code](response.json())

    def createFulfillmentOrder(
        self,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: CreateFulfillmentOrderResponse,
            400: CreateFulfillmentOrderResponse,
            401: CreateFulfillmentOrderResponse,
            403: CreateFulfillmentOrderResponse,
            404: CreateFulfillmentOrderResponse,
            429: CreateFulfillmentOrderResponse,
            500: CreateFulfillmentOrderResponse,
            503: CreateFulfillmentOrderResponse,
        }[response.status_code](response.json())

    def getPackageTrackingDetails(
        self,
        packageNumber: int,
    ):
        url = "/fba/outbound/2020-07-01/tracking".format()
        data = {}
        if packageNumber is not None:
            data["packageNumber"] = (packageNumber,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetPackageTrackingDetailsResponse,
            400: GetPackageTrackingDetailsResponse,
            401: GetPackageTrackingDetailsResponse,
            403: GetPackageTrackingDetailsResponse,
            404: GetPackageTrackingDetailsResponse,
            429: GetPackageTrackingDetailsResponse,
            500: GetPackageTrackingDetailsResponse,
            503: GetPackageTrackingDetailsResponse,
        }[response.status_code](response.json())

    def listReturnReasonCodes(
        self,
        sellerSku: str,
        language: str,
        marketplaceId: str = None,
        sellerFulfillmentOrderId: str = None,
    ):
        url = "/fba/outbound/2020-07-01/returnReasonCodes".format()
        data = {}
        if sellerSku is not None:
            data["sellerSku"] = (sellerSku,)
        if marketplaceId is not None:
            data["marketplaceId"] = (marketplaceId,)
        if sellerFulfillmentOrderId is not None:
            data["sellerFulfillmentOrderId"] = (sellerFulfillmentOrderId,)
        if language is not None:
            data["language"] = (language,)
        response = self.request(url, method="GET", params=data)
        return {
            200: ListReturnReasonCodesResponse,
            400: ListReturnReasonCodesResponse,
            401: ListReturnReasonCodesResponse,
            403: ListReturnReasonCodesResponse,
            404: ListReturnReasonCodesResponse,
            429: ListReturnReasonCodesResponse,
            500: ListReturnReasonCodesResponse,
            503: ListReturnReasonCodesResponse,
        }[response.status_code](response.json())

    def createFulfillmentReturn(
        self,
        sellerFulfillmentOrderId: str,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
            200: CreateFulfillmentReturnResponse,
            400: CreateFulfillmentReturnResponse,
            401: CreateFulfillmentReturnResponse,
            403: CreateFulfillmentReturnResponse,
            404: CreateFulfillmentReturnResponse,
            429: CreateFulfillmentReturnResponse,
            500: CreateFulfillmentReturnResponse,
            503: CreateFulfillmentReturnResponse,
        }[response.status_code](response.json())

    def getFulfillmentOrder(
        self,
        sellerFulfillmentOrderId: str,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        data = {}
        response = self.request(url, method="GET", params=data)
        return {
            200: GetFulfillmentOrderResponse,
            400: GetFulfillmentOrderResponse,
            401: GetFulfillmentOrderResponse,
            403: GetFulfillmentOrderResponse,
            404: GetFulfillmentOrderResponse,
            429: GetFulfillmentOrderResponse,
            500: GetFulfillmentOrderResponse,
            503: GetFulfillmentOrderResponse,
        }[response.status_code](response.json())

    def updateFulfillmentOrder(
        self,
        sellerFulfillmentOrderId: str,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
            200: UpdateFulfillmentOrderResponse,
            400: UpdateFulfillmentOrderResponse,
            401: UpdateFulfillmentOrderResponse,
            403: UpdateFulfillmentOrderResponse,
            404: UpdateFulfillmentOrderResponse,
            429: UpdateFulfillmentOrderResponse,
            500: UpdateFulfillmentOrderResponse,
            503: UpdateFulfillmentOrderResponse,
        }[response.status_code](response.json())

    def cancelFulfillmentOrder(
        self,
        sellerFulfillmentOrderId: str,
    ):
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
            200: CancelFulfillmentOrderResponse,
            400: CancelFulfillmentOrderResponse,
            401: CancelFulfillmentOrderResponse,
            403: CancelFulfillmentOrderResponse,
            404: CancelFulfillmentOrderResponse,
            429: CancelFulfillmentOrderResponse,
            500: CancelFulfillmentOrderResponse,
            503: CancelFulfillmentOrderResponse,
        }[response.status_code](response.json())

    def getFeatures(
        self,
        marketplaceId: str,
    ):
        url = "/fba/outbound/2020-07-01/features".format()
        data = {}
        if marketplaceId is not None:
            data["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetFeaturesResponse,
            400: GetFeaturesResponse,
            401: GetFeaturesResponse,
            403: GetFeaturesResponse,
            404: GetFeaturesResponse,
            429: GetFeaturesResponse,
            500: GetFeaturesResponse,
            503: GetFeaturesResponse,
        }[response.status_code](response.json())

    def getFeatureInventory(
        self,
        featureName: str,
        marketplaceId: str,
        nextToken: str = None,
    ):
        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}".format(
            featureName=featureName,
        )
        data = {}
        if marketplaceId is not None:
            data["marketplaceId"] = (marketplaceId,)
        if nextToken is not None:
            data["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetFeatureInventoryResponse,
            400: GetFeatureInventoryResponse,
            401: GetFeatureInventoryResponse,
            403: GetFeatureInventoryResponse,
            404: GetFeatureInventoryResponse,
            429: GetFeatureInventoryResponse,
            500: GetFeatureInventoryResponse,
            503: GetFeatureInventoryResponse,
        }[response.status_code](response.json())

    def getFeatureSKU(
        self,
        featureName: str,
        sellerSku: str,
        marketplaceId: str,
    ):
        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}".format(
            featureName=featureName,
            sellerSku=sellerSku,
        )
        data = {}
        if marketplaceId is not None:
            data["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetFeatureSkuResponse,
            400: GetFeatureSkuResponse,
            401: GetFeatureSkuResponse,
            403: GetFeatureSkuResponse,
            404: GetFeatureSkuResponse,
            429: GetFeatureSkuResponse,
            500: GetFeatureSkuResponse,
            503: GetFeatureSkuResponse,
        }[response.status_code](response.json())
