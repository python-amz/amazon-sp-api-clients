"""
Selling Partner API for Services
=============================================================================================
With the Services API, you can build applications that help service providers get and modify their service orders.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ServicesV1Client(BaseClient):
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
        path_parameters = {}

        path_parameters["serviceJobId"] = service_job_id

        url = "/service/v1/serviceJobs/{serviceJobId}".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        path_parameters["serviceJobId"] = service_job_id

        url = "/service/v1/serviceJobs/{serviceJobId}/cancellations".format(**path_parameters)

        query_parameters = {}

        query_parameters["cancellationReasonCode"] = cancellation_reason_code

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
        path_parameters = {}

        path_parameters["serviceJobId"] = service_job_id

        url = "/service/v1/serviceJobs/{serviceJobId}/completions".format(**path_parameters)

        query_parameters = {}

    def get_service_jobs(
        self,
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
        sort_field: str = None,
        sort_order: str = None,
        created_after: str = None,
        created_before: str = None,
        last_updated_after: str = None,
        last_updated_before: str = None,
        schedule_start_date: str = None,
        schedule_end_date: str = None,
        marketplace_ids: list[str],
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
        path_parameters = {}

        url = "/service/v1/serviceJobs".format(**path_parameters)

        query_parameters = {}

        if service_order_ids is not None:
            query_parameters["serviceOrderIds"] = service_order_ids

        if service_job_status is not None:
            query_parameters["serviceJobStatus"] = service_job_status

        if page_token is not None:
            query_parameters["pageToken"] = page_token

        if page_size is not None:
            query_parameters["pageSize"] = page_size

        if sort_field is not None:
            query_parameters["sortField"] = sort_field

        if sort_order is not None:
            query_parameters["sortOrder"] = sort_order

        if created_after is not None:
            query_parameters["createdAfter"] = created_after

        if created_before is not None:
            query_parameters["createdBefore"] = created_before

        if last_updated_after is not None:
            query_parameters["lastUpdatedAfter"] = last_updated_after

        if last_updated_before is not None:
            query_parameters["lastUpdatedBefore"] = last_updated_before

        if schedule_start_date is not None:
            query_parameters["scheduleStartDate"] = schedule_start_date

        if schedule_end_date is not None:
            query_parameters["scheduleEndDate"] = schedule_end_date

        query_parameters["marketplaceIds"] = marketplace_ids

    def add_appointment_for_service_job_by_service_job_id(
        self,
        service_job_id: str,
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
        """
        path_parameters = {}

        path_parameters["serviceJobId"] = service_job_id

        url = "/service/v1/serviceJobs/{serviceJobId}/appointments".format(**path_parameters)

        query_parameters = {}

    def reschedule_appointment_for_service_job_by_service_job_id(
        self,
        service_job_id: str,
        appointment_id: str,
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
        """
        path_parameters = {}

        path_parameters["serviceJobId"] = service_job_id

        path_parameters["appointmentId"] = appointment_id

        url = "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}".format(**path_parameters)

        query_parameters = {}
