"""
Selling Partner APIs for Fulfillment Outbound
=============================================================================================

The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
API Version: 2020-07-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


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
