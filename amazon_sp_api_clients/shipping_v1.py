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


class Location(__BaseDictObject):
    """
    The location where the person, business or institution is located.
    """

    def __init__(self, data):
        super().__init__(data)
        if "stateOrRegion" in data:
            self.stateOrRegion: StateOrRegion = self._get_value(StateOrRegion, "stateOrRegion")
        else:
            self.stateOrRegion: StateOrRegion = None
        if "city" in data:
            self.city: City = self._get_value(City, "city")
        else:
            self.city: City = None
        if "countryCode" in data:
            self.countryCode: CountryCode = self._get_value(CountryCode, "countryCode")
        else:
            self.countryCode: CountryCode = None
        if "postalCode" in data:
            self.postalCode: PostalCode = self._get_value(PostalCode, "postalCode")
        else:
            self.postalCode: PostalCode = None


class Event(__BaseDictObject):
    """
    An event of a shipment
    """

    def __init__(self, data):
        super().__init__(data)
        if "eventCode" in data:
            self.eventCode: EventCode = self._get_value(EventCode, "eventCode")
        else:
            self.eventCode: EventCode = None
        if "eventTime" in data:
            self.eventTime: str = self._get_value(str, "eventTime")
        else:
            self.eventTime: str = None
        if "location" in data:
            self.location: Location = self._get_value(Location, "location")
        else:
            self.location: Location = None


class TrackingSummary(__BaseDictObject):
    """
    The tracking summary.
    """

    def __init__(self, data):
        super().__init__(data)
        if "status" in data:
            self.status: str = self._get_value(str, "status")
        else:
            self.status: str = None


class Address(__BaseDictObject):
    """
    The address.
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
        if "stateOrRegion" in data:
            self.stateOrRegion: StateOrRegion = self._get_value(StateOrRegion, "stateOrRegion")
        else:
            self.stateOrRegion: StateOrRegion = None
        if "city" in data:
            self.city: City = self._get_value(City, "city")
        else:
            self.city: City = None
        if "countryCode" in data:
            self.countryCode: CountryCode = self._get_value(CountryCode, "countryCode")
        else:
            self.countryCode: CountryCode = None
        if "postalCode" in data:
            self.postalCode: PostalCode = self._get_value(PostalCode, "postalCode")
        else:
            self.postalCode: PostalCode = None
        if "email" in data:
            self.email: str = self._get_value(str, "email")
        else:
            self.email: str = None
        if "copyEmails" in data:
            self.copyEmails: _List[str] = [str(datum) for datum in data["copyEmails"]]
        else:
            self.copyEmails: _List[str] = []
        if "phoneNumber" in data:
            self.phoneNumber: str = self._get_value(str, "phoneNumber")
        else:
            self.phoneNumber: str = None


class TimeRange(__BaseDictObject):
    """
    The time range.
    """

    def __init__(self, data):
        super().__init__(data)
        if "start" in data:
            self.start: str = self._get_value(str, "start")
        else:
            self.start: str = None
        if "end" in data:
            self.end: str = self._get_value(str, "end")
        else:
            self.end: str = None


class ShippingPromiseSet(__BaseDictObject):
    """
    The promised delivery time and pickup time.
    """

    def __init__(self, data):
        super().__init__(data)
        if "deliveryWindow" in data:
            self.deliveryWindow: TimeRange = self._get_value(TimeRange, "deliveryWindow")
        else:
            self.deliveryWindow: TimeRange = None
        if "receiveWindow" in data:
            self.receiveWindow: TimeRange = self._get_value(TimeRange, "receiveWindow")
        else:
            self.receiveWindow: TimeRange = None


class Rate(__BaseDictObject):
    """
    The available rate that can be used to send the shipment
    """

    def __init__(self, data):
        super().__init__(data)
        if "rateId" in data:
            self.rateId: str = self._get_value(str, "rateId")
        else:
            self.rateId: str = None
        if "totalCharge" in data:
            self.totalCharge: Currency = self._get_value(Currency, "totalCharge")
        else:
            self.totalCharge: Currency = None
        if "billedWeight" in data:
            self.billedWeight: Weight = self._get_value(Weight, "billedWeight")
        else:
            self.billedWeight: Weight = None
        if "expirationTime" in data:
            self.expirationTime: str = self._get_value(str, "expirationTime")
        else:
            self.expirationTime: str = None
        if "serviceType" in data:
            self.serviceType: ServiceType = self._get_value(ServiceType, "serviceType")
        else:
            self.serviceType: ServiceType = None
        if "promise" in data:
            self.promise: ShippingPromiseSet = self._get_value(ShippingPromiseSet, "promise")
        else:
            self.promise: ShippingPromiseSet = None


class AcceptedRate(__BaseDictObject):
    """
    The specific rate purchased for the shipment, or null if unpurchased.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalCharge" in data:
            self.totalCharge: Currency = self._get_value(Currency, "totalCharge")
        else:
            self.totalCharge: Currency = None
        if "billedWeight" in data:
            self.billedWeight: Weight = self._get_value(Weight, "billedWeight")
        else:
            self.billedWeight: Weight = None
        if "serviceType" in data:
            self.serviceType: ServiceType = self._get_value(ServiceType, "serviceType")
        else:
            self.serviceType: ServiceType = None
        if "promise" in data:
            self.promise: ShippingPromiseSet = self._get_value(ShippingPromiseSet, "promise")
        else:
            self.promise: ShippingPromiseSet = None


class ServiceRate(__BaseDictObject):
    """
    The specific rate for a shipping service, or null if no service available.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalCharge" in data:
            self.totalCharge: Currency = self._get_value(Currency, "totalCharge")
        else:
            self.totalCharge: Currency = None
        if "billableWeight" in data:
            self.billableWeight: Weight = self._get_value(Weight, "billableWeight")
        else:
            self.billableWeight: Weight = None
        if "serviceType" in data:
            self.serviceType: ServiceType = self._get_value(ServiceType, "serviceType")
        else:
            self.serviceType: ServiceType = None
        if "promise" in data:
            self.promise: ShippingPromiseSet = self._get_value(ShippingPromiseSet, "promise")
        else:
            self.promise: ShippingPromiseSet = None


class Party(__BaseDictObject):
    """
    The account related with the shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "accountId" in data:
            self.accountId: AccountId = self._get_value(AccountId, "accountId")
        else:
            self.accountId: AccountId = None


class Currency(__BaseDictObject):
    """
    The total value of all items in the container.
    """

    def __init__(self, data):
        super().__init__(data)
        if "value" in data:
            self.value: float = self._get_value(float, "value")
        else:
            self.value: float = None
        if "unit" in data:
            self.unit: str = self._get_value(str, "unit")
        else:
            self.unit: str = None


class Dimensions(__BaseDictObject):
    """
    A set of measurements for a three-dimensional object.
    """

    def __init__(self, data):
        super().__init__(data)
        if "length" in data:
            self.length: float = self._get_value(float, "length")
        else:
            self.length: float = None
        if "width" in data:
            self.width: float = self._get_value(float, "width")
        else:
            self.width: float = None
        if "height" in data:
            self.height: float = self._get_value(float, "height")
        else:
            self.height: float = None
        if "unit" in data:
            self.unit: str = self._get_value(str, "unit")
        else:
            self.unit: str = None


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
            self.value: float = self._get_value(float, "value")
        else:
            self.value: float = None


class ContainerItem(__BaseDictObject):
    """
    Item in the container.
    """

    def __init__(self, data):
        super().__init__(data)
        if "quantity" in data:
            self.quantity: float = self._get_value(float, "quantity")
        else:
            self.quantity: float = None
        if "unitPrice" in data:
            self.unitPrice: Currency = self._get_value(Currency, "unitPrice")
        else:
            self.unitPrice: Currency = None
        if "unitWeight" in data:
            self.unitWeight: Weight = self._get_value(Weight, "unitWeight")
        else:
            self.unitWeight: Weight = None
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None


class Container(__BaseDictObject):
    """
    Container in the shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "containerType" in data:
            self.containerType: str = self._get_value(str, "containerType")
        else:
            self.containerType: str = None
        if "containerReferenceId" in data:
            self.containerReferenceId: ContainerReferenceId = self._get_value(
                ContainerReferenceId, "containerReferenceId"
            )
        else:
            self.containerReferenceId: ContainerReferenceId = None
        if "value" in data:
            self.value: Currency = self._get_value(Currency, "value")
        else:
            self.value: Currency = None
        if "dimensions" in data:
            self.dimensions: Dimensions = self._get_value(Dimensions, "dimensions")
        else:
            self.dimensions: Dimensions = None
        if "items" in data:
            self.items: _List[ContainerItem] = [ContainerItem(datum) for datum in data["items"]]
        else:
            self.items: _List[ContainerItem] = []
        if "weight" in data:
            self.weight: Weight = self._get_value(Weight, "weight")
        else:
            self.weight: Weight = None


class ContainerSpecification(__BaseDictObject):
    """
    Container specification for checking the service rate.
    """

    def __init__(self, data):
        super().__init__(data)
        if "dimensions" in data:
            self.dimensions: Dimensions = self._get_value(Dimensions, "dimensions")
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = self._get_value(Weight, "weight")
        else:
            self.weight: Weight = None


class Label(__BaseDictObject):
    """
    The label details of the container.
    """

    def __init__(self, data):
        super().__init__(data)
        if "labelStream" in data:
            self.labelStream: LabelStream = self._get_value(LabelStream, "labelStream")
        else:
            self.labelStream: LabelStream = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = self._get_value(LabelSpecification, "labelSpecification")
        else:
            self.labelSpecification: LabelSpecification = None


class LabelResult(__BaseDictObject):
    """
    Label details including label stream, format, size.
    """

    def __init__(self, data):
        super().__init__(data)
        if "containerReferenceId" in data:
            self.containerReferenceId: ContainerReferenceId = self._get_value(
                ContainerReferenceId, "containerReferenceId"
            )
        else:
            self.containerReferenceId: ContainerReferenceId = None
        if "trackingId" in data:
            self.trackingId: str = self._get_value(str, "trackingId")
        else:
            self.trackingId: str = None
        if "label" in data:
            self.label: Label = self._get_value(Label, "label")
        else:
            self.label: Label = None


class LabelSpecification(__BaseDictObject):
    """
    The label specification info.
    """

    def __init__(self, data):
        super().__init__(data)
        if "labelFormat" in data:
            self.labelFormat: str = self._get_value(str, "labelFormat")
        else:
            self.labelFormat: str = None
        if "labelStockSize" in data:
            self.labelStockSize: str = self._get_value(str, "labelStockSize")
        else:
            self.labelStockSize: str = None


class CreateShipmentRequest(__BaseDictObject):
    """
    The request schema for the createShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = self._get_value(ClientReferenceId, "clientReferenceId")
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "shipTo" in data:
            self.shipTo: Address = self._get_value(Address, "shipTo")
        else:
            self.shipTo: Address = None
        if "shipFrom" in data:
            self.shipFrom: Address = self._get_value(Address, "shipFrom")
        else:
            self.shipFrom: Address = None
        if "containers" in data:
            self.containers: ContainerList = self._get_value(ContainerList, "containers")
        else:
            self.containers: ContainerList = None


class PurchaseLabelsRequest(__BaseDictObject):
    """
    The request schema for the purchaseLabels operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "rateId" in data:
            self.rateId: RateId = self._get_value(RateId, "rateId")
        else:
            self.rateId: RateId = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = self._get_value(LabelSpecification, "labelSpecification")
        else:
            self.labelSpecification: LabelSpecification = None


class RetrieveShippingLabelRequest(__BaseDictObject):
    """
    The request schema for the retrieveShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = self._get_value(LabelSpecification, "labelSpecification")
        else:
            self.labelSpecification: LabelSpecification = None


class GetRatesRequest(__BaseDictObject):
    """
    The payload schema for the getRates operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipTo" in data:
            self.shipTo: Address = self._get_value(Address, "shipTo")
        else:
            self.shipTo: Address = None
        if "shipFrom" in data:
            self.shipFrom: Address = self._get_value(Address, "shipFrom")
        else:
            self.shipFrom: Address = None
        if "serviceTypes" in data:
            self.serviceTypes: ServiceTypeList = self._get_value(ServiceTypeList, "serviceTypes")
        else:
            self.serviceTypes: ServiceTypeList = None
        if "shipDate" in data:
            self.shipDate: str = self._get_value(str, "shipDate")
        else:
            self.shipDate: str = None
        if "containerSpecifications" in data:
            self.containerSpecifications: ContainerSpecificationList = self._get_value(
                ContainerSpecificationList, "containerSpecifications"
            )
        else:
            self.containerSpecifications: ContainerSpecificationList = None


class PurchaseShipmentRequest(__BaseDictObject):
    """
    The payload schema for the purchaseShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = self._get_value(ClientReferenceId, "clientReferenceId")
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "shipTo" in data:
            self.shipTo: Address = self._get_value(Address, "shipTo")
        else:
            self.shipTo: Address = None
        if "shipFrom" in data:
            self.shipFrom: Address = self._get_value(Address, "shipFrom")
        else:
            self.shipFrom: Address = None
        if "shipDate" in data:
            self.shipDate: str = self._get_value(str, "shipDate")
        else:
            self.shipDate: str = None
        if "serviceType" in data:
            self.serviceType: ServiceType = self._get_value(ServiceType, "serviceType")
        else:
            self.serviceType: ServiceType = None
        if "containers" in data:
            self.containers: ContainerList = self._get_value(ContainerList, "containers")
        else:
            self.containers: ContainerList = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = self._get_value(LabelSpecification, "labelSpecification")
        else:
            self.labelSpecification: LabelSpecification = None


class CreateShipmentResult(__BaseDictObject):
    """
    The payload schema for the createShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = self._get_value(ShipmentId, "shipmentId")
        else:
            self.shipmentId: ShipmentId = None
        if "eligibleRates" in data:
            self.eligibleRates: RateList = self._get_value(RateList, "eligibleRates")
        else:
            self.eligibleRates: RateList = None


class Shipment(__BaseDictObject):
    """
    The shipment related data.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = self._get_value(ShipmentId, "shipmentId")
        else:
            self.shipmentId: ShipmentId = None
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = self._get_value(ClientReferenceId, "clientReferenceId")
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "shipFrom" in data:
            self.shipFrom: Address = self._get_value(Address, "shipFrom")
        else:
            self.shipFrom: Address = None
        if "shipTo" in data:
            self.shipTo: Address = self._get_value(Address, "shipTo")
        else:
            self.shipTo: Address = None
        if "acceptedRate" in data:
            self.acceptedRate: AcceptedRate = self._get_value(AcceptedRate, "acceptedRate")
        else:
            self.acceptedRate: AcceptedRate = None
        if "shipper" in data:
            self.shipper: Party = self._get_value(Party, "shipper")
        else:
            self.shipper: Party = None
        if "containers" in data:
            self.containers: ContainerList = self._get_value(ContainerList, "containers")
        else:
            self.containers: ContainerList = None


class PurchaseLabelsResult(__BaseDictObject):
    """
    The payload schema for the purchaseLabels operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = self._get_value(ShipmentId, "shipmentId")
        else:
            self.shipmentId: ShipmentId = None
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = self._get_value(ClientReferenceId, "clientReferenceId")
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "acceptedRate" in data:
            self.acceptedRate: AcceptedRate = self._get_value(AcceptedRate, "acceptedRate")
        else:
            self.acceptedRate: AcceptedRate = None
        if "labelResults" in data:
            self.labelResults: LabelResultList = self._get_value(LabelResultList, "labelResults")
        else:
            self.labelResults: LabelResultList = None


class RetrieveShippingLabelResult(__BaseDictObject):
    """
    The payload schema for the retrieveShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "labelStream" in data:
            self.labelStream: LabelStream = self._get_value(LabelStream, "labelStream")
        else:
            self.labelStream: LabelStream = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = self._get_value(LabelSpecification, "labelSpecification")
        else:
            self.labelSpecification: LabelSpecification = None


class Account(__BaseDictObject):
    """
    The account related data.
    """

    def __init__(self, data):
        super().__init__(data)
        if "accountId" in data:
            self.accountId: AccountId = self._get_value(AccountId, "accountId")
        else:
            self.accountId: AccountId = None


class GetRatesResult(__BaseDictObject):
    """
    The payload schema for the getRates operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "serviceRates" in data:
            self.serviceRates: ServiceRateList = self._get_value(ServiceRateList, "serviceRates")
        else:
            self.serviceRates: ServiceRateList = None


class PurchaseShipmentResult(__BaseDictObject):
    """
    The payload schema for the purchaseShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = self._get_value(ShipmentId, "shipmentId")
        else:
            self.shipmentId: ShipmentId = None
        if "serviceRate" in data:
            self.serviceRate: ServiceRate = self._get_value(ServiceRate, "serviceRate")
        else:
            self.serviceRate: ServiceRate = None
        if "labelResults" in data:
            self.labelResults: LabelResultList = self._get_value(LabelResultList, "labelResults")
        else:
            self.labelResults: LabelResultList = None


class TrackingInformation(__BaseDictObject):
    """
    The payload schema for the getTrackingInformation operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "trackingId" in data:
            self.trackingId: TrackingId = self._get_value(TrackingId, "trackingId")
        else:
            self.trackingId: TrackingId = None
        if "summary" in data:
            self.summary: TrackingSummary = self._get_value(TrackingSummary, "summary")
        else:
            self.summary: TrackingSummary = None
        if "promisedDeliveryDate" in data:
            self.promisedDeliveryDate: PromisedDeliveryDate = self._get_value(
                PromisedDeliveryDate, "promisedDeliveryDate"
            )
        else:
            self.promisedDeliveryDate: PromisedDeliveryDate = None
        if "eventHistory" in data:
            self.eventHistory: EventList = self._get_value(EventList, "eventHistory")
        else:
            self.eventHistory: EventList = None


class CreateShipmentResponse(__BaseDictObject):
    """
    The response schema for the createShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CreateShipmentResult = self._get_value(CreateShipmentResult, "payload")
        else:
            self.payload: CreateShipmentResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetShipmentResponse(__BaseDictObject):
    """
    The response schema for the getShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Shipment = self._get_value(Shipment, "payload")
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetRatesResponse(__BaseDictObject):
    """
    The response schema for the getRates operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetRatesResult = self._get_value(GetRatesResult, "payload")
        else:
            self.payload: GetRatesResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class PurchaseShipmentResponse(__BaseDictObject):
    """
    The response schema for the purchaseShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: PurchaseShipmentResult = self._get_value(PurchaseShipmentResult, "payload")
        else:
            self.payload: PurchaseShipmentResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CancelShipmentResponse(__BaseDictObject):
    """
    The response schema for the cancelShipment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class PurchaseLabelsResponse(__BaseDictObject):
    """
    The response schema for the purchaseLabels operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: PurchaseLabelsResult = self._get_value(PurchaseLabelsResult, "payload")
        else:
            self.payload: PurchaseLabelsResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class RetrieveShippingLabelResponse(__BaseDictObject):
    """
    The response schema for the retrieveShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: RetrieveShippingLabelResult = self._get_value(RetrieveShippingLabelResult, "payload")
        else:
            self.payload: RetrieveShippingLabelResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetAccountResponse(__BaseDictObject):
    """
    The response schema for the getAccount operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Account = self._get_value(Account, "payload")
        else:
            self.payload: Account = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetTrackingInformationResponse(__BaseDictObject):
    """
    The response schema for the getTrackingInformation operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: TrackingInformation = self._get_value(TrackingInformation, "payload")
        else:
            self.payload: TrackingInformation = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class EventList(list, _List["Event"]):
    """
    A list of events of a shipment.
    """

    def __init__(self, data):
        super().__init__([Event(datum) for datum in data])
        self.data = data


class ServiceTypeList(list, _List["ServiceType"]):
    """
    A list of service types that can be used to send the shipment.
    """

    def __init__(self, data):
        super().__init__([ServiceType(datum) for datum in data])
        self.data = data


class RateList(list, _List["Rate"]):
    """
    A list of all the available rates that can be used to send the shipment.
    """

    def __init__(self, data):
        super().__init__([Rate(datum) for datum in data])
        self.data = data


class ServiceRateList(list, _List["ServiceRate"]):
    """
    A list of service rates.
    """

    def __init__(self, data):
        super().__init__([ServiceRate(datum) for datum in data])
        self.data = data


class ContainerList(list, _List["Container"]):
    """
    A list of container.
    """

    def __init__(self, data):
        super().__init__([Container(datum) for datum in data])
        self.data = data


class ContainerSpecificationList(list, _List["ContainerSpecification"]):
    """
    A list of container specifications.
    """

    def __init__(self, data):
        super().__init__([ContainerSpecification(datum) for datum in data])
        self.data = data


class LabelResultList(list, _List["LabelResult"]):
    """
    A list of label results
    """

    def __init__(self, data):
        super().__init__([LabelResult(datum) for datum in data])
        self.data = data


class AccountId(str):
    """
    This is the Amazon Shipping account id generated during the Amazon Shipping onboarding process.
    """


class ShipmentId(str):
    """
    The unique shipment identifier.
    """


class ClientReferenceId(str):
    """
    Client reference id.
    """


class ContainerReferenceId(str):
    """
    An identifier for the container. This must be unique within all the containers in the same shipment.
    """


class EventCode(str):
    """
    The event code of a shipment, such as Departed, Received, and ReadyForReceive.
    """


class StateOrRegion(str):
    """
    The state or region where the person, business or institution is located.
    """


class City(str):
    """
    The city where the person, business or institution is located.
    """


class CountryCode(str):
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """


class PostalCode(str):
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """


class TrackingId(str):
    """
    The tracking id generated to each shipment. It contains a series of letters or digits or both.
    """


class PromisedDeliveryDate(str):
    """
    The promised delivery date and time of a shipment.
    """


class ServiceType(str):
    """
    The type of shipping service that will be used for the service offering.
    """


class RateId(str):
    """
    An identifier for the rating.
    """


class LabelStream(str):
    """
    Contains binary image data encoded as a base-64 string.
    """


class ShippingV1Client(__BaseClient):
    def createShipment(
        self,
        data: CreateShipmentRequest,
    ):
        """
                Create a new shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/shipping/v1/shipments"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateShipmentResponse,
            400: CreateShipmentResponse,
            401: CreateShipmentResponse,
            403: CreateShipmentResponse,
            404: CreateShipmentResponse,
            429: CreateShipmentResponse,
            500: CreateShipmentResponse,
            503: CreateShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getShipment(
        self,
        shipmentId: str,
    ):
        """
                Return the entire shipment object for the shipmentId.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/shipments/{shipmentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetShipmentResponse,
            400: GetShipmentResponse,
            401: GetShipmentResponse,
            403: GetShipmentResponse,
            404: GetShipmentResponse,
            429: GetShipmentResponse,
            500: GetShipmentResponse,
            503: GetShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelShipment(
        self,
        shipmentId: str,
    ):
        """
                Cancel a shipment by the given shipmentId.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/shipments/{shipmentId}/cancel"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
        )
        response_type = {
            200: CancelShipmentResponse,
            400: CancelShipmentResponse,
            401: CancelShipmentResponse,
            403: CancelShipmentResponse,
            404: CancelShipmentResponse,
            429: CancelShipmentResponse,
            500: CancelShipmentResponse,
            503: CancelShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def purchaseLabels(
        self,
        data: PurchaseLabelsRequest,
        shipmentId: str,
    ):
        """
                Purchase shipping labels based on a given rate.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/shipments/{shipmentId}/purchaseLabels"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: PurchaseLabelsResponse,
            400: PurchaseLabelsResponse,
            401: PurchaseLabelsResponse,
            403: PurchaseLabelsResponse,
            404: PurchaseLabelsResponse,
            429: PurchaseLabelsResponse,
            500: PurchaseLabelsResponse,
            503: PurchaseLabelsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def retrieveShippingLabel(
        self,
        data: RetrieveShippingLabelRequest,
        shipmentId: str,
        trackingId: str,
    ):
        """
                Retrieve shipping label based on the shipment id and tracking id.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: RetrieveShippingLabelResponse,
            400: RetrieveShippingLabelResponse,
            401: RetrieveShippingLabelResponse,
            403: RetrieveShippingLabelResponse,
            404: RetrieveShippingLabelResponse,
            429: RetrieveShippingLabelResponse,
            500: RetrieveShippingLabelResponse,
            503: RetrieveShippingLabelResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def purchaseShipment(
        self,
        data: PurchaseShipmentRequest,
    ):
        """
                Purchase shipping labels.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/purchaseShipment"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: PurchaseShipmentResponse,
            400: PurchaseShipmentResponse,
            401: PurchaseShipmentResponse,
            403: PurchaseShipmentResponse,
            404: PurchaseShipmentResponse,
            429: PurchaseShipmentResponse,
            500: PurchaseShipmentResponse,
            503: PurchaseShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getRates(
        self,
        data: GetRatesRequest,
    ):
        """
                Get service rates.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/rates"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetRatesResponse,
            400: GetRatesResponse,
            401: GetRatesResponse,
            403: GetRatesResponse,
            404: GetRatesResponse,
            429: GetRatesResponse,
            500: GetRatesResponse,
            503: GetRatesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getAccount(
        self,
    ):
        """
                Verify if the current account is valid.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/account"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetAccountResponse,
            400: GetAccountResponse,
            401: GetAccountResponse,
            403: GetAccountResponse,
            404: GetAccountResponse,
            429: GetAccountResponse,
            500: GetAccountResponse,
            503: GetAccountResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getTrackingInformation(
        self,
        trackingId: str,
    ):
        """
                Return the tracking information of a shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/shipping/v1/tracking/{trackingId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetTrackingInformationResponse,
            400: GetTrackingInformationResponse,
            401: GetTrackingInformationResponse,
            403: GetTrackingInformationResponse,
            404: GetTrackingInformationResponse,
            429: GetTrackingInformationResponse,
            500: GetTrackingInformationResponse,
            503: GetTrackingInformationResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
