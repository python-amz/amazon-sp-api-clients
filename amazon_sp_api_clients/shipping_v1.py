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


class Location:
    """
    The location where the person, business or institution is located.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "stateOrRegion" in data:
            self.stateOrRegion: StateOrRegion = StateOrRegion(data["stateOrRegion"])
        else:
            self.stateOrRegion: StateOrRegion = None
        if "city" in data:
            self.city: City = City(data["city"])
        else:
            self.city: City = None
        if "countryCode" in data:
            self.countryCode: CountryCode = CountryCode(data["countryCode"])
        else:
            self.countryCode: CountryCode = None
        if "postalCode" in data:
            self.postalCode: PostalCode = PostalCode(data["postalCode"])
        else:
            self.postalCode: PostalCode = None


class Event:
    """
    An event of a shipment
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "eventCode" in data:
            self.eventCode: EventCode = EventCode(data["eventCode"])
        else:
            self.eventCode: EventCode = None
        if "eventTime" in data:
            self.eventTime: str = str(data["eventTime"])
        else:
            self.eventTime: str = None
        if "location" in data:
            self.location: Location = Location(data["location"])
        else:
            self.location: Location = None


class TrackingSummary:
    """
    The tracking summary.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "status" in data:
            self.status: str = str(data["status"])
        else:
            self.status: str = None


class Address:
    """
    The address.
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
        if "stateOrRegion" in data:
            self.stateOrRegion: StateOrRegion = StateOrRegion(data["stateOrRegion"])
        else:
            self.stateOrRegion: StateOrRegion = None
        if "city" in data:
            self.city: City = City(data["city"])
        else:
            self.city: City = None
        if "countryCode" in data:
            self.countryCode: CountryCode = CountryCode(data["countryCode"])
        else:
            self.countryCode: CountryCode = None
        if "postalCode" in data:
            self.postalCode: PostalCode = PostalCode(data["postalCode"])
        else:
            self.postalCode: PostalCode = None
        if "email" in data:
            self.email: str = str(data["email"])
        else:
            self.email: str = None
        if "copyEmails" in data:
            self.copyEmails: _List[str] = [str(datum) for datum in data["copyEmails"]]
        else:
            self.copyEmails: _List[str] = []
        if "phoneNumber" in data:
            self.phoneNumber: str = str(data["phoneNumber"])
        else:
            self.phoneNumber: str = None


class TimeRange:
    """
    The time range.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "start" in data:
            self.start: str = str(data["start"])
        else:
            self.start: str = None
        if "end" in data:
            self.end: str = str(data["end"])
        else:
            self.end: str = None


class ShippingPromiseSet:
    """
    The promised delivery time and pickup time.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "deliveryWindow" in data:
            self.deliveryWindow: TimeRange = TimeRange(data["deliveryWindow"])
        else:
            self.deliveryWindow: TimeRange = None
        if "receiveWindow" in data:
            self.receiveWindow: TimeRange = TimeRange(data["receiveWindow"])
        else:
            self.receiveWindow: TimeRange = None


class Rate:
    """
    The available rate that can be used to send the shipment
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "rateId" in data:
            self.rateId: str = str(data["rateId"])
        else:
            self.rateId: str = None
        if "totalCharge" in data:
            self.totalCharge: Currency = Currency(data["totalCharge"])
        else:
            self.totalCharge: Currency = None
        if "billedWeight" in data:
            self.billedWeight: Weight = Weight(data["billedWeight"])
        else:
            self.billedWeight: Weight = None
        if "expirationTime" in data:
            self.expirationTime: str = str(data["expirationTime"])
        else:
            self.expirationTime: str = None
        if "serviceType" in data:
            self.serviceType: ServiceType = ServiceType(data["serviceType"])
        else:
            self.serviceType: ServiceType = None
        if "promise" in data:
            self.promise: ShippingPromiseSet = ShippingPromiseSet(data["promise"])
        else:
            self.promise: ShippingPromiseSet = None


class AcceptedRate:
    """
    The specific rate purchased for the shipment, or null if unpurchased.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "totalCharge" in data:
            self.totalCharge: Currency = Currency(data["totalCharge"])
        else:
            self.totalCharge: Currency = None
        if "billedWeight" in data:
            self.billedWeight: Weight = Weight(data["billedWeight"])
        else:
            self.billedWeight: Weight = None
        if "serviceType" in data:
            self.serviceType: ServiceType = ServiceType(data["serviceType"])
        else:
            self.serviceType: ServiceType = None
        if "promise" in data:
            self.promise: ShippingPromiseSet = ShippingPromiseSet(data["promise"])
        else:
            self.promise: ShippingPromiseSet = None


class ServiceRate:
    """
    The specific rate for a shipping service, or null if no service available.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "totalCharge" in data:
            self.totalCharge: Currency = Currency(data["totalCharge"])
        else:
            self.totalCharge: Currency = None
        if "billableWeight" in data:
            self.billableWeight: Weight = Weight(data["billableWeight"])
        else:
            self.billableWeight: Weight = None
        if "serviceType" in data:
            self.serviceType: ServiceType = ServiceType(data["serviceType"])
        else:
            self.serviceType: ServiceType = None
        if "promise" in data:
            self.promise: ShippingPromiseSet = ShippingPromiseSet(data["promise"])
        else:
            self.promise: ShippingPromiseSet = None


class Party:
    """
    The account related with the shipment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "accountId" in data:
            self.accountId: AccountId = AccountId(data["accountId"])
        else:
            self.accountId: AccountId = None


class Currency:
    """
    The total value of all items in the container.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "value" in data:
            self.value: float = float(data["value"])
        else:
            self.value: float = None
        if "unit" in data:
            self.unit: str = str(data["unit"])
        else:
            self.unit: str = None


class Dimensions:
    """
    A set of measurements for a three-dimensional object.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "length" in data:
            self.length: float = float(data["length"])
        else:
            self.length: float = None
        if "width" in data:
            self.width: float = float(data["width"])
        else:
            self.width: float = None
        if "height" in data:
            self.height: float = float(data["height"])
        else:
            self.height: float = None
        if "unit" in data:
            self.unit: str = str(data["unit"])
        else:
            self.unit: str = None


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
            self.value: float = float(data["value"])
        else:
            self.value: float = None


class ContainerItem:
    """
    Item in the container.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "quantity" in data:
            self.quantity: float = float(data["quantity"])
        else:
            self.quantity: float = None
        if "unitPrice" in data:
            self.unitPrice: Currency = Currency(data["unitPrice"])
        else:
            self.unitPrice: Currency = None
        if "unitWeight" in data:
            self.unitWeight: Weight = Weight(data["unitWeight"])
        else:
            self.unitWeight: Weight = None
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None


class Container:
    """
    Container in the shipment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "containerType" in data:
            self.containerType: str = str(data["containerType"])
        else:
            self.containerType: str = None
        if "containerReferenceId" in data:
            self.containerReferenceId: ContainerReferenceId = ContainerReferenceId(data["containerReferenceId"])
        else:
            self.containerReferenceId: ContainerReferenceId = None
        if "value" in data:
            self.value: Currency = Currency(data["value"])
        else:
            self.value: Currency = None
        if "dimensions" in data:
            self.dimensions: Dimensions = Dimensions(data["dimensions"])
        else:
            self.dimensions: Dimensions = None
        if "items" in data:
            self.items: _List[ContainerItem] = [ContainerItem(datum) for datum in data["items"]]
        else:
            self.items: _List[ContainerItem] = []
        if "weight" in data:
            self.weight: Weight = Weight(data["weight"])
        else:
            self.weight: Weight = None


class ContainerSpecification:
    """
    Container specification for checking the service rate.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "dimensions" in data:
            self.dimensions: Dimensions = Dimensions(data["dimensions"])
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = Weight(data["weight"])
        else:
            self.weight: Weight = None


class Label:
    """
    The label details of the container.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "labelStream" in data:
            self.labelStream: LabelStream = LabelStream(data["labelStream"])
        else:
            self.labelStream: LabelStream = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = LabelSpecification(data["labelSpecification"])
        else:
            self.labelSpecification: LabelSpecification = None


class LabelResult:
    """
    Label details including label stream, format, size.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "containerReferenceId" in data:
            self.containerReferenceId: ContainerReferenceId = ContainerReferenceId(data["containerReferenceId"])
        else:
            self.containerReferenceId: ContainerReferenceId = None
        if "trackingId" in data:
            self.trackingId: str = str(data["trackingId"])
        else:
            self.trackingId: str = None
        if "label" in data:
            self.label: Label = Label(data["label"])
        else:
            self.label: Label = None


class LabelSpecification:
    """
    The label specification info.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "labelFormat" in data:
            self.labelFormat: str = str(data["labelFormat"])
        else:
            self.labelFormat: str = None
        if "labelStockSize" in data:
            self.labelStockSize: str = str(data["labelStockSize"])
        else:
            self.labelStockSize: str = None


class CreateShipmentRequest:
    """
    The request schema for the createShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = ClientReferenceId(data["clientReferenceId"])
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "shipTo" in data:
            self.shipTo: Address = Address(data["shipTo"])
        else:
            self.shipTo: Address = None
        if "shipFrom" in data:
            self.shipFrom: Address = Address(data["shipFrom"])
        else:
            self.shipFrom: Address = None
        if "containers" in data:
            self.containers: ContainerList = ContainerList(data["containers"])
        else:
            self.containers: ContainerList = None


class PurchaseLabelsRequest:
    """
    The request schema for the purchaseLabels operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "rateId" in data:
            self.rateId: RateId = RateId(data["rateId"])
        else:
            self.rateId: RateId = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = LabelSpecification(data["labelSpecification"])
        else:
            self.labelSpecification: LabelSpecification = None


class RetrieveShippingLabelRequest:
    """
    The request schema for the retrieveShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = LabelSpecification(data["labelSpecification"])
        else:
            self.labelSpecification: LabelSpecification = None


class GetRatesRequest:
    """
    The payload schema for the getRates operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipTo" in data:
            self.shipTo: Address = Address(data["shipTo"])
        else:
            self.shipTo: Address = None
        if "shipFrom" in data:
            self.shipFrom: Address = Address(data["shipFrom"])
        else:
            self.shipFrom: Address = None
        if "serviceTypes" in data:
            self.serviceTypes: ServiceTypeList = ServiceTypeList(data["serviceTypes"])
        else:
            self.serviceTypes: ServiceTypeList = None
        if "shipDate" in data:
            self.shipDate: str = str(data["shipDate"])
        else:
            self.shipDate: str = None
        if "containerSpecifications" in data:
            self.containerSpecifications: ContainerSpecificationList = ContainerSpecificationList(
                data["containerSpecifications"]
            )
        else:
            self.containerSpecifications: ContainerSpecificationList = None


class PurchaseShipmentRequest:
    """
    The payload schema for the purchaseShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = ClientReferenceId(data["clientReferenceId"])
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "shipTo" in data:
            self.shipTo: Address = Address(data["shipTo"])
        else:
            self.shipTo: Address = None
        if "shipFrom" in data:
            self.shipFrom: Address = Address(data["shipFrom"])
        else:
            self.shipFrom: Address = None
        if "shipDate" in data:
            self.shipDate: str = str(data["shipDate"])
        else:
            self.shipDate: str = None
        if "serviceType" in data:
            self.serviceType: ServiceType = ServiceType(data["serviceType"])
        else:
            self.serviceType: ServiceType = None
        if "containers" in data:
            self.containers: ContainerList = ContainerList(data["containers"])
        else:
            self.containers: ContainerList = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = LabelSpecification(data["labelSpecification"])
        else:
            self.labelSpecification: LabelSpecification = None


class CreateShipmentResult:
    """
    The payload schema for the createShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = ShipmentId(data["shipmentId"])
        else:
            self.shipmentId: ShipmentId = None
        if "eligibleRates" in data:
            self.eligibleRates: RateList = RateList(data["eligibleRates"])
        else:
            self.eligibleRates: RateList = None


class Shipment:
    """
    The shipment related data.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = ShipmentId(data["shipmentId"])
        else:
            self.shipmentId: ShipmentId = None
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = ClientReferenceId(data["clientReferenceId"])
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "shipFrom" in data:
            self.shipFrom: Address = Address(data["shipFrom"])
        else:
            self.shipFrom: Address = None
        if "shipTo" in data:
            self.shipTo: Address = Address(data["shipTo"])
        else:
            self.shipTo: Address = None
        if "acceptedRate" in data:
            self.acceptedRate: AcceptedRate = AcceptedRate(data["acceptedRate"])
        else:
            self.acceptedRate: AcceptedRate = None
        if "shipper" in data:
            self.shipper: Party = Party(data["shipper"])
        else:
            self.shipper: Party = None
        if "containers" in data:
            self.containers: ContainerList = ContainerList(data["containers"])
        else:
            self.containers: ContainerList = None


class PurchaseLabelsResult:
    """
    The payload schema for the purchaseLabels operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = ShipmentId(data["shipmentId"])
        else:
            self.shipmentId: ShipmentId = None
        if "clientReferenceId" in data:
            self.clientReferenceId: ClientReferenceId = ClientReferenceId(data["clientReferenceId"])
        else:
            self.clientReferenceId: ClientReferenceId = None
        if "acceptedRate" in data:
            self.acceptedRate: AcceptedRate = AcceptedRate(data["acceptedRate"])
        else:
            self.acceptedRate: AcceptedRate = None
        if "labelResults" in data:
            self.labelResults: LabelResultList = LabelResultList(data["labelResults"])
        else:
            self.labelResults: LabelResultList = None


class RetrieveShippingLabelResult:
    """
    The payload schema for the retrieveShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "labelStream" in data:
            self.labelStream: LabelStream = LabelStream(data["labelStream"])
        else:
            self.labelStream: LabelStream = None
        if "labelSpecification" in data:
            self.labelSpecification: LabelSpecification = LabelSpecification(data["labelSpecification"])
        else:
            self.labelSpecification: LabelSpecification = None


class Account:
    """
    The account related data.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "accountId" in data:
            self.accountId: AccountId = AccountId(data["accountId"])
        else:
            self.accountId: AccountId = None


class GetRatesResult:
    """
    The payload schema for the getRates operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "serviceRates" in data:
            self.serviceRates: ServiceRateList = ServiceRateList(data["serviceRates"])
        else:
            self.serviceRates: ServiceRateList = None


class PurchaseShipmentResult:
    """
    The payload schema for the purchaseShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "shipmentId" in data:
            self.shipmentId: ShipmentId = ShipmentId(data["shipmentId"])
        else:
            self.shipmentId: ShipmentId = None
        if "serviceRate" in data:
            self.serviceRate: ServiceRate = ServiceRate(data["serviceRate"])
        else:
            self.serviceRate: ServiceRate = None
        if "labelResults" in data:
            self.labelResults: LabelResultList = LabelResultList(data["labelResults"])
        else:
            self.labelResults: LabelResultList = None


class TrackingInformation:
    """
    The payload schema for the getTrackingInformation operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "trackingId" in data:
            self.trackingId: TrackingId = TrackingId(data["trackingId"])
        else:
            self.trackingId: TrackingId = None
        if "summary" in data:
            self.summary: TrackingSummary = TrackingSummary(data["summary"])
        else:
            self.summary: TrackingSummary = None
        if "promisedDeliveryDate" in data:
            self.promisedDeliveryDate: PromisedDeliveryDate = PromisedDeliveryDate(data["promisedDeliveryDate"])
        else:
            self.promisedDeliveryDate: PromisedDeliveryDate = None
        if "eventHistory" in data:
            self.eventHistory: EventList = EventList(data["eventHistory"])
        else:
            self.eventHistory: EventList = None


class CreateShipmentResponse:
    """
    The response schema for the createShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateShipmentResult = CreateShipmentResult(data["payload"])
        else:
            self.payload: CreateShipmentResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetShipmentResponse:
    """
    The response schema for the getShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Shipment = Shipment(data["payload"])
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetRatesResponse:
    """
    The response schema for the getRates operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetRatesResult = GetRatesResult(data["payload"])
        else:
            self.payload: GetRatesResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class PurchaseShipmentResponse:
    """
    The response schema for the purchaseShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: PurchaseShipmentResult = PurchaseShipmentResult(data["payload"])
        else:
            self.payload: PurchaseShipmentResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CancelShipmentResponse:
    """
    The response schema for the cancelShipment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class PurchaseLabelsResponse:
    """
    The response schema for the purchaseLabels operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: PurchaseLabelsResult = PurchaseLabelsResult(data["payload"])
        else:
            self.payload: PurchaseLabelsResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class RetrieveShippingLabelResponse:
    """
    The response schema for the retrieveShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: RetrieveShippingLabelResult = RetrieveShippingLabelResult(data["payload"])
        else:
            self.payload: RetrieveShippingLabelResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetAccountResponse:
    """
    The response schema for the getAccount operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Account = Account(data["payload"])
        else:
            self.payload: Account = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetTrackingInformationResponse:
    """
    The response schema for the getTrackingInformation operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: TrackingInformation = TrackingInformation(data["payload"])
        else:
            self.payload: TrackingInformation = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
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
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/shipping/v1/shipments".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: CreateShipmentResponse,
            400: CreateShipmentResponse,
            401: CreateShipmentResponse,
            403: CreateShipmentResponse,
            404: CreateShipmentResponse,
            429: CreateShipmentResponse,
            500: CreateShipmentResponse,
            503: CreateShipmentResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShipmentResponse,
            400: GetShipmentResponse,
            401: GetShipmentResponse,
            403: GetShipmentResponse,
            404: GetShipmentResponse,
            429: GetShipmentResponse,
            500: GetShipmentResponse,
            503: GetShipmentResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/shipments/{shipmentId}/cancel".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: CancelShipmentResponse,
            400: CancelShipmentResponse,
            401: CancelShipmentResponse,
            403: CancelShipmentResponse,
            404: CancelShipmentResponse,
            429: CancelShipmentResponse,
            500: CancelShipmentResponse,
            503: CancelShipmentResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/shipments/{shipmentId}/purchaseLabels".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: PurchaseLabelsResponse,
            400: PurchaseLabelsResponse,
            401: PurchaseLabelsResponse,
            403: PurchaseLabelsResponse,
            404: PurchaseLabelsResponse,
            429: PurchaseLabelsResponse,
            500: PurchaseLabelsResponse,
            503: PurchaseLabelsResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label".format(
            shipmentId=shipmentId,
            trackingId=trackingId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: RetrieveShippingLabelResponse,
            400: RetrieveShippingLabelResponse,
            401: RetrieveShippingLabelResponse,
            403: RetrieveShippingLabelResponse,
            404: RetrieveShippingLabelResponse,
            429: RetrieveShippingLabelResponse,
            500: RetrieveShippingLabelResponse,
            503: RetrieveShippingLabelResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/purchaseShipment".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: PurchaseShipmentResponse,
            400: PurchaseShipmentResponse,
            401: PurchaseShipmentResponse,
            403: PurchaseShipmentResponse,
            404: PurchaseShipmentResponse,
            429: PurchaseShipmentResponse,
            500: PurchaseShipmentResponse,
            503: PurchaseShipmentResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/rates".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: GetRatesResponse,
            400: GetRatesResponse,
            401: GetRatesResponse,
            403: GetRatesResponse,
            404: GetRatesResponse,
            429: GetRatesResponse,
            500: GetRatesResponse,
            503: GetRatesResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/account".format()
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetAccountResponse,
            400: GetAccountResponse,
            401: GetAccountResponse,
            403: GetAccountResponse,
            404: GetAccountResponse,
            429: GetAccountResponse,
            500: GetAccountResponse,
            503: GetAccountResponse,
        }[response.status_code](self._get_response_json(response))

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
        url = "/shipping/v1/tracking/{trackingId}".format(
            trackingId=trackingId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetTrackingInformationResponse,
            400: GetTrackingInformationResponse,
            401: GetTrackingInformationResponse,
            403: GetTrackingInformationResponse,
            404: GetTrackingInformationResponse,
            429: GetTrackingInformationResponse,
            500: GetTrackingInformationResponse,
            503: GetTrackingInformationResponse,
        }[response.status_code](self._get_response_json(response))
