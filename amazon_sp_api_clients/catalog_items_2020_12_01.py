from .base import BaseClient as __BaseClient
from typing import List as _List


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


class ErrorList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Item:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asin" in data:
            self.asin: ItemAsin = ItemAsin(data["asin"])
        else:
            self.asin: ItemAsin = None
        if "attributes" in data:
            self.attributes: ItemAttributes = ItemAttributes(data["attributes"])
        else:
            self.attributes: ItemAttributes = None
        if "identifiers" in data:
            self.identifiers: ItemIdentifiers = ItemIdentifiers(data["identifiers"])
        else:
            self.identifiers: ItemIdentifiers = None
        if "images" in data:
            self.images: ItemImages = ItemImages(data["images"])
        else:
            self.images: ItemImages = None
        if "productTypes" in data:
            self.productTypes: ItemProductTypes = ItemProductTypes(data["productTypes"])
        else:
            self.productTypes: ItemProductTypes = None
        if "salesRanks" in data:
            self.salesRanks: ItemSalesRanks = ItemSalesRanks(data["salesRanks"])
        else:
            self.salesRanks: ItemSalesRanks = None
        if "summaries" in data:
            self.summaries: ItemSummaries = ItemSummaries(data["summaries"])
        else:
            self.summaries: ItemSummaries = None
        if "variations" in data:
            self.variations: ItemVariations = ItemVariations(data["variations"])
        else:
            self.variations: ItemVariations = None
        if "vendorDetails" in data:
            self.vendorDetails: ItemVendorDetails = ItemVendorDetails(data["vendorDetails"])
        else:
            self.vendorDetails: ItemVendorDetails = None


class ItemAttributes:
    def __init__(self, data):
        super().__init__()
        self.data = data


class ItemIdentifiersByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "identifiers" in data:
            self.identifiers: _List[ItemIdentifier] = [ItemIdentifier(datum) for datum in data["identifiers"]]
        else:
            self.identifiers: _List[ItemIdentifier] = []


class ItemIdentifier:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "identifierType" in data:
            self.identifierType: str = str(data["identifierType"])
        else:
            self.identifierType: str = None
        if "identifier" in data:
            self.identifier: str = str(data["identifier"])
        else:
            self.identifier: str = None


class ItemImagesByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "images" in data:
            self.images: _List[ItemImage] = [ItemImage(datum) for datum in data["images"]]
        else:
            self.images: _List[ItemImage] = []


class ItemImage:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "variant" in data:
            self.variant: str = str(data["variant"])
        else:
            self.variant: str = None
        if "link" in data:
            self.link: str = str(data["link"])
        else:
            self.link: str = None
        if "height" in data:
            self.height: int = int(data["height"])
        else:
            self.height: int = None
        if "width" in data:
            self.width: int = int(data["width"])
        else:
            self.width: int = None


class ItemProductTypeByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None


class ItemSalesRanksByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "ranks" in data:
            self.ranks: _List[ItemSalesRank] = [ItemSalesRank(datum) for datum in data["ranks"]]
        else:
            self.ranks: _List[ItemSalesRank] = []


class ItemSalesRank:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "link" in data:
            self.link: str = str(data["link"])
        else:
            self.link: str = None
        if "rank" in data:
            self.rank: int = int(data["rank"])
        else:
            self.rank: int = None


class ItemSummaryByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "brandName" in data:
            self.brandName: str = str(data["brandName"])
        else:
            self.brandName: str = None
        if "browseNode" in data:
            self.browseNode: str = str(data["browseNode"])
        else:
            self.browseNode: str = None
        if "colorName" in data:
            self.colorName: str = str(data["colorName"])
        else:
            self.colorName: str = None
        if "itemName" in data:
            self.itemName: str = str(data["itemName"])
        else:
            self.itemName: str = None
        if "manufacturer" in data:
            self.manufacturer: str = str(data["manufacturer"])
        else:
            self.manufacturer: str = None
        if "modelNumber" in data:
            self.modelNumber: str = str(data["modelNumber"])
        else:
            self.modelNumber: str = None
        if "sizeName" in data:
            self.sizeName: str = str(data["sizeName"])
        else:
            self.sizeName: str = None
        if "styleName" in data:
            self.styleName: str = str(data["styleName"])
        else:
            self.styleName: str = None


class ItemVariationsByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "asins" in data:
            self.asins: _List[str] = [str(datum) for datum in data["asins"]]
        else:
            self.asins: _List[str] = []
        if "variationType" in data:
            self.variationType: str = str(data["variationType"])
        else:
            self.variationType: str = None


class ItemVendorDetailsByMarketplace:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: str = str(data["marketplaceId"])
        else:
            self.marketplaceId: str = None
        if "brandCode" in data:
            self.brandCode: str = str(data["brandCode"])
        else:
            self.brandCode: str = None
        if "categoryCode" in data:
            self.categoryCode: str = str(data["categoryCode"])
        else:
            self.categoryCode: str = None
        if "manufacturerCode" in data:
            self.manufacturerCode: str = str(data["manufacturerCode"])
        else:
            self.manufacturerCode: str = None
        if "manufacturerCodeParent" in data:
            self.manufacturerCodeParent: str = str(data["manufacturerCodeParent"])
        else:
            self.manufacturerCodeParent: str = None
        if "productGroup" in data:
            self.productGroup: str = str(data["productGroup"])
        else:
            self.productGroup: str = None
        if "replenishmentCategory" in data:
            self.replenishmentCategory: str = str(data["replenishmentCategory"])
        else:
            self.replenishmentCategory: str = None
        if "subcategoryCode" in data:
            self.subcategoryCode: str = str(data["subcategoryCode"])
        else:
            self.subcategoryCode: str = None


class ItemSearchResults:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "numberOfResults" in data:
            self.numberOfResults: int = int(data["numberOfResults"])
        else:
            self.numberOfResults: int = None
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "refinements" in data:
            self.refinements: Refinements = Refinements(data["refinements"])
        else:
            self.refinements: Refinements = None
        if "items" in data:
            self.items: _List[Item] = [Item(datum) for datum in data["items"]]
        else:
            self.items: _List[Item] = []


class Pagination:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None
        if "previousToken" in data:
            self.previousToken: str = str(data["previousToken"])
        else:
            self.previousToken: str = None


class Refinements:
    def __init__(self, data):
        super().__init__()
        self.data = data
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


class BrandRefinement:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "numberOfResults" in data:
            self.numberOfResults: int = int(data["numberOfResults"])
        else:
            self.numberOfResults: int = None
        if "brandName" in data:
            self.brandName: str = str(data["brandName"])
        else:
            self.brandName: str = None


class ClassificationRefinement:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "numberOfResults" in data:
            self.numberOfResults: int = int(data["numberOfResults"])
        else:
            self.numberOfResults: int = None
        if "displayName" in data:
            self.displayName: str = str(data["displayName"])
        else:
            self.displayName: str = None
        if "classificationId" in data:
            self.classificationId: str = str(data["classificationId"])
        else:
            self.classificationId: str = None


class ItemIdentifiers(list, _List["ItemIdentifiersByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemIdentifiersByMarketplace(datum) for datum in data])
        self.data = data


class ItemImages(list, _List["ItemImagesByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemImagesByMarketplace(datum) for datum in data])
        self.data = data


class ItemProductTypes(list, _List["ItemProductTypeByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemProductTypeByMarketplace(datum) for datum in data])
        self.data = data


class ItemSalesRanks(list, _List["ItemSalesRanksByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemSalesRanksByMarketplace(datum) for datum in data])
        self.data = data


class ItemSummaries(list, _List["ItemSummaryByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemSummaryByMarketplace(datum) for datum in data])
        self.data = data


class ItemVariations(list, _List["ItemVariationsByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemVariationsByMarketplace(datum) for datum in data])
        self.data = data


class ItemVendorDetails(list, _List["ItemVendorDetailsByMarketplace"]):
    def __init__(self, data):
        super().__init__([ItemVendorDetailsByMarketplace(datum) for datum in data])
        self.data = data


class ItemAsin(str):
    pass


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
        url = "/catalog/2020-12-01/items".format()
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
            params["pageSize"] = (pageSize,)
        if pageToken is not None:
            params["pageToken"] = (pageToken,)
        if keywordsLocale is not None:
            params["keywordsLocale"] = (keywordsLocale,)
        if locale is not None:
            params["locale"] = (locale,)
        response = self.request(url, method="GET", params=params)
        return {
            200: ItemSearchResults,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))

    def getCatalogItem(
        self,
        asin: str,
        marketplaceIds: _List[str],
        includedData: _List[str] = None,
        locale: str = None,
    ):
        url = "/catalog/2020-12-01/items/{asin}".format(
            asin=asin,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if includedData is not None:
            params["includedData"] = ",".join(map(str, includedData))
        if locale is not None:
            params["locale"] = (locale,)
        response = self.request(url, method="GET", params=params)
        return {
            200: Item,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self._get_response_json(response))
