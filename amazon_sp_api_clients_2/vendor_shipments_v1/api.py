"""
Selling Partner API for Retail Procurement Shipments
=============================================================================================
The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient


class VendorShipmentsV1Client(BaseClient):
    def Submit_shipment_confirmations(
        self,
    ):
        url = "/vendor/shipping/v1/shipmentConfirmations"
