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

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentResponse:
    """
    The response for the createFeedDocument operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateFeedDocumentResult"] = attrs.field()
    """
    Information required to encrypt and upload a feed document's contents.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentResult:
    """
    Information required to encrypt and upload a feed document's contents.
    """

    encryption_details: "FeedDocumentEncryptionDetails" = attrs.field()
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    feed_document_id: str = attrs.field()
    """
    The identifier of the feed document.
    """

    url: str = attrs.field()
    """
    The presigned URL for uploading the feed contents. This URL expires after 5 minutes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedDocumentSpecification:

    content_type: str = attrs.field()
    """
    The content type of the feed.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedResponse:
    """
    Response schema.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateFeedResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedResult:

    feed_id: str = attrs.field()
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFeedSpecification:

    feed_options: Optional["FeedOptions"] = attrs.field()
    """
    Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
    """

    feed_type: str = attrs.field()
    """
    The feed type.
    """

    input_feed_document_id: str = attrs.field()
    """
    The document identifier returned by the createFeedDocument operation. Encrypt and upload the feed document contents before calling the createFeed operation.
    """

    marketplace_ids: List[str] = attrs.field()
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

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Feed:

    created_time: datetime = attrs.field()
    """
    The date and time when the feed was created, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    feed_id: str = attrs.field()
    """
    The identifier for the feed. This identifier is unique only in combination with a seller ID.
    """

    feed_type: str = attrs.field()
    """
    The feed type.
    """

    marketplace_ids: Optional[List[str]] = attrs.field()
    """
    A list of identifiers for the marketplaces that the feed is applied to.
    """

    processing_end_time: Optional[datetime] = attrs.field()
    """
    The date and time when feed processing completed, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_start_time: Optional[datetime] = attrs.field()
    """
    The date and time when feed processing started, in ISO 8601 date time format.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    processing_status: Union[
        Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]
    ] = attrs.field()
    """
    The processing status of the feed.
    """

    result_feed_document_id: Optional[str] = attrs.field()
    """
    The identifier for the feed document. This identifier is unique only in combination with a seller ID.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeedDocument:

    compression_algorithm: Optional[Union[Literal["GZIP"]]] = attrs.field()
    """
    If present, the feed document contents are compressed using the indicated algorithm.
    """

    encryption_details: "FeedDocumentEncryptionDetails" = attrs.field()
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    feed_document_id: str = attrs.field()
    """
    The identifier for the feed document. This identifier is unique only in combination with a seller ID.
    """

    url: str = attrs.field()
    """
    A presigned URL for the feed document. This URL expires after 5 minutes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeedDocumentEncryptionDetails:
    """
    Encryption details for required client-side encryption and decryption of document contents.
    """

    initialization_vector: str = attrs.field()
    """
    The vector to encrypt or decrypt the document contents using Cipher Block Chaining (CBC).
    """

    key: str = attrs.field()
    """
    The encryption key used to encrypt or decrypt the document contents.
    """

    standard: Union[Literal["AES"]] = attrs.field()
    """
    The encryption standard required to encrypt or decrypt the document contents.
    """


@attrs.define(kw_only=True, frozen=True, slots=False)
class FeedOptions:
    """
    Additional options to control the feed. For feeds that use the feedOptions parameter, you can find the parameter values in the feed description in [feedType values](doc:feed-type-values).
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeedDocumentResponse:
    """
    Response schema.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["FeedDocument"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeedResponse:
    """
    Response schema.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Feed"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeedsResponse:
    """
    Response schema.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    next_token: Optional[str] = attrs.field()
    """
    Returned when the number of results exceeds pageSize. To get the next page of results, call the getFeeds operation with this token as the only parameter.
    """

    payload: Optional[List["Feed"]] = attrs.field()


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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _cancel_feed_params = (("feedId", "path"),)  # name, param in

    _cancel_feed_responses = {
        (200, "application/json"): CancelFeedResponse,
        (400, "application/json"): CancelFeedResponse,
        (401, "application/json"): CancelFeedResponse,
        (403, "application/json"): CancelFeedResponse,
        (404, "application/json"): CancelFeedResponse,
        (415, "application/json"): CancelFeedResponse,
        (429, "application/json"): CancelFeedResponse,
        (500, "application/json"): CancelFeedResponse,
        (503, "application/json"): CancelFeedResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_feed_params = (  # name, param in
        ("feedOptions", "body"),
        ("feedType", "body"),
        ("inputFeedDocumentId", "body"),
        ("marketplaceIds", "body"),
    )

    _create_feed_responses = {
        (202, "application/json"): CreateFeedResponse,
        (400, "application/json"): CreateFeedResponse,
        (401, "application/json"): CreateFeedResponse,
        (403, "application/json"): CreateFeedResponse,
        (404, "application/json"): CreateFeedResponse,
        (415, "application/json"): CreateFeedResponse,
        (429, "application/json"): CreateFeedResponse,
        (500, "application/json"): CreateFeedResponse,
        (503, "application/json"): CreateFeedResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_feed_document_params = (("contentType", "body"),)  # name, param in

    _create_feed_document_responses = {
        (201, "application/json"): CreateFeedDocumentResponse,
        (400, "application/json"): CreateFeedDocumentResponse,
        (403, "application/json"): CreateFeedDocumentResponse,
        (404, "application/json"): CreateFeedDocumentResponse,
        (413, "application/json"): CreateFeedDocumentResponse,
        (415, "application/json"): CreateFeedDocumentResponse,
        (429, "application/json"): CreateFeedDocumentResponse,
        (500, "application/json"): CreateFeedDocumentResponse,
        (503, "application/json"): CreateFeedDocumentResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_feed_params = (("feedId", "path"),)  # name, param in

    _get_feed_responses = {
        (200, "application/json"): GetFeedResponse,
        (400, "application/json"): GetFeedResponse,
        (401, "application/json"): GetFeedResponse,
        (403, "application/json"): GetFeedResponse,
        (404, "application/json"): GetFeedResponse,
        (415, "application/json"): GetFeedResponse,
        (429, "application/json"): GetFeedResponse,
        (500, "application/json"): GetFeedResponse,
        (503, "application/json"): GetFeedResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_feed_document_params = (("feedDocumentId", "path"),)  # name, param in

    _get_feed_document_responses = {
        (200, "application/json"): GetFeedDocumentResponse,
        (400, "application/json"): GetFeedDocumentResponse,
        (401, "application/json"): GetFeedDocumentResponse,
        (403, "application/json"): GetFeedDocumentResponse,
        (404, "application/json"): GetFeedDocumentResponse,
        (415, "application/json"): GetFeedDocumentResponse,
        (429, "application/json"): GetFeedDocumentResponse,
        (500, "application/json"): GetFeedDocumentResponse,
        (503, "application/json"): GetFeedDocumentResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

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
        (200, "application/json"): GetFeedsResponse,
        (400, "application/json"): GetFeedsResponse,
        (401, "application/json"): GetFeedsResponse,
        (403, "application/json"): GetFeedsResponse,
        (404, "application/json"): GetFeedsResponse,
        (415, "application/json"): GetFeedsResponse,
        (429, "application/json"): GetFeedsResponse,
        (500, "application/json"): GetFeedsResponse,
        (503, "application/json"): GetFeedsResponse,
    }
