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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AplusPaginatedResponse:
    """
    The base response data for paginated A+ Content operations. Individual operations may extend this with additional data. If nextPageToken is not returned, there are no more pages to return.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AplusResponse:
    """
    The base response data for all A+ Content operations when a request is successful or partially successful. Individual operations may extend this with additional data.
    """

    warnings: Optional[List["Error"]] = attrs.field()
    """
    A set of messages to the user, such as warnings or comments.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Asin:
    """
    The Amazon Standard Identification Number (ASIN).
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AsinBadge:
    """
    A flag that provides additional information about an ASIN. This is contextual and may change depending on the request that generated it.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AsinMetadata:
    """
    The A+ Content ASIN with additional metadata for content management. If you don't include the `includedDataSet` parameter in a call to the listContentDocumentAsinRelations operation, the related ASINs are returned without metadata.
    """

    asin: "Asin" = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN).
    """

    badge_set: Optional[List["AsinBadge"]] = attrs.field()
    """
    The set of ASIN badges.
    """

    content_reference_key_set: Optional[List["ContentReferenceKey"]] = attrs.field()
    """
    A set of content reference keys.
    """

    image_url: Optional[str] = attrs.field()
    """
    The default image for the ASIN in the Amazon catalog.

    Extra fields:
    {'minLength': 1}
    """

    parent: Optional["Asin"] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN).
    """

    title: Optional[str] = attrs.field()
    """
    The title for the ASIN in the Amazon catalog.

    Extra fields:
    {'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ColorType:
    """
    The relative color scheme of content.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentBadge:
    """
    A flag that provides additional information about an A+ Content document.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentDocument:
    """
    The A+ Content document. This is the enhanced content that is published to product detail pages.
    """

    content_module_list: List["ContentModule"] = attrs.field()
    """
    A list of A+ Content modules.
    """

    content_sub_type: Optional["ContentSubType"] = attrs.field()
    """
    The A+ Content document subtype. This represents a special-purpose type of an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any time.
    """

    content_type: "ContentType" = attrs.field()
    """
    The A+ Content document type.
    """

    locale: "LanguageTag" = attrs.field()
    """
    The IETF language tag. This only supports the primary language subtag with one secondary language subtag. The secondary language subtag is almost always a regional designation. This does not support additional subtags beyond the primary and secondary subtags.
        **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
    """

    name: str = attrs.field()
    """
    The A+ Content document name.

    Extra fields:
    {'maxLength': 100, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentMetadata:
    """
    The metadata of an A+ Content document.
    """

    badge_set: List["ContentBadge"] = attrs.field()
    """
    The set of content badges.
    """

    marketplace_id: "MarketplaceId" = attrs.field()
    """
    The identifier for the marketplace where the A+ Content is published.
    """

    name: str = attrs.field()
    """
    The A+ Content document name.

    Extra fields:
    {'maxLength': 100, 'minLength': 1}
    """

    status: "ContentStatus" = attrs.field()
    """
    The submission status of the content document.
    """

    update_time: datetime = attrs.field()
    """
    The approximate age of the A+ Content document and metadata.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentMetadataRecord:
    """
    The metadata for an A+ Content document, with additional information for content management.
    """

    content_metadata: "ContentMetadata" = attrs.field()
    """
    The metadata of an A+ Content document.
    """

    content_reference_key: "ContentReferenceKey" = attrs.field()
    """
    A unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentModule:
    """
    An A+ Content module. An A+ Content document is composed of content modules. The contentModuleType property selects which content module types to use.
    """

    content_module_type: "ContentModuleType" = attrs.field()
    """
    The type of A+ Content module.
    """

    standard_company_logo: Optional["StandardCompanyLogoModule"] = attrs.field()
    """
    The standard company logo image.
    """

    standard_comparison_table: Optional["StandardComparisonTableModule"] = attrs.field()
    """
    The standard product comparison table.
    """

    standard_four_image_text: Optional["StandardFourImageTextModule"] = attrs.field()
    """
    Four standard images with text, presented across a single row.
    """

    standard_four_image_text_quadrant: Optional["StandardFourImageTextQuadrantModule"] = attrs.field()
    """
    Four standard images with text, presented on a grid of four quadrants.
    """

    standard_header_image_text: Optional["StandardHeaderImageTextModule"] = attrs.field()
    """
    Standard headline text, an image, and body text.
    """

    standard_image_sidebar: Optional["StandardImageSidebarModule"] = attrs.field()
    """
    Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar.
    """

    standard_image_text_overlay: Optional["StandardImageTextOverlayModule"] = attrs.field()
    """
    A standard background image with a floating text box.
    """

    standard_multiple_image_text: Optional["StandardMultipleImageTextModule"] = attrs.field()
    """
    Standard images with text, presented one at a time. The user clicks on thumbnails to view each block.
    """

    standard_product_description: Optional["StandardProductDescriptionModule"] = attrs.field()
    """
    Standard product description text.
    """

    standard_single_image_highlights: Optional["StandardSingleImageHighlightsModule"] = attrs.field()
    """
    A standard image with several paragraphs and a bulleted list.
    """

    standard_single_image_specs_detail: Optional["StandardSingleImageSpecsDetailModule"] = attrs.field()
    """
    A standard image with paragraphs and a bulleted list, and extra space for technical details.
    """

    standard_single_side_image: Optional["StandardSingleSideImageModule"] = attrs.field()
    """
    A standard headline and body text with an image on the side.
    """

    standard_tech_specs: Optional["StandardTechSpecsModule"] = attrs.field()
    """
    The standard table of technical feature names and definitions.
    """

    standard_text: Optional["StandardTextModule"] = attrs.field()
    """
    A standard headline and body text.
    """

    standard_three_image_text: Optional["StandardThreeImageTextModule"] = attrs.field()
    """
    Three standard images with text, presented across a single row.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentModuleType:
    """
    The type of A+ Content module.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentRecord:
    """
    A content document with additional information for content management.
    """

    content_document: Optional["ContentDocument"] = attrs.field()
    """
    The A+ Content document. This is the enhanced content that is published to product detail pages.
    """

    content_metadata: Optional["ContentMetadata"] = attrs.field()
    """
    The metadata of an A+ Content document.
    """

    content_reference_key: "ContentReferenceKey" = attrs.field()
    """
    A unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentReferenceKey:
    """
    A unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentStatus:
    """
    The submission status of the content document.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentSubType:
    """
    The A+ Content document subtype. This represents a special-purpose type of an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any time.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContentType:
    """
    The A+ Content document type.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decorator:
    """
    A decorator applied to a content string value in order to create rich text.
    """

    depth: Optional[int] = attrs.field()
    """
    The relative intensity or variation of this decorator. Decorators such as bullet-points, for example, can have multiple indentation depths.

    Extra fields:
    {'maximum': 100.0, 'minimum': 0.0}
    """

    length: Optional[int] = attrs.field()
    """
    The number of content characters to alter with this decorator. Decorators such as line breaks can have zero length and fit between characters.

    Extra fields:
    {'maximum': 10000.0, 'minimum': 0.0}
    """

    offset: Optional[int] = attrs.field()
    """
    The starting character of this decorator within the content string. Use zero for the first character.

    Extra fields:
    {'maximum': 10000.0, 'minimum': 0.0}
    """

    type: Optional["DecoratorType"] = attrs.field()
    """
    The type of rich text decorator.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DecoratorType:
    """
    The type of rich text decorator.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    The code that identifies the type of error condition.

    Extra fields:
    {'minLength': 1}
    """

    details: Optional[str] = attrs.field()
    """
    Additional information, if available, to clarify the error condition.

    Extra fields:
    {'minLength': 1}
    """

    message: str = attrs.field()
    """
    A human readable description of the error condition.

    Extra fields:
    {'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    The error response for when a request is unsuccessful.
    """

    errors: List["Error"] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetContentDocumentResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImageComponent:
    """
    A reference to an image, hosted in the A+ Content media library.
    """

    alt_text: str = attrs.field()
    """
    The alternative text for the image.

    Extra fields:
    {'maxLength': 100, 'minLength': 1}
    """

    image_crop_specification: "ImageCropSpecification" = attrs.field()
    """
    The instructions for optionally cropping an image. If no cropping is desired, set the dimensions to the original image size. If the image is cropped and no offset values are provided, then the coordinates of the top left corner of the cropped image, relative to the original image, are defaulted to (0,0).
    """

    upload_destination_id: str = attrs.field()
    """
    This identifier is provided by the Selling Partner API for Uploads.

    Extra fields:
    {'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImageCropSpecification:
    """
    The instructions for optionally cropping an image. If no cropping is desired, set the dimensions to the original image size. If the image is cropped and no offset values are provided, then the coordinates of the top left corner of the cropped image, relative to the original image, are defaulted to (0,0).
    """

    offset: Optional["ImageOffsets"] = attrs.field()
    """
    The top left corner of the cropped image, specified in the original image's coordinate space.
    """

    size: "ImageDimensions" = attrs.field()
    """
    The dimensions extending from the top left corner of the cropped image, or the top left corner of the original image if there is no cropping. Only `pixels` is allowed as the units value for ImageDimensions.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImageDimensions:
    """
    The dimensions extending from the top left corner of the cropped image, or the top left corner of the original image if there is no cropping. Only `pixels` is allowed as the units value for ImageDimensions.
    """

    height: "IntegerWithUnits" = attrs.field()
    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """

    width: "IntegerWithUnits" = attrs.field()
    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImageOffsets:
    """
    The top left corner of the cropped image, specified in the original image's coordinate space.
    """

    x: "IntegerWithUnits" = attrs.field()
    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """

    y: "IntegerWithUnits" = attrs.field()
    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class IntegerWithUnits:
    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """

    units: str = attrs.field()
    """
    The unit of measurement.
    """

    value: int = attrs.field()
    """
    The dimension value.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LanguageTag:
    """
    The IETF language tag. This only supports the primary language subtag with one secondary language subtag. The secondary language subtag is almost always a regional designation. This does not support additional subtags beyond the primary and secondary subtags.
        **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListContentDocumentAsinRelationsResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceId:
    """
    The identifier for the marketplace where the A+ Content is published.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PageToken:
    """
    A page token that is returned when the results of the call exceed the page size. To get another page of results, call the operation again, passing in this value with the pageToken parameter.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ParagraphComponent:
    """
    A list of rich text content, usually presented in a text box.
    """

    text_list: List["TextComponent"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PlainTextItem:
    """
    Plain positional text, used in collections of brief labels and descriptors.
    """

    position: int = attrs.field()
    """
    The rank or index of this text item within the collection. Different items cannot occupy the same position within a single collection.

    Extra fields:
    {'maximum': 100.0, 'minimum': 1.0}
    """

    value: str = attrs.field()
    """
    The actual plain text.

    Extra fields:
    {'maxLength': 250, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PositionType:
    """
    The relative positioning of content.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostContentDocumentApprovalSubmissionResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostContentDocumentAsinRelationsRequest:

    asin_set: List["Asin"] = attrs.field()
    """
    The set of ASINs.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostContentDocumentAsinRelationsResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostContentDocumentRequest:

    content_document: "ContentDocument" = attrs.field()
    """
    The A+ Content document. This is the enhanced content that is published to product detail pages.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostContentDocumentResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostContentDocumentSuspendSubmissionResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PublishRecord:
    """
    The full context for an A+ Content publishing event.
    """

    asin: "Asin" = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN).
    """

    content_reference_key: "ContentReferenceKey" = attrs.field()
    """
    A unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """

    content_sub_type: Optional["ContentSubType"] = attrs.field()
    """
    The A+ Content document subtype. This represents a special-purpose type of an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any time.
    """

    content_type: "ContentType" = attrs.field()
    """
    The A+ Content document type.
    """

    locale: "LanguageTag" = attrs.field()
    """
    The IETF language tag. This only supports the primary language subtag with one secondary language subtag. The secondary language subtag is almost always a regional designation. This does not support additional subtags beyond the primary and secondary subtags.
        **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
    """

    marketplace_id: "MarketplaceId" = attrs.field()
    """
    The identifier for the marketplace where the A+ Content is published.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SearchContentDocumentsResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SearchContentPublishRecordsResponse:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardCompanyLogoModule:
    """
    The standard company logo image.
    """

    company_logo: "ImageComponent" = attrs.field()
    """
    A reference to an image, hosted in the A+ Content media library.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardComparisonProductBlock:
    """
    The A+ Content standard comparison product block.
    """

    asin: Optional["Asin"] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN).
    """

    highlight: Optional[bool] = attrs.field()
    """
    Determines whether this block of content is visually highlighted.
    """

    image: Optional["ImageComponent"] = attrs.field()
    """
    A reference to an image, hosted in the A+ Content media library.
    """

    metrics: Optional[List["PlainTextItem"]] = attrs.field()
    """
    Comparison metrics for the product.

    Extra fields:
    {'maxItems': 10, 'minItems': 0}
    """

    position: int = attrs.field()
    """
    The rank or index of this comparison product block within the module. Different blocks cannot occupy the same position within a single module.

    Extra fields:
    {'maximum': 6.0, 'minimum': 1.0}
    """

    title: Optional[str] = attrs.field()
    """
    The comparison product title.

    Extra fields:
    {'maxLength': 80, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardComparisonTableModule:
    """
    The standard product comparison table.
    """

    metric_row_labels: Optional[List["PlainTextItem"]] = attrs.field()

    product_columns: Optional[List["StandardComparisonProductBlock"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardFourImageTextModule:
    """
    Four standard images with text, presented across a single row.
    """

    block1: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block2: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block3: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block4: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardFourImageTextQuadrantModule:
    """
    Four standard images with text, presented on a grid of four quadrants.
    """

    block1: "StandardImageTextBlock" = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block2: "StandardImageTextBlock" = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block3: "StandardImageTextBlock" = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block4: "StandardImageTextBlock" = attrs.field()
    """
    The A+ Content standard image and text box block.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardHeaderImageTextModule:
    """
    Standard headline text, an image, and body text.
    """

    block: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardHeaderTextListBlock:
    """
    The A+ standard fixed-length list of text, with a related headline.
    """

    block: Optional["StandardTextListBlock"] = attrs.field()
    """
    The A+ Content standard fixed length list of text, usually presented as bullet points.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardImageCaptionBlock:
    """
    The A+ Content standard image and caption block.
    """

    caption: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    image: Optional["ImageComponent"] = attrs.field()
    """
    A reference to an image, hosted in the A+ Content media library.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardImageSidebarModule:
    """
    Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar.
    """

    description_list_block: Optional["StandardTextListBlock"] = attrs.field()
    """
    The A+ Content standard fixed length list of text, usually presented as bullet points.
    """

    description_text_block: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    image_caption_block: Optional["StandardImageCaptionBlock"] = attrs.field()
    """
    The A+ Content standard image and caption block.
    """

    sidebar_image_text_block: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    sidebar_list_block: Optional["StandardTextListBlock"] = attrs.field()
    """
    The A+ Content standard fixed length list of text, usually presented as bullet points.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardImageTextBlock:
    """
    The A+ Content standard image and text box block.
    """

    body: Optional["ParagraphComponent"] = attrs.field()
    """
    A list of rich text content, usually presented in a text box.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    image: Optional["ImageComponent"] = attrs.field()
    """
    A reference to an image, hosted in the A+ Content media library.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardImageTextCaptionBlock:
    """
    The A+ Content standard image and text block, with a related caption. The caption may not display on all devices.
    """

    block: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    caption: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardImageTextOverlayModule:
    """
    A standard background image with a floating text box.
    """

    block: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    overlay_color_type: "ColorType" = attrs.field()
    """
    The relative color scheme of content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardMultipleImageTextModule:
    """
    Standard images with text, presented one at a time. The user clicks on thumbnails to view each block.
    """

    blocks: Optional[List["StandardImageTextCaptionBlock"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardProductDescriptionModule:
    """
    Standard product description text.
    """

    body: "ParagraphComponent" = attrs.field()
    """
    A list of rich text content, usually presented in a text box.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardSingleImageHighlightsModule:
    """
    A standard image with several paragraphs and a bulleted list.
    """

    bulleted_list_block: Optional["StandardHeaderTextListBlock"] = attrs.field()
    """
    The A+ standard fixed-length list of text, with a related headline.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    image: Optional["ImageComponent"] = attrs.field()
    """
    A reference to an image, hosted in the A+ Content media library.
    """

    text_block1: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    text_block2: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    text_block3: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardSingleImageSpecsDetailModule:
    """
    A standard image with paragraphs and a bulleted list, and extra space for technical details.
    """

    description_block1: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    description_block2: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    description_headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    image: Optional["ImageComponent"] = attrs.field()
    """
    A reference to an image, hosted in the A+ Content media library.
    """

    specification_headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    specification_list_block: Optional["StandardHeaderTextListBlock"] = attrs.field()
    """
    The A+ standard fixed-length list of text, with a related headline.
    """

    specification_text_block: Optional["StandardTextBlock"] = attrs.field()
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardSingleSideImageModule:
    """
    A standard headline and body text with an image on the side.
    """

    block: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    image_position_type: "PositionType" = attrs.field()
    """
    The relative positioning of content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardTechSpecsModule:
    """
    The standard table of technical feature names and definitions.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    specification_list: List["StandardTextPairBlock"] = attrs.field()
    """
    The specification list.

    Extra fields:
    {'maxItems': 16, 'minItems': 4}
    """

    table_count: Optional[int] = attrs.field()
    """
    The number of tables to present. Features are evenly divided between the tables.

    Extra fields:
    {'maximum': 2.0, 'minimum': 1.0}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardTextBlock:
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    body: Optional["ParagraphComponent"] = attrs.field()
    """
    A list of rich text content, usually presented in a text box.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardTextListBlock:
    """
    The A+ Content standard fixed length list of text, usually presented as bullet points.
    """

    text_list: List["TextItem"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardTextModule:
    """
    A standard headline and body text.
    """

    body: "ParagraphComponent" = attrs.field()
    """
    A list of rich text content, usually presented in a text box.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardTextPairBlock:
    """
    The A+ Content standard label and description block, comprised of a pair of text components.
    """

    description: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """

    label: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardThreeImageTextModule:
    """
    Three standard images with text, presented across a single row.
    """

    block1: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block2: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    block3: Optional["StandardImageTextBlock"] = attrs.field()
    """
    The A+ Content standard image and text box block.
    """

    headline: Optional["TextComponent"] = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TextComponent:
    """
    Rich text content.
    """

    decorator_set: Optional[List["Decorator"]] = attrs.field()
    """
    A set of content decorators.
    """

    value: str = attrs.field()
    """
    The actual plain text.

    Extra fields:
    {'maxLength': 10000, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TextItem:
    """
    Rich positional text, usually presented as a collection of bullet points.
    """

    position: int = attrs.field()
    """
    The rank or index of this text item within the collection. Different items cannot occupy the same position within a single collection.

    Extra fields:
    {'maximum': 100.0, 'minimum': 1.0}
    """

    text: "TextComponent" = attrs.field()
    """
    Rich text content.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_content_document_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_content_document_params = (  # name, param in
        ("marketplaceId", "query"),
        ("contentDocument", "body"),
    )

    _create_content_document_responses = {
        200: PostContentDocumentResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_content_document_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_content_document_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("includedDataSet", "query"),
    )

    _get_content_document_responses = {
        200: GetContentDocumentResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_content_document_asin_relations_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _list_content_document_asin_relations_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("includedDataSet", "query"),
        ("asinSet", "query"),
        ("pageToken", "query"),
    )

    _list_content_document_asin_relations_responses = {
        200: ListContentDocumentAsinRelationsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
            url,
            "POST",
            values,
            self._post_content_document_approval_submission_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _post_content_document_approval_submission_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
    )

    _post_content_document_approval_submission_responses = {
        200: PostContentDocumentApprovalSubmissionResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._post_content_document_asin_relations_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _post_content_document_asin_relations_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("asinSet", "body"),
    )

    _post_content_document_asin_relations_responses = {
        200: PostContentDocumentAsinRelationsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
            url,
            "POST",
            values,
            self._post_content_document_suspend_submission_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _post_content_document_suspend_submission_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
    )

    _post_content_document_suspend_submission_responses = {
        200: PostContentDocumentSuspendSubmissionResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._search_content_documents_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _search_content_documents_params = (  # name, param in
        ("marketplaceId", "query"),
        ("pageToken", "query"),
    )

    _search_content_documents_responses = {
        200: SearchContentDocumentsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._search_content_publish_records_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _search_content_publish_records_params = (  # name, param in
        ("marketplaceId", "query"),
        ("asin", "query"),
        ("pageToken", "query"),
    )

    _search_content_publish_records_responses = {
        200: SearchContentPublishRecordsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._update_content_document_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _update_content_document_params = (  # name, param in
        ("contentReferenceKey", "path"),
        ("marketplaceId", "query"),
        ("contentDocument", "body"),
    )

    _update_content_document_responses = {
        200: PostContentDocumentResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        410: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

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
            url,
            "POST",
            values,
            self._validate_content_document_asin_relations_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _validate_content_document_asin_relations_params = (  # name, param in
        ("marketplaceId", "query"),
        ("asinSet", "query"),
        ("contentDocument", "body"),
    )

    _validate_content_document_asin_relations_responses = {
        200: ValidateContentDocumentAsinRelationsResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
