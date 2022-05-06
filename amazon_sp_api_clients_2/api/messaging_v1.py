"""
Selling Partner API for Messaging
=============================================================================================

With the Messaging API you can build applications that send messages to buyers. You can get a list of message types that are available for an order that you specify, then call an operation that sends a message to the buyer for that order. The Messaging API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Attachment:

    file_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the file, including the extension. This is the file name that will appear in the message. This does not need to match the file name of the file that you uploaded.
    """

    upload_destination_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier of the upload destination. Get this value by calling the createUploadDestination operation of the Uploads API.
    """

    pass


@attrs.define
class CreateAmazonMotorsRequest:

    attachments: list["Attachment"] = attrs.field(
        kw_only=True,
    )
    """
    Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
    """

    pass


@attrs.define
class CreateAmazonMotorsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateConfirmCustomizationDetailsRequest:

    attachments: list["Attachment"] = attrs.field(
        kw_only=True,
    )
    """
    Attachments to include in the message to the buyer.
    """

    text: str = attrs.field(
        kw_only=True,
    )
    """
    The text to be sent to the buyer. Only links related to customization details are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 800, 'minLength': 1}
    """

    pass


@attrs.define
class CreateConfirmCustomizationDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateConfirmDeliveryDetailsRequest:

    text: str = attrs.field(
        kw_only=True,
    )
    """
    The text to be sent to the buyer. Only links related to order delivery are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """

    pass


@attrs.define
class CreateConfirmDeliveryDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateConfirmOrderDetailsRequest:

    text: str = attrs.field(
        kw_only=True,
    )
    """
    The text to be sent to the buyer. Only links related to order completion are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """

    pass


@attrs.define
class CreateConfirmOrderDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateConfirmServiceDetailsRequest:

    text: str = attrs.field(
        kw_only=True,
    )
    """
    The text to be sent to the buyer. Only links related to Home Service calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """

    pass


@attrs.define
class CreateConfirmServiceDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateDigitalAccessKeyRequest:

    attachments: list["Attachment"] = attrs.field(
        kw_only=True,
    )
    """
    Attachments to include in the message to the buyer.
    """

    text: str = attrs.field(
        kw_only=True,
    )
    """
    The text to be sent to the buyer. Only links related to the digital access key are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 400, 'minLength': 1}
    """

    pass


@attrs.define
class CreateDigitalAccessKeyResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateLegalDisclosureRequest:

    attachments: list["Attachment"] = attrs.field(
        kw_only=True,
    )
    """
    Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
    """

    pass


@attrs.define
class CreateLegalDisclosureResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateNegativeFeedbackRemovalResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateUnexpectedProblemRequest:

    text: str = attrs.field(
        kw_only=True,
    )
    """
    The text to be sent to the buyer. Only links related to unexpected problem calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """

    pass


@attrs.define
class CreateUnexpectedProblemResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateWarrantyRequest:

    attachments: list["Attachment"] = attrs.field(
        kw_only=True,
    )
    """
    Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
    """

    coverage_end_date: str = attrs.field(
        kw_only=True,
    )
    """
    The end date of the warranty coverage to include in the message to the buyer.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    coverage_start_date: str = attrs.field(
        kw_only=True,
    )
    """
    The start date of the warranty coverage to include in the message to the buyer.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    pass


@attrs.define
class CreateWarrantyResponse:

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
    A message that describes the error condition.
    """

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetAttributesResponse:

    buyer: dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    The list of attributes related to the buyer.

    Extra fields:
    {'properties': {'locale': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='The buyer\'s language of preference, indicated with a locale-specific language tag. Examples: "en-US", "zh-CN", and "en-GB".', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetMessagingActionResponse:

    _embedded: dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'schema': Reference(ref='#/components/schemas/GetSchemaResponse')}}
    """

    _links: dict[str, Any] = attrs.field(
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

    payload: "MessagingAction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetMessagingActionsForOrderResponse:

    _embedded: dict[str, Any] = attrs.field(
        kw_only=True,
    )
    """
    no description.

    Extra fields:
    {'properties': {'actions': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/GetMessagingActionResponse'), properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}, 'required': ['actions']}
    """

    _links: dict[str, Any] = attrs.field(
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
class GetSchemaResponse:

    _links: dict[str, Any] = attrs.field(
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
class MessagingAction:

    name: str = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Schema:

    pass


class MessagingV1Client(BaseClient):
    def create_amazon_motors(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        attachments: list["Attachment"] = None,
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
            attachments: Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/amazonMotors"
        values = (
            amazon_order_id,
            marketplace_ids,
            attachments,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_amazon_motors_params)
        return response

    _create_amazon_motors_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
    )

    def create_warranty(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        attachments: list["Attachment"] = None,
        coverage_start_date: str = None,
        coverage_end_date: str = None,
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
            attachments: Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
            coverage_start_date: The start date of the warranty coverage to include in the message to the buyer.
            coverage_end_date: The end date of the warranty coverage to include in the message to the buyer.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/warranty"
        values = (
            amazon_order_id,
            marketplace_ids,
            attachments,
            coverage_start_date,
            coverage_end_date,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_warranty_params)
        return response

    _create_warranty_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
        ("coverageStartDate", "body"),
        ("coverageEndDate", "body"),
    )

    def get_attributes(
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
        url = "/messaging/v1/orders/{amazonOrderId}/attributes"
        values = (
            amazon_order_id,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_attributes_params)
        return response

    _get_attributes_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    def confirm_customization_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        text: str = None,
        attachments: list["Attachment"] = None,
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
            text: The text to be sent to the buyer. Only links related to customization details are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
            attachments: Attachments to include in the message to the buyer.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails"
        values = (
            amazon_order_id,
            marketplace_ids,
            text,
            attachments,
        )
        response = self._parse_args_and_request(url, "POST", values, self._confirm_customization_details_params)
        return response

    _confirm_customization_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
        ("attachments", "body"),
    )

    def create_confirm_delivery_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        text: str = None,
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
            text: The text to be sent to the buyer. Only links related to order delivery are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails"
        values = (
            amazon_order_id,
            marketplace_ids,
            text,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_confirm_delivery_details_params)
        return response

    _create_confirm_delivery_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    def create_confirm_order_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        text: str = None,
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
            text: The text to be sent to the buyer. Only links related to order completion are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails"
        values = (
            amazon_order_id,
            marketplace_ids,
            text,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_confirm_order_details_params)
        return response

    _create_confirm_order_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    def create_confirm_service_details(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        text: str = None,
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
            text: The text to be sent to the buyer. Only links related to Home Service calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails"
        values = (
            amazon_order_id,
            marketplace_ids,
            text,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_confirm_service_details_params)
        return response

    _create_confirm_service_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    def create_digital_access_key(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        text: str = None,
        attachments: list["Attachment"] = None,
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
            text: The text to be sent to the buyer. Only links related to the digital access key are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
            attachments: Attachments to include in the message to the buyer.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey"
        values = (
            amazon_order_id,
            marketplace_ids,
            text,
            attachments,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_digital_access_key_params)
        return response

    _create_digital_access_key_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
        ("attachments", "body"),
    )

    def create_legal_disclosure(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        attachments: list["Attachment"] = None,
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
            attachments: Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure"
        values = (
            amazon_order_id,
            marketplace_ids,
            attachments,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_legal_disclosure_params)
        return response

    _create_legal_disclosure_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
    )

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
        url = "/messaging/v1/orders/{amazonOrderId}/messages/negativeFeedbackRemoval"
        values = (
            amazon_order_id,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_negative_feedback_removal_params)
        return response

    _create_negative_feedback_removal_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    def create_unexpected_problem(
        self,
        amazon_order_id: str,
        marketplace_ids: list[str],
        text: str = None,
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
            text: The text to be sent to the buyer. Only links related to unexpected problem calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem"
        values = (
            amazon_order_id,
            marketplace_ids,
            text,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_unexpected_problem_params)
        return response

    _create_unexpected_problem_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

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
        url = "/messaging/v1/orders/{amazonOrderId}"
        values = (
            amazon_order_id,
            marketplace_ids,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_messaging_actions_for_order_params)
        return response

    _get_messaging_actions_for_order_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )
