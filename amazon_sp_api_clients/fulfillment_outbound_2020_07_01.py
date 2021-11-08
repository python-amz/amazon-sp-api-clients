from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


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
    """
    The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "isCodRequired" in data:
            self.isCodRequired: bool = convert_bool(data["isCodRequired"])
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
    """
    Item information for creating a fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The request body schema for the createFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The createFulfillmentReturn operation creates a fulfillment return for items that were fulfilled using the createFulfillmentOrder operation. For calls to createFulfillmentReturn, you must include ReturnReasonCode values returned by a previous call to the listReturnReasonCodes operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "items" in data:
            self.items: CreateReturnItemList = CreateReturnItemList(data["items"])
        else:
            self.items: CreateReturnItemList = None


class CreateFulfillmentReturnResult:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The response schema for the createFulfillmentReturn operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateFulfillmentReturnResult = CreateFulfillmentReturnResult(data["payload"])
        else:
            self.payload: CreateFulfillmentReturnResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateReturnItem:
    """
    An item that Amazon accepted for return.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
        if "value" in data:
            self.value: Decimal = Decimal(data["value"])
        else:
            self.value: Decimal = None


class DeliveryWindow:
    """
    The time range within which a Scheduled Delivery fulfillment order should be delivered.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "startDate" in data:
            self.startDate: Timestamp = Timestamp(data["startDate"])
        else:
            self.startDate: Timestamp = None
        if "endDate" in data:
            self.endDate: Timestamp = Timestamp(data["endDate"])
        else:
            self.endDate: Timestamp = None


class Fee:
    """
    Fee type and cost.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "amount" in data:
            self.amount: Money = Money(data["amount"])
        else:
            self.amount: Money = None


class FulfillmentOrder:
    """
    General information about a fulfillment order, including its status.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Item information for a fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Information about a fulfillment order preview, including delivery and fee information based on shipping method.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = ShippingSpeedCategory(data["shippingSpeedCategory"])
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "scheduledDeliveryInfo" in data:
            self.scheduledDeliveryInfo: ScheduledDeliveryInfo = ScheduledDeliveryInfo(data["scheduledDeliveryInfo"])
        else:
            self.scheduledDeliveryInfo: ScheduledDeliveryInfo = None
        if "isFulfillable" in data:
            self.isFulfillable: bool = convert_bool(data["isFulfillable"])
        else:
            self.isFulfillable: bool = None
        if "isCODCapable" in data:
            self.isCODCapable: bool = convert_bool(data["isCODCapable"])
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
    """
    Item information for a shipment in a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Delivery and item information for a shipment in a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Delivery and item information for a shipment in a fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Item information for a shipment in a fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Package information for a shipment in a fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The response schema for the getFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetFulfillmentOrderResult = GetFulfillmentOrderResult(data["payload"])
        else:
            self.payload: GetFulfillmentOrderResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFulfillmentPreviewItem:
    """
    Item information for a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The request body schema for the getFulfillmentPreview operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
            self.includeCODFulfillmentPreview: bool = convert_bool(data["includeCODFulfillmentPreview"])
        else:
            self.includeCODFulfillmentPreview: bool = None
        if "includeDeliveryWindows" in data:
            self.includeDeliveryWindows: bool = convert_bool(data["includeDeliveryWindows"])
        else:
            self.includeDeliveryWindows: bool = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class GetFulfillmentPreviewResult:
    """
    A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated ship dates and arrival dates.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "fulfillmentPreviews" in data:
            self.fulfillmentPreviews: FulfillmentPreviewList = FulfillmentPreviewList(data["fulfillmentPreviews"])
        else:
            self.fulfillmentPreviews: FulfillmentPreviewList = None


class GetFulfillmentPreviewResponse:
    """
    The response schema for the getFulfillmentPreview operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetFulfillmentPreviewResult = GetFulfillmentPreviewResult(data["payload"])
        else:
            self.payload: GetFulfillmentPreviewResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class InvalidItemReason:
    """
    The reason that the item is invalid for return.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "invalidItemReasonCode" in data:
            self.invalidItemReasonCode: InvalidItemReasonCode = InvalidItemReasonCode(data["invalidItemReasonCode"])
        else:
            self.invalidItemReasonCode: InvalidItemReasonCode = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None


class InvalidReturnItem:
    """
    An item that is invalid for return.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The response schema for the listAllFulfillmentOrders operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ListAllFulfillmentOrdersResult = ListAllFulfillmentOrdersResult(data["payload"])
        else:
            self.payload: ListAllFulfillmentOrdersResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ListReturnReasonCodesResult:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reasonCodeDetails" in data:
            self.reasonCodeDetails: ReasonCodeDetailsList = ReasonCodeDetailsList(data["reasonCodeDetails"])
        else:
            self.reasonCodeDetails: ReasonCodeDetailsList = None


class ListReturnReasonCodesResponse:
    """
    The response schema for the listReturnReasonCodes operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ListReturnReasonCodesResult = ListReturnReasonCodesResult(data["payload"])
        else:
            self.payload: ListReturnReasonCodesResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class PackageTrackingDetails:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The response schema for the getPackageTrackingDetails operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: PackageTrackingDetails = PackageTrackingDetails(data["payload"])
        else:
            self.payload: PackageTrackingDetails = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ReasonCodeDetails:
    """
    A return reason code, a description, and an optional description translation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Return authorization information for items accepted for return.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    An item that Amazon accepted for return.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Delivery information for a scheduled delivery.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "deliveryTimeZone" in data:
            self.deliveryTimeZone: str = str(data["deliveryTimeZone"])
        else:
            self.deliveryTimeZone: str = None
        if "deliveryWindows" in data:
            self.deliveryWindows: DeliveryWindowList = DeliveryWindowList(data["deliveryWindows"])
        else:
            self.deliveryWindows: DeliveryWindowList = None


class TrackingAddress:
    """
    Address information for tracking the package.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Information for tracking package deliveries.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Information about unfulfillable items in a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Item information for updating a fulfillment order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The response schema for the updateFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateFulfillmentOrderResponse:
    """
    The response schema for the createFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CancelFulfillmentOrderResponse:
    """
    The response schema for the cancelFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Weight:
    """
    The weight.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "unit" in data:
            self.unit: str = str(data["unit"])
        else:
            self.unit: str = None
        if "value" in data:
            self.value: str = str(data["value"])
        else:
            self.value: str = None


class GetFeatureInventoryResponse:
    """
    The breakdown of eligibility inventory by feature.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetFeatureInventoryResult = GetFeatureInventoryResult(data["payload"])
        else:
            self.payload: GetFeatureInventoryResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeatureInventoryResult:
    """
    The payload for the getEligibileInventory operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
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
    """
    The response schema for the getFeatures operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetFeaturesResult = GetFeaturesResult(data["payload"])
        else:
            self.payload: GetFeaturesResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeaturesResult:
    """
    The payload for the getFeatures operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "features" in data:
            self.features: Features = Features(data["features"])
        else:
            self.features: Features = None


class Feature:
    """
    A Multi-Channel Fulfillment feature.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "featureDescription" in data:
            self.featureDescription: str = str(data["featureDescription"])
        else:
            self.featureDescription: str = None
        if "sellerEligible" in data:
            self.sellerEligible: bool = convert_bool(data["sellerEligible"])
        else:
            self.sellerEligible: bool = None


class GetFeatureSkuResponse:
    """
    The response schema for the getFeatureSKU operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetFeatureSkuResult = GetFeatureSkuResult(data["payload"])
        else:
            self.payload: GetFeatureSkuResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeatureSkuResult:
    """
    The payload for the getFeatureSKU operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "isEligible" in data:
            self.isEligible: bool = convert_bool(data["isEligible"])
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
    """
    FeatureSettings allows users to apply fulfillment features to an order. To block an order from being shipped using Amazon Logistics (AMZL) and an AMZL tracking number, use featureName as BLOCK_AMZL and featureFulfillmentPolicy as Required. Blocking AMZL will incur an additional fee surcharge on your MCF orders and increase the risk of some of your orders being unfulfilled or delivered late if there are no alternative carriers available. Using BLOCK_AMZL in an order request will take precedence over your Seller Central account setting.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "featureName" in data:
            self.featureName: str = str(data["featureName"])
        else:
            self.featureName: str = None
        if "featureFulfillmentPolicy" in data:
            self.featureFulfillmentPolicy: str = str(data["featureFulfillmentPolicy"])
        else:
            self.featureFulfillmentPolicy: str = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class CreateFulfillmentOrderItemList(list, _List["CreateFulfillmentOrderItem"]):
    """
    An array of item information for creating a fulfillment order.
    """

    def __init__(self, data):
        super().__init__([CreateFulfillmentOrderItem(datum) for datum in data])
        self.data = data


class CreateReturnItemList(list, _List["CreateReturnItem"]):
    """
    An array of items to be returned.
    """

    def __init__(self, data):
        super().__init__([CreateReturnItem(datum) for datum in data])
        self.data = data


class DeliveryWindowList(list, _List["DeliveryWindow"]):
    """
    An array of delivery windows.
    """

    def __init__(self, data):
        super().__init__([DeliveryWindow(datum) for datum in data])
        self.data = data


class FeeList(list, _List["Fee"]):
    """
    An array of fee type and cost pairs.
    """

    def __init__(self, data):
        super().__init__([Fee(datum) for datum in data])
        self.data = data


class FulfillmentOrderItemList(list, _List["FulfillmentOrderItem"]):
    """
    An array of fulfillment order item information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentOrderItem(datum) for datum in data])
        self.data = data


class FulfillmentPreviewItemList(list, _List["FulfillmentPreviewItem"]):
    """
    An array of fulfillment preview item information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentPreviewItem(datum) for datum in data])
        self.data = data


class FulfillmentPreviewList(list, _List["FulfillmentPreview"]):
    """
    An array of fulfillment preview information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentPreview(datum) for datum in data])
        self.data = data


class FulfillmentPreviewShipmentList(list, _List["FulfillmentPreviewShipment"]):
    """
    An array of fulfillment preview shipment information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentPreviewShipment(datum) for datum in data])
        self.data = data


class FulfillmentShipmentItemList(list, _List["FulfillmentShipmentItem"]):
    """
    An array of fulfillment shipment item information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentShipmentItem(datum) for datum in data])
        self.data = data


class FulfillmentShipmentList(list, _List["FulfillmentShipment"]):
    """
    An array of fulfillment shipment information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentShipment(datum) for datum in data])
        self.data = data


class FulfillmentShipmentPackageList(list, _List["FulfillmentShipmentPackage"]):
    """
    An array of fulfillment shipment package information.
    """

    def __init__(self, data):
        super().__init__([FulfillmentShipmentPackage(datum) for datum in data])
        self.data = data


class GetFulfillmentPreviewItemList(list, _List["GetFulfillmentPreviewItem"]):
    """
    An array of fulfillment preview item information.
    """

    def __init__(self, data):
        super().__init__([GetFulfillmentPreviewItem(datum) for datum in data])
        self.data = data


class InvalidReturnItemList(list, _List["InvalidReturnItem"]):
    """
    An array of invalid return item information.
    """

    def __init__(self, data):
        super().__init__([InvalidReturnItem(datum) for datum in data])
        self.data = data


class NotificationEmailList(list, _List["str"]):
    """
    A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ReasonCodeDetailsList(list, _List["ReasonCodeDetails"]):
    """
    An array of return reason code details.
    """

    def __init__(self, data):
        super().__init__([ReasonCodeDetails(datum) for datum in data])
        self.data = data


class ReturnAuthorizationList(list, _List["ReturnAuthorization"]):
    """
    An array of return authorization information.
    """

    def __init__(self, data):
        super().__init__([ReturnAuthorization(datum) for datum in data])
        self.data = data


class ReturnItemList(list, _List["ReturnItem"]):
    """
    An array of items that Amazon accepted for return. Returns empty if no items were accepted for return.
    """

    def __init__(self, data):
        super().__init__([ReturnItem(datum) for datum in data])
        self.data = data


class ShippingSpeedCategoryList(list, _List["ShippingSpeedCategory"]):
    """ """

    def __init__(self, data):
        super().__init__([ShippingSpeedCategory(datum) for datum in data])
        self.data = data


class StringList(list, _List["str"]):
    """ """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class TrackingEventList(list, _List["TrackingEvent"]):
    """
    An array of tracking event information.
    """

    def __init__(self, data):
        super().__init__([TrackingEvent(datum) for datum in data])
        self.data = data


class UnfulfillablePreviewItemList(list, _List["UnfulfillablePreviewItem"]):
    """
    An array of unfulfillable preview item information.
    """

    def __init__(self, data):
        super().__init__([UnfulfillablePreviewItem(datum) for datum in data])
        self.data = data


class UpdateFulfillmentOrderItemList(list, _List["UpdateFulfillmentOrderItem"]):
    """
    An array of fulfillment order item information for updating a fulfillment order.
    """

    def __init__(self, data):
        super().__init__([UpdateFulfillmentOrderItem(datum) for datum in data])
        self.data = data


class Features(list, _List["Feature"]):
    """
    An array of features.
    """

    def __init__(self, data):
        super().__init__([Feature(datum) for datum in data])
        self.data = data


class FulfillmentPolicy(str):
    """
    The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
    """


class FulfillmentOrderStatus(str):
    """
    The current status of the fulfillment order.
    """


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """


class FulfillmentAction(str):
    """
    Specifies whether the fulfillment order should ship now or have an order hold put on it.
    """


class FulfillmentReturnItemStatus(str):
    """
    Indicates if the return item has been processed by a fulfillment center.
    """


class InvalidItemReasonCode(str):
    """
    A code for why the item is invalid for return.
    """


class CurrentStatus(str):
    """
    The current delivery status of the package.
    """


class AdditionalLocationInfo(str):
    """
    Additional location information.
    """


class ReturnItemDisposition(str):
    """
    The condition of the return item when received by an Amazon fulfillment center.
    """


class Timestamp(str):
    """ """


class EventCode(str):
    """
    The event code for the delivery event.
    """


class Quantity(int):
    """
    The item quantity.
    """


class ShippingSpeedCategory(str):
    """
    The shipping method used for the fulfillment order.
    """


class FulfillmentOutbound20200701Client(__BaseClient):
    def getFulfillmentPreview(
        self,
        data: GetFulfillmentPreviewRequest,
    ):
        """
                Returns a list of fulfillment order previews based on shipping criteria that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/preview".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: GetFulfillmentPreviewResponse,
            400: GetFulfillmentPreviewResponse,
            401: GetFulfillmentPreviewResponse,
            403: GetFulfillmentPreviewResponse,
            404: GetFulfillmentPreviewResponse,
            429: GetFulfillmentPreviewResponse,
            500: GetFulfillmentPreviewResponse,
            503: GetFulfillmentPreviewResponse,
        }[response.status_code](self._get_response_json(response))

    def listAllFulfillmentOrders(
        self,
        queryStartDate: str = None,
        nextToken: str = None,
    ):
        """
                Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the next token parameter.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders".format()
        params = {}
        if queryStartDate is not None:
            params["queryStartDate"] = queryStartDate
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(url, method="GET", params=params)
        return {
            200: ListAllFulfillmentOrdersResponse,
            400: ListAllFulfillmentOrdersResponse,
            401: ListAllFulfillmentOrdersResponse,
            403: ListAllFulfillmentOrdersResponse,
            404: ListAllFulfillmentOrdersResponse,
            429: ListAllFulfillmentOrdersResponse,
            500: ListAllFulfillmentOrdersResponse,
            503: ListAllFulfillmentOrdersResponse,
        }[response.status_code](self._get_response_json(response))

    def createFulfillmentOrder(
        self,
        data: CreateFulfillmentOrderRequest,
    ):
        """
                Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: CreateFulfillmentOrderResponse,
            400: CreateFulfillmentOrderResponse,
            401: CreateFulfillmentOrderResponse,
            403: CreateFulfillmentOrderResponse,
            404: CreateFulfillmentOrderResponse,
            429: CreateFulfillmentOrderResponse,
            500: CreateFulfillmentOrderResponse,
            503: CreateFulfillmentOrderResponse,
        }[response.status_code](self._get_response_json(response))

    def getPackageTrackingDetails(
        self,
        packageNumber: int,
    ):
        """
                Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/tracking".format()
        params = {}
        if packageNumber is not None:
            params["packageNumber"] = packageNumber
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPackageTrackingDetailsResponse,
            400: GetPackageTrackingDetailsResponse,
            401: GetPackageTrackingDetailsResponse,
            403: GetPackageTrackingDetailsResponse,
            404: GetPackageTrackingDetailsResponse,
            429: GetPackageTrackingDetailsResponse,
            500: GetPackageTrackingDetailsResponse,
            503: GetPackageTrackingDetailsResponse,
        }[response.status_code](self._get_response_json(response))

    def listReturnReasonCodes(
        self,
        sellerSku: str,
        language: str,
        marketplaceId: str = None,
        sellerFulfillmentOrderId: str = None,
    ):
        """
                Returns a list of return reason codes for a seller SKU in a given marketplace.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/returnReasonCodes".format()
        params = {}
        if sellerSku is not None:
            params["sellerSku"] = sellerSku
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if sellerFulfillmentOrderId is not None:
            params["sellerFulfillmentOrderId"] = sellerFulfillmentOrderId
        if language is not None:
            params["language"] = language
        response = self.request(url, method="GET", params=params)
        return {
            200: ListReturnReasonCodesResponse,
            400: ListReturnReasonCodesResponse,
            401: ListReturnReasonCodesResponse,
            403: ListReturnReasonCodesResponse,
            404: ListReturnReasonCodesResponse,
            429: ListReturnReasonCodesResponse,
            500: ListReturnReasonCodesResponse,
            503: ListReturnReasonCodesResponse,
        }[response.status_code](self._get_response_json(response))

    def createFulfillmentReturn(
        self,
        sellerFulfillmentOrderId: str,
    ):
        """
                Creates a fulfillment return.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        params = {}
        response = self.request(url, method="PUT", data=params)
        return {
            200: CreateFulfillmentReturnResponse,
            400: CreateFulfillmentReturnResponse,
            401: CreateFulfillmentReturnResponse,
            403: CreateFulfillmentReturnResponse,
            404: CreateFulfillmentReturnResponse,
            429: CreateFulfillmentReturnResponse,
            500: CreateFulfillmentReturnResponse,
            503: CreateFulfillmentReturnResponse,
        }[response.status_code](self._get_response_json(response))

    def getFulfillmentOrder(
        self,
        sellerFulfillmentOrderId: str,
    ):
        """
                Returns the fulfillment order indicated by the specified order identifier.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFulfillmentOrderResponse,
            400: GetFulfillmentOrderResponse,
            401: GetFulfillmentOrderResponse,
            403: GetFulfillmentOrderResponse,
            404: GetFulfillmentOrderResponse,
            429: GetFulfillmentOrderResponse,
            500: GetFulfillmentOrderResponse,
            503: GetFulfillmentOrderResponse,
        }[response.status_code](self._get_response_json(response))

    def updateFulfillmentOrder(
        self,
        sellerFulfillmentOrderId: str,
    ):
        """
                Updates and/or requests shipment for a fulfillment order with an order hold on it.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        params = {}
        response = self.request(url, method="PUT", data=params)
        return {
            200: UpdateFulfillmentOrderResponse,
            400: UpdateFulfillmentOrderResponse,
            401: UpdateFulfillmentOrderResponse,
            403: UpdateFulfillmentOrderResponse,
            404: UpdateFulfillmentOrderResponse,
            429: UpdateFulfillmentOrderResponse,
            500: UpdateFulfillmentOrderResponse,
            503: UpdateFulfillmentOrderResponse,
        }[response.status_code](self._get_response_json(response))

    def cancelFulfillmentOrder(
        self,
        sellerFulfillmentOrderId: str,
    ):
        """
                Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel".format(
            sellerFulfillmentOrderId=sellerFulfillmentOrderId,
        )
        params = {}
        response = self.request(url, method="PUT", data=params)
        return {
            200: CancelFulfillmentOrderResponse,
            400: CancelFulfillmentOrderResponse,
            401: CancelFulfillmentOrderResponse,
            403: CancelFulfillmentOrderResponse,
            404: CancelFulfillmentOrderResponse,
            429: CancelFulfillmentOrderResponse,
            500: CancelFulfillmentOrderResponse,
            503: CancelFulfillmentOrderResponse,
        }[response.status_code](self._get_response_json(response))

    def getFeatures(
        self,
        marketplaceId: str,
    ):
        """
                Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/features".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFeaturesResponse,
            400: GetFeaturesResponse,
            401: GetFeaturesResponse,
            403: GetFeaturesResponse,
            404: GetFeaturesResponse,
            429: GetFeaturesResponse,
            500: GetFeaturesResponse,
            503: GetFeaturesResponse,
        }[response.status_code](self._get_response_json(response))

    def getFeatureInventory(
        self,
        featureName: str,
        marketplaceId: str,
        nextToken: str = None,
    ):
        """
                Returns a list of inventory items that are eligible for the fulfillment feature you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}".format(
            featureName=featureName,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFeatureInventoryResponse,
            400: GetFeatureInventoryResponse,
            401: GetFeatureInventoryResponse,
            403: GetFeatureInventoryResponse,
            404: GetFeatureInventoryResponse,
            429: GetFeatureInventoryResponse,
            500: GetFeatureInventoryResponse,
            503: GetFeatureInventoryResponse,
        }[response.status_code](self._get_response_json(response))

    def getFeatureSKU(
        self,
        featureName: str,
        sellerSku: str,
        marketplaceId: str,
    ):
        """
                Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty skuInfo object.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}".format(
            featureName=featureName,
            sellerSku=sellerSku,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFeatureSkuResponse,
            400: GetFeatureSkuResponse,
            401: GetFeatureSkuResponse,
            403: GetFeatureSkuResponse,
            404: GetFeatureSkuResponse,
            429: GetFeatureSkuResponse,
            500: GetFeatureSkuResponse,
            503: GetFeatureSkuResponse,
        }[response.status_code](self._get_response_json(response))
