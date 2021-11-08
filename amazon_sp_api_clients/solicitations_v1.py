from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class LinkObject:
    """
    A Link object.
    """

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
    """
    A simple object containing the name of the template.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class Schema:
    """
    A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data


class GetSolicitationActionsForOrderResponse:
    """
    The response schema for the getSolicitationActionsForOrder operation.
    """

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
    """
    Describes a solicitation action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
    """

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
    """ """

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
    """
    The response schema for the createProductReviewAndSellerFeedbackSolicitation operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


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


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class SolicitationsV1Client(__BaseClient):
    def getSolicitationActionsForOrder(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Returns a list of solicitation types that are available for an order that you specify. A solicitation type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a solicitation. Currently only the productReviewAndSellerFeedbackSolicitation solicitation type is available.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/solicitations/v1/orders/{amazonOrderId}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetSolicitationActionsForOrderResponse,
            400: GetSolicitationActionsForOrderResponse,
            403: GetSolicitationActionsForOrderResponse,
            404: GetSolicitationActionsForOrderResponse,
            413: GetSolicitationActionsForOrderResponse,
            415: GetSolicitationActionsForOrderResponse,
            429: GetSolicitationActionsForOrderResponse,
            500: GetSolicitationActionsForOrderResponse,
            503: GetSolicitationActionsForOrderResponse,
        }[response.status_code]
        return None if response_type is None else response_type(self._get_response_json(response))

    def createProductReviewAndSellerFeedbackSolicitation(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a solicitation to a buyer asking for seller feedback and a product review for the specified order. Send only one productReviewAndSellerFeedback or free form proactive message per order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/solicitations/v1/orders/{amazonOrderId}/solicitations/productReviewAndSellerFeedback"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
        )
        response_type = {
            201: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            400: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            403: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            404: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            413: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            415: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            429: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            500: CreateProductReviewAndSellerFeedbackSolicitationResponse,
            503: CreateProductReviewAndSellerFeedbackSolicitationResponse,
        }[response.status_code]
        return None if response_type is None else response_type(self._get_response_json(response))
