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


@attrs.define
class CreateProductReviewAndSellerFeedbackSolicitationResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetSchemaResponse:

    _links: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'required': ['self'], 'properties': {'self': Reference(ref='#/components/schemas/LinkObject')}, 'type': 'object'}

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'ref': '#/components/schemas/Schema'}
    pass


@attrs.define
class GetSolicitationActionResponse:

    _embedded: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'properties': {'schema': Reference(ref='#/components/schemas/GetSchemaResponse')}, 'type': 'object'}
    _links: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'required': ['schema', 'self'], 'properties': {'self': Reference(ref='#/components/schemas/LinkObject'), 'schema': Reference(ref='#/components/schemas/LinkObject')}, 'type': 'object'}

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'ref': '#/components/schemas/SolicitationsAction'}
    pass


@attrs.define
class GetSolicitationActionsForOrderResponse:

    _embedded: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'required': ['actions'], 'properties': {'actions': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/GetSolicitationActionResponse'), properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'type': 'object'}
    _links: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'required': ['actions', 'self'], 'properties': {'self': Reference(ref='#/components/schemas/LinkObject'), 'actions': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/LinkObject'), properties=None, additionalProperties=None, description='Eligible actions for the specified amazonOrderId.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'type': 'object'}

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class LinkObject:

    href: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'type': 'string'}

    pass


@attrs.define
class Schema:

    pass


@attrs.define
class SolicitationsAction:

    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D732A2F20>, 'type': 'string'}

    pass


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
        response = self._parse_args_and_request(url, "GET", values, self._get_solicitation_actions_for_order_params)
        return response

    _get_solicitation_actions_for_order_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )
