from .base import BaseClient as __BaseClient
from typing import List as _List


class ErrorList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error:
    def __init__(self, data):
        super().__init__()
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


class Report:
    def __init__(self, data):
        super().__init__()
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


class CreateReportScheduleSpecification:
    def __init__(self, data):
        super().__init__()
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


class CreateReportSpecification:
    def __init__(self, data):
        super().__init__()
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


class ReportOptions:
    def __init__(self, data):
        super().__init__()
        self.data = data


class ReportSchedule:
    def __init__(self, data):
        super().__init__()
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


class ReportScheduleList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportSchedules" in data:
            self.reportSchedules: _List[ReportSchedule] = [ReportSchedule(datum) for datum in data["reportSchedules"]]
        else:
            self.reportSchedules: _List[ReportSchedule] = []


class CreateReportResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportId" in data:
            self.reportId: str = str(data["reportId"])
        else:
            self.reportId: str = None


class GetReportsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reports" in data:
            self.reports: ReportList = ReportList(data["reports"])
        else:
            self.reports: ReportList = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class CreateReportScheduleResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None


class ReportDocument:
    def __init__(self, data):
        super().__init__()
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
        url = "/reports/2021-06-30/reports".format()
        params = {}
        if reportTypes is not None:
            params["reportTypes"] = ",".join(map(str, reportTypes))
        if processingStatuses is not None:
            params["processingStatuses"] = ",".join(map(str, processingStatuses))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if pageSize is not None:
            params["pageSize"] = (pageSize,)
        if createdSince is not None:
            params["createdSince"] = (createdSince,)
        if createdUntil is not None:
            params["createdUntil"] = (createdUntil,)
        if nextToken is not None:
            params["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetReportsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def createReport(
        self,
        data: CreateReportSpecification,
    ):
        url = "/reports/2021-06-30/reports".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: CreateReportResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def getReport(
        self,
        reportId: str,
    ):
        url = "/reports/2021-06-30/reports/{reportId}".format(
            reportId=reportId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: Report,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def cancelReport(
        self,
        reportId: str,
    ):
        url = "/reports/2021-06-30/reports/{reportId}".format(
            reportId=reportId,
        )
        params = {}
        response = self.request(url, method="DELETE", data=data.data)
        return {
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def getReportSchedules(
        self,
        reportTypes: _List[str],
    ):
        url = "/reports/2021-06-30/schedules".format()
        params = {}
        if reportTypes is not None:
            params["reportTypes"] = ",".join(map(str, reportTypes))
        response = self.request(url, method="GET", params=params)
        return {
            200: ReportScheduleList,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def createReportSchedule(
        self,
        data: CreateReportScheduleSpecification,
    ):
        url = "/reports/2021-06-30/schedules".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateReportScheduleResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def getReportSchedule(
        self,
        reportScheduleId: str,
    ):
        url = "/reports/2021-06-30/schedules/{reportScheduleId}".format(
            reportScheduleId=reportScheduleId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: ReportSchedule,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def cancelReportSchedule(
        self,
        reportScheduleId: str,
    ):
        url = "/reports/2021-06-30/schedules/{reportScheduleId}".format(
            reportScheduleId=reportScheduleId,
        )
        params = {}
        response = self.request(url, method="DELETE", data=data.data)
        return {
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def getReportDocument(
        self,
        reportDocumentId: str,
    ):
        url = "/reports/2021-06-30/documents/{reportDocumentId}".format(
            reportDocumentId=reportDocumentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: ReportDocument,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())
