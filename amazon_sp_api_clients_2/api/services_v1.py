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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AddAppointmentRequest:

    appointment_time: dict[str, Any]
    # {'ref': '#/components/schemas/AppointmentTimeInput', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    pass


@attrs.define
class Appointment:

    appointment_status: Union[Literal["ACTIVE"], Literal["CANCELLED"], Literal["COMPLETED"]]
    # {'enum': ['ACTIVE', 'CANCELLED', 'COMPLETED'], 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    assigned_technicians: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Reference(ref='#/components/schemas/Technician'), 'minItems': 1, 'type': 'array'}

    appointment_id: str
    # {'ref': '#/components/schemas/AppointmentId', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    appointment_time: dict[str, Any]
    # {'ref': '#/components/schemas/AppointmentTime', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    poa: dict[str, Any]
    # {'ref': '#/components/schemas/Poa', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    rescheduled_appointment_id: str
    # {'ref': '#/components/schemas/AppointmentId', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class AppointmentId:

    pass


@attrs.define
class AppointmentTime:

    duration_in_minutes: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'minimum': 1.0, 'type': 'integer'}
    start_time: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}

    pass


@attrs.define
class AppointmentTimeInput:

    duration_in_minutes: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'integer'}
    start_time: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}

    pass


@attrs.define
class AssociatedItem:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    brand_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    item_status: Union[Literal["ACTIVE"], Literal["CANCELLED"], Literal["SHIPPED"], Literal["DELIVERED"]]
    # {'enum': ['ACTIVE', 'CANCELLED', 'SHIPPED', 'DELIVERED'], 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'integer'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    item_delivery: dict[str, Any]
    # {'ref': '#/components/schemas/ItemDelivery', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    order_id: str
    # {'ref': '#/components/schemas/OrderId', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class Buyer:

    buyer_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'pattern': '^[A-Z0-9]*$', 'type': 'string'}
    is_prime_member: bool
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'boolean'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    pass


@attrs.define
class CancelServiceJobByServiceJobIdResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class CompleteServiceJobByServiceJobIdResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    error_level: Union[Literal["ERROR"], Literal["WARNING"]]
    # {'enum': ['ERROR', 'WARNING'], 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetServiceJobByServiceJobIdResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ServiceJob', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class GetServiceJobsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/JobListing', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class ItemDelivery:

    estimated_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}

    item_delivery_promise: dict[str, Any]
    # {'ref': '#/components/schemas/ItemDeliveryPromise', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class ItemDeliveryPromise:

    end_time: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}
    start_time: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}

    pass


@attrs.define
class JobListing:

    jobs: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Reference(ref='#/components/schemas/ServiceJob'), 'type': 'array'}
    next_page_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    previous_page_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    total_result_size: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'integer'}

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
    ]
    # {'enum': ['NO_SIGNATURE_DUMMY_POS', 'CUSTOMER_SIGNATURE', 'DUMMY_RECEIPT', 'POA_RECEIPT'], 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    technicians: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Reference(ref='#/components/schemas/Technician'), 'minItems': 1, 'type': 'array'}
    upload_time: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}
    uploading_technician: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'pattern': '^[A-Z0-9]*$', 'type': 'string'}

    appointment_time: dict[str, Any]
    # {'ref': '#/components/schemas/AppointmentTime', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class RescheduleAppointmentRequest:

    appointment_time: dict[str, Any]
    # {'ref': '#/components/schemas/AppointmentTimeInput', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    reschedule_reason_code: str
    # {'ref': '#/components/schemas/RescheduleReasonCode', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class RescheduleReasonCode:

    pass


@attrs.define
class ScopeOfWork:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'integer'}
    required_skills: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    pass


@attrs.define
class Seller:

    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'pattern': '^[A-Z0-9]*$', 'type': 'string'}

    pass


@attrs.define
class ServiceJob:

    appointments: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Reference(ref='#/components/schemas/Appointment'), 'type': 'array'}
    associated_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Reference(ref='#/components/schemas/AssociatedItem'), 'type': 'array'}
    create_time: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'schema_format': 'date-time', 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'pattern': '^[A-Z0-9]*$', 'type': 'string'}
    preferred_appointment_times: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'items': Reference(ref='#/components/schemas/AppointmentTime'), 'type': 'array'}
    service_job_status: Union[
        Literal["NOT_SERVICED"],
        Literal["CANCELLED"],
        Literal["COMPLETED"],
        Literal["PENDING_SCHEDULE"],
        Literal["NOT_FULFILLABLE"],
        Literal["HOLD"],
        Literal["PAYMENT_DECLINED"],
    ]
    # {'enum': ['NOT_SERVICED', 'CANCELLED', 'COMPLETED', 'PENDING_SCHEDULE', 'NOT_FULFILLABLE', 'HOLD', 'PAYMENT_DECLINED'], 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    buyer: dict[str, Any]
    # {'ref': '#/components/schemas/Buyer', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    scope_of_work: dict[str, Any]
    # {'ref': '#/components/schemas/ScopeOfWork', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    seller: dict[str, Any]
    # {'ref': '#/components/schemas/Seller', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    service_job_id: str
    # {'ref': '#/components/schemas/ServiceJobId', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    service_job_provider: dict[str, Any]
    # {'ref': '#/components/schemas/ServiceJobProvider', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    service_location: dict[str, Any]
    # {'ref': '#/components/schemas/ServiceLocation', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    service_order_id: str
    # {'ref': '#/components/schemas/OrderId', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class ServiceJobId:

    pass


@attrs.define
class ServiceJobProvider:

    service_job_provider_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'pattern': '^[A-Z0-9]*$', 'type': 'string'}

    pass


@attrs.define
class ServiceLocation:

    service_location_type: Union[Literal["IN_HOME"], Literal["IN_STORE"], Literal["ONLINE"]]
    # {'enum': ['IN_HOME', 'IN_STORE', 'ONLINE'], 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

    address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class SetAppointmentResponse:

    appointment_id: str
    # {'ref': '#/components/schemas/AppointmentId', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    warnings: list[dict[str, Any]]
    # {'ref': '#/components/schemas/WarningList', 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>}
    pass


@attrs.define
class Technician:

    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    technician_id: str
    # {'minLength': 1, 'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'maxLength': 50, 'type': 'string'}

    pass


@attrs.define
class Warning:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000015D7D8AB160>, 'type': 'string'}

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
