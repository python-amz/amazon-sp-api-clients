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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AdditionalLocationInfo:

    pass


@attrs.define
class Address:

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    The first line of the address.
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.
    """

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city where the person, business, or institution is located.
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    district_or_county: str = attrs.field(
        kw_only=True,
    )
    """
    The district or county where the person, business, or institution is located.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person, business or institution at the address.
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the person, business, or institution located at the address.
    """

    postal_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal code of the address.
    """

    state_or_region: str = attrs.field(
        kw_only=True,
    )
    """
    The state or region where the person, business or institution is located.
    """

    pass


@attrs.define
class CODSettings:

    is_cod_required: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, this fulfillment order requires a COD (Cash On Delivery) payment.
    """

    cod_charge: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    cod_charge_tax: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_charge: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_charge_tax: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CancelFulfillmentOrderResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateFulfillmentOrderItem:

    displayable_comment: str = attrs.field(
        kw_only=True,
    )
    """
    Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 250}
    """

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    gift_message: str = attrs.field(
        kw_only=True,
    )
    """
    A message to the gift recipient, if applicable.

    Extra fields:
    {'maxLength': 512}
    """

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same SellerSKU. For example, the seller might assign different SellerFulfillmentOrderItemId values to two items in a fulfillment order that share the same SellerSKU but have different GiftMessage values.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.

    Extra fields:
    {'maxLength': 50}
    """

    per_unit_declared_value: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_tax: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateFulfillmentOrderItemList:

    pass


@attrs.define
class CreateFulfillmentOrderRequest:

    displayable_order_comment: str = attrs.field(
        kw_only=True,
    )
    """
    Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 1000}
    """

    displayable_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.
        The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed.

    Extra fields:
    {'maxLength': 40}
    """

    feature_constraints: list["FeatureSettings"] = attrs.field(
        kw_only=True,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The marketplace the fulfillment order is placed against.
    """

    seller_fulfillment_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order identifier that the seller creates to track their fulfillment order. The SellerFulfillmentOrderId must be unique for each fulfillment order that a seller creates. If the seller's system already creates unique order identifiers, then these might be good values for them to use.

    Extra fields:
    {'maxLength': 40}
    """

    ship_from_country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
    """

    cod_settings: "CODSettings" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    delivery_window: "DeliveryWindow" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    destination_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    displayable_order_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_action: "FulfillmentAction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_policy: "FulfillmentPolicy" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    items: "CreateFulfillmentOrderItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    notification_emails: "NotificationEmailList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateFulfillmentOrderResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateFulfillmentReturnRequest:

    items: "CreateReturnItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateFulfillmentReturnResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CreateFulfillmentReturnResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateFulfillmentReturnResult:

    invalid_return_items: "InvalidReturnItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    return_authorizations: "ReturnAuthorizationList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    return_items: "ReturnItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateReturnItem:

    amazon_shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the shipment that is associated with the return item.
    """

    return_comment: str = attrs.field(
        kw_only=True,
    )
    """
    An optional comment about the return item.

    Extra fields:
    {'maxLength': 1000}
    """

    return_reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    The return reason code assigned to the return item by the seller.
    """

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier assigned to the item by the seller when the fulfillment order was created.
    """

    seller_return_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier assigned by the seller to the return item.

    Extra fields:
    {'maxLength': 80}
    """

    pass


@attrs.define
class CreateReturnItemList:

    pass


@attrs.define
class CurrentStatus:

    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class DeliveryWindow:

    end_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    start_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class DeliveryWindowList:

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
class EventCode:

    pass


@attrs.define
class Feature:

    feature_description: str = attrs.field(
        kw_only=True,
    )
    """
    The feature description.
    """

    feature_name: str = attrs.field(
        kw_only=True,
    )
    """
    The feature name.
    """

    seller_eligible: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, indicates that the seller is eligible to use the feature.
    """

    pass


@attrs.define
class FeatureSettings:

    feature_fulfillment_policy: Union[Literal["Required"], Literal["NotRequired"]] = attrs.field(
        kw_only=True,
    )
    """
    Specifies the policy to use when fulfilling an order.
    """

    feature_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the feature.
    """

    pass


@attrs.define
class FeatureSku:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    fn_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The unique SKU used by Amazon's fulfillment network.
    """

    overlapping_skus: list[str] = attrs.field(
        kw_only=True,
    )
    """
    Other seller SKUs that are shared across the same inventory.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """

    sku_count: float = attrs.field(
        kw_only=True,
    )
    """
    The number of SKUs available for this service.
    """

    pass


@attrs.define
class Features:

    pass


@attrs.define
class Fee:

    name: Union[
        Literal["FBAPerUnitFulfillmentFee"],
        Literal["FBAPerOrderFulfillmentFee"],
        Literal["FBATransportationFee"],
        Literal["FBAFulfillmentCODFee"],
    ] = attrs.field(
        kw_only=True,
    )
    """
    The type of fee.
    """

    amount: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FeeList:

    pass


@attrs.define
class FulfillmentAction:

    pass


@attrs.define
class FulfillmentOrder:

    displayable_order_comment: str = attrs.field(
        kw_only=True,
    )
    """
    A text block submitted with the createFulfillmentOrder operation. Displays in recipient-facing materials such as the packing slip.
    """

    displayable_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order identifier submitted with the createFulfillmentOrder operation. Displays as the order identifier in recipient-facing materials such as the packing slip.
    """

    feature_constraints: list["FeatureSettings"] = attrs.field(
        kw_only=True,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the marketplace the fulfillment order is placed against.
    """

    seller_fulfillment_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The fulfillment order identifier submitted with the createFulfillmentOrder operation.
    """

    cod_settings: "CODSettings" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    delivery_window: "DeliveryWindow" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    destination_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    displayable_order_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_action: "FulfillmentAction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_order_status: "FulfillmentOrderStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_policy: "FulfillmentPolicy" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    notification_emails: "NotificationEmailList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    received_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    status_updated_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentOrderItem:

    displayable_comment: str = attrs.field(
        kw_only=True,
    )
    """
    Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.
    """

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    gift_message: str = attrs.field(
        kw_only=True,
    )
    """
    A message to the gift recipient, if applicable.
    """

    order_item_disposition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the item is sellable or unsellable.
    """

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order item identifier submitted with a call to the createFulfillmentOrder operation.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    cancelled_quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    estimated_arrival_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    estimated_ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_declared_value: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_tax: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    unfulfillable_quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentOrderItemList:

    pass


@attrs.define
class FulfillmentOrderStatus:

    pass


@attrs.define
class FulfillmentPolicy:

    pass


@attrs.define
class FulfillmentPreview:

    feature_constraints: list["FeatureSettings"] = attrs.field(
        kw_only=True,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    is_codcapable: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, this fulfillment order preview is for COD (Cash On Delivery).
    """

    is_fulfillable: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, this fulfillment order preview is fulfillable.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The marketplace the fulfillment order is placed against.
    """

    estimated_fees: "FeeList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    estimated_shipping_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_preview_shipments: "FulfillmentPreviewShipmentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    order_unfulfillable_reasons: "StringList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    scheduled_delivery_info: "ScheduledDeliveryInfo" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    unfulfillable_preview_items: "UnfulfillablePreviewItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentPreviewItem:

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order item identifier that the seller created with a call to the createFulfillmentOrder operation.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    shipping_weight_calculation_method: Union[Literal["Package"], Literal["Dimensional"]] = attrs.field(
        kw_only=True,
    )
    """
    The method used to calculate the estimated shipping weight.
    """

    estimated_shipping_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentPreviewItemList:

    pass


@attrs.define
class FulfillmentPreviewList:

    pass


@attrs.define
class FulfillmentPreviewShipment:

    shipping_notes: list[str] = attrs.field(
        kw_only=True,
    )
    """
    Provides additional insight into the shipment timeline when exact delivery dates are not able to be precomputed.
    """

    earliest_arrival_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    earliest_ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_preview_items: "FulfillmentPreviewItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    latest_arrival_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    latest_ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentPreviewShipmentList:

    pass


@attrs.define
class FulfillmentReturnItemStatus:

    pass


@attrs.define
class FulfillmentShipment:

    amazon_shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    A shipment identifier assigned by Amazon.
    """

    fulfillment_center_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for the fulfillment center that the shipment will be sent from.
    """

    fulfillment_shipment_status: Union[
        Literal["PENDING"], Literal["SHIPPED"], Literal["CANCELLED_BY_FULFILLER"], Literal["CANCELLED_BY_SELLER"]
    ] = attrs.field(
        kw_only=True,
    )
    """
    The current status of the shipment.
    """

    shipping_notes: list[str] = attrs.field(
        kw_only=True,
    )
    """
    Provides additional insight into shipment timeline. Primairly used to communicate that actual delivery dates aren't available.
    """

    estimated_arrival_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_shipment_item: "FulfillmentShipmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_shipment_package: "FulfillmentShipmentPackageList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentShipmentItem:

    package_number: int = attrs.field(
        kw_only=True,
    )
    """
    An identifier for the package that contains the item quantity.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The fulfillment order item identifier that the seller created and submitted with a call to the createFulfillmentOrder operation.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    serial_number: str = attrs.field(
        kw_only=True,
    )
    """
    The serial number of the shipped item.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentShipmentItemList:

    pass


@attrs.define
class FulfillmentShipmentList:

    pass


@attrs.define
class FulfillmentShipmentPackage:

    carrier_code: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the carrier who will deliver the shipment to the recipient.
    """

    package_number: int = attrs.field(
        kw_only=True,
    )
    """
    Identifies a package in a shipment.

    Extra fields:
    {'schema_format': 'int32'}
    """

    tracking_number: str = attrs.field(
        kw_only=True,
    )
    """
    The tracking number, if provided, can be used to obtain tracking and delivery information.
    """

    estimated_arrival_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FulfillmentShipmentPackageList:

    pass


@attrs.define
class GetFeatureInventoryResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetFeatureInventoryResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFeatureInventoryResult:

    feature_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the feature.
    """

    feature_skus: list["FeatureSku"] = attrs.field(
        kw_only=True,
    )
    """
    An array of SKUs eligible for this feature and the quantity available.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The requested marketplace.
    """

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    pass


@attrs.define
class GetFeatureSkuResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetFeatureSkuResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFeatureSkuResult:

    feature_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the feature.
    """

    ineligible_reasons: list[str] = attrs.field(
        kw_only=True,
    )
    """
    A list of one or more reasons that the seller SKU is ineligibile for the feature.
        Possible values:
        * MERCHANT_NOT_ENROLLED - The merchant isn't enrolled for the feature.
        * SKU_NOT_ELIGIBLE - The SKU doesn't reside in a warehouse that supports the feature.
        * INVALID_SKU - There is an issue with the SKU provided.
    """

    is_eligible: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the seller SKU is eligible for the requested feature.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The requested marketplace.
    """

    sku_info: "FeatureSku" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFeaturesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetFeaturesResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFeaturesResult:

    features: "Features" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFulfillmentOrderResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetFulfillmentOrderResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFulfillmentOrderResult:

    fulfillment_order: "FulfillmentOrder" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_order_items: "FulfillmentOrderItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_shipments: "FulfillmentShipmentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    return_authorizations: "ReturnAuthorizationList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    return_items: "ReturnItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFulfillmentPreviewItem:

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order item identifier that the seller creates to track items in the fulfillment preview.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.

    Extra fields:
    {'maxLength': 50}
    """

    per_unit_declared_value: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFulfillmentPreviewItemList:

    pass


@attrs.define
class GetFulfillmentPreviewRequest:

    feature_constraints: list["FeatureSettings"] = attrs.field(
        kw_only=True,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    include_codfulfillment_preview: bool = attrs.field(
        kw_only=True,
    )
    """
    Specifies whether to return fulfillment order previews that are for COD (Cash On Delivery).
        Possible values:
        * true - Returns all fulfillment order previews (both for COD and not for COD).
        * false - Returns only fulfillment order previews that are not for COD.
    """

    include_delivery_windows: bool = attrs.field(
        kw_only=True,
    )
    """
    Specifies whether to return the ScheduledDeliveryInfo response object, which contains the available delivery windows for a Scheduled Delivery. The ScheduledDeliveryInfo response object can only be returned for fulfillment order previews with ShippingSpeedCategories = ScheduledDelivery.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The marketplace the fulfillment order is placed against.
    """

    address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    items: "GetFulfillmentPreviewItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_speed_categories: "ShippingSpeedCategoryList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFulfillmentPreviewResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetFulfillmentPreviewResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetFulfillmentPreviewResult:

    fulfillment_previews: "FulfillmentPreviewList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetPackageTrackingDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "PackageTrackingDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InvalidItemReason:

    description: str = attrs.field(
        kw_only=True,
    )
    """
    A human readable description of the invalid item reason code.
    """

    invalid_item_reason_code: "InvalidItemReasonCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InvalidItemReasonCode:

    pass


@attrs.define
class InvalidReturnItem:

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier assigned to the item by the seller when the fulfillment order was created.
    """

    seller_return_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier assigned by the seller to the return item.
    """

    invalid_item_reason: "InvalidItemReason" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class InvalidReturnItemList:

    pass


@attrs.define
class ListAllFulfillmentOrdersResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ListAllFulfillmentOrdersResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ListAllFulfillmentOrdersResult:

    fulfillment_orders: list["FulfillmentOrder"] = attrs.field(
        kw_only=True,
    )
    """
    An array of fulfillment order information.
    """

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    pass


@attrs.define
class ListReturnReasonCodesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ListReturnReasonCodesResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ListReturnReasonCodesResult:

    reason_code_details: "ReasonCodeDetailsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Money:

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three digit currency code in ISO 4217 format.
    """

    value: "Decimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NotificationEmailList:

    pass


@attrs.define
class PackageTrackingDetails:

    carrier_code: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """

    carrier_phone_number: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the carrier.
    """

    carrier_url: str = attrs.field(
        kw_only=True,
    )
    """
    The URL of the carrier’s website.
    """

    current_status_description: str = attrs.field(
        kw_only=True,
    )
    """
    Description corresponding to the CurrentStatus value.
    """

    customer_tracking_link: str = attrs.field(
        kw_only=True,
    )
    """
    Link on swiship.com that allows customers to track the package.
    """

    package_number: int = attrs.field(
        kw_only=True,
    )
    """
    The package identifier.

    Extra fields:
    {'schema_format': 'int32'}
    """

    signed_for_by: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person who signed for the package.
    """

    tracking_number: str = attrs.field(
        kw_only=True,
    )
    """
    The tracking number for the package.
    """

    additional_location_info: "AdditionalLocationInfo" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    current_status: "CurrentStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    estimated_arrival_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to_address: "TrackingAddress" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tracking_events: "TrackingEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Quantity:

    pass


@attrs.define
class ReasonCodeDetails:

    description: str = attrs.field(
        kw_only=True,
    )
    """
    A human readable description of the return reason code.
    """

    return_reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    A code that indicates a valid return reason.
    """

    translated_description: str = attrs.field(
        kw_only=True,
    )
    """
    A translation of the description. The translation is in the language specified in the Language request parameter.
    """

    pass


@attrs.define
class ReasonCodeDetailsList:

    pass


@attrs.define
class ReturnAuthorization:

    amazon_rma_id: str = attrs.field(
        kw_only=True,
    )
    """
    The return merchandise authorization (RMA) that Amazon needs to process the return.
    """

    fulfillment_center_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for the Amazon fulfillment center that the return items should be sent to.
    """

    return_authorization_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for the return authorization. This identifier associates return items with the return authorization used to return them.
    """

    rma_page_url: str = attrs.field(
        kw_only=True,
    )
    """
    A URL for a web page that contains the return authorization barcode and the mailing label. This does not include pre-paid shipping.
    """

    return_to_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ReturnAuthorizationList:

    pass


@attrs.define
class ReturnItem:

    amazon_return_reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    The return reason code that the Amazon fulfillment center assigned to the return item.
    """

    amazon_shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the shipment that is associated with the return item.
    """

    fulfillment_center_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the Amazon fulfillment center that processed the return item.
    """

    return_authorization_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the return authorization used to return this item. See ReturnAuthorization.
    """

    return_comment: str = attrs.field(
        kw_only=True,
    )
    """
    An optional comment about the return item.
    """

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier assigned to the item by the seller when the fulfillment order was created.
    """

    seller_return_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier assigned by the seller to the return item.
    """

    seller_return_reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    The return reason code assigned to the return item by the seller.
    """

    return_received_condition: "ReturnItemDisposition" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    status: "FulfillmentReturnItemStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    status_changed_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ReturnItemDisposition:

    pass


@attrs.define
class ReturnItemList:

    pass


@attrs.define
class ScheduledDeliveryInfo:

    delivery_time_zone: str = attrs.field(
        kw_only=True,
    )
    """
    The time zone of the destination address for the fulfillment order preview. Must be an IANA time zone name. Example: Asia/Tokyo.
    """

    delivery_windows: "DeliveryWindowList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShippingSpeedCategory:

    pass


@attrs.define
class ShippingSpeedCategoryList:

    pass


@attrs.define
class StringList:

    pass


@attrs.define
class Timestamp:

    pass


@attrs.define
class TrackingAddress:

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city.

    Extra fields:
    {'maxLength': 150}
    """

    country: str = attrs.field(
        kw_only=True,
    )
    """
    The country.

    Extra fields:
    {'maxLength': 6}
    """

    state: str = attrs.field(
        kw_only=True,
    )
    """
    The state.

    Extra fields:
    {'maxLength': 150}
    """

    pass


@attrs.define
class TrackingEvent:

    event_description: str = attrs.field(
        kw_only=True,
    )
    """
    A description for the corresponding event code.
    """

    event_address: "TrackingAddress" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    event_code: "EventCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    event_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TrackingEventList:

    pass


@attrs.define
class UnfulfillablePreviewItem:

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order item identifier created with a call to the getFulfillmentPreview operation.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.

    Extra fields:
    {'maxLength': 50}
    """

    item_unfulfillable_reasons: "StringList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class UnfulfillablePreviewItemList:

    pass


@attrs.define
class UpdateFulfillmentOrderItem:

    displayable_comment: str = attrs.field(
        kw_only=True,
    )
    """
    Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 250}
    """

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    Amazon's fulfillment network SKU of the item.
    """

    gift_message: str = attrs.field(
        kw_only=True,
    )
    """
    A message to the gift recipient, if applicable.

    Extra fields:
    {'maxLength': 512}
    """

    order_item_disposition: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates whether the item is sellable or unsellable.
    """

    seller_fulfillment_order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies the fulfillment order item to update. Created with a previous call to the createFulfillmentOrder operation.

    Extra fields:
    {'maxLength': 50}
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    per_unit_declared_value: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    per_unit_tax: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "Quantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class UpdateFulfillmentOrderItemList:

    pass


@attrs.define
class UpdateFulfillmentOrderRequest:

    displayable_order_comment: str = attrs.field(
        kw_only=True,
    )
    """
    Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.

    Extra fields:
    {'maxLength': 1000}
    """

    displayable_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.

    Extra fields:
    {'maxLength': 40}
    """

    feature_constraints: list["FeatureSettings"] = attrs.field(
        kw_only=True,
    )
    """
    A list of features and their fulfillment policies to apply to the order.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The marketplace the fulfillment order is placed against.
    """

    ship_from_country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
    """

    destination_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    displayable_order_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_action: "FulfillmentAction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fulfillment_policy: "FulfillmentPolicy" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    items: "UpdateFulfillmentOrderItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    notification_emails: "NotificationEmailList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_speed_category: "ShippingSpeedCategory" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class UpdateFulfillmentOrderResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Weight:

    unit: Union[Literal["KG"], Literal["KILOGRAMS"], Literal["LB"], Literal["POUNDS"]] = attrs.field(
        kw_only=True,
    )
    """
    The unit of weight.
    """

    value: str = attrs.field(
        kw_only=True,
    )
    """
    The weight value.
    """

    pass


class FulfillmentOutbound20200701Client(BaseClient):
    def cancel_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
    ):
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
        response = self._parse_args_and_request(url, "PUT", values, self._cancel_fulfillment_order_params)
        return response

    _cancel_fulfillment_order_params = (("sellerFulfillmentOrderId", "path"),)  # name, param in

    def create_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        displayable_order_id: str,
        displayable_order_date: datetime,
        displayable_order_comment: str,
        shipping_speed_category: Union[
            Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
        ],
        destination_address: dict[str, Any],
        items: list["CreateFulfillmentOrderItem"],
        marketplace_id: str = None,
        delivery_window: dict[str, Any] = None,
        fulfillment_action: Union[Literal["Ship"], Literal["Hold"]] = None,
        fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]] = None,
        cod_settings: dict[str, Any] = None,
        ship_from_country_code: str = None,
        notification_emails: list[str] = None,
        feature_constraints: list["FeatureSettings"] = None,
    ):
        """
        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The marketplace the fulfillment order is placed against.
            seller_fulfillment_order_id: A fulfillment order identifier that the seller creates to track their fulfillment order. The SellerFulfillmentOrderId must be unique for each fulfillment order that a seller creates. If the seller's system already creates unique order identifiers, then these might be good values for them to use.
            displayable_order_id: A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.
                The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed.
            displayable_order_date: no description.
            displayable_order_comment: Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.
            shipping_speed_category: The shipping method used for the fulfillment order.
            delivery_window: The time range within which a Scheduled Delivery fulfillment order should be delivered.
            destination_address: A physical address.
            fulfillment_action: Specifies whether the fulfillment order should ship now or have an order hold put on it.
            fulfillment_policy: The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
            cod_settings: The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
            ship_from_country_code: The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
            notification_emails: A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
            feature_constraints: A list of features and their fulfillment policies to apply to the order.
            items: An array of item information for creating a fulfillment order.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders"
        values = (
            marketplace_id,
            seller_fulfillment_order_id,
            displayable_order_id,
            displayable_order_date,
            displayable_order_comment,
            shipping_speed_category,
            delivery_window,
            destination_address,
            fulfillment_action,
            fulfillment_policy,
            cod_settings,
            ship_from_country_code,
            notification_emails,
            feature_constraints,
            items,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_fulfillment_order_params)
        return response

    _create_fulfillment_order_params = (  # name, param in
        ("marketplaceId", "body"),
        ("sellerFulfillmentOrderId", "body"),
        ("displayableOrderId", "body"),
        ("displayableOrderDate", "body"),
        ("displayableOrderComment", "body"),
        ("shippingSpeedCategory", "body"),
        ("deliveryWindow", "body"),
        ("destinationAddress", "body"),
        ("fulfillmentAction", "body"),
        ("fulfillmentPolicy", "body"),
        ("codSettings", "body"),
        ("shipFromCountryCode", "body"),
        ("notificationEmails", "body"),
        ("featureConstraints", "body"),
        ("items", "body"),
    )

    def create_fulfillment_return(
        self,
        seller_fulfillment_order_id: str,
        items: list["CreateReturnItem"],
    ):
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
        response = self._parse_args_and_request(url, "PUT", values, self._create_fulfillment_return_params)
        return response

    _create_fulfillment_return_params = (  # name, param in
        ("sellerFulfillmentOrderId", "path"),
        ("items", "body"),
    )

    def get_feature_inventory(
        self,
        marketplace_id: str,
        feature_name: str,
        next_token: str = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_feature_inventory_params)
        return response

    _get_feature_inventory_params = (  # name, param in
        ("marketplaceId", "query"),
        ("featureName", "path"),
        ("nextToken", "query"),
    )

    def get_feature_sku(
        self,
        marketplace_id: str,
        feature_name: str,
        seller_sku: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_feature_sku_params)
        return response

    _get_feature_sku_params = (  # name, param in
        ("marketplaceId", "query"),
        ("featureName", "path"),
        ("sellerSku", "path"),
    )

    def get_features(
        self,
        marketplace_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_features_params)
        return response

    _get_features_params = (("marketplaceId", "query"),)  # name, param in

    def get_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_fulfillment_order_params)
        return response

    _get_fulfillment_order_params = (("sellerFulfillmentOrderId", "path"),)  # name, param in

    def get_fulfillment_preview(
        self,
        address: dict[str, Any],
        items: list["GetFulfillmentPreviewItem"],
        marketplace_id: str = None,
        shipping_speed_categories: list["ShippingSpeedCategory"] = None,
        include_codfulfillment_preview: bool = None,
        include_delivery_windows: bool = None,
        feature_constraints: list["FeatureSettings"] = None,
    ):
        """
        Returns a list of fulfillment order previews based on shipping criteria that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: The marketplace the fulfillment order is placed against.
            address: A physical address.
            items: An array of fulfillment preview item information.
            shipping_speed_categories: no description.
            include_codfulfillment_preview: Specifies whether to return fulfillment order previews that are for COD (Cash On Delivery).
                Possible values:
                * true - Returns all fulfillment order previews (both for COD and not for COD).
                * false - Returns only fulfillment order previews that are not for COD.
            include_delivery_windows: Specifies whether to return the ScheduledDeliveryInfo response object, which contains the available delivery windows for a Scheduled Delivery. The ScheduledDeliveryInfo response object can only be returned for fulfillment order previews with ShippingSpeedCategories = ScheduledDelivery.
            feature_constraints: A list of features and their fulfillment policies to apply to the order.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/preview"
        values = (
            marketplace_id,
            address,
            items,
            shipping_speed_categories,
            include_codfulfillment_preview,
            include_delivery_windows,
            feature_constraints,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_fulfillment_preview_params)
        return response

    _get_fulfillment_preview_params = (  # name, param in
        ("marketplaceId", "body"),
        ("address", "body"),
        ("items", "body"),
        ("shippingSpeedCategories", "body"),
        ("includeCODFulfillmentPreview", "body"),
        ("includeDeliveryWindows", "body"),
        ("featureConstraints", "body"),
    )

    def get_package_tracking_details(
        self,
        package_number: int,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_package_tracking_details_params)
        return response

    _get_package_tracking_details_params = (("packageNumber", "query"),)  # name, param in

    def list_all_fulfillment_orders(
        self,
        query_start_date: datetime = None,
        next_token: str = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._list_all_fulfillment_orders_params)
        return response

    _list_all_fulfillment_orders_params = (  # name, param in
        ("queryStartDate", "query"),
        ("nextToken", "query"),
    )

    def list_return_reason_codes(
        self,
        seller_sku: str,
        language: str,
        marketplace_id: str = None,
        seller_fulfillment_order_id: str = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._list_return_reason_codes_params)
        return response

    _list_return_reason_codes_params = (  # name, param in
        ("sellerSku", "query"),
        ("marketplaceId", "query"),
        ("sellerFulfillmentOrderId", "query"),
        ("language", "query"),
    )

    def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        marketplace_id: str = None,
        displayable_order_id: str = None,
        displayable_order_date: datetime = None,
        displayable_order_comment: str = None,
        shipping_speed_category: Union[
            Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
        ] = None,
        destination_address: dict[str, Any] = None,
        fulfillment_action: Union[Literal["Ship"], Literal["Hold"]] = None,
        fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]] = None,
        ship_from_country_code: str = None,
        notification_emails: list[str] = None,
        feature_constraints: list["FeatureSettings"] = None,
        items: list["UpdateFulfillmentOrderItem"] = None,
    ):
        """
        Updates and/or requests shipment for a fulfillment order with an order hold on it.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_fulfillment_order_id: The identifier assigned to the item by the seller when the fulfillment order was created.
            marketplace_id: The marketplace the fulfillment order is placed against.
            displayable_order_id: A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.
            displayable_order_date: no description.
            displayable_order_comment: Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.
            shipping_speed_category: The shipping method used for the fulfillment order.
            destination_address: A physical address.
            fulfillment_action: Specifies whether the fulfillment order should ship now or have an order hold put on it.
            fulfillment_policy: The FulfillmentPolicy value specified when you submitted the createFulfillmentOrder operation.
            ship_from_country_code: The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
            notification_emails: A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
            feature_constraints: A list of features and their fulfillment policies to apply to the order.
            items: An array of fulfillment order item information for updating a fulfillment order.
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}"
        values = (
            seller_fulfillment_order_id,
            marketplace_id,
            displayable_order_id,
            displayable_order_date,
            displayable_order_comment,
            shipping_speed_category,
            destination_address,
            fulfillment_action,
            fulfillment_policy,
            ship_from_country_code,
            notification_emails,
            feature_constraints,
            items,
        )
        response = self._parse_args_and_request(url, "PUT", values, self._update_fulfillment_order_params)
        return response

    _update_fulfillment_order_params = (  # name, param in
        ("sellerFulfillmentOrderId", "path"),
        ("marketplaceId", "body"),
        ("displayableOrderId", "body"),
        ("displayableOrderDate", "body"),
        ("displayableOrderComment", "body"),
        ("shippingSpeedCategory", "body"),
        ("destinationAddress", "body"),
        ("fulfillmentAction", "body"),
        ("fulfillmentPolicy", "body"),
        ("shipFromCountryCode", "body"),
        ("notificationEmails", "body"),
        ("featureConstraints", "body"),
        ("items", "body"),
    )
