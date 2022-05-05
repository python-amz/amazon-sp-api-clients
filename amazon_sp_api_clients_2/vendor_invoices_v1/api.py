"""
Selling Partner API for Retail Procurement Payments
=============================================================================================
The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v1
"""
from ..utils.base_client import BaseClient


class VendorInvoicesV1Client(BaseClient):
    def submit_invoices(
        self,
    ):
        url = "/vendor/payments/v1/invoices"
