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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class CreateDestinationRequest:

    name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}

    resource_specification: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/DestinationResourceSpecification'}
    pass


@attrs.define
class CreateDestinationResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/Destination'}
    pass


@attrs.define
class CreateSubscriptionRequest:

    destination_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    payload_version: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}

    pass


@attrs.define
class CreateSubscriptionResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/Subscription'}
    pass


@attrs.define
class DeleteDestinationResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class DeleteSubscriptionByIdResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class Destination:

    destination_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'maxLength': 256}

    resource: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/DestinationResource'}
    pass


@attrs.define
class DestinationList:

    pass


@attrs.define
class DestinationResource:

    event_bridge: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/EventBridgeResource'}
    sqs: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/SqsResource'}
    pass


@attrs.define
class DestinationResourceSpecification:

    event_bridge: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/EventBridgeResourceSpecification'}
    sqs: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/SqsResource'}
    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class EventBridgeResource:

    account_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'maxLength': 256}
    region: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}

    pass


@attrs.define
class EventBridgeResourceSpecification:

    account_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    region: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}

    pass


@attrs.define
class GetDestinationResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/Destination'}
    pass


@attrs.define
class GetDestinationsResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/DestinationList'}
    pass


@attrs.define
class GetSubscriptionByIdResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/Subscription'}
    pass


@attrs.define
class GetSubscriptionResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'ref': '#/components/schemas/Subscription'}
    pass


@attrs.define
class SqsResource:

    arn: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>, 'maxLength': 1000, 'pattern': '^arn:aws:sqs:\\S+:\\S+:\\S+'}

    pass


@attrs.define
class Subscription:

    destination_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    payload_version: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}
    subscription_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001B93797B700>}

    pass


class NotificationsV1Client(BaseClient):
    def create_destination(
        self,
    ):
        """
        Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/notifications/v1/destinations"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_destination_params)
        return response

    _create_destination_params = ()  # name, param in

    def create_subscription(
        self,
        notification_type: str,
        payload_version: str = None,
        destination_id: str = None,
    ):
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
            payload_version: The version of the payload object to be used in the notification.
            destination_id: The identifier for the destination where notifications will be delivered.
        """
        url = "/notifications/v1/subscriptions/{notificationType}"
        values = (
            notification_type,
            payload_version,
            destination_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_subscription_params)
        return response

    _create_subscription_params = (  # name, param in
        ("notificationType", "path"),
        ("payloadVersion", "body"),
        ("destinationId", "body"),
    )

    def delete_destination(
        self,
        destination_id: str,
    ):
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
        response = self._parse_args_and_request(url, "DELETE", values, self._delete_destination_params)
        return response

    _delete_destination_params = (("destinationId", "path"),)  # name, param in

    def delete_subscription_by_id(
        self,
        subscription_id: str,
        notification_type: str,
    ):
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
        response = self._parse_args_and_request(url, "DELETE", values, self._delete_subscription_by_id_params)
        return response

    _delete_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )

    def get_destination(
        self,
        destination_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_destination_params)
        return response

    _get_destination_params = (("destinationId", "path"),)  # name, param in

    def get_destinations(
        self,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_destinations_params)
        return response

    _get_destinations_params = ()  # name, param in

    def get_subscription(
        self,
        notification_type: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_subscription_params)
        return response

    _get_subscription_params = (("notificationType", "path"),)  # name, param in

    def get_subscription_by_id(
        self,
        subscription_id: str,
        notification_type: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_subscription_by_id_params)
        return response

    _get_subscription_by_id_params = (  # name, param in
        ("subscriptionId", "path"),
        ("notificationType", "path"),
    )
