"""
Selling Partner API for Finances
=============================================================================================

The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AdjustmentEvent:
    pass


@attrs.define
class AdjustmentEventList:
    pass


@attrs.define
class AdjustmentItem:
    pass


@attrs.define
class AdjustmentItemList:
    pass


@attrs.define
class AffordabilityExpenseEvent:
    pass


@attrs.define
class AffordabilityExpenseEventList:
    pass


@attrs.define
class BigDecimal:
    pass


@attrs.define
class ChargeComponent:
    pass


@attrs.define
class ChargeComponentList:
    pass


@attrs.define
class ChargeInstrument:
    pass


@attrs.define
class ChargeInstrumentList:
    pass


@attrs.define
class CouponPaymentEvent:
    pass


@attrs.define
class CouponPaymentEventList:
    pass


@attrs.define
class Currency:
    pass


@attrs.define
class Date:
    pass


@attrs.define
class DebtRecoveryEvent:
    pass


@attrs.define
class DebtRecoveryEventList:
    pass


@attrs.define
class DebtRecoveryItem:
    pass


@attrs.define
class DebtRecoveryItemList:
    pass


@attrs.define
class DirectPayment:
    pass


@attrs.define
class DirectPaymentList:
    pass


@attrs.define
class FBALiquidationEvent:
    pass


@attrs.define
class FBALiquidationEventList:
    pass


@attrs.define
class FeeComponent:
    pass


@attrs.define
class FeeComponentList:
    pass


@attrs.define
class FinancialEventGroup:
    pass


@attrs.define
class FinancialEventGroupList:
    pass


@attrs.define
class FinancialEvents:
    pass


@attrs.define
class ImagingServicesFeeEvent:
    pass


@attrs.define
class ImagingServicesFeeEventList:
    pass


@attrs.define
class ListFinancialEventGroupsPayload:
    pass


@attrs.define
class ListFinancialEventGroupsResponse:
    pass


@attrs.define
class ListFinancialEventsPayload:
    pass


@attrs.define
class ListFinancialEventsResponse:
    pass


@attrs.define
class LoanServicingEvent:
    pass


@attrs.define
class LoanServicingEventList:
    pass


@attrs.define
class NetworkComminglingTransactionEvent:
    pass


@attrs.define
class NetworkComminglingTransactionEventList:
    pass


@attrs.define
class PayWithAmazonEvent:
    pass


@attrs.define
class PayWithAmazonEventList:
    pass


@attrs.define
class ProductAdsPaymentEvent:
    pass


@attrs.define
class ProductAdsPaymentEventList:
    pass


@attrs.define
class Promotion:
    pass


@attrs.define
class PromotionList:
    pass


@attrs.define
class RemovalShipmentEvent:
    pass


@attrs.define
class RemovalShipmentEventList:
    pass


@attrs.define
class RemovalShipmentItem:
    pass


@attrs.define
class RemovalShipmentItemList:
    pass


@attrs.define
class RemovalShipmentAdjustmentEvent:
    pass


@attrs.define
class RemovalShipmentAdjustmentEventList:
    pass


@attrs.define
class RemovalShipmentItemAdjustment:
    pass


@attrs.define
class RentalTransactionEvent:
    pass


@attrs.define
class RentalTransactionEventList:
    pass


@attrs.define
class RetrochargeEvent:
    pass


@attrs.define
class RetrochargeEventList:
    pass


@attrs.define
class SAFETReimbursementEvent:
    pass


@attrs.define
class SAFETReimbursementEventList:
    pass


@attrs.define
class SAFETReimbursementItem:
    pass


@attrs.define
class SAFETReimbursementItemList:
    pass


@attrs.define
class SellerDealPaymentEvent:
    pass


@attrs.define
class SellerDealPaymentEventList:
    pass


@attrs.define
class SellerReviewEnrollmentPaymentEvent:
    pass


@attrs.define
class SellerReviewEnrollmentPaymentEventList:
    pass


@attrs.define
class ServiceFeeEvent:
    pass


@attrs.define
class ServiceFeeEventList:
    pass


@attrs.define
class ShipmentEvent:
    pass


@attrs.define
class ShipmentEventList:
    pass


@attrs.define
class ShipmentItem:
    pass


@attrs.define
class ShipmentItemList:
    pass


@attrs.define
class SolutionProviderCreditEvent:
    pass


@attrs.define
class SolutionProviderCreditEventList:
    pass


@attrs.define
class TaxWithholdingPeriod:
    pass


@attrs.define
class TaxWithholdingEvent:
    pass


@attrs.define
class TaxWithholdingEventList:
    pass


@attrs.define
class TaxWithheldComponent:
    pass


@attrs.define
class TaxWithheldComponentList:
    pass


@attrs.define
class TrialShipmentEvent:
    pass


@attrs.define
class TrialShipmentEventList:
    pass


@attrs.define
class ShipmentSettleEventList:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
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
