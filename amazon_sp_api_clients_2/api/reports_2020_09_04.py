"""
Selling Partner API for Reports
=============================================================================================

The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses.
API Version: 2020-09-04
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelReportResponse:
    """
    The response for the cancelReport operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelReportScheduleResponse:
    """
    The response for the cancelReportSchedule operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportResponse:
    """
    The response for the createReport operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateReportResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportResult:

    report_id: str = attrs.field()
    """
    The identifier for the report. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportScheduleResponse:
    """
    The response for the createReportSchedule operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateReportScheduleResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportScheduleResult:

    report_schedule_id: str = attrs.field()
    """
    The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportScheduleSpecification:

    marketplace_ids: List[str] = attrs.field()
    """
    A list of marketplace identifiers for the report schedule.

    Extra fields:
    {'maxItems': 25, 'minItems': 1}
    """

    next_report_creation_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when the schedule will create its next report, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    period: Union[
        Literal["PT5M"],
        Literal["PT15M"],
        Literal["PT30M"],
        Literal["PT1H"],
        Literal["PT2H"],
        Literal["PT4H"],
        Literal["PT8H"],
        Literal["PT12H"],
        Literal["P1D"],
        Literal["P2D"],
        Literal["P3D"],
        Literal["PT84H"],
        Literal["P7D"],
        Literal["P14D"],
        Literal["P15D"],
        Literal["P18D"],
        Literal["P30D"],
        Literal["P1M"],
    ] = attrs.field()
    """
    One of a set of predefined ISO 8601 periods that specifies how often a report should be created.
    """

    report_options: Optional["ReportOptions"] = attrs.field(
        default=None,
    )
    """
    Additional information passed to reports. This varies by report type.
    """

    report_type: str = attrs.field()
    """
    The report type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportSpecification:

    data_end_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The end of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    data_start_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The start of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    marketplace_ids: List[str] = attrs.field()
    """
    A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.

    Extra fields:
    {'maxItems': 25, 'minItems': 1}
    """

    report_options: Optional["ReportOptions"] = attrs.field(
        default=None,
    )
    """
    Additional information passed to reports. This varies by report type.
    """

    report_type: str = attrs.field()
    """
    The report type.
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

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetReportDocumentResponse:
    """
    Response schema.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ReportDocument"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetReportResponse:
    """
    The response for the getReport operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Report"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetReportScheduleResponse:
    """
    The response for the getReportSchedule operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ReportSchedule"] = attrs.field()
    """
    Detailed information about a report schedule.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetReportSchedulesResponse:
    """
    The response for the getReportSchedules operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional[List["ReportSchedule"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetReportsResponse:
    """
    The response for the getReports operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    next_token: Optional[str] = attrs.field()
    """
    Returned when the number of results exceeds pageSize. To get the next page of results, call getReports with this token as the only parameter.
    """

    payload: Optional[List["Report"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Report:

    created_time: datetime = attrs.field()
    """
    The date and time when the report was created.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    data_end_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The end of a date and time range used for selecting the data to report.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    data_start_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The start of a date and time range used for selecting the data to report.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    marketplace_ids: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of marketplace identifiers for the report.
    """

    processing_end_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when the report processing completed, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_start_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when the report processing started, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_status: Union[
        Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]
    ] = attrs.field()
    """
    The processing status of the report.
    """

    report_document_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the report document. Pass this into the getReportDocument operation to get the information you will need to retrieve and decrypt the report document's contents.
    """

    report_id: str = attrs.field()
    """
    The identifier for the report. This identifier is unique only in combination with a seller ID.
    """

    report_schedule_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier of the report schedule that created this report (if any). This identifier is unique only in combination with a seller ID.
    """

    report_type: str = attrs.field()
    """
    The report type.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReportDocument:

    compression_algorithm: Optional[Union[Literal["GZIP"]]] = attrs.field(
        default=None,
    )
    """
    If present, the report document contents have been compressed with the provided algorithm.
    """

    encryption_details: "ReportDocumentEncryptionDetails" = attrs.field()
    """
    Encryption details required for decryption of a report document's contents.
    """

    report_document_id: str = attrs.field()
    """
    The identifier for the report document. This identifier is unique only in combination with a seller ID.
    """

    url: str = attrs.field()
    """
    A presigned URL for the report document. This URL expires after 5 minutes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReportDocumentEncryptionDetails:
    """
    Encryption details required for decryption of a report document's contents.
    """

    initialization_vector: str = attrs.field()
    """
    The vector to decrypt the document contents using Cipher Block Chaining (CBC).
    """

    key: str = attrs.field()
    """
    The encryption key used to decrypt the document contents.
    """

    standard: Union[Literal["AES"]] = attrs.field()
    """
    The encryption standard required to decrypt the document contents.
    """


@attrs.define(kw_only=True, frozen=True, slots=False)
class ReportOptions:
    """
    Additional information passed to reports. This varies by report type.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReportSchedule:
    """
    Detailed information about a report schedule.
    """

    marketplace_ids: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.
    """

    next_report_creation_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when the schedule will create its next report, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    period: str = attrs.field()
    """
    An ISO 8601 period value that indicates how often a report should be created.
    """

    report_options: Optional["ReportOptions"] = attrs.field(
        default=None,
    )
    """
    Additional information passed to reports. This varies by report type.
    """

    report_schedule_id: str = attrs.field()
    """
    The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
    """

    report_type: str = attrs.field()
    """
    The report type.
    """


class Reports20200904Client(BaseClient):
    def cancel_report(
        self,
        report_id: str,
    ) -> Union[CancelReportResponse]:
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
        url = "/reports/2020-09-04/reports/{reportId}"
        values = (report_id,)
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._cancel_report_params,
        )
        klass = self._cancel_report_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _cancel_report_params = (("reportId", "path"),)  # name, param in

    _cancel_report_responses = {
        200: CancelReportResponse,
        400: CancelReportResponse,
        401: CancelReportResponse,
        403: CancelReportResponse,
        404: CancelReportResponse,
        415: CancelReportResponse,
        429: CancelReportResponse,
        500: CancelReportResponse,
        503: CancelReportResponse,
    }

    def cancel_report_schedule(
        self,
        report_schedule_id: str,
    ) -> Union[CancelReportScheduleResponse]:
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
        url = "/reports/2020-09-04/schedules/{reportScheduleId}"
        values = (report_schedule_id,)
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._cancel_report_schedule_params,
        )
        klass = self._cancel_report_schedule_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _cancel_report_schedule_params = (("reportScheduleId", "path"),)  # name, param in

    _cancel_report_schedule_responses = {
        200: CancelReportScheduleResponse,
        400: CancelReportScheduleResponse,
        401: CancelReportScheduleResponse,
        403: CancelReportScheduleResponse,
        404: CancelReportScheduleResponse,
        415: CancelReportScheduleResponse,
        429: CancelReportScheduleResponse,
        500: CancelReportScheduleResponse,
        503: CancelReportScheduleResponse,
    }

    def create_report(
        self,
        marketplace_ids: List[str],
        report_type: str,
        data_end_time: datetime = None,
        data_start_time: datetime = None,
        report_options: Dict[str, Any] = None,
    ) -> Union[CreateReportResponse]:
        """
        Creates a report.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            data_end_time: The end of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.
            data_start_time: The start of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.
            marketplace_ids: A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.
            report_options: Additional information passed to reports. This varies by report type.
            report_type: The report type.
        """
        url = "/reports/2020-09-04/reports"
        values = (
            data_end_time,
            data_start_time,
            marketplace_ids,
            report_options,
            report_type,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_report_params,
        )
        klass = self._create_report_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_report_params = (  # name, param in
        ("dataEndTime", "body"),
        ("dataStartTime", "body"),
        ("marketplaceIds", "body"),
        ("reportOptions", "body"),
        ("reportType", "body"),
    )

    _create_report_responses = {
        202: CreateReportResponse,
        400: CreateReportResponse,
        401: CreateReportResponse,
        403: CreateReportResponse,
        404: CreateReportResponse,
        415: CreateReportResponse,
        429: CreateReportResponse,
        500: CreateReportResponse,
        503: CreateReportResponse,
    }

    def create_report_schedule(
        self,
        marketplace_ids: List[str],
        period: Union[
            Literal["PT5M"],
            Literal["PT15M"],
            Literal["PT30M"],
            Literal["PT1H"],
            Literal["PT2H"],
            Literal["PT4H"],
            Literal["PT8H"],
            Literal["PT12H"],
            Literal["P1D"],
            Literal["P2D"],
            Literal["P3D"],
            Literal["PT84H"],
            Literal["P7D"],
            Literal["P14D"],
            Literal["P15D"],
            Literal["P18D"],
            Literal["P30D"],
            Literal["P1M"],
        ],
        report_type: str,
        next_report_creation_time: datetime = None,
        report_options: Dict[str, Any] = None,
    ) -> Union[CreateReportScheduleResponse]:
        """
        Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_ids: A list of marketplace identifiers for the report schedule.
            next_report_creation_time: The date and time when the schedule will create its next report, in ISO 8601 date time format.
            period: One of a set of predefined ISO 8601 periods that specifies how often a report should be created.
            report_options: Additional information passed to reports. This varies by report type.
            report_type: The report type.
        """
        url = "/reports/2020-09-04/schedules"
        values = (
            marketplace_ids,
            next_report_creation_time,
            period,
            report_options,
            report_type,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_report_schedule_params,
        )
        klass = self._create_report_schedule_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_report_schedule_params = (  # name, param in
        ("marketplaceIds", "body"),
        ("nextReportCreationTime", "body"),
        ("period", "body"),
        ("reportOptions", "body"),
        ("reportType", "body"),
    )

    _create_report_schedule_responses = {
        201: CreateReportScheduleResponse,
        400: CreateReportScheduleResponse,
        401: CreateReportScheduleResponse,
        403: CreateReportScheduleResponse,
        404: CreateReportScheduleResponse,
        415: CreateReportScheduleResponse,
        429: CreateReportScheduleResponse,
        500: CreateReportScheduleResponse,
        503: CreateReportScheduleResponse,
    }

    def get_report(
        self,
        report_id: str,
    ) -> Union[GetReportResponse]:
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
        url = "/reports/2020-09-04/reports/{reportId}"
        values = (report_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_params,
        )
        klass = self._get_report_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_report_params = (("reportId", "path"),)  # name, param in

    _get_report_responses = {
        200: GetReportResponse,
        400: GetReportResponse,
        401: GetReportResponse,
        403: GetReportResponse,
        404: GetReportResponse,
        415: GetReportResponse,
        429: GetReportResponse,
        500: GetReportResponse,
        503: GetReportResponse,
    }

    def get_report_document(
        self,
        report_document_id: str,
    ) -> Union[GetReportDocumentResponse]:
        """
        Returns the information required for retrieving a report document's contents. This includes a presigned URL for the report document as well as the information required to decrypt the document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_document_id: The identifier for the report document.
        """
        url = "/reports/2020-09-04/documents/{reportDocumentId}"
        values = (report_document_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_document_params,
        )
        klass = self._get_report_document_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_report_document_params = (("reportDocumentId", "path"),)  # name, param in

    _get_report_document_responses = {
        200: GetReportDocumentResponse,
        400: GetReportDocumentResponse,
        401: GetReportDocumentResponse,
        403: GetReportDocumentResponse,
        404: GetReportDocumentResponse,
        415: GetReportDocumentResponse,
        429: GetReportDocumentResponse,
        500: GetReportDocumentResponse,
        503: GetReportDocumentResponse,
    }

    def get_report_schedule(
        self,
        report_schedule_id: str,
    ) -> Union[GetReportScheduleResponse]:
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
        url = "/reports/2020-09-04/schedules/{reportScheduleId}"
        values = (report_schedule_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_schedule_params,
        )
        klass = self._get_report_schedule_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_report_schedule_params = (("reportScheduleId", "path"),)  # name, param in

    _get_report_schedule_responses = {
        200: GetReportScheduleResponse,
        400: GetReportScheduleResponse,
        401: GetReportScheduleResponse,
        403: GetReportScheduleResponse,
        404: GetReportScheduleResponse,
        415: GetReportScheduleResponse,
        429: GetReportScheduleResponse,
        500: GetReportScheduleResponse,
        503: GetReportScheduleResponse,
    }

    def get_report_schedules(
        self,
        report_types: List[str],
    ) -> Union[GetReportSchedulesResponse]:
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
        url = "/reports/2020-09-04/schedules"
        values = (report_types,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_schedules_params,
        )
        klass = self._get_report_schedules_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_report_schedules_params = (("reportTypes", "query"),)  # name, param in

    _get_report_schedules_responses = {
        200: GetReportSchedulesResponse,
        400: GetReportSchedulesResponse,
        401: GetReportSchedulesResponse,
        403: GetReportSchedulesResponse,
        404: GetReportSchedulesResponse,
        415: GetReportSchedulesResponse,
        429: GetReportSchedulesResponse,
        500: GetReportSchedulesResponse,
        503: GetReportSchedulesResponse,
    }

    def get_reports(
        self,
        report_types: List[str] = None,
        processing_statuses: List[
            Union[Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]]
        ] = None,
        marketplace_ids: List[str] = None,
        page_size: int = None,
        created_since: datetime = None,
        created_until: datetime = None,
        next_token: str = None,
    ) -> Union[GetReportsResponse]:
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
        url = "/reports/2020-09-04/reports"
        values = (
            report_types,
            processing_statuses,
            marketplace_ids,
            page_size,
            created_since,
            created_until,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_reports_params,
        )
        klass = self._get_reports_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_reports_params = (  # name, param in
        ("reportTypes", "query"),
        ("processingStatuses", "query"),
        ("marketplaceIds", "query"),
        ("pageSize", "query"),
        ("createdSince", "query"),
        ("createdUntil", "query"),
        ("nextToken", "query"),
    )

    _get_reports_responses = {
        200: GetReportsResponse,
        400: GetReportsResponse,
        401: GetReportsResponse,
        403: GetReportsResponse,
        404: GetReportsResponse,
        415: GetReportsResponse,
        429: GetReportsResponse,
        500: GetReportsResponse,
        503: GetReportsResponse,
    }
