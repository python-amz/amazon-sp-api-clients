from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class AplusResponse:
    """
    The base response data for all A+ Content operations when a request is successful or partially successful. Individual operations may extend this with additional data.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "warnings" in data:
            self.warnings: MessageSet = MessageSet(data["warnings"])
        else:
            self.warnings: MessageSet = None


class ErrorList:
    """
    The error response for when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

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


class ContentMetadataRecord:
    """
    The metadata for an A+ Content document, with additional information for content management.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentReferenceKey" in data:
            self.contentReferenceKey: ContentReferenceKey = ContentReferenceKey(data["contentReferenceKey"])
        else:
            self.contentReferenceKey: ContentReferenceKey = None
        if "contentMetadata" in data:
            self.contentMetadata: ContentMetadata = ContentMetadata(data["contentMetadata"])
        else:
            self.contentMetadata: ContentMetadata = None


class ContentMetadata:
    """
    The metadata of an A+ Content document.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = MarketplaceId(data["marketplaceId"])
        else:
            self.marketplaceId: MarketplaceId = None
        if "status" in data:
            self.status: ContentStatus = ContentStatus(data["status"])
        else:
            self.status: ContentStatus = None
        if "badgeSet" in data:
            self.badgeSet: ContentBadgeSet = ContentBadgeSet(data["badgeSet"])
        else:
            self.badgeSet: ContentBadgeSet = None
        if "updateTime" in data:
            self.updateTime: str = str(data["updateTime"])
        else:
            self.updateTime: str = None


class AsinMetadata:
    """
    The A+ Content ASIN with additional metadata for content management. If you don't include the `includedDataSet` parameter in a call to the listContentDocumentAsinRelations operation, the related ASINs are returned without metadata.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asin" in data:
            self.asin: Asin = Asin(data["asin"])
        else:
            self.asin: Asin = None
        if "badgeSet" in data:
            self.badgeSet: AsinBadgeSet = AsinBadgeSet(data["badgeSet"])
        else:
            self.badgeSet: AsinBadgeSet = None
        if "parent" in data:
            self.parent: Asin = Asin(data["parent"])
        else:
            self.parent: Asin = None
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "imageUrl" in data:
            self.imageUrl: str = str(data["imageUrl"])
        else:
            self.imageUrl: str = None
        if "contentReferenceKeySet" in data:
            self.contentReferenceKeySet: ContentReferenceKeySet = ContentReferenceKeySet(data["contentReferenceKeySet"])
        else:
            self.contentReferenceKeySet: ContentReferenceKeySet = None


class PublishRecord:
    """
    The full context for an A+ Content publishing event.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = MarketplaceId(data["marketplaceId"])
        else:
            self.marketplaceId: MarketplaceId = None
        if "locale" in data:
            self.locale: LanguageTag = LanguageTag(data["locale"])
        else:
            self.locale: LanguageTag = None
        if "asin" in data:
            self.asin: Asin = Asin(data["asin"])
        else:
            self.asin: Asin = None
        if "contentType" in data:
            self.contentType: ContentType = ContentType(data["contentType"])
        else:
            self.contentType: ContentType = None
        if "contentSubType" in data:
            self.contentSubType: ContentSubType = ContentSubType(data["contentSubType"])
        else:
            self.contentSubType: ContentSubType = None
        if "contentReferenceKey" in data:
            self.contentReferenceKey: ContentReferenceKey = ContentReferenceKey(data["contentReferenceKey"])
        else:
            self.contentReferenceKey: ContentReferenceKey = None


class ImageCropSpecification:
    """
    The instructions for optionally cropping an image. If no cropping is desired, set the dimensions to the original image size. If the image is cropped and no offset values are provided, then the coordinates of the top left corner of the cropped image, relative to the original image, are defaulted to (0,0).
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "size" in data:
            self.size: ImageDimensions = ImageDimensions(data["size"])
        else:
            self.size: ImageDimensions = None
        if "offset" in data:
            self.offset: ImageOffsets = ImageOffsets(data["offset"])
        else:
            self.offset: ImageOffsets = None


class ImageDimensions:
    """
    The dimensions extending from the top left corner of the cropped image, or the top left corner of the original image if there is no cropping. Only `pixels` is allowed as the units value for ImageDimensions.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "width" in data:
            self.width: IntegerWithUnits = IntegerWithUnits(data["width"])
        else:
            self.width: IntegerWithUnits = None
        if "height" in data:
            self.height: IntegerWithUnits = IntegerWithUnits(data["height"])
        else:
            self.height: IntegerWithUnits = None


class ImageOffsets:
    """
    The top left corner of the cropped image, specified in the original image's coordinate space.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "x" in data:
            self.x: IntegerWithUnits = IntegerWithUnits(data["x"])
        else:
            self.x: IntegerWithUnits = None
        if "y" in data:
            self.y: IntegerWithUnits = IntegerWithUnits(data["y"])
        else:
            self.y: IntegerWithUnits = None


class IntegerWithUnits:
    """
    A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "value" in data:
            self.value: int = int(data["value"])
        else:
            self.value: int = None
        if "units" in data:
            self.units: str = str(data["units"])
        else:
            self.units: str = None


class ContentRecord:
    """
    A content document with additional information for content management.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentReferenceKey" in data:
            self.contentReferenceKey: ContentReferenceKey = ContentReferenceKey(data["contentReferenceKey"])
        else:
            self.contentReferenceKey: ContentReferenceKey = None
        if "contentMetadata" in data:
            self.contentMetadata: ContentMetadata = ContentMetadata(data["contentMetadata"])
        else:
            self.contentMetadata: ContentMetadata = None
        if "contentDocument" in data:
            self.contentDocument: ContentDocument = ContentDocument(data["contentDocument"])
        else:
            self.contentDocument: ContentDocument = None


class ContentDocument:
    """
    The A+ Content document. This is the enhanced content that is published to product detail pages.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "contentType" in data:
            self.contentType: ContentType = ContentType(data["contentType"])
        else:
            self.contentType: ContentType = None
        if "contentSubType" in data:
            self.contentSubType: ContentSubType = ContentSubType(data["contentSubType"])
        else:
            self.contentSubType: ContentSubType = None
        if "locale" in data:
            self.locale: LanguageTag = LanguageTag(data["locale"])
        else:
            self.locale: LanguageTag = None
        if "contentModuleList" in data:
            self.contentModuleList: ContentModuleList = ContentModuleList(data["contentModuleList"])
        else:
            self.contentModuleList: ContentModuleList = None


class ContentModule:
    """
    An A+ Content module. An A+ Content document is composed of content modules. The contentModuleType property selects which content module types to use.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentModuleType" in data:
            self.contentModuleType: ContentModuleType = ContentModuleType(data["contentModuleType"])
        else:
            self.contentModuleType: ContentModuleType = None
        if "standardCompanyLogo" in data:
            self.standardCompanyLogo: StandardCompanyLogoModule = StandardCompanyLogoModule(data["standardCompanyLogo"])
        else:
            self.standardCompanyLogo: StandardCompanyLogoModule = None
        if "standardComparisonTable" in data:
            self.standardComparisonTable: StandardComparisonTableModule = StandardComparisonTableModule(
                data["standardComparisonTable"]
            )
        else:
            self.standardComparisonTable: StandardComparisonTableModule = None
        if "standardFourImageText" in data:
            self.standardFourImageText: StandardFourImageTextModule = StandardFourImageTextModule(
                data["standardFourImageText"]
            )
        else:
            self.standardFourImageText: StandardFourImageTextModule = None
        if "standardFourImageTextQuadrant" in data:
            self.standardFourImageTextQuadrant: StandardFourImageTextQuadrantModule = (
                StandardFourImageTextQuadrantModule(data["standardFourImageTextQuadrant"])
            )
        else:
            self.standardFourImageTextQuadrant: StandardFourImageTextQuadrantModule = None
        if "standardHeaderImageText" in data:
            self.standardHeaderImageText: StandardHeaderImageTextModule = StandardHeaderImageTextModule(
                data["standardHeaderImageText"]
            )
        else:
            self.standardHeaderImageText: StandardHeaderImageTextModule = None
        if "standardImageSidebar" in data:
            self.standardImageSidebar: StandardImageSidebarModule = StandardImageSidebarModule(
                data["standardImageSidebar"]
            )
        else:
            self.standardImageSidebar: StandardImageSidebarModule = None
        if "standardImageTextOverlay" in data:
            self.standardImageTextOverlay: StandardImageTextOverlayModule = StandardImageTextOverlayModule(
                data["standardImageTextOverlay"]
            )
        else:
            self.standardImageTextOverlay: StandardImageTextOverlayModule = None
        if "standardMultipleImageText" in data:
            self.standardMultipleImageText: StandardMultipleImageTextModule = StandardMultipleImageTextModule(
                data["standardMultipleImageText"]
            )
        else:
            self.standardMultipleImageText: StandardMultipleImageTextModule = None
        if "standardProductDescription" in data:
            self.standardProductDescription: StandardProductDescriptionModule = StandardProductDescriptionModule(
                data["standardProductDescription"]
            )
        else:
            self.standardProductDescription: StandardProductDescriptionModule = None
        if "standardSingleImageHighlights" in data:
            self.standardSingleImageHighlights: StandardSingleImageHighlightsModule = (
                StandardSingleImageHighlightsModule(data["standardSingleImageHighlights"])
            )
        else:
            self.standardSingleImageHighlights: StandardSingleImageHighlightsModule = None
        if "standardSingleImageSpecsDetail" in data:
            self.standardSingleImageSpecsDetail: StandardSingleImageSpecsDetailModule = (
                StandardSingleImageSpecsDetailModule(data["standardSingleImageSpecsDetail"])
            )
        else:
            self.standardSingleImageSpecsDetail: StandardSingleImageSpecsDetailModule = None
        if "standardSingleSideImage" in data:
            self.standardSingleSideImage: StandardSingleSideImageModule = StandardSingleSideImageModule(
                data["standardSingleSideImage"]
            )
        else:
            self.standardSingleSideImage: StandardSingleSideImageModule = None
        if "standardTechSpecs" in data:
            self.standardTechSpecs: StandardTechSpecsModule = StandardTechSpecsModule(data["standardTechSpecs"])
        else:
            self.standardTechSpecs: StandardTechSpecsModule = None
        if "standardText" in data:
            self.standardText: StandardTextModule = StandardTextModule(data["standardText"])
        else:
            self.standardText: StandardTextModule = None
        if "standardThreeImageText" in data:
            self.standardThreeImageText: StandardThreeImageTextModule = StandardThreeImageTextModule(
                data["standardThreeImageText"]
            )
        else:
            self.standardThreeImageText: StandardThreeImageTextModule = None


class StandardCompanyLogoModule:
    """
    The standard company logo image.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "companyLogo" in data:
            self.companyLogo: ImageComponent = ImageComponent(data["companyLogo"])
        else:
            self.companyLogo: ImageComponent = None


class StandardComparisonTableModule:
    """
    The standard product comparison table.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "productColumns" in data:
            self.productColumns: _List[StandardComparisonProductBlock] = [
                StandardComparisonProductBlock(datum) for datum in data["productColumns"]
            ]
        else:
            self.productColumns: _List[StandardComparisonProductBlock] = []
        if "metricRowLabels" in data:
            self.metricRowLabels: _List[PlainTextItem] = [PlainTextItem(datum) for datum in data["metricRowLabels"]]
        else:
            self.metricRowLabels: _List[PlainTextItem] = []


class StandardFourImageTextModule:
    """
    Four standard images with text, presented across a single row.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "block1" in data:
            self.block1: StandardImageTextBlock = StandardImageTextBlock(data["block1"])
        else:
            self.block1: StandardImageTextBlock = None
        if "block2" in data:
            self.block2: StandardImageTextBlock = StandardImageTextBlock(data["block2"])
        else:
            self.block2: StandardImageTextBlock = None
        if "block3" in data:
            self.block3: StandardImageTextBlock = StandardImageTextBlock(data["block3"])
        else:
            self.block3: StandardImageTextBlock = None
        if "block4" in data:
            self.block4: StandardImageTextBlock = StandardImageTextBlock(data["block4"])
        else:
            self.block4: StandardImageTextBlock = None


class StandardFourImageTextQuadrantModule:
    """
    Four standard images with text, presented on a grid of four quadrants.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "block1" in data:
            self.block1: StandardImageTextBlock = StandardImageTextBlock(data["block1"])
        else:
            self.block1: StandardImageTextBlock = None
        if "block2" in data:
            self.block2: StandardImageTextBlock = StandardImageTextBlock(data["block2"])
        else:
            self.block2: StandardImageTextBlock = None
        if "block3" in data:
            self.block3: StandardImageTextBlock = StandardImageTextBlock(data["block3"])
        else:
            self.block3: StandardImageTextBlock = None
        if "block4" in data:
            self.block4: StandardImageTextBlock = StandardImageTextBlock(data["block4"])
        else:
            self.block4: StandardImageTextBlock = None


class StandardHeaderImageTextModule:
    """
    Standard headline text, an image, and body text.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "block" in data:
            self.block: StandardImageTextBlock = StandardImageTextBlock(data["block"])
        else:
            self.block: StandardImageTextBlock = None


class StandardImageSidebarModule:
    """
    Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "imageCaptionBlock" in data:
            self.imageCaptionBlock: StandardImageCaptionBlock = StandardImageCaptionBlock(data["imageCaptionBlock"])
        else:
            self.imageCaptionBlock: StandardImageCaptionBlock = None
        if "descriptionTextBlock" in data:
            self.descriptionTextBlock: StandardTextBlock = StandardTextBlock(data["descriptionTextBlock"])
        else:
            self.descriptionTextBlock: StandardTextBlock = None
        if "descriptionListBlock" in data:
            self.descriptionListBlock: StandardTextListBlock = StandardTextListBlock(data["descriptionListBlock"])
        else:
            self.descriptionListBlock: StandardTextListBlock = None
        if "sidebarImageTextBlock" in data:
            self.sidebarImageTextBlock: StandardImageTextBlock = StandardImageTextBlock(data["sidebarImageTextBlock"])
        else:
            self.sidebarImageTextBlock: StandardImageTextBlock = None
        if "sidebarListBlock" in data:
            self.sidebarListBlock: StandardTextListBlock = StandardTextListBlock(data["sidebarListBlock"])
        else:
            self.sidebarListBlock: StandardTextListBlock = None


class StandardImageTextOverlayModule:
    """
    A standard background image with a floating text box.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "overlayColorType" in data:
            self.overlayColorType: ColorType = ColorType(data["overlayColorType"])
        else:
            self.overlayColorType: ColorType = None
        if "block" in data:
            self.block: StandardImageTextBlock = StandardImageTextBlock(data["block"])
        else:
            self.block: StandardImageTextBlock = None


class StandardMultipleImageTextModule:
    """
    Standard images with text, presented one at a time. The user clicks on thumbnails to view each block.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "blocks" in data:
            self.blocks: _List[StandardImageTextCaptionBlock] = [
                StandardImageTextCaptionBlock(datum) for datum in data["blocks"]
            ]
        else:
            self.blocks: _List[StandardImageTextCaptionBlock] = []


class StandardProductDescriptionModule:
    """
    Standard product description text.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "body" in data:
            self.body: ParagraphComponent = ParagraphComponent(data["body"])
        else:
            self.body: ParagraphComponent = None


class StandardSingleImageHighlightsModule:
    """
    A standard image with several paragraphs and a bulleted list.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "image" in data:
            self.image: ImageComponent = ImageComponent(data["image"])
        else:
            self.image: ImageComponent = None
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "textBlock1" in data:
            self.textBlock1: StandardTextBlock = StandardTextBlock(data["textBlock1"])
        else:
            self.textBlock1: StandardTextBlock = None
        if "textBlock2" in data:
            self.textBlock2: StandardTextBlock = StandardTextBlock(data["textBlock2"])
        else:
            self.textBlock2: StandardTextBlock = None
        if "textBlock3" in data:
            self.textBlock3: StandardTextBlock = StandardTextBlock(data["textBlock3"])
        else:
            self.textBlock3: StandardTextBlock = None
        if "bulletedListBlock" in data:
            self.bulletedListBlock: StandardHeaderTextListBlock = StandardHeaderTextListBlock(data["bulletedListBlock"])
        else:
            self.bulletedListBlock: StandardHeaderTextListBlock = None


class StandardSingleImageSpecsDetailModule:
    """
    A standard image with paragraphs and a bulleted list, and extra space for technical details.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "image" in data:
            self.image: ImageComponent = ImageComponent(data["image"])
        else:
            self.image: ImageComponent = None
        if "descriptionHeadline" in data:
            self.descriptionHeadline: TextComponent = TextComponent(data["descriptionHeadline"])
        else:
            self.descriptionHeadline: TextComponent = None
        if "descriptionBlock1" in data:
            self.descriptionBlock1: StandardTextBlock = StandardTextBlock(data["descriptionBlock1"])
        else:
            self.descriptionBlock1: StandardTextBlock = None
        if "descriptionBlock2" in data:
            self.descriptionBlock2: StandardTextBlock = StandardTextBlock(data["descriptionBlock2"])
        else:
            self.descriptionBlock2: StandardTextBlock = None
        if "specificationHeadline" in data:
            self.specificationHeadline: TextComponent = TextComponent(data["specificationHeadline"])
        else:
            self.specificationHeadline: TextComponent = None
        if "specificationListBlock" in data:
            self.specificationListBlock: StandardHeaderTextListBlock = StandardHeaderTextListBlock(
                data["specificationListBlock"]
            )
        else:
            self.specificationListBlock: StandardHeaderTextListBlock = None
        if "specificationTextBlock" in data:
            self.specificationTextBlock: StandardTextBlock = StandardTextBlock(data["specificationTextBlock"])
        else:
            self.specificationTextBlock: StandardTextBlock = None


class StandardSingleSideImageModule:
    """
    A standard headline and body text with an image on the side.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "imagePositionType" in data:
            self.imagePositionType: PositionType = PositionType(data["imagePositionType"])
        else:
            self.imagePositionType: PositionType = None
        if "block" in data:
            self.block: StandardImageTextBlock = StandardImageTextBlock(data["block"])
        else:
            self.block: StandardImageTextBlock = None


class StandardTechSpecsModule:
    """
    The standard table of technical feature names and definitions.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "specificationList" in data:
            self.specificationList: _List[StandardTextPairBlock] = [
                StandardTextPairBlock(datum) for datum in data["specificationList"]
            ]
        else:
            self.specificationList: _List[StandardTextPairBlock] = []
        if "tableCount" in data:
            self.tableCount: int = int(data["tableCount"])
        else:
            self.tableCount: int = None


class StandardTextModule:
    """
    A standard headline and body text.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "body" in data:
            self.body: ParagraphComponent = ParagraphComponent(data["body"])
        else:
            self.body: ParagraphComponent = None


class StandardThreeImageTextModule:
    """
    Three standard images with text, presented across a single row.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "block1" in data:
            self.block1: StandardImageTextBlock = StandardImageTextBlock(data["block1"])
        else:
            self.block1: StandardImageTextBlock = None
        if "block2" in data:
            self.block2: StandardImageTextBlock = StandardImageTextBlock(data["block2"])
        else:
            self.block2: StandardImageTextBlock = None
        if "block3" in data:
            self.block3: StandardImageTextBlock = StandardImageTextBlock(data["block3"])
        else:
            self.block3: StandardImageTextBlock = None


class StandardComparisonProductBlock:
    """
    The A+ Content standard comparison product block.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "position" in data:
            self.position: int = int(data["position"])
        else:
            self.position: int = None
        if "image" in data:
            self.image: ImageComponent = ImageComponent(data["image"])
        else:
            self.image: ImageComponent = None
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "asin" in data:
            self.asin: Asin = Asin(data["asin"])
        else:
            self.asin: Asin = None
        if "highlight" in data:
            self.highlight: bool = convert_bool(data["highlight"])
        else:
            self.highlight: bool = None
        if "metrics" in data:
            self.metrics: _List[PlainTextItem] = [PlainTextItem(datum) for datum in data["metrics"]]
        else:
            self.metrics: _List[PlainTextItem] = []


class StandardHeaderTextListBlock:
    """
    The A+ standard fixed-length list of text, with a related headline.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "block" in data:
            self.block: StandardTextListBlock = StandardTextListBlock(data["block"])
        else:
            self.block: StandardTextListBlock = None


class StandardTextListBlock:
    """
    The A+ Content standard fixed length list of text, usually presented as bullet points.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "textList" in data:
            self.textList: _List[TextItem] = [TextItem(datum) for datum in data["textList"]]
        else:
            self.textList: _List[TextItem] = []


class StandardImageTextCaptionBlock:
    """
    The A+ Content standard image and text block, with a related caption. The caption may not display on all devices.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "block" in data:
            self.block: StandardImageTextBlock = StandardImageTextBlock(data["block"])
        else:
            self.block: StandardImageTextBlock = None
        if "caption" in data:
            self.caption: TextComponent = TextComponent(data["caption"])
        else:
            self.caption: TextComponent = None


class StandardImageCaptionBlock:
    """
    The A+ Content standard image and caption block.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "image" in data:
            self.image: ImageComponent = ImageComponent(data["image"])
        else:
            self.image: ImageComponent = None
        if "caption" in data:
            self.caption: TextComponent = TextComponent(data["caption"])
        else:
            self.caption: TextComponent = None


class StandardImageTextBlock:
    """
    The A+ Content standard image and text box block.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "image" in data:
            self.image: ImageComponent = ImageComponent(data["image"])
        else:
            self.image: ImageComponent = None
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "body" in data:
            self.body: ParagraphComponent = ParagraphComponent(data["body"])
        else:
            self.body: ParagraphComponent = None


class StandardTextBlock:
    """
    The A+ Content standard text box block, comprised of a paragraph with a headline.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "headline" in data:
            self.headline: TextComponent = TextComponent(data["headline"])
        else:
            self.headline: TextComponent = None
        if "body" in data:
            self.body: ParagraphComponent = ParagraphComponent(data["body"])
        else:
            self.body: ParagraphComponent = None


class StandardTextPairBlock:
    """
    The A+ Content standard label and description block, comprised of a pair of text components.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "label" in data:
            self.label: TextComponent = TextComponent(data["label"])
        else:
            self.label: TextComponent = None
        if "description" in data:
            self.description: TextComponent = TextComponent(data["description"])
        else:
            self.description: TextComponent = None


class TextItem:
    """
    Rich positional text, usually presented as a collection of bullet points.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "position" in data:
            self.position: int = int(data["position"])
        else:
            self.position: int = None
        if "text" in data:
            self.text: TextComponent = TextComponent(data["text"])
        else:
            self.text: TextComponent = None


class PlainTextItem:
    """
    Plain positional text, used in collections of brief labels and descriptors.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "position" in data:
            self.position: int = int(data["position"])
        else:
            self.position: int = None
        if "value" in data:
            self.value: str = str(data["value"])
        else:
            self.value: str = None


class ImageComponent:
    """
    A reference to an image, hosted in the A+ Content media library.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = str(data["uploadDestinationId"])
        else:
            self.uploadDestinationId: str = None
        if "imageCropSpecification" in data:
            self.imageCropSpecification: ImageCropSpecification = ImageCropSpecification(data["imageCropSpecification"])
        else:
            self.imageCropSpecification: ImageCropSpecification = None
        if "altText" in data:
            self.altText: str = str(data["altText"])
        else:
            self.altText: str = None


class ParagraphComponent:
    """
    A list of rich text content, usually presented in a text box.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "textList" in data:
            self.textList: _List[TextComponent] = [TextComponent(datum) for datum in data["textList"]]
        else:
            self.textList: _List[TextComponent] = []


class TextComponent:
    """
    Rich text content.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "value" in data:
            self.value: str = str(data["value"])
        else:
            self.value: str = None
        if "decoratorSet" in data:
            self.decoratorSet: DecoratorSet = DecoratorSet(data["decoratorSet"])
        else:
            self.decoratorSet: DecoratorSet = None


class Decorator:
    """
    A decorator applied to a content string value in order to create rich text.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "type" in data:
            self.type: DecoratorType = DecoratorType(data["type"])
        else:
            self.type: DecoratorType = None
        if "offset" in data:
            self.offset: int = int(data["offset"])
        else:
            self.offset: int = None
        if "length" in data:
            self.length: int = int(data["length"])
        else:
            self.length: int = None
        if "depth" in data:
            self.depth: int = int(data["depth"])
        else:
            self.depth: int = None


class PostContentDocumentRequest:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentDocument" in data:
            self.contentDocument: ContentDocument = ContentDocument(data["contentDocument"])
        else:
            self.contentDocument: ContentDocument = None


class PostContentDocumentAsinRelationsRequest:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asinSet" in data:
            self.asinSet: AsinSet = AsinSet(data["asinSet"])
        else:
            self.asinSet: AsinSet = None


class MessageSet(list, _List["Error"]):
    """
    A set of messages to the user, such as warnings or comments.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class ContentMetadataRecordList(list, _List["ContentMetadataRecord"]):
    """
    A list of A+ Content metadata records.
    """

    def __init__(self, data):
        super().__init__([ContentMetadataRecord(datum) for datum in data])
        self.data = data


class ContentBadgeSet(list, _List["ContentBadge"]):
    """
    The set of content badges.
    """

    def __init__(self, data):
        super().__init__([ContentBadge(datum) for datum in data])
        self.data = data


class AsinBadgeSet(list, _List["AsinBadge"]):
    """
    The set of ASIN badges.
    """

    def __init__(self, data):
        super().__init__([AsinBadge(datum) for datum in data])
        self.data = data


class AsinSet(list, _List["Asin"]):
    """
    The set of ASINs.
    """

    def __init__(self, data):
        super().__init__([Asin(datum) for datum in data])
        self.data = data


class AsinMetadataSet(list, _List["AsinMetadata"]):
    """
    The set of ASIN metadata.
    """

    def __init__(self, data):
        super().__init__([AsinMetadata(datum) for datum in data])
        self.data = data


class PublishRecordList(list, _List["PublishRecord"]):
    """
    A list of A+ Content publishing records.
    """

    def __init__(self, data):
        super().__init__([PublishRecord(datum) for datum in data])
        self.data = data


class ContentReferenceKeySet(list, _List["ContentReferenceKey"]):
    """
    A set of content reference keys.
    """

    def __init__(self, data):
        super().__init__([ContentReferenceKey(datum) for datum in data])
        self.data = data


class ContentModuleList(list, _List["ContentModule"]):
    """
    A list of A+ Content modules.
    """

    def __init__(self, data):
        super().__init__([ContentModule(datum) for datum in data])
        self.data = data


class DecoratorSet(list, _List["Decorator"]):
    """
    A set of content decorators.
    """

    def __init__(self, data):
        super().__init__([Decorator(datum) for datum in data])
        self.data = data


class ContentType(str):
    """
    The A+ Content document type.
    """


class ContentSubType(str):
    """
    The A+ Content document subtype. This represents a special-purpose type of an A+ Content document. Not every A+ Content document type will have a subtype, and subtypes may change at any time.
    """


class ContentStatus(str):
    """
    The submission status of the content document.
    """


class ContentBadge(str):
    """
    A flag that provides additional information about an A+ Content document.
    """


class AsinBadge(str):
    """
    A flag that provides additional information about an ASIN. This is contextual and may change depending on the request that generated it.
    """


class MarketplaceId(str):
    """
    The identifier for the marketplace where the A+ Content is published.
    """


class LanguageTag(str):
    """
        The IETF language tag. This only supports the primary language subtag with one secondary language subtag. The secondary language subtag is almost always a regional designation. This does not support additional subtags beyond the primary and secondary subtags.
    **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$
    """


class Asin(str):
    """
    The Amazon Standard Identification Number (ASIN).
    """


class ContentReferenceKey(str):
    """
    A unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """


class PageToken(str):
    """
    A page token that is returned when the results of the call exceed the page size. To get another page of results, call the operation again, passing in this value with the pageToken parameter.
    """


class ContentModuleType(str):
    """
    The type of A+ Content module.
    """


class ColorType(str):
    """
    The relative color scheme of content.
    """


class PositionType(str):
    """
    The relative positioning of content.
    """


class DecoratorType(str):
    """
    The type of rich text decorator.
    """


class contentReferenceKey(str):
    """
    The unique reference key for the A+ Content document. A content reference key cannot form a permalink and may change in the future. A content reference key is not guaranteed to match any A+ content identifier.
    """


class marketplaceId(str):
    """
    The identifier for the marketplace where the A+ Content is published.
    """


class pageToken(str):
    """
    A page token from the nextPageToken response element returned by your previous call to this operation. nextPageToken is returned when the results of a call exceed the page size. To get the next page of results, call the operation and include pageToken as the only parameter. Specifying pageToken with any other parameter will cause the request to fail. When no nextPageToken value is returned there are no more pages to return. A pageToken value is not usable across different operations.
    """


class asinSet(list):
    """
    The set of ASINs.
    """


class asin(str):
    """
    The Amazon Standard Identification Number (ASIN).
    """


class getContentDocumentIncludedDataSet(list):
    """
    The set of A+ data types to include in the response.
    """


class listContentDocumentAsinRelationsIncludedDataSet(list):
    """
    The set of A+ data types to include in the response.
    """


class AplusPaginatedResponse:
    """
    The base response data for paginated A+ Content operations. Individual operations may extend this with additional data. If nextPageToken is not returned, there are no more pages to return.
    """

    def __init__(self, data):
        if "nextPageToken" in data:
            self.nextPageToken: PageToken = PageToken(data.pop("nextPageToken"))
        else:
            self.nextPageToken: PageToken = None
        self.data = data
        super().__init__(data)


class SearchContentDocumentsResponse:
    """ """

    def __init__(self, data):
        if "contentMetadataRecords" in data:
            self.contentMetadataRecords: ContentMetadataRecordList = ContentMetadataRecordList(
                data.pop("contentMetadataRecords")
            )
        else:
            self.contentMetadataRecords: ContentMetadataRecordList = None
        self.data = data
        super().__init__(data)


class GetContentDocumentResponse:
    """ """

    def __init__(self, data):
        if "contentRecord" in data:
            self.contentRecord: ContentRecord = ContentRecord(data.pop("contentRecord"))
        else:
            self.contentRecord: ContentRecord = None
        self.data = data
        super().__init__(data)


class PostContentDocumentResponse:
    """ """

    def __init__(self, data):
        if "contentReferenceKey" in data:
            self.contentReferenceKey: ContentReferenceKey = ContentReferenceKey(data.pop("contentReferenceKey"))
        else:
            self.contentReferenceKey: ContentReferenceKey = None
        self.data = data
        super().__init__(data)


class ListContentDocumentAsinRelationsResponse:
    """ """

    def __init__(self, data):
        if "asinMetadataSet" in data:
            self.asinMetadataSet: AsinMetadataSet = AsinMetadataSet(data.pop("asinMetadataSet"))
        else:
            self.asinMetadataSet: AsinMetadataSet = None
        self.data = data
        super().__init__(data)


class PostContentDocumentAsinRelationsResponse:
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class ValidateContentDocumentAsinRelationsResponse:
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class SearchContentPublishRecordsResponse:
    """ """

    def __init__(self, data):
        if "publishRecordList" in data:
            self.publishRecordList: PublishRecordList = PublishRecordList(data.pop("publishRecordList"))
        else:
            self.publishRecordList: PublishRecordList = None
        self.data = data
        super().__init__(data)


class PostContentDocumentApprovalSubmissionResponse:
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class PostContentDocumentSuspendSubmissionResponse:
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class AplusContent20201101Client(__BaseClient):
    """
        Returns a list of all A+ Content documents assigned to a selling partner. This operation returns only the metadata of the A+ Content documents. Call the getContentDocument operation to get the actual contents of the A+ Content documents.
    **Usage Plans:**
    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |
    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def searchContentDocuments(
        self,
        marketplaceId: str,
        pageToken: str = None,
    ):
        url = "/aplus/2020-11-01/contentDocuments".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if pageToken is not None:
            params["pageToken"] = pageToken
        response = self.request(url, method="GET", params=params)
        return {
            200: SearchContentDocumentsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Creates a new A+ Content document.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def createContentDocument(
        self,
        data: PostContentDocumentRequest,
        marketplaceId: str,
    ):
        url = "/aplus/2020-11-01/contentDocuments".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="POST", data=params)
        return {
            200: PostContentDocumentResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Returns an A+ Content document, if available.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def getContentDocument(
        self,
        contentReferenceKey: str,
        marketplaceId: str,
        includedDataSet: _List[str],
    ):
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}".format(
            contentReferenceKey=contentReferenceKey,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if includedDataSet is not None:
            params["includedDataSet"] = ",".join(map(str, includedDataSet))
        response = self.request(url, method="GET", params=params)
        return {
            200: GetContentDocumentResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Updates an existing A+ Content document.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def updateContentDocument(
        self,
        data: PostContentDocumentRequest,
        contentReferenceKey: str,
        marketplaceId: str,
    ):
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}".format(
            contentReferenceKey=contentReferenceKey,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="POST", data=params)
        return {
            200: PostContentDocumentResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Returns a list of ASINs related to the specified A+ Content document, if available. If you do not include the asinSet parameter, the operation returns all ASINs related to the content document.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def listContentDocumentAsinRelations(
        self,
        contentReferenceKey: str,
        marketplaceId: str,
        includedDataSet: _List[str] = None,
        asinSet: _List[str] = None,
        pageToken: str = None,
    ):
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins".format(
            contentReferenceKey=contentReferenceKey,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if includedDataSet is not None:
            params["includedDataSet"] = ",".join(map(str, includedDataSet))
        if asinSet is not None:
            params["asinSet"] = ",".join(map(str, asinSet))
        if pageToken is not None:
            params["pageToken"] = pageToken
        response = self.request(url, method="GET", params=params)
        return {
            200: ListContentDocumentAsinRelationsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Replaces all ASINs related to the specified A+ Content document, if available. This may add or remove ASINs, depending on the current set of related ASINs. Removing an ASIN has the side effect of suspending the content document from that ASIN.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def postContentDocumentAsinRelations(
        self,
        data: PostContentDocumentAsinRelationsRequest,
        contentReferenceKey: str,
        marketplaceId: str,
    ):
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins".format(
            contentReferenceKey=contentReferenceKey,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="POST", data=params)
        return {
            200: PostContentDocumentAsinRelationsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Checks if the A+ Content document is valid for use on a set of ASINs.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def validateContentDocumentAsinRelations(
        self,
        data: PostContentDocumentRequest,
        marketplaceId: str,
        asinSet: _List[str] = None,
    ):
        url = "/aplus/2020-11-01/contentAsinValidations".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if asinSet is not None:
            params["asinSet"] = ",".join(map(str, asinSet))
        response = self.request(url, method="POST", data=params)
        return {
            200: ValidateContentDocumentAsinRelationsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Searches for A+ Content publishing records, if available.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def searchContentPublishRecords(
        self,
        marketplaceId: str,
        asin: str,
        pageToken: str = None,
    ):
        url = "/aplus/2020-11-01/contentPublishRecords".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        if asin is not None:
            params["asin"] = asin
        if pageToken is not None:
            params["pageToken"] = pageToken
        response = self.request(url, method="GET", params=params)
        return {
            200: SearchContentPublishRecordsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Submits an A+ Content document for review, approval, and publishing.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def postContentDocumentApprovalSubmission(
        self,
        contentReferenceKey: str,
        marketplaceId: str,
    ):
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions".format(
            contentReferenceKey=contentReferenceKey,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="POST", data=params)
        return {
            200: PostContentDocumentApprovalSubmissionResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    """
    Submits a request to suspend visible A+ Content. This neither deletes the content document nor the ASIN relations.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def postContentDocumentSuspendSubmission(
        self,
        contentReferenceKey: str,
        marketplaceId: str,
    ):
        url = "/aplus/2020-11-01/contentDocuments/{contentReferenceKey}/suspendSubmissions".format(
            contentReferenceKey=contentReferenceKey,
        )
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = marketplaceId
        response = self.request(url, method="POST", data=params)
        return {
            200: PostContentDocumentSuspendSubmissionResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            410: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))
