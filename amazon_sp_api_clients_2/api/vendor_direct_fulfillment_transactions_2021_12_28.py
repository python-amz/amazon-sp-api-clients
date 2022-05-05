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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'type': 'array', 'items': Reference(ref='#/components/schemas/Error')}

    pass


@attrs.define
class Transaction:

    status: Union[Literal["Failure"], Literal["Processing"], Literal["Success"]]
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'enum': ['Failure', 'Processing', 'Success'], 'type': 'string'}
    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'type': 'string'}

    errors: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'ref': '#/components/schemas/ErrorList'}
    pass


@attrs.define
class TransactionStatus:

    transaction_status: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000001644F1956C0>, 'ref': '#/components/schemas/Transaction'}
    pass


class VendorDirectFulfillmentTransactions20211228Client(BaseClient):
    def get_transaction_status(
        self,
        transaction_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_transaction_status_params)
        return response

    _get_transaction_status_params = (("transactionId", "path"),)  # name, param in
