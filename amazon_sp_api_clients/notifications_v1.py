from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class Subscription(__BaseDictObject):
    """
    Represents a subscription to receive notifications.
    """

    def __init__(self, data):
        super().__init__(data)
        if "subscriptionId" in data:
            self.subscriptionId: str = self._get_value(str, "subscriptionId")
        else:
            self.subscriptionId: str = None
        if "payloadVersion" in data:
            self.payloadVersion: str = self._get_value(str, "payloadVersion")
        else:
            self.payloadVersion: str = None
        if "destinationId" in data:
            self.destinationId: str = self._get_value(str, "destinationId")
        else:
            self.destinationId: str = None


class CreateSubscriptionResponse(__BaseDictObject):
    """
    The response schema for the createSubscription operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Subscription = self._get_value(Subscription, "payload")
        else:
            self.payload: Subscription = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateSubscriptionRequest(__BaseDictObject):
    """
    The request schema for the createSubscription operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payloadVersion" in data:
            self.payloadVersion: str = self._get_value(str, "payloadVersion")
        else:
            self.payloadVersion: str = None
        if "destinationId" in data:
            self.destinationId: str = self._get_value(str, "destinationId")
        else:
            self.destinationId: str = None


class GetSubscriptionByIdResponse(__BaseDictObject):
    """
    The response schema for the getSubscriptionById operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Subscription = self._get_value(Subscription, "payload")
        else:
            self.payload: Subscription = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetSubscriptionResponse(__BaseDictObject):
    """
    The response schema for the getSubscription operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Subscription = self._get_value(Subscription, "payload")
        else:
            self.payload: Subscription = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class DeleteSubscriptionByIdResponse(__BaseDictObject):
    """
    The response schema for the deleteSubscriptionById operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Destination(__BaseDictObject):
    """
    Represents a destination created when you call the createDestination operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "destinationId" in data:
            self.destinationId: str = self._get_value(str, "destinationId")
        else:
            self.destinationId: str = None
        if "resource" in data:
            self.resource: DestinationResource = self._get_value(DestinationResource, "resource")
        else:
            self.resource: DestinationResource = None


class DestinationResource(__BaseDictObject):
    """
    The destination resource types.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sqs" in data:
            self.sqs: SqsResource = self._get_value(SqsResource, "sqs")
        else:
            self.sqs: SqsResource = None
        if "eventBridge" in data:
            self.eventBridge: EventBridgeResource = self._get_value(EventBridgeResource, "eventBridge")
        else:
            self.eventBridge: EventBridgeResource = None


class DestinationResourceSpecification(__BaseDictObject):
    """
    The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sqs" in data:
            self.sqs: SqsResource = self._get_value(SqsResource, "sqs")
        else:
            self.sqs: SqsResource = None
        if "eventBridge" in data:
            self.eventBridge: EventBridgeResourceSpecification = self._get_value(
                EventBridgeResourceSpecification, "eventBridge"
            )
        else:
            self.eventBridge: EventBridgeResourceSpecification = None


class SqsResource(__BaseDictObject):
    """
    The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.
    """

    def __init__(self, data):
        super().__init__(data)
        if "arn" in data:
            self.arn: str = self._get_value(str, "arn")
        else:
            self.arn: str = None


class EventBridgeResourceSpecification(__BaseDictObject):
    """
    The information required to create an Amazon EventBridge destination.
    """

    def __init__(self, data):
        super().__init__(data)
        if "region" in data:
            self.region: str = self._get_value(str, "region")
        else:
            self.region: str = None
        if "accountId" in data:
            self.accountId: str = self._get_value(str, "accountId")
        else:
            self.accountId: str = None


class EventBridgeResource(__BaseDictObject):
    """
    Represents an Amazon EventBridge destination.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "region" in data:
            self.region: str = self._get_value(str, "region")
        else:
            self.region: str = None
        if "accountId" in data:
            self.accountId: str = self._get_value(str, "accountId")
        else:
            self.accountId: str = None


class CreateDestinationRequest(__BaseDictObject):
    """
    The request schema for the createDestination operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "resourceSpecification" in data:
            self.resourceSpecification: DestinationResourceSpecification = self._get_value(
                DestinationResourceSpecification, "resourceSpecification"
            )
        else:
            self.resourceSpecification: DestinationResourceSpecification = None
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None


class CreateDestinationResponse(__BaseDictObject):
    """
    The response schema for the createDestination operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Destination = self._get_value(Destination, "payload")
        else:
            self.payload: Destination = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetDestinationResponse(__BaseDictObject):
    """
    The response schema for the getDestination operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Destination = self._get_value(Destination, "payload")
        else:
            self.payload: Destination = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetDestinationsResponse(__BaseDictObject):
    """
    The response schema for the getDestinations operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: DestinationList = self._get_value(DestinationList, "payload")
        else:
            self.payload: DestinationList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class DeleteDestinationResponse(__BaseDictObject):
    """
    The response schema for the deleteDestination operation.
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


class DestinationList(list, _List["Destination"]):
    """
    A list of destinations.
    """

    def __init__(self, data):
        super().__init__([Destination(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class NotificationType(str):
    """
       The type of notification.
    For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
    """


class NotificationsV1Client(__BaseClient):
    def getSubscription(
        self,
        notificationType: str,
    ):
        """
                Returns information about subscriptions of the specified notification type. You can use this API to get subscription information when you do not have a subscription identifier.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/subscriptions/{notificationType}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetSubscriptionResponse,
            400: GetSubscriptionResponse,
            403: GetSubscriptionResponse,
            404: GetSubscriptionResponse,
            413: GetSubscriptionResponse,
            415: GetSubscriptionResponse,
            429: GetSubscriptionResponse,
            500: GetSubscriptionResponse,
            503: GetSubscriptionResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createSubscription(
        self,
        data: CreateSubscriptionRequest,
        notificationType: str,
    ):
        """
                Creates a subscription for the specified notification type to be delivered to the specified destination. Before you can subscribe, you must first create the destination by calling the createDestination operation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/subscriptions/{notificationType}"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getSubscriptionById(
        self,
        subscriptionId: str,
        notificationType: str,
    ):
        """
                Returns information about a subscription for the specified notification type. The getSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/subscriptions/{notificationType}/{subscriptionId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def deleteSubscriptionById(
        self,
        subscriptionId: str,
        notificationType: str,
    ):
        """
                Deletes the subscription indicated by the subscription identifier and notification type that you specify. The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The deleteSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/subscriptions/{notificationType}/{subscriptionId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getDestinations(
        self,
    ):
        """
                Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/destinations"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createDestination(
        self,
        data: CreateDestinationRequest,
    ):
        """
                Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/destinations"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getDestination(
        self,
        destinationId: str,
    ):
        """
                Returns information about the destination that you specify. The getDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/destinations/{destinationId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def deleteDestination(
        self,
        destinationId: str,
    ):
        """
                Deletes the destination that you specify. The deleteDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/notifications/v1/destinations/{destinationId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
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
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
