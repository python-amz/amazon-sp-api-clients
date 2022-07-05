"""
Selling Partner API for Feeds
=============================================================================================

The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
API Version: 2020-09-04
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelFeedResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _cancel_feed_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CancelFeedResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentResponse:
    """
    The response for the createFeedDocument operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_document_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedDocumentResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateFeedDocumentResult"] = attrs.field(
        default=None,
    )
    """
    Information required to encrypt and upload a feed document's contents.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentResult:
    """
    Information required to encrypt and upload a feed document's contents.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_document_result_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedDocumentResult(**data)

    encryption_details: "FeedDocumentEncryptionDetails" = attrs.field(
        default=None,
    )
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

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

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateFeedResult"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedResult:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_result_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedResult(**data)

    feed_id: str = attrs.field(
        default=None,
    )
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedSpecification:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_feed_specification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return CreateFeedSpecification(**data)

    feed_options: Optional["FeedOptions"] = attrs.field(
        default=None,
    )
    """
    Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
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
    The document identifier returned by the createFeedDocument operation. Encrypt and upload the feed document contents before calling the createFeed operation.
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
class Feed:
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

    encryption_details: "FeedDocumentEncryptionDetails" = attrs.field(
        default=None,
    )
    """
    Encryption details for required client-side encryption and decryption of document contents.
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


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeedDocumentEncryptionDetails:
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _feed_document_encryption_details_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return FeedDocumentEncryptionDetails(**data)

    initialization_vector: str = attrs.field(
        default=None,
    )
    """
    The vector to encrypt or decrypt the document contents using Cipher Block Chaining (CBC).
    """

    key: str = attrs.field(
        default=None,
    )
    """
    The encryption key used to encrypt or decrypt the document contents.
    """

    standard: Union[Literal["AES"]] = attrs.field(
        default=None,
    )
    """
    The encryption standard required to encrypt or decrypt the document contents.
    """


@attrs.define(kw_only=True, frozen=True, slots=False)
class FeedOptions:
    """
    Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _feed_options_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return FeedOptions(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeedDocumentResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_feed_document_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetFeedDocumentResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["FeedDocument"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeedResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_feed_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetFeedResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Feed"] = attrs.field(
        default=None,
    )


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

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    Returned when the number of results exceeds pageSize. To get the next page of results, call the getFeeds operation with this token as the only parameter.
    """

    payload: Optional[List["Feed"]] = attrs.field(
        default=None,
    )


_cancel_feed_response_name_convert = {
    "errors": "errors",
}

_create_feed_document_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_create_feed_document_result_name_convert = {
    "encryptionDetails": "encryption_details",
    "feedDocumentId": "feed_document_id",
    "url": "url",
}

_create_feed_document_specification_name_convert = {
    "contentType": "content_type",
}

_create_feed_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_create_feed_result_name_convert = {
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
    "encryptionDetails": "encryption_details",
    "feedDocumentId": "feed_document_id",
    "url": "url",
}

_feed_document_encryption_details_name_convert = {
    "initializationVector": "initialization_vector",
    "key": "key",
    "standard": "standard",
}

_feed_options_name_convert = {}

_get_feed_document_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_feed_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_feeds_response_name_convert = {
    "errors": "errors",
    "nextToken": "next_token",
    "payload": "payload",
}


class Feeds20200904Client(BaseClient):
    def cancel_feed(
        self,
        feed_id: str,
    ) -> Union[CancelFeedResponse]:
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
        url = "/feeds/2020-09-04/feeds/{feedId}"
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
        200: CancelFeedResponse,
        400: CancelFeedResponse,
        401: CancelFeedResponse,
        403: CancelFeedResponse,
        404: CancelFeedResponse,
        415: CancelFeedResponse,
        429: CancelFeedResponse,
        500: CancelFeedResponse,
        503: CancelFeedResponse,
    }

    def create_feed(
        self,
        feed_type: str,
        input_feed_document_id: str,
        marketplace_ids: List[str],
        feed_options: Dict[str, Any] = None,
    ) -> Union[CreateFeedResponse]:
        """
        Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_options: Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
            feed_type: The feed type.
            input_feed_document_id: The document identifier returned by the createFeedDocument operation. Encrypt and upload the feed document contents before calling the createFeed operation.
            marketplace_ids: A list of identifiers for marketplaces that you want the feed to be applied to.
        """
        url = "/feeds/2020-09-04/feeds"
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
        400: CreateFeedResponse,
        401: CreateFeedResponse,
        403: CreateFeedResponse,
        404: CreateFeedResponse,
        415: CreateFeedResponse,
        429: CreateFeedResponse,
        500: CreateFeedResponse,
        503: CreateFeedResponse,
    }

    def create_feed_document(
        self,
        content_type: str,
    ) -> Union[CreateFeedDocumentResponse]:
        """
        Creates a feed document for the feed type that you specify. This operation returns encryption details for encrypting the contents of the document, as well as a presigned URL for uploading the encrypted feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_type: The content type of the feed.
        """
        url = "/feeds/2020-09-04/documents"
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
        400: CreateFeedDocumentResponse,
        403: CreateFeedDocumentResponse,
        404: CreateFeedDocumentResponse,
        413: CreateFeedDocumentResponse,
        415: CreateFeedDocumentResponse,
        429: CreateFeedDocumentResponse,
        500: CreateFeedDocumentResponse,
        503: CreateFeedDocumentResponse,
    }

    def get_feed(
        self,
        feed_id: str,
    ) -> Union[GetFeedResponse]:
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
        url = "/feeds/2020-09-04/feeds/{feedId}"
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
        200: GetFeedResponse,
        400: GetFeedResponse,
        401: GetFeedResponse,
        403: GetFeedResponse,
        404: GetFeedResponse,
        415: GetFeedResponse,
        429: GetFeedResponse,
        500: GetFeedResponse,
        503: GetFeedResponse,
    }

    def get_feed_document(
        self,
        feed_document_id: str,
    ) -> Union[GetFeedDocumentResponse]:
        """
        Returns the information required for retrieving a feed document's contents. This includes a presigned URL for the feed document as well as the information required to decrypt the document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_document_id: The identifier of the feed document.
        """
        url = "/feeds/2020-09-04/documents/{feedDocumentId}"
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
        200: GetFeedDocumentResponse,
        400: GetFeedDocumentResponse,
        401: GetFeedDocumentResponse,
        403: GetFeedDocumentResponse,
        404: GetFeedDocumentResponse,
        415: GetFeedDocumentResponse,
        429: GetFeedDocumentResponse,
        500: GetFeedDocumentResponse,
        503: GetFeedDocumentResponse,
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
    ) -> Union[GetFeedsResponse]:
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
        url = "/feeds/2020-09-04/feeds"
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
        400: GetFeedsResponse,
        401: GetFeedsResponse,
        403: GetFeedsResponse,
        404: GetFeedsResponse,
        415: GetFeedsResponse,
        429: GetFeedsResponse,
        500: GetFeedsResponse,
        503: GetFeedsResponse,
    }
