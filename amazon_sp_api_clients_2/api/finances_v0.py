"""
Selling Partner API for Finances
=============================================================================================

The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class AdjustmentEvent:
    pass


class AdjustmentEventList:
    pass


class AdjustmentItem:
    pass


class AdjustmentItemList:
    pass


class AffordabilityExpenseEvent:
    pass


class AffordabilityExpenseEventList:
    pass


class BigDecimal:
    pass


class ChargeComponent:
    pass


class ChargeComponentList:
    pass


class ChargeInstrument:
    pass


class ChargeInstrumentList:
    pass


class CouponPaymentEvent:
    pass


class CouponPaymentEventList:
    pass


class Currency:
    pass


class Date:
    pass


class DebtRecoveryEvent:
    pass


class DebtRecoveryEventList:
    pass


class DebtRecoveryItem:
    pass


class DebtRecoveryItemList:
    pass


class DirectPayment:
    pass


class DirectPaymentList:
    pass


class FBALiquidationEvent:
    pass


class FBALiquidationEventList:
    pass


class FeeComponent:
    pass


class FeeComponentList:
    pass


class FinancialEventGroup:
    pass


class FinancialEventGroupList:
    pass


class FinancialEvents:
    pass


class ImagingServicesFeeEvent:
    pass


class ImagingServicesFeeEventList:
    pass


class ListFinancialEventGroupsPayload:
    pass


class ListFinancialEventGroupsResponse:
    pass


class ListFinancialEventsPayload:
    pass


class ListFinancialEventsResponse:
    pass


class LoanServicingEvent:
    pass


class LoanServicingEventList:
    pass


class NetworkComminglingTransactionEvent:
    pass


class NetworkComminglingTransactionEventList:
    pass


class PayWithAmazonEvent:
    pass


class PayWithAmazonEventList:
    pass


class ProductAdsPaymentEvent:
    pass


class ProductAdsPaymentEventList:
    pass


class Promotion:
    pass


class PromotionList:
    pass


class RemovalShipmentEvent:
    pass


class RemovalShipmentEventList:
    pass


class RemovalShipmentItem:
    pass


class RemovalShipmentItemList:
    pass


class RemovalShipmentAdjustmentEvent:
    pass


class RemovalShipmentAdjustmentEventList:
    pass


class RemovalShipmentItemAdjustment:
    pass


class RentalTransactionEvent:
    pass


class RentalTransactionEventList:
    pass


class RetrochargeEvent:
    pass


class RetrochargeEventList:
    pass


class SAFETReimbursementEvent:
    pass


class SAFETReimbursementEventList:
    pass


class SAFETReimbursementItem:
    pass


class SAFETReimbursementItemList:
    pass


class SellerDealPaymentEvent:
    pass


class SellerDealPaymentEventList:
    pass


class SellerReviewEnrollmentPaymentEvent:
    pass


class SellerReviewEnrollmentPaymentEventList:
    pass


class ServiceFeeEvent:
    pass


class ServiceFeeEventList:
    pass


class ShipmentEvent:
    pass


class ShipmentEventList:
    pass


class ShipmentItem:
    pass


class ShipmentItemList:
    pass


class SolutionProviderCreditEvent:
    pass


class SolutionProviderCreditEventList:
    pass


class TaxWithholdingPeriod:
    pass


class TaxWithholdingEvent:
    pass


class TaxWithholdingEventList:
    pass


class TaxWithheldComponent:
    pass


class TaxWithheldComponentList:
    pass


class TrialShipmentEvent:
    pass


class TrialShipmentEventList:
    pass


class ShipmentSettleEventList:
    pass


class ErrorList:
    pass


class Error:
    pass


class FinancesV0Client(BaseClient):
    def list_financial_event_groups(
        self,
        max_results_per_page: int = None,
        financial_event_group_started_before: str = None,
        financial_event_group_started_after: str = None,
        next_token: str = None,
    ):
        """
        Returns financial event groups for a given date range.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            max_results_per_page: The maximum number of results to return per page.
            financial_event_group_started_before: A date used for selecting financial event groups that opened before (but not at) a specified date and time, in ISO 8601 format. The date-time  must be later than FinancialEventGroupStartedAfter and no later than two minutes before the request was submitted. If FinancialEventGroupStartedAfter and FinancialEventGroupStartedBefore are more than 180 days apart, no financial event groups are returned.
            financial_event_group_started_after: A date used for selecting financial event groups that opened after (or at) a specified date and time, in ISO 8601 format. The date-time must be no later than two minutes before the request was submitted.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/finances/v0/financialEventGroups"
        values = (
            max_results_per_page,
            financial_event_group_started_before,
            financial_event_group_started_after,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_financial_event_groups_params)
        return response

    _list_financial_event_groups_params = (  # name, param in
        ("MaxResultsPerPage", "query"),
        ("FinancialEventGroupStartedBefore", "query"),
        ("FinancialEventGroupStartedAfter", "query"),
        ("NextToken", "query"),
    )

    def list_financial_events(
        self,
        max_results_per_page: int = None,
        posted_after: str = None,
        posted_before: str = None,
        next_token: str = None,
    ):
        """
        Returns financial events for the specified data range.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            max_results_per_page: The maximum number of results to return per page.
            posted_after: A date used for selecting financial events posted after (or at) a specified time. The date-time must be no later than two minutes before the request was submitted, in ISO 8601 date time format.
            posted_before: A date used for selecting financial events posted before (but not at) a specified time. The date-time must be later than PostedAfter and no later than two minutes before the request was submitted, in ISO 8601 date time format. If PostedAfter and PostedBefore are more than 180 days apart, no financial events are returned. You must specify the PostedAfter parameter if you specify the PostedBefore parameter. Default: Now minus two minutes.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/finances/v0/financialEvents"
        values = (
            max_results_per_page,
            posted_after,
            posted_before,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_financial_events_params)
        return response

    _list_financial_events_params = (  # name, param in
        ("MaxResultsPerPage", "query"),
        ("PostedAfter", "query"),
        ("PostedBefore", "query"),
        ("NextToken", "query"),
    )

    def list_financial_events_by_group_id(
        self,
        event_group_id: str,
        max_results_per_page: int = None,
        next_token: str = None,
    ):
        """
        Returns all financial events for the specified financial event group.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            max_results_per_page: The maximum number of results to return per page.
            event_group_id: The identifier of the financial event group to which the events belong.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/finances/v0/financialEventGroups/{eventGroupId}/financialEvents"
        values = (
            max_results_per_page,
            event_group_id,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_financial_events_by_group_id_params)
        return response

    _list_financial_events_by_group_id_params = (  # name, param in
        ("MaxResultsPerPage", "query"),
        ("eventGroupId", "path"),
        ("NextToken", "query"),
    )

    def list_financial_events_by_order_id(
        self,
        order_id: str,
        max_results_per_page: int = None,
        next_token: str = None,
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
            max_results_per_page: The maximum number of results to return per page.
            next_token: A string token returned in the response of your previous request.
        """
        url = "/finances/v0/orders/{orderId}/financialEvents"
        values = (
            order_id,
            max_results_per_page,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._list_financial_events_by_order_id_params)
        return response

    _list_financial_events_by_order_id_params = (  # name, param in
        ("orderId", "path"),
        ("MaxResultsPerPage", "query"),
        ("NextToken", "query"),
    )
