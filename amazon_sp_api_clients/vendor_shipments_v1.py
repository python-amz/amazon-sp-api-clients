from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class SubmitShipmentConfirmationsRequest:
    """
    The request schema for the SubmitShipmentConfirmations operation.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentIdentifier" in data:
            self.shipmentIdentifier: str = str(data["shipmentIdentifier"])
        else:
            self.shipmentIdentifier: str = None
        if "shipmentConfirmationType" in data:
            self.shipmentConfirmationType: str = str(data["shipmentConfirmationType"])
        else:
            self.shipmentConfirmationType: str = None
        if "shipmentType" in data:
            self.shipmentType: str = str(data["shipmentType"])
        else:
            self.shipmentType: str = None
        if "shipmentStructure" in data:
            self.shipmentStructure: str = str(data["shipmentStructure"])
        else:
            self.shipmentStructure: str = None
        if "transportationDetails" in data:
            self.transportationDetails: TransportationDetails = TransportationDetails(data["transportationDetails"])
        else:
            self.transportationDetails: TransportationDetails = None
        if "amazonReferenceNumber" in data:
            self.amazonReferenceNumber: str = str(data["amazonReferenceNumber"])
        else:
            self.amazonReferenceNumber: str = None
        if "shipmentConfirmationDate" in data:
            self.shipmentConfirmationDate: str = str(data["shipmentConfirmationDate"])
        else:
            self.shipmentConfirmationDate: str = None
        if "shippedDate" in data:
            self.shippedDate: str = str(data["shippedDate"])
        else:
            self.shippedDate: str = None
        if "estimatedDeliveryDate" in data:
            self.estimatedDeliveryDate: str = str(data["estimatedDeliveryDate"])
        else:
            self.estimatedDeliveryDate: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = PartyIdentification(data["shipToParty"])
        else:
            self.shipToParty: PartyIdentification = None
        if "shipmentMeasurements" in data:
            self.shipmentMeasurements: ShipmentMeasurements = ShipmentMeasurements(data["shipmentMeasurements"])
        else:
            self.shipmentMeasurements: ShipmentMeasurements = None
        if "importDetails" in data:
            self.importDetails: ImportDetails = ImportDetails(data["importDetails"])
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


class ShipmentMeasurements:
    """
    Shipment measurement details.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "grossShipmentWeight" in data:
            self.grossShipmentWeight: Weight = Weight(data["grossShipmentWeight"])
        else:
            self.grossShipmentWeight: Weight = None
        if "shipmentVolume" in data:
            self.shipmentVolume: Volume = Volume(data["shipmentVolume"])
        else:
            self.shipmentVolume: Volume = None
        if "cartonCount" in data:
            self.cartonCount: int = int(data["cartonCount"])
        else:
            self.cartonCount: int = None
        if "palletCount" in data:
            self.palletCount: int = int(data["palletCount"])
        else:
            self.palletCount: int = None


class TransportationDetails:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "carrierScac" in data:
            self.carrierScac: str = str(data["carrierScac"])
        else:
            self.carrierScac: str = None
        if "carrierShipmentReferenceNumber" in data:
            self.carrierShipmentReferenceNumber: str = str(data["carrierShipmentReferenceNumber"])
        else:
            self.carrierShipmentReferenceNumber: str = None
        if "transportationMode" in data:
            self.transportationMode: str = str(data["transportationMode"])
        else:
            self.transportationMode: str = None
        if "billOfLadingNumber" in data:
            self.billOfLadingNumber: str = str(data["billOfLadingNumber"])
        else:
            self.billOfLadingNumber: str = None


class ImportDetails:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "methodOfPayment" in data:
            self.methodOfPayment: str = str(data["methodOfPayment"])
        else:
            self.methodOfPayment: str = None
        if "sealNumber" in data:
            self.sealNumber: str = str(data["sealNumber"])
        else:
            self.sealNumber: str = None
        if "route" in data:
            self.route: Route = Route(data["route"])
        else:
            self.route: Route = None
        if "importContainers" in data:
            self.importContainers: str = str(data["importContainers"])
        else:
            self.importContainers: str = None
        if "billableWeight" in data:
            self.billableWeight: Weight = Weight(data["billableWeight"])
        else:
            self.billableWeight: Weight = None
        if "estimatedShipByDate" in data:
            self.estimatedShipByDate: str = str(data["estimatedShipByDate"])
        else:
            self.estimatedShipByDate: str = None


class Item:
    """
    Details of the item being shipped.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = str(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: str = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = str(data["amazonProductIdentifier"])
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = ItemQuantity(data["shippedQuantity"])
        else:
            self.shippedQuantity: ItemQuantity = None
        if "itemDetails" in data:
            self.itemDetails: ItemDetails = ItemDetails(data["itemDetails"])
        else:
            self.itemDetails: ItemDetails = None


class Carton:
    """
    Details of the carton/package being shipped.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "cartonIdentifiers" in data:
            self.cartonIdentifiers: _List[ContainerIdentification] = [
                ContainerIdentification(datum) for datum in data["cartonIdentifiers"]
            ]
        else:
            self.cartonIdentifiers: _List[ContainerIdentification] = []
        if "cartonSequenceNumber" in data:
            self.cartonSequenceNumber: str = str(data["cartonSequenceNumber"])
        else:
            self.cartonSequenceNumber: str = None
        if "dimensions" in data:
            self.dimensions: Dimensions = Dimensions(data["dimensions"])
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = Weight(data["weight"])
        else:
            self.weight: Weight = None
        if "trackingNumber" in data:
            self.trackingNumber: str = str(data["trackingNumber"])
        else:
            self.trackingNumber: str = None
        if "items" in data:
            self.items: _List[ContainerItem] = [ContainerItem(datum) for datum in data["items"]]
        else:
            self.items: _List[ContainerItem] = []


class Pallet:
    """
    Details of the Pallet/Tare being shipped.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "palletIdentifiers" in data:
            self.palletIdentifiers: _List[ContainerIdentification] = [
                ContainerIdentification(datum) for datum in data["palletIdentifiers"]
            ]
        else:
            self.palletIdentifiers: _List[ContainerIdentification] = []
        if "tier" in data:
            self.tier: int = int(data["tier"])
        else:
            self.tier: int = None
        if "block" in data:
            self.block: int = int(data["block"])
        else:
            self.block: int = None
        if "dimensions" in data:
            self.dimensions: Dimensions = Dimensions(data["dimensions"])
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = Weight(data["weight"])
        else:
            self.weight: Weight = None
        if "cartonReferenceDetails" in data:
            self.cartonReferenceDetails: CartonReferenceDetails = CartonReferenceDetails(data["cartonReferenceDetails"])
        else:
            self.cartonReferenceDetails: CartonReferenceDetails = None
        if "items" in data:
            self.items: _List[ContainerItem] = [ContainerItem(datum) for datum in data["items"]]
        else:
            self.items: _List[ContainerItem] = []


class ItemDetails:
    """
    Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "lotNumber" in data:
            self.lotNumber: str = str(data["lotNumber"])
        else:
            self.lotNumber: str = None
        if "expiry" in data:
            self.expiry: Expiry = Expiry(data["expiry"])
        else:
            self.expiry: Expiry = None
        if "maximumRetailPrice" in data:
            self.maximumRetailPrice: Money = Money(data["maximumRetailPrice"])
        else:
            self.maximumRetailPrice: Money = None
        if "handlingCode" in data:
            self.handlingCode: str = str(data["handlingCode"])
        else:
            self.handlingCode: str = None


class ContainerIdentification:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "containerIdentificationType" in data:
            self.containerIdentificationType: str = str(data["containerIdentificationType"])
        else:
            self.containerIdentificationType: str = None
        if "containerIdentificationNumber" in data:
            self.containerIdentificationNumber: str = str(data["containerIdentificationNumber"])
        else:
            self.containerIdentificationNumber: str = None


class ContainerItem:
    """
    Carton/Pallet level details for the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemReference" in data:
            self.itemReference: str = str(data["itemReference"])
        else:
            self.itemReference: str = None
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = ItemQuantity(data["shippedQuantity"])
        else:
            self.shippedQuantity: ItemQuantity = None
        if "itemDetails" in data:
            self.itemDetails: ItemDetails = ItemDetails(data["itemDetails"])
        else:
            self.itemDetails: ItemDetails = None


class CartonReferenceDetails:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "cartonCount" in data:
            self.cartonCount: int = int(data["cartonCount"])
        else:
            self.cartonCount: int = None
        if "cartonReferenceNumbers" in data:
            self.cartonReferenceNumbers: _List[str] = [str(datum) for datum in data["cartonReferenceNumbers"]]
        else:
            self.cartonReferenceNumbers: _List[str] = []


class PartyIdentification:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "address" in data:
            self.address: Address = Address(data["address"])
        else:
            self.address: Address = None
        if "partyId" in data:
            self.partyId: str = str(data["partyId"])
        else:
            self.partyId: str = None
        if "taxRegistrationDetails" in data:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = [
                TaxRegistrationDetails(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = []


class TaxRegistrationDetails:
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


class Route:
    """
    This is used only for direct import shipment confirmations.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "stops" in data:
            self.stops: _List[Stop] = [Stop(datum) for datum in data["stops"]]
        else:
            self.stops: _List[Stop] = []


class Stop:
    """
    Contractual or operational port or point relevant to the movement of the cargo.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "functionCode" in data:
            self.functionCode: str = str(data["functionCode"])
        else:
            self.functionCode: str = None
        if "locationIdentification" in data:
            self.locationIdentification: Location = Location(data["locationIdentification"])
        else:
            self.locationIdentification: Location = None
        if "arrivalTime" in data:
            self.arrivalTime: str = str(data["arrivalTime"])
        else:
            self.arrivalTime: str = None
        if "departureTime" in data:
            self.departureTime: str = str(data["departureTime"])
        else:
            self.departureTime: str = None


class Location:
    """
    Location identifier.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "type" in data:
            self.type: str = str(data["type"])
        else:
            self.type: str = None
        if "locationCode" in data:
            self.locationCode: str = str(data["locationCode"])
        else:
            self.locationCode: str = None
        if "countryCode" in data:
            self.countryCode: str = str(data["countryCode"])
        else:
            self.countryCode: str = None


class Dimensions:
    """
    Physical dimensional measurements of a container.
    """

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


class Volume:
    """
    The volume of the container.
    """

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


class Weight:
    """
    The weight.
    """

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
        if "unitSize" in data:
            self.unitSize: int = int(data["unitSize"])
        else:
            self.unitSize: int = None


class Expiry:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "manufacturerDate" in data:
            self.manufacturerDate: str = str(data["manufacturerDate"])
        else:
            self.manufacturerDate: str = None
        if "expiryDate" in data:
            self.expiryDate: str = str(data["expiryDate"])
        else:
            self.expiryDate: str = None
        if "expiryAfterDuration" in data:
            self.expiryAfterDuration: Duration = Duration(data["expiryAfterDuration"])
        else:
            self.expiryAfterDuration: Duration = None


class Duration:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "durationUnit" in data:
            self.durationUnit: str = str(data["durationUnit"])
        else:
            self.durationUnit: str = None
        if "durationValue" in data:
            self.durationValue: int = int(data["durationValue"])
        else:
            self.durationValue: int = None


class SubmitShipmentConfirmationsResponse:
    """
    The response schema for the SubmitShipmentConfirmations operation.
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


class VendorShipmentsV1Client(__BaseClient):
    """
        Submits one or more shipment confirmations for vendor orders.
    **Usage Plans:**
    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |
    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def SubmitShipmentConfirmations(
        self,
        data: SubmitShipmentConfirmationsRequest,
    ):
        url = "/vendor/shipping/v1/shipmentConfirmations".format()
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
