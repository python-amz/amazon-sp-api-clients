"""
Selling Partner API for A+ Content Management
=============================================================================================

With the A+ Content API, you can build applications that help selling partners add rich marketing content to their Amazon product detail pages. A+ content helps selling partners share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners assemble content by choosing from content modules and adding images and text.
API Version: 2020-11-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class AplusPaginatedResponse:

    """
    The base response data for paginated A+ Content operations. Individual operations may extend this with additional data. If nextPageToken is not returned, there are no more pages to return.
    """

    pass


@attrs.define
class AplusResponse:

    """
    The base response data for all A+ Content operations when a request is successful or partially successful. Individual operations may extend this with additional data.
    """

    warnings: "MessageSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Asin:

    """
    The Amazon Standard Identification Number (ASIN).
    """

    pass


@attrs.define
class AsinBadge:

    """
    A flag that provides additional information about an ASIN. This is contextual and may change depending on the request that generated it.
    """

    pass


@attrs.define
class AsinBadgeSet:

    """
    The set of ASIN badges.
    """

    pass


@attrs.define
class AsinMetadata:

    """
    The A+ Content ASIN with additional metadata for content management. If you don't include the `includedDataSet` parameter in a call to the listContentDocumentAsinRelations operation, the related ASINs are returned without metadata.
    """

    image_url: str = attrs.field(
        kw_only=True,
    )
    """
    The default image for the ASIN in the Amazon catalog.

    Extra fields:
    {'minLength': 1}
    """

    title: str = attrs.field(
        kw_only=True,
    )
    """
    The title for the ASIN in the Amazon catalog.

    Extra fields:
    {'minLength': 1}
    """

    asin: "Asin" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    badge_set: "AsinBadgeSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_reference_key_set: "ContentReferenceKeySet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    parent: "Asin" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AsinMetadataSet:

    """
    The set of ASIN metadata.
    """

    pass


@attrs.define
class AsinSet:

    """
    The set of ASINs.
    """

    pass


@attrs.define
class ColorType:

    """
    The relative color scheme of content.
    """

    pass


@attrs.define
class ContentBadge:

    """
    A flag that provides additional information about an A+ Content document.
    """

    pass


@attrs.define
class ContentBadgeSet:

    """
    The set of content badges.
    """

    pass


@attrs.define
class ContentDocument:

    """
    The A+ Content document. This is the enhanced content that is published to product detail pages.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The A+ Content document name.

    Extra fields:
    {'maxLength': 100, 'minLength': 1}
    """

    content_module_list: "ContentModuleList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_sub_type: "ContentSubType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_type: "ContentType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    locale: "LanguageTag" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContentMetadata:

    """
    The metadata of an A+ Content document.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The A+ Content document name.

    Extra fields:
    {'maxLength': 100, 'minLength': 1}
    """

    update_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    The approximate age of the A+ Content document and metadata.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    badge_set: "ContentBadgeSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    marketplace_id: "MarketplaceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    status: "ContentStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContentMetadataRecord:

    """
    The metadata for an A+ Content document, with additional information for content management.
    """

    content_metadata: "ContentMetadata" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_reference_key: "ContentReferenceKey" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContentMetadataRecordList:

    """
    A list of A+ Content metadata records.
    """

    pass


@attrs.define
class ContentModule:

    """
    An A+ Content module. An A+ Content document is composed of content modules. The contentModuleType property selects which content module types to use.
    """

    content_module_type: "ContentModuleType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_company_logo: "StandardCompanyLogoModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_comparison_table: "StandardComparisonTableModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_four_image_text: "StandardFourImageTextModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_four_image_text_quadrant: "StandardFourImageTextQuadrantModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_header_image_text: "StandardHeaderImageTextModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_image_sidebar: "StandardImageSidebarModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_image_text_overlay: "StandardImageTextOverlayModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_multiple_image_text: "StandardMultipleImageTextModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_product_description: "StandardProductDescriptionModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_single_image_highlights: "StandardSingleImageHighlightsModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_single_image_specs_detail: "StandardSingleImageSpecsDetailModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_single_side_image: "StandardSingleSideImageModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_tech_specs: "StandardTechSpecsModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_text: "StandardTextModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_three_image_text: "StandardThreeImageTextModule" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContentModuleList:

    """
    A list of A+ Content modules.
    """

    pass


@attrs.define
class ContentModuleType:

    """
    The type of A+ Content module.
    """

    pass


@attrs.define
class ContentRecord:

    """
    A content document with additional information for content management.
    """

    content_document: "ContentDocument" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_metadata: "ContentMetadata" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_reference_key: "ContentReferenceKey" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContentReferenceKey:

    """
    A unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """

    pass


@attrs.define
class ContentReferenceKeySet:

    """
    A set of content reference keys.
    """

    pass


@attrs.define
class ContentStatus:

    """
    The submission status of the content document.
    """

    pass


@attrs.define
class ContentSubType:

    """
    The A+ Content document subtype. This represents a special-purpose type of an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any time.
    """

    pass


@attrs.define
class ContentType:

    """
    The A+ Content document type.
    """

    pass


@attrs.define
class Decorator:

    """
    A decorator applied to a content string value in order to create rich text.
    """

    depth: int = attrs.field(
        kw_only=True,
    )
    """
    The relative intensity or variation of this decorator. Decorators such as bullet-points, for example, can have multiple indentation depths.

    Extra fields:
    {'maximum': 100.0, 'minimum': 0.0}
    """

    length: int = attrs.field(
        kw_only=True,
    )
    """
    The number of content characters to alter with this decorator. Decorators such as line breaks can have zero length and fit between characters.

    Extra fields:
    {'maximum': 10000.0, 'minimum': 0.0}
    """

    offset: int = attrs.field(
        kw_only=True,
    )
    """
    The starting character of this decorator within the content string. Use zero for the first character.

    Extra fields:
    {'maximum': 10000.0, 'minimum': 0.0}
    """

    type: "DecoratorType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class DecoratorSet:

    """
    A set of content decorators.
    """

    pass


@attrs.define
class DecoratorType:

    """
    The type of rich text decorator.
    """

    pass


@attrs.define
class Error:

    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    The code that identifies the type of error condition.

    Extra fields:
    {'minLength': 1}
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional information, if available, to clarify the error condition.

    Extra fields:
    {'minLength': 1}
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A human readable description of the error condition.

    Extra fields:
    {'minLength': 1}
    """

    pass


@attrs.define
class ErrorList:

    """
    The error response for when a request is unsuccessful.
    """

    errors: List["Error"] = attrs.field(
        kw_only=True,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class GetContentDocumentResponse:

    pass


@attrs.define
class ImageComponent:

    """
    A reference to an image, hosted in the A+ Content media library.
    """

    alt_text: str = attrs.field(
        kw_only=True,
    )
    """
    The alternative text for the image.

    Extra fields:
    {'maxLength': 100, 'minLength': 1}
    """

    upload_destination_id: str = attrs.field(
        kw_only=True,
    )
    """
    This identifier is provided by the Selling Partner API for Uploads.

    Extra fields:
    {'minLength': 1}
    """

    image_crop_specification: "ImageCropSpecification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ImageCropSpecification:

    """
    The instructions for optionally cropping an image. If no cropping is desired, set the dimensions to the original image size. If the image is cropped and no offset values are provided, then the coordinates of the top left corner of the cropped image, relative to the original image, are defaulted to (0,0).
    """

    offset: "ImageOffsets" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    size: "ImageDimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ImageDimensions:

    """
    The dimensions extending from the top left corner of the cropped image, or the top left corner of the original image if there is no cropping. Only `pixels` is allowed as the units value for ImageDimensions.
    """

    height: "IntegerWithUnits" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    width: "IntegerWithUnits" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ImageOffsets:

    """
    The top left corner of the cropped image, specified in the original image's coordinate space.
    """

    x: "IntegerWithUnits" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    y: "IntegerWithUnits" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class IntegerWithUnits:

    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """

    units: str = attrs.field(
        kw_only=True,
    )
    """
    The unit of measurement.
    """

    value: int = attrs.field(
        kw_only=True,
    )
    """
    The dimension value.
    """

    pass


@attrs.define
class LanguageTag:

    """
        The IETF language tag. This only supports the primary language subtag with one secondary language subtag. The secondary language subtag is almost always a regional designation. This does not support additional subtags beyond the primary and secondary subtags.
    **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
    """

    pass


@attrs.define
class ListContentDocumentAsinRelationsResponse:

    pass


@attrs.define
class MarketplaceId:

    """
    The identifier for the marketplace where the A+ Content is published.
    """

    pass


@attrs.define
class MessageSet:

    """
    A set of messages to the user, such as warnings or comments.
    """

    pass


@attrs.define
class PageToken:

    """
    A page token that is returned when the results of the call exceed the page size. To get another page of results, call the operation again, passing in this value with the pageToken parameter.
    """

    pass


@attrs.define
class ParagraphComponent:

    """
    A list of rich text content, usually presented in a text box.
    """

    text_list: List["TextComponent"] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'maxItems': 100, 'minItems': 1}
    """

    pass


@attrs.define
class PlainTextItem:

    """
    Plain positional text, used in collections of brief labels and descriptors.
    """

    position: int = attrs.field(
        kw_only=True,
    )
    """
    The rank or index of this text item within the collection. Different items cannot occupy the same position within a single collection.

    Extra fields:
    {'maximum': 100.0, 'minimum': 1.0}
    """

    value: str = attrs.field(
        kw_only=True,
    )
    """
    The actual plain text.

    Extra fields:
    {'maxLength': 250, 'minLength': 1}
    """

    pass


@attrs.define
class PositionType:

    """
    The relative positioning of content.
    """

    pass


@attrs.define
class PostContentDocumentApprovalSubmissionResponse:

    pass


@attrs.define
class PostContentDocumentAsinRelationsRequest:

    asin_set: "AsinSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PostContentDocumentAsinRelationsResponse:

    pass


@attrs.define
class PostContentDocumentRequest:

    content_document: "ContentDocument" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PostContentDocumentResponse:

    pass


@attrs.define
class PostContentDocumentSuspendSubmissionResponse:

    pass


@attrs.define
class PublishRecord:

    """
    The full context for an A+ Content publishing event.
    """

    asin: "Asin" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_reference_key: "ContentReferenceKey" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_sub_type: "ContentSubType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    content_type: "ContentType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    locale: "LanguageTag" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    marketplace_id: "MarketplaceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PublishRecordList:

    """
    A list of A+ Content publishing records.
    """

    pass


@attrs.define
class SearchContentDocumentsResponse:

    pass


@attrs.define
class SearchContentPublishRecordsResponse:

    pass


@attrs.define
class StandardCompanyLogoModule:

    """
    The standard company logo image.
    """

    company_logo: "ImageComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardComparisonProductBlock:

    """
    The A+ Content standard comparison product block.
    """

    highlight: bool = attrs.field(
        kw_only=True,
    )
    """
    Determines whether this block of content is visually highlighted.
    """

    metrics: List["PlainTextItem"] = attrs.field(
        kw_only=True,
    )
    """
    Comparison metrics for the product.

    Extra fields:
    {'maxItems': 10, 'minItems': 0}
    """

    position: int = attrs.field(
        kw_only=True,
    )
    """
    The rank or index of this comparison product block within the module. Different blocks cannot occupy the same position within a single module.

    Extra fields:
    {'maximum': 6.0, 'minimum': 1.0}
    """

    title: str = attrs.field(
        kw_only=True,
    )
    """
    The comparison product title.

    Extra fields:
    {'maxLength': 80, 'minLength': 1}
    """

    asin: "Asin" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image: "ImageComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardComparisonTableModule:

    """
    The standard product comparison table.
    """

    metric_row_labels: List["PlainTextItem"] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'maxItems': 10, 'minItems': 0}
    """

    product_columns: List["StandardComparisonProductBlock"] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'maxItems': 6, 'minItems': 0}
    """

    pass


@attrs.define
class StandardFourImageTextModule:

    """
    Four standard images with text, presented across a single row.
    """

    block1: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block2: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block3: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block4: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardFourImageTextQuadrantModule:

    """
    Four standard images with text, presented on a grid of four quadrants.
    """

    block1: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block2: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block3: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block4: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardHeaderImageTextModule:

    """
    Standard headline text, an image, and body text.
    """

    block: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardHeaderTextListBlock:

    """
    The A+ standard fixed-length list of text, with a related headline.
    """

    block: "StandardTextListBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardImageCaptionBlock:

    """
    The A+ Content standard image and caption block.
    """

    caption: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image: "ImageComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardImageSidebarModule:

    """
    Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar.
    """

    description_list_block: "StandardTextListBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    description_text_block: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image_caption_block: "StandardImageCaptionBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    sidebar_image_text_block: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    sidebar_list_block: "StandardTextListBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardImageTextBlock:

    """
    The A+ Content standard image and text box block.
    """

    body: "ParagraphComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image: "ImageComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardImageTextCaptionBlock:

    """
    The A+ Content standard image and text block, with a related caption. The caption may not display on all devices.
    """

    block: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    caption: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardImageTextOverlayModule:

    """
    A standard background image with a floating text box.
    """

    block: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    overlay_color_type: "ColorType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardMultipleImageTextModule:

    """
    Standard images with text, presented one at a time. The user clicks on thumbnails to view each block.
    """

    blocks: List["StandardImageTextCaptionBlock"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardProductDescriptionModule:

    """
    Standard product description text.
    """

    body: "ParagraphComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardSingleImageHighlightsModule:

    """
    A standard image with several paragraphs and a bulleted list.
    """

    bulleted_list_block: "StandardHeaderTextListBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image: "ImageComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    text_block1: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    text_block2: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    text_block3: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardSingleImageSpecsDetailModule:

    """
    A standard image with paragraphs and a bulleted list, and extra space for technical details.
    """

    description_block1: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    description_block2: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    description_headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image: "ImageComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    specification_headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    specification_list_block: "StandardHeaderTextListBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    specification_text_block: "StandardTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardSingleSideImageModule:

    """
    A standard headline and body text with an image on the side.
    """

    block: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    image_position_type: "PositionType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardTechSpecsModule:

    """
    The standard table of technical feature names and definitions.
    """

    specification_list: List["StandardTextPairBlock"] = attrs.field(
        kw_only=True,
    )
    """
    The specification list.

    Extra fields:
    {'maxItems': 16, 'minItems': 4}
    """

    table_count: int = attrs.field(
        kw_only=True,
    )
    """
    The number of tables to present. Features are evenly divided between the tables.

    Extra fields:
    {'maximum': 2.0, 'minimum': 1.0}
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardTextBlock:

    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    body: "ParagraphComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardTextListBlock:

    """
    The A+ Content standard fixed length list of text, usually presented as bullet points.
    """

    text_list: List["TextItem"] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'maxItems': 8, 'minItems': 0}
    """

    pass


@attrs.define
class StandardTextModule:

    """
    A standard headline and body text.
    """

    body: "ParagraphComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardTextPairBlock:

    """
    The A+ Content standard label and description block, comprised of a pair of text components.
    """

    description: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardThreeImageTextModule:

    """
    Three standard images with text, presented across a single row.
    """

    block1: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block2: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    block3: "StandardImageTextBlock" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    headline: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TextComponent:

    """
    Rich text content.
    """

    value: str = attrs.field(
        kw_only=True,
    )
    """
    The actual plain text.

    Extra fields:
    {'maxLength': 10000, 'minLength': 1}
    """

    decorator_set: "DecoratorSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TextItem:

    """
    Rich positional text, usually presented as a collection of bullet points.
    """

    position: int = attrs.field(
        kw_only=True,
    )
    """
    The rank or index of this text item within the collection. Different items cannot occupy the same position within a single collection.

    Extra fields:
    {'maximum': 100.0, 'minimum': 1.0}
    """

    text: "TextComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ValidateContentDocumentAsinRelationsResponse:

    pass


class AplusContent20201101Client(BaseClient):
    def create_content_document(
        self,
        marketplace_id: str,
        content_document: Dict[str, Any],
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
        included_data_set: List[Union[Literal["CONTENTS"], Literal["METADATA"]]],
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
        included_data_set: List[Union[Literal["METADATA"]]] = None,
        asin_set: List[str] = None,
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
        asin_set: List["Asin"],
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
        content_document: Dict[str, Any],
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
        content_document: Dict[str, Any],
        asin_set: List[str] = None,
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
