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
        if "salesRanks" in data:
            self.salesRanks: ItemSalesRanks = self._get_value(ItemSalesRanks, "salesRanks")
        else:
            self.salesRanks: ItemSalesRanks = None
        if "summaries" in data:
            self.summaries: ItemSummaries = self._get_value(ItemSummaries, "summaries")
        else:
            self.summaries: ItemSummaries = None
        if "variations" in data:
            self.variations: ItemVariations = self._get_value(ItemVariations, "variations")
        else:
            self.variations: ItemVariations = None
        if "vendorDetails" in data:
            self.vendorDetails: ItemVendorDetails = self._get_value(ItemVendorDetails, "vendorDetails")
        else:
            self.vendorDetails: ItemVendorDetails = None


class ItemAttributes(__BaseDictObject):
    """
    A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.
    """

    def __init__(self, data):
        super().__init__(data)


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
        if "ranks" in data:
            self.ranks: _List[ItemSalesRank] = [ItemSalesRank(datum) for datum in data["ranks"]]
        else:
            self.ranks: _List[ItemSalesRank] = []


class ItemSalesRank(__BaseDictObject):
    """
    Sales rank of an Amazon catalog item.
    """

    def __init__(self, data):
        super().__init__(data)
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
        if "brandName" in data:
            self.brandName: str = self._get_value(str, "brandName")
        else:
            self.brandName: str = None
        if "browseNode" in data:
            self.browseNode: str = self._get_value(str, "browseNode")
        else:
            self.browseNode: str = None
        if "colorName" in data:
            self.colorName: str = self._get_value(str, "colorName")
        else:
            self.colorName: str = None
        if "itemName" in data:
            self.itemName: str = self._get_value(str, "itemName")
        else:
            self.itemName: str = None
        if "manufacturer" in data:
            self.manufacturer: str = self._get_value(str, "manufacturer")
        else:
            self.manufacturer: str = None
        if "modelNumber" in data:
            self.modelNumber: str = self._get_value(str, "modelNumber")
        else:
            self.modelNumber: str = None
        if "sizeName" in data:
            self.sizeName: str = self._get_value(str, "sizeName")
        else:
            self.sizeName: str = None
        if "styleName" in data:
            self.styleName: str = self._get_value(str, "styleName")
        else:
            self.styleName: str = None


class ItemVariationsByMarketplace(__BaseDictObject):
    """
    Variation details for the Amazon catalog item for the indicated Amazon marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: str = self._get_value(str, "marketplaceId")
        else:
            self.marketplaceId: str = None
        if "asins" in data:
            self.asins: _List[str] = [str(datum) for datum in data["asins"]]
        else:
            self.asins: _List[str] = []
        if "variationType" in data:
            self.variationType: str = self._get_value(str, "variationType")
        else:
            self.variationType: str = None


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
        if "categoryCode" in data:
            self.categoryCode: str = self._get_value(str, "categoryCode")
        else:
            self.categoryCode: str = None
        if "manufacturerCode" in data:
            self.manufacturerCode: str = self._get_value(str, "manufacturerCode")
        else:
            self.manufacturerCode: str = None
        if "manufacturerCodeParent" in data:
            self.manufacturerCodeParent: str = self._get_value(str, "manufacturerCodeParent")
        else:
            self.manufacturerCodeParent: str = None
        if "productGroup" in data:
            self.productGroup: str = self._get_value(str, "productGroup")
        else:
            self.productGroup: str = None
        if "replenishmentCategory" in data:
            self.replenishmentCategory: str = self._get_value(str, "replenishmentCategory")
        else:
            self.replenishmentCategory: str = None
        if "subcategoryCode" in data:
            self.subcategoryCode: str = self._get_value(str, "subcategoryCode")
        else:
            self.subcategoryCode: str = None


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
    When a request produces a response that exceeds the pageSize, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the nextToken value or the previousToken value as the pageToken parameter in the next request. When you receive the last page, there will be no nextToken key in the pagination object.
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


class ItemIdentifiers(list, _List["ItemIdentifiersByMarketplace"]):
    """
    Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    """

    def __init__(self, data):
        super().__init__([ItemIdentifiersByMarketplace(datum) for datum in data])
        self.data = data


class ItemImages(list, _List["ItemImagesByMarketplace"]):
    """
    Images for an item in the Amazon catalog. All image variants are provided to brand owners. Otherwise, a thumbnail of the "MAIN" image variant is provided.
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


class ItemVariations(list, _List["ItemVariationsByMarketplace"]):
    """
    Variation details by marketplace for an Amazon catalog item (variation relationships).
    """

    def __init__(self, data):
        super().__init__([ItemVariationsByMarketplace(datum) for datum in data])
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


class CatalogItems20201201Client(__BaseClient):
    def searchCatalogItems(
        self,
        keywords: _List[str],
        marketplaceIds: _List[str],
        includedData: _List[str] = None,
        brandNames: _List[str] = None,
        classificationIds: _List[str] = None,
        pageSize: int = None,
        pageToken: str = None,
        keywordsLocale: str = None,
        locale: str = None,
    ):
        """
                Search for and return a list of Amazon catalog items and associated information.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 5 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/catalog/2020-12-01/items"
        params = {}
        if keywords is not None:
            params["keywords"] = ",".join(map(str, keywords))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if includedData is not None:
            params["includedData"] = ",".join(map(str, includedData))
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
        if locale is not None:
            params["locale"] = locale
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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 5 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/catalog/2020-12-01/items/{asin}"
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
