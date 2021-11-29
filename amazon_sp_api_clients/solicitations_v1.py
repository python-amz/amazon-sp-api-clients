from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class LinkObject(__BaseDictObject):
    """
    A Link object.
    """

    def __init__(self, data):
        super().__init__(data)
        if "href" in data:
            self.href: str = self._get_value(str, "href")
        else:
            self.href: str = None
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None


class SolicitationsAction(__BaseDictObject):
    """
    A simple object containing the name of the template.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None


class Schema(__BaseDictObject):
    """
    A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
    """

    def __init__(self, data):
        super().__init__(data)


class GetSolicitationActionsForOrderResponse(__BaseDictObject):
    """
    The response schema for the getSolicitationActionsForOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "_links" in data:
            self._links: dict = self._get_value(dict, "_links")
        else:
            self._links: dict = None
        if "_embedded" in data:
            self._embedded: dict = self._get_value(dict, "_embedded")
        else:
            self._embedded: dict = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetSolicitationActionResponse(__BaseDictObject):
    """
    Describes a solicitation action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
    """

    def __init__(self, data):
        super().__init__(data)
        if "_links" in data:
            self._links: dict = self._get_value(dict, "_links")
        else:
            self._links: dict = None
        if "_embedded" in data:
            self._embedded: dict = self._get_value(dict, "_embedded")
        else:
            self._embedded: dict = None
        if "payload" in data:
            self.payload: SolicitationsAction = self._get_value(SolicitationsAction, "payload")
        else:
            self.payload: SolicitationsAction = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetSchemaResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "_links" in data:
            self._links: dict = self._get_value(dict, "_links")
        else:
            self._links: dict = None
        if "payload" in data:
            self.payload: Schema = self._get_value(Schema, "payload")
        else:
            self.payload: Schema = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateProductReviewAndSellerFeedbackSolicitationResponse(__BaseDictObject):
    """
    The response schema for the createProductReviewAndSellerFeedbackSolicitation operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


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
        }.get(response.status_code, None)
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
