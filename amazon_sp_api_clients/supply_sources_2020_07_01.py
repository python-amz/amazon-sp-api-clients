from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class Error(__BaseDictObject):
    """
    An error response returned when the request is unsuccessful.
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


class ErrorList(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class GetSupplySourcesResponse(__BaseDictObject):
    """
    The paginated list of supply sources.
    """

    def __init__(self, data):
        super().__init__(data)
        if "supplySources" in data:
            self.supplySources: SupplySourceList = self._get_value(SupplySourceList, "supplySources")
        else:
            self.supplySources: SupplySourceList = None
        if "nextPageToken" in data:
            self.nextPageToken: str = self._get_value(str, "nextPageToken")
        else:
            self.nextPageToken: str = None


class UpdateSupplySourceStatusRequest(__BaseDictObject):
    """
    A request to update the status of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "status" in data:
            self.status: SupplySourceStatus = self._get_value(SupplySourceStatus, "status")
        else:
            self.status: SupplySourceStatus = None


class CreateSupplySourceRequest(__BaseDictObject):
    """
    A request to create a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "supplySourceCode" in data:
            self.supplySourceCode: SupplySourceCode = self._get_value(SupplySourceCode, "supplySourceCode")
        else:
            self.supplySourceCode: SupplySourceCode = None
        if "alias" in data:
            self.alias: SupplySourceAlias = self._get_value(SupplySourceAlias, "alias")
        else:
            self.alias: SupplySourceAlias = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None


class CreateSupplySourceResponse(__BaseDictObject):
    """
    The result of creating a new supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "supplySourceId" in data:
            self.supplySourceId: SupplySourceId = self._get_value(SupplySourceId, "supplySourceId")
        else:
            self.supplySourceId: SupplySourceId = None
        if "supplySourceCode" in data:
            self.supplySourceCode: SupplySourceCode = self._get_value(SupplySourceCode, "supplySourceCode")
        else:
            self.supplySourceCode: SupplySourceCode = None


class UpdateSupplySourceRequest(__BaseDictObject):
    """
    A request to update the configuration and capabilities of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "alias" in data:
            self.alias: SupplySourceAlias = self._get_value(SupplySourceAlias, "alias")
        else:
            self.alias: SupplySourceAlias = None
        if "configuration" in data:
            self.configuration: SupplySourceConfiguration = self._get_value(SupplySourceConfiguration, "configuration")
        else:
            self.configuration: SupplySourceConfiguration = None
        if "capabilities" in data:
            self.capabilities: SupplySourceCapabilities = self._get_value(SupplySourceCapabilities, "capabilities")
        else:
            self.capabilities: SupplySourceCapabilities = None


class SupplySource(__BaseDictObject):
    """
    The supply source details, including configurations and capabilities.
    """

    def __init__(self, data):
        super().__init__(data)
        if "supplySourceId" in data:
            self.supplySourceId: SupplySourceId = self._get_value(SupplySourceId, "supplySourceId")
        else:
            self.supplySourceId: SupplySourceId = None
        if "supplySourceCode" in data:
            self.supplySourceCode: SupplySourceCode = self._get_value(SupplySourceCode, "supplySourceCode")
        else:
            self.supplySourceCode: SupplySourceCode = None
        if "alias" in data:
            self.alias: SupplySourceAlias = self._get_value(SupplySourceAlias, "alias")
        else:
            self.alias: SupplySourceAlias = None
        if "status" in data:
            self.status: SupplySourceStatusReadOnly = self._get_value(SupplySourceStatusReadOnly, "status")
        else:
            self.status: SupplySourceStatusReadOnly = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None
        if "configuration" in data:
            self.configuration: SupplySourceConfiguration = self._get_value(SupplySourceConfiguration, "configuration")
        else:
            self.configuration: SupplySourceConfiguration = None
        if "capabilities" in data:
            self.capabilities: SupplySourceCapabilities = self._get_value(SupplySourceCapabilities, "capabilities")
        else:
            self.capabilities: SupplySourceCapabilities = None
        if "createdAt" in data:
            self.createdAt: DateTime = self._get_value(DateTime, "createdAt")
        else:
            self.createdAt: DateTime = None
        if "updatedAt" in data:
            self.updatedAt: DateTime = self._get_value(DateTime, "updatedAt")
        else:
            self.updatedAt: DateTime = None


class SupplySourceConfiguration(__BaseDictObject):
    """
    Includes configuration and timezone of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "operationalConfiguration" in data:
            self.operationalConfiguration: OperationalConfiguration = self._get_value(
                OperationalConfiguration, "operationalConfiguration"
            )
        else:
            self.operationalConfiguration: OperationalConfiguration = None
        if "timezone" in data:
            self.timezone: str = self._get_value(str, "timezone")
        else:
            self.timezone: str = None


class SupplySourceCapabilities(__BaseDictObject):
    """
    The capabilities of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "outbound" in data:
            self.outbound: OutboundCapability = self._get_value(OutboundCapability, "outbound")
        else:
            self.outbound: OutboundCapability = None
        if "services" in data:
            self.services: ServicesCapability = self._get_value(ServicesCapability, "services")
        else:
            self.services: ServicesCapability = None


class OutboundCapability(__BaseDictObject):
    """
    The outbound capability of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isSupported" in data:
            self.isSupported: bool = self._get_value(convert_bool, "isSupported")
        else:
            self.isSupported: bool = None
        if "operationalConfiguration" in data:
            self.operationalConfiguration: OperationalConfiguration = self._get_value(
                OperationalConfiguration, "operationalConfiguration"
            )
        else:
            self.operationalConfiguration: OperationalConfiguration = None
        if "returnLocation" in data:
            self.returnLocation: ReturnLocation = self._get_value(ReturnLocation, "returnLocation")
        else:
            self.returnLocation: ReturnLocation = None
        if "deliveryChannel" in data:
            self.deliveryChannel: DeliveryChannel = self._get_value(DeliveryChannel, "deliveryChannel")
        else:
            self.deliveryChannel: DeliveryChannel = None
        if "pickupChannel" in data:
            self.pickupChannel: PickupChannel = self._get_value(PickupChannel, "pickupChannel")
        else:
            self.pickupChannel: PickupChannel = None


class ServicesCapability(__BaseDictObject):
    """
    The services capability of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isSupported" in data:
            self.isSupported: bool = self._get_value(convert_bool, "isSupported")
        else:
            self.isSupported: bool = None
        if "operationalConfiguration" in data:
            self.operationalConfiguration: OperationalConfiguration = self._get_value(
                OperationalConfiguration, "operationalConfiguration"
            )
        else:
            self.operationalConfiguration: OperationalConfiguration = None


class PickupChannel(__BaseDictObject):
    """
    The pick up channel of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "inventoryHoldPeriod" in data:
            self.inventoryHoldPeriod: Duration = self._get_value(Duration, "inventoryHoldPeriod")
        else:
            self.inventoryHoldPeriod: Duration = None
        if "isSupported" in data:
            self.isSupported: bool = self._get_value(convert_bool, "isSupported")
        else:
            self.isSupported: bool = None
        if "operationalConfiguration" in data:
            self.operationalConfiguration: OperationalConfiguration = self._get_value(
                OperationalConfiguration, "operationalConfiguration"
            )
        else:
            self.operationalConfiguration: OperationalConfiguration = None
        if "inStorePickupConfiguration" in data:
            self.inStorePickupConfiguration: InStorePickupConfiguration = self._get_value(
                InStorePickupConfiguration, "inStorePickupConfiguration"
            )
        else:
            self.inStorePickupConfiguration: InStorePickupConfiguration = None
        if "curbsidePickupConfiguration" in data:
            self.curbsidePickupConfiguration: CurbsidePickupConfiguration = self._get_value(
                CurbsidePickupConfiguration, "curbsidePickupConfiguration"
            )
        else:
            self.curbsidePickupConfiguration: CurbsidePickupConfiguration = None


class ParkingConfiguration(__BaseDictObject):
    """
    The parking configuration.
    """

    def __init__(self, data):
        super().__init__(data)
        if "parkingCostType" in data:
            self.parkingCostType: ParkingCostType = self._get_value(ParkingCostType, "parkingCostType")
        else:
            self.parkingCostType: ParkingCostType = None
        if "parkingSpotIdentificationType" in data:
            self.parkingSpotIdentificationType: ParkingSpotIdentificationType = self._get_value(
                ParkingSpotIdentificationType, "parkingSpotIdentificationType"
            )
        else:
            self.parkingSpotIdentificationType: ParkingSpotIdentificationType = None
        if "numberOfParkingSpots" in data:
            self.numberOfParkingSpots: NonNegativeInteger = self._get_value(NonNegativeInteger, "numberOfParkingSpots")
        else:
            self.numberOfParkingSpots: NonNegativeInteger = None


class InStorePickupConfiguration(__BaseDictObject):
    """
    The in-store pickup configuration of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isSupported" in data:
            self.isSupported: bool = self._get_value(convert_bool, "isSupported")
        else:
            self.isSupported: bool = None
        if "parkingConfiguration" in data:
            self.parkingConfiguration: ParkingConfiguration = self._get_value(
                ParkingConfiguration, "parkingConfiguration"
            )
        else:
            self.parkingConfiguration: ParkingConfiguration = None


class CurbsidePickupConfiguration(__BaseDictObject):
    """
    The curbside pickup configuration of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isSupported" in data:
            self.isSupported: bool = self._get_value(convert_bool, "isSupported")
        else:
            self.isSupported: bool = None
        if "operationalConfiguration" in data:
            self.operationalConfiguration: OperationalConfiguration = self._get_value(
                OperationalConfiguration, "operationalConfiguration"
            )
        else:
            self.operationalConfiguration: OperationalConfiguration = None
        if "parkingWithAddressConfiguration" in data:
            self.parkingWithAddressConfiguration: ParkingWithAddressConfiguration = self._get_value(
                ParkingWithAddressConfiguration, "parkingWithAddressConfiguration"
            )
        else:
            self.parkingWithAddressConfiguration: ParkingWithAddressConfiguration = None


class DeliveryChannel(__BaseDictObject):
    """
    The delivery channel of a supply source.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isSupported" in data:
            self.isSupported: bool = self._get_value(convert_bool, "isSupported")
        else:
            self.isSupported: bool = None
        if "operationalConfiguration" in data:
            self.operationalConfiguration: OperationalConfiguration = self._get_value(
                OperationalConfiguration, "operationalConfiguration"
            )
        else:
            self.operationalConfiguration: OperationalConfiguration = None


class OperationalConfiguration(__BaseDictObject):
    """
    The operational configuration of `supplySources`.
    """

    def __init__(self, data):
        super().__init__(data)
        if "contactDetails" in data:
            self.contactDetails: ContactDetails = self._get_value(ContactDetails, "contactDetails")
        else:
            self.contactDetails: ContactDetails = None
        if "throughputConfig" in data:
            self.throughputConfig: ThroughputConfig = self._get_value(ThroughputConfig, "throughputConfig")
        else:
            self.throughputConfig: ThroughputConfig = None
        if "operatingHoursByDay" in data:
            self.operatingHoursByDay: OperatingHoursByDay = self._get_value(OperatingHoursByDay, "operatingHoursByDay")
        else:
            self.operatingHoursByDay: OperatingHoursByDay = None
        if "handlingTime" in data:
            self.handlingTime: Duration = self._get_value(Duration, "handlingTime")
        else:
            self.handlingTime: Duration = None


class Duration(__BaseDictObject):
    """
    The duration of time.
    """

    def __init__(self, data):
        super().__init__(data)
        if "value" in data:
            self.value: NonNegativeInteger = self._get_value(NonNegativeInteger, "value")
        else:
            self.value: NonNegativeInteger = None
        if "timeUnit" in data:
            self.timeUnit: TimeUnit = self._get_value(TimeUnit, "timeUnit")
        else:
            self.timeUnit: TimeUnit = None


class ThroughputConfig(__BaseDictObject):
    """
    The throughput configuration.
    """

    def __init__(self, data):
        super().__init__(data)
        if "throughputCap" in data:
            self.throughputCap: ThroughputCap = self._get_value(ThroughputCap, "throughputCap")
        else:
            self.throughputCap: ThroughputCap = None
        if "throughputUnit" in data:
            self.throughputUnit: ThroughputUnit = self._get_value(ThroughputUnit, "throughputUnit")
        else:
            self.throughputUnit: ThroughputUnit = None


class ReturnLocation(__BaseDictObject):
    """
    The address or reference to another `supplySourceId` to act as a return location.
    """

    def __init__(self, data):
        super().__init__(data)
        if "supplySourceId" in data:
            self.supplySourceId: str = self._get_value(str, "supplySourceId")
        else:
            self.supplySourceId: str = None
        if "addressWithContact" in data:
            self.addressWithContact: AddressWithContact = self._get_value(AddressWithContact, "addressWithContact")
        else:
            self.addressWithContact: AddressWithContact = None


class AddressWithContact(__BaseDictObject):
    """
    The address and contact details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "contactDetails" in data:
            self.contactDetails: ContactDetails = self._get_value(ContactDetails, "contactDetails")
        else:
            self.contactDetails: ContactDetails = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None


class ContactDetails(__BaseDictObject):
    """
    The contact details
    """

    def __init__(self, data):
        super().__init__(data)
        if "primary" in data:
            self.primary: dict = self._get_value(dict, "primary")
        else:
            self.primary: dict = None


class ThroughputCap(__BaseDictObject):
    """
    The throughput capacity
    """

    def __init__(self, data):
        super().__init__(data)
        if "value" in data:
            self.value: NonNegativeInteger = self._get_value(NonNegativeInteger, "value")
        else:
            self.value: NonNegativeInteger = None
        if "timeUnit" in data:
            self.timeUnit: TimeUnit = self._get_value(TimeUnit, "timeUnit")
        else:
            self.timeUnit: TimeUnit = None


class OperatingHour(__BaseDictObject):
    """
    The operating hour schema
    """

    def __init__(self, data):
        super().__init__(data)
        if "startTime" in data:
            self.startTime: str = self._get_value(str, "startTime")
        else:
            self.startTime: str = None
        if "endTime" in data:
            self.endTime: str = self._get_value(str, "endTime")
        else:
            self.endTime: str = None


class OperatingHoursByDay(__BaseDictObject):
    """
    The operating hours per day
    """

    def __init__(self, data):
        super().__init__(data)
        if "monday" in data:
            self.monday: OperatingHours = self._get_value(OperatingHours, "monday")
        else:
            self.monday: OperatingHours = None
        if "tuesday" in data:
            self.tuesday: OperatingHours = self._get_value(OperatingHours, "tuesday")
        else:
            self.tuesday: OperatingHours = None
        if "wednesday" in data:
            self.wednesday: OperatingHours = self._get_value(OperatingHours, "wednesday")
        else:
            self.wednesday: OperatingHours = None
        if "thursday" in data:
            self.thursday: OperatingHours = self._get_value(OperatingHours, "thursday")
        else:
            self.thursday: OperatingHours = None
        if "friday" in data:
            self.friday: OperatingHours = self._get_value(OperatingHours, "friday")
        else:
            self.friday: OperatingHours = None
        if "saturday" in data:
            self.saturday: OperatingHours = self._get_value(OperatingHours, "saturday")
        else:
            self.saturday: OperatingHours = None
        if "sunday" in data:
            self.sunday: OperatingHours = self._get_value(OperatingHours, "sunday")
        else:
            self.sunday: OperatingHours = None


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


class SupplySourceList(list, _List["dict"]):
    """
    The list of `SupplySource`s.
    """

    def __init__(self, data):
        super().__init__([dict(datum) for datum in data])
        self.data = data


class OperatingHours(list, _List["OperatingHour"]):
    """
    A list of Operating Hours.
    """

    def __init__(self, data):
        super().__init__([OperatingHour(datum) for datum in data])
        self.data = data


class SupplySourceId(str):
    """
    An Amazon generated unique supply source ID.
    """


class SupplySourceCode(str):
    """
    The seller-provided unique supply source code.
    """


class SupplySourceAlias(str):
    """
    The custom alias for this supply source
    """


class SupplySourceStatusReadOnly(str):
    """
    The `SupplySource` status.
    """


class SupplySourceStatus(str):
    """
    The `SupplySource` status
    """


class ParkingCostType(str):
    """
    The parking cost type.
    """


class ParkingSpotIdentificationType(str):
    """
    The type of parking spot identification.
    """


class ThroughputUnit(str):
    """
    The throughput unit
    """


class TimeUnit(str):
    """
    The time unit
    """


class NonNegativeInteger(int):
    """
    An unsigned integer that can be only positive or zero.
    """


class EmailAddress(str):
    """
    The email address to which email messages are delivered.
    """


class DateTime(str):
    """
    A date and time in the rfc3339 format.
    """


class ParkingWithAddressConfiguration(
    ParkingConfiguration,
):
    """
    The parking configuration with the address.
    """

    def __init__(self, data):
        if "address" in data:
            self.address: Address = Address(data.pop("address"))
        else:
            self.address: Address = None
        self.data = data
        super().__init__(data)


class SupplySources20200701Client(__BaseClient):
    def getSupplySources(
        self,
        nextPageToken: str = None,
        pageSize: float = None,
    ):
        """
        The path to retrieve paginated supply sources.
        """
        url = f"/supplySources/2020-07-01/supplySources"
        params = {}
        if nextPageToken is not None:
            params["nextPageToken"] = nextPageToken
        if pageSize is not None:
            params["pageSize"] = pageSize
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetSupplySourcesResponse,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createSupplySource(
        self,
        data: CreateSupplySourceRequest,
    ):
        """
        Create a new supply source.
        """
        url = f"/supplySources/2020-07-01/supplySources"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateSupplySourceResponse,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getSupplySource(
        self,
        supplySourceId: str,
    ):
        """
        Retrieve a supply source.
        """
        url = f"/supplySources/2020-07-01/supplySources/{supplySourceId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: SupplySource,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateSupplySource(
        self,
        data: UpdateSupplySourceRequest,
        supplySourceId: str,
    ):
        """
        Update the configuration and capabilities of a supply source.
        """
        url = f"/supplySources/2020-07-01/supplySources/{supplySourceId}"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            204: ErrorList,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def archiveSupplySource(
        self,
        supplySourceId: str,
    ):
        """
        Archive a supply source, making it inactive. Cannot be undone.
        """
        url = f"/supplySources/2020-07-01/supplySources/{supplySourceId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            204: ErrorList,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateSupplySourceStatus(
        self,
        data: UpdateSupplySourceStatusRequest,
        supplySourceId: str,
    ):
        """
        Update the status of a supply source.
        """
        url = f"/supplySources/2020-07-01/supplySources/{supplySourceId}/status"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            204: ErrorList,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
