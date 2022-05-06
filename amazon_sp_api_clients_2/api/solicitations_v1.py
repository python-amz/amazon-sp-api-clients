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
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class CreateProductReviewAndSellerFeedbackSolicitationResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Error:

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition in a human-readable form.
    """

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetSchemaResponse:

    _links: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'self': Reference(ref='#/components/schemas/LinkObject')}, 'required': ['self']}
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Schema" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetSolicitationActionResponse:

    _embedded: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'schema': Reference(ref='#/components/schemas/GetSchemaResponse')}}
    """

    _links: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'self': Reference(ref='#/components/schemas/LinkObject'), 'schema': Reference(ref='#/components/schemas/LinkObject')}, 'required': ['schema', 'self']}
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "SolicitationsAction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetSolicitationActionsForOrderResponse:

    _embedded: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'actions': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/GetSolicitationActionResponse'), properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'required': ['actions']}
    """

    _links: Dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'self': Reference(ref='#/components/schemas/LinkObject'), 'actions': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/LinkObject'), properties=None, additionalProperties=None, description='Eligible actions for the specified amazonOrderId.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'required': ['actions', 'self']}
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LinkObject:

    href: str = attrs.field(
        kw_only=True,
    )
    """
    A URI for this object.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for this object.
    """

    pass


@attrs.define
class Schema:

    pass


@attrs.define
class SolicitationsAction:

    name: str = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


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
            url, "POST", values, self._create_product_review_and_seller_feedback_solicitation_params
        )
        return response

    _create_product_review_and_seller_feedback_solicitation_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

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
        response = self._parse_args_and_request(url, "GET", values, self._get_solicitation_actions_for_order_params)
        return response

    _get_solicitation_actions_for_order_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )
