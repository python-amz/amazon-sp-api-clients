"""
Selling Partner API for Finances
=============================================================================================
The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class FinancesV0Client(BaseClient):
    def list_financial_event_groups(
        self,
        Max_results_per_page: int = None,
        Financial_event_group_started_before: str = None,
        Financial_event_group_started_after: str = None,
        Next_token: str = None,
    ):
        """
        Returns financial event groups for a given date range.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Max_results_per_page: The maximum number of results to return per page.
            Financial_event_group_started_before: A date used for selecting financial event groups that opened before (but not at) a specified date and time, in ISO 8601 format. The date-time  must be later than FinancialEventGroupStartedAfter and no later than two minutes before the request was submitted. If FinancialEventGroupStartedAfter and FinancialEventGroupStartedBefore are more than 180 days apart, no financial event groups are returned.
            Financial_event_group_started_after: A date used for selecting financial event groups that opened after (or at) a specified date and time, in ISO 8601 format. The date-time must be no later than two minutes before the request was submitted.
            Next_token: A string token returned in the response of your previous request.
        """
        path_parameters = {}

        url = "/finances/v0/financialEventGroups".format(**path_parameters)

        query_parameters = {}

        if Max_results_per_page is not None:
            query_parameters["MaxResultsPerPage"] = Max_results_per_page

        if Financial_event_group_started_before is not None:
            query_parameters["FinancialEventGroupStartedBefore"] = Financial_event_group_started_before

        if Financial_event_group_started_after is not None:
            query_parameters["FinancialEventGroupStartedAfter"] = Financial_event_group_started_after

        if Next_token is not None:
            query_parameters["NextToken"] = Next_token

    def list_financial_events_by_group_id(
        self,
        Max_results_per_page: int = None,
        event_group_id: str,
        Next_token: str = None,
    ):
        """
        Returns all financial events for the specified financial event group.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Max_results_per_page: The maximum number of results to return per page.
            event_group_id: The identifier of the financial event group to which the events belong.
            Next_token: A string token returned in the response of your previous request.
        """
        path_parameters = {}

        path_parameters["eventGroupId"] = event_group_id

        url = "/finances/v0/financialEventGroups/{eventGroupId}/financialEvents".format(**path_parameters)

        query_parameters = {}

        if Max_results_per_page is not None:
            query_parameters["MaxResultsPerPage"] = Max_results_per_page

        if Next_token is not None:
            query_parameters["NextToken"] = Next_token

    def list_financial_events_by_order_id(
        self,
        order_id: str,
        Max_results_per_page: int = None,
        Next_token: str = None,
    ):
        """
        Returns all financial events for the specified order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            Max_results_per_page: The maximum number of results to return per page.
            Next_token: A string token returned in the response of your previous request.
        """
        path_parameters = {}

        path_parameters["orderId"] = order_id

        url = "/finances/v0/orders/{orderId}/financialEvents".format(**path_parameters)

        query_parameters = {}

        if Max_results_per_page is not None:
            query_parameters["MaxResultsPerPage"] = Max_results_per_page

        if Next_token is not None:
            query_parameters["NextToken"] = Next_token

    def list_financial_events(
        self,
        Max_results_per_page: int = None,
        Posted_after: str = None,
        Posted_before: str = None,
        Next_token: str = None,
    ):
        """
        Returns financial events for the specified data range.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Max_results_per_page: The maximum number of results to return per page.
            Posted_after: A date used for selecting financial events posted after (or at) a specified time. The date-time must be no later than two minutes before the request was submitted, in ISO 8601 date time format.
            Posted_before: A date used for selecting financial events posted before (but not at) a specified time. The date-time must be later than PostedAfter and no later than two minutes before the request was submitted, in ISO 8601 date time format. If PostedAfter and PostedBefore are more than 180 days apart, no financial events are returned. You must specify the PostedAfter parameter if you specify the PostedBefore parameter. Default: Now minus two minutes.
            Next_token: A string token returned in the response of your previous request.
        """
        path_parameters = {}

        url = "/finances/v0/financialEvents".format(**path_parameters)

        query_parameters = {}

        if Max_results_per_page is not None:
            query_parameters["MaxResultsPerPage"] = Max_results_per_page

        if Posted_after is not None:
            query_parameters["PostedAfter"] = Posted_after

        if Posted_before is not None:
            query_parameters["PostedBefore"] = Posted_before

        if Next_token is not None:
            query_parameters["NextToken"] = Next_token
