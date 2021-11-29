from .base import BaseClient as __BaseClient, convert_bool, BaseObject as __BaseObject
from typing import List as _List


class ErrorList(__BaseObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error(__BaseObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
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


class Report(__BaseObject):
    """
    Detailed information about the report.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "reportId" in data:
            self.reportId: str = str(data["reportId"])
        else:
            self.reportId: str = None
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "dataStartTime" in data:
            self.dataStartTime: str = str(data["dataStartTime"])
        else:
            self.dataStartTime: str = None
        if "dataEndTime" in data:
            self.dataEndTime: str = str(data["dataEndTime"])
        else:
            self.dataEndTime: str = None
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None
        if "createdTime" in data:
            self.createdTime: str = str(data["createdTime"])
        else:
            self.createdTime: str = None
        if "processingStatus" in data:
            self.processingStatus: str = str(data["processingStatus"])
        else:
            self.processingStatus: str = None
        if "processingStartTime" in data:
            self.processingStartTime: str = str(data["processingStartTime"])
        else:
            self.processingStartTime: str = None
        if "processingEndTime" in data:
            self.processingEndTime: str = str(data["processingEndTime"])
        else:
            self.processingEndTime: str = None
        if "reportDocumentId" in data:
            self.reportDocumentId: str = str(data["reportDocumentId"])
        else:
            self.reportDocumentId: str = None


class CreateReportScheduleSpecification(__BaseObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "reportOptions" in data:
            self.reportOptions: ReportOptions = ReportOptions(data["reportOptions"])
        else:
            self.reportOptions: ReportOptions = None
        if "period" in data:
            self.period: str = str(data["period"])
        else:
            self.period: str = None
        if "nextReportCreationTime" in data:
            self.nextReportCreationTime: str = str(data["nextReportCreationTime"])
        else:
            self.nextReportCreationTime: str = None


class CreateReportSpecification(__BaseObject):
    """
    Information required to create the report.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportOptions" in data:
            self.reportOptions: ReportOptions = ReportOptions(data["reportOptions"])
        else:
            self.reportOptions: ReportOptions = None
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "dataStartTime" in data:
            self.dataStartTime: str = str(data["dataStartTime"])
        else:
            self.dataStartTime: str = None
        if "dataEndTime" in data:
            self.dataEndTime: str = str(data["dataEndTime"])
        else:
            self.dataEndTime: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []


class ReportOptions(__BaseObject):
    """
    Additional information passed to reports. This varies by report type.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data


class ReportSchedule(__BaseObject):
    """
    Detailed information about a report schedule.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "reportOptions" in data:
            self.reportOptions: ReportOptions = ReportOptions(data["reportOptions"])
        else:
            self.reportOptions: ReportOptions = None
        if "period" in data:
            self.period: str = str(data["period"])
        else:
            self.period: str = None
        if "nextReportCreationTime" in data:
            self.nextReportCreationTime: str = str(data["nextReportCreationTime"])
        else:
            self.nextReportCreationTime: str = None


class ReportScheduleList(__BaseObject):
    """
    A list of report schedules.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportSchedules" in data:
            self.reportSchedules: _List[ReportSchedule] = [ReportSchedule(datum) for datum in data["reportSchedules"]]
        else:
            self.reportSchedules: _List[ReportSchedule] = []


class CreateReportResponse(__BaseObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportId" in data:
            self.reportId: str = str(data["reportId"])
        else:
            self.reportId: str = None


class GetReportsResponse(__BaseObject):
    """
    The response for the getReports operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reports" in data:
            self.reports: ReportList = ReportList(data["reports"])
        else:
            self.reports: ReportList = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class CreateReportScheduleResponse(__BaseObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None


class ReportDocument(__BaseObject):
    """
    Information required for the report document.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "reportDocumentId" in data:
            self.reportDocumentId: str = str(data["reportDocumentId"])
        else:
            self.reportDocumentId: str = None
        if "url" in data:
            self.url: str = str(data["url"])
        else:
            self.url: str = None
        if "compressionAlgorithm" in data:
            self.compressionAlgorithm: str = str(data["compressionAlgorithm"])
        else:
            self.compressionAlgorithm: str = None


class ReportList(list, _List["Report"]):
    """
    A list of reports.
    """

    def __init__(self, data):
        super().__init__([Report(datum) for datum in data])
        self.data = data


class Reports20210630Client(__BaseClient):
    def getReports(
        self,
        reportTypes: _List[str] = None,
        processingStatuses: _List[str] = None,
        marketplaceIds: _List[str] = None,
        pageSize: int = None,
        createdSince: str = None,
        createdUntil: str = None,
        nextToken: str = None,
    ):
        """
                Returns report details for the reports that match the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/reports"
        params = {}
        if reportTypes is not None:
            params["reportTypes"] = ",".join(map(str, reportTypes))
        if processingStatuses is not None:
            params["processingStatuses"] = ",".join(map(str, processingStatuses))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if pageSize is not None:
            params["pageSize"] = pageSize
        if createdSince is not None:
            params["createdSince"] = createdSince
        if createdUntil is not None:
            params["createdUntil"] = createdUntil
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetReportsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createReport(
        self,
        data: CreateReportSpecification,
    ):
        """
                Creates a report.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/reports"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: CreateReportResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getReport(
        self,
        reportId: str,
    ):
        """
                Returns report details (including the reportDocumentId, if available) for the report that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/reports/{reportId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: Report,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelReport(
        self,
        reportId: str,
    ):
        """
                Cancels the report that you specify. Only reports with processingStatus=IN_QUEUE can be cancelled. Cancelled reports are returned in subsequent calls to the getReport and getReports operations.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/reports/{reportId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            200: None,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getReportSchedules(
        self,
        reportTypes: _List[str],
    ):
        """
                Returns report schedule details that match the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/schedules"
        params = {}
        if reportTypes is not None:
            params["reportTypes"] = ",".join(map(str, reportTypes))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ReportScheduleList,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createReportSchedule(
        self,
        data: CreateReportScheduleSpecification,
    ):
        """
                Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/schedules"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateReportScheduleResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getReportSchedule(
        self,
        reportScheduleId: str,
    ):
        """
                Returns report schedule details for the report schedule that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/schedules/{reportScheduleId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ReportSchedule,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelReportSchedule(
        self,
        reportScheduleId: str,
    ):
        """
                Cancels the report schedule that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/schedules/{reportScheduleId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            200: None,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getReportDocument(
        self,
        reportDocumentId: str,
    ):
        """
                Returns the information required for retrieving a report document's contents.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2021-06-30/documents/{reportDocumentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ReportDocument,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
