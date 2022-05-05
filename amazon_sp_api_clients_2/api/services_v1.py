"""
Selling Partner API for Services
=============================================================================================

With the Services API, you can build applications that help service providers get and modify their service orders.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Any, Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AddAppointmentRequest:
    appointment_time: "AppointmentTimeInput" = attrs.field()
    pass


@attrs.define
class Address:
    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class Appointment:
    appointment_status: Union[Literal["ACTIVE"], Literal["CANCELLED"], Literal["COMPLETED"]] = attrs.field()
    assigned_technicians: list["Technician"] = attrs.field()
    # {'minItems': 1}

    appointment_id: "AppointmentId" = attrs.field()
    appointment_time: "AppointmentTime" = attrs.field()
    poa: "Poa" = attrs.field()
    rescheduled_appointment_id: "AppointmentId" = attrs.field()
    pass


@attrs.define
class AppointmentId:
    pass


@attrs.define
class AppointmentTime:
    duration_in_minutes: int = attrs.field()
    # {'minimum': 1.0}
    start_time: str = attrs.field()
    # {'schema_format': 'date-time'}

    pass


@attrs.define
class AppointmentTimeInput:
    duration_in_minutes: int = attrs.field()
    start_time: str = attrs.field()
    # {'schema_format': 'date-time'}

    pass


@attrs.define
class AssociatedItem:
    asin: str = attrs.field()
    brand_name: str = attrs.field()
    item_status: Union[
        Literal["ACTIVE"], Literal["CANCELLED"], Literal["SHIPPED"], Literal["DELIVERED"]
    ] = attrs.field()
    quantity: int = attrs.field()
    title: str = attrs.field()

    item_delivery: "ItemDelivery" = attrs.field()
    order_id: "OrderId" = attrs.field()
    pass


@attrs.define
class Buyer:
    buyer_id: str = attrs.field()
    # {'pattern': '^[A-Z0-9]*$'}
    is_prime_member: bool = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()

    pass


@attrs.define
class CancelServiceJobByServiceJobIdResponse:
    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class CompleteServiceJobByServiceJobIdResponse:
    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    error_level: Union[Literal["ERROR"], Literal["WARNING"]] = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class GetServiceJobByServiceJobIdResponse:
    errors: "ErrorList" = attrs.field()
    payload: "ServiceJob" = attrs.field()
    pass


@attrs.define
class GetServiceJobsResponse:
    errors: "ErrorList" = attrs.field()
    payload: "JobListing" = attrs.field()
    pass


@attrs.define
class ItemDelivery:
    estimated_delivery_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    item_delivery_promise: "ItemDeliveryPromise" = attrs.field()
    pass


@attrs.define
class ItemDeliveryPromise:
    end_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    start_time: str = attrs.field()
    # {'schema_format': 'date-time'}

    pass


@attrs.define
class JobListing:
    jobs: list["ServiceJob"] = attrs.field()
    next_page_token: str = attrs.field()
    previous_page_token: str = attrs.field()
    total_result_size: int = attrs.field()

    pass


@attrs.define
class OrderId:
    pass


@attrs.define
class Poa:
    poa_type: Union[
        Literal["NO_SIGNATURE_DUMMY_POS"],
        Literal["CUSTOMER_SIGNATURE"],
        Literal["DUMMY_RECEIPT"],
        Literal["POA_RECEIPT"],
    ] = attrs.field()
    technicians: list["Technician"] = attrs.field()
    # {'minItems': 1}
    upload_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    uploading_technician: str = attrs.field()
    # {'pattern': '^[A-Z0-9]*$'}

    appointment_time: "AppointmentTime" = attrs.field()
    pass


@attrs.define
class RescheduleAppointmentRequest:
    appointment_time: "AppointmentTimeInput" = attrs.field()
    reschedule_reason_code: "RescheduleReasonCode" = attrs.field()
    pass


@attrs.define
class RescheduleReasonCode:
    pass


@attrs.define
class ScopeOfWork:
    asin: str = attrs.field()
    quantity: int = attrs.field()
    required_skills: list[str] = attrs.field()
    title: str = attrs.field()

    pass


@attrs.define
class Seller:
    seller_id: str = attrs.field()
    # {'pattern': '^[A-Z0-9]*$'}

    pass


@attrs.define
class ServiceJob:
    appointments: list["Appointment"] = attrs.field()
    associated_items: list["AssociatedItem"] = attrs.field()
    create_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    marketplace_id: str = attrs.field()
    # {'pattern': '^[A-Z0-9]*$'}
    preferred_appointment_times: list["AppointmentTime"] = attrs.field()
    service_job_status: Union[
        Literal["NOT_SERVICED"],
        Literal["CANCELLED"],
        Literal["COMPLETED"],
        Literal["PENDING_SCHEDULE"],
        Literal["NOT_FULFILLABLE"],
        Literal["HOLD"],
        Literal["PAYMENT_DECLINED"],
    ] = attrs.field()

    buyer: "Buyer" = attrs.field()
    scope_of_work: "ScopeOfWork" = attrs.field()
    seller: "Seller" = attrs.field()
    service_job_id: "ServiceJobId" = attrs.field()
    service_job_provider: "ServiceJobProvider" = attrs.field()
    service_location: "ServiceLocation" = attrs.field()
    service_order_id: "OrderId" = attrs.field()
    pass


@attrs.define
class ServiceJobId:
    pass


@attrs.define
class ServiceJobProvider:
    service_job_provider_id: str = attrs.field()
    # {'pattern': '^[A-Z0-9]*$'}

    pass


@attrs.define
class ServiceLocation:
    service_location_type: Union[Literal["IN_HOME"], Literal["IN_STORE"], Literal["ONLINE"]] = attrs.field()

    address: "Address" = attrs.field()
    pass


@attrs.define
class SetAppointmentResponse:
    appointment_id: "AppointmentId" = attrs.field()
    errors: "ErrorList" = attrs.field()
    warnings: "WarningList" = attrs.field()
    pass


@attrs.define
class Technician:
    name: str = attrs.field()
    technician_id: str = attrs.field()
    # {'minLength': 1, 'maxLength': 50}

    pass


@attrs.define
class Warning:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class WarningList:
    pass


class ServicesV1Client(BaseClient):
    def add_appointment_for_service_job_by_service_job_id(
            self,
            service_job_id: str,
            appointment_time: dict[str, Any],
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
            url, "POST", values, self._add_appointment_for_service_job_by_service_job_id_params
        )
        return response

    _add_appointment_for_service_job_by_service_job_id_params = (  # name, param in
        ("serviceJobId", "path"),
        ("appointmentTime", "body"),
    )

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
        response = self._parse_args_and_request(url, "PUT", values, self._cancel_service_job_by_service_job_id_params)
        return response

    _cancel_service_job_by_service_job_id_params = (  # name, param in
        ("serviceJobId", "path"),
        ("cancellationReasonCode", "query"),
    )

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
        response = self._parse_args_and_request(url, "PUT", values, self._complete_service_job_by_service_job_id_params)
        return response

    _complete_service_job_by_service_job_id_params = (("serviceJobId", "path"),)  # name, param in

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
        response = self._parse_args_and_request(url, "GET", values, self._get_service_job_by_service_job_id_params)
        return response

    _get_service_job_by_service_job_id_params = (("serviceJobId", "path"),)  # name, param in

    def get_service_jobs(
            self,
            marketplace_ids: list[str],
            service_order_ids: list[str] = None,
            service_job_status: list[
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
        response = self._parse_args_and_request(url, "GET", values, self._get_service_jobs_params)
        return response

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

    def reschedule_appointment_for_service_job_by_service_job_id(
            self,
            service_job_id: str,
            appointment_id: str,
            appointment_time: dict[str, Any],
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
            url, "POST", values, self._reschedule_appointment_for_service_job_by_service_job_id_params
        )
        return response

    _reschedule_appointment_for_service_job_by_service_job_id_params = (  # name, param in
        ("serviceJobId", "path"),
        ("appointmentId", "path"),
        ("appointmentTime", "body"),
        ("rescheduleReasonCode", "body"),
    )
