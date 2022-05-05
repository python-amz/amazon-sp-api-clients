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

    adjustment_type: str = attrs.field()

    adjustment_amount: "Currency" = attrs.field()
    adjustment_item_list: "AdjustmentItemList" = attrs.field()
    posted_date: "Date" = attrs.field()
    pass


@attrs.define
class AdjustmentEventList:

    pass


@attrs.define
class AdjustmentItem:

    asin: str = attrs.field()
    fn_sku: str = attrs.field()
    product_description: str = attrs.field()
    quantity: str = attrs.field()
    seller_sku: str = attrs.field()

    per_unit_amount: "Currency" = attrs.field()
    total_amount: "Currency" = attrs.field()
    pass


@attrs.define
class AdjustmentItemList:

    pass


@attrs.define
class AffordabilityExpenseEvent:

    amazon_order_id: str = attrs.field()
    marketplace_id: str = attrs.field()
    transaction_type: str = attrs.field()

    base_expense: "Currency" = attrs.field()
    posted_date: "Date" = attrs.field()
    tax_type_cgst: "Currency" = attrs.field()
    tax_type_igst: "Currency" = attrs.field()
    tax_type_sgst: "Currency" = attrs.field()
    total_expense: "Currency" = attrs.field()
    pass


@attrs.define
class AffordabilityExpenseEventList:

    pass


@attrs.define
class BigDecimal:

    pass


@attrs.define
class ChargeComponent:

    charge_type: str = attrs.field()

    charge_amount: "Currency" = attrs.field()
    pass


@attrs.define
class ChargeComponentList:

    pass


@attrs.define
class ChargeInstrument:

    description: str = attrs.field()
    tail: str = attrs.field()

    amount: "Currency" = attrs.field()
    pass


@attrs.define
class ChargeInstrumentList:

    pass


@attrs.define
class CouponPaymentEvent:

    clip_or_redemption_count: int = attrs.field()
    # {'schema_format': 'int64'}
    coupon_id: str = attrs.field()
    payment_event_id: str = attrs.field()
    seller_coupon_description: str = attrs.field()

    charge_component: "ChargeComponent" = attrs.field()
    fee_component: "FeeComponent" = attrs.field()
    posted_date: "Date" = attrs.field()
    total_amount: "Currency" = attrs.field()
    pass


@attrs.define
class CouponPaymentEventList:

    pass


@attrs.define
class Currency:

    currency_code: str = attrs.field()

    currency_amount: "BigDecimal" = attrs.field()
    pass


@attrs.define
class Date:

    pass


@attrs.define
class DebtRecoveryEvent:

    debt_recovery_type: str = attrs.field()

    charge_instrument_list: "ChargeInstrumentList" = attrs.field()
    debt_recovery_item_list: "DebtRecoveryItemList" = attrs.field()
    over_payment_credit: "Currency" = attrs.field()
    recovery_amount: "Currency" = attrs.field()
    pass


@attrs.define
class DebtRecoveryEventList:

    pass


@attrs.define
class DebtRecoveryItem:

    group_begin_date: "Date" = attrs.field()
    group_end_date: "Date" = attrs.field()
    original_amount: "Currency" = attrs.field()
    recovery_amount: "Currency" = attrs.field()
    pass


@attrs.define
class DebtRecoveryItemList:

    pass


@attrs.define
class DirectPayment:

    direct_payment_type: str = attrs.field()

    direct_payment_amount: "Currency" = attrs.field()
    pass


@attrs.define
class DirectPaymentList:

    pass


@attrs.define
class Error:

    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FBALiquidationEvent:

    original_removal_order_id: str = attrs.field()

    liquidation_fee_amount: "Currency" = attrs.field()
    liquidation_proceeds_amount: "Currency" = attrs.field()
    posted_date: "Date" = attrs.field()
    pass


@attrs.define
class FBALiquidationEventList:

    pass


@attrs.define
class FeeComponent:

    fee_type: str = attrs.field()

    fee_amount: "Currency" = attrs.field()
    pass


@attrs.define
class FeeComponentList:

    pass


@attrs.define
class FinancialEventGroup:

    account_tail: str = attrs.field()
    financial_event_group_id: str = attrs.field()
    fund_transfer_status: str = attrs.field()
    processing_status: str = attrs.field()
    trace_id: str = attrs.field()

    beginning_balance: "Currency" = attrs.field()
    converted_total: "Currency" = attrs.field()
    financial_event_group_end: "Date" = attrs.field()
    financial_event_group_start: "Date" = attrs.field()
    fund_transfer_date: "Date" = attrs.field()
    original_total: "Currency" = attrs.field()
    pass


@attrs.define
class FinancialEventGroupList:

    pass


@attrs.define
class FinancialEvents:

    adjustment_event_list: "AdjustmentEventList" = attrs.field()
    affordability_expense_event_list: "AffordabilityExpenseEventList" = attrs.field()
    affordability_expense_reversal_event_list: "AffordabilityExpenseEventList" = attrs.field()
    chargeback_event_list: "ShipmentEventList" = attrs.field()
    coupon_payment_event_list: "CouponPaymentEventList" = attrs.field()
    debt_recovery_event_list: "DebtRecoveryEventList" = attrs.field()
    fbaliquidation_event_list: "FBALiquidationEventList" = attrs.field()
    guarantee_claim_event_list: "ShipmentEventList" = attrs.field()
    imaging_services_fee_event_list: "ImagingServicesFeeEventList" = attrs.field()
    loan_servicing_event_list: "LoanServicingEventList" = attrs.field()
    network_commingling_transaction_event_list: "NetworkComminglingTransactionEventList" = attrs.field()
    pay_with_amazon_event_list: "PayWithAmazonEventList" = attrs.field()
    product_ads_payment_event_list: "ProductAdsPaymentEventList" = attrs.field()
    refund_event_list: "ShipmentEventList" = attrs.field()
    removal_shipment_adjustment_event_list: "RemovalShipmentAdjustmentEventList" = attrs.field()
    removal_shipment_event_list: "RemovalShipmentEventList" = attrs.field()
    rental_transaction_event_list: "RentalTransactionEventList" = attrs.field()
    retrocharge_event_list: "RetrochargeEventList" = attrs.field()
    safetreimbursement_event_list: "SAFETReimbursementEventList" = attrs.field()
    seller_deal_payment_event_list: "SellerDealPaymentEventList" = attrs.field()
    seller_review_enrollment_payment_event_list: "SellerReviewEnrollmentPaymentEventList" = attrs.field()
    service_fee_event_list: "ServiceFeeEventList" = attrs.field()
    service_provider_credit_event_list: "SolutionProviderCreditEventList" = attrs.field()
    shipment_event_list: "ShipmentEventList" = attrs.field()
    shipment_settle_event_list: "ShipmentSettleEventList" = attrs.field()
    tax_withholding_event_list: "TaxWithholdingEventList" = attrs.field()
    trial_shipment_event_list: "TrialShipmentEventList" = attrs.field()
    pass


@attrs.define
class ImagingServicesFeeEvent:

    asin: str = attrs.field()
    imaging_request_billing_item_id: str = attrs.field()

    fee_list: "FeeComponentList" = attrs.field()
    posted_date: "Date" = attrs.field()
    pass


@attrs.define
class ImagingServicesFeeEventList:

    pass


@attrs.define
class ListFinancialEventGroupsPayload:

    next_token: str = attrs.field()

    financial_event_group_list: "FinancialEventGroupList" = attrs.field()
    pass


@attrs.define
class ListFinancialEventGroupsResponse:

    errors: "ErrorList" = attrs.field()
    payload: "ListFinancialEventGroupsPayload" = attrs.field()
    pass


@attrs.define
class ListFinancialEventsPayload:

    next_token: str = attrs.field()

    financial_events: "FinancialEvents" = attrs.field()
    pass


@attrs.define
class ListFinancialEventsResponse:

    errors: "ErrorList" = attrs.field()
    payload: "ListFinancialEventsPayload" = attrs.field()
    pass


@attrs.define
class LoanServicingEvent:

    source_business_event_type: str = attrs.field()

    loan_amount: "Currency" = attrs.field()
    pass


@attrs.define
class LoanServicingEventList:

    pass


@attrs.define
class NetworkComminglingTransactionEvent:

    asin: str = attrs.field()
    marketplace_id: str = attrs.field()
    net_co_transaction_id: str = attrs.field()
    swap_reason: str = attrs.field()
    transaction_type: str = attrs.field()

    posted_date: "Date" = attrs.field()
    tax_amount: "Currency" = attrs.field()
    tax_exclusive_amount: "Currency" = attrs.field()
    pass


@attrs.define
class NetworkComminglingTransactionEventList:

    pass


@attrs.define
class PayWithAmazonEvent:

    amount_description: str = attrs.field()
    business_object_type: str = attrs.field()
    fulfillment_channel: str = attrs.field()
    payment_amount_type: str = attrs.field()
    sales_channel: str = attrs.field()
    seller_order_id: str = attrs.field()
    store_name: str = attrs.field()

    charge: "ChargeComponent" = attrs.field()
    fee_list: "FeeComponentList" = attrs.field()
    transaction_posted_date: "Date" = attrs.field()
    pass


@attrs.define
class PayWithAmazonEventList:

    pass


@attrs.define
class ProductAdsPaymentEvent:

    invoice_id: str = attrs.field()
    transaction_type: str = attrs.field()

    base_value: "Currency" = attrs.field()
    posted_date: "Date" = attrs.field()
    tax_value: "Currency" = attrs.field()
    transaction_value: "Currency" = attrs.field()
    pass


@attrs.define
class ProductAdsPaymentEventList:

    pass


@attrs.define
class Promotion:

    promotion_id: str = attrs.field()
    promotion_type: str = attrs.field()

    promotion_amount: "Currency" = attrs.field()
    pass


@attrs.define
class PromotionList:

    pass


@attrs.define
class RemovalShipmentAdjustmentEvent:

    adjustment_event_id: str = attrs.field()
    merchant_order_id: str = attrs.field()
    order_id: str = attrs.field()
    removal_shipment_item_adjustment_list: list["RemovalShipmentItemAdjustment"] = attrs.field()
    transaction_type: str = attrs.field()

    posted_date: "Date" = attrs.field()
    pass


@attrs.define
class RemovalShipmentAdjustmentEventList:

    pass


@attrs.define
class RemovalShipmentEvent:

    merchant_order_id: str = attrs.field()
    order_id: str = attrs.field()
    transaction_type: str = attrs.field()

    posted_date: "Date" = attrs.field()
    removal_shipment_item_list: "RemovalShipmentItemList" = attrs.field()
    pass


@attrs.define
class RemovalShipmentEventList:

    pass


@attrs.define
class RemovalShipmentItem:

    fulfillment_network_sku: str = attrs.field()
    quantity: int = attrs.field()
    # {'schema_format': 'int32'}
    removal_shipment_item_id: str = attrs.field()
    tax_collection_model: str = attrs.field()

    fee_amount: "Currency" = attrs.field()
    revenue: "Currency" = attrs.field()
    tax_amount: "Currency" = attrs.field()
    tax_withheld: "Currency" = attrs.field()
    pass


@attrs.define
class RemovalShipmentItemAdjustment:

    adjusted_quantity: int = attrs.field()
    # {'schema_format': 'int32'}
    fulfillment_network_sku: str = attrs.field()
    removal_shipment_item_id: str = attrs.field()
    tax_collection_model: str = attrs.field()

    revenue_adjustment: "Currency" = attrs.field()
    tax_amount_adjustment: "Currency" = attrs.field()
    tax_withheld_adjustment: "Currency" = attrs.field()
    pass


@attrs.define
class RemovalShipmentItemList:

    pass


@attrs.define
class RentalTransactionEvent:

    amazon_order_id: str = attrs.field()
    extension_length: int = attrs.field()
    # {'schema_format': 'int32'}
    marketplace_name: str = attrs.field()
    rental_event_type: str = attrs.field()

    posted_date: "Date" = attrs.field()
    rental_charge_list: "ChargeComponentList" = attrs.field()
    rental_fee_list: "FeeComponentList" = attrs.field()
    rental_initial_value: "Currency" = attrs.field()
    rental_reimbursement: "Currency" = attrs.field()
    rental_tax_withheld_list: "TaxWithheldComponentList" = attrs.field()
    pass


@attrs.define
class RentalTransactionEventList:

    pass


@attrs.define
class RetrochargeEvent:

    amazon_order_id: str = attrs.field()
    marketplace_name: str = attrs.field()
    retrocharge_event_type: str = attrs.field()

    base_tax: "Currency" = attrs.field()
    posted_date: "Date" = attrs.field()
    retrocharge_tax_withheld_list: "TaxWithheldComponentList" = attrs.field()
    shipping_tax: "Currency" = attrs.field()
    pass


@attrs.define
class RetrochargeEventList:

    pass


@attrs.define
class SAFETReimbursementEvent:

    reason_code: str = attrs.field()
    safetclaim_id: str = attrs.field()

    posted_date: "Date" = attrs.field()
    reimbursed_amount: "Currency" = attrs.field()
    safetreimbursement_item_list: "SAFETReimbursementItemList" = attrs.field()
    pass


@attrs.define
class SAFETReimbursementEventList:

    pass


@attrs.define
class SAFETReimbursementItem:

    product_description: str = attrs.field()
    quantity: str = attrs.field()

    item_charge_list: "ChargeComponentList" = attrs.field()
    pass


@attrs.define
class SAFETReimbursementItemList:

    pass


@attrs.define
class SellerDealPaymentEvent:

    deal_description: str = attrs.field()
    deal_id: str = attrs.field()
    event_type: str = attrs.field()
    fee_type: str = attrs.field()

    fee_amount: "Currency" = attrs.field()
    posted_date: "Date" = attrs.field()
    tax_amount: "Currency" = attrs.field()
    total_amount: "Currency" = attrs.field()
    pass


@attrs.define
class SellerDealPaymentEventList:

    pass


@attrs.define
class SellerReviewEnrollmentPaymentEvent:

    enrollment_id: str = attrs.field()
    parent_asin: str = attrs.field()

    charge_component: "ChargeComponent" = attrs.field()
    fee_component: "FeeComponent" = attrs.field()
    posted_date: "Date" = attrs.field()
    total_amount: "Currency" = attrs.field()
    pass


@attrs.define
class SellerReviewEnrollmentPaymentEventList:

    pass


@attrs.define
class ServiceFeeEvent:

    asin: str = attrs.field()
    amazon_order_id: str = attrs.field()
    fee_description: str = attrs.field()
    fee_reason: str = attrs.field()
    fn_sku: str = attrs.field()
    seller_sku: str = attrs.field()

    fee_list: "FeeComponentList" = attrs.field()
    pass


@attrs.define
class ServiceFeeEventList:

    pass


@attrs.define
class ShipmentEvent:

    amazon_order_id: str = attrs.field()
    marketplace_name: str = attrs.field()
    seller_order_id: str = attrs.field()

    direct_payment_list: "DirectPaymentList" = attrs.field()
    order_charge_adjustment_list: "ChargeComponentList" = attrs.field()
    order_charge_list: "ChargeComponentList" = attrs.field()
    order_fee_adjustment_list: "FeeComponentList" = attrs.field()
    order_fee_list: "FeeComponentList" = attrs.field()
    posted_date: "Date" = attrs.field()
    shipment_fee_adjustment_list: "FeeComponentList" = attrs.field()
    shipment_fee_list: "FeeComponentList" = attrs.field()
    shipment_item_adjustment_list: "ShipmentItemList" = attrs.field()
    shipment_item_list: "ShipmentItemList" = attrs.field()
    pass


@attrs.define
class ShipmentEventList:

    pass


@attrs.define
class ShipmentItem:

    order_adjustment_item_id: str = attrs.field()
    order_item_id: str = attrs.field()
    quantity_shipped: int = attrs.field()
    # {'schema_format': 'int32'}
    seller_sku: str = attrs.field()

    cost_of_points_granted: "Currency" = attrs.field()
    cost_of_points_returned: "Currency" = attrs.field()
    item_charge_adjustment_list: "ChargeComponentList" = attrs.field()
    item_charge_list: "ChargeComponentList" = attrs.field()
    item_fee_adjustment_list: "FeeComponentList" = attrs.field()
    item_fee_list: "FeeComponentList" = attrs.field()
    item_tax_withheld_list: "TaxWithheldComponentList" = attrs.field()
    promotion_adjustment_list: "PromotionList" = attrs.field()
    promotion_list: "PromotionList" = attrs.field()
    pass


@attrs.define
class ShipmentItemList:

    pass


@attrs.define
class ShipmentSettleEventList:

    pass


@attrs.define
class SolutionProviderCreditEvent:

    marketplace_country_code: str = attrs.field()
    marketplace_id: str = attrs.field()
    provider_id: str = attrs.field()
    provider_store_name: str = attrs.field()
    provider_transaction_type: str = attrs.field()
    seller_id: str = attrs.field()
    seller_order_id: str = attrs.field()
    seller_store_name: str = attrs.field()

    transaction_amount: "Currency" = attrs.field()
    transaction_creation_date: "Date" = attrs.field()
    pass


@attrs.define
class SolutionProviderCreditEventList:

    pass


@attrs.define
class TaxWithheldComponent:

    tax_collection_model: str = attrs.field()

    taxes_withheld: "ChargeComponentList" = attrs.field()
    pass


@attrs.define
class TaxWithheldComponentList:

    pass


@attrs.define
class TaxWithholdingEvent:

    base_amount: "Currency" = attrs.field()
    posted_date: "Date" = attrs.field()
    tax_withholding_period: "TaxWithholdingPeriod" = attrs.field()
    withheld_amount: "Currency" = attrs.field()
    pass


@attrs.define
class TaxWithholdingEventList:

    pass


@attrs.define
class TaxWithholdingPeriod:

    end_date: "Date" = attrs.field()
    start_date: "Date" = attrs.field()
    pass


@attrs.define
class TrialShipmentEvent:

    amazon_order_id: str = attrs.field()
    financial_event_group_id: str = attrs.field()
    sku: str = attrs.field()

    fee_list: "FeeComponentList" = attrs.field()
    posted_date: "Date" = attrs.field()
    pass


@attrs.define
class TrialShipmentEventList:

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
