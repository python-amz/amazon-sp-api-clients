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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    district_or_county: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    pass


@attrs.define
class CODSettings:

    is_cod_required: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}

    cod_charge: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    cod_charge_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_charge: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_charge_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CancelFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateFulfillmentOrderItem:

    displayable_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 250}
    fulfillment_network_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    gift_message: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 512}
    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}

    per_unit_declared_value: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateFulfillmentOrderItemList:

    pass


@attrs.define
class CreateFulfillmentOrderRequest:

    displayable_order_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 1000}
    displayable_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 40}
    feature_constraints: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_fulfillment_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 40}
    ship_from_country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    cod_settings: dict[str, Any]
    # {'ref': '#/components/schemas/CODSettings', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    delivery_window: dict[str, Any]
    # {'ref': '#/components/schemas/DeliveryWindow', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    destination_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    displayable_order_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_action: Union[Literal["Ship"], Literal["Hold"]]
    # {'ref': '#/components/schemas/FulfillmentAction', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]]
    # {'ref': '#/components/schemas/FulfillmentPolicy', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/CreateFulfillmentOrderItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    notification_emails: list[str]
    # {'ref': '#/components/schemas/NotificationEmailList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'ref': '#/components/schemas/ShippingSpeedCategory', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateFulfillmentReturnRequest:

    items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/CreateReturnItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateFulfillmentReturnResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/CreateFulfillmentReturnResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateFulfillmentReturnResult:

    invalid_return_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/InvalidReturnItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    return_authorizations: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ReturnAuthorizationList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    return_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ReturnItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class CreateReturnItem:

    amazon_shipment_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    return_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 1000}
    return_reason_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_return_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 80}

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
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    start_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class DeliveryWindowList:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    feature_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_eligible: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}

    pass


@attrs.define
class FeatureSettings:

    feature_fulfillment_policy: Union[Literal["Required"], Literal["NotRequired"]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'enum': ['Required', 'NotRequired']}
    feature_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    pass


@attrs.define
class FeatureSku:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    fn_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    overlapping_skus: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    sku_count: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'number'}

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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'enum': ['FBAPerUnitFulfillmentFee', 'FBAPerOrderFulfillmentFee', 'FBATransportationFee', 'FBAFulfillmentCODFee']}

    amount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    displayable_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    feature_constraints: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_fulfillment_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    cod_settings: dict[str, Any]
    # {'ref': '#/components/schemas/CODSettings', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    delivery_window: dict[str, Any]
    # {'ref': '#/components/schemas/DeliveryWindow', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    destination_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    displayable_order_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_action: Union[Literal["Ship"], Literal["Hold"]]
    # {'ref': '#/components/schemas/FulfillmentAction', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'ref': '#/components/schemas/FulfillmentOrderStatus', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]]
    # {'ref': '#/components/schemas/FulfillmentPolicy', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    notification_emails: list[str]
    # {'ref': '#/components/schemas/NotificationEmailList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    received_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'ref': '#/components/schemas/ShippingSpeedCategory', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    status_updated_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class FulfillmentOrderItem:

    displayable_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    fulfillment_network_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    gift_message: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    order_item_disposition: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    cancelled_quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    estimated_arrival_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    estimated_ship_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_declared_value: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    unfulfillable_quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    is_codcapable: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}
    is_fulfillable: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    estimated_fees: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    estimated_shipping_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_preview_shipments: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentPreviewShipmentList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    order_unfulfillable_reasons: list[str]
    # {'ref': '#/components/schemas/StringList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    scheduled_delivery_info: dict[str, Any]
    # {'ref': '#/components/schemas/ScheduledDeliveryInfo', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'ref': '#/components/schemas/ShippingSpeedCategory', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    unfulfillable_preview_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/UnfulfillablePreviewItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class FulfillmentPreviewItem:

    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    shipping_weight_calculation_method: Union[Literal["Package"], Literal["Dimensional"]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'enum': ['Package', 'Dimensional']}

    estimated_shipping_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}

    earliest_arrival_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    earliest_ship_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_preview_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentPreviewItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    latest_arrival_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    latest_ship_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    fulfillment_center_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    fulfillment_shipment_status: Union[
        Literal["PENDING"], Literal["SHIPPED"], Literal["CANCELLED_BY_FULFILLER"], Literal["CANCELLED_BY_SELLER"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'enum': ['PENDING', 'SHIPPED', 'CANCELLED_BY_FULFILLER', 'CANCELLED_BY_SELLER']}
    shipping_notes: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}

    estimated_arrival_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_shipment_item: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentShipmentItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_shipment_package: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentShipmentPackageList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class FulfillmentShipmentItem:

    package_number: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'integer'}
    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    serial_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    package_number: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'integer'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    estimated_arrival_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class FulfillmentShipmentPackageList:

    pass


@attrs.define
class GetFeatureInventoryResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetFeatureInventoryResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFeatureInventoryResult:

    feature_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    feature_skus: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FeatureSku')}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    pass


@attrs.define
class GetFeatureSkuResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetFeatureSkuResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFeatureSkuResult:

    feature_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    ineligible_reasons: list[str]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}
    is_eligible: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    sku_info: dict[str, Any]
    # {'ref': '#/components/schemas/FeatureSku', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFeaturesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetFeaturesResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFeaturesResult:

    features: list[dict[str, Any]]
    # {'ref': '#/components/schemas/Features', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetFulfillmentOrderResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFulfillmentOrderResult:

    fulfillment_order: dict[str, Any]
    # {'ref': '#/components/schemas/FulfillmentOrder', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_order_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentOrderItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_shipments: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentShipmentList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    return_authorizations: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ReturnAuthorizationList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    return_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ReturnItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFulfillmentPreviewItem:

    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}

    per_unit_declared_value: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFulfillmentPreviewItemList:

    pass


@attrs.define
class GetFulfillmentPreviewRequest:

    feature_constraints: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    include_codfulfillment_preview: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}
    include_delivery_windows: bool
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'boolean'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/GetFulfillmentPreviewItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_speed_categories: list[
        Union[Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]]
    ]
    # {'ref': '#/components/schemas/ShippingSpeedCategoryList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFulfillmentPreviewResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetFulfillmentPreviewResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetFulfillmentPreviewResult:

    fulfillment_previews: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FulfillmentPreviewList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class GetPackageTrackingDetailsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/PackageTrackingDetails', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class InvalidItemReason:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    invalid_item_reason_code: Union[
        Literal["InvalidValues"],
        Literal["DuplicateRequest"],
        Literal["NoCompletedShipItems"],
        Literal["NoReturnableQuantity"],
    ]
    # {'ref': '#/components/schemas/InvalidItemReasonCode', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class InvalidItemReasonCode:

    pass


@attrs.define
class InvalidReturnItem:

    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_return_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    invalid_item_reason: dict[str, Any]
    # {'ref': '#/components/schemas/InvalidItemReason', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class InvalidReturnItemList:

    pass


@attrs.define
class ListAllFulfillmentOrdersResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ListAllFulfillmentOrdersResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class ListAllFulfillmentOrdersResult:

    fulfillment_orders: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FulfillmentOrder')}
    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    pass


@attrs.define
class ListReturnReasonCodesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ListReturnReasonCodesResult', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class ListReturnReasonCodesResult:

    reason_code_details: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ReasonCodeDetailsList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    value: str
    # {'ref': '#/components/schemas/Decimal', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class NotificationEmailList:

    pass


@attrs.define
class PackageTrackingDetails:

    carrier_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    carrier_phone_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    carrier_url: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    current_status_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    customer_tracking_link: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    package_number: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'integer'}
    signed_for_by: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

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
    # {'ref': '#/components/schemas/AdditionalLocationInfo', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'ref': '#/components/schemas/CurrentStatus', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    estimated_arrival_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    ship_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    ship_to_address: dict[str, Any]
    # {'ref': '#/components/schemas/TrackingAddress', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    tracking_events: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TrackingEventList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class Quantity:

    pass


@attrs.define
class ReasonCodeDetails:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    return_reason_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    translated_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    pass


@attrs.define
class ReasonCodeDetailsList:

    pass


@attrs.define
class ReturnAuthorization:

    amazon_rma_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    fulfillment_center_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    return_authorization_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    rma_page_url: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    return_to_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class ReturnAuthorizationList:

    pass


@attrs.define
class ReturnItem:

    amazon_return_reason_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    amazon_shipment_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    fulfillment_center_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    return_authorization_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    return_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_return_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_return_reason_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    return_received_condition: Union[
        Literal["Sellable"],
        Literal["Defective"],
        Literal["CustomerDamaged"],
        Literal["CarrierDamaged"],
        Literal["FulfillerDamaged"],
    ]
    # {'ref': '#/components/schemas/ReturnItemDisposition', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    status: Union[Literal["New"], Literal["Processed"]]
    # {'ref': '#/components/schemas/FulfillmentReturnItemStatus', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    status_changed_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    delivery_windows: list[dict[str, Any]]
    # {'ref': '#/components/schemas/DeliveryWindowList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 150}
    country: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 6}
    state: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 150}

    pass


@attrs.define
class TrackingEvent:

    event_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    event_address: dict[str, Any]
    # {'ref': '#/components/schemas/TrackingAddress', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
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
    # {'ref': '#/components/schemas/EventCode', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    event_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class TrackingEventList:

    pass


@attrs.define
class UnfulfillablePreviewItem:

    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}

    item_unfulfillable_reasons: list[str]
    # {'ref': '#/components/schemas/StringList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class UnfulfillablePreviewItemList:

    pass


@attrs.define
class UpdateFulfillmentOrderItem:

    displayable_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 250}
    fulfillment_network_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    gift_message: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 512}
    order_item_disposition: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    seller_fulfillment_order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 50}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    per_unit_declared_value: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    per_unit_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    quantity: int
    # {'ref': '#/components/schemas/Quantity', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class UpdateFulfillmentOrderItemList:

    pass


@attrs.define
class UpdateFulfillmentOrderRequest:

    displayable_order_comment: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 1000}
    displayable_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'maxLength': 40}
    feature_constraints: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/FeatureSettings')}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}
    ship_from_country_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

    destination_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    displayable_order_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_action: Union[Literal["Ship"], Literal["Hold"]]
    # {'ref': '#/components/schemas/FulfillmentAction', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    fulfillment_policy: Union[Literal["FillOrKill"], Literal["FillAll"], Literal["FillAllAvailable"]]
    # {'ref': '#/components/schemas/FulfillmentPolicy', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/UpdateFulfillmentOrderItemList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    notification_emails: list[str]
    # {'ref': '#/components/schemas/NotificationEmailList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    shipping_speed_category: Union[
        Literal["Standard"], Literal["Expedited"], Literal["Priority"], Literal["ScheduledDelivery"]
    ]
    # {'ref': '#/components/schemas/ShippingSpeedCategory', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class UpdateFulfillmentOrderResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>}
    pass


@attrs.define
class Weight:

    unit: Union[Literal["KG"], Literal["KILOGRAMS"], Literal["LB"], Literal["POUNDS"]]
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string', 'enum': ['KG', 'KILOGRAMS', 'LB', 'POUNDS']}
    value: str
    # {'generator': <__mp_main__.Generator object at 0x0000013BEBEBB310>, 'type': 'string'}

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
