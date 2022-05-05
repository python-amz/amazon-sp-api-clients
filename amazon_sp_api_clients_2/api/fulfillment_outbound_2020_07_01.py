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

    address_line1: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    address_line2: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    address_line3: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    city: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    country_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    district_or_county: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    phone: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    postal_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    state_or_region: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class CODSettings:

    is_cod_required: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    cod_charge: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    cod_charge_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    shipping_charge: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    shipping_charge_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class CancelFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class CreateFulfillmentOrderItem:

    displayable_comment: str
    # {'type': 'string', 'maxLength': 250, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_network_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    gift_message: str
    # {'type': 'string', 'maxLength': 512, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    per_unit_declared_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    per_unit_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    per_unit_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    pass


@attrs.define
class CreateFulfillmentOrderItemList:

    pass


@attrs.define
class CreateFulfillmentOrderRequest:

    displayable_order_comment: str
    # {'type': 'string', 'maxLength': 1000, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    displayable_order_id: str
    # {'type': 'string', 'maxLength': 40, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    feature_constraints: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_id: str
    # {'type': 'string', 'maxLength': 40, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    ship_from_country_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    cod_settings: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/CODSettings'}
    delivery_window: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/DeliveryWindow'}
    destination_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Address'}
    displayable_order_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    fulfillment_action: Union[Literal["Ship"], Literal["Hold"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentAction'}
    fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentPolicy'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/CreateFulfillmentOrderItemList'}
    notification_emails: list[str]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/NotificationEmailList'}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ShippingSpeedCategory'}
    pass


@attrs.define
class CreateFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class CreateFulfillmentReturnRequest:

    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/CreateReturnItemList'}
    pass


@attrs.define
class CreateFulfillmentReturnResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/CreateFulfillmentReturnResult'}
    pass


@attrs.define
class CreateFulfillmentReturnResult:

    invalid_return_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/InvalidReturnItemList'}
    return_authorizations: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ReturnAuthorizationList'}
    return_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ReturnItemList'}
    pass


@attrs.define
class CreateReturnItem:

    amazon_shipment_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    return_comment: str
    # {'type': 'string', 'maxLength': 1000, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    return_reason_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_return_item_id: str
    # {'type': 'string', 'maxLength': 80, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

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

    end_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    start_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class DeliveryWindowList:

    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class EventCode:

    pass


@attrs.define
class Feature:

    feature_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    feature_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_eligible: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class FeatureSettings:

    feature_fulfillment_policy: Union[Literal["Required"], Literal["NotRequired"]]
    # {'type': 'string', 'enum': ['Required', 'NotRequired'], 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    feature_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class FeatureSku:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fn_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    overlapping_skus: list[str]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    sku_count: Union[float, int]
    # {'type': 'number', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

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
    ]
    # {'type': 'string', 'enum': ['FBAPerUnitFulfillmentFee', 'FBAPerOrderFulfillmentFee', 'FBATransportationFee', 'FBAFulfillmentCODFee'], 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class FeeList:

    pass


@attrs.define
class FulfillmentAction:

    pass


@attrs.define
class FulfillmentOrder:

    displayable_order_comment: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    displayable_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    feature_constraints: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    cod_settings: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/CODSettings'}
    delivery_window: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/DeliveryWindow'}
    destination_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Address'}
    displayable_order_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    fulfillment_action: Union[Literal["Ship"], Literal["Hold"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentAction'}
    fulfillment_order_status: Union[
        Literal["New"],
        Literal["Received"],
        Literal["Planning"],
        Literal["Processing"],
        Literal["Cancelled"],
        Literal["Complete"],
        Literal["CompletePartialled"],
        Literal["Unfulfillable"],
        Literal["Invalid"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentOrderStatus'}
    fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentPolicy'}
    notification_emails: list[str]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/NotificationEmailList'}
    received_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ShippingSpeedCategory'}
    status_updated_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class FulfillmentOrderItem:

    displayable_comment: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_network_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    gift_message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    order_item_disposition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    cancelled_quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    estimated_arrival_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    estimated_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    per_unit_declared_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    per_unit_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    per_unit_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    unfulfillable_quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
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

    feature_constraints: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    is_codcapable: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    is_fulfillable: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    estimated_fees: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FeeList'}
    estimated_shipping_weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Weight'}
    fulfillment_preview_shipments: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentPreviewShipmentList'}
    order_unfulfillable_reasons: list[str]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/StringList'}
    scheduled_delivery_info: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ScheduledDeliveryInfo'}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ShippingSpeedCategory'}
    unfulfillable_preview_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/UnfulfillablePreviewItemList'}
    pass


@attrs.define
class FulfillmentPreviewItem:

    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    shipping_weight_calculation_method: Union[Literal["Package"], Literal["Dimensional"]]
    # {'type': 'string', 'enum': ['Package', 'Dimensional'], 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    estimated_shipping_weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Weight'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    pass


@attrs.define
class FulfillmentPreviewItemList:

    pass


@attrs.define
class FulfillmentPreviewList:

    pass


@attrs.define
class FulfillmentPreviewShipment:

    shipping_notes: list[str]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}

    earliest_arrival_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    earliest_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    fulfillment_preview_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentPreviewItemList'}
    latest_arrival_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    latest_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class FulfillmentPreviewShipmentList:

    pass


@attrs.define
class FulfillmentReturnItemStatus:

    pass


@attrs.define
class FulfillmentShipment:

    amazon_shipment_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_center_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_shipment_status: Union[
        Literal["PENDING"], Literal["SHIPPED"], Literal["CANCELLED_BY_FULFILLER"], Literal["CANCELLED_BY_SELLER"]
    ]
    # {'type': 'string', 'enum': ['PENDING', 'SHIPPED', 'CANCELLED_BY_FULFILLER', 'CANCELLED_BY_SELLER'], 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    shipping_notes: list[str]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}

    estimated_arrival_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    fulfillment_shipment_item: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentShipmentItemList'}
    fulfillment_shipment_package: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentShipmentPackageList'}
    shipping_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class FulfillmentShipmentItem:

    package_number: int
    # {'schema_format': 'int32', 'type': 'integer', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    serial_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    pass


@attrs.define
class FulfillmentShipmentItemList:

    pass


@attrs.define
class FulfillmentShipmentList:

    pass


@attrs.define
class FulfillmentShipmentPackage:

    carrier_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    package_number: int
    # {'schema_format': 'int32', 'type': 'integer', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    tracking_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    estimated_arrival_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class FulfillmentShipmentPackageList:

    pass


@attrs.define
class GetFeatureInventoryResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/GetFeatureInventoryResult'}
    pass


@attrs.define
class GetFeatureInventoryResult:

    feature_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    feature_skus: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FeatureSku')}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    next_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class GetFeatureSkuResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/GetFeatureSkuResult'}
    pass


@attrs.define
class GetFeatureSkuResult:

    feature_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    ineligible_reasons: list[str]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}
    is_eligible: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    sku_info: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FeatureSku'}
    pass


@attrs.define
class GetFeaturesResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/GetFeaturesResult'}
    pass


@attrs.define
class GetFeaturesResult:

    features: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Features'}
    pass


@attrs.define
class GetFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/GetFulfillmentOrderResult'}
    pass


@attrs.define
class GetFulfillmentOrderResult:

    fulfillment_order: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentOrder'}
    fulfillment_order_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentOrderItemList'}
    fulfillment_shipments: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentShipmentList'}
    return_authorizations: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ReturnAuthorizationList'}
    return_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ReturnItemList'}
    pass


@attrs.define
class GetFulfillmentPreviewItem:

    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    per_unit_declared_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    pass


@attrs.define
class GetFulfillmentPreviewItemList:

    pass


@attrs.define
class GetFulfillmentPreviewRequest:

    feature_constraints: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    include_codfulfillment_preview: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    include_delivery_windows: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Address'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/GetFulfillmentPreviewItemList'}
    shipping_speed_categories: list[
        Union[Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]]
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ShippingSpeedCategoryList'}
    pass


@attrs.define
class GetFulfillmentPreviewResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/GetFulfillmentPreviewResult'}
    pass


@attrs.define
class GetFulfillmentPreviewResult:

    fulfillment_previews: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentPreviewList'}
    pass


@attrs.define
class GetPackageTrackingDetailsResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/PackageTrackingDetails'}
    pass


@attrs.define
class InvalidItemReason:

    description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    invalid_item_reason_code: Union[
        Literal["InvalidValues"],
        Literal["DuplicateRequest"],
        Literal["NoCompletedShipItems"],
        Literal["NoReturnableQuantity"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/InvalidItemReasonCode'}
    pass


@attrs.define
class InvalidItemReasonCode:

    pass


@attrs.define
class InvalidReturnItem:

    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_return_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    invalid_item_reason: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/InvalidItemReason'}
    pass


@attrs.define
class InvalidReturnItemList:

    pass


@attrs.define
class ListAllFulfillmentOrdersResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ListAllFulfillmentOrdersResult'}
    pass


@attrs.define
class ListAllFulfillmentOrdersResult:

    fulfillment_orders: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FulfillmentOrder')}
    next_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class ListReturnReasonCodesResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ListReturnReasonCodesResult'}
    pass


@attrs.define
class ListReturnReasonCodesResult:

    reason_code_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ReasonCodeDetailsList'}
    pass


@attrs.define
class Money:

    currency_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    value: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class NotificationEmailList:

    pass


@attrs.define
class PackageTrackingDetails:

    carrier_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    carrier_phone_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    carrier_url: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    current_status_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    customer_tracking_link: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    package_number: int
    # {'schema_format': 'int32', 'type': 'integer', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    signed_for_by: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    tracking_number: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    additional_location_info: Union[
        Literal["AS_INSTRUCTED"],
        Literal["CARPORT"],
        Literal["CUSTOMER_PICKUP"],
        Literal["DECK"],
        Literal["DOOR_PERSON"],
        Literal["FRONT_DESK"],
        Literal["FRONT_DOOR"],
        Literal["GARAGE"],
        Literal["GUARD"],
        Literal["MAIL_ROOM"],
        Literal["MAIL_SLOT"],
        Literal["MAILBOX"],
        Literal["MC_BOY"],
        Literal["MC_GIRL"],
        Literal["MC_MAN"],
        Literal["MC_WOMAN"],
        Literal["NEIGHBOR"],
        Literal["OFFICE"],
        Literal["OUTBUILDING"],
        Literal["PATIO"],
        Literal["PORCH"],
        Literal["REAR_DOOR"],
        Literal["RECEPTIONIST"],
        Literal["RECEIVER"],
        Literal["SECURE_LOCATION"],
        Literal["SIDE_DOOR"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/AdditionalLocationInfo'}
    current_status: Union[
        Literal["IN_TRANSIT"],
        Literal["DELIVERED"],
        Literal["RETURNING"],
        Literal["RETURNED"],
        Literal["UNDELIVERABLE"],
        Literal["DELAYED"],
        Literal["AVAILABLE_FOR_PICKUP"],
        Literal["CUSTOMER_ACTION"],
        Literal["UNKNOWN"],
        Literal["OUT_FOR_DELIVERY"],
        Literal["DELIVERY_ATTEMPTED"],
        Literal["PICKUP_SUCCESSFUL"],
        Literal["PICKUP_CANCELLED"],
        Literal["PICKUP_ATTEMPTED"],
        Literal["PICKUP_SCHEDULED"],
        Literal["RETURN_REQUEST_ACCEPTED"],
        Literal["REFUND_ISSUED"],
        Literal["RETURN_RECEIVED_IN_FC"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/CurrentStatus'}
    estimated_arrival_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    ship_to_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/TrackingAddress'}
    tracking_events: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/TrackingEventList'}
    pass


@attrs.define
class Quantity:

    pass


@attrs.define
class ReasonCodeDetails:

    description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    return_reason_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    translated_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class ReasonCodeDetailsList:

    pass


@attrs.define
class ReturnAuthorization:

    amazon_rma_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_center_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    return_authorization_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    rma_page_url: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    return_to_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class ReturnAuthorizationList:

    pass


@attrs.define
class ReturnItem:

    amazon_return_reason_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    amazon_shipment_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_center_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    return_authorization_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    return_comment: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_return_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_return_reason_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    return_received_condition: Union[
        Literal["Sellable"],
        Literal["Defective"],
        Literal["CustomerDamaged"],
        Literal["CarrierDamaged"],
        Literal["FulfillerDamaged"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ReturnItemDisposition'}
    status: Union[Literal["New"], Literal["Processed"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentReturnItemStatus'}
    status_changed_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class ReturnItemDisposition:

    pass


@attrs.define
class ReturnItemList:

    pass


@attrs.define
class ScheduledDeliveryInfo:

    delivery_time_zone: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    delivery_windows: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/DeliveryWindowList'}
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

    city: str
    # {'type': 'string', 'maxLength': 150, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    country: str
    # {'type': 'string', 'maxLength': 6, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    state: str
    # {'type': 'string', 'maxLength': 150, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    pass


@attrs.define
class TrackingEvent:

    event_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    event_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/TrackingAddress'}
    event_code: Union[
        Literal["EVENT_101"],
        Literal["EVENT_102"],
        Literal["EVENT_201"],
        Literal["EVENT_202"],
        Literal["EVENT_203"],
        Literal["EVENT_204"],
        Literal["EVENT_205"],
        Literal["EVENT_206"],
        Literal["EVENT_301"],
        Literal["EVENT_302"],
        Literal["EVENT_304"],
        Literal["EVENT_306"],
        Literal["EVENT_307"],
        Literal["EVENT_308"],
        Literal["EVENT_309"],
        Literal["EVENT_401"],
        Literal["EVENT_402"],
        Literal["EVENT_403"],
        Literal["EVENT_404"],
        Literal["EVENT_405"],
        Literal["EVENT_406"],
        Literal["EVENT_407"],
        Literal["EVENT_408"],
        Literal["EVENT_409"],
        Literal["EVENT_411"],
        Literal["EVENT_412"],
        Literal["EVENT_413"],
        Literal["EVENT_414"],
        Literal["EVENT_415"],
        Literal["EVENT_416"],
        Literal["EVENT_417"],
        Literal["EVENT_418"],
        Literal["EVENT_419"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/EventCode'}
    event_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    pass


@attrs.define
class TrackingEventList:

    pass


@attrs.define
class UnfulfillablePreviewItem:

    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    item_unfulfillable_reasons: list[str]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/StringList'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    pass


@attrs.define
class UnfulfillablePreviewItemList:

    pass


@attrs.define
class UpdateFulfillmentOrderItem:

    displayable_comment: str
    # {'type': 'string', 'maxLength': 250, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    fulfillment_network_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    gift_message: str
    # {'type': 'string', 'maxLength': 512, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    order_item_disposition: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_fulfillment_order_item_id: str
    # {'type': 'string', 'maxLength': 50, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    per_unit_declared_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    per_unit_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    per_unit_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Money'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Quantity'}
    pass


@attrs.define
class UpdateFulfillmentOrderItemList:

    pass


@attrs.define
class UpdateFulfillmentOrderRequest:

    displayable_order_comment: str
    # {'type': 'string', 'maxLength': 1000, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    displayable_order_id: str
    # {'type': 'string', 'maxLength': 40, 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    feature_constraints: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    ship_from_country_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

    destination_address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Address'}
    displayable_order_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/Timestamp'}
    fulfillment_action: Union[Literal["Ship"], Literal["Hold"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentAction'}
    fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/FulfillmentPolicy'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/UpdateFulfillmentOrderItemList'}
    notification_emails: list[str]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/NotificationEmailList'}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ShippingSpeedCategory'}
    pass


@attrs.define
class UpdateFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class Weight:

    unit: Union[Literal["KG"], Literal["KILOGRAMS"], Literal["LB"], Literal["POUNDS"]]
    # {'type': 'string', 'enum': ['KG', 'KILOGRAMS', 'LB', 'POUNDS'], 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}
    value: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x00000181BEC6B310>}

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
        items: list[dict[str, Any]],
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
        feature_constraints: list[dict[str, Any]] = None,
        items: list[dict[str, Any]] = None,
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
