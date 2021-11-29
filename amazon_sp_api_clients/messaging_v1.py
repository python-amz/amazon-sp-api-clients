from .base import BaseClient as __BaseClient, convert_bool, BaseObject as __BaseObject
from typing import List as _List


class Attachment(__BaseObject):
    """
    Represents a file uploaded to a destination that was created by the createUploadDestination operation of the Uploads API.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = str(data["uploadDestinationId"])
        else:
            self.uploadDestinationId: str = None
        if "fileName" in data:
            self.fileName: str = str(data["fileName"])
        else:
            self.fileName: str = None


class LinkObject(__BaseObject):
    """
    A Link object.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "href" in data:
            self.href: str = str(data["href"])
        else:
            self.href: str = None
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class MessagingAction(__BaseObject):
    """
    A simple object containing the name of the template.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class Schema(__BaseObject):
    """
    A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data


class GetMessagingActionsForOrderResponse(__BaseObject):
    """
    The response schema for the getMessagingActionsForOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
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


class GetMessagingActionResponse(__BaseObject):
    """
    Describes a messaging action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
    """

    def __init__(self, data):
        super().__init__(data)
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
            self.payload: MessagingAction = MessagingAction(data["payload"])
        else:
            self.payload: MessagingAction = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetSchemaResponse(__BaseObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
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


class CreateConfirmCustomizationDetailsRequest(__BaseObject):
    """
    The request schema for the confirmCustomizationDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateConfirmCustomizationDetailsResponse(__BaseObject):
    """
    The response schema for the confirmCustomizationDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateConfirmDeliveryDetailsRequest(__BaseObject):
    """
    The request schema for the createConfirmDeliveryDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateConfirmDeliveryDetailsResponse(__BaseObject):
    """
    The response schema for the createConfirmDeliveryDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateNegativeFeedbackRemovalResponse(__BaseObject):
    """
    The response schema for the createNegativeFeedbackRemoval operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateLegalDisclosureRequest(__BaseObject):
    """
    The request schema for the createLegalDisclosure operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateLegalDisclosureResponse(__BaseObject):
    """
    The response schema for the createLegalDisclosure operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateConfirmOrderDetailsRequest(__BaseObject):
    """
    The request schema for the createConfirmOrderDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateConfirmOrderDetailsResponse(__BaseObject):
    """
    The response schema for the createConfirmOrderDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateConfirmServiceDetailsRequest(__BaseObject):
    """
    The request schema for the createConfirmServiceDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateConfirmServiceDetailsResponse(__BaseObject):
    """
    The response schema for the createConfirmServiceDetails operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateAmazonMotorsRequest(__BaseObject):
    """
    The request schema for the createAmazonMotors operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateAmazonMotorsResponse(__BaseObject):
    """
    The response schema for the createAmazonMotors operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateWarrantyRequest(__BaseObject):
    """
    The request schema for the createWarranty operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []
        if "coverageStartDate" in data:
            self.coverageStartDate: str = str(data["coverageStartDate"])
        else:
            self.coverageStartDate: str = None
        if "coverageEndDate" in data:
            self.coverageEndDate: str = str(data["coverageEndDate"])
        else:
            self.coverageEndDate: str = None


class CreateWarrantyResponse(__BaseObject):
    """
    The response schema for the createWarranty operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetAttributesResponse(__BaseObject):
    """
    The response schema for the GetAttributes operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "buyer" in data:
            self.buyer: dict = dict(data["buyer"])
        else:
            self.buyer: dict = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateDigitalAccessKeyRequest(__BaseObject):
    """
    The request schema for the createDigitalAccessKey operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateDigitalAccessKeyResponse(__BaseObject):
    """
    The response schema for the createDigitalAccessKey operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateUnexpectedProblemRequest(__BaseObject):
    """
    The request schema for the createUnexpectedProblem operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateUnexpectedProblemResponse(__BaseObject):
    """
    The response schema for the createUnexpectedProblem operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Error(__BaseObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
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


class MessagingV1Client(__BaseClient):
    def getMessagingActionsForOrder(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Returns a list of message types that are available for an order that you specify. A message type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a message.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetMessagingActionsForOrderResponse,
            400: GetMessagingActionsForOrderResponse,
            403: GetMessagingActionsForOrderResponse,
            404: GetMessagingActionsForOrderResponse,
            413: GetMessagingActionsForOrderResponse,
            415: GetMessagingActionsForOrderResponse,
            429: GetMessagingActionsForOrderResponse,
            500: GetMessagingActionsForOrderResponse,
            503: GetMessagingActionsForOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def confirmCustomizationDetails(
        self,
        data: CreateConfirmCustomizationDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message asking a buyer to provide or verify customization details such as name spelling, images, initials, etc.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateConfirmCustomizationDetailsResponse,
            400: CreateConfirmCustomizationDetailsResponse,
            403: CreateConfirmCustomizationDetailsResponse,
            404: CreateConfirmCustomizationDetailsResponse,
            413: CreateConfirmCustomizationDetailsResponse,
            415: CreateConfirmCustomizationDetailsResponse,
            429: CreateConfirmCustomizationDetailsResponse,
            500: CreateConfirmCustomizationDetailsResponse,
            503: CreateConfirmCustomizationDetailsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createConfirmDeliveryDetails(
        self,
        data: CreateConfirmDeliveryDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message to a buyer to arrange a delivery or to confirm contact information for making a delivery.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateConfirmDeliveryDetailsResponse,
            400: CreateConfirmDeliveryDetailsResponse,
            403: CreateConfirmDeliveryDetailsResponse,
            404: CreateConfirmDeliveryDetailsResponse,
            413: CreateConfirmDeliveryDetailsResponse,
            415: CreateConfirmDeliveryDetailsResponse,
            429: CreateConfirmDeliveryDetailsResponse,
            500: CreateConfirmDeliveryDetailsResponse,
            503: CreateConfirmDeliveryDetailsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createLegalDisclosure(
        self,
        data: CreateLegalDisclosureRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a critical message that contains documents that a seller is legally obligated to provide to the buyer. This message should only be used to deliver documents that are required by law.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateLegalDisclosureResponse,
            400: CreateLegalDisclosureResponse,
            403: CreateLegalDisclosureResponse,
            404: CreateLegalDisclosureResponse,
            413: CreateLegalDisclosureResponse,
            415: CreateLegalDisclosureResponse,
            429: CreateLegalDisclosureResponse,
            500: CreateLegalDisclosureResponse,
            503: CreateLegalDisclosureResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createNegativeFeedbackRemoval(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a non-critical message that asks a buyer to remove their negative feedback. This message should only be sent after the seller has resolved the buyer's problem.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/negativeFeedbackRemoval"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
        )
        response_type = {
            201: CreateNegativeFeedbackRemovalResponse,
            400: CreateNegativeFeedbackRemovalResponse,
            403: CreateNegativeFeedbackRemovalResponse,
            404: CreateNegativeFeedbackRemovalResponse,
            413: CreateNegativeFeedbackRemovalResponse,
            415: CreateNegativeFeedbackRemovalResponse,
            429: CreateNegativeFeedbackRemovalResponse,
            500: CreateNegativeFeedbackRemovalResponse,
            503: CreateNegativeFeedbackRemovalResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createConfirmOrderDetails(
        self,
        data: CreateConfirmOrderDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message to ask a buyer an order-related question prior to shipping their order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateConfirmOrderDetailsResponse,
            400: CreateConfirmOrderDetailsResponse,
            403: CreateConfirmOrderDetailsResponse,
            404: CreateConfirmOrderDetailsResponse,
            413: CreateConfirmOrderDetailsResponse,
            415: CreateConfirmOrderDetailsResponse,
            429: CreateConfirmOrderDetailsResponse,
            500: CreateConfirmOrderDetailsResponse,
            503: CreateConfirmOrderDetailsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createConfirmServiceDetails(
        self,
        data: CreateConfirmServiceDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message to contact a Home Service customer to arrange a service call or to gather information prior to a service call.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateConfirmServiceDetailsResponse,
            400: CreateConfirmServiceDetailsResponse,
            403: CreateConfirmServiceDetailsResponse,
            404: CreateConfirmServiceDetailsResponse,
            413: CreateConfirmServiceDetailsResponse,
            415: CreateConfirmServiceDetailsResponse,
            429: CreateConfirmServiceDetailsResponse,
            500: CreateConfirmServiceDetailsResponse,
            503: CreateConfirmServiceDetailsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def CreateAmazonMotors(
        self,
        data: CreateAmazonMotorsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message to a buyer to provide details about an Amazon Motors order. This message can only be sent by Amazon Motors sellers.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/amazonMotors"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateAmazonMotorsResponse,
            400: CreateAmazonMotorsResponse,
            403: CreateAmazonMotorsResponse,
            404: CreateAmazonMotorsResponse,
            413: CreateAmazonMotorsResponse,
            415: CreateAmazonMotorsResponse,
            429: CreateAmazonMotorsResponse,
            500: CreateAmazonMotorsResponse,
            503: CreateAmazonMotorsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def CreateWarranty(
        self,
        data: CreateWarrantyRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message to a buyer to provide details about warranty information on a purchase in their order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/warranty"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateWarrantyResponse,
            400: CreateWarrantyResponse,
            403: CreateWarrantyResponse,
            404: CreateWarrantyResponse,
            413: CreateWarrantyResponse,
            415: CreateWarrantyResponse,
            429: CreateWarrantyResponse,
            500: CreateWarrantyResponse,
            503: CreateWarrantyResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def GetAttributes(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Returns a response containing attributes related to an order. This includes buyer preferences.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/attributes"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetAttributesResponse,
            400: GetAttributesResponse,
            403: GetAttributesResponse,
            404: GetAttributesResponse,
            413: GetAttributesResponse,
            415: GetAttributesResponse,
            429: GetAttributesResponse,
            500: GetAttributesResponse,
            503: GetAttributesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createDigitalAccessKey(
        self,
        data: CreateDigitalAccessKeyRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a message to a buyer to share a digital access key needed to utilize digital content in their order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateDigitalAccessKeyResponse,
            400: CreateDigitalAccessKeyResponse,
            403: CreateDigitalAccessKeyResponse,
            404: CreateDigitalAccessKeyResponse,
            413: CreateDigitalAccessKeyResponse,
            415: CreateDigitalAccessKeyResponse,
            429: CreateDigitalAccessKeyResponse,
            500: CreateDigitalAccessKeyResponse,
            503: CreateDigitalAccessKeyResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createUnexpectedProblem(
        self,
        data: CreateUnexpectedProblemRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        """
                Sends a critical message to a buyer that an unexpected problem was encountered affecting the completion of the order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            201: CreateUnexpectedProblemResponse,
            400: CreateUnexpectedProblemResponse,
            403: CreateUnexpectedProblemResponse,
            404: CreateUnexpectedProblemResponse,
            413: CreateUnexpectedProblemResponse,
            415: CreateUnexpectedProblemResponse,
            429: CreateUnexpectedProblemResponse,
            500: CreateUnexpectedProblemResponse,
            503: CreateUnexpectedProblemResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
