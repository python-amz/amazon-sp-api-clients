from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class ErrorList(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Item(__BaseDictObject):
    """
    An item in the Amazon catalog.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: ItemAsin = self._get_value(ItemAsin, "asin")
        else:
            self.asin: ItemAsin = None
        if "attributes" in data:
            self.attributes: ItemAttributes = self._get_value(ItemAttributes, "attributes")
        else:
            self.attributes: ItemAttributes = None
        if "dimensions" in data:
            self.dimensions: ItemDimensions = self._get_value(ItemDimensions, "dimensions")
        else:
            self.dimensions: ItemDimensions = None
        if "identifiers" in data:
            self.identifiers: ItemIdentifiers = self._get_value(ItemIdentifiers, "identifiers")
        else:
            self.identifiers: ItemIdentifiers = None
        if "images" in data:
            self.images: ItemImages = self._get_value(ItemImages, "images")
        else:
            self.images: ItemImages = None
        if "productTypes" in data:
            self.productTypes: ItemProductTypes = self._get_value(ItemProductTypes, "productTypes")
        else:
            self.productTypes: ItemProductTypes = None
        if "relationships" in data:
            self.relationships: ItemRelationships = self._get_value(ItemRelationships, "relationships")
        else:
            self.relationships: ItemRelationships = None
        if "salesRanks" in data:
            self.salesRanks: ItemSalesRanks = self._get_value(ItemSalesRanks, "salesRanks")
        else:
            self.salesRanks: ItemSalesRanks = None
        if "summaries" in data:
            self.summaries: ItemSummaries = self._get_value(ItemSummaries, "summaries")
        else:
            self.summaries: ItemSummaries = None
        if "vendorDetails" in data:
            self.vendorDetails: ItemVendorDetails = self._get_value(ItemVendorDetails, "vendorDetails")
        else:
            self.vendorDetails: ItemVendorDetails = None


class ItemAttributes(__BaseDictObject):
    """
    A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.
    """

    def __init__(self, data):
        super().__init__(data)


class ItemBrowseClassification(__BaseDictObject):
    """
    Classification (browse node) associated with an Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "displayName" in data:
            self.displayName: str = self._get_value(str, "displayName")
        else:
            self.displayName: str = None
        if "classificationId" in data:
            self.classificationId: str = self._get_value(str, "classificationId")
        else:
            self.classificationId: str = None


class ItemContributor(__BaseDictObject):
    """
    Individual contributor to the creation of an item, such as an author or actor.
    """

    def __init__(self, data):
        super().__init__(data)
        if "role" in data:
            self.role: ItemContributorRole = self._get_value(ItemContributorRole, "role")
        else:
            self.role: ItemContributorRole = None
        if "value" in data:
            self.value: str = self._get_value(str, "value")
        else:
            self.value: str = None


class ItemContributorRole(__BaseDictObject):
    """
    Role of an individual contributor in the creation of an item, such as author or actor.
    """

    def __init__(self, data):
        super().__init__(data)
        if "displayName" in data:
            self.displayName: str = self._get_value(str, "displayName")
        else:
            self.displayName: str = None
        if "value" in data:
            self.value: str = self._get_value(str, "value")
        else:
            self.value: str = None


class Dimension(__BaseDictObject):
    """
    Individual dimension value of an Amazon catalog item or item package.
    """

    def __init__(self, data):
        super().__init__(data)
        if "unit" in data:
            self.unit: str = self._get_value(str, "unit")
        else:
            self.unit: str = None
        if "value" in data:
            self.value: float = self._get_value(float, "value")
        else:
            self.value: float = None


class Dimensions(__BaseDictObject):
    """
    Dimensions of an Amazon catalog item or item in its packaging.
    """

    def __init__(self, data):
        super().__init__(data)
        if "height" in data:
            self.height: Dimension = self._get_value(Dimension, "height")
        else:
            self.height: Dimension = None
        if "length" in data:
            self.length: Dimension = self._get_value(Dimension, "length")
        else:
            self.length: Dimension = None
        if "weight" in data:
            self.weight: Dimension = self._get_value(Dimension, "weight")
        else:
            self.weight: Dimension = None
        if "width" in data:
            self.width: Dimension = self._get_value(Dimension, "width")
        else:
            self.width: Dimension = None


class ItemDimensionsByMarketplace(__BaseDictObject):
    """
    Dimensions associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "item" in data:
            self.item: Dimensions = self._get_value(Dimensions, "item")
        else:
            self.item: Dimensions = None
        if "package" in data:
            self.package: Dimensions = self._get_value(Dimensions, "package")
        else:
            self.package: Dimensions = None


class ItemIdentifiersByMarketplace(__BaseDictObject):
    """
    Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "identifiers" in data:
            self.identifiers: _List[ItemIdentifier] = [ItemIdentifier(datum) for datum in data["identifiers"]]
        else:
            self.identifiers: _List[ItemIdentifier] = []


class ItemIdentifier(__BaseDictObject):
    """
    Identifier associated with the item in the Amazon catalog, such as a UPC or EAN identifier.
    """

    def __init__(self, data):
        super().__init__(data)
        if "identifierType" in data:
            self.identifierType: str = self._get_value(str, "identifierType")
        else:
            self.identifierType: str = None
        if "identifier" in data:
            self.identifier: str = self._get_value(str, "identifier")
        else:
            self.identifier: str = None


class ItemImagesByMarketplace(__BaseDictObject):
    """
    Images for an item in the Amazon catalog for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "images" in data:
            self.images: _List[ItemImage] = [ItemImage(datum) for datum in data["images"]]
        else:
            self.images: _List[ItemImage] = []


class ItemImage(__BaseDictObject):
    """
    Image for an item in the Amazon catalog.
    """

    def __init__(self, data):
        super().__init__(data)
        if "variant" in data:
            self.variant: str = self._get_value(str, "variant")
        else:
            self.variant: str = None
        if "link" in data:
            self.link: str = self._get_value(str, "link")
        else:
            self.link: str = None
        if "height" in data:
            self.height: int = self._get_value(int, "height")
        else:
            self.height: int = None
        if "width" in data:
            self.width: int = self._get_value(int, "width")
        else:
            self.width: int = None


class ItemProductTypeByMarketplace(__BaseDictObject):
    """
    Product type associated with the Amazon catalog item for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "productType" in data:
            self.productType: str = self._get_value(str, "productType")
        else:
            self.productType: str = None


class ItemSalesRanksByMarketplace(__BaseDictObject):
    """
    Sales ranks of an Amazon catalog item for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "classificationRanks" in data:
            self.classificationRanks: _List[ItemClassificationSalesRank] = [
                ItemClassificationSalesRank(datum) for datum in data["classificationRanks"]
            ]
        else:
            self.classificationRanks: _List[ItemClassificationSalesRank] = []
        if "displayGroupRanks" in data:
            self.displayGroupRanks: _List[ItemDisplayGroupSalesRank] = [
                ItemDisplayGroupSalesRank(datum) for datum in data["displayGroupRanks"]
            ]
        else:
            self.displayGroupRanks: _List[ItemDisplayGroupSalesRank] = []


class ItemClassificationSalesRank(__BaseDictObject):
    """
    Sales rank of an Amazon catalog item by classification.
    """

    def __init__(self, data):
        super().__init__(data)
        if "classificationId" in data:
            self.classificationId: str = self._get_value(str, "classificationId")
        else:
            self.classificationId: str = None
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None
        if "link" in data:
            self.link: str = self._get_value(str, "link")
        else:
            self.link: str = None
        if "rank" in data:
            self.rank: int = self._get_value(int, "rank")
        else:
            self.rank: int = None


class ItemDisplayGroupSalesRank(__BaseDictObject):
    """
    Sales rank of an Amazon catalog item by website display group.
    """

    def __init__(self, data):
        super().__init__(data)
        if "websiteDisplayGroup" in data:
            self.websiteDisplayGroup: str = self._get_value(str, "websiteDisplayGroup")
        else:
            self.websiteDisplayGroup: str = None
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None
        if "link" in data:
            self.link: str = self._get_value(str, "link")
        else:
            self.link: str = None
        if "rank" in data:
            self.rank: int = self._get_value(int, "rank")
        else:
            self.rank: int = None


class ItemSummaryByMarketplace(__BaseDictObject):
    """
    Summary details of an Amazon catalog item for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "adultProduct" in data:
            self.adultProduct: bool = self._get_value(convert_bool, "adultProduct")
        else:
            self.adultProduct: bool = None
        if "autographed" in data:
            self.autographed: bool = self._get_value(convert_bool, "autographed")
        else:
            self.autographed: bool = None
        if "brand" in data:
            self.brand: str = self._get_value(str, "brand")
        else:
            self.brand: str = None
        if "browseClassification" in data:
            self.browseClassification: ItemBrowseClassification = self._get_value(
                ItemBrowseClassification, "browseClassification"
            )
        else:
            self.browseClassification: ItemBrowseClassification = None
        if "color" in data:
            self.color: str = self._get_value(str, "color")
        else:
            self.color: str = None
        if "contributors" in data:
            self.contributors: _List[ItemContributor] = [ItemContributor(datum) for datum in data["contributors"]]
        else:
            self.contributors: _List[ItemContributor] = []
        if "itemClassification" in data:
            self.itemClassification: str = self._get_value(str, "itemClassification")
        else:
            self.itemClassification: str = None
        if "itemName" in data:
            self.itemName: str = self._get_value(str, "itemName")
        else:
            self.itemName: str = None
        if "manufacturer" in data:
            self.manufacturer: str = self._get_value(str, "manufacturer")
        else:
            self.manufacturer: str = None
        if "memorabilia" in data:
            self.memorabilia: bool = self._get_value(convert_bool, "memorabilia")
        else:
            self.memorabilia: bool = None
        if "modelNumber" in data:
            self.modelNumber: str = self._get_value(str, "modelNumber")
        else:
            self.modelNumber: str = None
        if "packageQuantity" in data:
            self.packageQuantity: int = self._get_value(int, "packageQuantity")
        else:
            self.packageQuantity: int = None
        if "partNumber" in data:
            self.partNumber: str = self._get_value(str, "partNumber")
        else:
            self.partNumber: str = None
        if "releaseDate" in data:
            self.releaseDate: str = self._get_value(str, "releaseDate")
        else:
            self.releaseDate: str = None
        if "size" in data:
            self.size: str = self._get_value(str, "size")
        else:
            self.size: str = None
        if "style" in data:
            self.style: str = self._get_value(str, "style")
        else:
            self.style: str = None
        if "tradeInEligible" in data:
            self.tradeInEligible: bool = self._get_value(convert_bool, "tradeInEligible")
        else:
            self.tradeInEligible: bool = None
        if "websiteDisplayGroup" in data:
            self.websiteDisplayGroup: str = self._get_value(str, "websiteDisplayGroup")
        else:
            self.websiteDisplayGroup: str = None
        if "websiteDisplayGroupName" in data:
            self.websiteDisplayGroupName: str = self._get_value(str, "websiteDisplayGroupName")
        else:
            self.websiteDisplayGroupName: str = None


class ItemVariationTheme(__BaseDictObject):
    """
    Variation theme indicating the combination of Amazon item catalog attributes that define the variation family.
    """

    def __init__(self, data):
        super().__init__(data)
        if "attributes" in data:
            self.attributes: _List[str] = [str(datum) for datum in data["attributes"]]
        else:
            self.attributes: _List[str] = []
        if "theme" in data:
            self.theme: str = self._get_value(str, "theme")
        else:
            self.theme: str = None


class ItemRelationshipsByMarketplace(__BaseDictObject):
    """
    Relationship details for the Amazon catalog item for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "relationships" in data:
            self.relationships: _List[ItemRelationship] = [ItemRelationship(datum) for datum in data["relationships"]]
        else:
            self.relationships: _List[ItemRelationship] = []


class ItemRelationship(__BaseDictObject):
    """
    Relationship details for an Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "childAsins" in data:
            self.childAsins: _List[str] = [str(datum) for datum in data["childAsins"]]
        else:
            self.childAsins: _List[str] = []
        if "parentAsins" in data:
            self.parentAsins: _List[str] = [str(datum) for datum in data["parentAsins"]]
        else:
            self.parentAsins: _List[str] = []
        if "variationTheme" in data:
            self.variationTheme: ItemVariationTheme = self._get_value(ItemVariationTheme, "variationTheme")
        else:
            self.variationTheme: ItemVariationTheme = None
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None


class ItemVendorDetailsCategory(__BaseDictObject):
    """
    Product category or subcategory associated with an Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "displayName" in data:
            self.displayName: str = self._get_value(str, "displayName")
        else:
            self.displayName: str = None
        if "value" in data:
            self.value: str = self._get_value(str, "value")
        else:
            self.value: str = None


class ItemVendorDetailsByMarketplace(__BaseDictObject):
    """
    Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "brandCode" in data:
            self.brandCode: str = self._get_value(str, "brandCode")
        else:
            self.brandCode: str = None
        if "manufacturerCode" in data:
            self.manufacturerCode: str = self._get_value(str, "manufacturerCode")
        else:
            self.manufacturerCode: str = None
        if "manufacturerCodeParent" in data:
            self.manufacturerCodeParent: str = self._get_value(str, "manufacturerCodeParent")
        else:
            self.manufacturerCodeParent: str = None
        if "productCategory" in data:
            self.productCategory: ItemVendorDetailsCategory = self._get_value(
                ItemVendorDetailsCategory, "productCategory"
            )
        else:
            self.productCategory: ItemVendorDetailsCategory = None
        if "productGroup" in data:
            self.productGroup: str = self._get_value(str, "productGroup")
        else:
            self.productGroup: str = None
        if "productSubcategory" in data:
            self.productSubcategory: ItemVendorDetailsCategory = self._get_value(
                ItemVendorDetailsCategory, "productSubcategory"
            )
        else:
            self.productSubcategory: ItemVendorDetailsCategory = None
        if "replenishmentCategory" in data:
            self.replenishmentCategory: str = self._get_value(str, "replenishmentCategory")
        else:
            self.replenishmentCategory: str = None


class ItemSearchResults(__BaseDictObject):
    """
    Items in the Amazon catalog and search related metadata.
    """

    def __init__(self, data):
        super().__init__(data)
        if "numberOfResults" in data:
            self.numberOfResults: int = self._get_value(int, "numberOfResults")
        else:
            self.numberOfResults: int = None
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "refinements" in data:
            self.refinements: Refinements = self._get_value(Refinements, "refinements")
        else:
            self.refinements: Refinements = None
        if "items" in data:
            self.items: _List[Item] = [Item(datum) for datum in data["items"]]
        else:
            self.items: _List[Item] = []


class Pagination(__BaseDictObject):
    """
    When a request produces a response that exceeds the `pageSize`, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. When you receive the last page, there will be no `nextToken` key in the pagination object.
    """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None
        if "previousToken" in data:
            self.previousToken: str = self._get_value(str, "previousToken")
        else:
            self.previousToken: str = None


class Refinements(__BaseDictObject):
    """
    Search refinements.
    """

    def __init__(self, data):
        super().__init__(data)
        if "brands" in data:
            self.brands: _List[BrandRefinement] = [BrandRefinement(datum) for datum in data["brands"]]
        else:
            self.brands: _List[BrandRefinement] = []
        if "classifications" in data:
            self.classifications: _List[ClassificationRefinement] = [
                ClassificationRefinement(datum) for datum in data["classifications"]
            ]
        else:
            self.classifications: _List[ClassificationRefinement] = []


class BrandRefinement(__BaseDictObject):
    """
    Description of a brand that can be used to get more fine-grained search results.
    """

    def __init__(self, data):
        super().__init__(data)
        if "numberOfResults" in data:
            self.numberOfResults: int = self._get_value(int, "numberOfResults")
        else:
            self.numberOfResults: int = None
        if "brandName" in data:
            self.brandName: str = self._get_value(str, "brandName")
        else:
            self.brandName: str = None


class ClassificationRefinement(__BaseDictObject):
    """
    Description of a classification that can be used to get more fine-grained search results.
    """

    def __init__(self, data):
        super().__init__(data)
        if "numberOfResults" in data:
            self.numberOfResults: int = self._get_value(int, "numberOfResults")
        else:
            self.numberOfResults: int = None
        if "displayName" in data:
            self.displayName: str = self._get_value(str, "displayName")
        else:
            self.displayName: str = None
        if "classificationId" in data:
            self.classificationId: str = self._get_value(str, "classificationId")
        else:
            self.classificationId: str = None


class ItemDimensions(list, _List["ItemDimensionsByMarketplace"]):
    """
    Array of dimensions associated with the item in the Amazon catalog by Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__([ItemDimensionsByMarketplace(datum) for datum in data])
        self.data = data


class ItemIdentifiers(list, _List["ItemIdentifiersByMarketplace"]):
    """
    Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    """

    def __init__(self, data):
        super().__init__([ItemIdentifiersByMarketplace(datum) for datum in data])
        self.data = data


class ItemImages(list, _List["ItemImagesByMarketplace"]):
    """
    Images for an item in the Amazon catalog.
    """

    def __init__(self, data):
        super().__init__([ItemImagesByMarketplace(datum) for datum in data])
        self.data = data


class ItemProductTypes(list, _List["ItemProductTypeByMarketplace"]):
    """
    Product types associated with the Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__([ItemProductTypeByMarketplace(datum) for datum in data])
        self.data = data


class ItemSalesRanks(list, _List["ItemSalesRanksByMarketplace"]):
    """
    Sales ranks of an Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__([ItemSalesRanksByMarketplace(datum) for datum in data])
        self.data = data


class ItemSummaries(list, _List["ItemSummaryByMarketplace"]):
    """
    Summary details of an Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__([ItemSummaryByMarketplace(datum) for datum in data])
        self.data = data


class ItemRelationships(list, _List["ItemRelationshipsByMarketplace"]):
    """
    Relationships by marketplace for an Amazon catalog item (for example, variations).
    """

    def __init__(self, data):
        super().__init__([ItemRelationshipsByMarketplace(datum) for datum in data])
        self.data = data


class ItemVendorDetails(list, _List["ItemVendorDetailsByMarketplace"]):
    """
    Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.
    """

    def __init__(self, data):
        super().__init__([ItemVendorDetailsByMarketplace(datum) for datum in data])
        self.data = data


class ItemAsin(str):
    """
    Amazon Standard Identification Number (ASIN) is the unique identifier for an item in the Amazon catalog.
    """


class CatalogItems20220401Client(__BaseClient):
    def searchCatalogItems(
        self,
        marketplaceIds: _List[str],
        identifiers: _List[str] = None,
        identifiersType: str = None,
        includedData: _List[str] = None,
        locale: str = None,
        sellerId: str = None,
        keywords: _List[str] = None,
        brandNames: _List[str] = None,
        classificationIds: _List[str] = None,
        pageSize: int = None,
        pageToken: str = None,
        keywordsLocale: str = None,
    ):
        """
                Search for and return a list of Amazon catalog items and associated information either by identifier or by keywords.
        **Usage Plans:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may observe higher rate and burst values than those shown here. For more information, refer to the [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/catalog/2022-04-01/items"
        params = {}
        if identifiers is not None:
            params["identifiers"] = ",".join(map(str, identifiers))
        if identifiersType is not None:
            params["identifiersType"] = identifiersType
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if includedData is not None:
            params["includedData"] = ",".join(map(str, includedData))
        if locale is not None:
            params["locale"] = locale
        if sellerId is not None:
            params["sellerId"] = sellerId
        if keywords is not None:
            params["keywords"] = ",".join(map(str, keywords))
        if brandNames is not None:
            params["brandNames"] = ",".join(map(str, brandNames))
        if classificationIds is not None:
            params["classificationIds"] = ",".join(map(str, classificationIds))
        if pageSize is not None:
            params["pageSize"] = pageSize
        if pageToken is not None:
            params["pageToken"] = pageToken
        if keywordsLocale is not None:
            params["keywordsLocale"] = keywordsLocale
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ItemSearchResults,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getCatalogItem(
        self,
        asin: str,
        marketplaceIds: _List[str],
        includedData: _List[str] = None,
        locale: str = None,
    ):
        """
                Retrieves details for an item in the Amazon catalog.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may observe higher rate and burst values than those shown here. For more information, refer to the [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/catalog/2022-04-01/items/{asin}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if includedData is not None:
            params["includedData"] = ",".join(map(str, includedData))
        if locale is not None:
            params["locale"] = locale
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: Item,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
