from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


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


class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Item:
    """
    An item in the Amazon catalog.
    """

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
    """
    A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data


class ItemIdentifiersByMarketplace:
    """
    Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
    """

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
    """
    Identifier associated with the item in the Amazon catalog, such as a UPC or EAN identifier.
    """

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
    """
    Images for an item in the Amazon catalog for the indicated Amazon marketplace.
    """

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
    """
    Image for an item in the Amazon catalog.
    """

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
    """
    Product type associated with the Amazon catalog item for the indicated Amazon marketplace.
    """

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
    """
    Sales ranks of an Amazon catalog item for the indicated Amazon marketplace.
    """

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
    """
    Sales rank of an Amazon catalog item.
    """

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
    """
    Summary details of an Amazon catalog item for the indicated Amazon marketplace.
    """

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
    """
    Variation details for the Amazon catalog item for the indicated Amazon marketplace.
    """

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
    """
    Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace.
    """

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
    """
    Items in the Amazon catalog and search related metadata.
    """

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
    """
    When a request produces a response that exceeds the pageSize, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the nextToken value or the previousToken value as the pageToken parameter in the next request. When you receive the last page, there will be no nextToken key in the pagination object.
    """

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
    """
    Search refinements.
    """

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
    """
    Description of a brand that can be used to get more fine-grained search results.
    """

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
    """
    Description of a classification that can be used to get more fine-grained search results.
    """

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
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
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
        }[response.status_code]
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
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
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
        }[response.status_code]
        return None if response_type is None else response_type(self._get_response_json(response))
