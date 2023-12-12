from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class SubmitShipmentConfirmationsRequest(__BaseDictObject):
    """
    The request schema for the SubmitShipmentConfirmations operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentConfirmations" in data:
            self.shipmentConfirmations: _List[ShipmentConfirmation] = [
                ShipmentConfirmation(datum) for datum in data["shipmentConfirmations"]
            ]
        else:
            self.shipmentConfirmations: _List[ShipmentConfirmation] = []


class SubmitShipments(__BaseDictObject):
    """
    The request schema for the SubmitTransportRequestConfirmations operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipments" in data:
            self.shipments: _List[Shipment] = [Shipment(datum) for datum in data["shipments"]]
        else:
            self.shipments: _List[Shipment] = []


class GetShipmentDetailsResponse(__BaseDictObject):
    """
    The response schema for the GetShipmentDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ShipmentDetails = self._get_value(ShipmentDetails, "payload")
        else:
            self.payload: ShipmentDetails = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetShipmentLabels(__BaseDictObject):
    """
    The response schema for the GetShipmentLabels operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: transportationLabels = self._get_value(transportationLabels, "payload")
        else:
            self.payload: transportationLabels = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ShipmentDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "shipments" in data:
            self.shipments: _List[Shipment] = [Shipment(datum) for datum in data["shipments"]]
        else:
            self.shipments: _List[Shipment] = []


class transportationLabels(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "transportLabels" in data:
            self.transportLabels: _List[transportLabel] = [transportLabel(datum) for datum in data["transportLabels"]]
        else:
            self.transportLabels: _List[transportLabel] = []


class Pagination(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None


class ShipmentConfirmation(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentIdentifier" in data:
            self.shipmentIdentifier: str = self._get_value(str, "shipmentIdentifier")
        else:
            self.shipmentIdentifier: str = None
        if "shipmentConfirmationType" in data:
            self.shipmentConfirmationType: str = self._get_value(str, "shipmentConfirmationType")
        else:
            self.shipmentConfirmationType: str = None
        if "shipmentType" in data:
            self.shipmentType: str = self._get_value(str, "shipmentType")
        else:
            self.shipmentType: str = None
        if "shipmentStructure" in data:
            self.shipmentStructure: str = self._get_value(str, "shipmentStructure")
        else:
            self.shipmentStructure: str = None
        if "transportationDetails" in data:
            self.transportationDetails: TransportationDetails = self._get_value(
                TransportationDetails, "transportationDetails"
            )
        else:
            self.transportationDetails: TransportationDetails = None
        if "amazonReferenceNumber" in data:
            self.amazonReferenceNumber: str = self._get_value(str, "amazonReferenceNumber")
        else:
            self.amazonReferenceNumber: str = None
        if "shipmentConfirmationDate" in data:
            self.shipmentConfirmationDate: str = self._get_value(str, "shipmentConfirmationDate")
        else:
            self.shipmentConfirmationDate: str = None
        if "shippedDate" in data:
            self.shippedDate: str = self._get_value(str, "shippedDate")
        else:
            self.shippedDate: str = None
        if "estimatedDeliveryDate" in data:
            self.estimatedDeliveryDate: str = self._get_value(str, "estimatedDeliveryDate")
        else:
            self.estimatedDeliveryDate: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = self._get_value(PartyIdentification, "shipToParty")
        else:
            self.shipToParty: PartyIdentification = None
        if "shipmentMeasurements" in data:
            self.shipmentMeasurements: ShipmentMeasurements = self._get_value(
                ShipmentMeasurements, "shipmentMeasurements"
            )
        else:
            self.shipmentMeasurements: ShipmentMeasurements = None
        if "importDetails" in data:
            self.importDetails: ImportDetails = self._get_value(ImportDetails, "importDetails")
        else:
            self.importDetails: ImportDetails = None
        if "shippedItems" in data:
            self.shippedItems: _List[Item] = [Item(datum) for datum in data["shippedItems"]]
        else:
            self.shippedItems: _List[Item] = []
        if "cartons" in data:
            self.cartons: _List[Carton] = [Carton(datum) for datum in data["cartons"]]
        else:
            self.cartons: _List[Carton] = []
        if "pallets" in data:
            self.pallets: _List[Pallet] = [Pallet(datum) for datum in data["pallets"]]
        else:
            self.pallets: _List[Pallet] = []


class Shipment(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "vendorShipmentIdentifier" in data:
            self.vendorShipmentIdentifier: str = self._get_value(str, "vendorShipmentIdentifier")
        else:
            self.vendorShipmentIdentifier: str = None
        if "transactionType" in data:
            self.transactionType: str = self._get_value(str, "transactionType")
        else:
            self.transactionType: str = None
        if "buyerReferenceNumber" in data:
            self.buyerReferenceNumber: str = self._get_value(str, "buyerReferenceNumber")
        else:
            self.buyerReferenceNumber: str = None
        if "transactionDate" in data:
            self.transactionDate: str = self._get_value(str, "transactionDate")
        else:
            self.transactionDate: str = None
        if "currentShipmentStatus" in data:
            self.currentShipmentStatus: str = self._get_value(str, "currentShipmentStatus")
        else:
            self.currentShipmentStatus: str = None
        if "currentshipmentStatusDate" in data:
            self.currentshipmentStatusDate: str = self._get_value(str, "currentshipmentStatusDate")
        else:
            self.currentshipmentStatusDate: str = None
        if "shipmentStatusDetails" in data:
            self.shipmentStatusDetails: _List[ShipmentStatusDetails] = [
                ShipmentStatusDetails(datum) for datum in data["shipmentStatusDetails"]
            ]
        else:
            self.shipmentStatusDetails: _List[ShipmentStatusDetails] = []
        if "shipmentCreateDate" in data:
            self.shipmentCreateDate: str = self._get_value(str, "shipmentCreateDate")
        else:
            self.shipmentCreateDate: str = None
        if "shipmentConfirmDate" in data:
            self.shipmentConfirmDate: str = self._get_value(str, "shipmentConfirmDate")
        else:
            self.shipmentConfirmDate: str = None
        if "packageLabelCreateDate" in data:
            self.packageLabelCreateDate: str = self._get_value(str, "packageLabelCreateDate")
        else:
            self.packageLabelCreateDate: str = None
        if "shipmentFreightTerm" in data:
            self.shipmentFreightTerm: str = self._get_value(str, "shipmentFreightTerm")
        else:
            self.shipmentFreightTerm: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = self._get_value(PartyIdentification, "shipToParty")
        else:
            self.shipToParty: PartyIdentification = None
        if "shipmentMeasurements" in data:
            self.shipmentMeasurements: TransportShipmentMeasurements = self._get_value(
                TransportShipmentMeasurements, "shipmentMeasurements"
            )
        else:
            self.shipmentMeasurements: TransportShipmentMeasurements = None
        if "collectFreightPickupDetails" in data:
            self.collectFreightPickupDetails: collectFreightPickupDetails = self._get_value(
                collectFreightPickupDetails, "collectFreightPickupDetails"
            )
        else:
            self.collectFreightPickupDetails: collectFreightPickupDetails = None
        if "purchaseOrders" in data:
            self.purchaseOrders: _List[purchaseOrders] = [purchaseOrders(datum) for datum in data["purchaseOrders"]]
        else:
            self.purchaseOrders: _List[purchaseOrders] = []
        if "importDetails" in data:
            self.importDetails: ImportDetails = self._get_value(ImportDetails, "importDetails")
        else:
            self.importDetails: ImportDetails = None
        if "containers" in data:
            self.containers: _List[containers] = [containers(datum) for datum in data["containers"]]
        else:
            self.containers: _List[containers] = []
        if "transportationDetails" in data:
            self.transportationDetails: TransportationDetails = self._get_value(
                TransportationDetails, "transportationDetails"
            )
        else:
            self.transportationDetails: TransportationDetails = None


class transportLabel(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "labelCreateDateTime" in data:
            self.labelCreateDateTime: str = self._get_value(str, "labelCreateDateTime")
        else:
            self.labelCreateDateTime: str = None
        if "shipmentInformation" in data:
            self.shipmentInformation: ShipmentInformation = self._get_value(ShipmentInformation, "shipmentInformation")
        else:
            self.shipmentInformation: ShipmentInformation = None
        if "labelData" in data:
            self.labelData: _List[LabelData] = [LabelData(datum) for datum in data["labelData"]]
        else:
            self.labelData: _List[LabelData] = []


class ShipmentMeasurements(__BaseDictObject):
    """
    Shipment measurement details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "grossShipmentWeight" in data:
            self.grossShipmentWeight: Weight = self._get_value(Weight, "grossShipmentWeight")
        else:
            self.grossShipmentWeight: Weight = None
        if "shipmentVolume" in data:
            self.shipmentVolume: Volume = self._get_value(Volume, "shipmentVolume")
        else:
            self.shipmentVolume: Volume = None
        if "cartonCount" in data:
            self.cartonCount: int = self._get_value(int, "cartonCount")
        else:
            self.cartonCount: int = None
        if "palletCount" in data:
            self.palletCount: int = self._get_value(int, "palletCount")
        else:
            self.palletCount: int = None


class ShipmentInformation(__BaseDictObject):
    """
    Shipment Information details for Label request.
    """

    def __init__(self, data):
        super().__init__(data)
        if "vendorDetails" in data:
            self.vendorDetails: VendorDetails = self._get_value(VendorDetails, "vendorDetails")
        else:
            self.vendorDetails: VendorDetails = None
        if "buyerReferenceNumber" in data:
            self.buyerReferenceNumber: str = self._get_value(str, "buyerReferenceNumber")
        else:
            self.buyerReferenceNumber: str = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = self._get_value(PartyIdentification, "shipToParty")
        else:
            self.shipToParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "warehouseId" in data:
            self.warehouseId: str = self._get_value(str, "warehouseId")
        else:
            self.warehouseId: str = None
        if "masterTrackingId" in data:
            self.masterTrackingId: str = self._get_value(str, "masterTrackingId")
        else:
            self.masterTrackingId: str = None
        if "totalLabelCount" in data:
            self.totalLabelCount: int = self._get_value(int, "totalLabelCount")
        else:
            self.totalLabelCount: int = None
        if "shipMode" in data:
            self.shipMode: str = self._get_value(str, "shipMode")
        else:
            self.shipMode: str = None


class LabelData(__BaseDictObject):
    """
    Label details as part of the transport label response
    """

    def __init__(self, data):
        super().__init__(data)
        if "labelSequenceNumber" in data:
            self.labelSequenceNumber: int = self._get_value(int, "labelSequenceNumber")
        else:
            self.labelSequenceNumber: int = None
        if "labelFormat" in data:
            self.labelFormat: str = self._get_value(str, "labelFormat")
        else:
            self.labelFormat: str = None
        if "carrierCode" in data:
            self.carrierCode: str = self._get_value(str, "carrierCode")
        else:
            self.carrierCode: str = None
        if "trackingId" in data:
            self.trackingId: str = self._get_value(str, "trackingId")
        else:
            self.trackingId: str = None
        if "label" in data:
            self.label: str = self._get_value(str, "label")
        else:
            self.label: str = None


class VendorDetails(__BaseDictObject):
    """
    Vendor Details as part of Label response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "vendorShipmentId" in data:
            self.vendorShipmentId: str = self._get_value(str, "vendorShipmentId")
        else:
            self.vendorShipmentId: str = None


class ShipmentStatusDetails(__BaseDictObject):
    """
    Shipment Status details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentStatus" in data:
            self.shipmentStatus: str = self._get_value(str, "shipmentStatus")
        else:
            self.shipmentStatus: str = None
        if "shipmentStatusDate" in data:
            self.shipmentStatusDate: str = self._get_value(str, "shipmentStatusDate")
        else:
            self.shipmentStatusDate: str = None


class TransportShipmentMeasurements(__BaseDictObject):
    """
    Shipment measurement details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalCartonCount" in data:
            self.totalCartonCount: int = self._get_value(int, "totalCartonCount")
        else:
            self.totalCartonCount: int = None
        if "totalPalletStackable" in data:
            self.totalPalletStackable: int = self._get_value(int, "totalPalletStackable")
        else:
            self.totalPalletStackable: int = None
        if "totalPalletNonStackable" in data:
            self.totalPalletNonStackable: int = self._get_value(int, "totalPalletNonStackable")
        else:
            self.totalPalletNonStackable: int = None
        if "shipmentWeight" in data:
            self.shipmentWeight: Weight = self._get_value(Weight, "shipmentWeight")
        else:
            self.shipmentWeight: Weight = None
        if "shipmentVolume" in data:
            self.shipmentVolume: Volume = self._get_value(Volume, "shipmentVolume")
        else:
            self.shipmentVolume: Volume = None


class collectFreightPickupDetails(__BaseDictObject):
    """
    Transport Request pickup date from Vendor Warehouse by Buyer
    """

    def __init__(self, data):
        super().__init__(data)
        if "requestedPickUp" in data:
            self.requestedPickUp: str = self._get_value(str, "requestedPickUp")
        else:
            self.requestedPickUp: str = None
        if "scheduledPickUp" in data:
            self.scheduledPickUp: str = self._get_value(str, "scheduledPickUp")
        else:
            self.scheduledPickUp: str = None
        if "carrierAssignmentDate" in data:
            self.carrierAssignmentDate: str = self._get_value(str, "carrierAssignmentDate")
        else:
            self.carrierAssignmentDate: str = None


class purchaseOrders(__BaseDictObject):
    """
    Transport Request pickup date
    """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "purchaseOrderDate" in data:
            self.purchaseOrderDate: str = self._get_value(str, "purchaseOrderDate")
        else:
            self.purchaseOrderDate: str = None
        if "shipWindow" in data:
            self.shipWindow: str = self._get_value(str, "shipWindow")
        else:
            self.shipWindow: str = None
        if "items" in data:
            self.items: _List[PurchaseOrderItems] = [PurchaseOrderItems(datum) for datum in data["items"]]
        else:
            self.items: _List[PurchaseOrderItems] = []


class TransportationDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "shipMode" in data:
            self.shipMode: str = self._get_value(str, "shipMode")
        else:
            self.shipMode: str = None
        if "transportationMode" in data:
            self.transportationMode: str = self._get_value(str, "transportationMode")
        else:
            self.transportationMode: str = None
        if "shippedDate" in data:
            self.shippedDate: str = self._get_value(str, "shippedDate")
        else:
            self.shippedDate: str = None
        if "estimatedDeliveryDate" in data:
            self.estimatedDeliveryDate: str = self._get_value(str, "estimatedDeliveryDate")
        else:
            self.estimatedDeliveryDate: str = None
        if "shipmentDeliveryDate" in data:
            self.shipmentDeliveryDate: str = self._get_value(str, "shipmentDeliveryDate")
        else:
            self.shipmentDeliveryDate: str = None
        if "carrierDetails" in data:
            self.carrierDetails: CarrierDetails = self._get_value(CarrierDetails, "carrierDetails")
        else:
            self.carrierDetails: CarrierDetails = None
        if "billOfLadingNumber" in data:
            self.billOfLadingNumber: str = self._get_value(str, "billOfLadingNumber")
        else:
            self.billOfLadingNumber: str = None


class CarrierDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "phone" in data:
            self.phone: str = self._get_value(str, "phone")
        else:
            self.phone: str = None
        if "email" in data:
            self.email: str = self._get_value(str, "email")
        else:
            self.email: str = None
        if "shipmentReferenceNumber" in data:
            self.shipmentReferenceNumber: str = self._get_value(str, "shipmentReferenceNumber")
        else:
            self.shipmentReferenceNumber: str = None


class ImportDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "methodOfPayment" in data:
            self.methodOfPayment: str = self._get_value(str, "methodOfPayment")
        else:
            self.methodOfPayment: str = None
        if "sealNumber" in data:
            self.sealNumber: str = self._get_value(str, "sealNumber")
        else:
            self.sealNumber: str = None
        if "route" in data:
            self.route: Route = self._get_value(Route, "route")
        else:
            self.route: Route = None
        if "importContainers" in data:
            self.importContainers: str = self._get_value(str, "importContainers")
        else:
            self.importContainers: str = None
        if "billableWeight" in data:
            self.billableWeight: Weight = self._get_value(Weight, "billableWeight")
        else:
            self.billableWeight: Weight = None
        if "estimatedShipByDate" in data:
            self.estimatedShipByDate: str = self._get_value(str, "estimatedShipByDate")
        else:
            self.estimatedShipByDate: str = None
        if "handlingInstructions" in data:
            self.handlingInstructions: str = self._get_value(str, "handlingInstructions")
        else:
            self.handlingInstructions: str = None


class containers(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "containerType" in data:
            self.containerType: str = self._get_value(str, "containerType")
        else:
            self.containerType: str = None
        if "containerSequenceNumber" in data:
            self.containerSequenceNumber: str = self._get_value(str, "containerSequenceNumber")
        else:
            self.containerSequenceNumber: str = None
        if "containerIdentifiers" in data:
            self.containerIdentifiers: _List[ContainerIdentification] = [
                ContainerIdentification(datum) for datum in data["containerIdentifiers"]
            ]
        else:
            self.containerIdentifiers: _List[ContainerIdentification] = []
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "dimensions" in data:
            self.dimensions: Dimensions = self._get_value(Dimensions, "dimensions")
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = self._get_value(Weight, "weight")
        else:
            self.weight: Weight = None
        if "tier" in data:
            self.tier: int = self._get_value(int, "tier")
        else:
            self.tier: int = None
        if "block" in data:
            self.block: int = self._get_value(int, "block")
        else:
            self.block: int = None
        if "innerContainersDetails" in data:
            self.innerContainersDetails: InnerContainersDetails = self._get_value(
                InnerContainersDetails, "innerContainersDetails"
            )
        else:
            self.innerContainersDetails: InnerContainersDetails = None
        if "packedItems" in data:
            self.packedItems: _List[PackedItems] = [PackedItems(datum) for datum in data["packedItems"]]
        else:
            self.packedItems: _List[PackedItems] = []


class PackedItems(__BaseDictObject):
    """
    Details of the item being shipped.
    """

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
        if "packedQuantity" in data:
            self.packedQuantity: ItemQuantity = self._get_value(ItemQuantity, "packedQuantity")
        else:
            self.packedQuantity: ItemQuantity = None
        if "itemDetails" in data:
            self.itemDetails: PackageItemDetails = self._get_value(PackageItemDetails, "itemDetails")
        else:
            self.itemDetails: PackageItemDetails = None


class Item(__BaseDictObject):
    """
    Details of the item being shipped.
    """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = self._get_value(str, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: str = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = self._get_value(str, "amazonProductIdentifier")
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = self._get_value(ItemQuantity, "shippedQuantity")
        else:
            self.shippedQuantity: ItemQuantity = None
        if "itemDetails" in data:
            self.itemDetails: ItemDetails = self._get_value(ItemDetails, "itemDetails")
        else:
            self.itemDetails: ItemDetails = None


class PurchaseOrderItems(__BaseDictObject):
    """
    Details of the item being shipped.
    """

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
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = self._get_value(ItemQuantity, "shippedQuantity")
        else:
            self.shippedQuantity: ItemQuantity = None
        if "maximumRetailPrice" in data:
            self.maximumRetailPrice: Money = self._get_value(Money, "maximumRetailPrice")
        else:
            self.maximumRetailPrice: Money = None


class Carton(__BaseDictObject):
    """
    Details of the carton/package being shipped.
    """

    def __init__(self, data):
        super().__init__(data)
        if "cartonIdentifiers" in data:
            self.cartonIdentifiers: _List[ContainerIdentification] = [
                ContainerIdentification(datum) for datum in data["cartonIdentifiers"]
            ]
        else:
            self.cartonIdentifiers: _List[ContainerIdentification] = []
        if "cartonSequenceNumber" in data:
            self.cartonSequenceNumber: str = self._get_value(str, "cartonSequenceNumber")
        else:
            self.cartonSequenceNumber: str = None
        if "dimensions" in data:
            self.dimensions: Dimensions = self._get_value(Dimensions, "dimensions")
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = self._get_value(Weight, "weight")
        else:
            self.weight: Weight = None
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "items" in data:
            self.items: _List[ContainerItem] = [ContainerItem(datum) for datum in data["items"]]
        else:
            self.items: _List[ContainerItem] = []


class InnerContainersDetails(__BaseDictObject):
    """
    Details of the innerContainersDetails.
    """

    def __init__(self, data):
        super().__init__(data)
        if "containerCount" in data:
            self.containerCount: int = self._get_value(int, "containerCount")
        else:
            self.containerCount: int = None
        if "containerSequenceNumbers" in data:
            self.containerSequenceNumbers: _List[ContainerSequenceNumbers] = [
                ContainerSequenceNumbers(datum) for datum in data["containerSequenceNumbers"]
            ]
        else:
            self.containerSequenceNumbers: _List[ContainerSequenceNumbers] = []


class ContainerSequenceNumbers(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "containerSequenceNumber" in data:
            self.containerSequenceNumber: str = self._get_value(str, "containerSequenceNumber")
        else:
            self.containerSequenceNumber: str = None


class Pallet(__BaseDictObject):
    """
    Details of the Pallet/Tare being shipped.
    """

    def __init__(self, data):
        super().__init__(data)
        if "palletIdentifiers" in data:
            self.palletIdentifiers: _List[ContainerIdentification] = [
                ContainerIdentification(datum) for datum in data["palletIdentifiers"]
            ]
        else:
            self.palletIdentifiers: _List[ContainerIdentification] = []
        if "tier" in data:
            self.tier: int = self._get_value(int, "tier")
        else:
            self.tier: int = None
        if "block" in data:
            self.block: int = self._get_value(int, "block")
        else:
            self.block: int = None
        if "dimensions" in data:
            self.dimensions: Dimensions = self._get_value(Dimensions, "dimensions")
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = self._get_value(Weight, "weight")
        else:
            self.weight: Weight = None
        if "cartonReferenceDetails" in data:
            self.cartonReferenceDetails: CartonReferenceDetails = self._get_value(
                CartonReferenceDetails, "cartonReferenceDetails"
            )
        else:
            self.cartonReferenceDetails: CartonReferenceDetails = None
        if "items" in data:
            self.items: _List[ContainerItem] = [ContainerItem(datum) for datum in data["items"]]
        else:
            self.items: _List[ContainerItem] = []


class ItemDetails(__BaseDictObject):
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "lotNumber" in data:
            self.lotNumber: str = self._get_value(str, "lotNumber")
        else:
            self.lotNumber: str = None
        if "expiry" in data:
            self.expiry: Expiry = self._get_value(Expiry, "expiry")
        else:
            self.expiry: Expiry = None
        if "maximumRetailPrice" in data:
            self.maximumRetailPrice: Money = self._get_value(Money, "maximumRetailPrice")
        else:
            self.maximumRetailPrice: Money = None
        if "handlingCode" in data:
            self.handlingCode: str = self._get_value(str, "handlingCode")
        else:
            self.handlingCode: str = None


class PackageItemDetails(__BaseDictObject):
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "lotNumber" in data:
            self.lotNumber: str = self._get_value(str, "lotNumber")
        else:
            self.lotNumber: str = None
        if "expiry" in data:
            self.expiry: Expiry = self._get_value(Expiry, "expiry")
        else:
            self.expiry: Expiry = None


class PurchaseOrderItemDetails(__BaseDictObject):
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    def __init__(self, data):
        super().__init__(data)
        if "maximumRetailPrice" in data:
            self.maximumRetailPrice: Money = self._get_value(Money, "maximumRetailPrice")
        else:
            self.maximumRetailPrice: Money = None


class ContainerIdentification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "containerIdentificationType" in data:
            self.containerIdentificationType: str = self._get_value(str, "containerIdentificationType")
        else:
            self.containerIdentificationType: str = None
        if "containerIdentificationNumber" in data:
            self.containerIdentificationNumber: str = self._get_value(str, "containerIdentificationNumber")
        else:
            self.containerIdentificationNumber: str = None


class ContainerItem(__BaseDictObject):
    """
    Carton/Pallet level details for the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "itemReference" in data:
            self.itemReference: str = self._get_value(str, "itemReference")
        else:
            self.itemReference: str = None
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = self._get_value(ItemQuantity, "shippedQuantity")
        else:
            self.shippedQuantity: ItemQuantity = None
        if "itemDetails" in data:
            self.itemDetails: ItemDetails = self._get_value(ItemDetails, "itemDetails")
        else:
            self.itemDetails: ItemDetails = None


class CartonReferenceDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "cartonCount" in data:
            self.cartonCount: int = self._get_value(int, "cartonCount")
        else:
            self.cartonCount: int = None
        if "cartonReferenceNumbers" in data:
            self.cartonReferenceNumbers: _List[str] = [str(datum) for datum in data["cartonReferenceNumbers"]]
        else:
            self.cartonReferenceNumbers: _List[str] = []


class PartyIdentification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None
        if "partyId" in data:
            self.partyId: str = self._get_value(str, "partyId")
        else:
            self.partyId: str = None
        if "taxRegistrationDetails" in data:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = [
                TaxRegistrationDetails(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = []


class TaxRegistrationDetails(__BaseDictObject):
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


class Route(__BaseDictObject):
    """
    This is used only for direct import shipment confirmations.
    """

    def __init__(self, data):
        super().__init__(data)
        if "stops" in data:
            self.stops: _List[Stop] = [Stop(datum) for datum in data["stops"]]
        else:
            self.stops: _List[Stop] = []


class Stop(__BaseDictObject):
    """
    Contractual or operational port or point relevant to the movement of the cargo.
    """

    def __init__(self, data):
        super().__init__(data)
        if "functionCode" in data:
            self.functionCode: str = self._get_value(str, "functionCode")
        else:
            self.functionCode: str = None
        if "locationIdentification" in data:
            self.locationIdentification: Location = self._get_value(Location, "locationIdentification")
        else:
            self.locationIdentification: Location = None
        if "arrivalTime" in data:
            self.arrivalTime: str = self._get_value(str, "arrivalTime")
        else:
            self.arrivalTime: str = None
        if "departureTime" in data:
            self.departureTime: str = self._get_value(str, "departureTime")
        else:
            self.departureTime: str = None


class Location(__BaseDictObject):
    """
    Location identifier.
    """

    def __init__(self, data):
        super().__init__(data)
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None
        if "locationCode" in data:
            self.locationCode: str = self._get_value(str, "locationCode")
        else:
            self.locationCode: str = None
        if "countryCode" in data:
            self.countryCode: str = self._get_value(str, "countryCode")
        else:
            self.countryCode: str = None


class Dimensions(__BaseDictObject):
    """
    Physical dimensional measurements of a container.
    """

    def __init__(self, data):
        super().__init__(data)
        if "length" in data:
            self.length: Decimal = self._get_value(Decimal, "length")
        else:
            self.length: Decimal = None
        if "width" in data:
            self.width: Decimal = self._get_value(Decimal, "width")
        else:
            self.width: Decimal = None
        if "height" in data:
            self.height: Decimal = self._get_value(Decimal, "height")
        else:
            self.height: Decimal = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None


class Volume(__BaseDictObject):
    """
    The volume of the shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None
        if "value" in data:
            self.value: Decimal = self._get_value(Decimal, "value")
        else:
            self.value: Decimal = None


class Weight(__BaseDictObject):
    """
    The weight of the shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None
        if "value" in data:
            self.value: Decimal = self._get_value(Decimal, "value")
        else:
            self.value: Decimal = None


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
        if "unitSize" in data:
            self.unitSize: int = self._get_value(int, "unitSize")
        else:
            self.unitSize: int = None


class packedQuantity(__BaseDictObject):
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
        if "unitSize" in data:
            self.unitSize: int = self._get_value(int, "unitSize")
        else:
            self.unitSize: int = None


class Expiry(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "manufacturerDate" in data:
            self.manufacturerDate: str = self._get_value(str, "manufacturerDate")
        else:
            self.manufacturerDate: str = None
        if "expiryDate" in data:
            self.expiryDate: str = self._get_value(str, "expiryDate")
        else:
            self.expiryDate: str = None
        if "expiryAfterDuration" in data:
            self.expiryAfterDuration: Duration = self._get_value(Duration, "expiryAfterDuration")
        else:
            self.expiryAfterDuration: Duration = None


class Duration(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "durationUnit" in data:
            self.durationUnit: str = self._get_value(str, "durationUnit")
        else:
            self.durationUnit: str = None
        if "durationValue" in data:
            self.durationValue: int = self._get_value(int, "durationValue")
        else:
            self.durationValue: int = None


class SubmitShipmentConfirmationsResponse(__BaseDictObject):
    """
    The response schema for the SubmitShipmentConfirmations operation.
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


class VendorShipmentsV1Client(__BaseClient):
    def SubmitShipmentConfirmations(
        self,
        data: SubmitShipmentConfirmationsRequest,
    ):
        """
                Submits one or more shipment confirmations for vendor orders.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/shipping/v1/shipmentConfirmations"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: SubmitShipmentConfirmationsResponse,
            400: SubmitShipmentConfirmationsResponse,
            403: SubmitShipmentConfirmationsResponse,
            404: SubmitShipmentConfirmationsResponse,
            413: SubmitShipmentConfirmationsResponse,
            415: SubmitShipmentConfirmationsResponse,
            429: SubmitShipmentConfirmationsResponse,
            500: SubmitShipmentConfirmationsResponse,
            503: SubmitShipmentConfirmationsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def GetShipmentDetails(
        self,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
        createdAfter: str = None,
        createdBefore: str = None,
        shipmentConfirmedBefore: str = None,
        shipmentConfirmedAfter: str = None,
        packageLabelCreatedBefore: str = None,
        packageLabelCreatedAfter: str = None,
        shippedBefore: str = None,
        shippedAfter: str = None,
        estimatedDeliveryBefore: str = None,
        estimatedDeliveryAfter: str = None,
        shipmentDeliveryBefore: str = None,
        shipmentDeliveryAfter: str = None,
        requestedPickUpBefore: str = None,
        requestedPickUpAfter: str = None,
        scheduledPickUpBefore: str = None,
        scheduledPickUpAfter: str = None,
        currentShipmentStatus: str = None,
        vendorShipmentIdentifier: str = None,
        buyerReferenceNumber: str = None,
        buyerWarehouseCode: str = None,
        sellerWarehouseCode: str = None,
    ):
        """
                Returns the Details about Shipment, Carrier Details,  status of the shipment, container details and other details related to shipment based on the filter parameters value that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/shipping/v1/shipments"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if sortOrder is not None:
            params["sortOrder"] = sortOrder
        if nextToken is not None:
            params["nextToken"] = nextToken
        if createdAfter is not None:
            params["createdAfter"] = createdAfter
        if createdBefore is not None:
            params["createdBefore"] = createdBefore
        if shipmentConfirmedBefore is not None:
            params["shipmentConfirmedBefore"] = shipmentConfirmedBefore
        if shipmentConfirmedAfter is not None:
            params["shipmentConfirmedAfter"] = shipmentConfirmedAfter
        if packageLabelCreatedBefore is not None:
            params["packageLabelCreatedBefore"] = packageLabelCreatedBefore
        if packageLabelCreatedAfter is not None:
            params["packageLabelCreatedAfter"] = packageLabelCreatedAfter
        if shippedBefore is not None:
            params["shippedBefore"] = shippedBefore
        if shippedAfter is not None:
            params["shippedAfter"] = shippedAfter
        if estimatedDeliveryBefore is not None:
            params["estimatedDeliveryBefore"] = estimatedDeliveryBefore
        if estimatedDeliveryAfter is not None:
            params["estimatedDeliveryAfter"] = estimatedDeliveryAfter
        if shipmentDeliveryBefore is not None:
            params["shipmentDeliveryBefore"] = shipmentDeliveryBefore
        if shipmentDeliveryAfter is not None:
            params["shipmentDeliveryAfter"] = shipmentDeliveryAfter
        if requestedPickUpBefore is not None:
            params["requestedPickUpBefore"] = requestedPickUpBefore
        if requestedPickUpAfter is not None:
            params["requestedPickUpAfter"] = requestedPickUpAfter
        if scheduledPickUpBefore is not None:
            params["scheduledPickUpBefore"] = scheduledPickUpBefore
        if scheduledPickUpAfter is not None:
            params["scheduledPickUpAfter"] = scheduledPickUpAfter
        if currentShipmentStatus is not None:
            params["currentShipmentStatus"] = currentShipmentStatus
        if vendorShipmentIdentifier is not None:
            params["vendorShipmentIdentifier"] = vendorShipmentIdentifier
        if buyerReferenceNumber is not None:
            params["buyerReferenceNumber"] = buyerReferenceNumber
        if buyerWarehouseCode is not None:
            params["buyerWarehouseCode"] = buyerWarehouseCode
        if sellerWarehouseCode is not None:
            params["sellerWarehouseCode"] = sellerWarehouseCode
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

    def SubmitShipments(
        self,
        data: SubmitShipments,
    ):
        """
                Submits one or more shipment request for vendor Orders.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/shipping/v1/shipments"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: SubmitShipmentConfirmationsResponse,
            400: SubmitShipmentConfirmationsResponse,
            403: SubmitShipmentConfirmationsResponse,
            404: SubmitShipmentConfirmationsResponse,
            413: SubmitShipmentConfirmationsResponse,
            415: SubmitShipmentConfirmationsResponse,
            429: SubmitShipmentConfirmationsResponse,
            500: SubmitShipmentConfirmationsResponse,
            503: SubmitShipmentConfirmationsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def GetShipmentLabels(
        self,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
        labelCreatedAfter: str = None,
        labelcreatedBefore: str = None,
        buyerReferenceNumber: str = None,
        vendorShipmentIdentifier: str = None,
        sellerWarehouseCode: str = None,
    ):
        """
                Returns transport Labels based on the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/shipping/v1/transportLabels"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if sortOrder is not None:
            params["sortOrder"] = sortOrder
        if nextToken is not None:
            params["nextToken"] = nextToken
        if labelCreatedAfter is not None:
            params["labelCreatedAfter"] = labelCreatedAfter
        if labelcreatedBefore is not None:
            params["labelcreatedBefore"] = labelcreatedBefore
        if buyerReferenceNumber is not None:
            params["buyerReferenceNumber"] = buyerReferenceNumber
        if vendorShipmentIdentifier is not None:
            params["vendorShipmentIdentifier"] = vendorShipmentIdentifier
        if sellerWarehouseCode is not None:
            params["sellerWarehouseCode"] = sellerWarehouseCode
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetShipmentLabels,
            400: GetShipmentLabels,
            401: GetShipmentLabels,
            403: GetShipmentLabels,
            404: GetShipmentLabels,
            415: GetShipmentLabels,
            429: GetShipmentLabels,
            500: GetShipmentLabels,
            503: GetShipmentLabels,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
