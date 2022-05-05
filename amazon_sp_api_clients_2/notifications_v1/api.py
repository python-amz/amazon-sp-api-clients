"""
Selling Partner API for Notifications
=============================================================================================
The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.

For more information, see the [Notifications Use Case Guide](doc:notifications-api-v1-use-case-guide)
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient


class NotificationsV1Client(BaseClient):
    def create_subscription(
        self,
        notification_type,
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
        """
        url = "/notifications/v1/subscriptions/{notificationType}"

    def get_subscription(
        self,
        notification_type,
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

    def get_subscription_by_id(
        self,
        subscription_id,
        notification_type,
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

    def delete_subscription_by_id(
        self,
        subscription_id,
        notification_type,
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

    def get_destination(
        self,
        destination_id,
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

    def delete_destination(
        self,
        destination_id,
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
