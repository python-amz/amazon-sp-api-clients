from .base import BaseClient as __BaseClient
from typing import List as _List


class PackingSlip:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "content" in data:
            self.content: str = str(data["content"])
        else:
            self.content: str = None
        if "contentType" in data:
            self.contentType: str = str(data["contentType"])
        else:
            self.contentType: str = None


class PackingSlipList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "packingSlips" in data:
            self.packingSlips: _List[PackingSlip] = [PackingSlip(datum) for datum in data["packingSlips"]]
        else:
            self.packingSlips: _List[PackingSlip] = []


class GetPackingSlipListResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: PackingSlipList = PackingSlipList(data["payload"])
        else:
            self.payload: PackingSlipList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetPackingSlipResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: PackingSlip = PackingSlip(data["payload"])
        else:
            self.payload: PackingSlip = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class SubmitShippingLabelsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shippingLabelRequests" in data:
            self.shippingLabelRequests: _List[ShippingLabelRequest] = [
                ShippingLabelRequest(datum) for datum in data["shippingLabelRequests"]
            ]
        else:
            self.shippingLabelRequests: _List[ShippingLabelRequest] = []


class ShippingLabelRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "containers" in data:
            self.containers: _List[Container] = [Container(datum) for datum in data["containers"]]
        else:
            self.containers: _List[Container] = []


class Item:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: int = int(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: int = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = str(data["buyerProductIdentifier"])
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = ItemQuantity(data["shippedQuantity"])
        else:
            self.shippedQuantity: ItemQuantity = None


class PackedItem:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: int = int(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: int = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = str(data["buyerProductIdentifier"])
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "packedQuantity" in data:
            self.packedQuantity: ItemQuantity = ItemQuantity(data["packedQuantity"])
        else:
            self.packedQuantity: ItemQuantity = None


class Package:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "packageIdentifier" in data:
            self.packageIdentifier: str = str(data["packageIdentifier"])
        else:
            self.packageIdentifier: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "manifestId" in data:
            self.manifestId: str = str(data["manifestId"])
        else:
            self.manifestId: str = None
        if "manifestDate" in data:
            self.manifestDate: str = str(data["manifestDate"])
        else:
            self.manifestDate: str = None
        if "shipMethod" in data:
            self.shipMethod: str = str(data["shipMethod"])
        else:
            self.shipMethod: str = None
        if "weight" in data:
            self.weight: Weight = Weight(data["weight"])
        else:
            self.weight: Weight = None
        if "dimensions" in data:
            self.dimensions: Dimensions = Dimensions(data["dimensions"])
        else:
            self.dimensions: Dimensions = None


class PartyIdentification:
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


class ShipmentDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shippedDate" in data:
            self.shippedDate: str = str(data["shippedDate"])
        else:
            self.shippedDate: str = None
        if "shipmentStatus" in data:
            self.shipmentStatus: str = str(data["shipmentStatus"])
        else:
            self.shipmentStatus: str = None
        if "isPriorityShipment" in data:
            self.isPriorityShipment: bool = bool(data["isPriorityShipment"])
        else:
            self.isPriorityShipment: bool = None
        if "vendorOrderNumber" in data:
            self.vendorOrderNumber: str = str(data["vendorOrderNumber"])
        else:
            self.vendorOrderNumber: str = None
        if "estimatedDeliveryDate" in data:
            self.estimatedDeliveryDate: str = str(data["estimatedDeliveryDate"])
        else:
            self.estimatedDeliveryDate: str = None


class StatusUpdateDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "statusCode" in data:
            self.statusCode: str = str(data["statusCode"])
        else:
            self.statusCode: str = None
        if "reasonCode" in data:
            self.reasonCode: str = str(data["reasonCode"])
        else:
            self.reasonCode: str = None
        if "statusDateTime" in data:
            self.statusDateTime: str = str(data["statusDateTime"])
        else:
            self.statusDateTime: str = None
        if "statusLocationAddress" in data:
            self.statusLocationAddress: Address = Address(data["statusLocationAddress"])
        else:
            self.statusLocationAddress: Address = None
        if "shipmentSchedule" in data:
            self.shipmentSchedule: dict = dict(data["shipmentSchedule"])
        else:
            self.shipmentSchedule: dict = None


class TaxRegistrationDetails:
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
        if "taxRegistrationMessages" in data:
            self.taxRegistrationMessages: str = str(data["taxRegistrationMessages"])
        else:
            self.taxRegistrationMessages: str = None


class Address:
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


class Dimensions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "length" in data:
            self.length: Decimal = Decimal(data["length"])
        else:
            self.length: Decimal = None
        if "width" in data:
            self.width: Decimal = Decimal(data["width"])
        else:
            self.width: Decimal = None
        if "height" in data:
            self.height: Decimal = Decimal(data["height"])
        else:
            self.height: Decimal = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = str(data["unitOfMeasure"])
        else:
            self.unitOfMeasure: str = None


class Weight:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = str(data["unitOfMeasure"])
        else:
            self.unitOfMeasure: str = None
        if "value" in data:
            self.value: Decimal = Decimal(data["value"])
        else:
            self.value: Decimal = None


class ItemQuantity:
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


class SubmitShipmentConfirmationsResponse:
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


class SubmitShipmentStatusUpdatesResponse:
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


class GetShippingLabelListResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ShippingLabelList = ShippingLabelList(data["payload"])
        else:
            self.payload: ShippingLabelList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetShippingLabelResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ShippingLabel = ShippingLabel(data["payload"])
        else:
            self.payload: ShippingLabel = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ShippingLabelList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "shippingLabels" in data:
            self.shippingLabels: _List[ShippingLabel] = [ShippingLabel(datum) for datum in data["shippingLabels"]]
        else:
            self.shippingLabels: _List[ShippingLabel] = []


class LabelData:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "packageIdentifier" in data:
            self.packageIdentifier: str = str(data["packageIdentifier"])
        else:
            self.packageIdentifier: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "shipMethod" in data:
            self.shipMethod: str = str(data["shipMethod"])
        else:
            self.shipMethod: str = None
        if "shipMethodName" in data:
            self.shipMethodName: str = str(data["shipMethodName"])
        else:
            self.shipMethodName: str = None
        if "content" in data:
            self.content: str = str(data["content"])
        else:
            self.content: str = None


class ShippingLabel:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "labelFormat" in data:
            self.labelFormat: str = str(data["labelFormat"])
        else:
            self.labelFormat: str = None
        if "labelData" in data:
            self.labelData: _List[LabelData] = [LabelData(datum) for datum in data["labelData"]]
        else:
            self.labelData: _List[LabelData] = []


class SubmitShippingLabelsResponse:
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


class SubmitShipmentConfirmationsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentConfirmations" in data:
            self.shipmentConfirmations: _List[ShipmentConfirmation] = [
                ShipmentConfirmation(datum) for datum in data["shipmentConfirmations"]
            ]
        else:
            self.shipmentConfirmations: _List[ShipmentConfirmation] = []


class ShipmentConfirmation:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "shipmentDetails" in data:
            self.shipmentDetails: ShipmentDetails = ShipmentDetails(data["shipmentDetails"])
        else:
            self.shipmentDetails: ShipmentDetails = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "items" in data:
            self.items: _List[Item] = [Item(datum) for datum in data["items"]]
        else:
            self.items: _List[Item] = []
        if "containers" in data:
            self.containers: _List[Container] = [Container(datum) for datum in data["containers"]]
        else:
            self.containers: _List[Container] = []


class SubmitShipmentStatusUpdatesRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentStatusUpdates" in data:
            self.shipmentStatusUpdates: _List[ShipmentStatusUpdate] = [
                ShipmentStatusUpdate(datum) for datum in data["shipmentStatusUpdates"]
            ]
        else:
            self.shipmentStatusUpdates: _List[ShipmentStatusUpdate] = []


class ShipmentStatusUpdate:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "statusUpdateDetails" in data:
            self.statusUpdateDetails: StatusUpdateDetails = StatusUpdateDetails(data["statusUpdateDetails"])
        else:
            self.statusUpdateDetails: StatusUpdateDetails = None


class GetCustomerInvoicesResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CustomerInvoiceList = CustomerInvoiceList(data["payload"])
        else:
            self.payload: CustomerInvoiceList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetCustomerInvoiceResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CustomerInvoice = CustomerInvoice(data["payload"])
        else:
            self.payload: CustomerInvoice = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CustomerInvoiceList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "customerInvoices" in data:
            self.customerInvoices: _List[CustomerInvoice] = [
                CustomerInvoice(datum) for datum in data["customerInvoices"]
            ]
        else:
            self.customerInvoices: _List[CustomerInvoice] = []


class Pagination:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class CustomerInvoice:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "content" in data:
            self.content: str = str(data["content"])
        else:
            self.content: str = None


class TransactionReference:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "transactionId" in data:
            self.transactionId: str = str(data["transactionId"])
        else:
            self.transactionId: str = None


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


class Container:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "containerType" in data:
            self.containerType: str = str(data["containerType"])
        else:
            self.containerType: str = None
        if "containerIdentifier" in data:
            self.containerIdentifier: str = str(data["containerIdentifier"])
        else:
            self.containerIdentifier: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "manifestId" in data:
            self.manifestId: str = str(data["manifestId"])
        else:
            self.manifestId: str = None
        if "manifestDate" in data:
            self.manifestDate: str = str(data["manifestDate"])
        else:
            self.manifestDate: str = None
        if "shipMethod" in data:
            self.shipMethod: str = str(data["shipMethod"])
        else:
            self.shipMethod: str = None
        if "scacCode" in data:
            self.scacCode: str = str(data["scacCode"])
        else:
            self.scacCode: str = None
        if "carrier" in data:
            self.carrier: str = str(data["carrier"])
        else:
            self.carrier: str = None
        if "containerSequenceNumber" in data:
            self.containerSequenceNumber: int = int(data["containerSequenceNumber"])
        else:
            self.containerSequenceNumber: int = None
        if "dimensions" in data:
            self.dimensions: Dimensions = Dimensions(data["dimensions"])
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = Weight(data["weight"])
        else:
            self.weight: Weight = None
        if "packedItems" in data:
            self.packedItems: _List[PackedItem] = [PackedItem(datum) for datum in data["packedItems"]]
        else:
            self.packedItems: _List[PackedItem] = []


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class Decimal(str):
    pass


class VendorDirectFulfillmentShippingV1Client(__BaseClient):
    def getShippingLabels(
        self,
        createdAfter: str,
        createdBefore: str,
        shipFromPartyId: str = None,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
    ):
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels".format()
        params = {}
        if shipFromPartyId is not None:
            params["shipFromPartyId"] = (shipFromPartyId,)
        if limit is not None:
            params["limit"] = (limit,)
        if createdAfter is not None:
            params["createdAfter"] = (createdAfter,)
        if createdBefore is not None:
            params["createdBefore"] = (createdBefore,)
        if sortOrder is not None:
            params["sortOrder"] = (sortOrder,)
        if nextToken is not None:
            params["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShippingLabelListResponse,
            400: GetShippingLabelListResponse,
            403: GetShippingLabelListResponse,
            404: GetShippingLabelListResponse,
            415: GetShippingLabelListResponse,
            429: GetShippingLabelListResponse,
            500: GetShippingLabelListResponse,
            503: GetShippingLabelListResponse,
        }[response.status_code](self._get_response_json(response))

    def submitShippingLabelRequest(
        self,
        data: SubmitShippingLabelsRequest,
    ):
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: SubmitShippingLabelsResponse,
            400: SubmitShippingLabelsResponse,
            403: SubmitShippingLabelsResponse,
            404: SubmitShippingLabelsResponse,
            413: SubmitShippingLabelsResponse,
            415: SubmitShippingLabelsResponse,
            429: SubmitShippingLabelsResponse,
            500: SubmitShippingLabelsResponse,
            503: SubmitShippingLabelsResponse,
        }[response.status_code](self._get_response_json(response))

    def getShippingLabel(
        self,
        purchaseOrderNumber: str,
    ):
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels/{purchaseOrderNumber}".format(
            purchaseOrderNumber=purchaseOrderNumber,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShippingLabelResponse,
            400: GetShippingLabelResponse,
            401: GetShippingLabelResponse,
            403: GetShippingLabelResponse,
            404: GetShippingLabelResponse,
            415: GetShippingLabelResponse,
            429: GetShippingLabelResponse,
            500: GetShippingLabelResponse,
            503: GetShippingLabelResponse,
        }[response.status_code](self._get_response_json(response))

    def submitShipmentConfirmations(
        self,
        data: SubmitShipmentConfirmationsRequest,
    ):
        url = "/vendor/directFulfillment/shipping/v1/shipmentConfirmations".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: SubmitShipmentConfirmationsResponse,
            400: SubmitShipmentConfirmationsResponse,
            403: SubmitShipmentConfirmationsResponse,
            404: SubmitShipmentConfirmationsResponse,
            413: SubmitShipmentConfirmationsResponse,
            415: SubmitShipmentConfirmationsResponse,
            429: SubmitShipmentConfirmationsResponse,
            500: SubmitShipmentConfirmationsResponse,
            503: SubmitShipmentConfirmationsResponse,
        }[response.status_code](self._get_response_json(response))

    def submitShipmentStatusUpdates(
        self,
        data: SubmitShipmentStatusUpdatesRequest,
    ):
        url = "/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: SubmitShipmentStatusUpdatesResponse,
            400: SubmitShipmentStatusUpdatesResponse,
            403: SubmitShipmentStatusUpdatesResponse,
            404: SubmitShipmentStatusUpdatesResponse,
            413: SubmitShipmentStatusUpdatesResponse,
            415: SubmitShipmentStatusUpdatesResponse,
            429: SubmitShipmentStatusUpdatesResponse,
            500: SubmitShipmentStatusUpdatesResponse,
            503: SubmitShipmentStatusUpdatesResponse,
        }[response.status_code](self._get_response_json(response))

    def getCustomerInvoices(
        self,
        createdAfter: str,
        createdBefore: str,
        shipFromPartyId: str = None,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
    ):
        url = "/vendor/directFulfillment/shipping/v1/customerInvoices".format()
        params = {}
        if shipFromPartyId is not None:
            params["shipFromPartyId"] = (shipFromPartyId,)
        if limit is not None:
            params["limit"] = (limit,)
        if createdAfter is not None:
            params["createdAfter"] = (createdAfter,)
        if createdBefore is not None:
            params["createdBefore"] = (createdBefore,)
        if sortOrder is not None:
            params["sortOrder"] = (sortOrder,)
        if nextToken is not None:
            params["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetCustomerInvoicesResponse,
            400: GetCustomerInvoiceResponse,
            403: GetCustomerInvoiceResponse,
            404: GetCustomerInvoiceResponse,
            415: GetCustomerInvoiceResponse,
            429: GetCustomerInvoiceResponse,
            500: GetCustomerInvoiceResponse,
            503: GetCustomerInvoiceResponse,
        }[response.status_code](self._get_response_json(response))

    def getCustomerInvoice(
        self,
        purchaseOrderNumber: str,
    ):
        url = "/vendor/directFulfillment/shipping/v1/customerInvoices/{purchaseOrderNumber}".format(
            purchaseOrderNumber=purchaseOrderNumber,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetCustomerInvoiceResponse,
            400: GetCustomerInvoiceResponse,
            401: GetCustomerInvoiceResponse,
            403: GetCustomerInvoiceResponse,
            404: GetCustomerInvoiceResponse,
            415: GetCustomerInvoiceResponse,
            429: GetCustomerInvoiceResponse,
            500: GetCustomerInvoiceResponse,
            503: GetCustomerInvoiceResponse,
        }[response.status_code](self._get_response_json(response))

    def getPackingSlips(
        self,
        createdAfter: str,
        createdBefore: str,
        shipFromPartyId: str = None,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
    ):
        url = "/vendor/directFulfillment/shipping/v1/packingSlips".format()
        params = {}
        if shipFromPartyId is not None:
            params["shipFromPartyId"] = (shipFromPartyId,)
        if limit is not None:
            params["limit"] = (limit,)
        if createdAfter is not None:
            params["createdAfter"] = (createdAfter,)
        if createdBefore is not None:
            params["createdBefore"] = (createdBefore,)
        if sortOrder is not None:
            params["sortOrder"] = (sortOrder,)
        if nextToken is not None:
            params["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPackingSlipListResponse,
            400: GetPackingSlipListResponse,
            401: GetPackingSlipListResponse,
            403: GetPackingSlipListResponse,
            404: GetPackingSlipListResponse,
            415: GetPackingSlipListResponse,
            429: GetPackingSlipListResponse,
            500: GetPackingSlipListResponse,
            503: GetPackingSlipListResponse,
        }[response.status_code](self._get_response_json(response))

    def getPackingSlip(
        self,
        purchaseOrderNumber: str,
    ):
        url = "/vendor/directFulfillment/shipping/v1/packingSlips/{purchaseOrderNumber}".format(
            purchaseOrderNumber=purchaseOrderNumber,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPackingSlipResponse,
            400: GetPackingSlipResponse,
            401: GetPackingSlipResponse,
            403: GetPackingSlipResponse,
            404: GetPackingSlipResponse,
            415: GetPackingSlipResponse,
            429: GetPackingSlipResponse,
            500: GetPackingSlipResponse,
            503: GetPackingSlipResponse,
        }[response.status_code](self._get_response_json(response))
