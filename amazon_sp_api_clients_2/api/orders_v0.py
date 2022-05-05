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

    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    address_type: Union[Literal["Residential"], Literal["Commercial"]] = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    county: str = attrs.field()
    district: str = attrs.field()
    municipality: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class AutomatedShippingSettings:

    automated_carrier: str = attrs.field()
    automated_ship_method: str = attrs.field()
    has_automated_shipping_settings: bool = attrs.field()

    pass


@attrs.define
class BuyerCustomizedInfoDetail:

    customized_url: str = attrs.field()

    pass


@attrs.define
class BuyerInfo:

    buyer_county: str = attrs.field()
    buyer_email: str = attrs.field()
    buyer_name: str = attrs.field()
    purchase_order_number: str = attrs.field()

    buyer_tax_info: "BuyerTaxInfo" = attrs.field()
    pass


@attrs.define
class BuyerRequestedCancel:

    buyer_cancel_reason: str = attrs.field()
    is_buyer_requested_cancel: bool = attrs.field()

    pass


@attrs.define
class BuyerTaxInfo:

    company_legal_name: str = attrs.field()
    tax_classifications: list["TaxClassification"] = attrs.field()
    taxing_region: str = attrs.field()

    pass


@attrs.define
class BuyerTaxInformation:

    buyer_business_address: str = attrs.field()
    buyer_legal_company_name: str = attrs.field()
    buyer_tax_office: str = attrs.field()
    buyer_tax_registration_id: str = attrs.field()

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
class FulfillmentInstruction:

    fulfillment_supply_source_id: str = attrs.field()

    pass


@attrs.define
class GetOrderAddressResponse:

    errors: "ErrorList" = attrs.field()
    payload: "OrderAddress" = attrs.field()
    pass


@attrs.define
class GetOrderBuyerInfoResponse:

    errors: "ErrorList" = attrs.field()
    payload: "OrderBuyerInfo" = attrs.field()
    pass


@attrs.define
class GetOrderItemsBuyerInfoResponse:

    errors: "ErrorList" = attrs.field()
    payload: "OrderItemsBuyerInfoList" = attrs.field()
    pass


@attrs.define
class GetOrderItemsResponse:

    errors: "ErrorList" = attrs.field()
    payload: "OrderItemsList" = attrs.field()
    pass


@attrs.define
class GetOrderRegulatedInfoResponse:

    errors: "ErrorList" = attrs.field()
    payload: "OrderRegulatedInfo" = attrs.field()
    pass


@attrs.define
class GetOrderResponse:

    errors: "ErrorList" = attrs.field()
    payload: "Order" = attrs.field()
    pass


@attrs.define
class GetOrdersResponse:

    errors: "ErrorList" = attrs.field()
    payload: "OrdersList" = attrs.field()
    pass


@attrs.define
class ItemBuyerInfo:

    gift_message_text: str = attrs.field()
    gift_wrap_level: str = attrs.field()

    buyer_customized_info: "BuyerCustomizedInfoDetail" = attrs.field()
    gift_wrap_price: "Money" = attrs.field()
    gift_wrap_tax: "Money" = attrs.field()
    pass


@attrs.define
class MarketplaceId:

    pass


@attrs.define
class MarketplaceTaxInfo:

    tax_classifications: list["TaxClassification"] = attrs.field()

    pass


@attrs.define
class Money:

    amount: str = attrs.field()
    currency_code: str = attrs.field()

    pass


@attrs.define
class Order:

    amazon_order_id: str = attrs.field()
    buyer_invoice_preference: Union[Literal["INDIVIDUAL"], Literal["BUSINESS"]] = attrs.field()
    cba_displayable_shipping_label: str = attrs.field()
    earliest_delivery_date: str = attrs.field()
    earliest_ship_date: str = attrs.field()
    easy_ship_shipment_status: str = attrs.field()
    fulfillment_channel: Union[Literal["MFN"], Literal["AFN"]] = attrs.field()
    has_regulated_items: bool = attrs.field()
    is_business_order: bool = attrs.field()
    is_estimated_ship_date_set: bool = attrs.field()
    is_global_express_enabled: bool = attrs.field()
    is_iba: bool = attrs.field()
    is_ispu: bool = attrs.field()
    is_premium_order: bool = attrs.field()
    is_prime: bool = attrs.field()
    is_replacement_order: bool = attrs.field()
    is_sold_by_ab: bool = attrs.field()
    last_update_date: str = attrs.field()
    latest_delivery_date: str = attrs.field()
    latest_ship_date: str = attrs.field()
    marketplace_id: str = attrs.field()
    number_of_items_shipped: int = attrs.field()
    number_of_items_unshipped: int = attrs.field()
    order_channel: str = attrs.field()
    order_status: Union[
        Literal["Pending"],
        Literal["Unshipped"],
        Literal["PartiallyShipped"],
        Literal["Shipped"],
        Literal["Canceled"],
        Literal["Unfulfillable"],
        Literal["InvoiceUnconfirmed"],
        Literal["PendingAvailability"],
    ] = attrs.field()
    order_type: Union[
        Literal["StandardOrder"],
        Literal["LongLeadTimeOrder"],
        Literal["Preorder"],
        Literal["BackOrder"],
        Literal["SourcingOnDemandOrder"],
    ] = attrs.field()
    payment_method: Union[Literal["COD"], Literal["CVS"], Literal["Other"]] = attrs.field()
    promise_response_due_date: str = attrs.field()
    purchase_date: str = attrs.field()
    replaced_order_id: str = attrs.field()
    sales_channel: str = attrs.field()
    seller_display_name: str = attrs.field()
    seller_order_id: str = attrs.field()
    ship_service_level: str = attrs.field()
    shipment_service_level_category: str = attrs.field()

    automated_shipping_settings: "AutomatedShippingSettings" = attrs.field()
    buyer_info: "BuyerInfo" = attrs.field()
    buyer_tax_information: "BuyerTaxInformation" = attrs.field()
    default_ship_from_location_address: "Address" = attrs.field()
    fulfillment_instruction: "FulfillmentInstruction" = attrs.field()
    marketplace_tax_info: "MarketplaceTaxInfo" = attrs.field()
    order_total: "Money" = attrs.field()
    payment_execution_detail: "PaymentExecutionDetailItemList" = attrs.field()
    payment_method_details: "PaymentMethodDetailItemList" = attrs.field()
    shipping_address: "Address" = attrs.field()
    pass


@attrs.define
class OrderAddress:

    amazon_order_id: str = attrs.field()

    shipping_address: "Address" = attrs.field()
    pass


@attrs.define
class OrderBuyerInfo:

    amazon_order_id: str = attrs.field()
    buyer_county: str = attrs.field()
    buyer_email: str = attrs.field()
    buyer_name: str = attrs.field()
    purchase_order_number: str = attrs.field()

    buyer_tax_info: "BuyerTaxInfo" = attrs.field()
    pass


@attrs.define
class OrderItem:

    asin: str = attrs.field()
    condition_id: str = attrs.field()
    condition_note: str = attrs.field()
    condition_subtype_id: str = attrs.field()
    deemed_reseller_category: Union[Literal["IOSS"], Literal["UOSS"]] = attrs.field()
    ioss_number: str = attrs.field()
    is_gift: bool = attrs.field()
    is_transparency: bool = attrs.field()
    order_item_id: str = attrs.field()
    price_designation: str = attrs.field()
    quantity_ordered: int = attrs.field()
    quantity_shipped: int = attrs.field()
    scheduled_delivery_end_date: str = attrs.field()
    scheduled_delivery_start_date: str = attrs.field()
    seller_sku: str = attrs.field()
    serial_number_required: bool = attrs.field()
    store_chain_store_id: str = attrs.field()
    title: str = attrs.field()

    buyer_info: "ItemBuyerInfo" = attrs.field()
    buyer_requested_cancel: "BuyerRequestedCancel" = attrs.field()
    codfee: "Money" = attrs.field()
    codfee_discount: "Money" = attrs.field()
    item_price: "Money" = attrs.field()
    item_tax: "Money" = attrs.field()
    points_granted: "PointsGrantedDetail" = attrs.field()
    product_info: "ProductInfoDetail" = attrs.field()
    promotion_discount: "Money" = attrs.field()
    promotion_discount_tax: "Money" = attrs.field()
    promotion_ids: "PromotionIdList" = attrs.field()
    shipping_discount: "Money" = attrs.field()
    shipping_discount_tax: "Money" = attrs.field()
    shipping_price: "Money" = attrs.field()
    shipping_tax: "Money" = attrs.field()
    tax_collection: "TaxCollection" = attrs.field()
    pass


@attrs.define
class OrderItemBuyerInfo:

    gift_message_text: str = attrs.field()
    gift_wrap_level: str = attrs.field()
    order_item_id: str = attrs.field()

    buyer_customized_info: "BuyerCustomizedInfoDetail" = attrs.field()
    gift_wrap_price: "Money" = attrs.field()
    gift_wrap_tax: "Money" = attrs.field()
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

    amazon_order_id: str = attrs.field()
    next_token: str = attrs.field()

    order_items: "OrderItemBuyerInfoList" = attrs.field()
    pass


@attrs.define
class OrderItemsList:

    amazon_order_id: str = attrs.field()
    next_token: str = attrs.field()

    order_items: "OrderItemList" = attrs.field()
    pass


@attrs.define
class OrderList:

    pass


@attrs.define
class OrderRegulatedInfo:

    amazon_order_id: str = attrs.field()
    requires_dosage_label: bool = attrs.field()

    regulated_information: "RegulatedInformation" = attrs.field()
    regulated_order_verification_status: "RegulatedOrderVerificationStatus" = attrs.field()
    pass


@attrs.define
class OrdersList:

    created_before: str = attrs.field()
    last_updated_before: str = attrs.field()
    next_token: str = attrs.field()

    orders: "OrderList" = attrs.field()
    pass


@attrs.define
class PaymentExecutionDetailItem:

    payment_method: str = attrs.field()

    payment: "Money" = attrs.field()
    pass


@attrs.define
class PaymentExecutionDetailItemList:

    pass


@attrs.define
class PaymentMethodDetailItemList:

    pass


@attrs.define
class PointsGrantedDetail:

    points_number: int = attrs.field()

    points_monetary_value: "Money" = attrs.field()
    pass


@attrs.define
class ProductInfoDetail:

    number_of_items: int = attrs.field()

    pass


@attrs.define
class PromotionIdList:

    pass


@attrs.define
class RegulatedInformation:

    fields: list["RegulatedInformationField"] = attrs.field()

    pass


@attrs.define
class RegulatedInformationField:

    field_id: str = attrs.field()
    field_label: str = attrs.field()
    field_type: Union[Literal["Text"], Literal["FileAttachment"]] = attrs.field()
    field_value: str = attrs.field()

    pass


@attrs.define
class RegulatedOrderVerificationStatus:

    external_reviewer_id: str = attrs.field()
    requires_merchant_action: bool = attrs.field()
    review_date: str = attrs.field()
    status: Union[
        Literal["Pending"], Literal["Approved"], Literal["Rejected"], Literal["Expired"], Literal["Cancelled"]
    ] = attrs.field()
    valid_rejection_reasons: list["RejectionReason"] = attrs.field()

    rejection_reason: "RejectionReason" = attrs.field()
    pass


@attrs.define
class RejectionReason:

    rejection_reason_description: str = attrs.field()
    rejection_reason_id: str = attrs.field()

    pass


@attrs.define
class ShipmentStatus:

    pass


@attrs.define
class TaxClassification:

    name: str = attrs.field()
    value: str = attrs.field()

    pass


@attrs.define
class TaxCollection:

    model: Union[Literal["MarketplaceFacilitator"]] = attrs.field()
    responsible_party: Union[Literal["Amazon Services, Inc."]] = attrs.field()

    pass


@attrs.define
class UpdateShipmentStatusErrorResponse:

    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class UpdateShipmentStatusRequest:

    marketplace_id: "MarketplaceId" = attrs.field()
    order_items: "OrderItems" = attrs.field()
    shipment_status: "ShipmentStatus" = attrs.field()
    pass


@attrs.define
class UpdateVerificationStatusErrorResponse:

    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class UpdateVerificationStatusRequest:

    regulated_order_verification_status: "UpdateVerificationStatusRequestBody" = attrs.field()
    pass


@attrs.define
class UpdateVerificationStatusRequestBody:

    external_reviewer_id: str = attrs.field()
    rejection_reason_id: str = attrs.field()
    status: Union[Literal["Approved"], Literal["Rejected"]] = attrs.field()

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
