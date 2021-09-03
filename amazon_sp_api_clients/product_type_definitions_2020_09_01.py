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


class SchemaLink:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "link" in data:
            self.link: dict = dict(data["link"])
        else:
            self.link: dict = None
        if "checksum" in data:
            self.checksum: str = str(data["checksum"])
        else:
            self.checksum: str = None


class ProductTypeDefinition:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "metaSchema" in data:
            self.metaSchema: SchemaLink = SchemaLink(data["metaSchema"])
        else:
            self.metaSchema: SchemaLink = None
        if "schema" in data:
            self.schema: SchemaLink = SchemaLink(data["schema"])
        else:
            self.schema: SchemaLink = None
        if "requirements" in data:
            self.requirements: str = str(data["requirements"])
        else:
            self.requirements: str = None
        if "requirementsEnforced" in data:
            self.requirementsEnforced: str = str(data["requirementsEnforced"])
        else:
            self.requirementsEnforced: str = None
        if "propertyGroups" in data:
            self.propertyGroups: dict = dict(data["propertyGroups"])
        else:
            self.propertyGroups: dict = None
        if "locale" in data:
            self.locale: str = str(data["locale"])
        else:
            self.locale: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None
        if "productTypeVersion" in data:
            self.productTypeVersion: ProductTypeVersion = ProductTypeVersion(data["productTypeVersion"])
        else:
            self.productTypeVersion: ProductTypeVersion = None


class PropertyGroup:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None
        if "propertyNames" in data:
            self.propertyNames: _List[str] = [str(datum) for datum in data["propertyNames"]]
        else:
            self.propertyNames: _List[str] = []


class ProductTypeVersion:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "version" in data:
            self.version: str = str(data["version"])
        else:
            self.version: str = None
        if "latest" in data:
            self.latest: bool = bool(data["latest"])
        else:
            self.latest: bool = None
        if "releaseCandidate" in data:
            self.releaseCandidate: bool = bool(data["releaseCandidate"])
        else:
            self.releaseCandidate: bool = None


class ProductType:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []


class ProductTypeList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "productTypes" in data:
            self.productTypes: _List[ProductType] = [ProductType(datum) for datum in data["productTypes"]]
        else:
            self.productTypes: _List[ProductType] = []


class ProductTypeDefinitions20200901Client(__BaseClient):
    def searchDefinitionsProductTypes(
        self,
        marketplaceIds: _List[str],
        keywords: _List[str] = None,
    ):
        url = "/definitions/2020-09-01/productTypes".format()
        params = {}
        if keywords is not None:
            params["keywords"] = ",".join(map(str, keywords))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=params)
        return {
            200: ProductTypeList,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def getDefinitionsProductType(
        self,
        productType: str,
        marketplaceIds: _List[str],
        sellerId: str = None,
        productTypeVersion: str = None,
        requirements: str = None,
        requirementsEnforced: str = None,
        locale: str = None,
    ):
        url = "/definitions/2020-09-01/productTypes/{productType}".format(
            productType=productType,
        )
        params = {}
        if sellerId is not None:
            params["sellerId"] = (sellerId,)
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if productTypeVersion is not None:
            params["productTypeVersion"] = (productTypeVersion,)
        if requirements is not None:
            params["requirements"] = (requirements,)
        if requirementsEnforced is not None:
            params["requirementsEnforced"] = (requirementsEnforced,)
        if locale is not None:
            params["locale"] = (locale,)
        response = self.request(url, method="GET", params=params)
        return {
            200: ProductTypeDefinition,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))
