"""
Selling Partner API for Messaging
=============================================================================================
With the Messaging API you can build applications that send messages to buyers. You can get a list of message types that are available for an order that you specify, then call an operation that sends a message to the buyer for that order. The Messaging API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class MessagingV1Client(BaseClient):
    def get_messaging_actions_for_order(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Returns a list of message types that are available for an order that you specify. A message type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a message.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which you want a list of available message types.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def confirm_customization_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message asking a buyer to provide or verify customization details such as name spelling, images, initials, etc.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_confirm_delivery_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message to a buyer to arrange a delivery or to confirm contact information for making a delivery.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_legal_disclosure(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a critical message that contains documents that a seller is legally obligated to provide to the buyer. This message should only be used to deliver documents that are required by law.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_negative_feedback_removal(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a non-critical message that asks a buyer to remove their negative feedback. This message should only be sent after the seller has resolved the buyer's problem.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/negativeFeedbackRemoval".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_confirm_order_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message to ask a buyer an order-related question prior to shipping their order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_confirm_service_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message to contact a Home Service customer to arrange a service call or to gather information prior to a service call.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def Create_amazon_motors(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message to a buyer to provide details about an Amazon Motors order. This message can only be sent by Amazon Motors sellers.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/amazonMotors".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def Create_warranty(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message to a buyer to provide details about warranty information on a purchase in their order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/warranty".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def Get_attributes(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Returns a response containing attributes related to an order. This includes buyer preferences.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/attributes".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_digital_access_key(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a message to a buyer to share a digital access key needed to utilize digital content in their order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids

    def create_unexpected_problem(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a critical message to a buyer that an unexpected problem was encountered affecting the completion of the order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        path_parameters = {}

        path_parameters["amazonOrderId"] = amazon_order_id

        url = "/messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceIds"] = marketplace_ids
