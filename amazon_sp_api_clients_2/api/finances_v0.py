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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    adjustment_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    adjustment_item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AdjustmentItemList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class AdjustmentEventList:

    pass


@attrs.define
class AdjustmentItem:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fn_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    product_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    quantity: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    per_unit_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    total_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class AdjustmentItemList:

    pass


@attrs.define
class AffordabilityExpenseEvent:

    amazon_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    base_expense: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_type_cgst: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_type_igst: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_type_sgst: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    total_expense: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    charge_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ChargeComponentList:

    pass


@attrs.define
class ChargeInstrument:

    description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tail: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ChargeInstrumentList:

    pass


@attrs.define
class CouponPaymentEvent:

    clip_or_redemption_count: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>, 'schema_format': 'int64'}
    coupon_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    payment_event_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_coupon_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    charge_component: dict[str, Any]
    # {'ref': '#/components/schemas/ChargeComponent', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fee_component: dict[str, Any]
    # {'ref': '#/components/schemas/FeeComponent', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    total_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class CouponPaymentEventList:

    pass


@attrs.define
class Currency:

    currency_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    currency_amount: Union[float, int]
    # {'ref': '#/components/schemas/BigDecimal', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class Date:

    pass


@attrs.define
class DebtRecoveryEvent:

    debt_recovery_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    charge_instrument_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeInstrumentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    debt_recovery_item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/DebtRecoveryItemList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    over_payment_credit: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    recovery_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class DebtRecoveryEventList:

    pass


@attrs.define
class DebtRecoveryItem:

    group_begin_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    group_end_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    original_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    recovery_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class DebtRecoveryItemList:

    pass


@attrs.define
class DirectPayment:

    direct_payment_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    direct_payment_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class DirectPaymentList:

    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FBALiquidationEvent:

    original_removal_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    liquidation_fee_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    liquidation_proceeds_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class FBALiquidationEventList:

    pass


@attrs.define
class FeeComponent:

    fee_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    fee_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class FeeComponentList:

    pass


@attrs.define
class FinancialEventGroup:

    account_tail: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    financial_event_group_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fund_transfer_status: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    processing_status: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    trace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    beginning_balance: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    converted_total: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    financial_event_group_end: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    financial_event_group_start: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fund_transfer_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    original_total: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class FinancialEventGroupList:

    pass


@attrs.define
class FinancialEvents:

    adjustment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AdjustmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    affordability_expense_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AffordabilityExpenseEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    affordability_expense_reversal_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AffordabilityExpenseEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    chargeback_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    coupon_payment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/CouponPaymentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    debt_recovery_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/DebtRecoveryEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fbaliquidation_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FBALiquidationEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    guarantee_claim_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    imaging_services_fee_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ImagingServicesFeeEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    loan_servicing_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/LoanServicingEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    network_commingling_transaction_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/NetworkComminglingTransactionEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pay_with_amazon_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/PayWithAmazonEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    product_ads_payment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ProductAdsPaymentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    refund_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    removal_shipment_adjustment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RemovalShipmentAdjustmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    removal_shipment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RemovalShipmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_transaction_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RentalTransactionEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    retrocharge_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RetrochargeEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    safetreimbursement_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SAFETReimbursementEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_deal_payment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SellerDealPaymentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_review_enrollment_payment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SellerReviewEnrollmentPaymentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    service_fee_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ServiceFeeEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    service_provider_credit_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SolutionProviderCreditEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipment_settle_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentSettleEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_withholding_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TaxWithholdingEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    trial_shipment_event_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TrialShipmentEventList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ImagingServicesFeeEvent:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    imaging_request_billing_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ImagingServicesFeeEventList:

    pass


@attrs.define
class ListFinancialEventGroupsPayload:

    next_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    financial_event_group_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FinancialEventGroupList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ListFinancialEventGroupsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ListFinancialEventGroupsPayload', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ListFinancialEventsPayload:

    next_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    financial_events: dict[str, Any]
    # {'ref': '#/components/schemas/FinancialEvents', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ListFinancialEventsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ListFinancialEventsPayload', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class LoanServicingEvent:

    source_business_event_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    loan_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class LoanServicingEventList:

    pass


@attrs.define
class NetworkComminglingTransactionEvent:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    net_co_transaction_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    swap_reason: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_exclusive_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class NetworkComminglingTransactionEventList:

    pass


@attrs.define
class PayWithAmazonEvent:

    amount_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    business_object_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fulfillment_channel: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    payment_amount_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    sales_channel: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    store_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    charge: dict[str, Any]
    # {'ref': '#/components/schemas/ChargeComponent', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class PayWithAmazonEventList:

    pass


@attrs.define
class ProductAdsPaymentEvent:

    invoice_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    base_value: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_value: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_value: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ProductAdsPaymentEventList:

    pass


@attrs.define
class Promotion:

    promotion_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    promotion_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    promotion_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class PromotionList:

    pass


@attrs.define
class RemovalShipmentAdjustmentEvent:

    adjustment_event_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    merchant_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    removal_shipment_item_adjustment_list: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/RemovalShipmentItemAdjustment'), 'type': 'array', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class RemovalShipmentAdjustmentEventList:

    pass


@attrs.define
class RemovalShipmentEvent:

    merchant_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    removal_shipment_item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RemovalShipmentItemList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class RemovalShipmentEventList:

    pass


@attrs.define
class RemovalShipmentItem:

    fulfillment_network_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    quantity: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>, 'schema_format': 'int32'}
    removal_shipment_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_collection_model: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    fee_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    revenue: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_withheld: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class RemovalShipmentItemAdjustment:

    adjusted_quantity: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>, 'schema_format': 'int32'}
    fulfillment_network_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    removal_shipment_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_collection_model: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    revenue_adjustment: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_amount_adjustment: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_withheld_adjustment: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class RemovalShipmentItemList:

    pass


@attrs.define
class RentalTransactionEvent:

    amazon_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    extension_length: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>, 'schema_format': 'int32'}
    marketplace_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_event_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_charge_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_initial_value: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_reimbursement: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    rental_tax_withheld_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TaxWithheldComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class RentalTransactionEventList:

    pass


@attrs.define
class RetrochargeEvent:

    amazon_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    marketplace_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    retrocharge_event_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    base_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    retrocharge_tax_withheld_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TaxWithheldComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipping_tax: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class RetrochargeEventList:

    pass


@attrs.define
class SAFETReimbursementEvent:

    reason_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    safetclaim_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    reimbursed_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    safetreimbursement_item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/SAFETReimbursementItemList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class SAFETReimbursementEventList:

    pass


@attrs.define
class SAFETReimbursementItem:

    product_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    quantity: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    item_charge_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class SAFETReimbursementItemList:

    pass


@attrs.define
class SellerDealPaymentEvent:

    deal_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    deal_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    event_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fee_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    fee_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    total_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class SellerDealPaymentEventList:

    pass


@attrs.define
class SellerReviewEnrollmentPaymentEvent:

    enrollment_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    parent_asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    charge_component: dict[str, Any]
    # {'ref': '#/components/schemas/ChargeComponent', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fee_component: dict[str, Any]
    # {'ref': '#/components/schemas/FeeComponent', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    total_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class SellerReviewEnrollmentPaymentEventList:

    pass


@attrs.define
class ServiceFeeEvent:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    amazon_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fee_description: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fee_reason: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    fn_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ServiceFeeEventList:

    pass


@attrs.define
class ShipmentEvent:

    amazon_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    marketplace_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    direct_payment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/DirectPaymentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_charge_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_charge_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_fee_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipment_fee_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipment_fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipment_item_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentItemList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    shipment_item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentItemList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class ShipmentEventList:

    pass


@attrs.define
class ShipmentItem:

    order_adjustment_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    order_item_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    quantity_shipped: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>, 'schema_format': 'int32'}
    seller_sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    cost_of_points_granted: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    cost_of_points_returned: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    item_charge_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    item_charge_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    item_fee_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    item_fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    item_tax_withheld_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TaxWithheldComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    promotion_adjustment_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/PromotionList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    promotion_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/PromotionList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
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
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    marketplace_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    provider_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    provider_store_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    provider_transaction_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    seller_store_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    transaction_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    transaction_creation_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class SolutionProviderCreditEventList:

    pass


@attrs.define
class TaxWithheldComponent:

    tax_collection_model: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    taxes_withheld: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ChargeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class TaxWithheldComponentList:

    pass


@attrs.define
class TaxWithholdingEvent:

    base_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    tax_withholding_period: dict[str, Any]
    # {'ref': '#/components/schemas/TaxWithholdingPeriod', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    withheld_amount: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class TaxWithholdingEventList:

    pass


@attrs.define
class TaxWithholdingPeriod:

    end_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    start_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    pass


@attrs.define
class TrialShipmentEvent:

    amazon_order_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    financial_event_group_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    sku: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}

    fee_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/FeeComponentList', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
    posted_date: str
    # {'ref': '#/components/schemas/Date', 'generator': <__mp_main__.Generator object at 0x0000020CF228B310>}
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
