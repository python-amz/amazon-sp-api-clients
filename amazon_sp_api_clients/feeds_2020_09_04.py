from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class Error(__BaseDictObject):
    """
    An error response returned when the request is unsuccessful.
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


class CancelFeedResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateFeedResult(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "feedId" in data:
            self.feedId: str = self._get_value(str, "feedId")
        else:
            self.feedId: str = None


class Feed(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "feedId" in data:
            self.feedId: str = self._get_value(str, "feedId")
        else:
            self.feedId: str = None
        if "feedType" in data:
            self.feedType: str = self._get_value(str, "feedType")
        else:
            self.feedType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
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
        if "resultFeedDocumentId" in data:
            self.resultFeedDocumentId: str = self._get_value(str, "resultFeedDocumentId")
        else:
            self.resultFeedDocumentId: str = None


class GetFeedsResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: FeedList = self._get_value(FeedList, "payload")
        else:
            self.payload: FeedList = None
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetFeedResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Feed = self._get_value(Feed, "payload")
        else:
            self.payload: Feed = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class FeedDocumentEncryptionDetails(__BaseDictObject):
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    def __init__(self, data):
        super().__init__(data)
        if "standard" in data:
            self.standard: str = self._get_value(str, "standard")
        else:
            self.standard: str = None
        if "initializationVector" in data:
            self.initializationVector: str = self._get_value(str, "initializationVector")
        else:
            self.initializationVector: str = None
        if "key" in data:
            self.key: str = self._get_value(str, "key")
        else:
            self.key: str = None


class FeedDocument(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "feedDocumentId" in data:
            self.feedDocumentId: str = self._get_value(str, "feedDocumentId")
        else:
            self.feedDocumentId: str = None
        if "url" in data:
            self.url: str = self._get_value(str, "url")
        else:
            self.url: str = None
        if "encryptionDetails" in data:
            self.encryptionDetails: FeedDocumentEncryptionDetails = self._get_value(
                FeedDocumentEncryptionDetails, "encryptionDetails"
            )
        else:
            self.encryptionDetails: FeedDocumentEncryptionDetails = None
        if "compressionAlgorithm" in data:
            self.compressionAlgorithm: str = self._get_value(str, "compressionAlgorithm")
        else:
            self.compressionAlgorithm: str = None


class GetFeedDocumentResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: FeedDocument = self._get_value(FeedDocument, "payload")
        else:
            self.payload: FeedDocument = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateFeedResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CreateFeedResult = self._get_value(CreateFeedResult, "payload")
        else:
            self.payload: CreateFeedResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class FeedOptions(__BaseDictObject):
    """
    Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
    """

    def __init__(self, data):
        super().__init__(data)


class CreateFeedSpecification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "feedType" in data:
            self.feedType: str = self._get_value(str, "feedType")
        else:
            self.feedType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "inputFeedDocumentId" in data:
            self.inputFeedDocumentId: str = self._get_value(str, "inputFeedDocumentId")
        else:
            self.inputFeedDocumentId: str = None
        if "feedOptions" in data:
            self.feedOptions: FeedOptions = self._get_value(FeedOptions, "feedOptions")
        else:
            self.feedOptions: FeedOptions = None


class CreateFeedDocumentSpecification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "contentType" in data:
            self.contentType: str = self._get_value(str, "contentType")
        else:
            self.contentType: str = None


class CreateFeedDocumentResponse(__BaseDictObject):
    """
    The response for the createFeedDocument operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CreateFeedDocumentResult = self._get_value(CreateFeedDocumentResult, "payload")
        else:
            self.payload: CreateFeedDocumentResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateFeedDocumentResult(__BaseDictObject):
    """
    Information required to encrypt and upload a feed document's contents.
    """

    def __init__(self, data):
        super().__init__(data)
        if "feedDocumentId" in data:
            self.feedDocumentId: str = self._get_value(str, "feedDocumentId")
        else:
            self.feedDocumentId: str = None
        if "url" in data:
            self.url: str = self._get_value(str, "url")
        else:
            self.url: str = None
        if "encryptionDetails" in data:
            self.encryptionDetails: FeedDocumentEncryptionDetails = self._get_value(
                FeedDocumentEncryptionDetails, "encryptionDetails"
            )
        else:
            self.encryptionDetails: FeedDocumentEncryptionDetails = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class FeedList(list, _List["Feed"]):
    """ """

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
        """
                Returns feed details for the feeds that match the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2020-09-04/feeds"
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
            400: GetFeedsResponse,
            401: GetFeedsResponse,
            403: GetFeedsResponse,
            404: GetFeedsResponse,
            415: GetFeedsResponse,
            429: GetFeedsResponse,
            500: GetFeedsResponse,
            503: GetFeedsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createFeed(
        self,
        data: CreateFeedSpecification,
    ):
        """
                Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2020-09-04/feeds"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: CreateFeedResponse,
            400: CreateFeedResponse,
            401: CreateFeedResponse,
            403: CreateFeedResponse,
            404: CreateFeedResponse,
            415: CreateFeedResponse,
            429: CreateFeedResponse,
            500: CreateFeedResponse,
            503: CreateFeedResponse,
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
        url = f"/feeds/2020-09-04/feeds/{feedId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetFeedResponse,
            400: GetFeedResponse,
            401: GetFeedResponse,
            403: GetFeedResponse,
            404: GetFeedResponse,
            415: GetFeedResponse,
            429: GetFeedResponse,
            500: GetFeedResponse,
            503: GetFeedResponse,
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
        url = f"/feeds/2020-09-04/feeds/{feedId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            200: CancelFeedResponse,
            400: CancelFeedResponse,
            401: CancelFeedResponse,
            403: CancelFeedResponse,
            404: CancelFeedResponse,
            415: CancelFeedResponse,
            429: CancelFeedResponse,
            500: CancelFeedResponse,
            503: CancelFeedResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createFeedDocument(
        self,
        data: CreateFeedDocumentSpecification,
    ):
        """
                Creates a feed document for the feed type that you specify. This operation returns encryption details for encrypting the contents of the document, as well as a presigned URL for uploading the encrypted feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2020-09-04/documents"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateFeedDocumentResponse,
            400: CreateFeedDocumentResponse,
            403: CreateFeedDocumentResponse,
            404: CreateFeedDocumentResponse,
            413: CreateFeedDocumentResponse,
            415: CreateFeedDocumentResponse,
            429: CreateFeedDocumentResponse,
            500: CreateFeedDocumentResponse,
            503: CreateFeedDocumentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getFeedDocument(
        self,
        feedDocumentId: str,
    ):
        """
                Returns the information required for retrieving a feed document's contents. This includes a presigned URL for the feed document as well as the information required to decrypt the document's contents.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/feeds/2020-09-04/documents/{feedDocumentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetFeedDocumentResponse,
            400: GetFeedDocumentResponse,
            401: GetFeedDocumentResponse,
            403: GetFeedDocumentResponse,
            404: GetFeedDocumentResponse,
            415: GetFeedDocumentResponse,
            429: GetFeedDocumentResponse,
            500: GetFeedDocumentResponse,
            503: GetFeedDocumentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
