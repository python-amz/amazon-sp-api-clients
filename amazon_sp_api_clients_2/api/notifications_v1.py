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

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeleteSubscriptionByIdResponse:
    """
    The response schema for the deleteSubscriptionById operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Destination:
    """
    Represents a destination created when you call the createDestination operation.
    """

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

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_destination_params = (  # name, param in
        ("name", "body"),
        ("resourceSpecification", "body"),
    )

    _create_destination_responses = {
        (200, "application/json"): CreateDestinationResponse,
        (400, "application/json"): CreateDestinationResponse,
        (403, "application/json"): CreateDestinationResponse,
        (404, "application/json"): CreateDestinationResponse,
        (409, "application/json"): CreateDestinationResponse,
        (413, "application/json"): CreateDestinationResponse,
        (415, "application/json"): CreateDestinationResponse,
        (429, "application/json"): CreateDestinationResponse,
        (500, "application/json"): CreateDestinationResponse,
        (503, "application/json"): CreateDestinationResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_subscription_params = (  # name, param in
        ("notificationType", "path"),
        ("destinationId", "body"),
        ("payloadVersion", "body"),
    )

    _create_subscription_responses = {
        (200, "application/json"): CreateSubscriptionResponse,
        (400, "application/json"): CreateSubscriptionResponse,
        (403, "application/json"): CreateSubscriptionResponse,
        (404, "application/json"): CreateSubscriptionResponse,
        (409, "application/json"): CreateSubscriptionResponse,
        (413, "application/json"): CreateSubscriptionResponse,
        (415, "application/json"): CreateSubscriptionResponse,
        (429, "application/json"): CreateSubscriptionResponse,
        (500, "application/json"): CreateSubscriptionResponse,
        (503, "application/json"): CreateSubscriptionResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _delete_destination_params = (("destinationId", "path"),)  # name, param in

    _delete_destination_responses = {
        (200, "application/json"): DeleteDestinationResponse,
        (400, "application/json"): DeleteDestinationResponse,
        (403, "application/json"): DeleteDestinationResponse,
        (404, "application/json"): DeleteDestinationResponse,
        (409, "application/json"): DeleteDestinationResponse,
        (413, "application/json"): DeleteDestinationResponse,
        (415, "application/json"): DeleteDestinationResponse,
        (429, "application/json"): DeleteDestinationResponse,
        (500, "application/json"): DeleteDestinationResponse,
        (503, "application/json"): DeleteDestinationResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _delete_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )

    _delete_subscription_by_id_responses = {
        (200, "application/json"): DeleteSubscriptionByIdResponse,
        (400, "application/json"): DeleteSubscriptionByIdResponse,
        (403, "application/json"): DeleteSubscriptionByIdResponse,
        (404, "application/json"): DeleteSubscriptionByIdResponse,
        (409, "application/json"): DeleteSubscriptionByIdResponse,
        (413, "application/json"): DeleteSubscriptionByIdResponse,
        (415, "application/json"): DeleteSubscriptionByIdResponse,
        (429, "application/json"): DeleteSubscriptionByIdResponse,
        (500, "application/json"): DeleteSubscriptionByIdResponse,
        (503, "application/json"): DeleteSubscriptionByIdResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_destination_params = (("destinationId", "path"),)  # name, param in

    _get_destination_responses = {
        (200, "application/json"): GetDestinationResponse,
        (400, "application/json"): GetDestinationResponse,
        (403, "application/json"): GetDestinationResponse,
        (404, "application/json"): GetDestinationResponse,
        (409, "application/json"): GetDestinationResponse,
        (413, "application/json"): GetDestinationResponse,
        (415, "application/json"): GetDestinationResponse,
        (429, "application/json"): GetDestinationResponse,
        (500, "application/json"): GetDestinationResponse,
        (503, "application/json"): GetDestinationResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_destinations_params = ()  # name, param in

    _get_destinations_responses = {
        (200, "application/json"): GetDestinationsResponse,
        (400, "application/json"): GetDestinationsResponse,
        (403, "application/json"): GetDestinationsResponse,
        (404, "application/json"): GetDestinationsResponse,
        (409, "application/json"): GetDestinationsResponse,
        (413, "application/json"): GetDestinationsResponse,
        (415, "application/json"): GetDestinationsResponse,
        (429, "application/json"): GetDestinationsResponse,
        (500, "application/json"): GetDestinationsResponse,
        (503, "application/json"): GetDestinationsResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_subscription_params = (("notificationType", "path"),)  # name, param in

    _get_subscription_responses = {
        (200, "application/json"): GetSubscriptionResponse,
        (400, "application/json"): GetSubscriptionResponse,
        (403, "application/json"): GetSubscriptionResponse,
        (404, "application/json"): GetSubscriptionResponse,
        (413, "application/json"): GetSubscriptionResponse,
        (415, "application/json"): GetSubscriptionResponse,
        (429, "application/json"): GetSubscriptionResponse,
        (500, "application/json"): GetSubscriptionResponse,
        (503, "application/json"): GetSubscriptionResponse,
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )

    _get_subscription_by_id_responses = {
        (200, "application/json"): GetSubscriptionByIdResponse,
        (400, "application/json"): GetSubscriptionByIdResponse,
        (403, "application/json"): GetSubscriptionByIdResponse,
        (404, "application/json"): GetSubscriptionResponse,
        (409, "application/json"): GetSubscriptionByIdResponse,
        (413, "application/json"): GetSubscriptionByIdResponse,
        (415, "application/json"): GetSubscriptionByIdResponse,
        (429, "application/json"): GetSubscriptionByIdResponse,
        (500, "application/json"): GetSubscriptionByIdResponse,
        (503, "application/json"): GetSubscriptionByIdResponse,
    }
