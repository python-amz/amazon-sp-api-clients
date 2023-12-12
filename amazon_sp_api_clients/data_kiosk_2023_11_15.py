from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class ErrorList(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class Query(__BaseDictObject):
    """
    Detailed information about the query.
    """

    def __init__(self, data):
        super().__init__(data)
        if "queryId" in data:
            self.queryId: str = self._get_value(str, "queryId")
        else:
            self.queryId: str = None
        if "query" in data:
            self.query: str = self._get_value(str, "query")
        else:
            self.query: str = None
        if "createdTime" in data:
            self.createdTime: str = self._get_value(str, "createdTime")
        else:
            self.createdTime: str = None
        if "processingStatus" in data:
            self.processingStatus: str = self._get_value(str, "processingStatus")
        else:
            self.processingStatus: str = None
        if "processingStartTime" in data:
            self.processingStartTime: str = self._get_value(str, "processingStartTime")
        else:
            self.processingStartTime: str = None
        if "processingEndTime" in data:
            self.processingEndTime: str = self._get_value(str, "processingEndTime")
        else:
            self.processingEndTime: str = None
        if "dataDocumentId" in data:
            self.dataDocumentId: str = self._get_value(str, "dataDocumentId")
        else:
            self.dataDocumentId: str = None
        if "errorDocumentId" in data:
            self.errorDocumentId: str = self._get_value(str, "errorDocumentId")
        else:
            self.errorDocumentId: str = None
        if "pagination" in data:
            self.pagination: dict = self._get_value(dict, "pagination")
        else:
            self.pagination: dict = None


class CreateQuerySpecification(__BaseDictObject):
    """
    Information required to create the query.
    """

    def __init__(self, data):
        super().__init__(data)
        if "query" in data:
            self.query: str = self._get_value(str, "query")
        else:
            self.query: str = None
        if "paginationToken" in data:
            self.paginationToken: str = self._get_value(str, "paginationToken")
        else:
            self.paginationToken: str = None


class CreateQueryResponse(__BaseDictObject):
    """
    The response for the `createQuery` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "queryId" in data:
            self.queryId: str = self._get_value(str, "queryId")
        else:
            self.queryId: str = None


class GetQueriesResponse(__BaseDictObject):
    """
    The response for the `getQueries` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "queries" in data:
            self.queries: QueryList = self._get_value(QueryList, "queries")
        else:
            self.queries: QueryList = None
        if "pagination" in data:
            self.pagination: dict = self._get_value(dict, "pagination")
        else:
            self.pagination: dict = None


class GetDocumentResponse(__BaseDictObject):
    """
    The response for the `getDocument` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "documentId" in data:
            self.documentId: str = self._get_value(str, "documentId")
        else:
            self.documentId: str = None
        if "documentUrl" in data:
            self.documentUrl: str = self._get_value(str, "documentUrl")
        else:
            self.documentUrl: str = None


class QueryList(list, _List["Query"]):
    """
    A list of queries.
    """

    def __init__(self, data):
        super().__init__([Query(datum) for datum in data])
        self.data = data


class DataKiosk20231115Client(__BaseClient):
    def getQueries(
        self,
        processingStatuses: _List[str] = None,
        pageSize: int = None,
        createdSince: str = None,
        createdUntil: str = None,
        paginationToken: str = None,
    ):
        """
                Returns details for the Data Kiosk queries that match the specified filters. See the `createQuery` operation for details about query retention.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/dataKiosk/2023-11-15/queries"
        params = {}
        if processingStatuses is not None:
            params["processingStatuses"] = ",".join(map(str, processingStatuses))
        if pageSize is not None:
            params["pageSize"] = pageSize
        if createdSince is not None:
            params["createdSince"] = createdSince
        if createdUntil is not None:
            params["createdUntil"] = createdUntil
        if paginationToken is not None:
            params["paginationToken"] = paginationToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetQueriesResponse,
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

    def createQuery(
        self,
        data: CreateQuerySpecification,
    ):
        """
                Creates a Data Kiosk query request.
        **Note:** The retention of a query varies based on the fields requested. Each field within a schema is annotated with a `@resultRetention` directive that defines how long a query containing that field will be retained. When a query contains multiple fields with different retentions, the shortest (minimum) retention is applied. The retention of a query's resulting documents always matches the retention of the query.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/dataKiosk/2023-11-15/queries"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: CreateQueryResponse,
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

    def getQuery(
        self,
        queryId: str,
    ):
        """
                Returns query details for the query specified by the `queryId` parameter. See the `createQuery` operation for details about query retention.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/dataKiosk/2023-11-15/queries/{queryId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: Query,
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

    def cancelQuery(
        self,
        queryId: str,
    ):
        """
                Cancels the query specified by the `queryId` parameter. Only queries with a non-terminal `processingStatus` (`IN_QUEUE`, `IN_PROGRESS`) can be cancelled. Cancelling a query that already has a `processingStatus` of `CANCELLED` will no-op. Cancelled queries are returned in subsequent calls to the `getQuery` and `getQueries` operations.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/dataKiosk/2023-11-15/queries/{queryId}"
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

    def getDocument(
        self,
        documentId: str,
    ):
        """
                Returns the information required for retrieving a Data Kiosk document's contents. See the `createQuery` operation for details about document retention.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/dataKiosk/2023-11-15/documents/{documentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetDocumentResponse,
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
