from .base import BaseClient as __BaseClient
from typing import List as _List


class GetServiceJobByServiceJobIdResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: ServiceJob = ServiceJob(data["payload"])
        else:
            self.payload: ServiceJob = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CancelServiceJobByServiceJobIdResponse:
    def __init__(self, data):
        super().__init__()
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CompleteServiceJobByServiceJobIdResponse:
    def __init__(self, data):
        super().__init__()
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetServiceJobsResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: JobListing = JobListing(data["payload"])
        else:
            self.payload: JobListing = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class SetAppointmentResponse:
    def __init__(self, data):
        super().__init__()
        if "appointmentId" in data:
            self.appointmentId: AppointmentId = AppointmentId(data["appointmentId"])
        else:
            self.appointmentId: AppointmentId = None
        if "warnings" in data:
            self.warnings: WarningList = WarningList(data["warnings"])
        else:
            self.warnings: WarningList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class JobListing:
    def __init__(self, data):
        super().__init__()
        if "totalResultSize" in data:
            self.totalResultSize: int = int(data["totalResultSize"])
        else:
            self.totalResultSize: int = None
        if "nextPageToken" in data:
            self.nextPageToken: str = str(data["nextPageToken"])
        else:
            self.nextPageToken: str = None
        if "previousPageToken" in data:
            self.previousPageToken: str = str(data["previousPageToken"])
        else:
            self.previousPageToken: str = None
        if "jobs" in data:
            self.jobs: _List[ServiceJob] = [ServiceJob(datum) for datum in data["jobs"]]
        else:
            self.jobs: _List[ServiceJob] = []


class ServiceJob:
    def __init__(self, data):
        super().__init__()
        if "createTime" in data:
            self.createTime: str = str(data["createTime"])
        else:
            self.createTime: str = None
        if "serviceJobId" in data:
            self.serviceJobId: ServiceJobId = ServiceJobId(data["serviceJobId"])
        else:
            self.serviceJobId: ServiceJobId = None
        if "serviceJobStatus" in data:
            self.serviceJobStatus: str = str(data["serviceJobStatus"])
        else:
            self.serviceJobStatus: str = None
        if "scopeOfWork" in data:
            self.scopeOfWork: ScopeOfWork = ScopeOfWork(data["scopeOfWork"])
        else:
            self.scopeOfWork: ScopeOfWork = None
        if "seller" in data:
            self.seller: Seller = Seller(data["seller"])
        else:
            self.seller: Seller = None
        if "serviceJobProvider" in data:
            self.serviceJobProvider: ServiceJobProvider = ServiceJobProvider(data["serviceJobProvider"])
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
            self.serviceOrderId: OrderId = OrderId(data["serviceOrderId"])
        else:
            self.serviceOrderId: OrderId = None
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "buyer" in data:
            self.buyer: Buyer = Buyer(data["buyer"])
        else:
            self.buyer: Buyer = None
        if "associatedItems" in data:
            self.associatedItems: _List[AssociatedItem] = [AssociatedItem(datum) for datum in data["associatedItems"]]
        else:
            self.associatedItems: _List[AssociatedItem] = []
        if "serviceLocation" in data:
            self.serviceLocation: ServiceLocation = ServiceLocation(data["serviceLocation"])
        else:
            self.serviceLocation: ServiceLocation = None


class ScopeOfWork:
    def __init__(self, data):
        super().__init__()
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "quantity" in data:
            self.quantity: int = int(data["quantity"])
        else:
            self.quantity: int = None
        if "requiredSkills" in data:
            self.requiredSkills: _List[str] = [str(datum) for datum in data["requiredSkills"]]
        else:
            self.requiredSkills: _List[str] = []


class Seller:
    def __init__(self, data):
        super().__init__()
        if "sellerId" in data:
            self.sellerId: str = str(data["sellerId"])
        else:
            self.sellerId: str = None


class ServiceJobProvider:
    def __init__(self, data):
        super().__init__()
        if "serviceJobProviderId" in data:
            self.serviceJobProviderId: str = str(data["serviceJobProviderId"])
        else:
            self.serviceJobProviderId: str = None


class Buyer:
    def __init__(self, data):
        super().__init__()
        if "buyerId" in data:
            self.buyerId: str = str(data["buyerId"])
        else:
            self.buyerId: str = None
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "phone" in data:
            self.phone: str = str(data["phone"])
        else:
            self.phone: str = None
        if "isPrimeMember" in data:
            self.isPrimeMember: bool = bool(data["isPrimeMember"])
        else:
            self.isPrimeMember: bool = None


class AppointmentTime:
    def __init__(self, data):
        super().__init__()
        if "startTime" in data:
            self.startTime: str = str(data["startTime"])
        else:
            self.startTime: str = None
        if "durationInMinutes" in data:
            self.durationInMinutes: int = int(data["durationInMinutes"])
        else:
            self.durationInMinutes: int = None


class Appointment:
    def __init__(self, data):
        super().__init__()
        if "appointmentId" in data:
            self.appointmentId: AppointmentId = AppointmentId(data["appointmentId"])
        else:
            self.appointmentId: AppointmentId = None
        if "appointmentStatus" in data:
            self.appointmentStatus: str = str(data["appointmentStatus"])
        else:
            self.appointmentStatus: str = None
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTime = AppointmentTime(data["appointmentTime"])
        else:
            self.appointmentTime: AppointmentTime = None
        if "assignedTechnicians" in data:
            self.assignedTechnicians: _List[Technician] = [Technician(datum) for datum in data["assignedTechnicians"]]
        else:
            self.assignedTechnicians: _List[Technician] = []
        if "rescheduledAppointmentId" in data:
            self.rescheduledAppointmentId: AppointmentId = AppointmentId(data["rescheduledAppointmentId"])
        else:
            self.rescheduledAppointmentId: AppointmentId = None
        if "poa" in data:
            self.poa: Poa = Poa(data["poa"])
        else:
            self.poa: Poa = None


class Technician:
    def __init__(self, data):
        super().__init__()
        if "technicianId" in data:
            self.technicianId: str = str(data["technicianId"])
        else:
            self.technicianId: str = None
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class Poa:
    def __init__(self, data):
        super().__init__()
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTime = AppointmentTime(data["appointmentTime"])
        else:
            self.appointmentTime: AppointmentTime = None
        if "technicians" in data:
            self.technicians: _List[Technician] = [Technician(datum) for datum in data["technicians"]]
        else:
            self.technicians: _List[Technician] = []
        if "uploadingTechnician" in data:
            self.uploadingTechnician: str = str(data["uploadingTechnician"])
        else:
            self.uploadingTechnician: str = None
        if "uploadTime" in data:
            self.uploadTime: str = str(data["uploadTime"])
        else:
            self.uploadTime: str = None
        if "poaType" in data:
            self.poaType: str = str(data["poaType"])
        else:
            self.poaType: str = None


class AssociatedItem:
    def __init__(self, data):
        super().__init__()
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "quantity" in data:
            self.quantity: int = int(data["quantity"])
        else:
            self.quantity: int = None
        if "orderId" in data:
            self.orderId: OrderId = OrderId(data["orderId"])
        else:
            self.orderId: OrderId = None
        if "itemStatus" in data:
            self.itemStatus: str = str(data["itemStatus"])
        else:
            self.itemStatus: str = None
        if "brandName" in data:
            self.brandName: str = str(data["brandName"])
        else:
            self.brandName: str = None
        if "itemDelivery" in data:
            self.itemDelivery: ItemDelivery = ItemDelivery(data["itemDelivery"])
        else:
            self.itemDelivery: ItemDelivery = None


class ItemDelivery:
    def __init__(self, data):
        super().__init__()
        if "estimatedDeliveryDate" in data:
            self.estimatedDeliveryDate: str = str(data["estimatedDeliveryDate"])
        else:
            self.estimatedDeliveryDate: str = None
        if "itemDeliveryPromise" in data:
            self.itemDeliveryPromise: ItemDeliveryPromise = ItemDeliveryPromise(data["itemDeliveryPromise"])
        else:
            self.itemDeliveryPromise: ItemDeliveryPromise = None


class ItemDeliveryPromise:
    def __init__(self, data):
        super().__init__()
        if "startTime" in data:
            self.startTime: str = str(data["startTime"])
        else:
            self.startTime: str = None
        if "endTime" in data:
            self.endTime: str = str(data["endTime"])
        else:
            self.endTime: str = None


class ServiceLocation:
    def __init__(self, data):
        super().__init__()
        if "serviceLocationType" in data:
            self.serviceLocationType: str = str(data["serviceLocationType"])
        else:
            self.serviceLocationType: str = None
        if "address" in data:
            self.address: Address = Address(data["address"])
        else:
            self.address: Address = None


class Address:
    def __init__(self, data):
        super().__init__()
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


class AddAppointmentRequest:
    def __init__(self, data):
        super().__init__()
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTimeInput = AppointmentTimeInput(data["appointmentTime"])
        else:
            self.appointmentTime: AppointmentTimeInput = None


class RescheduleAppointmentRequest:
    def __init__(self, data):
        super().__init__()
        if "appointmentTime" in data:
            self.appointmentTime: AppointmentTimeInput = AppointmentTimeInput(data["appointmentTime"])
        else:
            self.appointmentTime: AppointmentTimeInput = None
        if "rescheduleReasonCode" in data:
            self.rescheduleReasonCode: RescheduleReasonCode = RescheduleReasonCode(data["rescheduleReasonCode"])
        else:
            self.rescheduleReasonCode: RescheduleReasonCode = None


class AppointmentTimeInput:
    def __init__(self, data):
        super().__init__()
        if "startTime" in data:
            self.startTime: str = str(data["startTime"])
        else:
            self.startTime: str = None
        if "durationInMinutes" in data:
            self.durationInMinutes: int = int(data["durationInMinutes"])
        else:
            self.durationInMinutes: int = None


class Error:
    def __init__(self, data):
        super().__init__()
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
        if "errorLevel" in data:
            self.errorLevel: str = str(data["errorLevel"])
        else:
            self.errorLevel: str = None


class Warning:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])


class WarningList(list, _List["Warning"]):
    def __init__(self, data):
        super().__init__([Warning(datum) for datum in data])


ServiceJobId = str
OrderId = str
AppointmentId = str
RescheduleReasonCode = str


class ServicesClient(__BaseClient):
    def getServiceJobByServiceJobId(
        self,
        serviceJobId: str,
    ):
        url = "/service/v1/serviceJobs/{serviceJobId}".format(
            serviceJobId=serviceJobId,
        )
        data = {}
        response = self.request(url, method="GET", params=data)
        return {
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
        }[response.status_code](response.json())

    def cancelServiceJobByServiceJobId(
        self,
        serviceJobId: str,
        cancellationReasonCode: str,
    ):
        url = "/service/v1/serviceJobs/{serviceJobId}/cancellations".format(
            serviceJobId=serviceJobId,
        )
        data = {}
        if cancellationReasonCode is not None:
            data["cancellationReasonCode"] = (cancellationReasonCode,)
        response = self.request(url, method="PUT", data=data)
        return {
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
        }[response.status_code](response.json())

    def completeServiceJobByServiceJobId(
        self,
        serviceJobId: str,
    ):
        url = "/service/v1/serviceJobs/{serviceJobId}/completions".format(
            serviceJobId=serviceJobId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
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
        }[response.status_code](response.json())

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
        url = "/service/v1/serviceJobs".format()
        data = {}
        if serviceOrderIds is not None:
            data["serviceOrderIds"] = ",".join(map(str, serviceOrderIds))
        if serviceJobStatus is not None:
            data["serviceJobStatus"] = ",".join(map(str, serviceJobStatus))
        if pageToken is not None:
            data["pageToken"] = (pageToken,)
        if pageSize is not None:
            data["pageSize"] = (pageSize,)
        if sortField is not None:
            data["sortField"] = (sortField,)
        if sortOrder is not None:
            data["sortOrder"] = (sortOrder,)
        if createdAfter is not None:
            data["createdAfter"] = (createdAfter,)
        if createdBefore is not None:
            data["createdBefore"] = (createdBefore,)
        if lastUpdatedAfter is not None:
            data["lastUpdatedAfter"] = (lastUpdatedAfter,)
        if lastUpdatedBefore is not None:
            data["lastUpdatedBefore"] = (lastUpdatedBefore,)
        if scheduleStartDate is not None:
            data["scheduleStartDate"] = (scheduleStartDate,)
        if scheduleEndDate is not None:
            data["scheduleEndDate"] = (scheduleEndDate,)
        if marketplaceIds is not None:
            data["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=data)
        return {
            200: GetServiceJobsResponse,
            400: GetServiceJobsResponse,
            403: GetServiceJobsResponse,
            404: GetServiceJobsResponse,
            413: GetServiceJobsResponse,
            415: GetServiceJobsResponse,
            429: GetServiceJobsResponse,
            500: GetServiceJobsResponse,
            503: GetServiceJobsResponse,
        }[response.status_code](response.json())

    def addAppointmentForServiceJobByServiceJobId(
        self,
        serviceJobId: str,
    ):
        url = "/service/v1/serviceJobs/{serviceJobId}/appointments".format(
            serviceJobId=serviceJobId,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
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
        }[response.status_code](response.json())

    def rescheduleAppointmentForServiceJobByServiceJobId(
        self,
        serviceJobId: str,
        appointmentId: str,
    ):
        url = "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}".format(
            serviceJobId=serviceJobId,
            appointmentId=appointmentId,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
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
        }[response.status_code](response.json())
