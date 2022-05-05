"""
Selling Partner API for Orders
=============================================================================================
The Selling Partner API for Orders helps you programmatically retrieve order information. These APIs let you develop fast, flexible, custom applications in areas like order synchronization, order research, and demand-based decision support tools.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


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

    _get_order_params = (("orderId", "path", True),)  # name, param in, required

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

    _get_order_address_params = (("orderId", "path", True),)  # name, param in, required

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

    _get_order_buyer_info_params = (("orderId", "path", True),)  # name, param in, required

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

    _get_order_items_params = (  # name, param in, required
        ("orderId", "path", True),
        ("NextToken", "query", False),
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

    _get_order_items_buyer_info_params = (  # name, param in, required
        ("orderId", "path", True),
        ("NextToken", "query", False),
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

    _get_order_regulated_info_params = (("orderId", "path", True),)  # name, param in, required

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

    _get_orders_params = (  # name, param in, required
        ("CreatedAfter", "query", False),
        ("CreatedBefore", "query", False),
        ("LastUpdatedAfter", "query", False),
        ("LastUpdatedBefore", "query", False),
        ("OrderStatuses", "query", False),
        ("MarketplaceIds", "query", True),
        ("FulfillmentChannels", "query", False),
        ("PaymentMethods", "query", False),
        ("BuyerEmail", "query", False),
        ("SellerOrderId", "query", False),
        ("MaxResultsPerPage", "query", False),
        ("EasyShipShipmentStatuses", "query", False),
        ("NextToken", "query", False),
        ("AmazonOrderIds", "query", False),
        ("ActualFulfillmentSupplySourceId", "query", False),
        ("IsISPU", "query", False),
        ("StoreChainStoreId", "query", False),
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

    _update_shipment_status_params = (  # name, param in, required
        ("orderId", "path", True),
        ("marketplaceId", "body", True),
        ("shipmentStatus", "body", True),
        ("orderItems", "body", False),
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

    _update_verification_status_params = (  # name, param in, required
        ("orderId", "path", True),
        ("regulatedOrderVerificationStatus", "body", True),
    )
