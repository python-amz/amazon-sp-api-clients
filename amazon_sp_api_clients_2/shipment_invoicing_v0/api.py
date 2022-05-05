"""
Selling Partner API for Shipment Invoicing
=============================================================================================
The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner¡¯s Fulfillment by Amazon (FBA) orders.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ShipmentInvoicingV0Client(BaseClient):
    def get_shipment_details(
        self,
        shipment_id: str,
    ):
        """
        Returns the shipment details required to issue an invoice for the specified shipment.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}".format(**path_parameters)

        query_parameters = {}

    def submit_invoice(
        self,
        shipment_id: str,
    ):
        """
        Submits a shipment invoice document for a given shipment.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The identifier for the shipment.
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice".format(**path_parameters)

        query_parameters = {}

    def get_invoice_status(
        self,
        shipment_id: str,
    ):
        """
        Returns the invoice status for the shipment you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The shipment identifier for the shipment.
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status".format(**path_parameters)

        query_parameters = {}
