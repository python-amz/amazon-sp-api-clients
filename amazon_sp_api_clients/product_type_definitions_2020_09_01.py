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


class SchemaLink(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "link" in data:
            self.link: dict = self._get_value(dict, "link")
        else:
            self.link: dict = None
        if "checksum" in data:
            self.checksum: str = self._get_value(str, "checksum")
        else:
            self.checksum: str = None


class ProductTypeDefinition(__BaseDictObject):
    """
    A product type definition represents the attributes and data requirements for a product type in the Amazon catalog. Product type definitions are used interchangeably between the Selling Partner API for Listings Items, Selling Partner API for Catalog Items, and JSON-based listings feeds in the Selling Partner API for Feeds.
    """

    def __init__(self, data):
        super().__init__(data)
        if "metaSchema" in data:
            self.metaSchema: SchemaLink = self._get_value(SchemaLink, "metaSchema")
        else:
            self.metaSchema: SchemaLink = None
        if "schema" in data:
            self.schema: SchemaLink = self._get_value(SchemaLink, "schema")
        else:
            self.schema: SchemaLink = None
        if "requirements" in data:
            self.requirements: str = self._get_value(str, "requirements")
        else:
            self.requirements: str = None
        if "requirementsEnforced" in data:
            self.requirementsEnforced: str = self._get_value(str, "requirementsEnforced")
        else:
            self.requirementsEnforced: str = None
        if "propertyGroups" in data:
            self.propertyGroups: dict = self._get_value(dict, "propertyGroups")
        else:
            self.propertyGroups: dict = None
        if "locale" in data:
            self.locale: str = self._get_value(str, "locale")
        else:
            self.locale: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "productType" in data:
            self.productType: str = self._get_value(str, "productType")
        else:
            self.productType: str = None
        if "displayName" in data:
            self.displayName: str = self._get_value(str, "displayName")
        else:
            self.displayName: str = None
        if "productTypeVersion" in data:
            self.productTypeVersion: ProductTypeVersion = self._get_value(ProductTypeVersion, "productTypeVersion")
        else:
            self.productTypeVersion: ProductTypeVersion = None


class PropertyGroup(__BaseDictObject):
    """
    A property group represents a logical grouping of schema properties that can be used for display or informational purposes.
    """

    def __init__(self, data):
        super().__init__(data)
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None
        if "description" in data:
            self.description: str = self._get_value(str, "description")
        else:
            self.description: str = None
        if "propertyNames" in data:
            self.propertyNames: _List[str] = [str(datum) for datum in data["propertyNames"]]
        else:
            self.propertyNames: _List[str] = []


class ProductTypeVersion(__BaseDictObject):
    """
    The version details for an Amazon product type.
    """

    def __init__(self, data):
        super().__init__(data)
        if "version" in data:
            self.version: str = self._get_value(str, "version")
        else:
            self.version: str = None
        if "latest" in data:
            self.latest: bool = self._get_value(convert_bool, "latest")
        else:
            self.latest: bool = None
        if "releaseCandidate" in data:
            self.releaseCandidate: bool = self._get_value(convert_bool, "releaseCandidate")
        else:
            self.releaseCandidate: bool = None


class ProductType(__BaseDictObject):
    """
    An Amazon product type with a definition available.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "displayName" in data:
            self.displayName: str = self._get_value(str, "displayName")
        else:
            self.displayName: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []


class ProductTypeList(__BaseDictObject):
    """
    A list of Amazon product types with definitions available.
    """

    def __init__(self, data):
        super().__init__(data)
        if "productTypes" in data:
            self.productTypes: _List[ProductType] = [ProductType(datum) for datum in data["productTypes"]]
        else:
            self.productTypes: _List[ProductType] = []
        if "productTypeVersion" in data:
            self.productTypeVersion: str = self._get_value(str, "productTypeVersion")
        else:
            self.productTypeVersion: str = None


class ProductTypeDefinitions20200901Client(__BaseClient):
    def searchDefinitionsProductTypes(
        self,
        marketplaceIds: _List[str],
        keywords: _List[str] = None,
        itemName: str = None,
        locale: str = None,
        searchLocale: str = None,
    ):
        """
                Search for and return a list of Amazon product types that have definitions available.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/definitions/2020-09-01/productTypes"
        params = {}
        if keywords is not None:
            params["keywords"] = ",".join(map(str, keywords))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if itemName is not None:
            params["itemName"] = itemName
        if locale is not None:
            params["locale"] = locale
        if searchLocale is not None:
            params["searchLocale"] = searchLocale
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ProductTypeList,
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
        """
                Retrieve an Amazon product type definition.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/definitions/2020-09-01/productTypes/{productType}"
        params = {}
        if sellerId is not None:
            params["sellerId"] = sellerId
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if productTypeVersion is not None:
            params["productTypeVersion"] = productTypeVersion
        if requirements is not None:
            params["requirements"] = requirements
        if requirementsEnforced is not None:
            params["requirementsEnforced"] = requirementsEnforced
        if locale is not None:
            params["locale"] = locale
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ProductTypeDefinition,
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
