"""
Selling Partner API for Reports
=============================================================================================
The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-06-30
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class Reports20210630Client(BaseClient):
    def create_report(
        self,
    ):
        """
        Creates a report.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        path_parameters = {}

        url = "/reports/2021-06-30/reports".format(**path_parameters)

        query_parameters = {}

    def get_reports(
        self,
        report_types: list[str] = None,
        processing_statuses: list[
            Union[Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]]
        ] = None,
        marketplace_ids: list[str] = None,
        page_size: int = None,
        created_since: str = None,
        created_until: str = None,
        next_token: str = None,
    ):
        """
        Returns report details for the reports that match the filters that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_types: A list of report types used to filter reports. When reportTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either reportTypes or nextToken is required.
            processing_statuses: A list of processing statuses used to filter reports.
            marketplace_ids: A list of marketplace identifiers used to filter reports. The reports returned will match at least one of the marketplaces that you specify.
            page_size: The maximum number of reports to return in a single call.
            created_since: The earliest report creation date and time for reports to include in the response, in ISO 8601 date time format. The default is 90 days ago. Reports are retained for a maximum of 90 days.
            created_until: The latest report creation date and time for reports to include in the response, in ISO 8601 date time format. The default is now.
            next_token: A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getReports operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        """
        path_parameters = {}

        url = "/reports/2021-06-30/reports".format(**path_parameters)

        query_parameters = {}

        if report_types is not None:
            query_parameters["reportTypes"] = report_types

        if processing_statuses is not None:
            query_parameters["processingStatuses"] = processing_statuses

        if marketplace_ids is not None:
            query_parameters["marketplaceIds"] = marketplace_ids

        if page_size is not None:
            query_parameters["pageSize"] = page_size

        if created_since is not None:
            query_parameters["createdSince"] = created_since

        if created_until is not None:
            query_parameters["createdUntil"] = created_until

        if next_token is not None:
            query_parameters["nextToken"] = next_token

    def get_report(
        self,
        report_id: str,
    ):
        """
        Returns report details (including the reportDocumentId, if available) for the report that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_id: The identifier for the report. This identifier is unique only in combination with a seller ID.
        """
        path_parameters = {}

        path_parameters["reportId"] = report_id

        url = "/reports/2021-06-30/reports/{reportId}".format(**path_parameters)

        query_parameters = {}

    def cancel_report(
        self,
        report_id: str,
    ):
        """
        Cancels the report that you specify. Only reports with processingStatus=IN_QUEUE can be cancelled. Cancelled reports are returned in subsequent calls to the getReport and getReports operations.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_id: The identifier for the report. This identifier is unique only in combination with a seller ID.
        """
        path_parameters = {}

        path_parameters["reportId"] = report_id

        url = "/reports/2021-06-30/reports/{reportId}".format(**path_parameters)

        query_parameters = {}

    def create_report_schedule(
        self,
    ):
        """
        Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        path_parameters = {}

        url = "/reports/2021-06-30/schedules".format(**path_parameters)

        query_parameters = {}

    def get_report_schedules(
        self,
        report_types: list[str],
    ):
        """
        Returns report schedule details that match the filters that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_types: A list of report types used to filter report schedules.
        """
        path_parameters = {}

        url = "/reports/2021-06-30/schedules".format(**path_parameters)

        query_parameters = {}

        query_parameters["reportTypes"] = report_types

    def get_report_schedule(
        self,
        report_schedule_id: str,
    ):
        """
        Returns report schedule details for the report schedule that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_schedule_id: The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
        """
        path_parameters = {}

        path_parameters["reportScheduleId"] = report_schedule_id

        url = "/reports/2021-06-30/schedules/{reportScheduleId}".format(**path_parameters)

        query_parameters = {}

    def cancel_report_schedule(
        self,
        report_schedule_id: str,
    ):
        """
        Cancels the report schedule that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_schedule_id: The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
        """
        path_parameters = {}

        path_parameters["reportScheduleId"] = report_schedule_id

        url = "/reports/2021-06-30/schedules/{reportScheduleId}".format(**path_parameters)

        query_parameters = {}

    def get_report_document(
        self,
        report_document_id: str,
    ):
        """
        Returns the information required for retrieving a report document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_document_id: The identifier for the report document.
        """
        path_parameters = {}

        path_parameters["reportDocumentId"] = report_document_id

        url = "/reports/2021-06-30/documents/{reportDocumentId}".format(**path_parameters)

        query_parameters = {}
