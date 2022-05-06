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

    adjustment_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of adjustment.
        Possible values:
        * FBAInventoryReimbursement - An FBA inventory reimbursement to a seller's account. This occurs if a seller's inventory is damaged.
        * ReserveEvent - A reserve event that is generated at the time of a settlement period closing. This occurs when some money from a seller's account is held back.
        * PostageBilling - The amount paid by a seller for shipping labels.
        * PostageRefund - The reimbursement of shipping labels purchased for orders that were canceled or refunded.
        * LostOrDamagedReimbursement - An Amazon Easy Ship reimbursement to a seller's account for a package that we lost or damaged.
        * CanceledButPickedUpReimbursement - An Amazon Easy Ship reimbursement to a seller's account. This occurs when a package is picked up and the order is subsequently canceled. This value is used only in the India marketplace.
        * ReimbursementClawback - An Amazon Easy Ship reimbursement clawback from a seller's account. This occurs when a prior reimbursement is reversed. This value is used only in the India marketplace.
        * SellerRewards - An award credited to a seller's account for their participation in an offer in the Seller Rewards program. Applies only to the India marketplace.
    """

    adjustment_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    adjustment_item_list: "AdjustmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AdjustmentEventList:

    pass


@attrs.define
class AdjustmentItem:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    fn_sku: str = attrs.field(
        kw_only=True,
    )
    """
    A unique identifier assigned to products stored in and fulfilled from a fulfillment center.
    """

    product_description: str = attrs.field(
        kw_only=True,
    )
    """
    A short description of the item.
    """

    quantity: str = attrs.field(
        kw_only=True,
    )
    """
    Represents the number of units in the seller's inventory when the AdustmentType is FBAInventoryReimbursement.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """

    per_unit_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AdjustmentItemList:

    pass


@attrs.define
class AffordabilityExpenseEvent:

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined identifier for an order.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    An encrypted, Amazon-defined marketplace identifier.
    """

    transaction_type: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates the type of transaction.
        Possible values:
        * Charge - For an affordability promotion expense.
        * Refund - For an affordability promotion expense reversal.
    """

    base_expense: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_type_cgst: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_type_igst: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_type_sgst: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_expense: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AffordabilityExpenseEventList:

    pass


@attrs.define
class BigDecimal:

    pass


@attrs.define
class ChargeComponent:

    charge_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of charge.
    """

    charge_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ChargeComponentList:

    pass


@attrs.define
class ChargeInstrument:

    description: str = attrs.field(
        kw_only=True,
    )
    """
    A short description of the charge instrument.
    """

    tail: str = attrs.field(
        kw_only=True,
    )
    """
    The account tail (trailing digits) of the charge instrument.
    """

    amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ChargeInstrumentList:

    pass


@attrs.define
class CouponPaymentEvent:

    clip_or_redemption_count: int = attrs.field(
        kw_only=True,
    )
    """
    The number of coupon clips or redemptions.

    Extra fields:
    {'schema_format': 'int64'}
    """

    coupon_id: str = attrs.field(
        kw_only=True,
    )
    """
    A coupon identifier.
    """

    payment_event_id: str = attrs.field(
        kw_only=True,
    )
    """
    A payment event identifier.
    """

    seller_coupon_description: str = attrs.field(
        kw_only=True,
    )
    """
    The description provided by the seller when they created the coupon.
    """

    charge_component: "ChargeComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fee_component: "FeeComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CouponPaymentEventList:

    pass


@attrs.define
class Currency:

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    The three-digit currency code in ISO 4217 format.
    """

    currency_amount: "BigDecimal" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Date:

    pass


@attrs.define
class DebtRecoveryEvent:

    debt_recovery_type: str = attrs.field(
        kw_only=True,
    )
    """
    The debt recovery type.
        Possible values:
        * DebtPayment
        * DebtPaymentFailure
        *DebtAdjustment
    """

    charge_instrument_list: "ChargeInstrumentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    debt_recovery_item_list: "DebtRecoveryItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    over_payment_credit: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    recovery_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class DebtRecoveryEventList:

    pass


@attrs.define
class DebtRecoveryItem:

    group_begin_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    group_end_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    original_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    recovery_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class DebtRecoveryItemList:

    pass


@attrs.define
class DirectPayment:

    direct_payment_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of payment.
        Possible values:
        * StoredValueCardRevenue - The amount that is deducted from the seller's account because the seller received money through a stored value card.
        * StoredValueCardRefund - The amount that Amazon returns to the seller if the order that is bought using a stored value card is refunded.
        * PrivateLabelCreditCardRevenue - The amount that is deducted from the seller's account because the seller received money through a private label credit card offered by Amazon.
        * PrivateLabelCreditCardRefund - The amount that Amazon returns to the seller if the order that is bought using a private label credit card offered by Amazon is refunded.
        * CollectOnDeliveryRevenue - The COD amount that the seller collected directly from the buyer.
        * CollectOnDeliveryRefund - The amount that Amazon refunds to the buyer if an order paid for by COD is refunded.
    """

    direct_payment_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class DirectPaymentList:

    pass


@attrs.define
class Error:

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition in a human-readable form.
    """

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FBALiquidationEvent:

    original_removal_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the original removal order.
    """

    liquidation_fee_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    liquidation_proceeds_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FBALiquidationEventList:

    pass


@attrs.define
class FeeComponent:

    fee_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of fee. For more information about Selling on Amazon fees, see [Selling on Amazon Fee Schedule](https://sellercentral.amazon.com/gp/help/200336920) on Seller Central. For more information about Fulfillment by Amazon fees, see [FBA features, services and fees](https://sellercentral.amazon.com/gp/help/201074400) on Seller Central.
    """

    fee_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FeeComponentList:

    pass


@attrs.define
class FinancialEventGroup:

    account_tail: str = attrs.field(
        kw_only=True,
    )
    """
    The account tail of the payment instrument.
    """

    financial_event_group_id: str = attrs.field(
        kw_only=True,
    )
    """
    A unique identifier for the financial event group.
    """

    fund_transfer_status: str = attrs.field(
        kw_only=True,
    )
    """
    The status of the fund transfer.
    """

    processing_status: str = attrs.field(
        kw_only=True,
    )
    """
    The processing status of the financial event group indicates whether the balance of the financial event group is settled.
        Possible values:
        * Open
        * Closed
    """

    trace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The trace identifier used by sellers to look up transactions externally.
    """

    beginning_balance: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    converted_total: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    financial_event_group_end: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    financial_event_group_start: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fund_transfer_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    original_total: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FinancialEventGroupList:

    pass


@attrs.define
class FinancialEvents:

    adjustment_event_list: "AdjustmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    affordability_expense_event_list: "AffordabilityExpenseEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    affordability_expense_reversal_event_list: "AffordabilityExpenseEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    chargeback_event_list: "ShipmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    coupon_payment_event_list: "CouponPaymentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    debt_recovery_event_list: "DebtRecoveryEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fbaliquidation_event_list: "FBALiquidationEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    guarantee_claim_event_list: "ShipmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    imaging_services_fee_event_list: "ImagingServicesFeeEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    loan_servicing_event_list: "LoanServicingEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    network_commingling_transaction_event_list: "NetworkComminglingTransactionEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pay_with_amazon_event_list: "PayWithAmazonEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    product_ads_payment_event_list: "ProductAdsPaymentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    refund_event_list: "ShipmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    removal_shipment_adjustment_event_list: "RemovalShipmentAdjustmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    removal_shipment_event_list: "RemovalShipmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rental_transaction_event_list: "RentalTransactionEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    retrocharge_event_list: "RetrochargeEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    safetreimbursement_event_list: "SAFETReimbursementEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_deal_payment_event_list: "SellerDealPaymentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_review_enrollment_payment_event_list: "SellerReviewEnrollmentPaymentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_fee_event_list: "ServiceFeeEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_provider_credit_event_list: "SolutionProviderCreditEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_event_list: "ShipmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_settle_event_list: "ShipmentSettleEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_withholding_event_list: "TaxWithholdingEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    trial_shipment_event_list: "TrialShipmentEventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ImagingServicesFeeEvent:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item for which the imaging service was requested.
    """

    imaging_request_billing_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the imaging services request.
    """

    fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ImagingServicesFeeEventList:

    pass


@attrs.define
class ListFinancialEventGroupsPayload:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    financial_event_group_list: "FinancialEventGroupList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ListFinancialEventGroupsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ListFinancialEventGroupsPayload" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ListFinancialEventsPayload:

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    financial_events: "FinancialEvents" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ListFinancialEventsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ListFinancialEventsPayload" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LoanServicingEvent:

    source_business_event_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of event.
        Possible values:
        * LoanAdvance
        * LoanPayment
        * LoanRefund
    """

    loan_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LoanServicingEventList:

    pass


@attrs.define
class NetworkComminglingTransactionEvent:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the swapped item.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The marketplace in which the event took place.
    """

    net_co_transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the network item swap.
    """

    swap_reason: str = attrs.field(
        kw_only=True,
    )
    """
    The reason for the network item swap.
    """

    transaction_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of network item swap.
        Possible values:
        * NetCo - A Fulfillment by Amazon inventory pooling transaction. Available only in the India marketplace.
        * ComminglingVAT - A commingling VAT transaction. Available only in the UK, Spain, France, Germany, and Italy marketplaces.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_exclusive_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class NetworkComminglingTransactionEventList:

    pass


@attrs.define
class PayWithAmazonEvent:

    amount_description: str = attrs.field(
        kw_only=True,
    )
    """
    A short description of this payment event.
    """

    business_object_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of business object.
    """

    fulfillment_channel: str = attrs.field(
        kw_only=True,
    )
    """
    The fulfillment channel.
        Possible values:
        * AFN - Amazon Fulfillment Network (Fulfillment by Amazon)
        * MFN - Merchant Fulfillment Network (self-fulfilled)
    """

    payment_amount_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of payment.
        Possible values:
        * Sales
    """

    sales_channel: str = attrs.field(
        kw_only=True,
    )
    """
    The sales channel for the transaction.
    """

    seller_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An order identifier that is specified by the seller.
    """

    store_name: str = attrs.field(
        kw_only=True,
    )
    """
    The store name where the event occurred.
    """

    charge: "ChargeComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transaction_posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PayWithAmazonEventList:

    pass


@attrs.define
class ProductAdsPaymentEvent:

    invoice_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifier for the invoice that the transaction appears in.
    """

    transaction_type: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates if the transaction is for a charge or a refund.
        Possible values:
        * charge - Charge
        * refund - Refund
    """

    base_value: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_value: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transaction_value: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ProductAdsPaymentEventList:

    pass


@attrs.define
class Promotion:

    promotion_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller-specified identifier for the promotion.
    """

    promotion_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of promotion.
    """

    promotion_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PromotionList:

    pass


@attrs.define
class RemovalShipmentAdjustmentEvent:

    adjustment_event_id: str = attrs.field(
        kw_only=True,
    )
    """
    The unique identifier for the adjustment event.
    """

    merchant_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The merchant removal orderId.
    """

    order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The orderId for shipping inventory.
    """

    removal_shipment_item_adjustment_list: list["RemovalShipmentItemAdjustment"] = attrs.field(
        kw_only=True,
    )
    """
    A comma-delimited list of Removal shipmentItemAdjustment details for FBA inventory.
    """

    transaction_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of removal order.
        Possible values:
        * WHOLESALE_LIQUIDATION.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RemovalShipmentAdjustmentEventList:

    pass


@attrs.define
class RemovalShipmentEvent:

    merchant_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The merchant removal orderId.
    """

    order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the removal shipment order.
    """

    transaction_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of removal order.
        Possible values:
        * WHOLESALE_LIQUIDATION
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    removal_shipment_item_list: "RemovalShipmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RemovalShipmentEventList:

    pass


@attrs.define
class RemovalShipmentItem:

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon fulfillment network SKU for the item.
    """

    quantity: int = attrs.field(
        kw_only=True,
    )
    """
    The quantity of the item.

    Extra fields:
    {'schema_format': 'int32'}
    """

    removal_shipment_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for an item in a removal shipment.
    """

    tax_collection_model: str = attrs.field(
        kw_only=True,
    )
    """
    The tax collection model applied to the item.
        Possible values:
        * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.
        * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
    """

    fee_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    revenue: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_withheld: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RemovalShipmentItemAdjustment:

    adjusted_quantity: int = attrs.field(
        kw_only=True,
    )
    """
    Adjusted quantity of removal shipmentItemAdjustment items.

    Extra fields:
    {'schema_format': 'int32'}
    """

    fulfillment_network_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon fulfillment network SKU for the item.
    """

    removal_shipment_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for an item in a removal shipment.
    """

    tax_collection_model: str = attrs.field(
        kw_only=True,
    )
    """
    The tax collection model applied to the item.
        Possible values:
        * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.
        * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
    """

    revenue_adjustment: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_amount_adjustment: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_withheld_adjustment: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RemovalShipmentItemList:

    pass


@attrs.define
class RentalTransactionEvent:

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined identifier for an order.
    """

    extension_length: int = attrs.field(
        kw_only=True,
    )
    """
    The number of days that the buyer extended an already rented item. This value is only returned for RentalCustomerPayment-Extension and RentalCustomerRefund-Extension events.

    Extra fields:
    {'schema_format': 'int32'}
    """

    marketplace_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the marketplace.
    """

    rental_event_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of rental event.
        Possible values:
        * RentalCustomerPayment-Buyout - Transaction type that represents when the customer wants to buy out a rented item.
        * RentalCustomerPayment-Extension - Transaction type that represents when the customer wants to extend the rental period.
        * RentalCustomerRefund-Buyout - Transaction type that represents when the customer requests a refund for the buyout of the rented item.
        * RentalCustomerRefund-Extension - Transaction type that represents when the customer requests a refund over the extension on the rented item.
        * RentalHandlingFee - Transaction type that represents the fee that Amazon charges sellers who rent through Amazon.
        * RentalChargeFailureReimbursement - Transaction type that represents when Amazon sends money to the seller to compensate for a failed charge.
        * RentalLostItemReimbursement - Transaction type that represents when Amazon sends money to the seller to compensate for a lost item.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rental_charge_list: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rental_fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rental_initial_value: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rental_reimbursement: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rental_tax_withheld_list: "TaxWithheldComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RentalTransactionEventList:

    pass


@attrs.define
class RetrochargeEvent:

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined identifier for an order.
    """

    marketplace_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the marketplace where the retrocharge event occurred.
    """

    retrocharge_event_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of event.
        Possible values:
        * Retrocharge
        * RetrochargeReversal
    """

    base_tax: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    retrocharge_tax_withheld_list: "TaxWithheldComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_tax: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RetrochargeEventList:

    pass


@attrs.define
class SAFETReimbursementEvent:

    reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    Indicates why the seller was reimbursed.
    """

    safetclaim_id: str = attrs.field(
        kw_only=True,
    )
    """
    A SAFE-T claim identifier.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    reimbursed_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    safetreimbursement_item_list: "SAFETReimbursementItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SAFETReimbursementEventList:

    pass


@attrs.define
class SAFETReimbursementItem:

    product_description: str = attrs.field(
        kw_only=True,
    )
    """
    The description of the item as shown on the product detail page on the retail website.
    """

    quantity: str = attrs.field(
        kw_only=True,
    )
    """
    The number of units of the item being reimbursed.
    """

    item_charge_list: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SAFETReimbursementItemList:

    pass


@attrs.define
class SellerDealPaymentEvent:

    deal_description: str = attrs.field(
        kw_only=True,
    )
    """
    The internal description of the deal.
    """

    deal_id: str = attrs.field(
        kw_only=True,
    )
    """
    The unique identifier of the deal.
    """

    event_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of event: SellerDealComplete.
    """

    fee_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of fee: RunLightningDealFee.
    """

    fee_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SellerDealPaymentEventList:

    pass


@attrs.define
class SellerReviewEnrollmentPaymentEvent:

    enrollment_id: str = attrs.field(
        kw_only=True,
    )
    """
    An enrollment identifier.
    """

    parent_asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item that was enrolled in the Early Reviewer Program.
    """

    charge_component: "ChargeComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    fee_component: "FeeComponent" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SellerReviewEnrollmentPaymentEventList:

    pass


@attrs.define
class ServiceFeeEvent:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined identifier for an order.
    """

    fee_description: str = attrs.field(
        kw_only=True,
    )
    """
    A short description of the service fee event.
    """

    fee_reason: str = attrs.field(
        kw_only=True,
    )
    """
    A short description of the service fee reason.
    """

    fn_sku: str = attrs.field(
        kw_only=True,
    )
    """
    A unique identifier assigned by Amazon to products stored in and fulfilled from an Amazon fulfillment center.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """

    fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ServiceFeeEventList:

    pass


@attrs.define
class ShipmentEvent:

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined identifier for an order.
    """

    marketplace_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the marketplace where the event occurred.
    """

    seller_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    A seller-defined identifier for an order.
    """

    direct_payment_list: "DirectPaymentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    order_charge_adjustment_list: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    order_charge_list: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    order_fee_adjustment_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    order_fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_fee_adjustment_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_item_adjustment_list: "ShipmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_item_list: "ShipmentItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentEventList:

    pass


@attrs.define
class ShipmentItem:

    order_adjustment_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined order adjustment identifier defined for refunds, guarantee claims, and chargeback events.
    """

    order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined order item identifier.
    """

    quantity_shipped: int = attrs.field(
        kw_only=True,
    )
    """
    The number of items shipped.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """

    cost_of_points_granted: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    cost_of_points_returned: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_charge_adjustment_list: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_charge_list: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_fee_adjustment_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_tax_withheld_list: "TaxWithheldComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promotion_adjustment_list: "PromotionList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promotion_list: "PromotionList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentItemList:

    pass


@attrs.define
class ShipmentSettleEventList:

    pass


@attrs.define
class SolutionProviderCreditEvent:

    marketplace_country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The two-letter country code of the country associated with the marketplace where the order was placed.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier of the marketplace where the order was placed.
    """

    provider_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier of the solution provider.
    """

    provider_store_name: str = attrs.field(
        kw_only=True,
    )
    """
    The store name where the payment event occurred.
    """

    provider_transaction_type: str = attrs.field(
        kw_only=True,
    )
    """
    The transaction type.
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier of the seller.
    """

    seller_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    A seller-defined identifier for an order.
    """

    seller_store_name: str = attrs.field(
        kw_only=True,
    )
    """
    The store name where the payment event occurred.
    """

    transaction_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transaction_creation_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SolutionProviderCreditEventList:

    pass


@attrs.define
class TaxWithheldComponent:

    tax_collection_model: str = attrs.field(
        kw_only=True,
    )
    """
    The tax collection model applied to the item.
        Possible values:
        * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.
        * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
    """

    taxes_withheld: "ChargeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TaxWithheldComponentList:

    pass


@attrs.define
class TaxWithholdingEvent:

    base_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tax_withholding_period: "TaxWithholdingPeriod" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    withheld_amount: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TaxWithholdingEventList:

    pass


@attrs.define
class TaxWithholdingPeriod:

    end_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    start_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TrialShipmentEvent:

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined identifier for an order.
    """

    financial_event_group_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier of the financial event group.
    """

    sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """

    fee_list: "FeeComponentList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    posted_date: "Date" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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
