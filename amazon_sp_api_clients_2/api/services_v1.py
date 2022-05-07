"""
Selling Partner API for Services
=============================================================================================

With the Services API, you can build applications that help service providers get and modify their service orders.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddAppointmentRequest:
    """
    Input for add appointment operation.
    """

    appointment_time: "AppointmentTimeInput" = attrs.field()
    """
    The input appointment time details.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    The shipping address for the service job.
    """

    address_line1: str = attrs.field()
    """
    The first line of the address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional address information, if required.
    """

    city: Optional[str] = attrs.field()
    """
    The city.
    """

    country_code: Optional[str] = attrs.field()
    """
    The two digit country code, in ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field()
    """
    The county.
    """

    district: Optional[str] = attrs.field()
    """
    The district.
    """

    name: str = attrs.field()
    """
    The name of the person, business, or institution.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number.
    """

    postal_code: Optional[str] = attrs.field()
    """
    The postal code. This can contain letters, digits, spaces, and/or punctuation.
    """

    state_or_region: Optional[str] = attrs.field()
    """
    The state or region.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Appointment:
    """
    The details of an appointment.
    """

    appointment_id: Optional["AppointmentId"] = attrs.field()
    """
    The appointment identifier.
    """

    appointment_status: Optional[Union[Literal["ACTIVE"], Literal["CANCELLED"], Literal["COMPLETED"]]] = attrs.field()
    """
    The status of the appointment.
    """

    appointment_time: Optional["AppointmentTime"] = attrs.field()
    """
    The time of the appointment window.
    """

    assigned_technicians: Optional[List["Technician"]] = attrs.field()
    """
    A list of technicians assigned to the service job.

    Extra fields:
    {'minItems': 1}
    """

    poa: Optional["Poa"] = attrs.field()
    """
    Proof of Appointment (POA) details.
    """

    rescheduled_appointment_id: Optional["AppointmentId"] = attrs.field()
    """
    The appointment identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AppointmentId:
    """
    The appointment identifier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AppointmentTime:
    """
    The time of the appointment window.
    """

    duration_in_minutes: int = attrs.field()
    """
    The duration of the appointment window, in minutes.

    Extra fields:
    {'minimum': 1.0}
    """

    start_time: datetime = attrs.field()
    """
    The date and time of the start of the appointment window, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AppointmentTimeInput:
    """
    The input appointment time details.
    """

    duration_in_minutes: Optional[int] = attrs.field()
    """
    The duration of an appointment in minutes.
    """

    start_time: datetime = attrs.field()
    """
    The date, time in UTC for the start time of an appointment in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AssociatedItem:
    """
    Information about an item associated with the service job.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    brand_name: Optional[str] = attrs.field()
    """
    The brand name of the item.
    """

    item_delivery: Optional["ItemDelivery"] = attrs.field()
    """
    Delivery information for the item.
    """

    item_status: Optional[
        Union[Literal["ACTIVE"], Literal["CANCELLED"], Literal["SHIPPED"], Literal["DELIVERED"]]
    ] = attrs.field()
    """
    The status of the item.
    """

    order_id: Optional["OrderId"] = attrs.field()
    """
    The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format.
    """

    quantity: Optional[int] = attrs.field()
    """
    The total number of items included in the order.
    """

    title: Optional[str] = attrs.field()
    """
    The title of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Buyer:
    """
    Information about the buyer.
    """

    buyer_id: Optional[str] = attrs.field()
    """
    The identifier of the buyer.

    Extra fields:
    {'pattern': '^[A-Z0-9]*$'}
    """

    is_prime_member: Optional[bool] = attrs.field()
    """
    When true, the service is for an Amazon Prime buyer.
    """

    name: Optional[str] = attrs.field()
    """
    The name of the buyer.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number of the buyer.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelServiceJobByServiceJobIdResponse:
    """
    Response schema for CancelServiceJobByServiceJobId operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CompleteServiceJobByServiceJobIdResponse:
    """
    Response schema for CompleteServiceJobByServiceJobId operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    error_level: Optional[Union[Literal["ERROR"], Literal["WARNING"]]] = attrs.field()
    """
    The type of error.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetServiceJobByServiceJobIdResponse:
    """
    The response schema for the GetServiceJobByServiceJobId operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ServiceJob"] = attrs.field()
    """
    The job details of a service.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetServiceJobsResponse:
    """
    Response schema for GetJobs operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["JobListing"] = attrs.field()
    """
    The payload for the GetJobs operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDelivery:
    """
    Delivery information for the item.
    """

    estimated_delivery_date: Optional[datetime] = attrs.field()
    """
    The date and time of the latest Estimated Delivery Date (EDD) of all the items with an EDD. In ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    item_delivery_promise: Optional["ItemDeliveryPromise"] = attrs.field()
    """
    Promised delivery information for the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDeliveryPromise:
    """
    Promised delivery information for the item.
    """

    end_time: Optional[datetime] = attrs.field()
    """
    The date and time of the end of the promised delivery window, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    start_time: Optional[datetime] = attrs.field()
    """
    The date and time of the start of the promised delivery window, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class JobListing:
    """
    The payload for the GetJobs operation.
    """

    jobs: Optional[List["ServiceJob"]] = attrs.field()
    """
    List of job details for the given input.
    """

    next_page_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request.If nextPageToken is returned, pass the value of nextPageToken to the pageToken to get next results.
    """

    previous_page_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request.If previousPageToken is returned, pass the value of previousPageToken to the pageToken to get previous page results.
    """

    total_result_size: Optional[int] = attrs.field()
    """
    Total result size of the query result.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderId:
    """
    The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Poa:
    """
    Proof of Appointment (POA) details.
    """

    appointment_time: Optional["AppointmentTime"] = attrs.field()
    """
    The time of the appointment window.
    """

    poa_type: Optional[
        Union[
            Literal["NO_SIGNATURE_DUMMY_POS"],
            Literal["CUSTOMER_SIGNATURE"],
            Literal["DUMMY_RECEIPT"],
            Literal["POA_RECEIPT"],
        ]
    ] = attrs.field()
    """
    The type of POA uploaded.
    """

    technicians: Optional[List["Technician"]] = attrs.field()
    """
    A list of technicians.

    Extra fields:
    {'minItems': 1}
    """

    upload_time: Optional[datetime] = attrs.field()
    """
    The date and time when the POA was uploaded, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    uploading_technician: Optional[str] = attrs.field()
    """
    The identifier of the technician who uploaded the POA.

    Extra fields:
    {'pattern': '^[A-Z0-9]*$'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RescheduleAppointmentRequest:
    """
    Input for rescheduled appointment operation.
    """

    appointment_time: "AppointmentTimeInput" = attrs.field()
    """
    The input appointment time details.
    """

    reschedule_reason_code: "RescheduleReasonCode" = attrs.field()
    """
    Appointment reschedule reason code.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RescheduleReasonCode:
    """
    Appointment reschedule reason code.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ScopeOfWork:
    """
    The scope of work for the order.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the service job.
    """

    quantity: Optional[int] = attrs.field()
    """
    The number of service jobs.
    """

    required_skills: Optional[List[str]] = attrs.field()
    """
    A list of skills required to perform the job.
    """

    title: Optional[str] = attrs.field()
    """
    The title of the service job.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Seller:
    """
    Information about the seller of the service job.
    """

    seller_id: Optional[str] = attrs.field()
    """
    The identifier of the seller of the service job.

    Extra fields:
    {'pattern': '^[A-Z0-9]*$'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceJob:
    """
    The job details of a service.
    """

    appointments: Optional[List["Appointment"]] = attrs.field()
    """
    A list of appointments.
    """

    associated_items: Optional[List["AssociatedItem"]] = attrs.field()
    """
    A list of items associated with the service job.
    """

    buyer: Optional["Buyer"] = attrs.field()
    """
    Information about the buyer.
    """

    create_time: Optional[datetime] = attrs.field()
    """
    The date and time of the creation of the job, in ISO 8601 format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    The marketplace identifier.

    Extra fields:
    {'pattern': '^[A-Z0-9]*$'}
    """

    preferred_appointment_times: Optional[List["AppointmentTime"]] = attrs.field()
    """
    A list of appointment windows preferred by the buyer. Included only if the buyer selected appointment windows when creating the order.
    """

    scope_of_work: Optional["ScopeOfWork"] = attrs.field()
    """
    The scope of work for the order.
    """

    seller: Optional["Seller"] = attrs.field()
    """
    Information about the seller of the service job.
    """

    service_job_id: Optional["ServiceJobId"] = attrs.field()
    """
    Amazon identifier for the service job.
    """

    service_job_provider: Optional["ServiceJobProvider"] = attrs.field()
    """
    Information about the service job provider.
    """

    service_job_status: Optional[
        Union[
            Literal["NOT_SERVICED"],
            Literal["CANCELLED"],
            Literal["COMPLETED"],
            Literal["PENDING_SCHEDULE"],
            Literal["NOT_FULFILLABLE"],
            Literal["HOLD"],
            Literal["PAYMENT_DECLINED"],
        ]
    ] = attrs.field()
    """
    The status of the service job.
    """

    service_location: Optional["ServiceLocation"] = attrs.field()
    """
    Information about the location of the service job.
    """

    service_order_id: Optional["OrderId"] = attrs.field()
    """
    The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceJobId:
    """
    Amazon identifier for the service job.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceJobProvider:
    """
    Information about the service job provider.
    """

    service_job_provider_id: Optional[str] = attrs.field()
    """
    The identifier of the service job provider.

    Extra fields:
    {'pattern': '^[A-Z0-9]*$'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceLocation:
    """
    Information about the location of the service job.
    """

    address: Optional["Address"] = attrs.field()
    """
    The shipping address for the service job.
    """

    service_location_type: Optional[Union[Literal["IN_HOME"], Literal["IN_STORE"], Literal["ONLINE"]]] = attrs.field()
    """
    The location of the service job.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SetAppointmentResponse:
    """
    Response schema for add or reschedule appointment operation.
    """

    appointment_id: Optional["AppointmentId"] = attrs.field()
    """
    The appointment identifier.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    warnings: Optional[List["Warning"]] = attrs.field()
    """
    A list of warnings returned in the sucessful execution response of an API request.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Technician:
    """
    A technician who is assigned to perform the service job in part or in full.
    """

    name: Optional[str] = attrs.field()
    """
    The name of the technician.
    """

    technician_id: Optional[str] = attrs.field()
    """
    The technician identifier.

    Extra fields:
    {'maxLength': 50, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Warning:
    """
    Warning returned when the request is successful but execution have some important callouts on basis of which API clients should take defined actions.
    """

    code: str = attrs.field()
    """
    An warning code that identifies the type of warning that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or address the warning.
    """

    message: str = attrs.field()
    """
    A message that describes the warning condition in a human-readable form.
    """


class ServicesV1Client(BaseClient):
    def add_appointment_for_service_job_by_service_job_id(
        self,
        service_job_id: str,
        appointment_time: Dict[str, Any],
    ):
        """
        Adds an appointment to the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            service_job_id: An Amazon defined service job identifier.
            appointment_time: The input appointment time details.
        """
        url = "/service/v1/serviceJobs/{serviceJobId}/appointments"
        values = (
            service_job_id,
            appointment_time,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._add_appointment_for_service_job_by_service_job_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _add_appointment_for_service_job_by_service_job_id_params = (  # name, param in
        ("serviceJobId", "path"),
        ("appointmentTime", "body"),
    )

    _add_appointment_for_service_job_by_service_job_id_responses = {
        (200, "application/json"): SetAppointmentResponse,
        (400, "application/json"): SetAppointmentResponse,
        (403, "application/json"): SetAppointmentResponse,
        (404, "application/json"): SetAppointmentResponse,
        (413, "application/json"): SetAppointmentResponse,
        (415, "application/json"): SetAppointmentResponse,
        (422, "application/json"): SetAppointmentResponse,
        (429, "application/json"): SetAppointmentResponse,
        (500, "application/json"): SetAppointmentResponse,
        (503, "application/json"): SetAppointmentResponse,
    }

    def cancel_service_job_by_service_job_id(
        self,
        service_job_id: str,
        cancellation_reason_code: str,
    ):
        """
        Cancels the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            service_job_id: An Amazon defined service job identifier.
            cancellation_reason_code: A cancel reason code that specifies the reason for cancelling a service job.
        """
        url = "/service/v1/serviceJobs/{serviceJobId}/cancellations"
        values = (
            service_job_id,
            cancellation_reason_code,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._cancel_service_job_by_service_job_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _cancel_service_job_by_service_job_id_params = (  # name, param in
        ("serviceJobId", "path"),
        ("cancellationReasonCode", "query"),
    )

    _cancel_service_job_by_service_job_id_responses = {
        (200, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (400, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (403, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (404, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (413, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (415, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (422, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (429, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (500, "application/json"): CancelServiceJobByServiceJobIdResponse,
        (503, "application/json"): CancelServiceJobByServiceJobIdResponse,
    }

    def complete_service_job_by_service_job_id(
        self,
        service_job_id: str,
    ):
        """
        Completes the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            service_job_id: An Amazon defined service job identifier.
        """
        url = "/service/v1/serviceJobs/{serviceJobId}/completions"
        values = (service_job_id,)
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._complete_service_job_by_service_job_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _complete_service_job_by_service_job_id_params = (("serviceJobId", "path"),)  # name, param in

    _complete_service_job_by_service_job_id_responses = {
        (200, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (400, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (403, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (404, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (413, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (415, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (422, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (429, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (500, "application/json"): CompleteServiceJobByServiceJobIdResponse,
        (503, "application/json"): CompleteServiceJobByServiceJobIdResponse,
    }

    def get_service_job_by_service_job_id(
        self,
        service_job_id: str,
    ):
        """
        Gets service job details for the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 20 | 40 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            service_job_id: A service job identifier.
        """
        url = "/service/v1/serviceJobs/{serviceJobId}"
        values = (service_job_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_service_job_by_service_job_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_service_job_by_service_job_id_params = (("serviceJobId", "path"),)  # name, param in

    _get_service_job_by_service_job_id_responses = {
        (200, "application/json"): GetServiceJobByServiceJobIdResponse,
        (400, "application/json"): GetServiceJobByServiceJobIdResponse,
        (403, "application/json"): GetServiceJobByServiceJobIdResponse,
        (404, "application/json"): GetServiceJobByServiceJobIdResponse,
        (413, "application/json"): GetServiceJobByServiceJobIdResponse,
        (415, "application/json"): GetServiceJobByServiceJobIdResponse,
        (422, "application/json"): GetServiceJobByServiceJobIdResponse,
        (429, "application/json"): GetServiceJobByServiceJobIdResponse,
        (500, "application/json"): GetServiceJobByServiceJobIdResponse,
        (503, "application/json"): GetServiceJobByServiceJobIdResponse,
    }

    def get_service_jobs(
        self,
        marketplace_ids: List[str],
        service_order_ids: List[str] = None,
        service_job_status: List[
            Union[
                Literal["NOT_SERVICED"],
                Literal["CANCELLED"],
                Literal["COMPLETED"],
                Literal["PENDING_SCHEDULE"],
                Literal["NOT_FULFILLABLE"],
                Literal["HOLD"],
                Literal["PAYMENT_DECLINED"],
            ]
        ] = None,
        page_token: str = None,
        page_size: int = None,
        sort_field: Union[Literal["JOB_DATE"], Literal["JOB_STATUS"]] = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        created_after: str = None,
        created_before: str = None,
        last_updated_after: str = None,
        last_updated_before: str = None,
        schedule_start_date: str = None,
        schedule_end_date: str = None,
    ):
        """
        Gets service job details for the specified filter query.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 40 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            service_order_ids: List of service order ids for the query you want to perform.Max values supported 20.
            service_job_status: A list of one or more job status by which to filter the list of jobs.
            page_token: String returned in the response of your previous request.
            page_size: A non-negative integer that indicates the maximum number of jobs to return in the list, Value must be 1 - 20. Default 20.
            sort_field: Sort fields on which you want to sort the output.
            sort_order: Sort order for the query you want to perform.
            created_after: A date used for selecting jobs created after (or at) a specified time must be in ISO 8601 format. Required if LastUpdatedAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.
            created_before: A date used for selecting jobs created before (or at) a specified time must be in ISO 8601 format.
            last_updated_after: A date used for selecting jobs updated after (or at) a specified time must be in ISO 8601 format. Required if createdAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.
            last_updated_before: A date used for selecting jobs updated before (or at) a specified time must be in ISO 8601 format.
            schedule_start_date: A date used for filtering jobs schedule after (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.
            schedule_end_date: A date used for filtering jobs schedule before (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.
            marketplace_ids: Used to select jobs that were placed in the specified marketplaces.
        """
        url = "/service/v1/serviceJobs"
        values = (
            service_order_ids,
            service_job_status,
            page_token,
            page_size,
            sort_field,
            sort_order,
            created_after,
            created_before,
            last_updated_after,
            last_updated_before,
            schedule_start_date,
            schedule_end_date,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_service_jobs_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_service_jobs_params = (  # name, param in
        ("serviceOrderIds", "query"),
        ("serviceJobStatus", "query"),
        ("pageToken", "query"),
        ("pageSize", "query"),
        ("sortField", "query"),
        ("sortOrder", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("lastUpdatedAfter", "query"),
        ("lastUpdatedBefore", "query"),
        ("scheduleStartDate", "query"),
        ("scheduleEndDate", "query"),
        ("marketplaceIds", "query"),
    )

    _get_service_jobs_responses = {
        (200, "application/json"): GetServiceJobsResponse,
        (400, "application/json"): GetServiceJobsResponse,
        (403, "application/json"): GetServiceJobsResponse,
        (404, "application/json"): GetServiceJobsResponse,
        (413, "application/json"): GetServiceJobsResponse,
        (415, "application/json"): GetServiceJobsResponse,
        (429, "application/json"): GetServiceJobsResponse,
        (500, "application/json"): GetServiceJobsResponse,
        (503, "application/json"): GetServiceJobsResponse,
    }

    def reschedule_appointment_for_service_job_by_service_job_id(
        self,
        service_job_id: str,
        appointment_id: str,
        appointment_time: Dict[str, Any],
        reschedule_reason_code: str,
    ):
        """
        Reschedules an appointment for the service job indicated by the service job identifier you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 20 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            service_job_id: An Amazon defined service job identifier.
            appointment_id: An existing appointment identifier for the Service Job.
            appointment_time: The input appointment time details.
            reschedule_reason_code: Appointment reschedule reason code.
        """
        url = "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}"
        values = (
            service_job_id,
            appointment_id,
            appointment_time,
            reschedule_reason_code,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._reschedule_appointment_for_service_job_by_service_job_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _reschedule_appointment_for_service_job_by_service_job_id_params = (  # name, param in
        ("serviceJobId", "path"),
        ("appointmentId", "path"),
        ("appointmentTime", "body"),
        ("rescheduleReasonCode", "body"),
    )

    _reschedule_appointment_for_service_job_by_service_job_id_responses = {
        (200, "application/json"): SetAppointmentResponse,
        (400, "application/json"): SetAppointmentResponse,
        (403, "application/json"): SetAppointmentResponse,
        (404, "application/json"): SetAppointmentResponse,
        (413, "application/json"): SetAppointmentResponse,
        (415, "application/json"): SetAppointmentResponse,
        (422, "application/json"): SetAppointmentResponse,
        (429, "application/json"): SetAppointmentResponse,
        (500, "application/json"): SetAppointmentResponse,
        (503, "application/json"): SetAppointmentResponse,
    }
