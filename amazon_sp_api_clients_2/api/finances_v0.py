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

    adjustment_type: str

    adjustment_amount: "Currency"
    adjustment_item_list: "AdjustmentItemList"
    posted_date: "Date"
    pass


@attrs.define
class AdjustmentEventList:

    pass


@attrs.define
class AdjustmentItem:

    asin: str
    fn_sku: str
    product_description: str
    quantity: str
    seller_sku: str

    per_unit_amount: "Currency"
    total_amount: "Currency"
    pass


@attrs.define
class AdjustmentItemList:

    pass


@attrs.define
class AffordabilityExpenseEvent:

    amazon_order_id: str
    marketplace_id: str
    transaction_type: str

    base_expense: "Currency"
    posted_date: "Date"
    tax_type_cgst: "Currency"
    tax_type_igst: "Currency"
    tax_type_sgst: "Currency"
    total_expense: "Currency"
    pass


@attrs.define
class AffordabilityExpenseEventList:

    pass


@attrs.define
class BigDecimal:

    pass


@attrs.define
class ChargeComponent:

    charge_type: str

    charge_amount: "Currency"
    pass


@attrs.define
class ChargeComponentList:

    pass


@attrs.define
class ChargeInstrument:

    description: str
    tail: str

    amount: "Currency"
    pass


@attrs.define
class ChargeInstrumentList:

    pass


@attrs.define
class CouponPaymentEvent:

    clip_or_redemption_count: int
    # {'schema_format': 'int64'}
    coupon_id: str
    payment_event_id: str
    seller_coupon_description: str

    charge_component: "ChargeComponent"
    fee_component: "FeeComponent"
    posted_date: "Date"
    total_amount: "Currency"
    pass


@attrs.define
class CouponPaymentEventList:

    pass


@attrs.define
class Currency:

    currency_code: str

    currency_amount: "BigDecimal"
    pass


@attrs.define
class Date:

    pass


@attrs.define
class DebtRecoveryEvent:

    debt_recovery_type: str

    charge_instrument_list: "ChargeInstrumentList"
    debt_recovery_item_list: "DebtRecoveryItemList"
    over_payment_credit: "Currency"
    recovery_amount: "Currency"
    pass


@attrs.define
class DebtRecoveryEventList:

    pass


@attrs.define
class DebtRecoveryItem:

    group_begin_date: "Date"
    group_end_date: "Date"
    original_amount: "Currency"
    recovery_amount: "Currency"
    pass


@attrs.define
class DebtRecoveryItemList:

    pass


@attrs.define
class DirectPayment:

    direct_payment_type: str

    direct_payment_amount: "Currency"
    pass


@attrs.define
class DirectPaymentList:

    pass


@attrs.define
class Error:

    code: str
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FBALiquidationEvent:

    original_removal_order_id: str

    liquidation_fee_amount: "Currency"
    liquidation_proceeds_amount: "Currency"
    posted_date: "Date"
    pass


@attrs.define
class FBALiquidationEventList:

    pass


@attrs.define
class FeeComponent:

    fee_type: str

    fee_amount: "Currency"
    pass


@attrs.define
class FeeComponentList:

    pass


@attrs.define
class FinancialEventGroup:

    account_tail: str
    financial_event_group_id: str
    fund_transfer_status: str
    processing_status: str
    trace_id: str

    beginning_balance: "Currency"
    converted_total: "Currency"
    financial_event_group_end: "Date"
    financial_event_group_start: "Date"
    fund_transfer_date: "Date"
    original_total: "Currency"
    pass


@attrs.define
class FinancialEventGroupList:

    pass


@attrs.define
class FinancialEvents:

    adjustment_event_list: "AdjustmentEventList"
    affordability_expense_event_list: "AffordabilityExpenseEventList"
    affordability_expense_reversal_event_list: "AffordabilityExpenseEventList"
    chargeback_event_list: "ShipmentEventList"
    coupon_payment_event_list: "CouponPaymentEventList"
    debt_recovery_event_list: "DebtRecoveryEventList"
    fbaliquidation_event_list: "FBALiquidationEventList"
    guarantee_claim_event_list: "ShipmentEventList"
    imaging_services_fee_event_list: "ImagingServicesFeeEventList"
    loan_servicing_event_list: "LoanServicingEventList"
    network_commingling_transaction_event_list: "NetworkComminglingTransactionEventList"
    pay_with_amazon_event_list: "PayWithAmazonEventList"
    product_ads_payment_event_list: "ProductAdsPaymentEventList"
    refund_event_list: "ShipmentEventList"
    removal_shipment_adjustment_event_list: "RemovalShipmentAdjustmentEventList"
    removal_shipment_event_list: "RemovalShipmentEventList"
    rental_transaction_event_list: "RentalTransactionEventList"
    retrocharge_event_list: "RetrochargeEventList"
    safetreimbursement_event_list: "SAFETReimbursementEventList"
    seller_deal_payment_event_list: "SellerDealPaymentEventList"
    seller_review_enrollment_payment_event_list: "SellerReviewEnrollmentPaymentEventList"
    service_fee_event_list: "ServiceFeeEventList"
    service_provider_credit_event_list: "SolutionProviderCreditEventList"
    shipment_event_list: "ShipmentEventList"
    shipment_settle_event_list: "ShipmentSettleEventList"
    tax_withholding_event_list: "TaxWithholdingEventList"
    trial_shipment_event_list: "TrialShipmentEventList"
    pass


@attrs.define
class ImagingServicesFeeEvent:

    asin: str
    imaging_request_billing_item_id: str

    fee_list: "FeeComponentList"
    posted_date: "Date"
    pass


@attrs.define
class ImagingServicesFeeEventList:

    pass


@attrs.define
class ListFinancialEventGroupsPayload:

    next_token: str

    financial_event_group_list: "FinancialEventGroupList"
    pass


@attrs.define
class ListFinancialEventGroupsResponse:

    errors: "ErrorList"
    payload: "ListFinancialEventGroupsPayload"
    pass


@attrs.define
class ListFinancialEventsPayload:

    next_token: str

    financial_events: "FinancialEvents"
    pass


@attrs.define
class ListFinancialEventsResponse:

    errors: "ErrorList"
    payload: "ListFinancialEventsPayload"
    pass


@attrs.define
class LoanServicingEvent:

    source_business_event_type: str

    loan_amount: "Currency"
    pass


@attrs.define
class LoanServicingEventList:

    pass


@attrs.define
class NetworkComminglingTransactionEvent:

    asin: str
    marketplace_id: str
    net_co_transaction_id: str
    swap_reason: str
    transaction_type: str

    posted_date: "Date"
    tax_amount: "Currency"
    tax_exclusive_amount: "Currency"
    pass


@attrs.define
class NetworkComminglingTransactionEventList:

    pass


@attrs.define
class PayWithAmazonEvent:

    amount_description: str
    business_object_type: str
    fulfillment_channel: str
    payment_amount_type: str
    sales_channel: str
    seller_order_id: str
    store_name: str

    charge: "ChargeComponent"
    fee_list: "FeeComponentList"
    transaction_posted_date: "Date"
    pass


@attrs.define
class PayWithAmazonEventList:

    pass


@attrs.define
class ProductAdsPaymentEvent:

    invoice_id: str
    transaction_type: str

    base_value: "Currency"
    posted_date: "Date"
    tax_value: "Currency"
    transaction_value: "Currency"
    pass


@attrs.define
class ProductAdsPaymentEventList:

    pass


@attrs.define
class Promotion:

    promotion_id: str
    promotion_type: str

    promotion_amount: "Currency"
    pass


@attrs.define
class PromotionList:

    pass


@attrs.define
class RemovalShipmentAdjustmentEvent:

    adjustment_event_id: str
    merchant_order_id: str
    order_id: str
    removal_shipment_item_adjustment_list: list["RemovalShipmentItemAdjustment"]
    transaction_type: str

    posted_date: "Date"
    pass


@attrs.define
class RemovalShipmentAdjustmentEventList:

    pass


@attrs.define
class RemovalShipmentEvent:

    merchant_order_id: str
    order_id: str
    transaction_type: str

    posted_date: "Date"
    removal_shipment_item_list: "RemovalShipmentItemList"
    pass


@attrs.define
class RemovalShipmentEventList:

    pass


@attrs.define
class RemovalShipmentItem:

    fulfillment_network_sku: str
    quantity: int
    # {'schema_format': 'int32'}
    removal_shipment_item_id: str
    tax_collection_model: str

    fee_amount: "Currency"
    revenue: "Currency"
    tax_amount: "Currency"
    tax_withheld: "Currency"
    pass


@attrs.define
class RemovalShipmentItemAdjustment:

    adjusted_quantity: int
    # {'schema_format': 'int32'}
    fulfillment_network_sku: str
    removal_shipment_item_id: str
    tax_collection_model: str

    revenue_adjustment: "Currency"
    tax_amount_adjustment: "Currency"
    tax_withheld_adjustment: "Currency"
    pass


@attrs.define
class RemovalShipmentItemList:

    pass


@attrs.define
class RentalTransactionEvent:

    amazon_order_id: str
    extension_length: int
    # {'schema_format': 'int32'}
    marketplace_name: str
    rental_event_type: str

    posted_date: "Date"
    rental_charge_list: "ChargeComponentList"
    rental_fee_list: "FeeComponentList"
    rental_initial_value: "Currency"
    rental_reimbursement: "Currency"
    rental_tax_withheld_list: "TaxWithheldComponentList"
    pass


@attrs.define
class RentalTransactionEventList:

    pass


@attrs.define
class RetrochargeEvent:

    amazon_order_id: str
    marketplace_name: str
    retrocharge_event_type: str

    base_tax: "Currency"
    posted_date: "Date"
    retrocharge_tax_withheld_list: "TaxWithheldComponentList"
    shipping_tax: "Currency"
    pass


@attrs.define
class RetrochargeEventList:

    pass


@attrs.define
class SAFETReimbursementEvent:

    reason_code: str
    safetclaim_id: str

    posted_date: "Date"
    reimbursed_amount: "Currency"
    safetreimbursement_item_list: "SAFETReimbursementItemList"
    pass


@attrs.define
class SAFETReimbursementEventList:

    pass


@attrs.define
class SAFETReimbursementItem:

    product_description: str
    quantity: str

    item_charge_list: "ChargeComponentList"
    pass


@attrs.define
class SAFETReimbursementItemList:

    pass


@attrs.define
class SellerDealPaymentEvent:

    deal_description: str
    deal_id: str
    event_type: str
    fee_type: str

    fee_amount: "Currency"
    posted_date: "Date"
    tax_amount: "Currency"
    total_amount: "Currency"
    pass


@attrs.define
class SellerDealPaymentEventList:

    pass


@attrs.define
class SellerReviewEnrollmentPaymentEvent:

    enrollment_id: str
    parent_asin: str

    charge_component: "ChargeComponent"
    fee_component: "FeeComponent"
    posted_date: "Date"
    total_amount: "Currency"
    pass


@attrs.define
class SellerReviewEnrollmentPaymentEventList:

    pass


@attrs.define
class ServiceFeeEvent:

    asin: str
    amazon_order_id: str
    fee_description: str
    fee_reason: str
    fn_sku: str
    seller_sku: str

    fee_list: "FeeComponentList"
    pass


@attrs.define
class ServiceFeeEventList:

    pass


@attrs.define
class ShipmentEvent:

    amazon_order_id: str
    marketplace_name: str
    seller_order_id: str

    direct_payment_list: "DirectPaymentList"
    order_charge_adjustment_list: "ChargeComponentList"
    order_charge_list: "ChargeComponentList"
    order_fee_adjustment_list: "FeeComponentList"
    order_fee_list: "FeeComponentList"
    posted_date: "Date"
    shipment_fee_adjustment_list: "FeeComponentList"
    shipment_fee_list: "FeeComponentList"
    shipment_item_adjustment_list: "ShipmentItemList"
    shipment_item_list: "ShipmentItemList"
    pass


@attrs.define
class ShipmentEventList:

    pass


@attrs.define
class ShipmentItem:

    order_adjustment_item_id: str
    order_item_id: str
    quantity_shipped: int
    # {'schema_format': 'int32'}
    seller_sku: str

    cost_of_points_granted: "Currency"
    cost_of_points_returned: "Currency"
    item_charge_adjustment_list: "ChargeComponentList"
    item_charge_list: "ChargeComponentList"
    item_fee_adjustment_list: "FeeComponentList"
    item_fee_list: "FeeComponentList"
    item_tax_withheld_list: "TaxWithheldComponentList"
    promotion_adjustment_list: "PromotionList"
    promotion_list: "PromotionList"
    pass


@attrs.define
class ShipmentItemList:

    pass


@attrs.define
class ShipmentSettleEventList:

    pass


@attrs.define
class SolutionProviderCreditEvent:

    marketplace_country_code: str
    marketplace_id: str
    provider_id: str
    provider_store_name: str
    provider_transaction_type: str
    seller_id: str
    seller_order_id: str
    seller_store_name: str

    transaction_amount: "Currency"
    transaction_creation_date: "Date"
    pass


@attrs.define
class SolutionProviderCreditEventList:

    pass


@attrs.define
class TaxWithheldComponent:

    tax_collection_model: str

    taxes_withheld: "ChargeComponentList"
    pass


@attrs.define
class TaxWithheldComponentList:

    pass


@attrs.define
class TaxWithholdingEvent:

    base_amount: "Currency"
    posted_date: "Date"
    tax_withholding_period: "TaxWithholdingPeriod"
    withheld_amount: "Currency"
    pass


@attrs.define
class TaxWithholdingEventList:

    pass


@attrs.define
class TaxWithholdingPeriod:

    end_date: "Date"
    start_date: "Date"
    pass


@attrs.define
class TrialShipmentEvent:

    amazon_order_id: str
    financial_event_group_id: str
    sku: str

    fee_list: "FeeComponentList"
    posted_date: "Date"
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
