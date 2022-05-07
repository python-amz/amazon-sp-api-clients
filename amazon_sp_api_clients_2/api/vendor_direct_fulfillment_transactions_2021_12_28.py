"""
Selling Partner API for Direct Fulfillment Transaction Status
=============================================================================================

The Selling Partner API for Direct Fulfillment Transaction Status provides programmatic access to a direct fulfillment vendor's transaction status.
API Version: 2021-12-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Transaction:
    """
    The transaction status details.
    """

    errors: Optional["ErrorList"] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    status: Union[Literal["Failure"], Literal["Processing"], Literal["Success"]] = attrs.field()
    """
    Current processing status of the transaction.
    """

    transaction_id: str = attrs.field()
    """
    The unique identifier sent in the 'transactionId' field in response to the post request of a specific transaction.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionStatus:
    """
    The payload for the getTransactionStatus operation.
    """

    transaction_status: Optional["Transaction"] = attrs.field()
    """
    The transaction status details.
    """


class VendorDirectFulfillmentTransactions20211228Client(BaseClient):
    def get_transaction_status(
        self,
        transaction_id: str,
    ) -> Union[Error, ErrorList, TransactionStatus]:
        """
        Returns the status of the transaction indicated by the specified transactionId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            transaction_id: Previously returned in the response to the POST request of a specific transaction.
        """
        url = "/vendor/directFulfillment/transactions/2021-12-28/transactions/{transactionId}"
        values = (transaction_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_transaction_status_params,
        )
        klass = self._get_transaction_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_transaction_status_params = (("transactionId", "path"),)  # name, param in

    _get_transaction_status_responses = {
        200: TransactionStatus,
        400: ErrorList,
        401: Error,
        403: Error,
        404: Error,
        415: Error,
        429: Error,
        500: Error,
        503: Error,
    }
