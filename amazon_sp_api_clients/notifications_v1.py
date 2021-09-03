from .base import BaseClient as __BaseClient
from typing import List as _List


class Subscription:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "subscriptionId" in data:
            self.subscriptionId: str = str(data["subscriptionId"])
        else:
            self.subscriptionId: str = None
        if "payloadVersion" in data:
            self.payloadVersion: str = str(data["payloadVersion"])
        else:
            self.payloadVersion: str = None
        if "destinationId" in data:
            self.destinationId: str = str(data["destinationId"])
        else:
            self.destinationId: str = None


class CreateSubscriptionResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Subscription = Subscription(data["payload"])
        else:
            self.payload: Subscription = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateSubscriptionRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payloadVersion" in data:
            self.payloadVersion: str = str(data["payloadVersion"])
        else:
            self.payloadVersion: str = None
        if "destinationId" in data:
            self.destinationId: str = str(data["destinationId"])
        else:
            self.destinationId: str = None


class GetSubscriptionByIdResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Subscription = Subscription(data["payload"])
        else:
            self.payload: Subscription = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetSubscriptionResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Subscription = Subscription(data["payload"])
        else:
            self.payload: Subscription = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class DeleteSubscriptionByIdResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Destination:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "destinationId" in data:
            self.destinationId: str = str(data["destinationId"])
        else:
            self.destinationId: str = None
        if "resource" in data:
            self.resource: DestinationResource = DestinationResource(data["resource"])
        else:
            self.resource: DestinationResource = None


class DestinationResource:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "sqs" in data:
            self.sqs: SqsResource = SqsResource(data["sqs"])
        else:
            self.sqs: SqsResource = None
        if "eventBridge" in data:
            self.eventBridge: EventBridgeResource = EventBridgeResource(data["eventBridge"])
        else:
            self.eventBridge: EventBridgeResource = None


class DestinationResourceSpecification:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "sqs" in data:
            self.sqs: SqsResource = SqsResource(data["sqs"])
        else:
            self.sqs: SqsResource = None
        if "eventBridge" in data:
            self.eventBridge: EventBridgeResourceSpecification = EventBridgeResourceSpecification(data["eventBridge"])
        else:
            self.eventBridge: EventBridgeResourceSpecification = None


class SqsResource:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "arn" in data:
            self.arn: str = str(data["arn"])
        else:
            self.arn: str = None


class EventBridgeResourceSpecification:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "region" in data:
            self.region: str = str(data["region"])
        else:
            self.region: str = None
        if "accountId" in data:
            self.accountId: str = str(data["accountId"])
        else:
            self.accountId: str = None


class EventBridgeResource:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "region" in data:
            self.region: str = str(data["region"])
        else:
            self.region: str = None
        if "accountId" in data:
            self.accountId: str = str(data["accountId"])
        else:
            self.accountId: str = None


class CreateDestinationRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "resourceSpecification" in data:
            self.resourceSpecification: DestinationResourceSpecification = DestinationResourceSpecification(
                data["resourceSpecification"]
            )
        else:
            self.resourceSpecification: DestinationResourceSpecification = None
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None


class CreateDestinationResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Destination = Destination(data["payload"])
        else:
            self.payload: Destination = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetDestinationResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Destination = Destination(data["payload"])
        else:
            self.payload: Destination = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetDestinationsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: DestinationList = DestinationList(data["payload"])
        else:
            self.payload: DestinationList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class DeleteDestinationResponse:
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


class DestinationList(list, _List["Destination"]):
    def __init__(self, data):
        super().__init__([Destination(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class NotificationType(str):
    pass


class NotificationsV1Client(__BaseClient):
    def getSubscription(
        self,
        notificationType: str,
    ):
        url = "/notifications/v1/subscriptions/{notificationType}".format(
            notificationType=notificationType,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetSubscriptionResponse,
            400: GetSubscriptionResponse,
            403: GetSubscriptionResponse,
            404: GetSubscriptionResponse,
            413: GetSubscriptionResponse,
            415: GetSubscriptionResponse,
            429: GetSubscriptionResponse,
            500: GetSubscriptionResponse,
            503: GetSubscriptionResponse,
        }[response.status_code](self.__get_response_json(response))

    def createSubscription(
        self,
        data: CreateSubscriptionRequest,
        notificationType: str,
    ):
        url = "/notifications/v1/subscriptions/{notificationType}".format(
            notificationType=notificationType,
        )
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            200: CreateSubscriptionResponse,
            400: CreateSubscriptionResponse,
            403: CreateSubscriptionResponse,
            404: CreateSubscriptionResponse,
            409: CreateSubscriptionResponse,
            413: CreateSubscriptionResponse,
            415: CreateSubscriptionResponse,
            429: CreateSubscriptionResponse,
            500: CreateSubscriptionResponse,
            503: CreateSubscriptionResponse,
        }[response.status_code](self.__get_response_json(response))

    def getSubscriptionById(
        self,
        subscriptionId: str,
        notificationType: str,
    ):
        url = "/notifications/v1/subscriptions/{notificationType}/{subscriptionId}".format(
            subscriptionId=subscriptionId,
            notificationType=notificationType,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetSubscriptionByIdResponse,
            400: GetSubscriptionByIdResponse,
            403: GetSubscriptionByIdResponse,
            404: GetSubscriptionResponse,
            409: GetSubscriptionByIdResponse,
            413: GetSubscriptionByIdResponse,
            415: GetSubscriptionByIdResponse,
            429: GetSubscriptionByIdResponse,
            500: GetSubscriptionByIdResponse,
            503: GetSubscriptionByIdResponse,
        }[response.status_code](self.__get_response_json(response))

    def deleteSubscriptionById(
        self,
        subscriptionId: str,
        notificationType: str,
    ):
        url = "/notifications/v1/subscriptions/{notificationType}/{subscriptionId}".format(
            subscriptionId=subscriptionId,
            notificationType=notificationType,
        )
        params = {}
        response = self.request(url, method="DELETE", data=data.data)
        return {
            200: DeleteSubscriptionByIdResponse,
            400: DeleteSubscriptionByIdResponse,
            403: DeleteSubscriptionByIdResponse,
            404: DeleteSubscriptionByIdResponse,
            409: DeleteSubscriptionByIdResponse,
            413: DeleteSubscriptionByIdResponse,
            415: DeleteSubscriptionByIdResponse,
            429: DeleteSubscriptionByIdResponse,
            500: DeleteSubscriptionByIdResponse,
            503: DeleteSubscriptionByIdResponse,
        }[response.status_code](self.__get_response_json(response))

    def getDestinations(
        self,
    ):
        url = "/notifications/v1/destinations".format()
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetDestinationsResponse,
            400: GetDestinationsResponse,
            403: GetDestinationsResponse,
            404: GetDestinationsResponse,
            409: GetDestinationsResponse,
            413: GetDestinationsResponse,
            415: GetDestinationsResponse,
            429: GetDestinationsResponse,
            500: GetDestinationsResponse,
            503: GetDestinationsResponse,
        }[response.status_code](self.__get_response_json(response))

    def createDestination(
        self,
        data: CreateDestinationRequest,
    ):
        url = "/notifications/v1/destinations".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            200: CreateDestinationResponse,
            400: CreateDestinationResponse,
            403: CreateDestinationResponse,
            404: CreateDestinationResponse,
            409: CreateDestinationResponse,
            413: CreateDestinationResponse,
            415: CreateDestinationResponse,
            429: CreateDestinationResponse,
            500: CreateDestinationResponse,
            503: CreateDestinationResponse,
        }[response.status_code](self.__get_response_json(response))

    def getDestination(
        self,
        destinationId: str,
    ):
        url = "/notifications/v1/destinations/{destinationId}".format(
            destinationId=destinationId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetDestinationResponse,
            400: GetDestinationResponse,
            403: GetDestinationResponse,
            404: GetDestinationResponse,
            409: GetDestinationResponse,
            413: GetDestinationResponse,
            415: GetDestinationResponse,
            429: GetDestinationResponse,
            500: GetDestinationResponse,
            503: GetDestinationResponse,
        }[response.status_code](self.__get_response_json(response))

    def deleteDestination(
        self,
        destinationId: str,
    ):
        url = "/notifications/v1/destinations/{destinationId}".format(
            destinationId=destinationId,
        )
        params = {}
        response = self.request(url, method="DELETE", data=data.data)
        return {
            200: DeleteDestinationResponse,
            400: DeleteDestinationResponse,
            403: DeleteDestinationResponse,
            404: DeleteDestinationResponse,
            409: DeleteDestinationResponse,
            413: DeleteDestinationResponse,
            415: DeleteDestinationResponse,
            429: DeleteDestinationResponse,
            500: DeleteDestinationResponse,
            503: DeleteDestinationResponse,
        }[response.status_code](self.__get_response_json(response))
