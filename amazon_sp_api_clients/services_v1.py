from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetServiceJobByServiceJobIdResponse(__BaseDictObject):
    """
    The response schema for the GetServiceJobByServiceJobId operation.
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
    Response schema for CancelServiceJobByServiceJobId operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CompleteServiceJobByServiceJobIdResponse(__BaseDictObject):
    """
    Response schema for CompleteServiceJobByServiceJobId operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetServiceJobsResponse(__BaseDictObject):
    """
    Response schema for GetJobs operation.
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
    Response schema for add or reschedule appointment operation.
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


class JobListing(__BaseDictObject):
    """
    The payload for the GetJobs operation.
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
    Warning returned when the request is successful but execution have some important callouts on basis of which API clients should take defined actions.
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


class WarningList(list, _List["Warning"]):
    """
    A list of warnings returned in the sucessful execution response of an API request.
    """

    def __init__(self, data):
        super().__init__([Warning(datum) for datum in data])
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
    Appointment reschedule reason code.
    """


class ServicesV1Client(__BaseClient):
    def getServiceJobByServiceJobId(
        self,
        serviceJobId: str,
    ):
        """
                Gets service job details for the service job indicated by the service job identifier you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 20 | 40 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
                Cancels the service job indicated by the service job identifier you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
                Completes the service job indicated by the service job identifier you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
    ):
        """
                Gets service job details for the specified filter query.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 40 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
                Adds an appointment to the service job indicated by the service job identifier you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
                Reschedules an appointment for the service job indicated by the service job identifier you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
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
