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
        url = "/service/v1/serviceJobs/{serviceJobId}"
        params = (("serviceJobId", "path", service_job_id, True),)  # name, param in, value, required

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
        url = "/service/v1/serviceJobs/{serviceJobId}/cancellations"
        params = (  # name, param in, value, required
            ("serviceJobId", "path", service_job_id, True),
            ("cancellationReasonCode", "query", cancellation_reason_code, True),
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
        path_parameters = {}
        url = "/service/v1/serviceJobs/{serviceJobId}/completions"
        params = (("serviceJobId", "path", service_job_id, True),)  # name, param in, value, required

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
        url = "/service/v1/serviceJobs"
        params = (  # name, param in, value, required
            ("serviceOrderIds", "query", service_order_ids, False),
            ("serviceJobStatus", "query", service_job_status, False),
            ("pageToken", "query", page_token, False),
            ("pageSize", "query", page_size, False),
            ("sortField", "query", sort_field, False),
            ("sortOrder", "query", sort_order, False),
            ("createdAfter", "query", created_after, False),
            ("createdBefore", "query", created_before, False),
            ("lastUpdatedAfter", "query", last_updated_after, False),
            ("lastUpdatedBefore", "query", last_updated_before, False),
            ("scheduleStartDate", "query", schedule_start_date, False),
            ("scheduleEndDate", "query", schedule_end_date, False),
            ("marketplaceIds", "query", marketplace_ids, True),
        )

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
        url = "/service/v1/serviceJobs/{serviceJobId}/appointments"
        params = (("serviceJobId", "path", service_job_id, True),)  # name, param in, value, required

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
        url = "/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}"
        params = (  # name, param in, value, required
            ("serviceJobId", "path", service_job_id, True),
            ("appointmentId", "path", appointment_id, True),
        )
