"""
Selling Partner API for Solicitations
=============================================================================================

With the Solicitations API you can build applications that send non-critical solicitations to buyers. You can get a list of solicitation types that are available for an order that you specify, then call an operation that sends a solicitation to the buyer for that order. Buyers cannot respond to solicitations sent by this API, and these solicitations do not appear in the Messaging section of Seller Central or in the recipient's Message Center. The Solicitations API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateProductReviewAndSellerFeedbackSolicitationResponse:
    """
    The response schema for the createProductReviewAndSellerFeedbackSolicitation operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
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
class GetSchemaResponse:

    _links: Optional["GetSchemaResponseLinks"] = attrs.field()

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Schema"] = attrs.field()
    """
    A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSchemaResponseLinks:

    self: "LinkObject" = attrs.field()
    """
    A Link object.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSolicitationActionResponse:
    """
    Describes a solicitation action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
    """

    _embedded: Optional["GetSolicitationActionResponseEmbedded"] = attrs.field()

    _links: Optional["GetSolicitationActionResponseLinks"] = attrs.field()

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["SolicitationsAction"] = attrs.field()
    """
    A simple object containing the name of the template.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSolicitationActionResponseEmbedded:

    schema: Optional["GetSchemaResponse"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSolicitationActionResponseLinks:

    schema: "LinkObject" = attrs.field()
    """
    A Link object.
    """

    self: "LinkObject" = attrs.field()
    """
    A Link object.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSolicitationActionsForOrderResponse:
    """
    The response schema for the getSolicitationActionsForOrder operation.
    """

    _embedded: Optional["GetSolicitationActionsForOrderResponseEmbedded"] = attrs.field()

    _links: Optional["GetSolicitationActionsForOrderResponseLinks"] = attrs.field()

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSolicitationActionsForOrderResponseEmbedded:

    actions: List["GetSolicitationActionResponse"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetSolicitationActionsForOrderResponseLinks:

    actions: List["LinkObject"] = attrs.field()
    """
    Eligible actions for the specified amazonOrderId.
    """

    self: "LinkObject" = attrs.field()
    """
    A Link object.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LinkObject:
    """
    A Link object.
    """

    href: str = attrs.field()
    """
    A URI for this object.
    """

    name: Optional[str] = attrs.field()
    """
    An identifier for this object.
    """


@attrs.define(kw_only=True, frozen=True, slots=False)
class Schema:
    """
    A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SolicitationsAction:
    """
    A simple object containing the name of the template.
    """

    name: str = attrs.field()


class SolicitationsV1Client(BaseClient):
    def create_product_review_and_seller_feedback_solicitation(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_product_review_and_seller_feedback_solicitation_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_product_review_and_seller_feedback_solicitation_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    _create_product_review_and_seller_feedback_solicitation_responses = {
        (201, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (400, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (403, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (404, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (413, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (415, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (429, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (500, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
        (503, "application/hal+json"): CreateProductReviewAndSellerFeedbackSolicitationResponse,
    }

    def get_solicitation_actions_for_order(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_solicitation_actions_for_order_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_solicitation_actions_for_order_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    _get_solicitation_actions_for_order_responses = {
        (200, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (400, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (403, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (404, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (413, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (415, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (429, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (500, "application/hal+json"): GetSolicitationActionsForOrderResponse,
        (503, "application/hal+json"): GetSolicitationActionsForOrderResponse,
    }
