"""
Selling Partner API for Direct Fulfillment Payments
=============================================================================================
The Selling Partner API for Direct Fulfillment Payments provides programmatic access to a direct fulfillment vendor's invoice data.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient


class VendorDirectFulfillmentPaymentsV1Client(BaseClient):
    def submit_invoice(
        self,
    ):
        url = "/vendor/directFulfillment/payments/v1/invoices"
