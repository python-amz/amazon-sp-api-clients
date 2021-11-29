from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


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
        if "districtOrCounty" in data:
            self.districtOrCounty: str = self._get_value(str, "districtOrCounty")
        else:
            self.districtOrCounty: str = None
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


class CODSettings(__BaseDictObject):
    """
    The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isCodRequired" in data:
            self.isCodRequired: bool = self._get_value(convert_bool, "isCodRequired")
        else:
            self.isCodRequired: bool = None
        if "codCharge" in data:
            self.codCharge: Money = self._get_value(Money, "codCharge")
        else:
            self.codCharge: Money = None
        if "codChargeTax" in data:
            self.codChargeTax: Money = self._get_value(Money, "codChargeTax")
        else:
            self.codChargeTax: Money = None
        if "shippingCharge" in data:
            self.shippingCharge: Money = self._get_value(Money, "shippingCharge")
        else:
            self.shippingCharge: Money = None
        if "shippingChargeTax" in data:
            self.shippingChargeTax: Money = self._get_value(Money, "shippingChargeTax")
        else:
            self.shippingChargeTax: Money = None


class CreateFulfillmentOrderItem(__BaseDictObject):
    """
    Item information for creating a fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "giftMessage" in data:
            self.giftMessage: str = self._get_value(str, "giftMessage")
        else:
            self.giftMessage: str = None
        if "displayableComment" in data:
            self.displayableComment: str = self._get_value(str, "displayableComment")
        else:
            self.displayableComment: str = None
        if "fulfillmentNetworkSku" in data:
            self.fulfillmentNetworkSku: str = self._get_value(str, "fulfillmentNetworkSku")
        else:
            self.fulfillmentNetworkSku: str = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = self._get_value(Money, "perUnitDeclaredValue")
        else:
            self.perUnitDeclaredValue: Money = None
        if "perUnitPrice" in data:
            self.perUnitPrice: Money = self._get_value(Money, "perUnitPrice")
        else:
            self.perUnitPrice: Money = None
        if "perUnitTax" in data:
            self.perUnitTax: Money = self._get_value(Money, "perUnitTax")
        else:
            self.perUnitTax: Money = None


class CreateFulfillmentOrderRequest(__BaseDictObject):
    """
    The request body schema for the createFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "sellerFulfillmentOrderId" in data:
            self.sellerFulfillmentOrderId: str = self._get_value(str, "sellerFulfillmentOrderId")
        else:
            self.sellerFulfillmentOrderId: str = None
        if "displayableOrderId" in data:
            self.displayableOrderId: str = self._get_value(str, "displayableOrderId")
        else:
            self.displayableOrderId: str = None
        if "displayableOrderDate" in data:
            self.displayableOrderDate: Timestamp = self._get_value(Timestamp, "displayableOrderDate")
        else:
            self.displayableOrderDate: Timestamp = None
        if "displayableOrderComment" in data:
            self.displayableOrderComment: str = self._get_value(str, "displayableOrderComment")
        else:
            self.displayableOrderComment: str = None
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = self._get_value(
                ShippingSpeedCategory, "shippingSpeedCategory"
            )
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "deliveryWindow" in data:
            self.deliveryWindow: DeliveryWindow = self._get_value(DeliveryWindow, "deliveryWindow")
        else:
            self.deliveryWindow: DeliveryWindow = None
        if "destinationAddress" in data:
            self.destinationAddress: Address = self._get_value(Address, "destinationAddress")
        else:
            self.destinationAddress: Address = None
        if "fulfillmentAction" in data:
            self.fulfillmentAction: FulfillmentAction = self._get_value(FulfillmentAction, "fulfillmentAction")
        else:
            self.fulfillmentAction: FulfillmentAction = None
        if "fulfillmentPolicy" in data:
            self.fulfillmentPolicy: FulfillmentPolicy = self._get_value(FulfillmentPolicy, "fulfillmentPolicy")
        else:
            self.fulfillmentPolicy: FulfillmentPolicy = None
        if "codSettings" in data:
            self.codSettings: CODSettings = self._get_value(CODSettings, "codSettings")
        else:
            self.codSettings: CODSettings = None
        if "shipFromCountryCode" in data:
            self.shipFromCountryCode: str = self._get_value(str, "shipFromCountryCode")
        else:
            self.shipFromCountryCode: str = None
        if "notificationEmails" in data:
            self.notificationEmails: NotificationEmailList = self._get_value(
                NotificationEmailList, "notificationEmails"
            )
        else:
            self.notificationEmails: NotificationEmailList = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []
        if "items" in data:
            self.items: CreateFulfillmentOrderItemList = self._get_value(CreateFulfillmentOrderItemList, "items")
        else:
            self.items: CreateFulfillmentOrderItemList = None


class CreateFulfillmentReturnRequest(__BaseDictObject):
    """
    The createFulfillmentReturn operation creates a fulfillment return for items that were fulfilled using the createFulfillmentOrder operation. For calls to createFulfillmentReturn, you must include ReturnReasonCode values returned by a previous call to the listReturnReasonCodes operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "items" in data:
            self.items: CreateReturnItemList = self._get_value(CreateReturnItemList, "items")
        else:
            self.items: CreateReturnItemList = None


class CreateFulfillmentReturnResult(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "returnItems" in data:
            self.returnItems: ReturnItemList = self._get_value(ReturnItemList, "returnItems")
        else:
            self.returnItems: ReturnItemList = None
        if "invalidReturnItems" in data:
            self.invalidReturnItems: InvalidReturnItemList = self._get_value(
                InvalidReturnItemList, "invalidReturnItems"
            )
        else:
            self.invalidReturnItems: InvalidReturnItemList = None
        if "returnAuthorizations" in data:
            self.returnAuthorizations: ReturnAuthorizationList = self._get_value(
                ReturnAuthorizationList, "returnAuthorizations"
            )
        else:
            self.returnAuthorizations: ReturnAuthorizationList = None


class CreateFulfillmentReturnResponse(__BaseDictObject):
    """
    The response schema for the createFulfillmentReturn operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CreateFulfillmentReturnResult = self._get_value(CreateFulfillmentReturnResult, "payload")
        else:
            self.payload: CreateFulfillmentReturnResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateReturnItem(__BaseDictObject):
    """
    An item that Amazon accepted for return.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerReturnItemId" in data:
            self.sellerReturnItemId: str = self._get_value(str, "sellerReturnItemId")
        else:
            self.sellerReturnItemId: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "amazonShipmentId" in data:
            self.amazonShipmentId: str = self._get_value(str, "amazonShipmentId")
        else:
            self.amazonShipmentId: str = None
        if "returnReasonCode" in data:
            self.returnReasonCode: str = self._get_value(str, "returnReasonCode")
        else:
            self.returnReasonCode: str = None
        if "returnComment" in data:
            self.returnComment: str = self._get_value(str, "returnComment")
        else:
            self.returnComment: str = None


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
        if "value" in data:
            self.value: Decimal = self._get_value(Decimal, "value")
        else:
            self.value: Decimal = None


class DeliveryWindow(__BaseDictObject):
    """
    The time range within which a Scheduled Delivery fulfillment order should be delivered.
    """

    def __init__(self, data):
        super().__init__(data)
        if "startDate" in data:
            self.startDate: Timestamp = self._get_value(Timestamp, "startDate")
        else:
            self.startDate: Timestamp = None
        if "endDate" in data:
            self.endDate: Timestamp = self._get_value(Timestamp, "endDate")
        else:
            self.endDate: Timestamp = None


class Fee(__BaseDictObject):
    """
    Fee type and cost.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "amount" in data:
            self.amount: Money = self._get_value(Money, "amount")
        else:
            self.amount: Money = None


class FulfillmentOrder(__BaseDictObject):
    """
    General information about a fulfillment order, including its status.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerFulfillmentOrderId" in data:
            self.sellerFulfillmentOrderId: str = self._get_value(str, "sellerFulfillmentOrderId")
        else:
            self.sellerFulfillmentOrderId: str = None
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "displayableOrderId" in data:
            self.displayableOrderId: str = self._get_value(str, "displayableOrderId")
        else:
            self.displayableOrderId: str = None
        if "displayableOrderDate" in data:
            self.displayableOrderDate: Timestamp = self._get_value(Timestamp, "displayableOrderDate")
        else:
            self.displayableOrderDate: Timestamp = None
        if "displayableOrderComment" in data:
            self.displayableOrderComment: str = self._get_value(str, "displayableOrderComment")
        else:
            self.displayableOrderComment: str = None
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = self._get_value(
                ShippingSpeedCategory, "shippingSpeedCategory"
            )
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "deliveryWindow" in data:
            self.deliveryWindow: DeliveryWindow = self._get_value(DeliveryWindow, "deliveryWindow")
        else:
            self.deliveryWindow: DeliveryWindow = None
        if "destinationAddress" in data:
            self.destinationAddress: Address = self._get_value(Address, "destinationAddress")
        else:
            self.destinationAddress: Address = None
        if "fulfillmentAction" in data:
            self.fulfillmentAction: FulfillmentAction = self._get_value(FulfillmentAction, "fulfillmentAction")
        else:
            self.fulfillmentAction: FulfillmentAction = None
        if "fulfillmentPolicy" in data:
            self.fulfillmentPolicy: FulfillmentPolicy = self._get_value(FulfillmentPolicy, "fulfillmentPolicy")
        else:
            self.fulfillmentPolicy: FulfillmentPolicy = None
        if "codSettings" in data:
            self.codSettings: CODSettings = self._get_value(CODSettings, "codSettings")
        else:
            self.codSettings: CODSettings = None
        if "receivedDate" in data:
            self.receivedDate: Timestamp = self._get_value(Timestamp, "receivedDate")
        else:
            self.receivedDate: Timestamp = None
        if "fulfillmentOrderStatus" in data:
            self.fulfillmentOrderStatus: FulfillmentOrderStatus = self._get_value(
                FulfillmentOrderStatus, "fulfillmentOrderStatus"
            )
        else:
            self.fulfillmentOrderStatus: FulfillmentOrderStatus = None
        if "statusUpdatedDate" in data:
            self.statusUpdatedDate: Timestamp = self._get_value(Timestamp, "statusUpdatedDate")
        else:
            self.statusUpdatedDate: Timestamp = None
        if "notificationEmails" in data:
            self.notificationEmails: NotificationEmailList = self._get_value(
                NotificationEmailList, "notificationEmails"
            )
        else:
            self.notificationEmails: NotificationEmailList = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class FulfillmentOrderItem(__BaseDictObject):
    """
    Item information for a fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "giftMessage" in data:
            self.giftMessage: str = self._get_value(str, "giftMessage")
        else:
            self.giftMessage: str = None
        if "displayableComment" in data:
            self.displayableComment: str = self._get_value(str, "displayableComment")
        else:
            self.displayableComment: str = None
        if "fulfillmentNetworkSku" in data:
            self.fulfillmentNetworkSku: str = self._get_value(str, "fulfillmentNetworkSku")
        else:
            self.fulfillmentNetworkSku: str = None
        if "orderItemDisposition" in data:
            self.orderItemDisposition: str = self._get_value(str, "orderItemDisposition")
        else:
            self.orderItemDisposition: str = None
        if "cancelledQuantity" in data:
            self.cancelledQuantity: Quantity = self._get_value(Quantity, "cancelledQuantity")
        else:
            self.cancelledQuantity: Quantity = None
        if "unfulfillableQuantity" in data:
            self.unfulfillableQuantity: Quantity = self._get_value(Quantity, "unfulfillableQuantity")
        else:
            self.unfulfillableQuantity: Quantity = None
        if "estimatedShipDate" in data:
            self.estimatedShipDate: Timestamp = self._get_value(Timestamp, "estimatedShipDate")
        else:
            self.estimatedShipDate: Timestamp = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = self._get_value(Timestamp, "estimatedArrivalDate")
        else:
            self.estimatedArrivalDate: Timestamp = None
        if "perUnitPrice" in data:
            self.perUnitPrice: Money = self._get_value(Money, "perUnitPrice")
        else:
            self.perUnitPrice: Money = None
        if "perUnitTax" in data:
            self.perUnitTax: Money = self._get_value(Money, "perUnitTax")
        else:
            self.perUnitTax: Money = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = self._get_value(Money, "perUnitDeclaredValue")
        else:
            self.perUnitDeclaredValue: Money = None


class FulfillmentPreview(__BaseDictObject):
    """
    Information about a fulfillment order preview, including delivery and fee information based on shipping method.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = self._get_value(
                ShippingSpeedCategory, "shippingSpeedCategory"
            )
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "scheduledDeliveryInfo" in data:
            self.scheduledDeliveryInfo: ScheduledDeliveryInfo = self._get_value(
                ScheduledDeliveryInfo, "scheduledDeliveryInfo"
            )
        else:
            self.scheduledDeliveryInfo: ScheduledDeliveryInfo = None
        if "isFulfillable" in data:
            self.isFulfillable: bool = self._get_value(convert_bool, "isFulfillable")
        else:
            self.isFulfillable: bool = None
        if "isCODCapable" in data:
            self.isCODCapable: bool = self._get_value(convert_bool, "isCODCapable")
        else:
            self.isCODCapable: bool = None
        if "estimatedShippingWeight" in data:
            self.estimatedShippingWeight: Weight = self._get_value(Weight, "estimatedShippingWeight")
        else:
            self.estimatedShippingWeight: Weight = None
        if "estimatedFees" in data:
            self.estimatedFees: FeeList = self._get_value(FeeList, "estimatedFees")
        else:
            self.estimatedFees: FeeList = None
        if "fulfillmentPreviewShipments" in data:
            self.fulfillmentPreviewShipments: FulfillmentPreviewShipmentList = self._get_value(
                FulfillmentPreviewShipmentList, "fulfillmentPreviewShipments"
            )
        else:
            self.fulfillmentPreviewShipments: FulfillmentPreviewShipmentList = None
        if "unfulfillablePreviewItems" in data:
            self.unfulfillablePreviewItems: UnfulfillablePreviewItemList = self._get_value(
                UnfulfillablePreviewItemList, "unfulfillablePreviewItems"
            )
        else:
            self.unfulfillablePreviewItems: UnfulfillablePreviewItemList = None
        if "orderUnfulfillableReasons" in data:
            self.orderUnfulfillableReasons: StringList = self._get_value(StringList, "orderUnfulfillableReasons")
        else:
            self.orderUnfulfillableReasons: StringList = None
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class FulfillmentPreviewItem(__BaseDictObject):
    """
    Item information for a shipment in a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "estimatedShippingWeight" in data:
            self.estimatedShippingWeight: Weight = self._get_value(Weight, "estimatedShippingWeight")
        else:
            self.estimatedShippingWeight: Weight = None
        if "shippingWeightCalculationMethod" in data:
            self.shippingWeightCalculationMethod: str = self._get_value(str, "shippingWeightCalculationMethod")
        else:
            self.shippingWeightCalculationMethod: str = None


class FulfillmentPreviewShipment(__BaseDictObject):
    """
    Delivery and item information for a shipment in a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__(data)
        if "earliestShipDate" in data:
            self.earliestShipDate: Timestamp = self._get_value(Timestamp, "earliestShipDate")
        else:
            self.earliestShipDate: Timestamp = None
        if "latestShipDate" in data:
            self.latestShipDate: Timestamp = self._get_value(Timestamp, "latestShipDate")
        else:
            self.latestShipDate: Timestamp = None
        if "earliestArrivalDate" in data:
            self.earliestArrivalDate: Timestamp = self._get_value(Timestamp, "earliestArrivalDate")
        else:
            self.earliestArrivalDate: Timestamp = None
        if "latestArrivalDate" in data:
            self.latestArrivalDate: Timestamp = self._get_value(Timestamp, "latestArrivalDate")
        else:
            self.latestArrivalDate: Timestamp = None
        if "shippingNotes" in data:
            self.shippingNotes: _List[str] = [str(datum) for datum in data["shippingNotes"]]
        else:
            self.shippingNotes: _List[str] = []
        if "fulfillmentPreviewItems" in data:
            self.fulfillmentPreviewItems: FulfillmentPreviewItemList = self._get_value(
                FulfillmentPreviewItemList, "fulfillmentPreviewItems"
            )
        else:
            self.fulfillmentPreviewItems: FulfillmentPreviewItemList = None


class FulfillmentShipment(__BaseDictObject):
    """
    Delivery and item information for a shipment in a fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "amazonShipmentId" in data:
            self.amazonShipmentId: str = self._get_value(str, "amazonShipmentId")
        else:
            self.amazonShipmentId: str = None
        if "fulfillmentCenterId" in data:
            self.fulfillmentCenterId: str = self._get_value(str, "fulfillmentCenterId")
        else:
            self.fulfillmentCenterId: str = None
        if "fulfillmentShipmentStatus" in data:
            self.fulfillmentShipmentStatus: str = self._get_value(str, "fulfillmentShipmentStatus")
        else:
            self.fulfillmentShipmentStatus: str = None
        if "shippingDate" in data:
            self.shippingDate: Timestamp = self._get_value(Timestamp, "shippingDate")
        else:
            self.shippingDate: Timestamp = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = self._get_value(Timestamp, "estimatedArrivalDate")
        else:
            self.estimatedArrivalDate: Timestamp = None
        if "shippingNotes" in data:
            self.shippingNotes: _List[str] = [str(datum) for datum in data["shippingNotes"]]
        else:
            self.shippingNotes: _List[str] = []
        if "fulfillmentShipmentItem" in data:
            self.fulfillmentShipmentItem: FulfillmentShipmentItemList = self._get_value(
                FulfillmentShipmentItemList, "fulfillmentShipmentItem"
            )
        else:
            self.fulfillmentShipmentItem: FulfillmentShipmentItemList = None
        if "fulfillmentShipmentPackage" in data:
            self.fulfillmentShipmentPackage: FulfillmentShipmentPackageList = self._get_value(
                FulfillmentShipmentPackageList, "fulfillmentShipmentPackage"
            )
        else:
            self.fulfillmentShipmentPackage: FulfillmentShipmentPackageList = None


class FulfillmentShipmentItem(__BaseDictObject):
    """
    Item information for a shipment in a fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "packageNumber" in data:
            self.packageNumber: int = self._get_value(int, "packageNumber")
        else:
            self.packageNumber: int = None
        if "serialNumber" in data:
            self.serialNumber: str = self._get_value(str, "serialNumber")
        else:
            self.serialNumber: str = None


class FulfillmentShipmentPackage(__BaseDictObject):
    """
    Package information for a shipment in a fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "packageNumber" in data:
            self.packageNumber: int = self._get_value(int, "packageNumber")
        else:
            self.packageNumber: int = None
        if "carrierCode" in data:
            self.carrierCode: str = self._get_value(str, "carrierCode")
        else:
            self.carrierCode: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = self._get_value(Timestamp, "estimatedArrivalDate")
        else:
            self.estimatedArrivalDate: Timestamp = None


class GetFulfillmentOrderResult(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "fulfillmentOrder" in data:
            self.fulfillmentOrder: FulfillmentOrder = self._get_value(FulfillmentOrder, "fulfillmentOrder")
        else:
            self.fulfillmentOrder: FulfillmentOrder = None
        if "fulfillmentOrderItems" in data:
            self.fulfillmentOrderItems: FulfillmentOrderItemList = self._get_value(
                FulfillmentOrderItemList, "fulfillmentOrderItems"
            )
        else:
            self.fulfillmentOrderItems: FulfillmentOrderItemList = None
        if "fulfillmentShipments" in data:
            self.fulfillmentShipments: FulfillmentShipmentList = self._get_value(
                FulfillmentShipmentList, "fulfillmentShipments"
            )
        else:
            self.fulfillmentShipments: FulfillmentShipmentList = None
        if "returnItems" in data:
            self.returnItems: ReturnItemList = self._get_value(ReturnItemList, "returnItems")
        else:
            self.returnItems: ReturnItemList = None
        if "returnAuthorizations" in data:
            self.returnAuthorizations: ReturnAuthorizationList = self._get_value(
                ReturnAuthorizationList, "returnAuthorizations"
            )
        else:
            self.returnAuthorizations: ReturnAuthorizationList = None


class GetFulfillmentOrderResponse(__BaseDictObject):
    """
    The response schema for the getFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetFulfillmentOrderResult = self._get_value(GetFulfillmentOrderResult, "payload")
        else:
            self.payload: GetFulfillmentOrderResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetFulfillmentPreviewItem(__BaseDictObject):
    """
    Item information for a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = self._get_value(Money, "perUnitDeclaredValue")
        else:
            self.perUnitDeclaredValue: Money = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None


class GetFulfillmentPreviewRequest(__BaseDictObject):
    """
    The request body schema for the getFulfillmentPreview operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None
        if "items" in data:
            self.items: GetFulfillmentPreviewItemList = self._get_value(GetFulfillmentPreviewItemList, "items")
        else:
            self.items: GetFulfillmentPreviewItemList = None
        if "shippingSpeedCategories" in data:
            self.shippingSpeedCategories: ShippingSpeedCategoryList = self._get_value(
                ShippingSpeedCategoryList, "shippingSpeedCategories"
            )
        else:
            self.shippingSpeedCategories: ShippingSpeedCategoryList = None
        if "includeCODFulfillmentPreview" in data:
            self.includeCODFulfillmentPreview: bool = self._get_value(convert_bool, "includeCODFulfillmentPreview")
        else:
            self.includeCODFulfillmentPreview: bool = None
        if "includeDeliveryWindows" in data:
            self.includeDeliveryWindows: bool = self._get_value(convert_bool, "includeDeliveryWindows")
        else:
            self.includeDeliveryWindows: bool = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []


class GetFulfillmentPreviewResult(__BaseDictObject):
    """
    A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated ship dates and arrival dates.
    """

    def __init__(self, data):
        super().__init__(data)
        if "fulfillmentPreviews" in data:
            self.fulfillmentPreviews: FulfillmentPreviewList = self._get_value(
                FulfillmentPreviewList, "fulfillmentPreviews"
            )
        else:
            self.fulfillmentPreviews: FulfillmentPreviewList = None


class GetFulfillmentPreviewResponse(__BaseDictObject):
    """
    The response schema for the getFulfillmentPreview operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetFulfillmentPreviewResult = self._get_value(GetFulfillmentPreviewResult, "payload")
        else:
            self.payload: GetFulfillmentPreviewResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class InvalidItemReason(__BaseDictObject):
    """
    The reason that the item is invalid for return.
    """

    def __init__(self, data):
        super().__init__(data)
        if "invalidItemReasonCode" in data:
            self.invalidItemReasonCode: InvalidItemReasonCode = self._get_value(
                InvalidItemReasonCode, "invalidItemReasonCode"
            )
        else:
            self.invalidItemReasonCode: InvalidItemReasonCode = None
        if "description" in data:
            self.description: str = self._get_value(str, "description")
        else:
            self.description: str = None


class InvalidReturnItem(__BaseDictObject):
    """
    An item that is invalid for return.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerReturnItemId" in data:
            self.sellerReturnItemId: str = self._get_value(str, "sellerReturnItemId")
        else:
            self.sellerReturnItemId: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "invalidItemReason" in data:
            self.invalidItemReason: InvalidItemReason = self._get_value(InvalidItemReason, "invalidItemReason")
        else:
            self.invalidItemReason: InvalidItemReason = None


class ListAllFulfillmentOrdersResult(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None
        if "fulfillmentOrders" in data:
            self.fulfillmentOrders: _List[FulfillmentOrder] = [
                FulfillmentOrder(datum) for datum in data["fulfillmentOrders"]
            ]
        else:
            self.fulfillmentOrders: _List[FulfillmentOrder] = []


class ListAllFulfillmentOrdersResponse(__BaseDictObject):
    """
    The response schema for the listAllFulfillmentOrders operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ListAllFulfillmentOrdersResult = self._get_value(ListAllFulfillmentOrdersResult, "payload")
        else:
            self.payload: ListAllFulfillmentOrdersResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ListReturnReasonCodesResult(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "reasonCodeDetails" in data:
            self.reasonCodeDetails: ReasonCodeDetailsList = self._get_value(ReasonCodeDetailsList, "reasonCodeDetails")
        else:
            self.reasonCodeDetails: ReasonCodeDetailsList = None


class ListReturnReasonCodesResponse(__BaseDictObject):
    """
    The response schema for the listReturnReasonCodes operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ListReturnReasonCodesResult = self._get_value(ListReturnReasonCodesResult, "payload")
        else:
            self.payload: ListReturnReasonCodesResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class PackageTrackingDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "packageNumber" in data:
            self.packageNumber: int = self._get_value(int, "packageNumber")
        else:
            self.packageNumber: int = None
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "customerTrackingLink" in data:
            self.customerTrackingLink: str = self._get_value(str, "customerTrackingLink")
        else:
            self.customerTrackingLink: str = None
        if "carrierCode" in data:
            self.carrierCode: str = self._get_value(str, "carrierCode")
        else:
            self.carrierCode: str = None
        if "carrierPhoneNumber" in data:
            self.carrierPhoneNumber: str = self._get_value(str, "carrierPhoneNumber")
        else:
            self.carrierPhoneNumber: str = None
        if "carrierURL" in data:
            self.carrierURL: str = self._get_value(str, "carrierURL")
        else:
            self.carrierURL: str = None
        if "shipDate" in data:
            self.shipDate: Timestamp = self._get_value(Timestamp, "shipDate")
        else:
            self.shipDate: Timestamp = None
        if "estimatedArrivalDate" in data:
            self.estimatedArrivalDate: Timestamp = self._get_value(Timestamp, "estimatedArrivalDate")
        else:
            self.estimatedArrivalDate: Timestamp = None
        if "shipToAddress" in data:
            self.shipToAddress: TrackingAddress = self._get_value(TrackingAddress, "shipToAddress")
        else:
            self.shipToAddress: TrackingAddress = None
        if "currentStatus" in data:
            self.currentStatus: CurrentStatus = self._get_value(CurrentStatus, "currentStatus")
        else:
            self.currentStatus: CurrentStatus = None
        if "currentStatusDescription" in data:
            self.currentStatusDescription: str = self._get_value(str, "currentStatusDescription")
        else:
            self.currentStatusDescription: str = None
        if "signedForBy" in data:
            self.signedForBy: str = self._get_value(str, "signedForBy")
        else:
            self.signedForBy: str = None
        if "additionalLocationInfo" in data:
            self.additionalLocationInfo: AdditionalLocationInfo = self._get_value(
                AdditionalLocationInfo, "additionalLocationInfo"
            )
        else:
            self.additionalLocationInfo: AdditionalLocationInfo = None
        if "trackingEvents" in data:
            self.trackingEvents: TrackingEventList = self._get_value(TrackingEventList, "trackingEvents")
        else:
            self.trackingEvents: TrackingEventList = None


class GetPackageTrackingDetailsResponse(__BaseDictObject):
    """
    The response schema for the getPackageTrackingDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: PackageTrackingDetails = self._get_value(PackageTrackingDetails, "payload")
        else:
            self.payload: PackageTrackingDetails = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ReasonCodeDetails(__BaseDictObject):
    """
    A return reason code, a description, and an optional description translation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "returnReasonCode" in data:
            self.returnReasonCode: str = self._get_value(str, "returnReasonCode")
        else:
            self.returnReasonCode: str = None
        if "description" in data:
            self.description: str = self._get_value(str, "description")
        else:
            self.description: str = None
        if "translatedDescription" in data:
            self.translatedDescription: str = self._get_value(str, "translatedDescription")
        else:
            self.translatedDescription: str = None


class ReturnAuthorization(__BaseDictObject):
    """
    Return authorization information for items accepted for return.
    """

    def __init__(self, data):
        super().__init__(data)
        if "returnAuthorizationId" in data:
            self.returnAuthorizationId: str = self._get_value(str, "returnAuthorizationId")
        else:
            self.returnAuthorizationId: str = None
        if "fulfillmentCenterId" in data:
            self.fulfillmentCenterId: str = self._get_value(str, "fulfillmentCenterId")
        else:
            self.fulfillmentCenterId: str = None
        if "returnToAddress" in data:
            self.returnToAddress: Address = self._get_value(Address, "returnToAddress")
        else:
            self.returnToAddress: Address = None
        if "amazonRmaId" in data:
            self.amazonRmaId: str = self._get_value(str, "amazonRmaId")
        else:
            self.amazonRmaId: str = None
        if "rmaPageURL" in data:
            self.rmaPageURL: str = self._get_value(str, "rmaPageURL")
        else:
            self.rmaPageURL: str = None


class ReturnItem(__BaseDictObject):
    """
    An item that Amazon accepted for return.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerReturnItemId" in data:
            self.sellerReturnItemId: str = self._get_value(str, "sellerReturnItemId")
        else:
            self.sellerReturnItemId: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "amazonShipmentId" in data:
            self.amazonShipmentId: str = self._get_value(str, "amazonShipmentId")
        else:
            self.amazonShipmentId: str = None
        if "sellerReturnReasonCode" in data:
            self.sellerReturnReasonCode: str = self._get_value(str, "sellerReturnReasonCode")
        else:
            self.sellerReturnReasonCode: str = None
        if "returnComment" in data:
            self.returnComment: str = self._get_value(str, "returnComment")
        else:
            self.returnComment: str = None
        if "amazonReturnReasonCode" in data:
            self.amazonReturnReasonCode: str = self._get_value(str, "amazonReturnReasonCode")
        else:
            self.amazonReturnReasonCode: str = None
        if "status" in data:
            self.status: FulfillmentReturnItemStatus = self._get_value(FulfillmentReturnItemStatus, "status")
        else:
            self.status: FulfillmentReturnItemStatus = None
        if "statusChangedDate" in data:
            self.statusChangedDate: Timestamp = self._get_value(Timestamp, "statusChangedDate")
        else:
            self.statusChangedDate: Timestamp = None
        if "returnAuthorizationId" in data:
            self.returnAuthorizationId: str = self._get_value(str, "returnAuthorizationId")
        else:
            self.returnAuthorizationId: str = None
        if "returnReceivedCondition" in data:
            self.returnReceivedCondition: ReturnItemDisposition = self._get_value(
                ReturnItemDisposition, "returnReceivedCondition"
            )
        else:
            self.returnReceivedCondition: ReturnItemDisposition = None
        if "fulfillmentCenterId" in data:
            self.fulfillmentCenterId: str = self._get_value(str, "fulfillmentCenterId")
        else:
            self.fulfillmentCenterId: str = None


class ScheduledDeliveryInfo(__BaseDictObject):
    """
    Delivery information for a scheduled delivery.
    """

    def __init__(self, data):
        super().__init__(data)
        if "deliveryTimeZone" in data:
            self.deliveryTimeZone: str = self._get_value(str, "deliveryTimeZone")
        else:
            self.deliveryTimeZone: str = None
        if "deliveryWindows" in data:
            self.deliveryWindows: DeliveryWindowList = self._get_value(DeliveryWindowList, "deliveryWindows")
        else:
            self.deliveryWindows: DeliveryWindowList = None


class TrackingAddress(__BaseDictObject):
    """
    Address information for tracking the package.
    """

    def __init__(self, data):
        super().__init__(data)
        if "city" in data:
            self.city: str = self._get_value(str, "city")
        else:
            self.city: str = None
        if "state" in data:
            self.state: str = self._get_value(str, "state")
        else:
            self.state: str = None
        if "country" in data:
            self.country: str = self._get_value(str, "country")
        else:
            self.country: str = None


class TrackingEvent(__BaseDictObject):
    """
    Information for tracking package deliveries.
    """

    def __init__(self, data):
        super().__init__(data)
        if "eventDate" in data:
            self.eventDate: Timestamp = self._get_value(Timestamp, "eventDate")
        else:
            self.eventDate: Timestamp = None
        if "eventAddress" in data:
            self.eventAddress: TrackingAddress = self._get_value(TrackingAddress, "eventAddress")
        else:
            self.eventAddress: TrackingAddress = None
        if "eventCode" in data:
            self.eventCode: EventCode = self._get_value(EventCode, "eventCode")
        else:
            self.eventCode: EventCode = None
        if "eventDescription" in data:
            self.eventDescription: str = self._get_value(str, "eventDescription")
        else:
            self.eventDescription: str = None


class UnfulfillablePreviewItem(__BaseDictObject):
    """
    Information about unfulfillable items in a fulfillment order preview.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "itemUnfulfillableReasons" in data:
            self.itemUnfulfillableReasons: StringList = self._get_value(StringList, "itemUnfulfillableReasons")
        else:
            self.itemUnfulfillableReasons: StringList = None


class UpdateFulfillmentOrderItem(__BaseDictObject):
    """
    Item information for updating a fulfillment order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "sellerFulfillmentOrderItemId" in data:
            self.sellerFulfillmentOrderItemId: str = self._get_value(str, "sellerFulfillmentOrderItemId")
        else:
            self.sellerFulfillmentOrderItemId: str = None
        if "quantity" in data:
            self.quantity: Quantity = self._get_value(Quantity, "quantity")
        else:
            self.quantity: Quantity = None
        if "giftMessage" in data:
            self.giftMessage: str = self._get_value(str, "giftMessage")
        else:
            self.giftMessage: str = None
        if "displayableComment" in data:
            self.displayableComment: str = self._get_value(str, "displayableComment")
        else:
            self.displayableComment: str = None
        if "fulfillmentNetworkSku" in data:
            self.fulfillmentNetworkSku: str = self._get_value(str, "fulfillmentNetworkSku")
        else:
            self.fulfillmentNetworkSku: str = None
        if "orderItemDisposition" in data:
            self.orderItemDisposition: str = self._get_value(str, "orderItemDisposition")
        else:
            self.orderItemDisposition: str = None
        if "perUnitDeclaredValue" in data:
            self.perUnitDeclaredValue: Money = self._get_value(Money, "perUnitDeclaredValue")
        else:
            self.perUnitDeclaredValue: Money = None
        if "perUnitPrice" in data:
            self.perUnitPrice: Money = self._get_value(Money, "perUnitPrice")
        else:
            self.perUnitPrice: Money = None
        if "perUnitTax" in data:
            self.perUnitTax: Money = self._get_value(Money, "perUnitTax")
        else:
            self.perUnitTax: Money = None


class UpdateFulfillmentOrderRequest(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "displayableOrderId" in data:
            self.displayableOrderId: str = self._get_value(str, "displayableOrderId")
        else:
            self.displayableOrderId: str = None
        if "displayableOrderDate" in data:
            self.displayableOrderDate: Timestamp = self._get_value(Timestamp, "displayableOrderDate")
        else:
            self.displayableOrderDate: Timestamp = None
        if "displayableOrderComment" in data:
            self.displayableOrderComment: str = self._get_value(str, "displayableOrderComment")
        else:
            self.displayableOrderComment: str = None
        if "shippingSpeedCategory" in data:
            self.shippingSpeedCategory: ShippingSpeedCategory = self._get_value(
                ShippingSpeedCategory, "shippingSpeedCategory"
            )
        else:
            self.shippingSpeedCategory: ShippingSpeedCategory = None
        if "destinationAddress" in data:
            self.destinationAddress: Address = self._get_value(Address, "destinationAddress")
        else:
            self.destinationAddress: Address = None
        if "fulfillmentAction" in data:
            self.fulfillmentAction: FulfillmentAction = self._get_value(FulfillmentAction, "fulfillmentAction")
        else:
            self.fulfillmentAction: FulfillmentAction = None
        if "fulfillmentPolicy" in data:
            self.fulfillmentPolicy: FulfillmentPolicy = self._get_value(FulfillmentPolicy, "fulfillmentPolicy")
        else:
            self.fulfillmentPolicy: FulfillmentPolicy = None
        if "shipFromCountryCode" in data:
            self.shipFromCountryCode: str = self._get_value(str, "shipFromCountryCode")
        else:
            self.shipFromCountryCode: str = None
        if "notificationEmails" in data:
            self.notificationEmails: NotificationEmailList = self._get_value(
                NotificationEmailList, "notificationEmails"
            )
        else:
            self.notificationEmails: NotificationEmailList = None
        if "featureConstraints" in data:
            self.featureConstraints: _List[FeatureSettings] = [
                FeatureSettings(datum) for datum in data["featureConstraints"]
            ]
        else:
            self.featureConstraints: _List[FeatureSettings] = []
        if "items" in data:
            self.items: UpdateFulfillmentOrderItemList = self._get_value(UpdateFulfillmentOrderItemList, "items")
        else:
            self.items: UpdateFulfillmentOrderItemList = None


class UpdateFulfillmentOrderResponse(__BaseDictObject):
    """
    The response schema for the updateFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateFulfillmentOrderResponse(__BaseDictObject):
    """
    The response schema for the createFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CancelFulfillmentOrderResponse(__BaseDictObject):
    """
    The response schema for the cancelFulfillmentOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Weight(__BaseDictObject):
    """
    The weight.
    """

    def __init__(self, data):
        super().__init__(data)
        if "unit" in data:
            self.unit: str = self._get_value(str, "unit")
        else:
            self.unit: str = None
        if "value" in data:
            self.value: str = self._get_value(str, "value")
        else:
            self.value: str = None


class GetFeatureInventoryResponse(__BaseDictObject):
    """
    The breakdown of eligibility inventory by feature.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetFeatureInventoryResult = self._get_value(GetFeatureInventoryResult, "payload")
        else:
            self.payload: GetFeatureInventoryResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetFeatureInventoryResult(__BaseDictObject):
    """
    The payload for the getEligibileInventory operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "featureName" in data:
            self.featureName: str = self._get_value(str, "featureName")
        else:
            self.featureName: str = None
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None
        if "featureSkus" in data:
            self.featureSkus: _List[FeatureSku] = [FeatureSku(datum) for datum in data["featureSkus"]]
        else:
            self.featureSkus: _List[FeatureSku] = []


class FeatureSku(__BaseDictObject):
    """
    Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerSku" in data:
            self.sellerSku: str = self._get_value(str, "sellerSku")
        else:
            self.sellerSku: str = None
        if "fnSku" in data:
            self.fnSku: str = self._get_value(str, "fnSku")
        else:
            self.fnSku: str = None
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "skuCount" in data:
            self.skuCount: float = self._get_value(float, "skuCount")
        else:
            self.skuCount: float = None
        if "overlappingSkus" in data:
            self.overlappingSkus: _List[str] = [str(datum) for datum in data["overlappingSkus"]]
        else:
            self.overlappingSkus: _List[str] = []


class GetFeaturesResponse(__BaseDictObject):
    """
    The response schema for the getFeatures operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetFeaturesResult = self._get_value(GetFeaturesResult, "payload")
        else:
            self.payload: GetFeaturesResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetFeaturesResult(__BaseDictObject):
    """
    The payload for the getFeatures operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "features" in data:
            self.features: Features = self._get_value(Features, "features")
        else:
            self.features: Features = None


class Feature(__BaseDictObject):
    """
    A Multi-Channel Fulfillment feature.
    """

    def __init__(self, data):
        super().__init__(data)
        if "featureName" in data:
            self.featureName: str = self._get_value(str, "featureName")
        else:
            self.featureName: str = None
        if "featureDescription" in data:
            self.featureDescription: str = self._get_value(str, "featureDescription")
        else:
            self.featureDescription: str = None
        if "sellerEligible" in data:
            self.sellerEligible: bool = self._get_value(convert_bool, "sellerEligible")
        else:
            self.sellerEligible: bool = None


class GetFeatureSkuResponse(__BaseDictObject):
    """
    The response schema for the getFeatureSKU operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetFeatureSkuResult = self._get_value(GetFeatureSkuResult, "payload")
        else:
            self.payload: GetFeatureSkuResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetFeatureSkuResult(__BaseDictObject):
    """
    The payload for the getFeatureSKU operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "featureName" in data:
            self.featureName: str = self._get_value(str, "featureName")
        else:
            self.featureName: str = None
        if "isEligible" in data:
            self.isEligible: bool = self._get_value(convert_bool, "isEligible")
        else:
            self.isEligible: bool = None
        if "ineligibleReasons" in data:
            self.ineligibleReasons: _List[str] = [str(datum) for datum in data["ineligibleReasons"]]
        else:
            self.ineligibleReasons: _List[str] = []
        if "skuInfo" in data:
            self.skuInfo: FeatureSku = self._get_value(FeatureSku, "skuInfo")
        else:
            self.skuInfo: FeatureSku = None


class FeatureSettings(__BaseDictObject):
    """
    FeatureSettings allows users to apply fulfillment features to an order. To block an order from being shipped using Amazon Logistics (AMZL) and an AMZL tracking number, use featureName as BLOCK_AMZL and featureFulfillmentPolicy as Required. Blocking AMZL will incur an additional fee surcharge on your MCF orders and increase the risk of some of your orders being unfulfilled or delivered late if there are no alternative carriers available. Using BLOCK_AMZL in an order request will take precedence over your Seller Central account setting.
    """

    def __init__(self, data):
        super().__init__(data)
        if "featureName" in data:
            self.featureName: str = self._get_value(str, "featureName")
        else:
            self.featureName: str = None
        if "featureFulfillmentPolicy" in data:
            self.featureFulfillmentPolicy: str = self._get_value(str, "featureFulfillmentPolicy")
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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders/preview"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetFulfillmentPreviewResponse,
            400: GetFulfillmentPreviewResponse,
            401: GetFulfillmentPreviewResponse,
            403: GetFulfillmentPreviewResponse,
            404: GetFulfillmentPreviewResponse,
            429: GetFulfillmentPreviewResponse,
            500: GetFulfillmentPreviewResponse,
            503: GetFulfillmentPreviewResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders"
        params = {}
        if queryStartDate is not None:
            params["queryStartDate"] = queryStartDate
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListAllFulfillmentOrdersResponse,
            400: ListAllFulfillmentOrdersResponse,
            401: ListAllFulfillmentOrdersResponse,
            403: ListAllFulfillmentOrdersResponse,
            404: ListAllFulfillmentOrdersResponse,
            429: ListAllFulfillmentOrdersResponse,
            500: ListAllFulfillmentOrdersResponse,
            503: ListAllFulfillmentOrdersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateFulfillmentOrderResponse,
            400: CreateFulfillmentOrderResponse,
            401: CreateFulfillmentOrderResponse,
            403: CreateFulfillmentOrderResponse,
            404: CreateFulfillmentOrderResponse,
            429: CreateFulfillmentOrderResponse,
            500: CreateFulfillmentOrderResponse,
            503: CreateFulfillmentOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/tracking"
        params = {}
        if packageNumber is not None:
            params["packageNumber"] = packageNumber
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetPackageTrackingDetailsResponse,
            400: GetPackageTrackingDetailsResponse,
            401: GetPackageTrackingDetailsResponse,
            403: GetPackageTrackingDetailsResponse,
            404: GetPackageTrackingDetailsResponse,
            429: GetPackageTrackingDetailsResponse,
            500: GetPackageTrackingDetailsResponse,
            503: GetPackageTrackingDetailsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/returnReasonCodes"
        params = {}
        if sellerSku is not None:
            params["sellerSku"] = sellerSku
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if sellerFulfillmentOrderId is not None:
            params["sellerFulfillmentOrderId"] = sellerFulfillmentOrderId
        if language is not None:
            params["language"] = language
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListReturnReasonCodesResponse,
            400: ListReturnReasonCodesResponse,
            401: ListReturnReasonCodesResponse,
            403: ListReturnReasonCodesResponse,
            404: ListReturnReasonCodesResponse,
            429: ListReturnReasonCodesResponse,
            500: ListReturnReasonCodesResponse,
            503: ListReturnReasonCodesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createFulfillmentReturn(
        self,
        data: CreateFulfillmentReturnRequest,
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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateFulfillmentReturnResponse,
            400: CreateFulfillmentReturnResponse,
            401: CreateFulfillmentReturnResponse,
            403: CreateFulfillmentReturnResponse,
            404: CreateFulfillmentReturnResponse,
            429: CreateFulfillmentReturnResponse,
            500: CreateFulfillmentReturnResponse,
            503: CreateFulfillmentReturnResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetFulfillmentOrderResponse,
            400: GetFulfillmentOrderResponse,
            401: GetFulfillmentOrderResponse,
            403: GetFulfillmentOrderResponse,
            404: GetFulfillmentOrderResponse,
            429: GetFulfillmentOrderResponse,
            500: GetFulfillmentOrderResponse,
            503: GetFulfillmentOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateFulfillmentOrder(
        self,
        data: UpdateFulfillmentOrderRequest,
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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            200: UpdateFulfillmentOrderResponse,
            400: UpdateFulfillmentOrderResponse,
            401: UpdateFulfillmentOrderResponse,
            403: UpdateFulfillmentOrderResponse,
            404: UpdateFulfillmentOrderResponse,
            429: UpdateFulfillmentOrderResponse,
            500: UpdateFulfillmentOrderResponse,
            503: UpdateFulfillmentOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
        )
        response_type = {
            200: CancelFulfillmentOrderResponse,
            400: CancelFulfillmentOrderResponse,
            401: CancelFulfillmentOrderResponse,
            403: CancelFulfillmentOrderResponse,
            404: CancelFulfillmentOrderResponse,
            429: CancelFulfillmentOrderResponse,
            500: CancelFulfillmentOrderResponse,
            503: CancelFulfillmentOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/features"
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetFeaturesResponse,
            400: GetFeaturesResponse,
            401: GetFeaturesResponse,
            403: GetFeaturesResponse,
            404: GetFeaturesResponse,
            429: GetFeaturesResponse,
            500: GetFeaturesResponse,
            503: GetFeaturesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/features/inventory/{featureName}"
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetFeatureInventoryResponse,
            400: GetFeatureInventoryResponse,
            401: GetFeatureInventoryResponse,
            403: GetFeatureInventoryResponse,
            404: GetFeatureInventoryResponse,
            429: GetFeatureInventoryResponse,
            500: GetFeatureInventoryResponse,
            503: GetFeatureInventoryResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}"
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetFeatureSkuResponse,
            400: GetFeatureSkuResponse,
            401: GetFeatureSkuResponse,
            403: GetFeatureSkuResponse,
            404: GetFeatureSkuResponse,
            429: GetFeatureSkuResponse,
            500: GetFeatureSkuResponse,
            503: GetFeatureSkuResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
