"""
Selling Partner API for Reports
=============================================================================================

The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses.
API Version: 2021-06-30
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class ErrorList:
    pass


@attrs.define
class Error:
    pass


@attrs.define
class Report:
    pass


@attrs.define
class ReportList:
    pass


@attrs.define
class CreateReportScheduleSpecification:
    pass


@attrs.define
class CreateReportSpecification:
    pass


@attrs.define
class ReportOptions:
    pass


@attrs.define
class ReportSchedule:
    pass


@attrs.define
class ReportScheduleList:
    pass


@attrs.define
class CreateReportResponse:
    pass


@attrs.define
class GetReportsResponse:
    pass


@attrs.define
class CreateReportScheduleResponse:
    pass


@attrs.define
class ReportDocument:
    pass


class Reports20210630Client(BaseClient):
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
        url = "/reports/2021-06-30/reports/{reportId}"
        values = (report_id,)
        response = self._parse_args_and_request(url, "DELETE", values, self._cancel_report_params)
        return response

    _cancel_report_params = (("reportId", "path"),)  # name, param in

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
        url = "/reports/2021-06-30/schedules/{reportScheduleId}"
        values = (report_schedule_id,)
        response = self._parse_args_and_request(url, "DELETE", values, self._cancel_report_schedule_params)
        return response

    _cancel_report_schedule_params = (("reportScheduleId", "path"),)  # name, param in

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
        url = "/reports/2021-06-30/reports"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_report_params)
        return response

    _create_report_params = ()  # name, param in

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
        url = "/reports/2021-06-30/schedules"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_report_schedule_params)
        return response

    _create_report_schedule_params = ()  # name, param in

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
        url = "/reports/2021-06-30/reports/{reportId}"
        values = (report_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_report_params)
        return response

    _get_report_params = (("reportId", "path"),)  # name, param in

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
        url = "/reports/2021-06-30/documents/{reportDocumentId}"
        values = (report_document_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_report_document_params)
        return response

    _get_report_document_params = (("reportDocumentId", "path"),)  # name, param in

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
        url = "/reports/2021-06-30/schedules/{reportScheduleId}"
        values = (report_schedule_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_report_schedule_params)
        return response

    _get_report_schedule_params = (("reportScheduleId", "path"),)  # name, param in

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
        url = "/reports/2021-06-30/schedules"
        values = (report_types,)
        response = self._parse_args_and_request(url, "GET", values, self._get_report_schedules_params)
        return response

    _get_report_schedules_params = (("reportTypes", "query"),)  # name, param in

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
        url = "/reports/2021-06-30/reports"
        values = (
            report_types,
            processing_statuses,
            marketplace_ids,
            page_size,
            created_since,
            created_until,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_reports_params)
        return response

    _get_reports_params = (  # name, param in
        ("reportTypes", "query"),
        ("processingStatuses", "query"),
        ("marketplaceIds", "query"),
        ("pageSize", "query"),
        ("createdSince", "query"),
        ("createdUntil", "query"),
        ("nextToken", "query"),
    )
