"""
Selling Partner API for A+ Content Management
=============================================================================================
With the A+ Content API, you can build applications that help selling partners add rich marketing content to their Amazon product detail pages. A+ content helps selling partners share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners assemble content by choosing from content modules and adding images and text.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-11-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class AplusContent20201101Client(BaseClient):
    def create_content_document(
        self,
        marketplace_id: str,
    ):
        """
        Creates a new A+ Content document.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        path_parameters = {}

        url = "/aplus/2020-11-01/contentDocuments".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

    def search_content_documents(
        self,
        marketplace_id: str,
        page_token: str = None,
    ):
        """
        Returns a list of all A+ Content documents assigned to a selling partner. This operation returns only the metadata of the A+ Content documents. Call the getContentDocument operation to get the actual contents of the A+ Content documents.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            page_token: A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
        """
        path_parameters = {}

        url = "/aplus/2020-11-01/contentDocuments".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

        if page_token is not None:
            query_parameters["pageToken"] = page_token

    def update_content_document(
        self,
        content_reference_key: str,
        marketplace_id: str,
    ):
        """
        Updates an existing A+ Content document.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        path_parameters = {}

        path_parameters["contentReferenceKey"] = content_reference_key

        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

    def get_content_document(
        self,
        content_reference_key: str,
        marketplace_id: str,
        included_data_set: list[Union[Literal["CONTENTS"], Literal["METADATA"]]],
    ):
        """
        Returns an A+ Content document, if available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            included_data_set: The set of A+ Content data types to include in the response.
        """
        path_parameters = {}

        path_parameters["contentReferenceKey"] = content_reference_key

        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

        query_parameters["includedDataSet"] = included_data_set

    def post_content_document_asin_relations(
        self,
        content_reference_key: str,
        marketplace_id: str,
    ):
        """
        Replaces all ASINs related to the specified A+ Content document, if available. This may add or remove ASINs, depending on the current set of related ASINs. Removing an ASIN has the side effect of suspending the content document from that ASIN.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        path_parameters = {}

        path_parameters["contentReferenceKey"] = content_reference_key

        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

    def list_content_document_asin_relations(
        self,
        content_reference_key: str,
        marketplace_id: str,
        included_data_set: list[Union[Literal["METADATA"]]] = None,
        asin_set: list[str] = None,
        page_token: str = None,
    ):
        """
        Returns a list of ASINs related to the specified A+ Content document, if available. If you do not include the asinSet parameter, the operation returns all ASINs related to the content document.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            included_data_set: The set of A+ Content data types to include in the response. If you do not include this parameter, the operation returns the related ASINs without metadata.
            asin_set: The set of ASINs.
            page_token: A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
        """
        path_parameters = {}

        path_parameters["contentReferenceKey"] = content_reference_key

        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

        if included_data_set is not None:
            query_parameters["includedDataSet"] = included_data_set

        if asin_set is not None:
            query_parameters["asinSet"] = asin_set

        if page_token is not None:
            query_parameters["pageToken"] = page_token

    def validate_content_document_asin_relations(
        self,
        marketplace_id: str,
        asin_set: list[str] = None,
    ):
        """
        Checks if the A+ Content document is valid for use on a set of ASINs.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            asin_set: The set of ASINs.
        """
        path_parameters = {}

        url = "/aplus/2020-11-01/contentAsinValidations".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

        if asin_set is not None:
            query_parameters["asinSet"] = asin_set

    def search_content_publish_records(
        self,
        marketplace_id: str,
        asin: str,
        page_token: str = None,
    ):
        """
        Searches for A+ Content publishing records, if available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
            asin: The Amazon Standard Identification Number (ASIN).
            page_token: A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
        """
        path_parameters = {}

        url = "/aplus/2020-11-01/contentPublishRecords".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

        query_parameters["asin"] = asin

        if page_token is not None:
            query_parameters["pageToken"] = page_token

    def post_content_document_approval_submission(
        self,
        content_reference_key: str,
        marketplace_id: str,
    ):
        """
        Submits an A+ Content document for review, approval, and publishing.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        path_parameters = {}

        path_parameters["contentReferenceKey"] = content_reference_key

        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

    def post_content_document_suspend_submission(
        self,
        content_reference_key: str,
        marketplace_id: str,
    ):
        """
        Submits a request to suspend visible A+ Content. This neither deletes the content document nor the ASIN relations.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            content_reference_key: The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            marketplace_id: The identifier for the marketplace where the A+ Content is published.
        """
        path_parameters = {}

        path_parameters["contentReferenceKey"] = content_reference_key

        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/suspendSubmissions".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id