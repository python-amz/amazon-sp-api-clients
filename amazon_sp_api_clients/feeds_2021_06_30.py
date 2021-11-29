from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class Error:
    """
    An error response returned when the request is unsuccessful.
    """

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


class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class CreateFeedResponse:
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feedId" in data:
            self.feedId: str = str(data["feedId"])
        else:
            self.feedId: str = None


class Feed:
    """
    Detailed information about the feed.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feedId" in data:
            self.feedId: str = str(data["feedId"])
        else:
            self.feedId: str = None
        if "feedType" in data:
            self.feedType: str = str(data["feedType"])
        else:
            self.feedType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
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
        if "resultFeedDocumentId" in data:
            self.resultFeedDocumentId: str = str(data["resultFeedDocumentId"])
        else:
            self.resultFeedDocumentId: str = None


class GetFeedsResponse:
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feeds" in data:
            self.feeds: FeedList = FeedList(data["feeds"])
        else:
            self.feeds: FeedList = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class FeedDocument:
    """
    Information required for the feed document.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feedDocumentId" in data:
            self.feedDocumentId: str = str(data["feedDocumentId"])
        else:
            self.feedDocumentId: str = None
        if "url" in data:
            self.url: str = str(data["url"])
        else:
            self.url: str = None
        if "compressionAlgorithm" in data:
            self.compressionAlgorithm: str = str(data["compressionAlgorithm"])
        else:
            self.compressionAlgorithm: str = None


class FeedOptions:
    """
    Additional options to control the feed. These vary by feed type.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data


class CreateFeedSpecification:
    """
    Information required to create the feed.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feedType" in data:
            self.feedType: str = str(data["feedType"])
        else:
            self.feedType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "inputFeedDocumentId" in data:
            self.inputFeedDocumentId: str = str(data["inputFeedDocumentId"])
        else:
            self.inputFeedDocumentId: str = None
        if "feedOptions" in data:
            self.feedOptions: FeedOptions = FeedOptions(data["feedOptions"])
        else:
            self.feedOptions: FeedOptions = None


class CreateFeedDocumentSpecification:
    """
    Specifies the content type for the createFeedDocument operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentType" in data:
            self.contentType: str = str(data["contentType"])
        else:
            self.contentType: str = None


class CreateFeedDocumentResponse:
    """
    Information required to upload a feed document's contents.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feedDocumentId" in data:
            self.feedDocumentId: str = str(data["feedDocumentId"])
        else:
            self.feedDocumentId: str = None
        if "url" in data:
            self.url: str = str(data["url"])
        else:
            self.url: str = None


class FeedList(list, _List["Feed"]):
    """
    A list of feeds.
    """

    def __init__(self, data):
        super().__init__([Feed(datum) for datum in data])
        self.data = data


class Feeds20210630Client(__BaseClient):
    def getFeeds(
        self,
        feedTypes: _List[str] = None,
        marketplaceIds: _List[str] = None,
        pageSize: int = None,
        processingStatuses: _List[str] = None,
        createdSince: str = None,
        createdUntil: str = None,
        nextToken: str = None,
    ):
        """
                Returns feed details for the feeds that match the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2021-06-30/feeds"
        params = {}
        if feedTypes is not None:
            params["feedTypes"] = ",".join(map(str, feedTypes))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if pageSize is not None:
            params["pageSize"] = pageSize
        if processingStatuses is not None:
            params["processingStatuses"] = ",".join(map(str, processingStatuses))
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
            200: GetFeedsResponse,
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

    def createFeed(
        self,
        data: CreateFeedSpecification,
    ):
        """
                Creates a feed. Upload the contents of the feed document before calling this operation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2021-06-30/feeds"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: CreateFeedResponse,
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

    def getFeed(
        self,
        feedId: str,
    ):
        """
                Returns feed details (including the resultDocumentId, if available) for the feed that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2021-06-30/feeds/{feedId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: Feed,
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

    def cancelFeed(
        self,
        feedId: str,
    ):
        """
                Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled. Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2021-06-30/feeds/{feedId}"
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

    def createFeedDocument(
        self,
        data: CreateFeedDocumentSpecification,
    ):
        """
                Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2021-06-30/documents"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateFeedDocumentResponse,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getFeedDocument(
        self,
        feedDocumentId: str,
    ):
        """
                Returns the information required for retrieving a feed document's contents.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2021-06-30/documents/{feedDocumentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: FeedDocument,
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
