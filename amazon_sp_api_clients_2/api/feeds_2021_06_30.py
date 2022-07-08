"""
Selling Partner API for Feeds
=============================================================================================

The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
API Version: 2021-06-30
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentResponse:
    """
    Information required to upload a feed document's contents.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_document_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedDocumentResponse(**data)

    feed_document_id: str = attrs.field(
        default=None,
    )
    """
    The identifier of the feed document.
    """

    url: str = attrs.field(
        default=None,
    )
    """
    The presigned URL for uploading the feed contents. This URL expires after 5 minutes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentSpecification:
    """
    Specifies the content type for the createFeedDocument operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_document_specification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedDocumentSpecification(**data)

    content_type: str = attrs.field(
        default=None,
    )
    """
    The content type of the feed.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedResponse(**data)

    feed_id: str = attrs.field(
        default=None,
    )
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedSpecification:
    """
    Information required to create the feed.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_specification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedSpecification(**data)

    feed_options: Optional["FeedOptions"] = attrs.field(
        default=None,
    )
    """
    Additional options to control the feed. These vary by feed type.
    """

    feed_type: str = attrs.field(
        default=None,
    )
    """
    The feed type.
    """

    input_feed_document_id: str = attrs.field(
        default=None,
    )
    """
    The document identifier returned by the createFeedDocument operation. Upload the feed document contents before calling the createFeed operation.
    """

    marketplace_ids: List[str] = attrs.field(
        default=None,
    )
    """
    A list of identifiers for marketplaces that you want the feed to be applied to.

    Extra fields:
    {'maxItems': 25, 'minItems': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    An error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
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
        data = {name_convert[k]: v for k, v in data.items()}
        return ErrorList(**data)

    errors: List["Error"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class Feed:
    """
    Detailed information about the feed.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _feed_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Feed(**data)

    created_time: datetime = attrs.field(
        default=None,
    )
    """
    The date and time when the feed was created, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    feed_id: str = attrs.field(
        default=None,
    )
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """

    feed_type: str = attrs.field(
        default=None,
    )
    """
    The feed type.
    """

    marketplace_ids: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of identifiers for the marketplaces that the feed is applied to.
    """

    processing_end_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when feed processing completed, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_start_time: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when feed processing started, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_status: Union[
        Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]
    ] = attrs.field(
        default=None,
    )
    """
    The processing status of the feed.
    """

    result_feed_document_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the feed document. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeedDocument:
    """
    Information required for the feed document.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _feed_document_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return FeedDocument(**data)

    compression_algorithm: Optional[Union[Literal["GZIP"]]] = attrs.field(
        default=None,
    )
    """
    If present, the feed document contents are compressed using the indicated algorithm.
    """

    feed_document_id: str = attrs.field(
        default=None,
    )
    """
    The identifier for the feed document. This identifier is unique only in combination with a seller ID.
    """

    url: str = attrs.field(
        default=None,
    )
    """
    A presigned URL for the feed document. This URL expires after 5 minutes.
    """


@attrs.define(kw_only=True, frozen=True, slots=False)
class FeedOptions:
    """
    Additional options to control the feed. These vary by feed type.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _feed_options_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return FeedOptions(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeedsResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_feeds_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetFeedsResponse(**data)

    feeds: List["Feed"] = attrs.field(
        default=None,
    )
    """
    A list of feeds.
    """

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    Returned when the number of results exceeds pageSize. To get the next page of results, call the getFeeds operation with this token as the only parameter.
    """


_create_feed_document_response_name_convert = {
    "feedDocumentId": "feed_document_id",
    "url": "url",
}

_create_feed_document_specification_name_convert = {
    "contentType": "content_type",
}

_create_feed_response_name_convert = {
    "feedId": "feed_id",
}

_create_feed_specification_name_convert = {
    "feedOptions": "feed_options",
    "feedType": "feed_type",
    "inputFeedDocumentId": "input_feed_document_id",
    "marketplaceIds": "marketplace_ids",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_feed_name_convert = {
    "createdTime": "created_time",
    "feedId": "feed_id",
    "feedType": "feed_type",
    "marketplaceIds": "marketplace_ids",
    "processingEndTime": "processing_end_time",
    "processingStartTime": "processing_start_time",
    "processingStatus": "processing_status",
    "resultFeedDocumentId": "result_feed_document_id",
}

_feed_document_name_convert = {
    "compressionAlgorithm": "compression_algorithm",
    "feedDocumentId": "feed_document_id",
    "url": "url",
}

_feed_options_name_convert = {}

_get_feeds_response_name_convert = {
    "feeds": "feeds",
    "nextToken": "next_token",
}


class Feeds20210630Client(BaseClient):
    def cancel_feed(
        self,
        feed_id: str,
    ) -> Union[ErrorList]:
        """
        Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled. Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_id: The identifier for the feed. This identifier is unique only in combination with a seller ID.
        """
        url = "/feeds/2021-06-30/feeds/{feedId}"
        values = (feed_id,)
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._cancel_feed_params,
            self._cancel_feed_responses,
        )
        return response

    _cancel_feed_params = (("feedId", "path"),)  # name, param in

    _cancel_feed_responses = {
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def create_feed(
        self,
        feed_type: str,
        input_feed_document_id: str,
        marketplace_ids: List[str],
        feed_options: Dict[str, Any] = None,
    ) -> Union[CreateFeedResponse, ErrorList]:
        """
        Creates a feed. Upload the contents of the feed document before calling this operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_options: Additional options to control the feed. These vary by feed type.
            feed_type: The feed type.
            input_feed_document_id: The document identifier returned by the createFeedDocument operation. Upload the feed document contents before calling the createFeed operation.
            marketplace_ids: A list of identifiers for marketplaces that you want the feed to be applied to.
        """
        url = "/feeds/2021-06-30/feeds"
        values = (
            feed_options,
            feed_type,
            input_feed_document_id,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_feed_params,
            self._create_feed_responses,
        )
        return response

    _create_feed_params = (  # name, param in
        ("feedOptions", "body"),
        ("feedType", "body"),
        ("inputFeedDocumentId", "body"),
        ("marketplaceIds", "body"),
    )

    _create_feed_responses = {
        202: CreateFeedResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def create_feed_document(
        self,
        content_type: str,
    ) -> Union[CreateFeedDocumentResponse, ErrorList]:
        """
        Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_type: The content type of the feed.
        """
        url = "/feeds/2021-06-30/documents"
        values = (content_type,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_feed_document_params,
            self._create_feed_document_responses,
        )
        return response

    _create_feed_document_params = (("contentType", "body"),)  # name, param in

    _create_feed_document_responses = {
        201: CreateFeedDocumentResponse,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_feed(
        self,
        feed_id: str,
    ) -> Union[ErrorList, Feed]:
        """
        Returns feed details (including the resultDocumentId, if available) for the feed that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_id: The identifier for the feed. This identifier is unique only in combination with a seller ID.
        """
        url = "/feeds/2021-06-30/feeds/{feedId}"
        values = (feed_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_feed_params,
            self._get_feed_responses,
        )
        return response

    _get_feed_params = (("feedId", "path"),)  # name, param in

    _get_feed_responses = {
        200: Feed,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_feed_document(
        self,
        feed_document_id: str,
    ) -> Union[ErrorList, FeedDocument]:
        """
        Returns the information required for retrieving a feed document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_document_id: The identifier of the feed document.
        """
        url = "/feeds/2021-06-30/documents/{feedDocumentId}"
        values = (feed_document_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_feed_document_params,
            self._get_feed_document_responses,
        )
        return response

    _get_feed_document_params = (("feedDocumentId", "path"),)  # name, param in

    _get_feed_document_responses = {
        200: FeedDocument,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_feeds(
        self,
        feed_types: List[str] = None,
        marketplace_ids: List[str] = None,
        page_size: int = None,
        processing_statuses: List[
            Union[Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]]
        ] = None,
        created_since: datetime = None,
        created_until: datetime = None,
        next_token: str = None,
    ) -> Union[ErrorList, GetFeedsResponse]:
        """
        Returns feed details for the feeds that match the filters that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_types: A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
            marketplace_ids: A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
            page_size: The maximum number of feeds to return in a single call.
            processing_statuses: A list of processing statuses used to filter feeds.
            created_since: The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
            created_until: The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
            next_token: A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        """
        url = "/feeds/2021-06-30/feeds"
        values = (
            feed_types,
            marketplace_ids,
            page_size,
            processing_statuses,
            created_since,
            created_until,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_feeds_params,
            self._get_feeds_responses,
        )
        return response

    _get_feeds_params = (  # name, param in
        ("feedTypes", "query"),
        ("marketplaceIds", "query"),
        ("pageSize", "query"),
        ("processingStatuses", "query"),
        ("createdSince", "query"),
        ("createdUntil", "query"),
        ("nextToken", "query"),
    )

    _get_feeds_responses = {
        200: GetFeedsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }