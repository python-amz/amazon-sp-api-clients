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


class Issue:
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
        if "severity" in data:
            self.severity: str = str(data["severity"])
        else:
            self.severity: str = None
        if "attributeName" in data:
            self.attributeName: str = str(data["attributeName"])
        else:
            self.attributeName: str = None


class PatchOperation:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "op" in data:
            self.op: str = str(data["op"])
        else:
            self.op: str = None
        if "path" in data:
            self.path: str = str(data["path"])
        else:
            self.path: str = None
        if "value" in data:
            self.value: _List[dict] = [dict(datum) for datum in data["value"]]
        else:
            self.value: _List[dict] = []


class ListingsItemPatchRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None
        if "patches" in data:
            self.patches: _List[PatchOperation] = [PatchOperation(datum) for datum in data["patches"]]
        else:
            self.patches: _List[PatchOperation] = []


class ListingsItemPutRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "productType" in data:
            self.productType: str = str(data["productType"])
        else:
            self.productType: str = None
        if "requirements" in data:
            self.requirements: str = str(data["requirements"])
        else:
            self.requirements: str = None
        if "attributes" in data:
            self.attributes: dict = dict(data["attributes"])
        else:
            self.attributes: dict = None


class ListingsItemSubmissionResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "sku" in data:
            self.sku: str = str(data["sku"])
        else:
            self.sku: str = None
        if "status" in data:
            self.status: str = str(data["status"])
        else:
            self.status: str = None
        if "submissionId" in data:
            self.submissionId: str = str(data["submissionId"])
        else:
            self.submissionId: str = None
        if "issues" in data:
            self.issues: _List[Issue] = [Issue(datum) for datum in data["issues"]]
        else:
            self.issues: _List[Issue] = []


class ListingsItems20200901Client(__BaseClient):
    def putListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        url = "/listings/2020-09-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = (issueLocale,)
        response = self.request(url, method="PUT", data=data.data)
        return {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def deleteListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        url = "/listings/2020-09-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = (issueLocale,)
        response = self.request(url, method="DELETE", data=data.data)
        return {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())

    def patchListingsItem(
        self,
        sellerId: str,
        sku: str,
        marketplaceIds: _List[str],
        issueLocale: str = None,
    ):
        url = "/listings/2020-09-01/items/{sellerId}/{sku}".format(
            sellerId=sellerId,
            sku=sku,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if issueLocale is not None:
            params["issueLocale"] = (issueLocale,)
        response = self.request(url, method="PATCH", data=data.data)
        return {
            200: ListingsItemSubmissionResponse,
            400: ErrorList,
            403: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](response.json())
