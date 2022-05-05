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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    adjustment_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    adjustment_item_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/AdjustmentItemList'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class AdjustmentEventList:

    pass


@attrs.define
class AdjustmentItem:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fn_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    product_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    quantity: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    per_unit_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    total_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class AdjustmentItemList:

    pass


@attrs.define
class AffordabilityExpenseEvent:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    transaction_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    base_expense: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    tax_type_cgst: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_type_igst: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_type_sgst: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    total_expense: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    charge_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class ChargeComponentList:

    pass


@attrs.define
class ChargeInstrument:

    description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    tail: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class ChargeInstrumentList:

    pass


@attrs.define
class CouponPaymentEvent:

    clip_or_redemption_count: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'integer', 'schema_format': 'int64'}
    coupon_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    payment_event_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_coupon_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    charge_component: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponent'}
    fee_component: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponent'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    total_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class CouponPaymentEventList:

    pass


@attrs.define
class Currency:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    currency_amount: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/BigDecimal'}
    pass


@attrs.define
class Date:

    pass


@attrs.define
class DebtRecoveryEvent:

    debt_recovery_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    charge_instrument_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeInstrumentList'}
    debt_recovery_item_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/DebtRecoveryItemList'}
    over_payment_credit: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    recovery_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class DebtRecoveryEventList:

    pass


@attrs.define
class DebtRecoveryItem:

    group_begin_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    group_end_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    original_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    recovery_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class DebtRecoveryItemList:

    pass


@attrs.define
class DirectPayment:

    direct_payment_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    direct_payment_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class DirectPaymentList:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FBALiquidationEvent:

    original_removal_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    liquidation_fee_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    liquidation_proceeds_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class FBALiquidationEventList:

    pass


@attrs.define
class FeeComponent:

    fee_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    fee_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class FeeComponentList:

    pass


@attrs.define
class FinancialEventGroup:

    account_tail: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    financial_event_group_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fund_transfer_status: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    processing_status: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    trace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    beginning_balance: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    converted_total: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    financial_event_group_end: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    financial_event_group_start: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    fund_transfer_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    original_total: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class FinancialEventGroupList:

    pass


@attrs.define
class FinancialEvents:

    adjustment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/AdjustmentEventList'}
    affordability_expense_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/AffordabilityExpenseEventList'}
    affordability_expense_reversal_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/AffordabilityExpenseEventList'}
    chargeback_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentEventList'}
    coupon_payment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/CouponPaymentEventList'}
    debt_recovery_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/DebtRecoveryEventList'}
    fbaliquidation_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FBALiquidationEventList'}
    guarantee_claim_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentEventList'}
    imaging_services_fee_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ImagingServicesFeeEventList'}
    loan_servicing_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/LoanServicingEventList'}
    network_commingling_transaction_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/NetworkComminglingTransactionEventList'}
    pay_with_amazon_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/PayWithAmazonEventList'}
    product_ads_payment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ProductAdsPaymentEventList'}
    refund_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentEventList'}
    removal_shipment_adjustment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/RemovalShipmentAdjustmentEventList'}
    removal_shipment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/RemovalShipmentEventList'}
    rental_transaction_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/RentalTransactionEventList'}
    retrocharge_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/RetrochargeEventList'}
    safetreimbursement_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/SAFETReimbursementEventList'}
    seller_deal_payment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/SellerDealPaymentEventList'}
    seller_review_enrollment_payment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/SellerReviewEnrollmentPaymentEventList'}
    service_fee_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ServiceFeeEventList'}
    service_provider_credit_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/SolutionProviderCreditEventList'}
    shipment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentEventList'}
    shipment_settle_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentSettleEventList'}
    tax_withholding_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/TaxWithholdingEventList'}
    trial_shipment_event_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/TrialShipmentEventList'}
    pass


@attrs.define
class ImagingServicesFeeEvent:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    imaging_request_billing_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class ImagingServicesFeeEventList:

    pass


@attrs.define
class ListFinancialEventGroupsPayload:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    financial_event_group_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FinancialEventGroupList'}
    pass


@attrs.define
class ListFinancialEventGroupsResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ListFinancialEventGroupsPayload'}
    pass


@attrs.define
class ListFinancialEventsPayload:

    next_token: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    financial_events: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FinancialEvents'}
    pass


@attrs.define
class ListFinancialEventsResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ListFinancialEventsPayload'}
    pass


@attrs.define
class LoanServicingEvent:

    source_business_event_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    loan_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class LoanServicingEventList:

    pass


@attrs.define
class NetworkComminglingTransactionEvent:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    net_co_transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    swap_reason: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    transaction_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_exclusive_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class NetworkComminglingTransactionEventList:

    pass


@attrs.define
class PayWithAmazonEvent:

    amount_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    business_object_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fulfillment_channel: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    payment_amount_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    sales_channel: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    store_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    charge: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponent'}
    fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    transaction_posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class PayWithAmazonEventList:

    pass


@attrs.define
class ProductAdsPaymentEvent:

    invoice_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    transaction_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    base_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    tax_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    transaction_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class ProductAdsPaymentEventList:

    pass


@attrs.define
class Promotion:

    promotion_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    promotion_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    promotion_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class PromotionList:

    pass


@attrs.define
class RemovalShipmentAdjustmentEvent:

    adjustment_event_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    merchant_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    removal_shipment_item_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'array', 'items': Reference(ref='#/components/schemas/RemovalShipmentItemAdjustment')}
    transaction_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class RemovalShipmentAdjustmentEventList:

    pass


@attrs.define
class RemovalShipmentEvent:

    merchant_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    transaction_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    removal_shipment_item_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/RemovalShipmentItemList'}
    pass


@attrs.define
class RemovalShipmentEventList:

    pass


@attrs.define
class RemovalShipmentItem:

    fulfillment_network_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    quantity: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'integer', 'schema_format': 'int32'}
    removal_shipment_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    tax_collection_model: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    fee_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    revenue: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_withheld: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class RemovalShipmentItemAdjustment:

    adjusted_quantity: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'integer', 'schema_format': 'int32'}
    fulfillment_network_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    removal_shipment_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    tax_collection_model: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    revenue_adjustment: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_amount_adjustment: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    tax_withheld_adjustment: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class RemovalShipmentItemList:

    pass


@attrs.define
class RentalTransactionEvent:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    extension_length: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'integer', 'schema_format': 'int32'}
    marketplace_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    rental_event_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    rental_charge_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    rental_fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    rental_initial_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    rental_reimbursement: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    rental_tax_withheld_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/TaxWithheldComponentList'}
    pass


@attrs.define
class RentalTransactionEventList:

    pass


@attrs.define
class RetrochargeEvent:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    marketplace_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    retrocharge_event_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    base_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    retrocharge_tax_withheld_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/TaxWithheldComponentList'}
    shipping_tax: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class RetrochargeEventList:

    pass


@attrs.define
class SAFETReimbursementEvent:

    reason_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    safetclaim_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    reimbursed_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    safetreimbursement_item_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/SAFETReimbursementItemList'}
    pass


@attrs.define
class SAFETReimbursementEventList:

    pass


@attrs.define
class SAFETReimbursementItem:

    product_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    quantity: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    item_charge_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    pass


@attrs.define
class SAFETReimbursementItemList:

    pass


@attrs.define
class SellerDealPaymentEvent:

    deal_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    deal_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    event_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fee_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    fee_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    total_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class SellerDealPaymentEventList:

    pass


@attrs.define
class SellerReviewEnrollmentPaymentEvent:

    enrollment_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    parent_asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    charge_component: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponent'}
    fee_component: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponent'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    total_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class SellerReviewEnrollmentPaymentEventList:

    pass


@attrs.define
class ServiceFeeEvent:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fee_description: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fee_reason: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    fn_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    pass


@attrs.define
class ServiceFeeEventList:

    pass


@attrs.define
class ShipmentEvent:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    marketplace_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    direct_payment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/DirectPaymentList'}
    order_charge_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    order_charge_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    order_fee_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    order_fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    shipment_fee_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    shipment_fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    shipment_item_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentItemList'}
    shipment_item_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ShipmentItemList'}
    pass


@attrs.define
class ShipmentEventList:

    pass


@attrs.define
class ShipmentItem:

    order_adjustment_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    quantity_shipped: int
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'integer', 'schema_format': 'int32'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    cost_of_points_granted: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    cost_of_points_returned: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    item_charge_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    item_charge_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    item_fee_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    item_fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    item_tax_withheld_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/TaxWithheldComponentList'}
    promotion_adjustment_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/PromotionList'}
    promotion_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/PromotionList'}
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
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    provider_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    provider_store_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    provider_transaction_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    seller_store_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    transaction_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    transaction_creation_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class SolutionProviderCreditEventList:

    pass


@attrs.define
class TaxWithheldComponent:

    tax_collection_model: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    taxes_withheld: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/ChargeComponentList'}
    pass


@attrs.define
class TaxWithheldComponentList:

    pass


@attrs.define
class TaxWithholdingEvent:

    base_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    tax_withholding_period: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/TaxWithholdingPeriod'}
    withheld_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Currency'}
    pass


@attrs.define
class TaxWithholdingEventList:

    pass


@attrs.define
class TaxWithholdingPeriod:

    end_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    start_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
    pass


@attrs.define
class TrialShipmentEvent:

    amazon_order_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    financial_event_group_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}
    sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'type': 'string'}

    fee_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/FeeComponentList'}
    posted_date: str
    # {'generator': <__mp_main__.Generator object at 0x0000020F15EEB310>, 'ref': '#/components/schemas/Date'}
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
