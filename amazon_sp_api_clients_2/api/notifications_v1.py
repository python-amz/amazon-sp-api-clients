"""
Selling Partner API for Notifications
=============================================================================================

The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.

For more information, see the [Notifications Use Case Guide](doc:notifications-api-v1-use-case-guide)
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateDestinationRequest:
    """
    The request schema for the createDestination operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_destination_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateDestinationRequest(**data)

    name: str = attrs.field()
    """
    A developer-defined name to help identify this destination.
    """

    resource_specification: "DestinationResourceSpecification" = attrs.field()
    """
    The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateDestinationResponse:
    """
    The response schema for the createDestination operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_destination_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateDestinationResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Destination"] = attrs.field()
    """
    Represents a destination created when you call the createDestination operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateSubscriptionRequest:
    """
    The request schema for the createSubscription operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_subscription_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateSubscriptionRequest(**data)

    destination_id: Optional[str] = attrs.field()
    """
    The identifier for the destination where notifications will be delivered.
    """

    payload_version: Optional[str] = attrs.field()
    """
    The version of the payload object to be used in the notification.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateSubscriptionResponse:
    """
    The response schema for the createSubscription operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_subscription_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateSubscriptionResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Subscription"] = attrs.field()
    """
    Represents a subscription to receive notifications.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeleteDestinationResponse:
    """
    The response schema for the deleteDestination operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _delete_destination_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DeleteDestinationResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeleteSubscriptionByIdResponse:
    """
    The response schema for the deleteSubscriptionById operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _delete_subscription_by_id_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DeleteSubscriptionByIdResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Destination:
    """
    Represents a destination created when you call the createDestination operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _destination_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Destination(**data)

    destination_id: str = attrs.field()
    """
    The destination identifier generated when you created the destination.
    """

    name: str = attrs.field()
    """
    The developer-defined name for this destination.

    Extra fields:
    {'maxLength': 256}
    """

    resource: "DestinationResource" = attrs.field()
    """
    The destination resource types.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DestinationResource:
    """
    The destination resource types.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _destination_resource_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DestinationResource(**data)

    event_bridge: Optional["EventBridgeResource"] = attrs.field()
    """
    Represents an Amazon EventBridge destination.
    """

    sqs: Optional["SqsResource"] = attrs.field()
    """
    The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DestinationResourceSpecification:
    """
    The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _destination_resource_specification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DestinationResourceSpecification(**data)

    event_bridge: Optional["EventBridgeResourceSpecification"] = attrs.field()
    """
    The information required to create an Amazon EventBridge destination.
    """

    sqs: Optional["SqsResource"] = attrs.field()
    """
    The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class EventBridgeResource:
    """
    Represents an Amazon EventBridge destination.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _event_bridge_resource_name_convert
        data = {name_convert[k]: v for k, v in data}
        return EventBridgeResource(**data)

    account_id: str = attrs.field()
    """
    The identifier for the AWS account that is responsible for charges related to receiving notifications.
    """

    name: str = attrs.field()
    """
    The name of the partner event source associated with the destination.

    Extra fields:
    {'maxLength': 256}
    """

    region: str = attrs.field()
    """
    The AWS region in which you receive the notifications. For AWS regions that are supported in Amazon EventBridge, see https://docs.aws.amazon.com/general/latest/gr/ev.html.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class EventBridgeResourceSpecification:
    """
    The information required to create an Amazon EventBridge destination.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _event_bridge_resource_specification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return EventBridgeResourceSpecification(**data)

    account_id: str = attrs.field()
    """
    The identifier for the AWS account that is responsible for charges related to receiving notifications.
    """

    region: str = attrs.field()
    """
    The AWS region in which you will be receiving the notifications.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetDestinationResponse:
    """
    The response schema for the getDestination operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_destination_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetDestinationResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Destination"] = attrs.field()
    """
    Represents a destination created when you call the createDestination operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetDestinationsResponse:
    """
    The response schema for the getDestinations operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_destinations_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetDestinationsResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional[List["Destination"]] = attrs.field()
    """
    A list of destinations.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSubscriptionByIdResponse:
    """
    The response schema for the getSubscriptionById operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_subscription_by_id_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetSubscriptionByIdResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Subscription"] = attrs.field()
    """
    Represents a subscription to receive notifications.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSubscriptionResponse:
    """
    The response schema for the getSubscription operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_subscription_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetSubscriptionResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Subscription"] = attrs.field()
    """
    Represents a subscription to receive notifications.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SqsResource:
    """
    The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _sqs_resource_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SqsResource(**data)

    arn: str = attrs.field()
    """
    The Amazon Resource Name (ARN) associated with the SQS queue.

    Extra fields:
    {'maxLength': 1000, 'pattern': '^arn:aws:sqs:\\S+:\\S+:\\S+'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Subscription:
    """
    Represents a subscription to receive notifications.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _subscription_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Subscription(**data)

    destination_id: str = attrs.field()
    """
    The identifier for the destination where notifications will be delivered.
    """

    payload_version: str = attrs.field()
    """
    The version of the payload object to be used in the notification.
    """

    subscription_id: str = attrs.field()
    """
    The subscription identifier generated when the subscription is created.
    """


_create_destination_request_name_convert = {
    "name": "name",
    "resourceSpecification": "resource_specification",
}

_create_destination_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_create_subscription_request_name_convert = {
    "destinationId": "destination_id",
    "payloadVersion": "payload_version",
}

_create_subscription_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_delete_destination_response_name_convert = {
    "errors": "errors",
}

_delete_subscription_by_id_response_name_convert = {
    "errors": "errors",
}

_destination_name_convert = {
    "destinationId": "destination_id",
    "name": "name",
    "resource": "resource",
}

_destination_resource_name_convert = {
    "eventBridge": "event_bridge",
    "sqs": "sqs",
}

_destination_resource_specification_name_convert = {
    "eventBridge": "event_bridge",
    "sqs": "sqs",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_event_bridge_resource_name_convert = {
    "accountId": "account_id",
    "name": "name",
    "region": "region",
}

_event_bridge_resource_specification_name_convert = {
    "accountId": "account_id",
    "region": "region",
}

_get_destination_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_destinations_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_subscription_by_id_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_subscription_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_sqs_resource_name_convert = {
    "arn": "arn",
}

_subscription_name_convert = {
    "destinationId": "destination_id",
    "payloadVersion": "payload_version",
    "subscriptionId": "subscription_id",
}


class NotificationsV1Client(BaseClient):
    def create_destination(
        self,
        name: str,
        resource_specification: Dict[str, Any],
    ) -> Union[CreateDestinationResponse]:
        """
        Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            name: A developer-defined name to help identify this destination.
            resource_specification: The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
        """
        url = "/notifications/v1/destinations"
        values = (
            name,
            resource_specification,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_destination_params,
            self._create_destination_responses,
        )
        return response

    _create_destination_params = (  # name, param in
        ("name", "body"),
        ("resourceSpecification", "body"),
    )

    _create_destination_responses = {
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
    }

    def create_subscription(
        self,
        notification_type: str,
        destination_id: str = None,
        payload_version: str = None,
    ) -> Union[CreateSubscriptionResponse]:
        """
        Creates a subscription for the specified notification type to be delivered to the specified destination. Before you can subscribe, you must first create the destination by calling the createDestination operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
            destination_id: The identifier for the destination where notifications will be delivered.
            payload_version: The version of the payload object to be used in the notification.
        """
        url = "/notifications/v1/subscriptions/{notificationType}"
        values = (
            notification_type,
            destination_id,
            payload_version,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_subscription_params,
            self._create_subscription_responses,
        )
        return response

    _create_subscription_params = (  # name, param in
        ("notificationType", "path"),
        ("destinationId", "body"),
        ("payloadVersion", "body"),
    )

    _create_subscription_responses = {
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
    }

    def delete_destination(
        self,
        destination_id: str,
    ) -> Union[DeleteDestinationResponse]:
        """
        Deletes the destination that you specify. The deleteDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            destination_id: The identifier for the destination that you want to delete.
        """
        url = "/notifications/v1/destinations/{destinationId}"
        values = (destination_id,)
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._delete_destination_params,
            self._delete_destination_responses,
        )
        return response

    _delete_destination_params = (("destinationId", "path"),)  # name, param in

    _delete_destination_responses = {
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
    }

    def delete_subscription_by_id(
        self,
        subscription_id: str,
        notification_type: str,
    ) -> Union[DeleteSubscriptionByIdResponse]:
        """
        Deletes the subscription indicated by the subscription identifier and notification type that you specify. The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The deleteSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            subscription_id: The identifier for the subscription that you want to delete.
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/notifications/v1/subscriptions/{notificationType}/{subscriptionId}"
        values = (
            subscription_id,
            notification_type,
        )
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._delete_subscription_by_id_params,
            self._delete_subscription_by_id_responses,
        )
        return response

    _delete_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )

    _delete_subscription_by_id_responses = {
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
    }

    def get_destination(
        self,
        destination_id: str,
    ) -> Union[GetDestinationResponse]:
        """
        Returns information about the destination that you specify. The getDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            destination_id: The identifier generated when you created the destination.
        """
        url = "/notifications/v1/destinations/{destinationId}"
        values = (destination_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_destination_params,
            self._get_destination_responses,
        )
        return response

    _get_destination_params = (("destinationId", "path"),)  # name, param in

    _get_destination_responses = {
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
    }

    def get_destinations(
        self,
    ) -> Union[GetDestinationsResponse]:
        """
        Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/notifications/v1/destinations"
        values = ()
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_destinations_params,
            self._get_destinations_responses,
        )
        return response

    _get_destinations_params = ()  # name, param in

    _get_destinations_responses = {
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
    }

    def get_subscription(
        self,
        notification_type: str,
    ) -> Union[GetSubscriptionResponse]:
        """
        Returns information about subscriptions of the specified notification type. You can use this API to get subscription information when you do not have a subscription identifier.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/notifications/v1/subscriptions/{notificationType}"
        values = (notification_type,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_subscription_params,
            self._get_subscription_responses,
        )
        return response

    _get_subscription_params = (("notificationType", "path"),)  # name, param in

    _get_subscription_responses = {
        200: GetSubscriptionResponse,
        400: GetSubscriptionResponse,
        403: GetSubscriptionResponse,
        404: GetSubscriptionResponse,
        413: GetSubscriptionResponse,
        415: GetSubscriptionResponse,
        429: GetSubscriptionResponse,
        500: GetSubscriptionResponse,
        503: GetSubscriptionResponse,
    }

    def get_subscription_by_id(
        self,
        subscription_id: str,
        notification_type: str,
    ) -> Union[GetSubscriptionByIdResponse, GetSubscriptionResponse]:
        """
        Returns information about a subscription for the specified notification type. The getSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            subscription_id: The identifier for the subscription that you want to get.
            notification_type: The type of notification.
                For more information about notification types, see [the Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/notifications/v1/subscriptions/{notificationType}/{subscriptionId}"
        values = (
            subscription_id,
            notification_type,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_subscription_by_id_params,
            self._get_subscription_by_id_responses,
        )
        return response

    _get_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )

    _get_subscription_by_id_responses = {
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
    }
