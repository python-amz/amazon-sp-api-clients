"""
Selling Partner API for Solicitations
=============================================================================================
With the Solicitations API you can build applications that send non-critical solicitations to buyers. You can get a list of solicitation types that are available for an order that you specify, then call an operation that sends a solicitation to the buyer for that order. Buyers cannot respond to solicitations sent by this API, and these solicitations do not appear in the Messaging section of Seller Central or in the recipient's Message Center. The Solicitations API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class SolicitationsV1Client(BaseClient):
    def create_product_review_and_seller_feedback_solicitation(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Sends a solicitation to a buyer asking for seller feedback and a product review for the specified order. Send only one productReviewAndSellerFeedback or free form proactive message per order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which a solicitation is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        url = "/solicitations/v1/orders/{amazonOrderId}/solicitations/productReviewAndSellerFeedback"
        values = (
            amazon_order_id,
            marketplace_ids,
        )

    _create_product_review_and_seller_feedback_solicitation_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    def get_solicitation_actions_for_order(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
    ):
        """
        Returns a list of solicitation types that are available for an order that you specify. A solicitation type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a solicitation. Currently only the productReviewAndSellerFeedbackSolicitation solicitation type is available.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            amazon_order_id: An Amazon order identifier. This specifies the order for which you want a list of available solicitation types.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.
        """
        url = "/solicitations/v1/orders/{amazonOrderId}"
        values = (
            amazon_order_id,
            marketplace_ids,
        )

    _get_solicitation_actions_for_order_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )
