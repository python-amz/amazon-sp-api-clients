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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Attachment:
    """
    Represents a file uploaded to a destination that was created by the createUploadDestination operation of the Uploads API.
    """

    file_name: str = attrs.field()
    """
    The name of the file, including the extension. This is the file name that will appear in the message. This does not need to match the file name of the file that you uploaded.
    """

    upload_destination_id: str = attrs.field()
    """
    The identifier of the upload destination. Get this value by calling the createUploadDestination operation of the Uploads API.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateAmazonMotorsRequest:
    """
    The request schema for the createAmazonMotors operation.
    """

    attachments: Optional[List["Attachment"]] = attrs.field()
    """
    Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateAmazonMotorsResponse:
    """
    The response schema for the createAmazonMotors operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmCustomizationDetailsRequest:
    """
    The request schema for the confirmCustomizationDetails operation.
    """

    attachments: Optional[List["Attachment"]] = attrs.field()
    """
    Attachments to include in the message to the buyer.
    """

    text: Optional[str] = attrs.field()
    """
    The text to be sent to the buyer. Only links related to customization details are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 800, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmCustomizationDetailsResponse:
    """
    The response schema for the confirmCustomizationDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmDeliveryDetailsRequest:
    """
    The request schema for the createConfirmDeliveryDetails operation.
    """

    text: Optional[str] = attrs.field()
    """
    The text to be sent to the buyer. Only links related to order delivery are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmDeliveryDetailsResponse:
    """
    The response schema for the createConfirmDeliveryDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmOrderDetailsRequest:
    """
    The request schema for the createConfirmOrderDetails operation.
    """

    text: Optional[str] = attrs.field()
    """
    The text to be sent to the buyer. Only links related to order completion are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmOrderDetailsResponse:
    """
    The response schema for the createConfirmOrderDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmServiceDetailsRequest:
    """
    The request schema for the createConfirmServiceDetails operation.
    """

    text: Optional[str] = attrs.field()
    """
    The text to be sent to the buyer. Only links related to Home Service calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateConfirmServiceDetailsResponse:
    """
    The response schema for the createConfirmServiceDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateDigitalAccessKeyRequest:
    """
    The request schema for the createDigitalAccessKey operation.
    """

    attachments: Optional[List["Attachment"]] = attrs.field()
    """
    Attachments to include in the message to the buyer.
    """

    text: Optional[str] = attrs.field()
    """
    The text to be sent to the buyer. Only links related to the digital access key are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 400, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateDigitalAccessKeyResponse:
    """
    The response schema for the createDigitalAccessKey operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateLegalDisclosureRequest:
    """
    The request schema for the createLegalDisclosure operation.
    """

    attachments: Optional[List["Attachment"]] = attrs.field()
    """
    Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateLegalDisclosureResponse:
    """
    The response schema for the createLegalDisclosure operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateNegativeFeedbackRemovalResponse:
    """
    The response schema for the createNegativeFeedbackRemoval operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateUnexpectedProblemRequest:
    """
    The request schema for the createUnexpectedProblem operation.
    """

    text: Optional[str] = attrs.field()
    """
    The text to be sent to the buyer. Only links related to unexpected problem calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.

    Extra fields:
    {'maxLength': 2000, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateUnexpectedProblemResponse:
    """
    The response schema for the createUnexpectedProblem operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateWarrantyRequest:
    """
    The request schema for the createWarranty operation.
    """

    attachments: Optional[List["Attachment"]] = attrs.field()
    """
    Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
    """

    coverage_end_date: Optional[datetime] = attrs.field()
    """
    The end date of the warranty coverage to include in the message to the buyer.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    coverage_start_date: Optional[datetime] = attrs.field()
    """
    The start date of the warranty coverage to include in the message to the buyer.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateWarrantyResponse:
    """
    The response schema for the createWarranty operation.
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
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAttributesResponse:
    """
    The response schema for the GetAttributes operation.
    """

    buyer: Optional["GetAttributesResponseBuyer"] = attrs.field()
    """
    The list of attributes related to the buyer.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAttributesResponseBuyer:
    """
    The list of attributes related to the buyer.
    """

    locale: Optional[str] = attrs.field()
    """
    The buyer's language of preference, indicated with a locale-specific language tag. Examples: "en-US", "zh-CN", and "en-GB".
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMessagingActionResponse:
    """
    Describes a messaging action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
    """

    _embedded: Optional["GetMessagingActionResponseEmbedded"] = attrs.field()

    _links: Optional["GetMessagingActionResponseLinks"] = attrs.field()

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["MessagingAction"] = attrs.field()
    """
    A simple object containing the name of the template.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMessagingActionResponseEmbedded:

    schema: Optional["GetSchemaResponse"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMessagingActionResponseLinks:

    schema: "LinkObject" = attrs.field()
    """
    A Link object.
    """

    self: "LinkObject" = attrs.field()
    """
    A Link object.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMessagingActionsForOrderResponse:
    """
    The response schema for the getMessagingActionsForOrder operation.
    """

    _embedded: Optional["GetMessagingActionsForOrderResponseEmbedded"] = attrs.field()

    _links: Optional["GetMessagingActionsForOrderResponseLinks"] = attrs.field()

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMessagingActionsForOrderResponseEmbedded:

    actions: List["GetMessagingActionResponse"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMessagingActionsForOrderResponseLinks:

    actions: List["LinkObject"] = attrs.field()
    """
    Eligible actions for the specified amazonOrderId.
    """

    self: "LinkObject" = attrs.field()
    """
    A Link object.
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


@attrs.define(kw_only=True, frozen=True, slots=True)
class MessagingAction:
    """
    A simple object containing the name of the template.
    """

    name: str = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Schema:
    """
    A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
    """

    pass


class MessagingV1Client(BaseClient):
    def create_amazon_motors(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
        attachments: List["Attachment"] = None,
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_amazon_motors_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_amazon_motors_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
    )

    _create_amazon_motors_responses = {
        201: CreateAmazonMotorsResponse,
        400: CreateAmazonMotorsResponse,
        403: CreateAmazonMotorsResponse,
        404: CreateAmazonMotorsResponse,
        413: CreateAmazonMotorsResponse,
        415: CreateAmazonMotorsResponse,
        429: CreateAmazonMotorsResponse,
        500: CreateAmazonMotorsResponse,
        503: CreateAmazonMotorsResponse,
    }

    def create_warranty(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
        attachments: List["Attachment"] = None,
        coverage_end_date: datetime = None,
        coverage_start_date: datetime = None,
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
            coverage_end_date: The end date of the warranty coverage to include in the message to the buyer.
            coverage_start_date: The start date of the warranty coverage to include in the message to the buyer.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/warranty"
        values = (
            amazon_order_id,
            marketplace_ids,
            attachments,
            coverage_end_date,
            coverage_start_date,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_warranty_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_warranty_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
        ("coverageEndDate", "body"),
        ("coverageStartDate", "body"),
    )

    _create_warranty_responses = {
        201: CreateWarrantyResponse,
        400: CreateWarrantyResponse,
        403: CreateWarrantyResponse,
        404: CreateWarrantyResponse,
        413: CreateWarrantyResponse,
        415: CreateWarrantyResponse,
        429: CreateWarrantyResponse,
        500: CreateWarrantyResponse,
        503: CreateWarrantyResponse,
    }

    def get_attributes(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_attributes_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_attributes_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    _get_attributes_responses = {
        200: GetAttributesResponse,
        400: GetAttributesResponse,
        403: GetAttributesResponse,
        404: GetAttributesResponse,
        413: GetAttributesResponse,
        415: GetAttributesResponse,
        429: GetAttributesResponse,
        500: GetAttributesResponse,
        503: GetAttributesResponse,
    }

    def confirm_customization_details(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
        attachments: List["Attachment"] = None,
        text: str = None,
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
            attachments: Attachments to include in the message to the buyer.
            text: The text to be sent to the buyer. Only links related to customization details are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails"
        values = (
            amazon_order_id,
            marketplace_ids,
            attachments,
            text,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._confirm_customization_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _confirm_customization_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
        ("text", "body"),
    )

    _confirm_customization_details_responses = {
        201: CreateConfirmCustomizationDetailsResponse,
        400: CreateConfirmCustomizationDetailsResponse,
        403: CreateConfirmCustomizationDetailsResponse,
        404: CreateConfirmCustomizationDetailsResponse,
        413: CreateConfirmCustomizationDetailsResponse,
        415: CreateConfirmCustomizationDetailsResponse,
        429: CreateConfirmCustomizationDetailsResponse,
        500: CreateConfirmCustomizationDetailsResponse,
        503: CreateConfirmCustomizationDetailsResponse,
    }

    def create_confirm_delivery_details(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_confirm_delivery_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_confirm_delivery_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    _create_confirm_delivery_details_responses = {
        201: CreateConfirmDeliveryDetailsResponse,
        400: CreateConfirmDeliveryDetailsResponse,
        403: CreateConfirmDeliveryDetailsResponse,
        404: CreateConfirmDeliveryDetailsResponse,
        413: CreateConfirmDeliveryDetailsResponse,
        415: CreateConfirmDeliveryDetailsResponse,
        429: CreateConfirmDeliveryDetailsResponse,
        500: CreateConfirmDeliveryDetailsResponse,
        503: CreateConfirmDeliveryDetailsResponse,
    }

    def create_confirm_order_details(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_confirm_order_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_confirm_order_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    _create_confirm_order_details_responses = {
        201: CreateConfirmOrderDetailsResponse,
        400: CreateConfirmOrderDetailsResponse,
        403: CreateConfirmOrderDetailsResponse,
        404: CreateConfirmOrderDetailsResponse,
        413: CreateConfirmOrderDetailsResponse,
        415: CreateConfirmOrderDetailsResponse,
        429: CreateConfirmOrderDetailsResponse,
        500: CreateConfirmOrderDetailsResponse,
        503: CreateConfirmOrderDetailsResponse,
    }

    def create_confirm_service_details(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_confirm_service_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_confirm_service_details_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    _create_confirm_service_details_responses = {
        201: CreateConfirmServiceDetailsResponse,
        400: CreateConfirmServiceDetailsResponse,
        403: CreateConfirmServiceDetailsResponse,
        404: CreateConfirmServiceDetailsResponse,
        413: CreateConfirmServiceDetailsResponse,
        415: CreateConfirmServiceDetailsResponse,
        429: CreateConfirmServiceDetailsResponse,
        500: CreateConfirmServiceDetailsResponse,
        503: CreateConfirmServiceDetailsResponse,
    }

    def create_digital_access_key(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
        attachments: List["Attachment"] = None,
        text: str = None,
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
            attachments: Attachments to include in the message to the buyer.
            text: The text to be sent to the buyer. Only links related to the digital access key are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.
        """
        url = "/messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey"
        values = (
            amazon_order_id,
            marketplace_ids,
            attachments,
            text,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_digital_access_key_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_digital_access_key_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
        ("text", "body"),
    )

    _create_digital_access_key_responses = {
        201: CreateDigitalAccessKeyResponse,
        400: CreateDigitalAccessKeyResponse,
        403: CreateDigitalAccessKeyResponse,
        404: CreateDigitalAccessKeyResponse,
        413: CreateDigitalAccessKeyResponse,
        415: CreateDigitalAccessKeyResponse,
        429: CreateDigitalAccessKeyResponse,
        500: CreateDigitalAccessKeyResponse,
        503: CreateDigitalAccessKeyResponse,
    }

    def create_legal_disclosure(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
        attachments: List["Attachment"] = None,
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_legal_disclosure_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_legal_disclosure_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("attachments", "body"),
    )

    _create_legal_disclosure_responses = {
        201: CreateLegalDisclosureResponse,
        400: CreateLegalDisclosureResponse,
        403: CreateLegalDisclosureResponse,
        404: CreateLegalDisclosureResponse,
        413: CreateLegalDisclosureResponse,
        415: CreateLegalDisclosureResponse,
        429: CreateLegalDisclosureResponse,
        500: CreateLegalDisclosureResponse,
        503: CreateLegalDisclosureResponse,
    }

    def create_negative_feedback_removal(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_negative_feedback_removal_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_negative_feedback_removal_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    _create_negative_feedback_removal_responses = {
        201: CreateNegativeFeedbackRemovalResponse,
        400: CreateNegativeFeedbackRemovalResponse,
        403: CreateNegativeFeedbackRemovalResponse,
        404: CreateNegativeFeedbackRemovalResponse,
        413: CreateNegativeFeedbackRemovalResponse,
        415: CreateNegativeFeedbackRemovalResponse,
        429: CreateNegativeFeedbackRemovalResponse,
        500: CreateNegativeFeedbackRemovalResponse,
        503: CreateNegativeFeedbackRemovalResponse,
    }

    def create_unexpected_problem(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_unexpected_problem_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_unexpected_problem_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
        ("text", "body"),
    )

    _create_unexpected_problem_responses = {
        201: CreateUnexpectedProblemResponse,
        400: CreateUnexpectedProblemResponse,
        403: CreateUnexpectedProblemResponse,
        404: CreateUnexpectedProblemResponse,
        413: CreateUnexpectedProblemResponse,
        415: CreateUnexpectedProblemResponse,
        429: CreateUnexpectedProblemResponse,
        500: CreateUnexpectedProblemResponse,
        503: CreateUnexpectedProblemResponse,
    }

    def get_messaging_actions_for_order(
        self,
        amazon_order_id: str,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_messaging_actions_for_order_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_messaging_actions_for_order_params = (  # name, param in
        ("amazonOrderId", "path"),
        ("marketplaceIds", "query"),
    )

    _get_messaging_actions_for_order_responses = {
        200: GetMessagingActionsForOrderResponse,
        400: GetMessagingActionsForOrderResponse,
        403: GetMessagingActionsForOrderResponse,
        404: GetMessagingActionsForOrderResponse,
        413: GetMessagingActionsForOrderResponse,
        415: GetMessagingActionsForOrderResponse,
        429: GetMessagingActionsForOrderResponse,
        500: GetMessagingActionsForOrderResponse,
        503: GetMessagingActionsForOrderResponse,
    }
