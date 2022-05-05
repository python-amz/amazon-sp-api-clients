"""
Selling Partner API for A+ Content Management
=============================================================================================

With the A+ Content API, you can build applications that help selling partners add rich marketing content to their Amazon product detail pages. A+ content helps selling partners share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners assemble content by choosing from content modules and adding images and text.
API Version: 2020-11-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Any, Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AplusPaginatedResponse:
    pass


@attrs.define
class AplusResponse:
    warnings: "MessageSet" = attrs.field()
    pass


@attrs.define
class Asin:
    pass


@attrs.define
class AsinBadge:
    pass


@attrs.define
class AsinBadgeSet:
    pass


@attrs.define
class AsinMetadata:
    image_url: str = attrs.field()
    # {'minLength': 1}
    title: str = attrs.field()
    # {'minLength': 1}

    asin: "Asin" = attrs.field()
    badge_set: "AsinBadgeSet" = attrs.field()
    content_reference_key_set: "ContentReferenceKeySet" = attrs.field()
    parent: "Asin" = attrs.field()
    pass


@attrs.define
class AsinMetadataSet:
    pass


@attrs.define
class AsinSet:
    pass


@attrs.define
class ColorType:
    pass


@attrs.define
class ContentBadge:
    pass


@attrs.define
class ContentBadgeSet:
    pass


@attrs.define
class ContentDocument:
    name: str = attrs.field()
    # {'minLength': 1, 'maxLength': 100}

    content_module_list: "ContentModuleList" = attrs.field()
    content_sub_type: "ContentSubType" = attrs.field()
    content_type: "ContentType" = attrs.field()
    locale: "LanguageTag" = attrs.field()
    pass


@attrs.define
class ContentMetadata:
    name: str = attrs.field()
    # {'minLength': 1, 'maxLength': 100}
    update_time: str = attrs.field()
    # {'schema_format': 'date-time'}

    badge_set: "ContentBadgeSet" = attrs.field()
    marketplace_id: "MarketplaceId" = attrs.field()
    status: "ContentStatus" = attrs.field()
    pass


@attrs.define
class ContentMetadataRecord:
    content_metadata: "ContentMetadata" = attrs.field()
    content_reference_key: "ContentReferenceKey" = attrs.field()
    pass


@attrs.define
class ContentMetadataRecordList:
    pass


@attrs.define
class ContentModule:
    content_module_type: "ContentModuleType" = attrs.field()
    standard_company_logo: "StandardCompanyLogoModule" = attrs.field()
    standard_comparison_table: "StandardComparisonTableModule" = attrs.field()
    standard_four_image_text: "StandardFourImageTextModule" = attrs.field()
    standard_four_image_text_quadrant: "StandardFourImageTextQuadrantModule" = attrs.field()
    standard_header_image_text: "StandardHeaderImageTextModule" = attrs.field()
    standard_image_sidebar: "StandardImageSidebarModule" = attrs.field()
    standard_image_text_overlay: "StandardImageTextOverlayModule" = attrs.field()
    standard_multiple_image_text: "StandardMultipleImageTextModule" = attrs.field()
    standard_product_description: "StandardProductDescriptionModule" = attrs.field()
    standard_single_image_highlights: "StandardSingleImageHighlightsModule" = attrs.field()
    standard_single_image_specs_detail: "StandardSingleImageSpecsDetailModule" = attrs.field()
    standard_single_side_image: "StandardSingleSideImageModule" = attrs.field()
    standard_tech_specs: "StandardTechSpecsModule" = attrs.field()
    standard_text: "StandardTextModule" = attrs.field()
    standard_three_image_text: "StandardThreeImageTextModule" = attrs.field()
    pass


@attrs.define
class ContentModuleList:
    pass


@attrs.define
class ContentModuleType:
    pass


@attrs.define
class ContentRecord:
    content_document: "ContentDocument" = attrs.field()
    content_metadata: "ContentMetadata" = attrs.field()
    content_reference_key: "ContentReferenceKey" = attrs.field()
    pass


@attrs.define
class ContentReferenceKey:
    pass


@attrs.define
class ContentReferenceKeySet:
    pass


@attrs.define
class ContentStatus:
    pass


@attrs.define
class ContentSubType:
    pass


@attrs.define
class ContentType:
    pass


@attrs.define
class Decorator:
    depth: int = attrs.field()
    # {'maximum': 100.0, 'minimum': 0.0}
    length: int = attrs.field()
    # {'maximum': 10000.0, 'minimum': 0.0}
    offset: int = attrs.field()
    # {'maximum': 10000.0, 'minimum': 0.0}

    type: "DecoratorType" = attrs.field()
    pass


@attrs.define
class DecoratorSet:
    pass


@attrs.define
class DecoratorType:
    pass


@attrs.define
class Error:
    code: str = attrs.field()
    # {'minLength': 1}
    details: str = attrs.field()
    # {'minLength': 1}
    message: str = attrs.field()
    # {'minLength': 1}

    pass


@attrs.define
class ErrorList:
    errors: list["Error"] = attrs.field()

    pass


@attrs.define
class GetContentDocumentResponse:
    pass


@attrs.define
class ImageComponent:
    alt_text: str = attrs.field()
    # {'minLength': 1, 'maxLength': 100}
    upload_destination_id: str = attrs.field()
    # {'minLength': 1}

    image_crop_specification: "ImageCropSpecification" = attrs.field()
    pass


@attrs.define
class ImageCropSpecification:
    offset: "ImageOffsets" = attrs.field()
    size: "ImageDimensions" = attrs.field()
    pass


@attrs.define
class ImageDimensions:
    height: "IntegerWithUnits" = attrs.field()
    width: "IntegerWithUnits" = attrs.field()
    pass


@attrs.define
class ImageOffsets:
    x: "IntegerWithUnits" = attrs.field()
    y: "IntegerWithUnits" = attrs.field()
    pass


@attrs.define
class IntegerWithUnits:
    units: str = attrs.field()
    value: int = attrs.field()

    pass


@attrs.define
class LanguageTag:
    pass


@attrs.define
class ListContentDocumentAsinRelationsResponse:
    pass


@attrs.define
class MarketplaceId:
    pass


@attrs.define
class MessageSet:
    pass


@attrs.define
class PageToken:
    pass


@attrs.define
class ParagraphComponent:
    text_list: list["TextComponent"] = attrs.field()
    # {'maxItems': 100, 'minItems': 1}

    pass


@attrs.define
class PlainTextItem:
    position: int = attrs.field()
    # {'maximum': 100.0, 'minimum': 1.0}
    value: str = attrs.field()
    # {'minLength': 1, 'maxLength': 250}

    pass


@attrs.define
class PositionType:
    pass


@attrs.define
class PostContentDocumentApprovalSubmissionResponse:
    pass


@attrs.define
class PostContentDocumentAsinRelationsRequest:
    asin_set: "AsinSet" = attrs.field()
    pass


@attrs.define
class PostContentDocumentAsinRelationsResponse:
    pass


@attrs.define
class PostContentDocumentRequest:
    content_document: "ContentDocument" = attrs.field()
    pass


@attrs.define
class PostContentDocumentResponse:
    pass


@attrs.define
class PostContentDocumentSuspendSubmissionResponse:
    pass


@attrs.define
class PublishRecord:
    asin: "Asin" = attrs.field()
    content_reference_key: "ContentReferenceKey" = attrs.field()
    content_sub_type: "ContentSubType" = attrs.field()
    content_type: "ContentType" = attrs.field()
    locale: "LanguageTag" = attrs.field()
    marketplace_id: "MarketplaceId" = attrs.field()
    pass


@attrs.define
class PublishRecordList:
    pass


@attrs.define
class SearchContentDocumentsResponse:
    pass


@attrs.define
class SearchContentPublishRecordsResponse:
    pass


@attrs.define
class StandardCompanyLogoModule:
    company_logo: "ImageComponent" = attrs.field()
    pass


@attrs.define
class StandardComparisonProductBlock:
    highlight: bool = attrs.field()
    metrics: list["PlainTextItem"] = attrs.field()
    # {'maxItems': 10, 'minItems': 0}
    position: int = attrs.field()
    # {'maximum': 6.0, 'minimum': 1.0}
    title: str = attrs.field()
    # {'minLength': 1, 'maxLength': 80}

    asin: "Asin" = attrs.field()
    image: "ImageComponent" = attrs.field()
    pass


@attrs.define
class StandardComparisonTableModule:
    metric_row_labels: list["PlainTextItem"] = attrs.field()
    # {'maxItems': 10, 'minItems': 0}
    product_columns: list["StandardComparisonProductBlock"] = attrs.field()
    # {'maxItems': 6, 'minItems': 0}

    pass


@attrs.define
class StandardFourImageTextModule:
    block1: "StandardImageTextBlock" = attrs.field()
    block2: "StandardImageTextBlock" = attrs.field()
    block3: "StandardImageTextBlock" = attrs.field()
    block4: "StandardImageTextBlock" = attrs.field()
    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardFourImageTextQuadrantModule:
    block1: "StandardImageTextBlock" = attrs.field()
    block2: "StandardImageTextBlock" = attrs.field()
    block3: "StandardImageTextBlock" = attrs.field()
    block4: "StandardImageTextBlock" = attrs.field()
    pass


@attrs.define
class StandardHeaderImageTextModule:
    block: "StandardImageTextBlock" = attrs.field()
    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardHeaderTextListBlock:
    block: "StandardTextListBlock" = attrs.field()
    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardImageCaptionBlock:
    caption: "TextComponent" = attrs.field()
    image: "ImageComponent" = attrs.field()
    pass


@attrs.define
class StandardImageSidebarModule:
    description_list_block: "StandardTextListBlock" = attrs.field()
    description_text_block: "StandardTextBlock" = attrs.field()
    headline: "TextComponent" = attrs.field()
    image_caption_block: "StandardImageCaptionBlock" = attrs.field()
    sidebar_image_text_block: "StandardImageTextBlock" = attrs.field()
    sidebar_list_block: "StandardTextListBlock" = attrs.field()
    pass


@attrs.define
class StandardImageTextBlock:
    body: "ParagraphComponent" = attrs.field()
    headline: "TextComponent" = attrs.field()
    image: "ImageComponent" = attrs.field()
    pass


@attrs.define
class StandardImageTextCaptionBlock:
    block: "StandardImageTextBlock" = attrs.field()
    caption: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardImageTextOverlayModule:
    block: "StandardImageTextBlock" = attrs.field()
    overlay_color_type: "ColorType" = attrs.field()
    pass


@attrs.define
class StandardMultipleImageTextModule:
    blocks: list["StandardImageTextCaptionBlock"] = attrs.field()

    pass


@attrs.define
class StandardProductDescriptionModule:
    body: "ParagraphComponent" = attrs.field()
    pass


@attrs.define
class StandardSingleImageHighlightsModule:
    bulleted_list_block: "StandardHeaderTextListBlock" = attrs.field()
    headline: "TextComponent" = attrs.field()
    image: "ImageComponent" = attrs.field()
    text_block1: "StandardTextBlock" = attrs.field()
    text_block2: "StandardTextBlock" = attrs.field()
    text_block3: "StandardTextBlock" = attrs.field()
    pass


@attrs.define
class StandardSingleImageSpecsDetailModule:
    description_block1: "StandardTextBlock" = attrs.field()
    description_block2: "StandardTextBlock" = attrs.field()
    description_headline: "TextComponent" = attrs.field()
    headline: "TextComponent" = attrs.field()
    image: "ImageComponent" = attrs.field()
    specification_headline: "TextComponent" = attrs.field()
    specification_list_block: "StandardHeaderTextListBlock" = attrs.field()
    specification_text_block: "StandardTextBlock" = attrs.field()
    pass


@attrs.define
class StandardSingleSideImageModule:
    block: "StandardImageTextBlock" = attrs.field()
    image_position_type: "PositionType" = attrs.field()
    pass


@attrs.define
class StandardTechSpecsModule:
    specification_list: list["StandardTextPairBlock"] = attrs.field()
    # {'maxItems': 16, 'minItems': 4}
    table_count: int = attrs.field()
    # {'maximum': 2.0, 'minimum': 1.0}

    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardTextBlock:
    body: "ParagraphComponent" = attrs.field()
    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardTextListBlock:
    text_list: list["TextItem"] = attrs.field()
    # {'maxItems': 8, 'minItems': 0}

    pass


@attrs.define
class StandardTextModule:
    body: "ParagraphComponent" = attrs.field()
    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardTextPairBlock:
    description: "TextComponent" = attrs.field()
    label: "TextComponent" = attrs.field()
    pass


@attrs.define
class StandardThreeImageTextModule:
    block1: "StandardImageTextBlock" = attrs.field()
    block2: "StandardImageTextBlock" = attrs.field()
    block3: "StandardImageTextBlock" = attrs.field()
    headline: "TextComponent" = attrs.field()
    pass


@attrs.define
class TextComponent:
    value: str = attrs.field()
    # {'minLength': 1, 'maxLength': 10000}

    decorator_set: "DecoratorSet" = attrs.field()
    pass


@attrs.define
class TextItem:
    position: int = attrs.field()
    # {'maximum': 100.0, 'minimum': 1.0}

    text: "TextComponent" = attrs.field()
    pass


@attrs.define
class ValidateContentDocumentAsinRelationsResponse:
    pass


class AplusContent20201101Client(BaseClient):
    def create_content_document(
            self,
            marketplace_id: str,
            content_document: dict[str, Any],
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
            content_document: The A+ Content document. This is the enhanced content that is published to product detail pages.
        """
        url = "/aplus/2020-11-01/contentDocuments"
        values = (
            marketplace_id,
            content_document,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_content_document_params)
        return response

    _create_content_document_params = (  # name, param in
        ("marketplaceId", "query"),
        ("contentDocument", "body"),
    )

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
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}"
        values = (
            content_reference_key,
            marketplace_id,
            included_data_set,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_content_document_params)
        return response

    _get_content_document_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("includedDataSet", "query"),
    )

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
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins"
        values = (
            content_reference_key,
            marketplace_id,
            included_data_set,
            asin_set,
            page_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_content_document_asin_relations_params)
        return response

    _list_content_document_asin_relations_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("includedDataSet", "query"),
        ("asinSet", "query"),
        ("pageToken", "query"),
    )

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
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions"
        values = (
            content_reference_key,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._post_content_document_approval_submission_params
        )
        return response

    _post_content_document_approval_submission_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
    )

    def post_content_document_asin_relations(
            self,
            content_reference_key: str,
            marketplace_id: str,
            asin_set: list["Asin"],
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
            asin_set: The set of ASINs.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins"
        values = (
            content_reference_key,
            marketplace_id,
            asin_set,
        )
        response = self._parse_args_and_request(url, "POST", values, self._post_content_document_asin_relations_params)
        return response

    _post_content_document_asin_relations_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("asinSet", "body"),
    )

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
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/suspendSubmissions"
        values = (
            content_reference_key,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._post_content_document_suspend_submission_params
        )
        return response

    _post_content_document_suspend_submission_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
    )

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
        url = "/aplus/2020-11-01/contentDocuments"
        values = (
            marketplace_id,
            page_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._search_content_documents_params)
        return response

    _search_content_documents_params = (  # name, param in
        ("marketplaceId", "query"),
        ("pageToken", "query"),
    )

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
        url = "/aplus/2020-11-01/contentPublishRecords"
        values = (
            marketplace_id,
            asin,
            page_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._search_content_publish_records_params)
        return response

    _search_content_publish_records_params = (  # name, param in
        ("marketplaceId", "query"),
        ("asin", "query"),
        ("pageToken", "query"),
    )

    def update_content_document(
            self,
            content_reference_key: str,
            marketplace_id: str,
            content_document: dict[str, Any],
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
            content_document: The A+ Content document. This is the enhanced content that is published to product detail pages.
        """
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}"
        values = (
            content_reference_key,
            marketplace_id,
            content_document,
        )
        response = self._parse_args_and_request(url, "POST", values, self._update_content_document_params)
        return response

    _update_content_document_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("contentDocument", "body"),
    )

    def validate_content_document_asin_relations(
            self,
            marketplace_id: str,
            content_document: dict[str, Any],
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
            content_document: The A+ Content document. This is the enhanced content that is published to product detail pages.
        """
        url = "/aplus/2020-11-01/contentAsinValidations"
        values = (
            marketplace_id,
            asin_set,
            content_document,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._validate_content_document_asin_relations_params
        )
        return response

    _validate_content_document_asin_relations_params = (  # name, param in
        ("marketplaceId", "query"),
        ("asinSet", "query"),
        ("contentDocument", "body"),
    )
