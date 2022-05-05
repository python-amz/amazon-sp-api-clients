"""
Selling Partner API for Retail Procurement Payments
=============================================================================================

The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class SubmitInvoicesResponse:
    pass


@attrs.define
class TransactionId:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class Error:
    pass


@attrs.define
class SubmitInvoicesRequest:
    pass


@attrs.define
class Invoice:
    pass


@attrs.define
class PartyIdentification:
    pass


@attrs.define
class TaxRegistrationDetails:
    pass


@attrs.define
class Address:
    pass


@attrs.define
class InvoiceItem:
    pass


@attrs.define
class TaxDetails:
    pass


@attrs.define
class Money:
    pass


@attrs.define
class AdditionalDetails:
    pass


@attrs.define
class ChargeDetails:
    pass


@attrs.define
class AllowanceDetails:
    pass


@attrs.define
class PaymentTerms:
    pass


@attrs.define
class CreditNoteDetails:
    pass


@attrs.define
class ItemQuantity:
    pass


@attrs.define
class Decimal:
    pass


@attrs.define
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
