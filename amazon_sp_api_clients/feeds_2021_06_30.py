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


class ErrorList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class CreateFeedResponse:
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
        if "feeds" in data:
            self.feeds: FeedList = FeedList(data["feeds"])
        else:
            self.feeds: FeedList = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


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
        if "compressionAlgorithm" in data:
            self.compressionAlgorithm: str = str(data["compressionAlgorithm"])
        else:
            self.compressionAlgorithm: str = None


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
        if "feedDocumentId" in data:
            self.feedDocumentId: str = str(data["feedDocumentId"])
        else:
            self.feedDocumentId: str = None
        if "url" in data:
            self.url: str = str(data["url"])
        else:
            self.url: str = None


class FeedList(list, _List["Feed"]):
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
        url = "/feeds/2021-06-30/feeds".format()
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
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def createFeed(
        self,
        data: CreateFeedSpecification,
    ):
        url = "/feeds/2021-06-30/feeds".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: CreateFeedResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def getFeed(
        self,
        feedId: str,
    ):
        url = "/feeds/2021-06-30/feeds/{feedId}".format(
            feedId=feedId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: Feed,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def cancelFeed(
        self,
        feedId: str,
    ):
        url = "/feeds/2021-06-30/feeds/{feedId}".format(
            feedId=feedId,
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
        }[response.status_code](self.__get_response_json(response))

    def createFeedDocument(
        self,
        data: CreateFeedDocumentSpecification,
    ):
        url = "/feeds/2021-06-30/documents".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateFeedDocumentResponse,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def getFeedDocument(
        self,
        feedDocumentId: str,
    ):
        url = "/feeds/2021-06-30/documents/{feedDocumentId}".format(
            feedDocumentId=feedDocumentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: FeedDocument,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))
