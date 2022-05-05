"""
Selling Partner API for Feeds
=============================================================================================
The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-09-04
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class Feeds20200904Client(BaseClient):
    def create_feed(
        self,
    ):
        """
        Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        path_parameters = {}

        url = "/feeds/2020-09-04/feeds".format(**path_parameters)

        query_parameters = {}

    def get_feeds(
        self,
        feed_types: list[str] = None,
        marketplace_ids: list[str] = None,
        page_size: int = None,
        processing_statuses: list[
            Union[Literal["CANCELLED"], Literal["DONE"], Literal["FATAL"], Literal["IN_PROGRESS"], Literal["IN_QUEUE"]]
        ] = None,
        created_since: str = None,
        created_until: str = None,
        next_token: str = None,
    ):
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
        path_parameters = {}

        url = "/feeds/2020-09-04/feeds".format(**path_parameters)

        query_parameters = {}

        if feed_types is not None:
            query_parameters["feedTypes"] = feed_types

        if marketplace_ids is not None:
            query_parameters["marketplaceIds"] = marketplace_ids

        if page_size is not None:
            query_parameters["pageSize"] = page_size

        if processing_statuses is not None:
            query_parameters["processingStatuses"] = processing_statuses

        if created_since is not None:
            query_parameters["createdSince"] = created_since

        if created_until is not None:
            query_parameters["createdUntil"] = created_until

        if next_token is not None:
            query_parameters["nextToken"] = next_token

    def get_feed(
        self,
        feed_id: str,
    ):
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
        path_parameters = {}

        path_parameters["feedId"] = feed_id

        url = "/feeds/2020-09-04/feeds/{feedId}".format(**path_parameters)

        query_parameters = {}

    def cancel_feed(
        self,
        feed_id: str,
    ):
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
        path_parameters = {}

        path_parameters["feedId"] = feed_id

        url = "/feeds/2020-09-04/feeds/{feedId}".format(**path_parameters)

        query_parameters = {}

    def create_feed_document(
        self,
    ):
        """
        Creates a feed document for the feed type that you specify. This operation returns encryption details for encrypting the contents of the document, as well as a presigned URL for uploading the encrypted feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0083 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        path_parameters = {}

        url = "/feeds/2020-09-04/documents".format(**path_parameters)

        query_parameters = {}

    def get_feed_document(
        self,
        feed_document_id: str,
    ):
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
        path_parameters = {}

        path_parameters["feedDocumentId"] = feed_document_id

        url = "/feeds/2020-09-04/documents/{feedDocumentId}".format(**path_parameters)

        query_parameters = {}