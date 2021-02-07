from .base import BaseClient as __BaseClient
from typing import List as _List


class LinkObject:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "href" in data:
            self.href: str = str(data["href"])
        else:
            self.href: str = None
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class SolicitationsAction:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class Schema:
    def __init__(self, data):
        super().__init__()
        self.data = data


class GetSolicitationActionsForOrderResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "_links" in data:
            self._links: dict = dict(data["_links"])
        else:
            self._links: dict = None
        if "_embedded" in data:
            self._embedded: dict = dict(data["_embedded"])
        else:
            self._embedded: dict = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetSolicitationActionResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "_links" in data:
            self._links: dict = dict(data["_links"])
        else:
            self._links: dict = None
        if "_embedded" in data:
            self._embedded: dict = dict(data["_embedded"])
        else:
            self._embedded: dict = None
        if "payload" in data:
            self.payload: SolicitationsAction = SolicitationsAction(data["payload"])
        else:
            self.payload: SolicitationsAction = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetSchemaResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "_links" in data:
            self._links: dict = dict(data["_links"])
        else:
            self._links: dict = None
        if "payload" in data:
            self.payload: Schema = Schema(data["payload"])
        else:
            self.payload: Schema = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateProductReviewAndSellerFeedbackSolicitationResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


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


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class SolicitationsClient(__BaseClient):
    def getSolicitationActionsForOrder(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/solicitations/v1/orders/{amazonOrderId}".format(
            amazonOrderId=amazonOrderId,
        )
        data = {}
        if marketplaceIds is not None:
            data["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=data)
        return {
            200: GetSolicitationActionsForOrderResponse,
            400: GetSolicitationActionsForOrderResponse,
            403: GetSolicitationActionsForOrderResponse,
            404: GetSolicitationActionsForOrderResponse,
            413: GetSolicitationActionsForOrderResponse,
            415: GetSolicitationActionsForOrderResponse,
            429: GetSolicitationActionsForOrderResponse,
            500: GetSolicitationActionsForOrderResponse,
            503: GetSolicitationActionsForOrderResponse,
        }[response.status_code](response.json())

    def createProductReviewAndSellerFeedbackSolicitation(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/solicitations/v1/orders/{amazonOrderId}/solicitations/productReviewAndSellerFeedback".format(
            amazonOrderId=amazonOrderId,
        )
        data = {}
        if marketplaceIds is not None:
            data["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data)
        return {
            201: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            400: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            403: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            404: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            413: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            415: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            429: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            500: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            503: CreateProductReviewAndSellerFeedbackSolicitationResponse,
        }[response.status_code](response.json())
