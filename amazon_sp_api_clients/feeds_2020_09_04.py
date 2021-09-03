from .base import BaseClient as __BaseClient
from typing import List as _List


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


class CancelFeedResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateFeedResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feedId" in data:
            self.feedId: str = str(data["feedId"])
        else:
            self.feedId: str = None


class Feed:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: FeedList = FeedList(data["payload"])
        else:
            self.payload: FeedList = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetFeedResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Feed = Feed(data["payload"])
        else:
            self.payload: Feed = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class FeedDocumentEncryptionDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "standard" in data:
            self.standard: str = str(data["standard"])
        else:
            self.standard: str = None
        if "initializationVector" in data:
            self.initializationVector: str = str(data["initializationVector"])
        else:
            self.initializationVector: str = None
        if "key" in data:
            self.key: str = str(data["key"])
        else:
            self.key: str = None


class FeedDocument:
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
        if "encryptionDetails" in data:
            self.encryptionDetails: FeedDocumentEncryptionDetails = FeedDocumentEncryptionDetails(
                data["encryptionDetails"]
            )
        else:
            self.encryptionDetails: FeedDocumentEncryptionDetails = None
        if "compressionAlgorithm" in data:
            self.compressionAlgorithm: str = str(data["compressionAlgorithm"])
        else:
            self.compressionAlgorithm: str = None


class GetFeedDocumentResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: FeedDocument = FeedDocument(data["payload"])
        else:
            self.payload: FeedDocument = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateFeedResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateFeedResult = CreateFeedResult(data["payload"])
        else:
            self.payload: CreateFeedResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class FeedOptions:
    def __init__(self, data):
        super().__init__()
        self.data = data


class CreateFeedSpecification:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentType" in data:
            self.contentType: str = str(data["contentType"])
        else:
            self.contentType: str = None


class CreateFeedDocumentResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateFeedDocumentResult = CreateFeedDocumentResult(data["payload"])
        else:
            self.payload: CreateFeedDocumentResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateFeedDocumentResult:
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
        if "encryptionDetails" in data:
            self.encryptionDetails: FeedDocumentEncryptionDetails = FeedDocumentEncryptionDetails(
                data["encryptionDetails"]
            )
        else:
            self.encryptionDetails: FeedDocumentEncryptionDetails = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class FeedList(list, _List["Feed"]):
    def __init__(self, data):
        super().__init__([Feed(datum) for datum in data])
        self.data = data


class Feeds20200904Client(__BaseClient):
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
        url = "/feeds/2020-09-04/feeds".format()
        params = {}
        if feedTypes is not None:
            params["feedTypes"] = ",".join(map(str, feedTypes))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if pageSize is not None:
            params["pageSize"] = (pageSize,)
        if processingStatuses is not None:
            params["processingStatuses"] = ",".join(map(str, processingStatuses))
        if createdSince is not None:
            params["createdSince"] = (createdSince,)
        if createdUntil is not None:
            params["createdUntil"] = (createdUntil,)
        if nextToken is not None:
            params["nextToken"] = (nextToken,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFeedsResponse,
            400: GetFeedsResponse,
            401: GetFeedsResponse,
            403: GetFeedsResponse,
            404: GetFeedsResponse,
            415: GetFeedsResponse,
            429: GetFeedsResponse,
            500: GetFeedsResponse,
            503: GetFeedsResponse,
        }[response.status_code](self._get_response_json(response))

    def createFeed(
        self,
        data: CreateFeedSpecification,
    ):
        url = "/feeds/2020-09-04/feeds".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: CreateFeedResponse,
            400: CreateFeedResponse,
            401: CreateFeedResponse,
            403: CreateFeedResponse,
            404: CreateFeedResponse,
            415: CreateFeedResponse,
            429: CreateFeedResponse,
            500: CreateFeedResponse,
            503: CreateFeedResponse,
        }[response.status_code](self._get_response_json(response))

    def getFeed(
        self,
        feedId: str,
    ):
        url = "/feeds/2020-09-04/feeds/{feedId}".format(
            feedId=feedId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFeedResponse,
            400: GetFeedResponse,
            401: GetFeedResponse,
            403: GetFeedResponse,
            404: GetFeedResponse,
            415: GetFeedResponse,
            429: GetFeedResponse,
            500: GetFeedResponse,
            503: GetFeedResponse,
        }[response.status_code](self._get_response_json(response))

    def cancelFeed(
        self,
        feedId: str,
    ):
        url = "/feeds/2020-09-04/feeds/{feedId}".format(
            feedId=feedId,
        )
        params = {}
        response = self.request(url, method="DELETE", data=data.data)
        return {
            200: CancelFeedResponse,
            400: CancelFeedResponse,
            401: CancelFeedResponse,
            403: CancelFeedResponse,
            404: CancelFeedResponse,
            415: CancelFeedResponse,
            429: CancelFeedResponse,
            500: CancelFeedResponse,
            503: CancelFeedResponse,
        }[response.status_code](self._get_response_json(response))

    def createFeedDocument(
        self,
        data: CreateFeedDocumentSpecification,
    ):
        url = "/feeds/2020-09-04/documents".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateFeedDocumentResponse,
            400: CreateFeedDocumentResponse,
            403: CreateFeedDocumentResponse,
            404: CreateFeedDocumentResponse,
            413: CreateFeedDocumentResponse,
            415: CreateFeedDocumentResponse,
            429: CreateFeedDocumentResponse,
            500: CreateFeedDocumentResponse,
            503: CreateFeedDocumentResponse,
        }[response.status_code](self._get_response_json(response))

    def getFeedDocument(
        self,
        feedDocumentId: str,
    ):
        url = "/feeds/2020-09-04/documents/{feedDocumentId}".format(
            feedDocumentId=feedDocumentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetFeedDocumentResponse,
            400: GetFeedDocumentResponse,
            401: GetFeedDocumentResponse,
            403: GetFeedDocumentResponse,
            404: GetFeedDocumentResponse,
            415: GetFeedDocumentResponse,
            429: GetFeedDocumentResponse,
            500: GetFeedDocumentResponse,
            503: GetFeedDocumentResponse,
        }[response.status_code](self._get_response_json(response))
