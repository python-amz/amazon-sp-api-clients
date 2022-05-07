"""
Selling Partner APIs for Fulfillment Outbound
=============================================================================================

The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
API Version: 2020-07-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalLocationInfo:
    """
    Additional location information.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    A physical address.
    """

    address_line1: str = attrs.field()
    """
    The first line of the address.
    """

    address_line2: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    address_line3: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional address information, if required.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city where the person, business, or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    district_or_county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district or county where the person, business, or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at the address.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the person, business, or institution located at the address.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code of the address.
    """

    state_or_region: str = attrs.field()
    """
    The state or region where the person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CODSettings:
    """
    The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
    """

    cod_charge: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    cod_charge_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    is_cod_required: bool = attrs.field()
    """
    When true, this fulfillment order requires a COD (Cash On Delivery) payment.
    """

    shipping_charge: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    shipping_charge_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelFulfillmentOrderResponse:
    """
    The response schema for the cancelFulfillmentOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFulfillmentOrderItem:
    """
    Item information for creating a fulfillment order.
    """

    displayable_comment: Optional[str] = attrs.field(
        default=None,
    )
    """
    Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 250}
    """

    fulfillment_network_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    gift_message: Optional[str] = attrs.field(
        default=None,
    )
    """
    A message to the gift recipient, if applicable.

    Extra fields:
    {'maxLength': 512}
    """

    per_unit_declared_value: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    per_unit_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    per_unit_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same SellerSKU. For example, the seller might assign different SellerFulfillmentOrderItemId values to two items in a fulfillment order that share the same SellerSKU but have different GiftMessage values.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.

    Extra fields:
    {'maxLength': 50}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFulfillmentOrderRequest:
    """
    The request body schema for the createFulfillmentOrder operation.
    """

    cod_settings: Optional["CODSettings"] = attrs.field(
        default=None,
    )
    """
    The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
    """

    delivery_window: Optional["DeliveryWindow"] = attrs.field(
        default=None,
    )
    """
    The time range within which a Scheduled Delivery fulfillment order should be delivered.
    """

    destination_address: "Address" = attrs.field()
    """
    A physical address.
    """

    displayable_order_comment: str = attrs.field()
    """
    Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 1000}
    """

    displayable_order_date: "Timestamp" = attrs.field()

    displayable_order_id: str = attrs.field()
    """
    A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.
        The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed.

    Extra fields:
    {'maxLength': 40}
    """

    feature_constraints: Optional[List["FeatureSettings"]] = attrs.field(
        default=None,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    fulfillment_action: Optional["FulfillmentAction"] = attrs.field(
        default=None,
    )
    """
    Specifies whether the fulfillment order should ship now or have an order hold put on it.
    """

    fulfillment_policy: Optional["FulfillmentPolicy"] = attrs.field(
        default=None,
    )
    """
    The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
    """

    items: List["CreateFulfillmentOrderItem"] = attrs.field()
    """
    An array of item information for creating a fulfillment order.
    """

    marketplace_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The marketplace the fulfillment order is placed against.
    """

    notification_emails: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
    """

    seller_fulfillment_order_id: str = attrs.field()
    """
    A fulfillment order identifier that the seller creates to track their fulfillment order. The SellerFulfillmentOrderId must be unique for each fulfillment order that a seller creates. If the seller's system already creates unique order identifiers, then these might be good values for them to use.

    Extra fields:
    {'maxLength': 40}
    """

    ship_from_country_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    """
    The shipping method used for the fulfillment order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFulfillmentOrderResponse:
    """
    The response schema for the createFulfillmentOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFulfillmentReturnRequest:
    """
    The createFulfillmentReturn operation creates a fulfillment return for items that were fulfilled using the createFulfillmentOrder operation. For calls to createFulfillmentReturn, you must include ReturnReasonCode values returned by a previous call to the listReturnReasonCodes operation.
    """

    items: List["CreateReturnItem"] = attrs.field()
    """
    An array of items to be returned.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFulfillmentReturnResponse:
    """
    The response schema for the createFulfillmentReturn operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateFulfillmentReturnResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateFulfillmentReturnResult:

    invalid_return_items: Optional[List["InvalidReturnItem"]] = attrs.field()
    """
    An array of invalid return item information.
    """

    return_authorizations: Optional[List["ReturnAuthorization"]] = attrs.field()
    """
    An array of return authorization information.
    """

    return_items: Optional[List["ReturnItem"]] = attrs.field()
    """
    An array of items that Amazon accepted for return. Returns empty if no items were accepted for return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateReturnItem:
    """
    An item that Amazon accepted for return.
    """

    amazon_shipment_id: str = attrs.field()
    """
    The identifier for the shipment that is associated with the return item.
    """

    return_comment: Optional[str] = attrs.field(
        default=None,
    )
    """
    An optional comment about the return item.

    Extra fields:
    {'maxLength': 1000}
    """

    return_reason_code: str = attrs.field()
    """
    The return reason code assigned to the return item by the seller.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    The identifier assigned to the item by the seller when the fulfillment order was created.
    """

    seller_return_item_id: str = attrs.field()
    """
    An identifier assigned by the seller to the return item.

    Extra fields:
    {'maxLength': 80}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CurrentStatus:
    """
    The current delivery status of the package.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeliveryWindow:
    """
    The time range within which a Scheduled Delivery fulfillment order should be delivered.
    """

    end_date: "Timestamp" = attrs.field()

    start_date: "Timestamp" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class EventCode:
    """
    The event code for the delivery event.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Feature:
    """
    A Multi-Channel Fulfillment feature.
    """

    feature_description: str = attrs.field()
    """
    The feature description.
    """

    feature_name: str = attrs.field()
    """
    The feature name.
    """

    seller_eligible: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, indicates that the seller is eligible to use the feature.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeatureSettings:
    """
    FeatureSettings allows users to apply fulfillment features to an order. To block an order from being shipped using Amazon Logistics (AMZL) and an AMZL tracking number, use featureName as BLOCK_AMZL and featureFulfillmentPolicy as Required. Blocking AMZL will incur an additional fee surcharge on your MCF orders and increase the risk of some of your orders being unfulfilled or delivered late if there are no alternative carriers available. Using BLOCK_AMZL in an order request will take precedence over your Seller Central account setting.
    """

    feature_fulfillment_policy: Optional[Union[Literal["Required"], Literal["NotRequired"]]] = attrs.field()
    """
    Specifies the policy to use when fulfilling an order.
    """

    feature_name: Optional[str] = attrs.field()
    """
    The name of the feature.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeatureSku:
    """
    Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    fn_sku: Optional[str] = attrs.field()
    """
    The unique SKU used by Amazon's fulfillment network.
    """

    overlapping_skus: Optional[List[str]] = attrs.field()
    """
    Other seller SKUs that are shared across the same inventory.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """

    sku_count: Optional[float] = attrs.field()
    """
    The number of SKUs available for this service.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Fee:
    """
    Fee type and cost.
    """

    amount: "Money" = attrs.field()
    """
    An amount of money, including units in the form of currency.
    """

    name: Union[
        Literal["FBAPerUnitFulfillmentFee"],
        Literal["FBAPerOrderFulfillmentFee"],
        Literal["FBATransportationFee"],
        Literal["FBAFulfillmentCODFee"],
    ] = attrs.field()
    """
    The type of fee.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentAction:
    """
    Specifies whether the fulfillment order should ship now or have an order hold put on it.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentOrder:
    """
    General information about a fulfillment order, including its status.
    """

    cod_settings: Optional["CODSettings"] = attrs.field(
        default=None,
    )
    """
    The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
    """

    delivery_window: Optional["DeliveryWindow"] = attrs.field(
        default=None,
    )
    """
    The time range within which a Scheduled Delivery fulfillment order should be delivered.
    """

    destination_address: "Address" = attrs.field()
    """
    A physical address.
    """

    displayable_order_comment: str = attrs.field()
    """
    A text block submitted with the createFulfillmentOrder operation. Displays in recipient-facing materials such as the packing slip.
    """

    displayable_order_date: "Timestamp" = attrs.field()

    displayable_order_id: str = attrs.field()
    """
    A fulfillment order identifier submitted with the createFulfillmentOrder operation. Displays as the order identifier in recipient-facing materials such as the packing slip.
    """

    feature_constraints: Optional[List["FeatureSettings"]] = attrs.field(
        default=None,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    fulfillment_action: Optional["FulfillmentAction"] = attrs.field(
        default=None,
    )
    """
    Specifies whether the fulfillment order should ship now or have an order hold put on it.
    """

    fulfillment_order_status: "FulfillmentOrderStatus" = attrs.field()
    """
    The current status of the fulfillment order.
    """

    fulfillment_policy: Optional["FulfillmentPolicy"] = attrs.field(
        default=None,
    )
    """
    The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
    """

    marketplace_id: str = attrs.field()
    """
    The identifier for the marketplace the fulfillment order is placed against.
    """

    notification_emails: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
    """

    received_date: "Timestamp" = attrs.field()

    seller_fulfillment_order_id: str = attrs.field()
    """
    The fulfillment order identifier submitted with the createFulfillmentOrder operation.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    """
    The shipping method used for the fulfillment order.
    """

    status_updated_date: "Timestamp" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentOrderItem:
    """
    Item information for a fulfillment order.
    """

    cancelled_quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    displayable_comment: Optional[str] = attrs.field(
        default=None,
    )
    """
    Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.
    """

    estimated_arrival_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    estimated_ship_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    fulfillment_network_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    gift_message: Optional[str] = attrs.field(
        default=None,
    )
    """
    A message to the gift recipient, if applicable.
    """

    order_item_disposition: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates whether the item is sellable or unsellable.
    """

    per_unit_declared_value: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    per_unit_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    per_unit_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    A fulfillment order item identifier submitted with a call to the createFulfillmentOrder operation.
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """

    unfulfillable_quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentOrderStatus:
    """
    The current status of the fulfillment order.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentPolicy:
    """
    The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentPreview:
    """
    Information about a fulfillment order preview, including delivery and fee information based on shipping method.
    """

    estimated_fees: Optional[List["Fee"]] = attrs.field(
        default=None,
    )
    """
    An array of fee type and cost pairs.
    """

    estimated_shipping_weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """

    feature_constraints: Optional[List["FeatureSettings"]] = attrs.field(
        default=None,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    fulfillment_preview_shipments: Optional[List["FulfillmentPreviewShipment"]] = attrs.field(
        default=None,
    )
    """
    An array of fulfillment preview shipment information.
    """

    is_codcapable: bool = attrs.field()
    """
    When true, this fulfillment order preview is for COD (Cash On Delivery).
    """

    is_fulfillable: bool = attrs.field()
    """
    When true, this fulfillment order preview is fulfillable.
    """

    marketplace_id: str = attrs.field()
    """
    The marketplace the fulfillment order is placed against.
    """

    order_unfulfillable_reasons: Optional[List[str]] = attrs.field(
        default=None,
    )

    scheduled_delivery_info: Optional["ScheduledDeliveryInfo"] = attrs.field(
        default=None,
    )
    """
    Delivery information for a scheduled delivery.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    """
    The shipping method used for the fulfillment order.
    """

    unfulfillable_preview_items: Optional[List["UnfulfillablePreviewItem"]] = attrs.field(
        default=None,
    )
    """
    An array of unfulfillable preview item information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentPreviewItem:
    """
    Item information for a shipment in a fulfillment order preview.
    """

    estimated_shipping_weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    A fulfillment order item identifier that the seller created with a call to the createFulfillmentOrder operation.
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """

    shipping_weight_calculation_method: Optional[Union[Literal["Package"], Literal["Dimensional"]]] = attrs.field(
        default=None,
    )
    """
    The method used to calculate the estimated shipping weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentPreviewShipment:
    """
    Delivery and item information for a shipment in a fulfillment order preview.
    """

    earliest_arrival_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    earliest_ship_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    fulfillment_preview_items: List["FulfillmentPreviewItem"] = attrs.field()
    """
    An array of fulfillment preview item information.
    """

    latest_arrival_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    latest_ship_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    shipping_notes: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    Provides additional insight into the shipment timeline when exact delivery dates are not able to be precomputed.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentReturnItemStatus:
    """
    Indicates if the return item has been processed by a fulfillment center.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentShipment:
    """
    Delivery and item information for a shipment in a fulfillment order.
    """

    amazon_shipment_id: str = attrs.field()
    """
    A shipment identifier assigned by Amazon.
    """

    estimated_arrival_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    fulfillment_center_id: str = attrs.field()
    """
    An identifier for the fulfillment center that the shipment will be sent from.
    """

    fulfillment_shipment_item: List["FulfillmentShipmentItem"] = attrs.field()
    """
    An array of fulfillment shipment item information.
    """

    fulfillment_shipment_package: Optional[List["FulfillmentShipmentPackage"]] = attrs.field(
        default=None,
    )
    """
    An array of fulfillment shipment package information.
    """

    fulfillment_shipment_status: Union[
        Literal["PENDING"], Literal["SHIPPED"], Literal["CANCELLED_BY_FULFILLER"], Literal["CANCELLED_BY_SELLER"]
    ] = attrs.field()
    """
    The current status of the shipment.
    """

    shipping_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    shipping_notes: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    Provides additional insight into shipment timeline. Primairly used to communicate that actual delivery dates aren't available.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentShipmentItem:
    """
    Item information for a shipment in a fulfillment order.
    """

    package_number: Optional[int] = attrs.field(
        default=None,
    )
    """
    An identifier for the package that contains the item quantity.

    Extra fields:
    {'schema_format': 'int32'}
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    The fulfillment order item identifier that the seller created and submitted with a call to the createFulfillmentOrder operation.
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """

    serial_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The serial number of the shipped item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FulfillmentShipmentPackage:
    """
    Package information for a shipment in a fulfillment order.
    """

    carrier_code: str = attrs.field()
    """
    Identifies the carrier who will deliver the shipment to the recipient.
    """

    estimated_arrival_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    package_number: int = attrs.field()
    """
    Identifies a package in a shipment.

    Extra fields:
    {'schema_format': 'int32'}
    """

    tracking_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The tracking number, if provided, can be used to obtain tracking and delivery information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeatureInventoryResponse:
    """
    The breakdown of eligibility inventory by feature.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetFeatureInventoryResult"] = attrs.field()
    """
    The payload for the getEligibileInventory operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeatureInventoryResult:
    """
    The payload for the getEligibileInventory operation.
    """

    feature_name: str = attrs.field()
    """
    The name of the feature.
    """

    feature_skus: Optional[List["FeatureSku"]] = attrs.field(
        default=None,
    )
    """
    An array of SKUs eligible for this feature and the quantity available.
    """

    marketplace_id: str = attrs.field()
    """
    The requested marketplace.
    """

    next_token: Optional[str] = attrs.field(
        default=None,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeatureSkuResponse:
    """
    The response schema for the getFeatureSKU operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetFeatureSkuResult"] = attrs.field()
    """
    The payload for the getFeatureSKU operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeatureSkuResult:
    """
    The payload for the getFeatureSKU operation.
    """

    feature_name: str = attrs.field()
    """
    The name of the feature.
    """

    ineligible_reasons: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    A list of one or more reasons that the seller SKU is ineligibile for the feature.
        Possible values:
        * MERCHANT_NOT_ENROLLED - The merchant isn't enrolled for the feature.
        * SKU_NOT_ELIGIBLE - The SKU doesn't reside in a warehouse that supports the feature.
        * INVALID_SKU - There is an issue with the SKU provided.
    """

    is_eligible: bool = attrs.field()
    """
    When true, the seller SKU is eligible for the requested feature.
    """

    marketplace_id: str = attrs.field()
    """
    The requested marketplace.
    """

    sku_info: Optional["FeatureSku"] = attrs.field(
        default=None,
    )
    """
    Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeaturesResponse:
    """
    The response schema for the getFeatures operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetFeaturesResult"] = attrs.field()
    """
    The payload for the getFeatures operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFeaturesResult:
    """
    The payload for the getFeatures operation.
    """

    features: List["Feature"] = attrs.field()
    """
    An array of features.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFulfillmentOrderResponse:
    """
    The response schema for the getFulfillmentOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetFulfillmentOrderResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFulfillmentOrderResult:

    fulfillment_order: "FulfillmentOrder" = attrs.field()
    """
    General information about a fulfillment order, including its status.
    """

    fulfillment_order_items: List["FulfillmentOrderItem"] = attrs.field()
    """
    An array of fulfillment order item information.
    """

    fulfillment_shipments: Optional[List["FulfillmentShipment"]] = attrs.field(
        default=None,
    )
    """
    An array of fulfillment shipment information.
    """

    return_authorizations: List["ReturnAuthorization"] = attrs.field()
    """
    An array of return authorization information.
    """

    return_items: List["ReturnItem"] = attrs.field()
    """
    An array of items that Amazon accepted for return. Returns empty if no items were accepted for return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFulfillmentPreviewItem:
    """
    Item information for a fulfillment order preview.
    """

    per_unit_declared_value: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    A fulfillment order item identifier that the seller creates to track items in the fulfillment preview.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.

    Extra fields:
    {'maxLength': 50}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFulfillmentPreviewRequest:
    """
    The request body schema for the getFulfillmentPreview operation.
    """

    address: "Address" = attrs.field()
    """
    A physical address.
    """

    feature_constraints: Optional[List["FeatureSettings"]] = attrs.field(
        default=None,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    include_codfulfillment_preview: Optional[bool] = attrs.field(
        default=None,
    )
    """
    Specifies whether to return fulfillment order previews that are for COD (Cash On Delivery).
        Possible values:
        * true - Returns all fulfillment order previews (both for COD and not for COD).
        * false - Returns only fulfillment order previews that are not for COD.
    """

    include_delivery_windows: Optional[bool] = attrs.field(
        default=None,
    )
    """
    Specifies whether to return the ScheduledDeliveryInfo response object, which contains the available delivery windows for a Scheduled Delivery. The ScheduledDeliveryInfo response object can only be returned for fulfillment order previews with ShippingSpeedCategories = ScheduledDelivery.
    """

    items: List["GetFulfillmentPreviewItem"] = attrs.field()
    """
    An array of fulfillment preview item information.
    """

    marketplace_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The marketplace the fulfillment order is placed against.
    """

    shipping_speed_categories: Optional[List["ShippingSpeedCategory"]] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFulfillmentPreviewResponse:
    """
    The response schema for the getFulfillmentPreview operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetFulfillmentPreviewResult"] = attrs.field()
    """
    A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated ship dates and arrival dates.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetFulfillmentPreviewResult:
    """
    A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated ship dates and arrival dates.
    """

    fulfillment_previews: Optional[List["FulfillmentPreview"]] = attrs.field()
    """
    An array of fulfillment preview information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPackageTrackingDetailsResponse:
    """
    The response schema for the getPackageTrackingDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["PackageTrackingDetails"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvalidItemReason:
    """
    The reason that the item is invalid for return.
    """

    description: str = attrs.field()
    """
    A human readable description of the invalid item reason code.
    """

    invalid_item_reason_code: "InvalidItemReasonCode" = attrs.field()
    """
    A code for why the item is invalid for return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvalidItemReasonCode:
    """
    A code for why the item is invalid for return.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvalidReturnItem:
    """
    An item that is invalid for return.
    """

    invalid_item_reason: "InvalidItemReason" = attrs.field()
    """
    The reason that the item is invalid for return.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    The identifier assigned to the item by the seller when the fulfillment order was created.
    """

    seller_return_item_id: str = attrs.field()
    """
    An identifier assigned by the seller to the return item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListAllFulfillmentOrdersResponse:
    """
    The response schema for the listAllFulfillmentOrders operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ListAllFulfillmentOrdersResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListAllFulfillmentOrdersResult:

    fulfillment_orders: Optional[List["FulfillmentOrder"]] = attrs.field()
    """
    An array of fulfillment order information.
    """

    next_token: Optional[str] = attrs.field()
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListReturnReasonCodesResponse:
    """
    The response schema for the listReturnReasonCodes operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ListReturnReasonCodesResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListReturnReasonCodesResult:

    reason_code_details: Optional[List["ReasonCodeDetails"]] = attrs.field()
    """
    An array of return reason code details.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    An amount of money, including units in the form of currency.
    """

    currency_code: str = attrs.field()
    """
    Three digit currency code in ISO 4217 format.
    """

    value: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackageTrackingDetails:

    additional_location_info: Optional["AdditionalLocationInfo"] = attrs.field(
        default=None,
    )
    """
    Additional location information.
    """

    carrier_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the carrier.
    """

    carrier_phone_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the carrier.
    """

    carrier_url: Optional[str] = attrs.field(
        default=None,
    )
    """
    The URL of the carrier’s website.
    """

    current_status: Optional["CurrentStatus"] = attrs.field(
        default=None,
    )
    """
    The current delivery status of the package.
    """

    current_status_description: Optional[str] = attrs.field(
        default=None,
    )
    """
    Description corresponding to the CurrentStatus value.
    """

    customer_tracking_link: Optional[str] = attrs.field(
        default=None,
    )
    """
    Link on swiship.com that allows customers to track the package.
    """

    estimated_arrival_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    package_number: int = attrs.field()
    """
    The package identifier.

    Extra fields:
    {'schema_format': 'int32'}
    """

    ship_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    ship_to_address: Optional["TrackingAddress"] = attrs.field(
        default=None,
    )
    """
    Address information for tracking the package.
    """

    signed_for_by: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the person who signed for the package.
    """

    tracking_events: Optional[List["TrackingEvent"]] = attrs.field(
        default=None,
    )
    """
    An array of tracking event information.
    """

    tracking_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The tracking number for the package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Quantity:
    """
    The item quantity.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReasonCodeDetails:
    """
    A return reason code, a description, and an optional description translation.
    """

    description: str = attrs.field()
    """
    A human readable description of the return reason code.
    """

    return_reason_code: str = attrs.field()
    """
    A code that indicates a valid return reason.
    """

    translated_description: Optional[str] = attrs.field(
        default=None,
    )
    """
    A translation of the description. The translation is in the language specified in the Language request parameter.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReturnAuthorization:
    """
    Return authorization information for items accepted for return.
    """

    amazon_rma_id: str = attrs.field()
    """
    The return merchandise authorization (RMA) that Amazon needs to process the return.
    """

    fulfillment_center_id: str = attrs.field()
    """
    An identifier for the Amazon fulfillment center that the return items should be sent to.
    """

    return_authorization_id: str = attrs.field()
    """
    An identifier for the return authorization. This identifier associates return items with the return authorization used to return them.
    """

    return_to_address: "Address" = attrs.field()
    """
    A physical address.
    """

    rma_page_url: str = attrs.field()
    """
    A URL for a web page that contains the return authorization barcode and the mailing label. This does not include pre-paid shipping.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReturnItem:
    """
    An item that Amazon accepted for return.
    """

    amazon_return_reason_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The return reason code that the Amazon fulfillment center assigned to the return item.
    """

    amazon_shipment_id: str = attrs.field()
    """
    The identifier for the shipment that is associated with the return item.
    """

    fulfillment_center_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the Amazon fulfillment center that processed the return item.
    """

    return_authorization_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    Identifies the return authorization used to return this item. See ReturnAuthorization.
    """

    return_comment: Optional[str] = attrs.field(
        default=None,
    )
    """
    An optional comment about the return item.
    """

    return_received_condition: Optional["ReturnItemDisposition"] = attrs.field(
        default=None,
    )
    """
    The condition of the return item when received by an Amazon fulfillment center.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    The identifier assigned to the item by the seller when the fulfillment order was created.
    """

    seller_return_item_id: str = attrs.field()
    """
    An identifier assigned by the seller to the return item.
    """

    seller_return_reason_code: str = attrs.field()
    """
    The return reason code assigned to the return item by the seller.
    """

    status: "FulfillmentReturnItemStatus" = attrs.field()
    """
    Indicates if the return item has been processed by a fulfillment center.
    """

    status_changed_date: "Timestamp" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ReturnItemDisposition:
    """
    The condition of the return item when received by an Amazon fulfillment center.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ScheduledDeliveryInfo:
    """
    Delivery information for a scheduled delivery.
    """

    delivery_time_zone: str = attrs.field()
    """
    The time zone of the destination address for the fulfillment order preview. Must be an IANA time zone name. Example: Asia/Tokyo.
    """

    delivery_windows: List["DeliveryWindow"] = attrs.field()
    """
    An array of delivery windows.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingSpeedCategory:
    """
    The shipping method used for the fulfillment order.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Timestamp:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingAddress:
    """
    Address information for tracking the package.
    """

    city: str = attrs.field()
    """
    The city.

    Extra fields:
    {'maxLength': 150}
    """

    country: str = attrs.field()
    """
    The country.

    Extra fields:
    {'maxLength': 6}
    """

    state: str = attrs.field()
    """
    The state.

    Extra fields:
    {'maxLength': 150}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingEvent:
    """
    Information for tracking package deliveries.
    """

    event_address: "TrackingAddress" = attrs.field()
    """
    Address information for tracking the package.
    """

    event_code: "EventCode" = attrs.field()
    """
    The event code for the delivery event.
    """

    event_date: "Timestamp" = attrs.field()

    event_description: str = attrs.field()
    """
    A description for the corresponding event code.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnfulfillablePreviewItem:
    """
    Information about unfulfillable items in a fulfillment order preview.
    """

    item_unfulfillable_reasons: Optional[List[str]] = attrs.field(
        default=None,
    )

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    A fulfillment order item identifier created with a call to the getFulfillmentPreview operation.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.

    Extra fields:
    {'maxLength': 50}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateFulfillmentOrderItem:
    """
    Item information for updating a fulfillment order.
    """

    displayable_comment: Optional[str] = attrs.field(
        default=None,
    )
    """
    Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 250}
    """

    fulfillment_network_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    gift_message: Optional[str] = attrs.field(
        default=None,
    )
    """
    A message to the gift recipient, if applicable.

    Extra fields:
    {'maxLength': 512}
    """

    order_item_disposition: Optional[str] = attrs.field(
        default=None,
    )
    """
    Indicates whether the item is sellable or unsellable.
    """

    per_unit_declared_value: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    per_unit_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    per_unit_tax: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    An amount of money, including units in the form of currency.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_fulfillment_order_item_id: str = attrs.field()
    """
    Identifies the fulfillment order item to update. Created with a previous call to the createFulfillmentOrder operation.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller SKU of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateFulfillmentOrderRequest:

    destination_address: Optional["Address"] = attrs.field()
    """
    A physical address.
    """

    displayable_order_comment: Optional[str] = attrs.field()
    """
    Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 1000}
    """

    displayable_order_date: Optional["Timestamp"] = attrs.field()

    displayable_order_id: Optional[str] = attrs.field()
    """
    A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.

    Extra fields:
    {'maxLength': 40}
    """

    feature_constraints: Optional[List["FeatureSettings"]] = attrs.field()
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    fulfillment_action: Optional["FulfillmentAction"] = attrs.field()
    """
    Specifies whether the fulfillment order should ship now or have an order hold put on it.
    """

    fulfillment_policy: Optional["FulfillmentPolicy"] = attrs.field()
    """
    The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
    """

    items: Optional[List["UpdateFulfillmentOrderItem"]] = attrs.field()
    """
    An array of fulfillment order item information for updating a fulfillment order.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    The marketplace the fulfillment order is placed against.
    """

    notification_emails: Optional[List[str]] = attrs.field()
    """
    A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
    """

    ship_from_country_code: Optional[str] = attrs.field()
    """
    The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
    """

    shipping_speed_category: Optional["ShippingSpeedCategory"] = attrs.field()
    """
    The shipping method used for the fulfillment order.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class UpdateFulfillmentOrderResponse:
    """
    The response schema for the updateFulfillmentOrder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight.
    """

    unit: Union[Literal["KG"], Literal["KILOGRAMS"], Literal["LB"], Literal["POUNDS"]] = attrs.field()
    """
    The unit of weight.
    """

    value: str = attrs.field()
    """
    The weight value.
    """


class FulfillmentOutbound20200701Client(BaseClient):
    def cancel_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
    ) -> Union[CancelFulfillmentOrderResponse]:
        """
        Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_fulfillment_order_id: The identifier assigned to the item by the seller when the fulfillment order was created.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel"
        values = (seller_fulfillment_order_id,)
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._cancel_fulfillment_order_params,
        )
        klass = self._cancel_fulfillment_order_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _cancel_fulfillment_order_params = (("sellerFulfillmentOrderId", "path"),)  # name, param in

    _cancel_fulfillment_order_responses = {
        200: CancelFulfillmentOrderResponse,
        400: CancelFulfillmentOrderResponse,
        401: CancelFulfillmentOrderResponse,
        403: CancelFulfillmentOrderResponse,
        404: CancelFulfillmentOrderResponse,
        429: CancelFulfillmentOrderResponse,
        500: CancelFulfillmentOrderResponse,
        503: CancelFulfillmentOrderResponse,
    }

    def create_fulfillment_order(
        self,
        destination_address: Dict[str, Any],
        displayable_order_comment: str,
        displayable_order_date: datetime,
        displayable_order_id: str,
        items: List["CreateFulfillmentOrderItem"],
        seller_fulfillment_order_id: str,
        shipping_speed_category: Union[
            Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
        ],
        cod_settings: Dict[str, Any] = None,
        delivery_window: Dict[str, Any] = None,
        feature_constraints: List["FeatureSettings"] = None,
        fulfillment_action: Union[Literal["Ship"], Literal["Hold"]] = None,
        fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]] = None,
        marketplace_id: str = None,
        notification_emails: List[str] = None,
        ship_from_country_code: str = None,
    ) -> Union[CreateFulfillmentOrderResponse]:
        """
        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            cod_settings: The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
            delivery_window: The time range within which a Scheduled Delivery fulfillment order should be delivered.
            destination_address: A physical address.
            displayable_order_comment: Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.
            displayable_order_date: no description.
            displayable_order_id: A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.
                The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed.
            feature_constraints: A list of features and their fulfillment policies to apply to the order.
            fulfillment_action: Specifies whether the fulfillment order should ship now or have an order hold put on it.
            fulfillment_policy: The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
            items: An array of item information for creating a fulfillment order.
            marketplace_id: The marketplace the fulfillment order is placed against.
            notification_emails: A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
            seller_fulfillment_order_id: A fulfillment order identifier that the seller creates to track their fulfillment order. The SellerFulfillmentOrderId must be unique for each fulfillment order that a seller creates. If the seller's system already creates unique order identifiers, then these might be good values for them to use.
            ship_from_country_code: The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
            shipping_speed_category: The shipping method used for the fulfillment order.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders"
        values = (
            cod_settings,
            delivery_window,
            destination_address,
            displayable_order_comment,
            displayable_order_date,
            displayable_order_id,
            feature_constraints,
            fulfillment_action,
            fulfillment_policy,
            items,
            marketplace_id,
            notification_emails,
            seller_fulfillment_order_id,
            ship_from_country_code,
            shipping_speed_category,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_fulfillment_order_params,
        )
        klass = self._create_fulfillment_order_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_fulfillment_order_params = (  # name, param in
        ("codSettings", "body"),
        ("deliveryWindow", "body"),
        ("destinationAddress", "body"),
        ("displayableOrderComment", "body"),
        ("displayableOrderDate", "body"),
        ("displayableOrderId", "body"),
        ("featureConstraints", "body"),
        ("fulfillmentAction", "body"),
        ("fulfillmentPolicy", "body"),
        ("items", "body"),
        ("marketplaceId", "body"),
        ("notificationEmails", "body"),
        ("sellerFulfillmentOrderId", "body"),
        ("shipFromCountryCode", "body"),
        ("shippingSpeedCategory", "body"),
    )

    _create_fulfillment_order_responses = {
        200: CreateFulfillmentOrderResponse,
        400: CreateFulfillmentOrderResponse,
        401: CreateFulfillmentOrderResponse,
        403: CreateFulfillmentOrderResponse,
        404: CreateFulfillmentOrderResponse,
        429: CreateFulfillmentOrderResponse,
        500: CreateFulfillmentOrderResponse,
        503: CreateFulfillmentOrderResponse,
    }

    def create_fulfillment_return(
        self,
        seller_fulfillment_order_id: str,
        items: List["CreateReturnItem"],
    ) -> Union[CreateFulfillmentReturnResponse]:
        """
        Creates a fulfillment return.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_fulfillment_order_id: An identifier assigned by the seller to the fulfillment order at the time it was created. The seller uses their own records to find the correct SellerFulfillmentOrderId value based on the buyer's request to return items.
            items: An array of items to be returned.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return"
        values = (
            seller_fulfillment_order_id,
            items,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._create_fulfillment_return_params,
        )
        klass = self._create_fulfillment_return_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_fulfillment_return_params = (  # name, param in
        ("sellerFulfillmentOrderId", "path"),
        ("items", "body"),
    )

    _create_fulfillment_return_responses = {
        200: CreateFulfillmentReturnResponse,
        400: CreateFulfillmentReturnResponse,
        401: CreateFulfillmentReturnResponse,
        403: CreateFulfillmentReturnResponse,
        404: CreateFulfillmentReturnResponse,
        429: CreateFulfillmentReturnResponse,
        500: CreateFulfillmentReturnResponse,
        503: CreateFulfillmentReturnResponse,
    }

    def get_feature_inventory(
        self,
        marketplace_id: str,
        feature_name: str,
        next_token: str = None,
    ) -> Union[GetFeatureInventoryResponse]:
        """
        Returns a list of inventory items that are eligible for the fulfillment feature you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The marketplace for which to return a list of the inventory that is eligible for the specified feature.
            feature_name: The name of the feature for which to return a list of eligible inventory.
            next_token: A string token returned in the response to your previous request that is used to return the next response page. A value of null will return the first page.
        """
        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}"
        values = (
            marketplace_id,
            feature_name,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_feature_inventory_params,
        )
        klass = self._get_feature_inventory_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_feature_inventory_params = (  # name, param in
        ("marketplaceId", "query"),
        ("featureName", "path"),
        ("nextToken", "query"),
    )

    _get_feature_inventory_responses = {
        200: GetFeatureInventoryResponse,
        400: GetFeatureInventoryResponse,
        401: GetFeatureInventoryResponse,
        403: GetFeatureInventoryResponse,
        404: GetFeatureInventoryResponse,
        429: GetFeatureInventoryResponse,
        500: GetFeatureInventoryResponse,
        503: GetFeatureInventoryResponse,
    }

    def get_feature_sku(
        self,
        marketplace_id: str,
        feature_name: str,
        seller_sku: str,
    ) -> Union[GetFeatureSkuResponse]:
        """
        Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty skuInfo object.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The marketplace for which to return the count.
            feature_name: The name of the feature.
            seller_sku: Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
        """
        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}"
        values = (
            marketplace_id,
            feature_name,
            seller_sku,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_feature_sku_params,
        )
        klass = self._get_feature_sku_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_feature_sku_params = (  # name, param in
        ("marketplaceId", "query"),
        ("featureName", "path"),
        ("sellerSku", "path"),
    )

    _get_feature_sku_responses = {
        200: GetFeatureSkuResponse,
        400: GetFeatureSkuResponse,
        401: GetFeatureSkuResponse,
        403: GetFeatureSkuResponse,
        404: GetFeatureSkuResponse,
        429: GetFeatureSkuResponse,
        500: GetFeatureSkuResponse,
        503: GetFeatureSkuResponse,
    }

    def get_features(
        self,
        marketplace_id: str,
    ) -> Union[GetFeaturesResponse]:
        """
        Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The marketplace for which to return the list of features.
        """
        url = "/fba/outbound/2020-07-01/features"
        values = (marketplace_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_features_params,
        )
        klass = self._get_features_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_features_params = (("marketplaceId", "query"),)  # name, param in

    _get_features_responses = {
        200: GetFeaturesResponse,
        400: GetFeaturesResponse,
        401: GetFeaturesResponse,
        403: GetFeaturesResponse,
        404: GetFeaturesResponse,
        429: GetFeaturesResponse,
        500: GetFeaturesResponse,
        503: GetFeaturesResponse,
    }

    def get_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
    ) -> Union[GetFulfillmentOrderResponse]:
        """
        Returns the fulfillment order indicated by the specified order identifier.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_fulfillment_order_id: The identifier assigned to the item by the seller when the fulfillment order was created.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}"
        values = (seller_fulfillment_order_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_fulfillment_order_params,
        )
        klass = self._get_fulfillment_order_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_fulfillment_order_params = (("sellerFulfillmentOrderId", "path"),)  # name, param in

    _get_fulfillment_order_responses = {
        200: GetFulfillmentOrderResponse,
        400: GetFulfillmentOrderResponse,
        401: GetFulfillmentOrderResponse,
        403: GetFulfillmentOrderResponse,
        404: GetFulfillmentOrderResponse,
        429: GetFulfillmentOrderResponse,
        500: GetFulfillmentOrderResponse,
        503: GetFulfillmentOrderResponse,
    }

    def get_fulfillment_preview(
        self,
        address: Dict[str, Any],
        items: List["GetFulfillmentPreviewItem"],
        feature_constraints: List["FeatureSettings"] = None,
        include_codfulfillment_preview: bool = None,
        include_delivery_windows: bool = None,
        marketplace_id: str = None,
        shipping_speed_categories: List["ShippingSpeedCategory"] = None,
    ) -> Union[GetFulfillmentPreviewResponse]:
        """
        Returns a list of fulfillment order previews based on shipping criteria that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            address: A physical address.
            feature_constraints: A list of features and their fulfillment policies to apply to the order.
            include_codfulfillment_preview: Specifies whether to return fulfillment order previews that are for COD (Cash On Delivery).
                Possible values:
                * true - Returns all fulfillment order previews (both for COD and not for COD).
                * false - Returns only fulfillment order previews that are not for COD.
            include_delivery_windows: Specifies whether to return the ScheduledDeliveryInfo response object, which contains the available delivery windows for a Scheduled Delivery. The ScheduledDeliveryInfo response object can only be returned for fulfillment order previews with ShippingSpeedCategories = ScheduledDelivery.
            items: An array of fulfillment preview item information.
            marketplace_id: The marketplace the fulfillment order is placed against.
            shipping_speed_categories: no description.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/preview"
        values = (
            address,
            feature_constraints,
            include_codfulfillment_preview,
            include_delivery_windows,
            items,
            marketplace_id,
            shipping_speed_categories,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_fulfillment_preview_params,
        )
        klass = self._get_fulfillment_preview_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_fulfillment_preview_params = (  # name, param in
        ("address", "body"),
        ("featureConstraints", "body"),
        ("includeCODFulfillmentPreview", "body"),
        ("includeDeliveryWindows", "body"),
        ("items", "body"),
        ("marketplaceId", "body"),
        ("shippingSpeedCategories", "body"),
    )

    _get_fulfillment_preview_responses = {
        200: GetFulfillmentPreviewResponse,
        400: GetFulfillmentPreviewResponse,
        401: GetFulfillmentPreviewResponse,
        403: GetFulfillmentPreviewResponse,
        404: GetFulfillmentPreviewResponse,
        429: GetFulfillmentPreviewResponse,
        500: GetFulfillmentPreviewResponse,
        503: GetFulfillmentPreviewResponse,
    }

    def get_package_tracking_details(
        self,
        package_number: int,
    ) -> Union[GetPackageTrackingDetailsResponse]:
        """
        Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            package_number: The unencrypted package identifier returned by the getFulfillmentOrder operation.
        """
        url = "/fba/outbound/2020-07-01/tracking"
        values = (package_number,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_package_tracking_details_params,
        )
        klass = self._get_package_tracking_details_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_package_tracking_details_params = (("packageNumber", "query"),)  # name, param in

    _get_package_tracking_details_responses = {
        200: GetPackageTrackingDetailsResponse,
        400: GetPackageTrackingDetailsResponse,
        401: GetPackageTrackingDetailsResponse,
        403: GetPackageTrackingDetailsResponse,
        404: GetPackageTrackingDetailsResponse,
        429: GetPackageTrackingDetailsResponse,
        500: GetPackageTrackingDetailsResponse,
        503: GetPackageTrackingDetailsResponse,
    }

    def list_all_fulfillment_orders(
        self,
        query_start_date: datetime = None,
        next_token: str = None,
    ) -> Union[ListAllFulfillmentOrdersResponse]:
        """
        Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the next token parameter.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            query_start_date: A date used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order.
            next_token: A string token returned in the response to your previous request.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders"
        values = (
            query_start_date,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_all_fulfillment_orders_params,
        )
        klass = self._list_all_fulfillment_orders_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_all_fulfillment_orders_params = (  # name, param in
        ("queryStartDate", "query"),
        ("nextToken", "query"),
    )

    _list_all_fulfillment_orders_responses = {
        200: ListAllFulfillmentOrdersResponse,
        400: ListAllFulfillmentOrdersResponse,
        401: ListAllFulfillmentOrdersResponse,
        403: ListAllFulfillmentOrdersResponse,
        404: ListAllFulfillmentOrdersResponse,
        429: ListAllFulfillmentOrdersResponse,
        500: ListAllFulfillmentOrdersResponse,
        503: ListAllFulfillmentOrdersResponse,
    }

    def list_return_reason_codes(
        self,
        seller_sku: str,
        language: str,
        marketplace_id: str = None,
        seller_fulfillment_order_id: str = None,
    ) -> Union[ListReturnReasonCodesResponse]:
        """
        Returns a list of return reason codes for a seller SKU in a given marketplace.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_sku: The seller SKU for which return reason codes are required.
            marketplace_id: The marketplace for which the seller wants return reason codes.
            seller_fulfillment_order_id: The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes.
            language: The language that the TranslatedDescription property of the ReasonCodeDetails response object should be translated into.
        """
        url = "/fba/outbound/2020-07-01/returnReasonCodes"
        values = (
            seller_sku,
            marketplace_id,
            seller_fulfillment_order_id,
            language,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_return_reason_codes_params,
        )
        klass = self._list_return_reason_codes_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_return_reason_codes_params = (  # name, param in
        ("sellerSku", "query"),
        ("marketplaceId", "query"),
        ("sellerFulfillmentOrderId", "query"),
        ("language", "query"),
    )

    _list_return_reason_codes_responses = {
        200: ListReturnReasonCodesResponse,
        400: ListReturnReasonCodesResponse,
        401: ListReturnReasonCodesResponse,
        403: ListReturnReasonCodesResponse,
        404: ListReturnReasonCodesResponse,
        429: ListReturnReasonCodesResponse,
        500: ListReturnReasonCodesResponse,
        503: ListReturnReasonCodesResponse,
    }

    def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        destination_address: Dict[str, Any] = None,
        displayable_order_comment: str = None,
        displayable_order_date: datetime = None,
        displayable_order_id: str = None,
        feature_constraints: List["FeatureSettings"] = None,
        fulfillment_action: Union[Literal["Ship"], Literal["Hold"]] = None,
        fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]] = None,
        items: List["UpdateFulfillmentOrderItem"] = None,
        marketplace_id: str = None,
        notification_emails: List[str] = None,
        ship_from_country_code: str = None,
        shipping_speed_category: Union[
            Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
        ] = None,
    ) -> Union[UpdateFulfillmentOrderResponse]:
        """
        Updates and/or requests shipment for a fulfillment order with an order hold on it.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_fulfillment_order_id: The identifier assigned to the item by the seller when the fulfillment order was created.
            destination_address: A physical address.
            displayable_order_comment: Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.
            displayable_order_date: no description.
            displayable_order_id: A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.
            feature_constraints: A list of features and their fulfillment policies to apply to the order.
            fulfillment_action: Specifies whether the fulfillment order should ship now or have an order hold put on it.
            fulfillment_policy: The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
            items: An array of fulfillment order item information for updating a fulfillment order.
            marketplace_id: The marketplace the fulfillment order is placed against.
            notification_emails: A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
            ship_from_country_code: The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
            shipping_speed_category: The shipping method used for the fulfillment order.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}"
        values = (
            seller_fulfillment_order_id,
            destination_address,
            displayable_order_comment,
            displayable_order_date,
            displayable_order_id,
            feature_constraints,
            fulfillment_action,
            fulfillment_policy,
            items,
            marketplace_id,
            notification_emails,
            ship_from_country_code,
            shipping_speed_category,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._update_fulfillment_order_params,
        )
        klass = self._update_fulfillment_order_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _update_fulfillment_order_params = (  # name, param in
        ("sellerFulfillmentOrderId", "path"),
        ("destinationAddress", "body"),
        ("displayableOrderComment", "body"),
        ("displayableOrderDate", "body"),
        ("displayableOrderId", "body"),
        ("featureConstraints", "body"),
        ("fulfillmentAction", "body"),
        ("fulfillmentPolicy", "body"),
        ("items", "body"),
        ("marketplaceId", "body"),
        ("notificationEmails", "body"),
        ("shipFromCountryCode", "body"),
        ("shippingSpeedCategory", "body"),
    )

    _update_fulfillment_order_responses = {
        200: UpdateFulfillmentOrderResponse,
        400: UpdateFulfillmentOrderResponse,
        401: UpdateFulfillmentOrderResponse,
        403: UpdateFulfillmentOrderResponse,
        404: UpdateFulfillmentOrderResponse,
        429: UpdateFulfillmentOrderResponse,
        500: UpdateFulfillmentOrderResponse,
        503: UpdateFulfillmentOrderResponse,
    }
