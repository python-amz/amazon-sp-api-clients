"""
Selling Partner API for Shipping
=============================================================================================
Provides programmatic access to Amazon Shipping APIs.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient


class ShippingV1Client(BaseClient):
    def create_shipment(
        self,
    ):
        """
        Create a new shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/shipments"

    def get_shipment(
        self,
        shipment_id,
    ):
        """
        Return the entire shipment object for the shipmentId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: None
        """
        url = "/shipping/v1/shipments/{shipmentId}"

    def cancel_shipment(
        self,
        shipment_id,
    ):
        """
        Cancel a shipment by the given shipmentId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: None
        """
        url = "/shipping/v1/shipments/{shipmentId}/cancel"

    def purchase_labels(
        self,
        shipment_id,
    ):
        """
        Purchase shipping labels based on a given rate.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: None
        """
        url = "/shipping/v1/shipments/{shipmentId}/purchaseLabels"

    def retrieve_shipping_label(
        self,
        shipment_id,
        tracking_id,
    ):
        """
        Retrieve shipping label based on the shipment id and tracking id.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: None
            tracking_id: None
        """
        url = "/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label"

    def purchase_shipment(
        self,
    ):
        """
        Purchase shipping labels.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/purchaseShipment"

    def get_rates(
        self,
    ):
        """
        Get service rates.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/rates"

    def get_account(
        self,
    ):
        """
        Verify if the current account is valid.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/account"

    def get_tracking_information(
        self,
        tracking_id,
    ):
        """
        Return the tracking information of a shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            tracking_id: None
        """
        url = "/shipping/v1/tracking/{trackingId}"
