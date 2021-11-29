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


class TransportationDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "carrierScac" in data:
            self.carrierScac: str = self._get_value(str, "carrierScac")
        else:
            self.carrierScac: str = None
        if "carrierShipmentReferenceNumber" in data:
            self.carrierShipmentReferenceNumber: str = self._get_value(str, "carrierShipmentReferenceNumber")
        else:
            self.carrierShipmentReferenceNumber: str = None
        if "transportationMode" in data:
            self.transportationMode: str = self._get_value(str, "transportationMode")
        else:
            self.transportationMode: str = None
        if "billOfLadingNumber" in data:
            self.billOfLadingNumber: str = self._get_value(str, "billOfLadingNumber")
        else:
            self.billOfLadingNumber: str = None


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
    The volume of the container.
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
    The weight.
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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
