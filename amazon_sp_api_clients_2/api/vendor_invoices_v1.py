"""
Selling Partner API for Retail Procurement Payments
=============================================================================================

The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class SubmitInvoicesResponse:
    pass


class TransactionId:
    pass


class ErrorList:
    pass


class Error:
    pass


class SubmitInvoicesRequest:
    pass


class Invoice:
    pass


class PartyIdentification:
    pass


class TaxRegistrationDetails:
    pass


class Address:
    pass


class InvoiceItem:
    pass


class TaxDetails:
    pass


class Money:
    pass


class AdditionalDetails:
    pass


class ChargeDetails:
    pass


class AllowanceDetails:
    pass


class PaymentTerms:
    pass


class CreditNoteDetails:
    pass


class ItemQuantity:
    pass


class Decimal:
    pass


class DateTime:
    pass


class VendorInvoicesV1Client(BaseClient):
    def submit_invoices(
        self,
    ):
        """
        Submit new invoices to Amazon.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/payments/v1/invoices"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoices_params)
        return response

    _submit_invoices_params = ()  # name, param in
