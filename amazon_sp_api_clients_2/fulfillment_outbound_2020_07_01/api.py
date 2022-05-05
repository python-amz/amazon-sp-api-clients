"""
Selling Partner APIs for Fulfillment Outbound
=============================================================================================
The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-07-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class FulfillmentOutbound20200701Client(BaseClient):
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
        path_parameters = {}

        url = "/fba/outbound/2020-07-01/fulfillmentOrders/preview".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        url = "/fba/outbound/2020-07-01/fulfillmentOrders".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        url = "/fba/outbound/2020-07-01/fulfillmentOrders".format(**path_parameters)

        query_parameters = {}

        if query_start_date is not None:
            query_parameters["queryStartDate"] = query_start_date

        if next_token is not None:
            query_parameters["nextToken"] = next_token

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
        path_parameters = {}

        url = "/fba/outbound/2020-07-01/tracking".format(**path_parameters)

        query_parameters = {}

        query_parameters["packageNumber"] = package_number

    def list_return_reason_codes(
        self,
        seller_sku: str,
        marketplace_id: str = None,
        seller_fulfillment_order_id: str = None,
        language: str,
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
        path_parameters = {}

        url = "/fba/outbound/2020-07-01/returnReasonCodes".format(**path_parameters)

        query_parameters = {}

        query_parameters["sellerSku"] = seller_sku

        if marketplace_id is not None:
            query_parameters["marketplaceId"] = marketplace_id

        if seller_fulfillment_order_id is not None:
            query_parameters["sellerFulfillmentOrderId"] = seller_fulfillment_order_id

        query_parameters["language"] = language

    def create_fulfillment_return(
        self,
        seller_fulfillment_order_id: str,
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
        """
        path_parameters = {}

        path_parameters["sellerFulfillmentOrderId"] = seller_fulfillment_order_id

        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        path_parameters["sellerFulfillmentOrderId"] = seller_fulfillment_order_id

        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}".format(**path_parameters)

        query_parameters = {}

    def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
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
        """
        path_parameters = {}

        path_parameters["sellerFulfillmentOrderId"] = seller_fulfillment_order_id

        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        path_parameters["sellerFulfillmentOrderId"] = seller_fulfillment_order_id

        url = "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        url = "/fba/outbound/2020-07-01/features".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

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
        path_parameters = {}

        path_parameters["featureName"] = feature_name

        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id

        if next_token is not None:
            query_parameters["nextToken"] = next_token

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
        path_parameters = {}

        path_parameters["featureName"] = feature_name

        path_parameters["sellerSku"] = seller_sku

        url = "/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}".format(**path_parameters)

        query_parameters = {}

        query_parameters["marketplaceId"] = marketplace_id
