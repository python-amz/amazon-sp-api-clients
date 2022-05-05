"""
Selling Partner API for Orders
=============================================================================================

The Selling Partner API for Orders helps you programmatically retrieve order information. These APIs let you develop fast, flexible, custom applications in areas like order synchronization, order research, and demand-based decision support tools.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    address_type: Union[Literal["Residential"], Literal["Commercial"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['Residential', 'Commercial'], 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    municipality: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class AutomatedShippingSettings:

    automated_carrier: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    automated_ship_method: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    has_automated_shipping_settings: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}

    pass


@attrs.define
class BuyerCustomizedInfoDetail:

    customized_url: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class BuyerInfo:

    buyer_county: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_email: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    buyer_tax_info: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerTaxInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class BuyerRequestedCancel:

    buyer_cancel_reason: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    is_buyer_requested_cancel: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}

    pass


@attrs.define
class BuyerTaxInfo:

    company_legal_name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    tax_classifications: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxClassification'), 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'array'}
    taxing_region: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class BuyerTaxInformation:

    buyer_business_address: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_legal_company_name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_tax_office: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_tax_registration_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FulfillmentInstruction:

    fulfillment_supply_source_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class GetOrderAddressResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrderAddress', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class GetOrderBuyerInfoResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrderBuyerInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class GetOrderItemsBuyerInfoResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrderItemsBuyerInfoList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class GetOrderItemsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrderItemsList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class GetOrderRegulatedInfoResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrderRegulatedInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class GetOrderResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Order', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class GetOrdersResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/OrdersList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class ItemBuyerInfo:

    gift_message_text: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    gift_wrap_level: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    buyer_customized_info: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerCustomizedInfoDetail', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    gift_wrap_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    gift_wrap_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class MarketplaceId:

    pass


@attrs.define
class MarketplaceTaxInfo:

    tax_classifications: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/TaxClassification'), 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'array'}

    pass


@attrs.define
class Money:

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class Order:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_invoice_preference: Union[Literal["INDIVIDUAL"], Literal["BUSINESS"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['INDIVIDUAL', 'BUSINESS'], 'type': 'string'}
    cba_displayable_shipping_label: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    earliest_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    earliest_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    easy_ship_shipment_status: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    fulfillment_channel: Union[Literal["MFN"], Literal["AFN"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['MFN', 'AFN'], 'type': 'string'}
    has_regulated_items: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_business_order: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_estimated_ship_date_set: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_global_express_enabled: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_iba: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_ispu: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_premium_order: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_prime: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_replacement_order: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_sold_by_ab: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    last_update_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    latest_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    latest_ship_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    number_of_items_shipped: int
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'integer'}
    number_of_items_unshipped: int
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'integer'}
    order_channel: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    order_status: Union[
        Literal["Pending"],
        Literal["Unshipped"],
        Literal["PartiallyShipped"],
        Literal["Shipped"],
        Literal["Canceled"],
        Literal["Unfulfillable"],
        Literal["InvoiceUnconfirmed"],
        Literal["PendingAvailability"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['Pending', 'Unshipped', 'PartiallyShipped', 'Shipped', 'Canceled', 'Unfulfillable', 'InvoiceUnconfirmed', 'PendingAvailability'], 'type': 'string'}
    order_type: Union[
        Literal["StandardOrder"],
        Literal["LongLeadTimeOrder"],
        Literal["Preorder"],
        Literal["BackOrder"],
        Literal["SourcingOnDemandOrder"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['StandardOrder', 'LongLeadTimeOrder', 'Preorder', 'BackOrder', 'SourcingOnDemandOrder'], 'type': 'string'}
    payment_method: Union[Literal["COD"], Literal["CVS"], Literal["Other"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['COD', 'CVS', 'Other'], 'type': 'string'}
    promise_response_due_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    purchase_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    replaced_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    sales_channel: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    seller_display_name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    seller_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    ship_service_level: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    shipment_service_level_category: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    automated_shipping_settings: dict[str, Any]
    # {'ref': '#/components/schemas/AutomatedShippingSettings', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    buyer_info: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    buyer_tax_information: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerTaxInformation', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    default_ship_from_location_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    fulfillment_instruction: dict[str, Any]
    # {'ref': '#/components/schemas/FulfillmentInstruction', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    marketplace_tax_info: dict[str, Any]
    # {'ref': '#/components/schemas/MarketplaceTaxInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    order_total: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payment_execution_detail: list[dict[str, Any]]
    # {'ref': '#/components/schemas/PaymentExecutionDetailItemList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    payment_method_details: list[str]
    # {'ref': '#/components/schemas/PaymentMethodDetailItemList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    shipping_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderAddress:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    shipping_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderBuyerInfo:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_county: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_email: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    buyer_name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    buyer_tax_info: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerTaxInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderItem:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    condition_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    condition_note: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    condition_subtype_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    deemed_reseller_category: Union[Literal["IOSS"], Literal["UOSS"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['IOSS', 'UOSS'], 'type': 'string'}
    ioss_number: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    is_gift: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    is_transparency: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    price_designation: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    quantity_ordered: int
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'integer'}
    quantity_shipped: int
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'integer'}
    scheduled_delivery_end_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    scheduled_delivery_start_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    serial_number_required: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    store_chain_store_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    buyer_info: dict[str, Any]
    # {'ref': '#/components/schemas/ItemBuyerInfo', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    buyer_requested_cancel: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerRequestedCancel', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    codfee: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    codfee_discount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    item_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    item_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    points_granted: dict[str, Any]
    # {'ref': '#/components/schemas/PointsGrantedDetail', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    product_info: dict[str, Any]
    # {'ref': '#/components/schemas/ProductInfoDetail', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    promotion_discount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    promotion_discount_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    promotion_ids: list[str]
    # {'ref': '#/components/schemas/PromotionIdList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    shipping_discount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    shipping_discount_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    shipping_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    shipping_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    tax_collection: dict[str, Any]
    # {'ref': '#/components/schemas/TaxCollection', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderItemBuyerInfo:

    gift_message_text: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    gift_wrap_level: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    buyer_customized_info: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerCustomizedInfoDetail', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    gift_wrap_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    gift_wrap_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderItemBuyerInfoList:

    pass


@attrs.define
class OrderItemList:

    pass


@attrs.define
class OrderItems:

    pass


@attrs.define
class OrderItemsBuyerInfoList:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    order_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/OrderItemBuyerInfoList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderItemsList:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    order_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/OrderItemList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrderList:

    pass


@attrs.define
class OrderRegulatedInfo:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    requires_dosage_label: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}

    regulated_information: dict[str, Any]
    # {'ref': '#/components/schemas/RegulatedInformation', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    regulated_order_verification_status: dict[str, Any]
    # {'ref': '#/components/schemas/RegulatedOrderVerificationStatus', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class OrdersList:

    created_before: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    last_updated_before: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    orders: list[dict[str, Any]]
    # {'ref': '#/components/schemas/OrderList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class PaymentExecutionDetailItem:

    payment_method: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    payment: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class PaymentExecutionDetailItemList:

    pass


@attrs.define
class PaymentMethodDetailItemList:

    pass


@attrs.define
class PointsGrantedDetail:

    points_number: int
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'integer'}

    points_monetary_value: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class ProductInfoDetail:

    number_of_items: int
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'integer'}

    pass


@attrs.define
class PromotionIdList:

    pass


@attrs.define
class RegulatedInformation:

    fields: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/RegulatedInformationField'), 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'array'}

    pass


@attrs.define
class RegulatedInformationField:

    field_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    field_label: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    field_type: Union[Literal["Text"], Literal["FileAttachment"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['Text', 'FileAttachment'], 'type': 'string'}
    field_value: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class RegulatedOrderVerificationStatus:

    external_reviewer_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    requires_merchant_action: bool
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'boolean'}
    review_date: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    status: Union[
        Literal["Pending"], Literal["Approved"], Literal["Rejected"], Literal["Expired"], Literal["Cancelled"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['Pending', 'Approved', 'Rejected', 'Expired', 'Cancelled'], 'type': 'string'}
    valid_rejection_reasons: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/RejectionReason'), 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'array'}

    rejection_reason: dict[str, Any]
    # {'ref': '#/components/schemas/RejectionReason', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class RejectionReason:

    rejection_reason_description: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    rejection_reason_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class ShipmentStatus:

    pass


@attrs.define
class TaxClassification:

    name: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    value: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}

    pass


@attrs.define
class TaxCollection:

    model: Union[Literal["MarketplaceFacilitator"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['MarketplaceFacilitator'], 'type': 'string'}
    responsible_party: Union[Literal["Amazon Services, Inc."]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['Amazon Services, Inc.'], 'type': 'string'}

    pass


@attrs.define
class UpdateShipmentStatusErrorResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class UpdateShipmentStatusRequest:

    marketplace_id: str
    # {'ref': '#/components/schemas/MarketplaceId', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    order_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/OrderItems', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    shipment_status: Union[Literal["ReadyForPickup"], Literal["PickedUp"], Literal["RefusedPickup"]]
    # {'ref': '#/components/schemas/ShipmentStatus', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class UpdateVerificationStatusErrorResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class UpdateVerificationStatusRequest:

    regulated_order_verification_status: dict[str, Any]
    # {'ref': '#/components/schemas/UpdateVerificationStatusRequestBody', 'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>}
    pass


@attrs.define
class UpdateVerificationStatusRequestBody:

    external_reviewer_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    rejection_reason_id: str
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'type': 'string'}
    status: Union[Literal["Approved"], Literal["Rejected"]]
    # {'generator': <__mp_main__.Generator object at 0x000002365F44B5B0>, 'enum': ['Approved', 'Rejected'], 'type': 'string'}

    pass


class OrdersV0Client(BaseClient):
    def get_order(
        self,
        order_id: str,
    ):
        """
        Returns the order indicated by the specified order ID.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}"
        values = (order_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_params)
        return response

    _get_order_params = (("orderId", "path"),)  # name, param in

    def get_order_address(
        self,
        order_id: str,
    ):
        """
        Returns the shipping address for the specified order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}/address"
        values = (order_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_address_params)
        return response

    _get_order_address_params = (("orderId", "path"),)  # name, param in

    def get_order_buyer_info(
        self,
        order_id: str,
    ):
        """
        Returns buyer information for the specified order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}/buyerInfo"
        values = (order_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_buyer_info_params)
        return response

    _get_order_buyer_info_params = (("orderId", "path"),)  # name, param in

    def get_order_items(
        self,
        order_id: str,
        next_token: str = None,
    ):
        """
        Returns detailed order item information for the order indicated by the specified order ID. If NextToken is provided, it's used to retrieve the next page of order items.

        Note: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/orders/v0/orders/{orderId}/orderItems"
        values = (
            order_id,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_order_items_params)
        return response

    _get_order_items_params = (  # name, param in
        ("orderId", "path"),
        ("NextToken", "query"),
    )

    def get_order_items_buyer_info(
        self,
        order_id: str,
        next_token: str = None,
    ):
        """
        Returns buyer information for the order items in the specified order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/orders/v0/orders/{orderId}/orderItems/buyerInfo"
        values = (
            order_id,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_order_items_buyer_info_params)
        return response

    _get_order_items_buyer_info_params = (  # name, param in
        ("orderId", "path"),
        ("NextToken", "query"),
    )

    def get_order_regulated_info(
        self,
        order_id: str,
    ):
        """
        Returns regulated information for the order indicated by the specified order ID.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/orders/v0/orders/{orderId}/regulatedInfo"
        values = (order_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_regulated_info_params)
        return response

    _get_order_regulated_info_params = (("orderId", "path"),)  # name, param in

    def get_orders(
        self,
        marketplace_ids: list[str],
        created_after: str = None,
        created_before: str = None,
        last_updated_after: str = None,
        last_updated_before: str = None,
        order_statuses: list[str] = None,
        fulfillment_channels: list[str] = None,
        payment_methods: list[str] = None,
        buyer_email: str = None,
        seller_order_id: str = None,
        max_results_per_page: int = None,
        easy_ship_shipment_statuses: list[str] = None,
        next_token: str = None,
        amazon_order_ids: list[str] = None,
        actual_fulfillment_supply_source_id: str = None,
        is_ispu: bool = None,
        store_chain_store_id: str = None,
    ):
        """
        Returns orders created or updated during the time frame indicated by the specified parameters. You can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is present, that will be used to retrieve the orders instead of other criteria.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            created_after: A date used for selecting orders created after (or at) a specified time. Only orders placed after the specified time are returned. Either the CreatedAfter parameter or the LastUpdatedAfter parameter is required. Both cannot be empty. The date must be in ISO 8601 format.
            created_before: A date used for selecting orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in ISO 8601 format.
            last_updated_after: A date used for selecting orders that were last updated after (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
            last_updated_before: A date used for selecting orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
            order_statuses: A list of OrderStatus values used to filter the results. Possible values: PendingAvailability (This status is available for pre-orders only. The order has been placed, payment has not been authorized, and the release date of the item is in the future.); Pending (The order has been placed but payment has not been authorized); Unshipped (Payment has been authorized and the order is ready for shipment, but no items in the order have been shipped); PartiallyShipped (One or more, but not all, items in the order have been shipped); Shipped (All items in the order have been shipped); InvoiceUnconfirmed (All items in the order have been shipped. The seller has not yet given confirmation to Amazon that the invoice has been shipped to the buyer.); Canceled (The order has been canceled); and Unfulfillable (The order cannot be fulfilled. This state applies only to Multi-Channel Fulfillment orders.).
            marketplace_ids: A list of MarketplaceId values. Used to select orders that were placed in the specified marketplaces.
                See the [Selling Partner API Developer Guide](doc:marketplace-ids) for a complete list of marketplaceId values.
            fulfillment_channels: A list that indicates how an order was fulfilled. Filters the results by fulfillment channel. Possible values: AFN (Fulfillment by Amazon); MFN (Fulfilled by the seller).
            payment_methods: A list of payment method values. Used to select orders paid using the specified payment methods. Possible values: COD (Cash on delivery); CVS (Convenience store payment); Other (Any payment method other than COD or CVS).
            buyer_email: The email address of a buyer. Used to select orders that contain the specified email address.
            seller_order_id: An order identifier that is specified by the seller. Used to select only the orders that match the order identifier. If SellerOrderId is specified, then FulfillmentChannels, OrderStatuses, PaymentMethod, LastUpdatedAfter, LastUpdatedBefore, and BuyerEmail cannot be specified.
            max_results_per_page: A number that indicates the maximum number of orders that can be returned per page. Value must be 1 - 100. Default 100.
            easy_ship_shipment_statuses: A list of EasyShipShipmentStatus values. Used to select Easy Ship orders with statuses that match the specified  values. If EasyShipShipmentStatus is specified, only Amazon Easy Ship orders are returned.Possible values: PendingPickUp (Amazon has not yet picked up the package from the seller). LabelCanceled (The seller canceled the pickup). PickedUp (Amazon has picked up the package from the seller). AtOriginFC (The packaged is at the origin fulfillment center). AtDestinationFC (The package is at the destination fulfillment center). OutForDelivery (The package is out for delivery). Damaged (The package was damaged by the carrier). Delivered (The package has been delivered to the buyer). RejectedByBuyer (The package has been rejected by the buyer). Undeliverable (The package cannot be delivered). ReturnedToSeller (The package was not delivered to the buyer and was returned to the seller). ReturningToSeller (The package was not delivered to the buyer and is being returned to the seller).
            next_token: A string token returned in the response of your previous request.
            amazon_order_ids: A list of AmazonOrderId values. An AmazonOrderId is an Amazon-defined order identifier, in 3-7-7 format.
            actual_fulfillment_supply_source_id: Denotes the recommended sourceId where the order should be fulfilled from.
            is_ispu: When true, this order is marked to be picked up from a store rather than delivered.
            store_chain_store_id: The store chain store identifier. Linked to a specific store in a store chain.
        """
        url = "/orders/v0/orders"
        values = (
            created_after,
            created_before,
            last_updated_after,
            last_updated_before,
            order_statuses,
            marketplace_ids,
            fulfillment_channels,
            payment_methods,
            buyer_email,
            seller_order_id,
            max_results_per_page,
            easy_ship_shipment_statuses,
            next_token,
            amazon_order_ids,
            actual_fulfillment_supply_source_id,
            is_ispu,
            store_chain_store_id,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_orders_params)
        return response

    _get_orders_params = (  # name, param in
        ("CreatedAfter", "query"),
        ("CreatedBefore", "query"),
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("OrderStatuses", "query"),
        ("MarketplaceIds", "query"),
        ("FulfillmentChannels", "query"),
        ("PaymentMethods", "query"),
        ("BuyerEmail", "query"),
        ("SellerOrderId", "query"),
        ("MaxResultsPerPage", "query"),
        ("EasyShipShipmentStatuses", "query"),
        ("NextToken", "query"),
        ("AmazonOrderIds", "query"),
        ("ActualFulfillmentSupplySourceId", "query"),
        ("IsISPU", "query"),
        ("StoreChainStoreId", "query"),
    )

    def update_shipment_status(
        self,
        order_id: str,
        marketplace_id: str,
        shipment_status: Union[Literal["ReadyForPickup"], Literal["PickedUp"], Literal["RefusedPickup"]],
        order_items: list[dict[str, Any]] = None,
    ):
        """
        Update the shipment status.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            marketplace_id: the unobfuscated marketplace ID
            shipment_status: the status of the shipment of the order to be updated
            order_items: the list of order items and quantities when the seller wants to partially update the shipment status of the order
        """
        url = "/orders/v0/orders/{orderId}/shipment"
        values = (
            order_id,
            marketplace_id,
            shipment_status,
            order_items,
        )
        response = self._parse_args_and_request(url, "POST", values, self._update_shipment_status_params)
        return response

    _update_shipment_status_params = (  # name, param in
        ("orderId", "path"),
        ("marketplaceId", "body"),
        ("shipmentStatus", "body"),
        ("orderItems", "body"),
    )

    def update_verification_status(
        self,
        order_id: str,
        regulated_order_verification_status: dict[str, Any],
    ):
        """
        Updates (approves or rejects) the verification status of an order containing regulated products.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format.
            regulated_order_verification_status: The updated values of the VerificationStatus field.
        """
        url = "/orders/v0/orders/{orderId}/regulatedInfo"
        values = (
            order_id,
            regulated_order_verification_status,
        )
        response = self._parse_args_and_request(url, "PATCH", values, self._update_verification_status_params)
        return response

    _update_verification_status_params = (  # name, param in
        ("orderId", "path"),
        ("regulatedOrderVerificationStatus", "body"),
    )
