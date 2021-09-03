from .base import BaseClient as __BaseClient
from typing import List as _List


class AplusResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "warnings" in data:
            self.warnings: MessageSet = MessageSet(data["warnings"])
        else:
            self.warnings: MessageSet = None


class ErrorList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "companyLogo" in data:
            self.companyLogo: ImageComponent = ImageComponent(data["companyLogo"])
        else:
            self.companyLogo: ImageComponent = None


class StandardComparisonTableModule:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "body" in data:
            self.body: ParagraphComponent = ParagraphComponent(data["body"])
        else:
            self.body: ParagraphComponent = None


class StandardSingleImageHighlightsModule:
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
            self.highlight: bool = bool(data["highlight"])
        else:
            self.highlight: bool = None
        if "metrics" in data:
            self.metrics: _List[PlainTextItem] = [PlainTextItem(datum) for datum in data["metrics"]]
        else:
            self.metrics: _List[PlainTextItem] = []


class StandardHeaderTextListBlock:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "textList" in data:
            self.textList: _List[TextItem] = [TextItem(datum) for datum in data["textList"]]
        else:
            self.textList: _List[TextItem] = []


class StandardImageTextCaptionBlock:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "textList" in data:
            self.textList: _List[TextComponent] = [TextComponent(datum) for datum in data["textList"]]
        else:
            self.textList: _List[TextComponent] = []


class TextComponent:
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "contentDocument" in data:
            self.contentDocument: ContentDocument = ContentDocument(data["contentDocument"])
        else:
            self.contentDocument: ContentDocument = None


class PostContentDocumentAsinRelationsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asinSet" in data:
            self.asinSet: AsinSet = AsinSet(data["asinSet"])
        else:
            self.asinSet: AsinSet = None


class MessageSet(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class ContentMetadataRecordList(list, _List["ContentMetadataRecord"]):
    def __init__(self, data):
        super().__init__([ContentMetadataRecord(datum) for datum in data])
        self.data = data


class ContentBadgeSet(list, _List["ContentBadge"]):
    def __init__(self, data):
        super().__init__([ContentBadge(datum) for datum in data])
        self.data = data


class AsinBadgeSet(list, _List["AsinBadge"]):
    def __init__(self, data):
        super().__init__([AsinBadge(datum) for datum in data])
        self.data = data


class AsinSet(list, _List["Asin"]):
    def __init__(self, data):
        super().__init__([Asin(datum) for datum in data])
        self.data = data


class AsinMetadataSet(list, _List["AsinMetadata"]):
    def __init__(self, data):
        super().__init__([AsinMetadata(datum) for datum in data])
        self.data = data


class PublishRecordList(list, _List["PublishRecord"]):
    def __init__(self, data):
        super().__init__([PublishRecord(datum) for datum in data])
        self.data = data


class ContentReferenceKeySet(list, _List["ContentReferenceKey"]):
    def __init__(self, data):
        super().__init__([ContentReferenceKey(datum) for datum in data])
        self.data = data


class ContentRecordList(list, _List["ContentRecord"]):
    def __init__(self, data):
        super().__init__([ContentRecord(datum) for datum in data])
        self.data = data


class ContentModuleList(list, _List["ContentModule"]):
    def __init__(self, data):
        super().__init__([ContentModule(datum) for datum in data])
        self.data = data


class DecoratorSet(list, _List["Decorator"]):
    def __init__(self, data):
        super().__init__([Decorator(datum) for datum in data])
        self.data = data


class ContentType(str):
    pass


class ContentSubType(str):
    pass


class ContentStatus(str):
    pass


class ContentBadge(str):
    pass


class AsinBadge(str):
    pass


class MarketplaceId(str):
    pass


class LanguageTag(str):
    pass


class Asin(str):
    pass


class ContentReferenceKey(str):
    pass


class PageToken(str):
    pass


class ContentModuleType(str):
    pass


class ColorType(str):
    pass


class PositionType(str):
    pass


class DecoratorType(str):
    pass


class GetContentDocumentIncludedDataType(str):
    pass


class ListContentDocumentAsinRelationsIncludedDataType(str):
    pass


class contentReferenceKey(str):
    pass


class marketplaceId(str):
    pass


class pageToken(str):
    pass


class asinSet(list):
    pass


class asin(str):
    pass


class getContentDocumentIncludedDataSet(list):
    pass


class listContentDocumentAsinRelationsIncludedDataSet(list):
    pass


class AplusPaginatedResponse:
    def __init__(self, data):
        if "nextPageToken" in data:
            self.nextPageToken: PageToken = PageToken(data.pop("nextPageToken"))
        else:
            self.nextPageToken: PageToken = None
        self.data = data
        super().__init__(data)


class SearchContentDocumentsResponse:
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
    def __init__(self, data):
        if "contentRecord" in data:
            self.contentRecord: ContentRecord = ContentRecord(data.pop("contentRecord"))
        else:
            self.contentRecord: ContentRecord = None
        self.data = data
        super().__init__(data)


class PostContentDocumentResponse:
    def __init__(self, data):
        if "contentReferenceKey" in data:
            self.contentReferenceKey: ContentReferenceKey = ContentReferenceKey(data.pop("contentReferenceKey"))
        else:
            self.contentReferenceKey: ContentReferenceKey = None
        self.data = data
        super().__init__(data)


class ListContentDocumentAsinRelationsResponse:
    def __init__(self, data):
        if "asinMetadataSet" in data:
            self.asinMetadataSet: AsinMetadataSet = AsinMetadataSet(data.pop("asinMetadataSet"))
        else:
            self.asinMetadataSet: AsinMetadataSet = None
        self.data = data
        super().__init__(data)


class PostContentDocumentAsinRelationsResponse:
    def __init__(self, data):
        self.data = data
        super().__init__(data)


class ValidateContentDocumentAsinRelationsResponse:
    def __init__(self, data):
        self.data = data
        super().__init__(data)


class SearchContentPublishRecordsResponse:
    def __init__(self, data):
        if "publishRecordList" in data:
            self.publishRecordList: PublishRecordList = PublishRecordList(data.pop("publishRecordList"))
        else:
            self.publishRecordList: PublishRecordList = None
        self.data = data
        super().__init__(data)


class PostContentDocumentApprovalSubmissionResponse:
    def __init__(self, data):
        self.data = data
        super().__init__(data)


class PostContentDocumentSuspendSubmissionResponse:
    def __init__(self, data):
        self.data = data
        super().__init__(data)


class AplusContent20201101Client(__BaseClient):
    def searchContentDocuments(
        self,
        marketplaceId: str,
        pageToken: str = None,
    ):
        url = "/aplus/2020-11-01/contentDocuments".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = (marketplaceId,)
        if pageToken is not None:
            params["pageToken"] = (pageToken,)
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
        }[response.status_code](self.__get_response_json(response))

    def createContentDocument(
        self,
        data: PostContentDocumentRequest,
        marketplaceId: str,
    ):
        url = "/aplus/2020-11-01/contentDocuments".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="POST", data=data.data)
        return {
            200: PostContentDocumentResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

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
            params["marketplaceId"] = (marketplaceId,)
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
        }[response.status_code](self.__get_response_json(response))

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
            params["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="POST", data=data.data)
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
        }[response.status_code](self.__get_response_json(response))

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
            params["marketplaceId"] = (marketplaceId,)
        if includedDataSet is not None:
            params["includedDataSet"] = ",".join(map(str, includedDataSet))
        if asinSet is not None:
            params["asinSet"] = ",".join(map(str, asinSet))
        if pageToken is not None:
            params["pageToken"] = (pageToken,)
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
        }[response.status_code](self.__get_response_json(response))

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
            params["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="POST", data=data.data)
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
        }[response.status_code](self.__get_response_json(response))

    def validateContentDocumentAsinRelations(
        self,
        data: PostContentDocumentRequest,
        marketplaceId: str,
        asinSet: _List[str] = None,
    ):
        url = "/aplus/2020-11-01/contentAsinValidations".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = (marketplaceId,)
        if asinSet is not None:
            params["asinSet"] = ",".join(map(str, asinSet))
        response = self.request(url, method="POST", data=data.data)
        return {
            200: ValidateContentDocumentAsinRelationsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def searchContentPublishRecords(
        self,
        marketplaceId: str,
        asin: str,
        pageToken: str = None,
    ):
        url = "/aplus/2020-11-01/contentPublishRecords".format()
        params = {}
        if marketplaceId is not None:
            params["marketplaceId"] = (marketplaceId,)
        if asin is not None:
            params["asin"] = (asin,)
        if pageToken is not None:
            params["pageToken"] = (pageToken,)
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
        }[response.status_code](self.__get_response_json(response))

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
            params["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="POST", data=data.data)
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
        }[response.status_code](self.__get_response_json(response))

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
            params["marketplaceId"] = (marketplaceId,)
        response = self.request(url, method="POST", data=data.data)
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
        }[response.status_code](self.__get_response_json(response))
