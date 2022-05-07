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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_report_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateReportResponse(**data)

    report_id: str = attrs.field()
    """
    The identifier for the report. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportScheduleResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_report_schedule_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateReportScheduleResponse(**data)

    report_schedule_id: str = attrs.field()
    """
    The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReportScheduleSpecification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_report_schedule_specification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateReportScheduleSpecification(**data)

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
    """
    Information required to create the report.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_report_specification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateReportSpecification(**data)

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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

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
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_list_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ErrorList(**data)

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetReportsResponse:
    """
    The response for the getReports operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_reports_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetReportsResponse(**data)

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    Returned when the number of results exceeds pageSize. To get the next page of results, call getReports with this token as the only parameter.
    """

    reports: List["Report"] = attrs.field()
    """
    A list of reports.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Report:
    """
    Detailed information about the report.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _report_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Report(**data)

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
    The identifier for the report document. Pass this into the getReportDocument operation to get the information you will need to retrieve the report document's contents.
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
    """
    Information required for the report document.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _report_document_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ReportDocument(**data)

    compression_algorithm: Optional[Union[Literal["GZIP"]]] = attrs.field(
        default=None,
    )
    """
    If present, the report document contents have been compressed with the provided algorithm.
    """

    report_document_id: str = attrs.field()
    """
    The identifier for the report document. This identifier is unique only in combination with a seller ID.
    """

    url: str = attrs.field()
    """
    A presigned URL for the report document. This URL expires after 5 minutes.
    """


@attrs.define(kw_only=True, frozen=True, slots=False)
class ReportOptions:
    """
    Additional information passed to reports. This varies by report type.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _report_options_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ReportOptions(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReportSchedule:
    """
    Detailed information about a report schedule.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _report_schedule_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ReportSchedule(**data)

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


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReportScheduleList:
    """
    A list of report schedules.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _report_schedule_list_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ReportScheduleList(**data)

    report_schedules: List["ReportSchedule"] = attrs.field()


_create_report_response_name_convert = {
    "reportId": "report_id",
}

_create_report_schedule_response_name_convert = {
    "reportScheduleId": "report_schedule_id",
}

_create_report_schedule_specification_name_convert = {
    "marketplaceIds": "marketplace_ids",
    "nextReportCreationTime": "next_report_creation_time",
    "period": "period",
    "reportOptions": "report_options",
    "reportType": "report_type",
}

_create_report_specification_name_convert = {
    "dataEndTime": "data_end_time",
    "dataStartTime": "data_start_time",
    "marketplaceIds": "marketplace_ids",
    "reportOptions": "report_options",
    "reportType": "report_type",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_get_reports_response_name_convert = {
    "nextToken": "next_token",
    "reports": "reports",
}

_report_name_convert = {
    "createdTime": "created_time",
    "dataEndTime": "data_end_time",
    "dataStartTime": "data_start_time",
    "marketplaceIds": "marketplace_ids",
    "processingEndTime": "processing_end_time",
    "processingStartTime": "processing_start_time",
    "processingStatus": "processing_status",
    "reportDocumentId": "report_document_id",
    "reportId": "report_id",
    "reportScheduleId": "report_schedule_id",
    "reportType": "report_type",
}

_report_document_name_convert = {
    "compressionAlgorithm": "compression_algorithm",
    "reportDocumentId": "report_document_id",
    "url": "url",
}

_report_options_name_convert = {}

_report_schedule_name_convert = {
    "marketplaceIds": "marketplace_ids",
    "nextReportCreationTime": "next_report_creation_time",
    "period": "period",
    "reportOptions": "report_options",
    "reportScheduleId": "report_schedule_id",
    "reportType": "report_type",
}

_report_schedule_list_name_convert = {
    "reportSchedules": "report_schedules",
}


class Reports20210630Client(BaseClient):
    def cancel_report(
        self,
        report_id: str,
    ) -> Union[ErrorList]:
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
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._cancel_report_params,
            self._cancel_report_responses,
        )
        return response

    _cancel_report_params = (("reportId", "path"),)  # name, param in

    _cancel_report_responses = {
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def cancel_report_schedule(
        self,
        report_schedule_id: str,
    ) -> Union[ErrorList]:
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
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._cancel_report_schedule_params,
            self._cancel_report_schedule_responses,
        )
        return response

    _cancel_report_schedule_params = (("reportScheduleId", "path"),)  # name, param in

    _cancel_report_schedule_responses = {
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def create_report(
        self,
        marketplace_ids: List[str],
        report_type: str,
        data_end_time: datetime = None,
        data_start_time: datetime = None,
        report_options: Dict[str, Any] = None,
    ) -> Union[CreateReportResponse, ErrorList]:
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
        url = "/reports/2021-06-30/reports"
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
            self._create_report_responses,
        )
        return response

    _create_report_params = (  # name, param in
        ("dataEndTime", "body"),
        ("dataStartTime", "body"),
        ("marketplaceIds", "body"),
        ("reportOptions", "body"),
        ("reportType", "body"),
    )

    _create_report_responses = {
        202: CreateReportResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
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
    ) -> Union[CreateReportScheduleResponse, ErrorList]:
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
        url = "/reports/2021-06-30/schedules"
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
            self._create_report_schedule_responses,
        )
        return response

    _create_report_schedule_params = (  # name, param in
        ("marketplaceIds", "body"),
        ("nextReportCreationTime", "body"),
        ("period", "body"),
        ("reportOptions", "body"),
        ("reportType", "body"),
    )

    _create_report_schedule_responses = {
        201: CreateReportScheduleResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_report(
        self,
        report_id: str,
    ) -> Union[ErrorList, Report]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_params,
            self._get_report_responses,
        )
        return response

    _get_report_params = (("reportId", "path"),)  # name, param in

    _get_report_responses = {
        200: Report,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_report_document(
        self,
        report_document_id: str,
    ) -> Union[ErrorList, ReportDocument]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_document_params,
            self._get_report_document_responses,
        )
        return response

    _get_report_document_params = (("reportDocumentId", "path"),)  # name, param in

    _get_report_document_responses = {
        200: ReportDocument,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_report_schedule(
        self,
        report_schedule_id: str,
    ) -> Union[ErrorList, ReportSchedule]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_schedule_params,
            self._get_report_schedule_responses,
        )
        return response

    _get_report_schedule_params = (("reportScheduleId", "path"),)  # name, param in

    _get_report_schedule_responses = {
        200: ReportSchedule,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_report_schedules(
        self,
        report_types: List[str],
    ) -> Union[ErrorList, ReportScheduleList]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_report_schedules_params,
            self._get_report_schedules_responses,
        )
        return response

    _get_report_schedules_params = (("reportTypes", "query"),)  # name, param in

    _get_report_schedules_responses = {
        200: ReportScheduleList,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
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
    ) -> Union[ErrorList, GetReportsResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_reports_params,
            self._get_reports_responses,
        )
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

    _get_reports_responses = {
        200: GetReportsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
