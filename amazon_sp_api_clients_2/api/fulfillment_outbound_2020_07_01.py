"""
Selling Partner APIs for Fulfillment Outbound
=============================================================================================

The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
API Version: 2020-07-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Any, Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AdditionalLocationInfo:
    pass


@attrs.define
class Address:
    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    district_or_county: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class CODSettings:
    is_cod_required: bool = attrs.field()

    cod_charge: "Money" = attrs.field()
    cod_charge_tax: "Money" = attrs.field()
    shipping_charge: "Money" = attrs.field()
    shipping_charge_tax: "Money" = attrs.field()
    pass


@attrs.define
class CancelFulfillmentOrderResponse:
    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class CreateFulfillmentOrderItem:
    displayable_comment: str = attrs.field()
    # {'maxLength': 250}
    fulfillment_network_sku: str = attrs.field()
    gift_message: str = attrs.field()
    # {'maxLength': 512}
    seller_fulfillment_order_item_id: str = attrs.field()
    # {'maxLength': 50}
    seller_sku: str = attrs.field()
    # {'maxLength': 50}

    per_unit_declared_value: "Money" = attrs.field()
    per_unit_price: "Money" = attrs.field()
    per_unit_tax: "Money" = attrs.field()
    quantity: "Quantity" = attrs.field()
    pass


@attrs.define
class CreateFulfillmentOrderItemList:
    pass


@attrs.define
class CreateFulfillmentOrderRequest:
    displayable_order_comment: str = attrs.field()
    # {'maxLength': 1000}
    displayable_order_id: str = attrs.field()
    # {'maxLength': 40}
    feature_constraints: list["FeatureSettings"] = attrs.field()
    marketplace_id: str = attrs.field()
    seller_fulfillment_order_id: str = attrs.field()
    # {'maxLength': 40}
    ship_from_country_code: str = attrs.field()

    cod_settings: "CODSettings" = attrs.field()
    delivery_window: "DeliveryWindow" = attrs.field()
    destination_address: "Address" = attrs.field()
    displayable_order_date: "Timestamp" = attrs.field()
    fulfillment_action: "FulfillmentAction" = attrs.field()
    fulfillment_policy: "FulfillmentPolicy" = attrs.field()
    items: "CreateFulfillmentOrderItemList" = attrs.field()
    notification_emails: "NotificationEmailList" = attrs.field()
    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    pass


@attrs.define
class CreateFulfillmentOrderResponse:
    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class CreateFulfillmentReturnRequest:
    items: "CreateReturnItemList" = attrs.field()
    pass


@attrs.define
class CreateFulfillmentReturnResponse:
    errors: "ErrorList" = attrs.field()
    payload: "CreateFulfillmentReturnResult" = attrs.field()
    pass


@attrs.define
class CreateFulfillmentReturnResult:
    invalid_return_items: "InvalidReturnItemList" = attrs.field()
    return_authorizations: "ReturnAuthorizationList" = attrs.field()
    return_items: "ReturnItemList" = attrs.field()
    pass


@attrs.define
class CreateReturnItem:
    amazon_shipment_id: str = attrs.field()
    return_comment: str = attrs.field()
    # {'maxLength': 1000}
    return_reason_code: str = attrs.field()
    seller_fulfillment_order_item_id: str = attrs.field()
    seller_return_item_id: str = attrs.field()
    # {'maxLength': 80}

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
    end_date: "Timestamp" = attrs.field()
    start_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class DeliveryWindowList:
    pass


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class EventCode:
    pass


@attrs.define
class Feature:
    feature_description: str = attrs.field()
    feature_name: str = attrs.field()
    seller_eligible: bool = attrs.field()

    pass


@attrs.define
class FeatureSettings:
    feature_fulfillment_policy: Union[Literal["Required"], Literal["NotRequired"]] = attrs.field()
    feature_name: str = attrs.field()

    pass


@attrs.define
class FeatureSku:
    asin: str = attrs.field()
    fn_sku: str = attrs.field()
    overlapping_skus: list[str] = attrs.field()
    seller_sku: str = attrs.field()
    sku_count: Union[float, int] = attrs.field()

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
    ] = attrs.field()

    amount: "Money" = attrs.field()
    pass


@attrs.define
class FeeList:
    pass


@attrs.define
class FulfillmentAction:
    pass


@attrs.define
class FulfillmentOrder:
    displayable_order_comment: str = attrs.field()
    displayable_order_id: str = attrs.field()
    feature_constraints: list["FeatureSettings"] = attrs.field()
    marketplace_id: str = attrs.field()
    seller_fulfillment_order_id: str = attrs.field()

    cod_settings: "CODSettings" = attrs.field()
    delivery_window: "DeliveryWindow" = attrs.field()
    destination_address: "Address" = attrs.field()
    displayable_order_date: "Timestamp" = attrs.field()
    fulfillment_action: "FulfillmentAction" = attrs.field()
    fulfillment_order_status: "FulfillmentOrderStatus" = attrs.field()
    fulfillment_policy: "FulfillmentPolicy" = attrs.field()
    notification_emails: "NotificationEmailList" = attrs.field()
    received_date: "Timestamp" = attrs.field()
    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    status_updated_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class FulfillmentOrderItem:
    displayable_comment: str = attrs.field()
    fulfillment_network_sku: str = attrs.field()
    gift_message: str = attrs.field()
    order_item_disposition: str = attrs.field()
    seller_fulfillment_order_item_id: str = attrs.field()
    seller_sku: str = attrs.field()

    cancelled_quantity: "Quantity" = attrs.field()
    estimated_arrival_date: "Timestamp" = attrs.field()
    estimated_ship_date: "Timestamp" = attrs.field()
    per_unit_declared_value: "Money" = attrs.field()
    per_unit_price: "Money" = attrs.field()
    per_unit_tax: "Money" = attrs.field()
    quantity: "Quantity" = attrs.field()
    unfulfillable_quantity: "Quantity" = attrs.field()
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
    feature_constraints: list["FeatureSettings"] = attrs.field()
    is_codcapable: bool = attrs.field()
    is_fulfillable: bool = attrs.field()
    marketplace_id: str = attrs.field()

    estimated_fees: "FeeList" = attrs.field()
    estimated_shipping_weight: "Weight" = attrs.field()
    fulfillment_preview_shipments: "FulfillmentPreviewShipmentList" = attrs.field()
    order_unfulfillable_reasons: "StringList" = attrs.field()
    scheduled_delivery_info: "ScheduledDeliveryInfo" = attrs.field()
    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    unfulfillable_preview_items: "UnfulfillablePreviewItemList" = attrs.field()
    pass


@attrs.define
class FulfillmentPreviewItem:
    seller_fulfillment_order_item_id: str = attrs.field()
    seller_sku: str = attrs.field()
    shipping_weight_calculation_method: Union[Literal["Package"], Literal["Dimensional"]] = attrs.field()

    estimated_shipping_weight: "Weight" = attrs.field()
    quantity: "Quantity" = attrs.field()
    pass


@attrs.define
class FulfillmentPreviewItemList:
    pass


@attrs.define
class FulfillmentPreviewList:
    pass


@attrs.define
class FulfillmentPreviewShipment:
    shipping_notes: list[str] = attrs.field()

    earliest_arrival_date: "Timestamp" = attrs.field()
    earliest_ship_date: "Timestamp" = attrs.field()
    fulfillment_preview_items: "FulfillmentPreviewItemList" = attrs.field()
    latest_arrival_date: "Timestamp" = attrs.field()
    latest_ship_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class FulfillmentPreviewShipmentList:
    pass


@attrs.define
class FulfillmentReturnItemStatus:
    pass


@attrs.define
class FulfillmentShipment:
    amazon_shipment_id: str = attrs.field()
    fulfillment_center_id: str = attrs.field()
    fulfillment_shipment_status: Union[
        Literal["PENDING"], Literal["SHIPPED"], Literal["CANCELLED_BY_FULFILLER"], Literal["CANCELLED_BY_SELLER"]
    ] = attrs.field()
    shipping_notes: list[str] = attrs.field()

    estimated_arrival_date: "Timestamp" = attrs.field()
    fulfillment_shipment_item: "FulfillmentShipmentItemList" = attrs.field()
    fulfillment_shipment_package: "FulfillmentShipmentPackageList" = attrs.field()
    shipping_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class FulfillmentShipmentItem:
    package_number: int = attrs.field()
    # {'schema_format': 'int32'}
    seller_fulfillment_order_item_id: str = attrs.field()
    seller_sku: str = attrs.field()
    serial_number: str = attrs.field()

    quantity: "Quantity" = attrs.field()
    pass


@attrs.define
class FulfillmentShipmentItemList:
    pass


@attrs.define
class FulfillmentShipmentList:
    pass


@attrs.define
class FulfillmentShipmentPackage:
    carrier_code: str = attrs.field()
    package_number: int = attrs.field()
    # {'schema_format': 'int32'}
    tracking_number: str = attrs.field()

    estimated_arrival_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class FulfillmentShipmentPackageList:
    pass


@attrs.define
class GetFeatureInventoryResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetFeatureInventoryResult" = attrs.field()
    pass


@attrs.define
class GetFeatureInventoryResult:
    feature_name: str = attrs.field()
    feature_skus: list["FeatureSku"] = attrs.field()
    marketplace_id: str = attrs.field()
    next_token: str = attrs.field()

    pass


@attrs.define
class GetFeatureSkuResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetFeatureSkuResult" = attrs.field()
    pass


@attrs.define
class GetFeatureSkuResult:
    feature_name: str = attrs.field()
    ineligible_reasons: list[str] = attrs.field()
    is_eligible: bool = attrs.field()
    marketplace_id: str = attrs.field()

    sku_info: "FeatureSku" = attrs.field()
    pass


@attrs.define
class GetFeaturesResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetFeaturesResult" = attrs.field()
    pass


@attrs.define
class GetFeaturesResult:
    features: "Features" = attrs.field()
    pass


@attrs.define
class GetFulfillmentOrderResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetFulfillmentOrderResult" = attrs.field()
    pass


@attrs.define
class GetFulfillmentOrderResult:
    fulfillment_order: "FulfillmentOrder" = attrs.field()
    fulfillment_order_items: "FulfillmentOrderItemList" = attrs.field()
    fulfillment_shipments: "FulfillmentShipmentList" = attrs.field()
    return_authorizations: "ReturnAuthorizationList" = attrs.field()
    return_items: "ReturnItemList" = attrs.field()
    pass


@attrs.define
class GetFulfillmentPreviewItem:
    seller_fulfillment_order_item_id: str = attrs.field()
    # {'maxLength': 50}
    seller_sku: str = attrs.field()
    # {'maxLength': 50}

    per_unit_declared_value: "Money" = attrs.field()
    quantity: "Quantity" = attrs.field()
    pass


@attrs.define
class GetFulfillmentPreviewItemList:
    pass


@attrs.define
class GetFulfillmentPreviewRequest:
    feature_constraints: list["FeatureSettings"] = attrs.field()
    include_codfulfillment_preview: bool = attrs.field()
    include_delivery_windows: bool = attrs.field()
    marketplace_id: str = attrs.field()

    address: "Address" = attrs.field()
    items: "GetFulfillmentPreviewItemList" = attrs.field()
    shipping_speed_categories: "ShippingSpeedCategoryList" = attrs.field()
    pass


@attrs.define
class GetFulfillmentPreviewResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetFulfillmentPreviewResult" = attrs.field()
    pass


@attrs.define
class GetFulfillmentPreviewResult:
    fulfillment_previews: "FulfillmentPreviewList" = attrs.field()
    pass


@attrs.define
class GetPackageTrackingDetailsResponse:
    errors: "ErrorList" = attrs.field()
    payload: "PackageTrackingDetails" = attrs.field()
    pass


@attrs.define
class InvalidItemReason:
    description: str = attrs.field()

    invalid_item_reason_code: "InvalidItemReasonCode" = attrs.field()
    pass


@attrs.define
class InvalidItemReasonCode:
    pass


@attrs.define
class InvalidReturnItem:
    seller_fulfillment_order_item_id: str = attrs.field()
    seller_return_item_id: str = attrs.field()

    invalid_item_reason: "InvalidItemReason" = attrs.field()
    pass


@attrs.define
class InvalidReturnItemList:
    pass


@attrs.define
class ListAllFulfillmentOrdersResponse:
    errors: "ErrorList" = attrs.field()
    payload: "ListAllFulfillmentOrdersResult" = attrs.field()
    pass


@attrs.define
class ListAllFulfillmentOrdersResult:
    fulfillment_orders: list["FulfillmentOrder"] = attrs.field()
    next_token: str = attrs.field()

    pass


@attrs.define
class ListReturnReasonCodesResponse:
    errors: "ErrorList" = attrs.field()
    payload: "ListReturnReasonCodesResult" = attrs.field()
    pass


@attrs.define
class ListReturnReasonCodesResult:
    reason_code_details: "ReasonCodeDetailsList" = attrs.field()
    pass


@attrs.define
class Money:
    currency_code: str = attrs.field()

    value: "Decimal" = attrs.field()
    pass


@attrs.define
class NotificationEmailList:
    pass


@attrs.define
class PackageTrackingDetails:
    carrier_code: str = attrs.field()
    carrier_phone_number: str = attrs.field()
    carrier_url: str = attrs.field()
    current_status_description: str = attrs.field()
    customer_tracking_link: str = attrs.field()
    package_number: int = attrs.field()
    # {'schema_format': 'int32'}
    signed_for_by: str = attrs.field()
    tracking_number: str = attrs.field()

    additional_location_info: "AdditionalLocationInfo" = attrs.field()
    current_status: "CurrentStatus" = attrs.field()
    estimated_arrival_date: "Timestamp" = attrs.field()
    ship_date: "Timestamp" = attrs.field()
    ship_to_address: "TrackingAddress" = attrs.field()
    tracking_events: "TrackingEventList" = attrs.field()
    pass


@attrs.define
class Quantity:
    pass


@attrs.define
class ReasonCodeDetails:
    description: str = attrs.field()
    return_reason_code: str = attrs.field()
    translated_description: str = attrs.field()

    pass


@attrs.define
class ReasonCodeDetailsList:
    pass


@attrs.define
class ReturnAuthorization:
    amazon_rma_id: str = attrs.field()
    fulfillment_center_id: str = attrs.field()
    return_authorization_id: str = attrs.field()
    rma_page_url: str = attrs.field()

    return_to_address: "Address" = attrs.field()
    pass


@attrs.define
class ReturnAuthorizationList:
    pass


@attrs.define
class ReturnItem:
    amazon_return_reason_code: str = attrs.field()
    amazon_shipment_id: str = attrs.field()
    fulfillment_center_id: str = attrs.field()
    return_authorization_id: str = attrs.field()
    return_comment: str = attrs.field()
    seller_fulfillment_order_item_id: str = attrs.field()
    seller_return_item_id: str = attrs.field()
    seller_return_reason_code: str = attrs.field()

    return_received_condition: "ReturnItemDisposition" = attrs.field()
    status: "FulfillmentReturnItemStatus" = attrs.field()
    status_changed_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class ReturnItemDisposition:
    pass


@attrs.define
class ReturnItemList:
    pass


@attrs.define
class ScheduledDeliveryInfo:
    delivery_time_zone: str = attrs.field()

    delivery_windows: "DeliveryWindowList" = attrs.field()
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
    city: str = attrs.field()
    # {'maxLength': 150}
    country: str = attrs.field()
    # {'maxLength': 6}
    state: str = attrs.field()
    # {'maxLength': 150}

    pass


@attrs.define
class TrackingEvent:
    event_description: str = attrs.field()

    event_address: "TrackingAddress" = attrs.field()
    event_code: "EventCode" = attrs.field()
    event_date: "Timestamp" = attrs.field()
    pass


@attrs.define
class TrackingEventList:
    pass


@attrs.define
class UnfulfillablePreviewItem:
    seller_fulfillment_order_item_id: str = attrs.field()
    # {'maxLength': 50}
    seller_sku: str = attrs.field()
    # {'maxLength': 50}

    item_unfulfillable_reasons: "StringList" = attrs.field()
    quantity: "Quantity" = attrs.field()
    pass


@attrs.define
class UnfulfillablePreviewItemList:
    pass


@attrs.define
class UpdateFulfillmentOrderItem:
    displayable_comment: str = attrs.field()
    # {'maxLength': 250}
    fulfillment_network_sku: str = attrs.field()
    gift_message: str = attrs.field()
    # {'maxLength': 512}
    order_item_disposition: str = attrs.field()
    seller_fulfillment_order_item_id: str = attrs.field()
    # {'maxLength': 50}
    seller_sku: str = attrs.field()

    per_unit_declared_value: "Money" = attrs.field()
    per_unit_price: "Money" = attrs.field()
    per_unit_tax: "Money" = attrs.field()
    quantity: "Quantity" = attrs.field()
    pass


@attrs.define
class UpdateFulfillmentOrderItemList:
    pass


@attrs.define
class UpdateFulfillmentOrderRequest:
    displayable_order_comment: str = attrs.field()
    # {'maxLength': 1000}
    displayable_order_id: str = attrs.field()
    # {'maxLength': 40}
    feature_constraints: list["FeatureSettings"] = attrs.field()
    marketplace_id: str = attrs.field()
    ship_from_country_code: str = attrs.field()

    destination_address: "Address" = attrs.field()
    displayable_order_date: "Timestamp" = attrs.field()
    fulfillment_action: "FulfillmentAction" = attrs.field()
    fulfillment_policy: "FulfillmentPolicy" = attrs.field()
    items: "UpdateFulfillmentOrderItemList" = attrs.field()
    notification_emails: "NotificationEmailList" = attrs.field()
    shipping_speed_category: "ShippingSpeedCategory" = attrs.field()
    pass


@attrs.define
class UpdateFulfillmentOrderResponse:
    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class Weight:
    unit: Union[Literal["KG"], Literal["KILOGRAMS"], Literal["LB"], Literal["POUNDS"]] = attrs.field()
    value: str = attrs.field()

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
    ):
        """
        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_fulfillment_order_params)
        return response

    _create_fulfillment_order_params = ()  # name, param in

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
    ):
        """
        Returns a list of fulfillment order previews based on shipping criteria that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/fba/outbound/2020-07-01/fulfillmentOrders/preview"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_fulfillment_preview_params)
        return response

    _get_fulfillment_preview_params = ()  # name, param in

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
            query_start_date: str = None,
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
            displayable_order_date: str = None,
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
