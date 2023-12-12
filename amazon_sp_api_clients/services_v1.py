from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetServiceJobByServiceJobIdResponse(__BaseDictObject):
    """
    The response schema for the `getServiceJobByServiceJobId` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ServiceJob = self._get_value(ServiceJob, "payload")
        else:
            self.payload: ServiceJob = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CancelServiceJobByServiceJobIdResponse(__BaseDictObject):
    """
    Response schema for the `cancelServiceJobByServiceJobId` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CompleteServiceJobByServiceJobIdResponse(__BaseDictObject):
    """
    Response schema for the `completeServiceJobByServiceJobId` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetServiceJobsResponse(__BaseDictObject):
    """
    Response schema for the `getServiceJobs` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: JobListing = self._get_value(JobListing, "payload")
        else:
            self.payload: JobListing = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class SetAppointmentResponse(__BaseDictObject):
    """
    Response schema for the `addAppointmentForServiceJobByServiceJobId` and `rescheduleAppointmentForServiceJobByServiceJobId` operations.
    """

    def __init__(self, data):
        super().__init__(data)
        if "appointmentId" in data:
            self.appointmentId: AppointmentId = self._get_value(AppointmentId, "appointmentId")
        else:
            self.appointmentId: AppointmentId = None
        if "warnings" in data:
            self.warnings: WarningList = self._get_value(WarningList, "warnings")
        else:
            self.warnings: WarningList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class AssignAppointmentResourcesResponse(__BaseDictObject):
    """
    Response schema for the `assignAppointmentResources` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: dict = self._get_value(dict, "payload")
        else:
            self.payload: dict = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class AssignAppointmentResourcesRequest(__BaseDictObject):
    """
    Request schema for the `assignAppointmentResources` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resources" in data:
            self.resources: AppointmentResources = self._get_value(AppointmentResources, "resources")
        else:
            self.resources: AppointmentResources = None


class JobListing(__BaseDictObject):
    """
    The payload for the `getServiceJobs` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalResultSize" in data:
            self.totalResultSize: int = self._get_value(int, "totalResultSize")
        else:
            self.totalResultSize: int = None
        if "nextPageToken" in data:
            self.nextPageToken: str = self._get_value(str, "nextPageToken")
        else:
            self.nextPageToken: str = None
        if "previousPageToken" in data:
            self.previousPageToken: str = self._get_value(str, "previousPageToken")
        else:
            self.previousPageToken: str = None
        if "jobs" in data:
            self.jobs: _List[ServiceJob] = [ServiceJob(datum) for datum in data["jobs"]]
        else:
            self.jobs: _List[ServiceJob] = []


class ServiceJob(__BaseDictObject):
    """
    The job details of a service.
    """

    def __init__(self, data):
        super().__init__(data)
        if "createTime" in data:
            self.createTime: str = self._get_value(str, "createTime")
        else:
            self.createTime: str = None
        if "serviceJobId" in data:
            self.serviceJobId: ServiceJobId = self._get_value(ServiceJobId, "serviceJobId")
        else:
            self.serviceJobId: ServiceJobId = None
        if "serviceJobStatus" in data:
            self.serviceJobStatus: str = self._get_value(str, "serviceJobStatus")
        else:
            self.serviceJobStatus: str = None
        if "scopeOfWork" in data:
            self.scopeOfWork: ScopeOfWork = self._get_value(ScopeOfWork, "scopeOfWork")
        else:
            self.scopeOfWork: ScopeOfWork = None
        if "seller" in data:
            self.seller: Seller = self._get_value(Seller, "seller")
        else:
            self.seller: Seller = None
        if "serviceJobProvider" in data:
            self.serviceJobProvider: ServiceJobProvider = self._get_value(ServiceJobProvider, "serviceJobProvider")
        else:
            self.serviceJobProvider: ServiceJobProvider = None
        if "preferredAppointmentTimes" in data:
            self.preferredAppointmentTimes: _List[AppointmentTime] = [
                AppointmentTime(datum) for datum in data["preferredAppointmentTimes"]
            ]
        else:
            self.preferredAppointmentTimes: _List[AppointmentTime] = []
        if "appointments" in data:
            self.appointments: _List[Appointment] = [Appointment(datum) for datum in data["appointments"]]
        else:
            self.appointments: _List[Appointment] = []
        if "serviceOrderId" in data:
            self.serviceOrderId: OrderId = self._get_value(OrderId, "serviceOrderId")
        else:
            self.serviceOrderId: OrderId = None
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "storeId" in data:
            self.storeId: str = self._get_value(str, "storeId")
        else:
            self.storeId: str = None
        if "buyer" in data:
            self.buyer: Buyer = self._get_value(Buyer, "buyer")
        else:
            self.buyer: Buyer = None
        if "associatedItems" in data:
            self.associatedItems: _List[AssociatedItem] = [AssociatedItem(datum) for datum in data["associatedItems"]]
        else:
            self.associatedItems: _List[AssociatedItem] = []
        if "serviceLocation" in data:
            self.serviceLocation: ServiceLocation = self._get_value(ServiceLocation, "serviceLocation")
        else:
            self.serviceLocation: ServiceLocation = None


class ScopeOfWork(__BaseDictObject):
    """
    The scope of work for the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None
        if "quantity" in data:
            self.quantity: int = self._get_value(int, "quantity")
        else:
            self.quantity: int = None
        if "requiredSkills" in data:
            self.requiredSkills: _List[str] = [str(datum) for datum in data["requiredSkills"]]
        else:
            self.requiredSkills: _List[str] = []


class Seller(__BaseDictObject):
    """
    Information about the seller of the service job.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellerId" in data:
            self.sellerId: str = self._get_value(str, "sellerId")
        else:
            self.sellerId: str = None


class ServiceJobProvider(__BaseDictObject):
    """
    Information about the service job provider.
    """

    def __init__(self, data):
        super().__init__(data)
        if "serviceJobProviderId" in data:
            self.serviceJobProviderId: str = self._get_value(str, "serviceJobProviderId")
        else:
            self.serviceJobProviderId: str = None


class Buyer(__BaseDictObject):
    """
    Information about the buyer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "buyerId" in data:
            self.buyerId: str = self._get_value(str, "buyerId")
        else:
            self.buyerId: str = None
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "phone" in data:
            self.phone: str = self._get_value(str, "phone")
        else:
            self.phone: str = None
        if "isPrimeMember" in data:
            self.isPrimeMember: bool = self._get_value(convert_bool, "isPrimeMember")
        else:
            self.isPrimeMember: bool = None


class AppointmentTime(__BaseDictObject):
    """
    The time of the appointment window.
    """

    def __init__(self, data):
        super().__init__(data)
        if "startTime" in data:
            self.startTime: str = self._get_value(str, "startTime")
        else:
            self.startTime: str = None
        if "durationInMinutes" in data:
            self.durationInMinutes: int = self._get_value(int, "durationInMinutes")
        else:
            self.durationInMinutes: int = None


class Appointment(__BaseDictObject):
    """
    The details of an appointment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "appointmentId" in data:
            self.appointmentId: AppointmentId = self._get_value(AppointmentId, "appointmentId")
        else:
            self.appointmentId: AppointmentId = None
        if "appointmentStatus" in data:
            self.appointmentStatus: str = self._get_value(str, "appointmentStatus")
        else:
            self.appointmentStatus: str = None
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTime = self._get_value(AppointmentTime, "appointmentTime")
        else:
            self.appointmentTime: AppointmentTime = None
        if "assignedTechnicians" in data:
            self.assignedTechnicians: _List[Technician] = [Technician(datum) for datum in data["assignedTechnicians"]]
        else:
            self.assignedTechnicians: _List[Technician] = []
        if "rescheduledAppointmentId" in data:
            self.rescheduledAppointmentId: AppointmentId = self._get_value(AppointmentId, "rescheduledAppointmentId")
        else:
            self.rescheduledAppointmentId: AppointmentId = None
        if "poa" in data:
            self.poa: Poa = self._get_value(Poa, "poa")
        else:
            self.poa: Poa = None


class Technician(__BaseDictObject):
    """
    A technician who is assigned to perform the service job in part or in full.
    """

    def __init__(self, data):
        super().__init__(data)
        if "technicianId" in data:
            self.technicianId: str = self._get_value(str, "technicianId")
        else:
            self.technicianId: str = None
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None


class Poa(__BaseDictObject):
    """
    Proof of Appointment (POA) details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTime = self._get_value(AppointmentTime, "appointmentTime")
        else:
            self.appointmentTime: AppointmentTime = None
        if "technicians" in data:
            self.technicians: _List[Technician] = [Technician(datum) for datum in data["technicians"]]
        else:
            self.technicians: _List[Technician] = []
        if "uploadingTechnician" in data:
            self.uploadingTechnician: str = self._get_value(str, "uploadingTechnician")
        else:
            self.uploadingTechnician: str = None
        if "uploadTime" in data:
            self.uploadTime: str = self._get_value(str, "uploadTime")
        else:
            self.uploadTime: str = None
        if "poaType" in data:
            self.poaType: str = self._get_value(str, "poaType")
        else:
            self.poaType: str = None


class AssociatedItem(__BaseDictObject):
    """
    Information about an item associated with the service job.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None
        if "quantity" in data:
            self.quantity: int = self._get_value(int, "quantity")
        else:
            self.quantity: int = None
        if "orderId" in data:
            self.orderId: OrderId = self._get_value(OrderId, "orderId")
        else:
            self.orderId: OrderId = None
        if "itemStatus" in data:
            self.itemStatus: str = self._get_value(str, "itemStatus")
        else:
            self.itemStatus: str = None
        if "brandName" in data:
            self.brandName: str = self._get_value(str, "brandName")
        else:
            self.brandName: str = None
        if "itemDelivery" in data:
            self.itemDelivery: ItemDelivery = self._get_value(ItemDelivery, "itemDelivery")
        else:
            self.itemDelivery: ItemDelivery = None


class ItemDelivery(__BaseDictObject):
    """
    Delivery information for the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "estimatedDeliveryDate" in data:
            self.estimatedDeliveryDate: str = self._get_value(str, "estimatedDeliveryDate")
        else:
            self.estimatedDeliveryDate: str = None
        if "itemDeliveryPromise" in data:
            self.itemDeliveryPromise: ItemDeliveryPromise = self._get_value(ItemDeliveryPromise, "itemDeliveryPromise")
        else:
            self.itemDeliveryPromise: ItemDeliveryPromise = None


class ItemDeliveryPromise(__BaseDictObject):
    """
    Promised delivery information for the item.
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


class ServiceLocation(__BaseDictObject):
    """
    Information about the location of the service job.
    """

    def __init__(self, data):
        super().__init__(data)
        if "serviceLocationType" in data:
            self.serviceLocationType: str = self._get_value(str, "serviceLocationType")
        else:
            self.serviceLocationType: str = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None


class Address(__BaseDictObject):
    """
    The shipping address for the service job.
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


class AddAppointmentRequest(__BaseDictObject):
    """
    Input for add appointment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTimeInput = self._get_value(AppointmentTimeInput, "appointmentTime")
        else:
            self.appointmentTime: AppointmentTimeInput = None


class RescheduleAppointmentRequest(__BaseDictObject):
    """
    Input for rescheduled appointment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTimeInput = self._get_value(AppointmentTimeInput, "appointmentTime")
        else:
            self.appointmentTime: AppointmentTimeInput = None
        if "rescheduleReasonCode" in data:
            self.rescheduleReasonCode: RescheduleReasonCode = self._get_value(
                RescheduleReasonCode, "rescheduleReasonCode"
            )
        else:
            self.rescheduleReasonCode: RescheduleReasonCode = None


class AppointmentTimeInput(__BaseDictObject):
    """
    The input appointment time details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "startTime" in data:
            self.startTime: str = self._get_value(str, "startTime")
        else:
            self.startTime: str = None
        if "durationInMinutes" in data:
            self.durationInMinutes: int = self._get_value(int, "durationInMinutes")
        else:
            self.durationInMinutes: int = None


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
        if "errorLevel" in data:
            self.errorLevel: str = self._get_value(str, "errorLevel")
        else:
            self.errorLevel: str = None


class Warning(__BaseDictObject):
    """
    Warning returned when the request is successful, but there are important callouts based on which API clients should take defined actions.
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


class RangeSlotCapacityErrors(__BaseDictObject):
    """
    The error response schema for the `getRangeSlotCapacity` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class RangeSlotCapacity(__BaseDictObject):
    """
    Response schema for the `getRangeSlotCapacity` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resourceId" in data:
            self.resourceId: str = self._get_value(str, "resourceId")
        else:
            self.resourceId: str = None
        if "capacities" in data:
            self.capacities: _List[RangeCapacity] = [RangeCapacity(datum) for datum in data["capacities"]]
        else:
            self.capacities: _List[RangeCapacity] = []
        if "nextPageToken" in data:
            self.nextPageToken: str = self._get_value(str, "nextPageToken")
        else:
            self.nextPageToken: str = None


class RangeCapacity(__BaseDictObject):
    """
    Range capacity entity where each entry has a capacity type and corresponding slots.
    """

    def __init__(self, data):
        super().__init__(data)
        if "capacityType" in data:
            self.capacityType: CapacityType = self._get_value(CapacityType, "capacityType")
        else:
            self.capacityType: CapacityType = None
        if "slots" in data:
            self.slots: _List[RangeSlot] = [RangeSlot(datum) for datum in data["slots"]]
        else:
            self.slots: _List[RangeSlot] = []


class RangeSlot(__BaseDictObject):
    """
    Capacity slots represented in a format similar to availability rules.
    """

    def __init__(self, data):
        super().__init__(data)
        if "startDateTime" in data:
            self.startDateTime: str = self._get_value(str, "startDateTime")
        else:
            self.startDateTime: str = None
        if "endDateTime" in data:
            self.endDateTime: str = self._get_value(str, "endDateTime")
        else:
            self.endDateTime: str = None
        if "capacity" in data:
            self.capacity: int = self._get_value(int, "capacity")
        else:
            self.capacity: int = None


class FixedSlotCapacityErrors(__BaseDictObject):
    """
    The error response schema for the `getFixedSlotCapacity` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class FixedSlotCapacity(__BaseDictObject):
    """
    Response schema for the `getFixedSlotCapacity` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resourceId" in data:
            self.resourceId: str = self._get_value(str, "resourceId")
        else:
            self.resourceId: str = None
        if "slotDuration" in data:
            self.slotDuration: float = self._get_value(float, "slotDuration")
        else:
            self.slotDuration: float = None
        if "capacities" in data:
            self.capacities: _List[FixedSlot] = [FixedSlot(datum) for datum in data["capacities"]]
        else:
            self.capacities: _List[FixedSlot] = []
        if "nextPageToken" in data:
            self.nextPageToken: str = self._get_value(str, "nextPageToken")
        else:
            self.nextPageToken: str = None


class FixedSlot(__BaseDictObject):
    """
    In this slot format each slot only has the requested capacity types. This slot size is as specified by slot duration.
    """

    def __init__(self, data):
        super().__init__(data)
        if "startDateTime" in data:
            self.startDateTime: str = self._get_value(str, "startDateTime")
        else:
            self.startDateTime: str = None
        if "scheduledCapacity" in data:
            self.scheduledCapacity: int = self._get_value(int, "scheduledCapacity")
        else:
            self.scheduledCapacity: int = None
        if "availableCapacity" in data:
            self.availableCapacity: int = self._get_value(int, "availableCapacity")
        else:
            self.availableCapacity: int = None
        if "encumberedCapacity" in data:
            self.encumberedCapacity: int = self._get_value(int, "encumberedCapacity")
        else:
            self.encumberedCapacity: int = None
        if "reservedCapacity" in data:
            self.reservedCapacity: int = self._get_value(int, "reservedCapacity")
        else:
            self.reservedCapacity: int = None


class UpdateScheduleResponse(__BaseDictObject):
    """
    Response schema for the `updateSchedule` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: _List[UpdateScheduleRecord] = [UpdateScheduleRecord(datum) for datum in data["payload"]]
        else:
            self.payload: _List[UpdateScheduleRecord] = []
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class SetAppointmentFulfillmentDataRequest(__BaseDictObject):
    """
    Input for set appointment fulfillment data operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "fulfillmentTime" in data:
            self.fulfillmentTime: FulfillmentTime = self._get_value(FulfillmentTime, "fulfillmentTime")
        else:
            self.fulfillmentTime: FulfillmentTime = None
        if "appointmentResources" in data:
            self.appointmentResources: AppointmentResources = self._get_value(
                AppointmentResources, "appointmentResources"
            )
        else:
            self.appointmentResources: AppointmentResources = None
        if "fulfillmentDocuments" in data:
            self.fulfillmentDocuments: FulfillmentDocuments = self._get_value(
                FulfillmentDocuments, "fulfillmentDocuments"
            )
        else:
            self.fulfillmentDocuments: FulfillmentDocuments = None


class FulfillmentTime(__BaseDictObject):
    """
    Input for fulfillment time details
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


class FulfillmentDocument(__BaseDictObject):
    """
    Document that captured during service appointment fulfillment that portrays proof of completion
    """

    def __init__(self, data):
        super().__init__(data)
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = self._get_value(str, "uploadDestinationId")
        else:
            self.uploadDestinationId: str = None
        if "contentSha256" in data:
            self.contentSha256: str = self._get_value(str, "contentSha256")
        else:
            self.contentSha256: str = None


class AppointmentResource(__BaseDictObject):
    """
    The resource that performs or performed appointment fulfillment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resourceId" in data:
            self.resourceId: str = self._get_value(str, "resourceId")
        else:
            self.resourceId: str = None


class CreateReservationResponse(__BaseDictObject):
    """
    Response schema for the `createReservation` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CreateReservationRecord = self._get_value(CreateReservationRecord, "payload")
        else:
            self.payload: CreateReservationRecord = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class UpdateReservationResponse(__BaseDictObject):
    """
    Response schema for the `updateReservation` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: UpdateReservationRecord = self._get_value(UpdateReservationRecord, "payload")
        else:
            self.payload: UpdateReservationRecord = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CancelReservationResponse(__BaseDictObject):
    """
    Response schema for the `cancelReservation` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Recurrence(__BaseDictObject):
    """
    Repeated occurrence of an event in a time range.
    """

    def __init__(self, data):
        super().__init__(data)
        if "endTime" in data:
            self.endTime: str = self._get_value(str, "endTime")
        else:
            self.endTime: str = None
        if "daysOfWeek" in data:
            self.daysOfWeek: _List[DayOfWeek] = [DayOfWeek(datum) for datum in data["daysOfWeek"]]
        else:
            self.daysOfWeek: _List[DayOfWeek] = []
        if "daysOfMonth" in data:
            self.daysOfMonth: _List[int] = [int(datum) for datum in data["daysOfMonth"]]
        else:
            self.daysOfMonth: _List[int] = []


class AvailabilityRecord(__BaseDictObject):
    """
    `AvailabilityRecord` to represent the capacity of a resource over a time range.
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
        if "recurrence" in data:
            self.recurrence: Recurrence = self._get_value(Recurrence, "recurrence")
        else:
            self.recurrence: Recurrence = None
        if "capacity" in data:
            self.capacity: int = self._get_value(int, "capacity")
        else:
            self.capacity: int = None


class Reservation(__BaseDictObject):
    """
    Reservation object reduces the capacity of a resource.
    """

    def __init__(self, data):
        super().__init__(data)
        if "reservationId" in data:
            self.reservationId: str = self._get_value(str, "reservationId")
        else:
            self.reservationId: str = None
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None
        if "availability" in data:
            self.availability: AvailabilityRecord = self._get_value(AvailabilityRecord, "availability")
        else:
            self.availability: AvailabilityRecord = None


class UpdateScheduleRecord(__BaseDictObject):
    """
    `UpdateScheduleRecord` entity contains the `AvailabilityRecord` if there is an error/warning while performing the requested operation on it.
    """

    def __init__(self, data):
        super().__init__(data)
        if "availability" in data:
            self.availability: AvailabilityRecord = self._get_value(AvailabilityRecord, "availability")
        else:
            self.availability: AvailabilityRecord = None
        if "warnings" in data:
            self.warnings: WarningList = self._get_value(WarningList, "warnings")
        else:
            self.warnings: WarningList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateReservationRecord(__BaseDictObject):
    """
    `CreateReservationRecord` entity contains the `Reservation` if there is an error/warning while performing the requested operation on it, otherwise it will contain the new `reservationId`.
    """

    def __init__(self, data):
        super().__init__(data)
        if "reservation" in data:
            self.reservation: Reservation = self._get_value(Reservation, "reservation")
        else:
            self.reservation: Reservation = None
        if "warnings" in data:
            self.warnings: WarningList = self._get_value(WarningList, "warnings")
        else:
            self.warnings: WarningList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class UpdateReservationRecord(__BaseDictObject):
    """
    `UpdateReservationRecord` entity contains the `Reservation` if there is an error/warning while performing the requested operation on it, otherwise it will contain the new `reservationId`.
    """

    def __init__(self, data):
        super().__init__(data)
        if "reservation" in data:
            self.reservation: Reservation = self._get_value(Reservation, "reservation")
        else:
            self.reservation: Reservation = None
        if "warnings" in data:
            self.warnings: WarningList = self._get_value(WarningList, "warnings")
        else:
            self.warnings: WarningList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class RangeSlotCapacityQuery(__BaseDictObject):
    """
    Request schema for the `getRangeSlotCapacity` operation. This schema is used to define the time range and capacity types that are being queried.
    """

    def __init__(self, data):
        super().__init__(data)
        if "capacityTypes" in data:
            self.capacityTypes: _List[CapacityType] = [CapacityType(datum) for datum in data["capacityTypes"]]
        else:
            self.capacityTypes: _List[CapacityType] = []
        if "startDateTime" in data:
            self.startDateTime: str = self._get_value(str, "startDateTime")
        else:
            self.startDateTime: str = None
        if "endDateTime" in data:
            self.endDateTime: str = self._get_value(str, "endDateTime")
        else:
            self.endDateTime: str = None


class FixedSlotCapacityQuery(__BaseDictObject):
    """
    Request schema for the `getFixedSlotCapacity` operation. This schema is used to define the time range, capacity types and slot duration which are being queried.
    """

    def __init__(self, data):
        super().__init__(data)
        if "capacityTypes" in data:
            self.capacityTypes: _List[CapacityType] = [CapacityType(datum) for datum in data["capacityTypes"]]
        else:
            self.capacityTypes: _List[CapacityType] = []
        if "slotDuration" in data:
            self.slotDuration: float = self._get_value(float, "slotDuration")
        else:
            self.slotDuration: float = None
        if "startDateTime" in data:
            self.startDateTime: str = self._get_value(str, "startDateTime")
        else:
            self.startDateTime: str = None
        if "endDateTime" in data:
            self.endDateTime: str = self._get_value(str, "endDateTime")
        else:
            self.endDateTime: str = None


class UpdateScheduleRequest(__BaseDictObject):
    """
    Request schema for the `updateSchedule` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "schedules" in data:
            self.schedules: AvailabilityRecords = self._get_value(AvailabilityRecords, "schedules")
        else:
            self.schedules: AvailabilityRecords = None


class CreateReservationRequest(__BaseDictObject):
    """
    Request schema for the `createReservation` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resourceId" in data:
            self.resourceId: str = self._get_value(str, "resourceId")
        else:
            self.resourceId: str = None
        if "reservation" in data:
            self.reservation: Reservation = self._get_value(Reservation, "reservation")
        else:
            self.reservation: Reservation = None


class UpdateReservationRequest(__BaseDictObject):
    """
    Request schema for the `updateReservation` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resourceId" in data:
            self.resourceId: str = self._get_value(str, "resourceId")
        else:
            self.resourceId: str = None
        if "reservation" in data:
            self.reservation: Reservation = self._get_value(Reservation, "reservation")
        else:
            self.reservation: Reservation = None


class GetAppointmentSlotsResponse(__BaseDictObject):
    """
    The response of fetching appointment slots based on service context.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: AppointmentSlotReport = self._get_value(AppointmentSlotReport, "payload")
        else:
            self.payload: AppointmentSlotReport = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class AppointmentSlotReport(__BaseDictObject):
    """
    Availability information as per the service context queried.
    """

    def __init__(self, data):
        super().__init__(data)
        if "schedulingType" in data:
            self.schedulingType: str = self._get_value(str, "schedulingType")
        else:
            self.schedulingType: str = None
        if "startTime" in data:
            self.startTime: str = self._get_value(str, "startTime")
        else:
            self.startTime: str = None
        if "endTime" in data:
            self.endTime: str = self._get_value(str, "endTime")
        else:
            self.endTime: str = None
        if "appointmentSlots" in data:
            self.appointmentSlots: _List[AppointmentSlot] = [
                AppointmentSlot(datum) for datum in data["appointmentSlots"]
            ]
        else:
            self.appointmentSlots: _List[AppointmentSlot] = []


class AppointmentSlot(__BaseDictObject):
    """
    A time window along with associated capacity in which the service can be performed.
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
        if "capacity" in data:
            self.capacity: int = self._get_value(int, "capacity")
        else:
            self.capacity: int = None


class ServiceUploadDocument(__BaseDictObject):
    """
    Input for to be uploaded document.
    """

    def __init__(self, data):
        super().__init__(data)
        if "contentType" in data:
            self.contentType: str = self._get_value(str, "contentType")
        else:
            self.contentType: str = None
        if "contentLength" in data:
            self.contentLength: float = self._get_value(float, "contentLength")
        else:
            self.contentLength: float = None
        if "contentMD5" in data:
            self.contentMD5: str = self._get_value(str, "contentMD5")
        else:
            self.contentMD5: str = None


class CreateServiceDocumentUploadDestination(__BaseDictObject):
    """
    The response schema for the `createServiceDocumentUploadDestination` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ServiceDocumentUploadDestination = self._get_value(
                ServiceDocumentUploadDestination, "payload"
            )
        else:
            self.payload: ServiceDocumentUploadDestination = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ServiceDocumentUploadDestination(__BaseDictObject):
    """
    Information about an upload destination.
    """

    def __init__(self, data):
        super().__init__(data)
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = self._get_value(str, "uploadDestinationId")
        else:
            self.uploadDestinationId: str = None
        if "url" in data:
            self.url: str = self._get_value(str, "url")
        else:
            self.url: str = None
        if "encryptionDetails" in data:
            self.encryptionDetails: EncryptionDetails = self._get_value(EncryptionDetails, "encryptionDetails")
        else:
            self.encryptionDetails: EncryptionDetails = None
        if "headers" in data:
            self.headers: dict = self._get_value(dict, "headers")
        else:
            self.headers: dict = None


class EncryptionDetails(__BaseDictObject):
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    def __init__(self, data):
        super().__init__(data)
        if "standard" in data:
            self.standard: str = self._get_value(str, "standard")
        else:
            self.standard: str = None
        if "initializationVector" in data:
            self.initializationVector: str = self._get_value(str, "initializationVector")
        else:
            self.initializationVector: str = None
        if "key" in data:
            self.key: str = self._get_value(str, "key")
        else:
            self.key: str = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class WarningList(list, _List["Warning"]):
    """
    A list of warnings returned in the sucessful execution response of an API request.
    """

    def __init__(self, data):
        super().__init__([Warning(datum) for datum in data])
        self.data = data


class FulfillmentDocuments(list, _List["FulfillmentDocument"]):
    """
    List of documents captured during service appointment fulfillment.
    """

    def __init__(self, data):
        super().__init__([FulfillmentDocument(datum) for datum in data])
        self.data = data


class AppointmentResources(list, _List["AppointmentResource"]):
    """
    List of resources that performs or performed job appointment fulfillment.
    """

    def __init__(self, data):
        super().__init__([AppointmentResource(datum) for datum in data])
        self.data = data


class AvailabilityRecords(list, _List["AvailabilityRecord"]):
    """
    List of `AvailabilityRecord`s to represent the capacity of a resource over a time range.
    """

    def __init__(self, data):
        super().__init__([AvailabilityRecord(datum) for datum in data])
        self.data = data


class ServiceJobId(str):
    """
    Amazon identifier for the service job.
    """


class OrderId(str):
    """
    The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format.
    """


class AppointmentId(str):
    """
    The appointment identifier.
    """


class RescheduleReasonCode(str):
    """
    The appointment reschedule reason code.
    """


class DayOfWeek(str):
    """
    The day of the week.
    """


class CapacityType(str):
    """
    Type of capacity
    """


class ServicesV1Client(__BaseClient):
    def getServiceJobByServiceJobId(
        self,
        serviceJobId: str,
    ):
        """
                Gets details of service job indicated by the provided `serviceJobID`.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 20 | 40 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetServiceJobByServiceJobIdResponse,
            400: GetServiceJobByServiceJobIdResponse,
            403: GetServiceJobByServiceJobIdResponse,
            404: GetServiceJobByServiceJobIdResponse,
            413: GetServiceJobByServiceJobIdResponse,
            415: GetServiceJobByServiceJobIdResponse,
            422: GetServiceJobByServiceJobIdResponse,
            429: GetServiceJobByServiceJobIdResponse,
            500: GetServiceJobByServiceJobIdResponse,
            503: GetServiceJobByServiceJobIdResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelServiceJobByServiceJobId(
        self,
        serviceJobId: str,
        cancellationReasonCode: str,
    ):
        """
                Cancels the service job indicated by the service job identifier specified.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/cancellations"
        params = {}
        if cancellationReasonCode is not None:
            params["cancellationReasonCode"] = cancellationReasonCode
        response = self.request(
            path=url,
            method="PUT",
            params=params,
        )
        response_type = {
            200: CancelServiceJobByServiceJobIdResponse,
            400: CancelServiceJobByServiceJobIdResponse,
            403: CancelServiceJobByServiceJobIdResponse,
            404: CancelServiceJobByServiceJobIdResponse,
            413: CancelServiceJobByServiceJobIdResponse,
            415: CancelServiceJobByServiceJobIdResponse,
            422: CancelServiceJobByServiceJobIdResponse,
            429: CancelServiceJobByServiceJobIdResponse,
            500: CancelServiceJobByServiceJobIdResponse,
            503: CancelServiceJobByServiceJobIdResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def completeServiceJobByServiceJobId(
        self,
        serviceJobId: str,
    ):
        """
                Completes the service job indicated by the service job identifier specified.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/completions"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
        )
        response_type = {
            200: CompleteServiceJobByServiceJobIdResponse,
            400: CompleteServiceJobByServiceJobIdResponse,
            403: CompleteServiceJobByServiceJobIdResponse,
            404: CompleteServiceJobByServiceJobIdResponse,
            413: CompleteServiceJobByServiceJobIdResponse,
            415: CompleteServiceJobByServiceJobIdResponse,
            422: CompleteServiceJobByServiceJobIdResponse,
            429: CompleteServiceJobByServiceJobIdResponse,
            500: CompleteServiceJobByServiceJobIdResponse,
            503: CompleteServiceJobByServiceJobIdResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getServiceJobs(
        self,
        marketplaceIds: _List[str],
        serviceOrderIds: _List[str] = None,
        serviceJobStatus: _List[str] = None,
        pageToken: str = None,
        pageSize: int = None,
        sortField: str = None,
        sortOrder: str = None,
        createdAfter: str = None,
        createdBefore: str = None,
        lastUpdatedAfter: str = None,
        lastUpdatedBefore: str = None,
        scheduleStartDate: str = None,
        scheduleEndDate: str = None,
        asins: _List[str] = None,
        requiredSkills: _List[str] = None,
        storeIds: _List[str] = None,
    ):
        """
                Gets service job details for the specified filter query.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 40 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs"
        params = {}
        if serviceOrderIds is not None:
            params["serviceOrderIds"] = ",".join(map(str, serviceOrderIds))
        if serviceJobStatus is not None:
            params["serviceJobStatus"] = ",".join(map(str, serviceJobStatus))
        if pageToken is not None:
            params["pageToken"] = pageToken
        if pageSize is not None:
            params["pageSize"] = pageSize
        if sortField is not None:
            params["sortField"] = sortField
        if sortOrder is not None:
            params["sortOrder"] = sortOrder
        if createdAfter is not None:
            params["createdAfter"] = createdAfter
        if createdBefore is not None:
            params["createdBefore"] = createdBefore
        if lastUpdatedAfter is not None:
            params["lastUpdatedAfter"] = lastUpdatedAfter
        if lastUpdatedBefore is not None:
            params["lastUpdatedBefore"] = lastUpdatedBefore
        if scheduleStartDate is not None:
            params["scheduleStartDate"] = scheduleStartDate
        if scheduleEndDate is not None:
            params["scheduleEndDate"] = scheduleEndDate
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if asins is not None:
            params["asins"] = ",".join(map(str, asins))
        if requiredSkills is not None:
            params["requiredSkills"] = ",".join(map(str, requiredSkills))
        if storeIds is not None:
            params["storeIds"] = ",".join(map(str, storeIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetServiceJobsResponse,
            400: GetServiceJobsResponse,
            403: GetServiceJobsResponse,
            404: GetServiceJobsResponse,
            413: GetServiceJobsResponse,
            415: GetServiceJobsResponse,
            429: GetServiceJobsResponse,
            500: GetServiceJobsResponse,
            503: GetServiceJobsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def addAppointmentForServiceJobByServiceJobId(
        self,
        data: AddAppointmentRequest,
        serviceJobId: str,
    ):
        """
                Adds an appointment to the service job indicated by the service job identifier specified.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/appointments"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: SetAppointmentResponse,
            400: SetAppointmentResponse,
            403: SetAppointmentResponse,
            404: SetAppointmentResponse,
            413: SetAppointmentResponse,
            415: SetAppointmentResponse,
            422: SetAppointmentResponse,
            429: SetAppointmentResponse,
            500: SetAppointmentResponse,
            503: SetAppointmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def rescheduleAppointmentForServiceJobByServiceJobId(
        self,
        data: RescheduleAppointmentRequest,
        serviceJobId: str,
        appointmentId: str,
    ):
        """
                Reschedules an appointment for the service job indicated by the service job identifier specified.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: SetAppointmentResponse,
            400: SetAppointmentResponse,
            403: SetAppointmentResponse,
            404: SetAppointmentResponse,
            413: SetAppointmentResponse,
            415: SetAppointmentResponse,
            422: SetAppointmentResponse,
            429: SetAppointmentResponse,
            500: SetAppointmentResponse,
            503: SetAppointmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def assignAppointmentResources(
        self,
        data: AssignAppointmentResourcesRequest,
        serviceJobId: str,
        appointmentId: str,
    ):
        """
                Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 2 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/resources"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            200: AssignAppointmentResourcesResponse,
            400: AssignAppointmentResourcesResponse,
            403: AssignAppointmentResourcesResponse,
            404: AssignAppointmentResourcesResponse,
            413: AssignAppointmentResourcesResponse,
            415: AssignAppointmentResourcesResponse,
            422: AssignAppointmentResourcesResponse,
            429: AssignAppointmentResourcesResponse,
            500: AssignAppointmentResourcesResponse,
            503: AssignAppointmentResourcesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def setAppointmentFulfillmentData(
        self,
        data: SetAppointmentFulfillmentDataRequest,
        serviceJobId: str,
        appointmentId: str,
    ):
        """
                Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/fulfillment"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            204: str,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            422: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getRangeSlotCapacity(
        self,
        data: RangeSlotCapacityQuery,
        resourceId: str,
        marketplaceIds: _List[str],
        nextPageToken: str = None,
    ):
        """
                Provides capacity slots in a format similar to availability records.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceResources/{resourceId}/capacity/range"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if nextPageToken is not None:
            params["nextPageToken"] = nextPageToken
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: RangeSlotCapacity,
            400: RangeSlotCapacityErrors,
            401: RangeSlotCapacityErrors,
            403: RangeSlotCapacityErrors,
            404: RangeSlotCapacityErrors,
            413: RangeSlotCapacityErrors,
            415: RangeSlotCapacityErrors,
            429: RangeSlotCapacityErrors,
            500: RangeSlotCapacityErrors,
            503: RangeSlotCapacityErrors,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getFixedSlotCapacity(
        self,
        data: FixedSlotCapacityQuery,
        resourceId: str,
        marketplaceIds: _List[str],
        nextPageToken: str = None,
    ):
        """
                Provides capacity in fixed-size slots.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceResources/{resourceId}/capacity/fixed"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if nextPageToken is not None:
            params["nextPageToken"] = nextPageToken
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: FixedSlotCapacity,
            400: FixedSlotCapacityErrors,
            401: FixedSlotCapacityErrors,
            403: FixedSlotCapacityErrors,
            404: FixedSlotCapacityErrors,
            413: FixedSlotCapacityErrors,
            415: FixedSlotCapacityErrors,
            429: FixedSlotCapacityErrors,
            500: FixedSlotCapacityErrors,
            503: FixedSlotCapacityErrors,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateSchedule(
        self,
        data: UpdateScheduleRequest,
        resourceId: str,
        marketplaceIds: _List[str],
    ):
        """
                Update the schedule of the given resource.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceResources/{resourceId}/schedules"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            200: UpdateScheduleResponse,
            400: UpdateScheduleResponse,
            403: UpdateScheduleResponse,
            404: UpdateScheduleResponse,
            413: UpdateScheduleResponse,
            415: UpdateScheduleResponse,
            429: UpdateScheduleResponse,
            500: UpdateScheduleResponse,
            503: UpdateScheduleResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createReservation(
        self,
        data: CreateReservationRequest,
        marketplaceIds: _List[str],
    ):
        """
                Create a reservation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/reservation"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateReservationResponse,
            400: CreateReservationResponse,
            403: CreateReservationResponse,
            404: CreateReservationResponse,
            413: CreateReservationResponse,
            415: CreateReservationResponse,
            429: CreateReservationResponse,
            500: CreateReservationResponse,
            503: CreateReservationResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def updateReservation(
        self,
        data: UpdateReservationRequest,
        reservationId: str,
        marketplaceIds: _List[str],
    ):
        """
                Update a reservation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/reservation/{reservationId}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="PUT",
            params=params,
            data=data.data,
        )
        response_type = {
            200: UpdateReservationResponse,
            400: UpdateReservationResponse,
            403: UpdateReservationResponse,
            404: UpdateReservationResponse,
            413: UpdateReservationResponse,
            415: UpdateReservationResponse,
            429: UpdateReservationResponse,
            500: UpdateReservationResponse,
            503: UpdateReservationResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelReservation(
        self,
        reservationId: str,
        marketplaceIds: _List[str],
    ):
        """
                Cancel a reservation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/reservation/{reservationId}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            204: CancelReservationResponse,
            400: CancelReservationResponse,
            403: CancelReservationResponse,
            404: CancelReservationResponse,
            413: CancelReservationResponse,
            415: CancelReservationResponse,
            429: CancelReservationResponse,
            500: CancelReservationResponse,
            503: CancelReservationResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getAppointmmentSlotsByJobId(
        self,
        serviceJobId: str,
        marketplaceIds: _List[str],
        startTime: str = None,
        endTime: str = None,
    ):
        """
                Gets appointment slots for the service associated with the service job id specified.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/serviceJobs/{serviceJobId}/appointmentSlots"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetAppointmentSlotsResponse,
            400: GetAppointmentSlotsResponse,
            403: GetAppointmentSlotsResponse,
            404: GetAppointmentSlotsResponse,
            415: GetAppointmentSlotsResponse,
            422: GetAppointmentSlotsResponse,
            429: GetAppointmentSlotsResponse,
            500: GetAppointmentSlotsResponse,
            503: GetAppointmentSlotsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getAppointmentSlots(
        self,
        asin: str,
        storeId: str,
        marketplaceIds: _List[str],
        startTime: str = None,
        endTime: str = None,
    ):
        """
                Gets appointment slots as per the service context specified.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 20 | 40 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/appointmentSlots"
        params = {}
        if asin is not None:
            params["asin"] = asin
        if storeId is not None:
            params["storeId"] = storeId
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetAppointmentSlotsResponse,
            400: GetAppointmentSlotsResponse,
            403: GetAppointmentSlotsResponse,
            404: GetAppointmentSlotsResponse,
            415: GetAppointmentSlotsResponse,
            422: GetAppointmentSlotsResponse,
            429: GetAppointmentSlotsResponse,
            500: GetAppointmentSlotsResponse,
            503: GetAppointmentSlotsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createServiceDocumentUploadDestination(
        self,
        data: ServiceUploadDocument,
    ):
        """
                Creates an upload destination.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/service/v1/documents"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateServiceDocumentUploadDestination,
            400: CreateServiceDocumentUploadDestination,
            403: CreateServiceDocumentUploadDestination,
            404: CreateServiceDocumentUploadDestination,
            413: CreateServiceDocumentUploadDestination,
            415: CreateServiceDocumentUploadDestination,
            422: CreateServiceDocumentUploadDestination,
            429: CreateServiceDocumentUploadDestination,
            500: CreateServiceDocumentUploadDestination,
            503: CreateServiceDocumentUploadDestination,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
