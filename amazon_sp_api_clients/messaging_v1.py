from .base import BaseClient as __BaseClient
from typing import List as _List


class Attachment:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "uploadDestinationId" in data:
            self.uploadDestinationId: str = str(data["uploadDestinationId"])
        else:
            self.uploadDestinationId: str = None
        if "fileName" in data:
            self.fileName: str = str(data["fileName"])
        else:
            self.fileName: str = None


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


class MessagingAction:
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


class GetMessagingActionsForOrderResponse:
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


class GetMessagingActionResponse:
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
            self.payload: MessagingAction = MessagingAction(data["payload"])
        else:
            self.payload: MessagingAction = None
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


class CreateConfirmCustomizationDetailsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateConfirmCustomizationDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateConfirmDeliveryDetailsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateConfirmDeliveryDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateNegativeFeedbackRemovalResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateLegalDisclosureRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateLegalDisclosureResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateConfirmOrderDetailsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateConfirmOrderDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateConfirmServiceDetailsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateConfirmServiceDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateAmazonMotorsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateAmazonMotorsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateWarrantyRequest:
    def __init__(self, data):
        super().__init__()
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


class CreateWarrantyResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetAttributesResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "buyer" in data:
            self.buyer: dict = dict(data["buyer"])
        else:
            self.buyer: dict = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateDigitalAccessKeyRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None
        if "attachments" in data:
            self.attachments: _List[Attachment] = [Attachment(datum) for datum in data["attachments"]]
        else:
            self.attachments: _List[Attachment] = []


class CreateDigitalAccessKeyResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateUnexpectedProblemRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "text" in data:
            self.text: str = str(data["text"])
        else:
            self.text: str = None


class CreateUnexpectedProblemResponse:
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


class MessagingV1Client(__BaseClient):
    def getMessagingActionsForOrder(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=params)
        return {
            200: GetMessagingActionsForOrderResponse,
            400: GetMessagingActionsForOrderResponse,
            403: GetMessagingActionsForOrderResponse,
            404: GetMessagingActionsForOrderResponse,
            413: GetMessagingActionsForOrderResponse,
            415: GetMessagingActionsForOrderResponse,
            429: GetMessagingActionsForOrderResponse,
            500: GetMessagingActionsForOrderResponse,
            503: GetMessagingActionsForOrderResponse,
        }[response.status_code](response.json())

    def confirmCustomizationDetails(
        self,
        data: CreateConfirmCustomizationDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateConfirmCustomizationDetailsResponse,
            400: CreateConfirmCustomizationDetailsResponse,
            403: CreateConfirmCustomizationDetailsResponse,
            404: CreateConfirmCustomizationDetailsResponse,
            413: CreateConfirmCustomizationDetailsResponse,
            415: CreateConfirmCustomizationDetailsResponse,
            429: CreateConfirmCustomizationDetailsResponse,
            500: CreateConfirmCustomizationDetailsResponse,
            503: CreateConfirmCustomizationDetailsResponse,
        }[response.status_code](response.json())

    def createConfirmDeliveryDetails(
        self,
        data: CreateConfirmDeliveryDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateConfirmDeliveryDetailsResponse,
            400: CreateConfirmDeliveryDetailsResponse,
            403: CreateConfirmDeliveryDetailsResponse,
            404: CreateConfirmDeliveryDetailsResponse,
            413: CreateConfirmDeliveryDetailsResponse,
            415: CreateConfirmDeliveryDetailsResponse,
            429: CreateConfirmDeliveryDetailsResponse,
            500: CreateConfirmDeliveryDetailsResponse,
            503: CreateConfirmDeliveryDetailsResponse,
        }[response.status_code](response.json())

    def createLegalDisclosure(
        self,
        data: CreateLegalDisclosureRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateLegalDisclosureResponse,
            400: CreateLegalDisclosureResponse,
            403: CreateLegalDisclosureResponse,
            404: CreateLegalDisclosureResponse,
            413: CreateLegalDisclosureResponse,
            415: CreateLegalDisclosureResponse,
            429: CreateLegalDisclosureResponse,
            500: CreateLegalDisclosureResponse,
            503: CreateLegalDisclosureResponse,
        }[response.status_code](response.json())

    def createNegativeFeedbackRemoval(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/negativeFeedbackRemoval".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateNegativeFeedbackRemovalResponse,
            400: CreateNegativeFeedbackRemovalResponse,
            403: CreateNegativeFeedbackRemovalResponse,
            404: CreateNegativeFeedbackRemovalResponse,
            413: CreateNegativeFeedbackRemovalResponse,
            415: CreateNegativeFeedbackRemovalResponse,
            429: CreateNegativeFeedbackRemovalResponse,
            500: CreateNegativeFeedbackRemovalResponse,
            503: CreateNegativeFeedbackRemovalResponse,
        }[response.status_code](response.json())

    def createConfirmOrderDetails(
        self,
        data: CreateConfirmOrderDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateConfirmOrderDetailsResponse,
            400: CreateConfirmOrderDetailsResponse,
            403: CreateConfirmOrderDetailsResponse,
            404: CreateConfirmOrderDetailsResponse,
            413: CreateConfirmOrderDetailsResponse,
            415: CreateConfirmOrderDetailsResponse,
            429: CreateConfirmOrderDetailsResponse,
            500: CreateConfirmOrderDetailsResponse,
            503: CreateConfirmOrderDetailsResponse,
        }[response.status_code](response.json())

    def createConfirmServiceDetails(
        self,
        data: CreateConfirmServiceDetailsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateConfirmServiceDetailsResponse,
            400: CreateConfirmServiceDetailsResponse,
            403: CreateConfirmServiceDetailsResponse,
            404: CreateConfirmServiceDetailsResponse,
            413: CreateConfirmServiceDetailsResponse,
            415: CreateConfirmServiceDetailsResponse,
            429: CreateConfirmServiceDetailsResponse,
            500: CreateConfirmServiceDetailsResponse,
            503: CreateConfirmServiceDetailsResponse,
        }[response.status_code](response.json())

    def CreateAmazonMotors(
        self,
        data: CreateAmazonMotorsRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/amazonMotors".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateAmazonMotorsResponse,
            400: CreateAmazonMotorsResponse,
            403: CreateAmazonMotorsResponse,
            404: CreateAmazonMotorsResponse,
            413: CreateAmazonMotorsResponse,
            415: CreateAmazonMotorsResponse,
            429: CreateAmazonMotorsResponse,
            500: CreateAmazonMotorsResponse,
            503: CreateAmazonMotorsResponse,
        }[response.status_code](response.json())

    def CreateWarranty(
        self,
        data: CreateWarrantyRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/warranty".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateWarrantyResponse,
            400: CreateWarrantyResponse,
            403: CreateWarrantyResponse,
            404: CreateWarrantyResponse,
            413: CreateWarrantyResponse,
            415: CreateWarrantyResponse,
            429: CreateWarrantyResponse,
            500: CreateWarrantyResponse,
            503: CreateWarrantyResponse,
        }[response.status_code](response.json())

    def GetAttributes(
        self,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/attributes".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=params)
        return {
            200: GetAttributesResponse,
            400: GetAttributesResponse,
            403: GetAttributesResponse,
            404: GetAttributesResponse,
            413: GetAttributesResponse,
            415: GetAttributesResponse,
            429: GetAttributesResponse,
            500: GetAttributesResponse,
            503: GetAttributesResponse,
        }[response.status_code](response.json())

    def createDigitalAccessKey(
        self,
        data: CreateDigitalAccessKeyRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateDigitalAccessKeyResponse,
            400: CreateDigitalAccessKeyResponse,
            403: CreateDigitalAccessKeyResponse,
            404: CreateDigitalAccessKeyResponse,
            413: CreateDigitalAccessKeyResponse,
            415: CreateDigitalAccessKeyResponse,
            429: CreateDigitalAccessKeyResponse,
            500: CreateDigitalAccessKeyResponse,
            503: CreateDigitalAccessKeyResponse,
        }[response.status_code](response.json())

    def createUnexpectedProblem(
        self,
        data: CreateUnexpectedProblemRequest,
        amazonOrderId: str,
        marketplaceIds: _List[str],
    ):
        url = "/messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem".format(
            amazonOrderId=amazonOrderId,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="POST", data=data.data)
        return {
            201: CreateUnexpectedProblemResponse,
            400: CreateUnexpectedProblemResponse,
            403: CreateUnexpectedProblemResponse,
            404: CreateUnexpectedProblemResponse,
            413: CreateUnexpectedProblemResponse,
            415: CreateUnexpectedProblemResponse,
            429: CreateUnexpectedProblemResponse,
            500: CreateUnexpectedProblemResponse,
            503: CreateUnexpectedProblemResponse,
        }[response.status_code](response.json())
