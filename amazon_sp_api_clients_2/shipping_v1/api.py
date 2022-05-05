"""
Selling Partner API for Shipping
=============================================================================================
Provides programmatic access to Amazon Shipping APIs.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ShippingV1Client(BaseClient):
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
        values = ()

    _get_account_params = ()  # name, param in, required

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
        values = ()

    _purchase_shipment_params = ()  # name, param in, required

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
        values = ()

    _get_rates_params = ()  # name, param in, required

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
        values = ()

    _create_shipment_params = ()  # name, param in, required

    def get_shipment(
        self,
        shipment_id: str,
    ):
        """
        Return the entire shipment object for the shipmentId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
        """
        url = "/shipping/v1/shipments/{shipmentId}"
        values = (shipment_id,)

    _get_shipment_params = (("shipmentId", "path", True),)  # name, param in, required

    def cancel_shipment(
        self,
        shipment_id: str,
    ):
        """
        Cancel a shipment by the given shipmentId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
        """
        url = "/shipping/v1/shipments/{shipmentId}/cancel"
        values = (shipment_id,)

    _cancel_shipment_params = (("shipmentId", "path", True),)  # name, param in, required

    def retrieve_shipping_label(
        self,
        shipment_id: str,
        tracking_id: str,
    ):
        """
        Retrieve shipping label based on the shipment id and tracking id.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
            tracking_id: no description.
        """
        url = "/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label"
        values = (
            shipment_id,
            tracking_id,
        )

    _retrieve_shipping_label_params = (  # name, param in, required
        ("shipmentId", "path", True),
        ("trackingId", "path", True),
    )

    def purchase_labels(
        self,
        shipment_id: str,
    ):
        """
        Purchase shipping labels based on a given rate.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
        """
        url = "/shipping/v1/shipments/{shipmentId}/purchaseLabels"
        values = (shipment_id,)

    _purchase_labels_params = (("shipmentId", "path", True),)  # name, param in, required

    def get_tracking_information(
        self,
        tracking_id: str,
    ):
        """
        Return the tracking information of a shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            tracking_id: no description.
        """
        url = "/shipping/v1/tracking/{trackingId}"
        values = (tracking_id,)

    _get_tracking_information_params = (("trackingId", "path", True),)  # name, param in, required
