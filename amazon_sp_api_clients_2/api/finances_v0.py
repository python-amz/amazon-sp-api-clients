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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdjustmentEvent:
    """
    An adjustment to the seller's account.
    """

    adjustment_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    adjustment_item_list: Optional[List["AdjustmentItem"]] = attrs.field()
    """
    A list of information about items in an adjustment to the seller's account.
    """

    adjustment_type: Optional[str] = attrs.field()
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

    posted_date: Optional["Date"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdjustmentItem:
    """
    An item in an adjustment to the seller's account.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    fn_sku: Optional[str] = attrs.field()
    """
    A unique identifier assigned to products stored in and fulfilled from a fulfillment center.
    """

    per_unit_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    product_description: Optional[str] = attrs.field()
    """
    A short description of the item.
    """

    quantity: Optional[str] = attrs.field()
    """
    Represents the number of units in the seller's inventory when the AdustmentType is FBAInventoryReimbursement.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """

    total_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AffordabilityExpenseEvent:
    """
    An expense related to an affordability promotion.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    An Amazon-defined identifier for an order.
    """

    base_expense: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    An encrypted, Amazon-defined marketplace identifier.
    """

    posted_date: Optional["Date"] = attrs.field()

    tax_type_cgst: "Currency" = attrs.field()
    """
    A currency type and amount.
    """

    tax_type_igst: "Currency" = attrs.field()
    """
    A currency type and amount.
    """

    tax_type_sgst: "Currency" = attrs.field()
    """
    A currency type and amount.
    """

    total_expense: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    transaction_type: Optional[str] = attrs.field()
    """
    Indicates the type of transaction.
        Possible values:
        * Charge - For an affordability promotion expense.
        * Refund - For an affordability promotion expense reversal.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class BigDecimal:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ChargeComponent:
    """
    A charge on the seller's account.
        Possible values:
        * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered.
        * Tax - The tax collected by the seller on the Principal.
        * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal.
        * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge.
        * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge.
        * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges.
        * Discount - The promotional discount for an order item.
        * TaxDiscount - The tax amount deducted for promotional rebates.
        * CODItemCharge - The COD charge for an order item.
        * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge.
        * CODOrderCharge - The COD charge for an order.
        * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge.
        * CODShippingCharge - Shipping charges for a COD order.
        * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge.
        * ShippingCharge - The shipping charge.
        * ShippingTax - The tax collected by the seller on a ShippingCharge.
        * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience.
        * Giftwrap - The gift wrap charge.
        * GiftwrapTax - The tax collected by the seller on a Giftwrap charge.
        * RestockingFee - The charge applied to the buyer when returning a product in certain categories.
        * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault.
        * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction.
        * GenericDeduction - A generic bad debt deduction.
        * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item.
        * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.
        * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program.
        * SAFE-TReimbursement - The SAFE-T claim amount for the item.
        * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).
        * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).
        * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).
        * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
    """

    charge_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    charge_type: Optional[str] = attrs.field()
    """
    The type of charge.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ChargeInstrument:
    """
    A payment instrument.
    """

    amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    description: Optional[str] = attrs.field()
    """
    A short description of the charge instrument.
    """

    tail: Optional[str] = attrs.field()
    """
    The account tail (trailing digits) of the charge instrument.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CouponPaymentEvent:
    """
    An event related to coupon payments.
    """

    charge_component: Optional["ChargeComponent"] = attrs.field()
    """
    A charge on the seller's account.
        Possible values:
        * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered.
        * Tax - The tax collected by the seller on the Principal.
        * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal.
        * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge.
        * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge.
        * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges.
        * Discount - The promotional discount for an order item.
        * TaxDiscount - The tax amount deducted for promotional rebates.
        * CODItemCharge - The COD charge for an order item.
        * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge.
        * CODOrderCharge - The COD charge for an order.
        * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge.
        * CODShippingCharge - Shipping charges for a COD order.
        * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge.
        * ShippingCharge - The shipping charge.
        * ShippingTax - The tax collected by the seller on a ShippingCharge.
        * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience.
        * Giftwrap - The gift wrap charge.
        * GiftwrapTax - The tax collected by the seller on a Giftwrap charge.
        * RestockingFee - The charge applied to the buyer when returning a product in certain categories.
        * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault.
        * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction.
        * GenericDeduction - A generic bad debt deduction.
        * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item.
        * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.
        * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program.
        * SAFE-TReimbursement - The SAFE-T claim amount for the item.
        * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).
        * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).
        * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).
        * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
    """

    clip_or_redemption_count: Optional[int] = attrs.field()
    """
    The number of coupon clips or redemptions.

    Extra fields:
    {'schema_format': 'int64'}
    """

    coupon_id: Optional[str] = attrs.field()
    """
    A coupon identifier.
    """

    fee_component: Optional["FeeComponent"] = attrs.field()
    """
    A fee associated with the event.
    """

    payment_event_id: Optional[str] = attrs.field()
    """
    A payment event identifier.
    """

    posted_date: Optional["Date"] = attrs.field()

    seller_coupon_description: Optional[str] = attrs.field()
    """
    The description provided by the seller when they created the coupon.
    """

    total_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Currency:
    """
    A currency type and amount.
    """

    currency_amount: Optional["BigDecimal"] = attrs.field()

    currency_code: Optional[str] = attrs.field()
    """
    The three-digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Date:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DebtRecoveryEvent:
    """
    A debt payment or debt adjustment.
    """

    charge_instrument_list: Optional[List["ChargeInstrument"]] = attrs.field()
    """
    A list of payment instruments.
    """

    debt_recovery_item_list: Optional[List["DebtRecoveryItem"]] = attrs.field()
    """
    A list of debt recovery item information.
    """

    debt_recovery_type: Optional[str] = attrs.field()
    """
    The debt recovery type.
        Possible values:
        * DebtPayment
        * DebtPaymentFailure
        *DebtAdjustment
    """

    over_payment_credit: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    recovery_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DebtRecoveryItem:
    """
    An item of a debt payment or debt adjustment.
    """

    group_begin_date: Optional["Date"] = attrs.field()

    group_end_date: Optional["Date"] = attrs.field()

    original_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    recovery_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class DirectPayment:
    """
    A payment made directly to a seller.
    """

    direct_payment_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    direct_payment_type: Optional[str] = attrs.field()
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


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FBALiquidationEvent:
    """
    A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US marketplace.
    """

    liquidation_fee_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    liquidation_proceeds_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    original_removal_order_id: Optional[str] = attrs.field()
    """
    The identifier for the original removal order.
    """

    posted_date: Optional["Date"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeeComponent:
    """
    A fee associated with the event.
    """

    fee_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    fee_type: Optional[str] = attrs.field()
    """
    The type of fee. For more information about Selling on Amazon fees, see [Selling on Amazon Fee Schedule](https://sellercentral.amazon.com/gp/help/200336920) on Seller Central. For more information about Fulfillment by Amazon fees, see [FBA features, services and fees](https://sellercentral.amazon.com/gp/help/201074400) on Seller Central.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FinancialEventGroup:
    """
    Information related to a financial event group.
    """

    account_tail: Optional[str] = attrs.field()
    """
    The account tail of the payment instrument.
    """

    beginning_balance: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    converted_total: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    financial_event_group_end: Optional["Date"] = attrs.field()

    financial_event_group_id: Optional[str] = attrs.field()
    """
    A unique identifier for the financial event group.
    """

    financial_event_group_start: Optional["Date"] = attrs.field()

    fund_transfer_date: Optional["Date"] = attrs.field()

    fund_transfer_status: Optional[str] = attrs.field()
    """
    The status of the fund transfer.
    """

    original_total: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    processing_status: Optional[str] = attrs.field()
    """
    The processing status of the financial event group indicates whether the balance of the financial event group is settled.
        Possible values:
        * Open
        * Closed
    """

    trace_id: Optional[str] = attrs.field()
    """
    The trace identifier used by sellers to look up transactions externally.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FinancialEvents:
    """
    Contains all information related to a financial event.
    """

    adjustment_event_list: Optional[List["AdjustmentEvent"]] = attrs.field()
    """
    A list of adjustment event information for the seller's account.
    """

    affordability_expense_event_list: Optional[List["AffordabilityExpenseEvent"]] = attrs.field()
    """
    A list of expense information related to an affordability promotion.
    """

    affordability_expense_reversal_event_list: Optional[List["AffordabilityExpenseEvent"]] = attrs.field()
    """
    A list of expense information related to an affordability promotion.
    """

    chargeback_event_list: Optional[List["ShipmentEvent"]] = attrs.field()
    """
    A list of shipment event information.
    """

    coupon_payment_event_list: Optional[List["CouponPaymentEvent"]] = attrs.field()
    """
    A list of coupon payment event information.
    """

    debt_recovery_event_list: Optional[List["DebtRecoveryEvent"]] = attrs.field()
    """
    A list of debt recovery event information.
    """

    fbaliquidation_event_list: Optional[List["FBALiquidationEvent"]] = attrs.field()
    """
    A list of FBA inventory liquidation payment events.
    """

    guarantee_claim_event_list: Optional[List["ShipmentEvent"]] = attrs.field()
    """
    A list of shipment event information.
    """

    imaging_services_fee_event_list: Optional[List["ImagingServicesFeeEvent"]] = attrs.field()
    """
    A list of fee events related to Amazon Imaging services.
    """

    loan_servicing_event_list: Optional[List["LoanServicingEvent"]] = attrs.field()
    """
    A list of loan servicing events.
    """

    network_commingling_transaction_event_list: Optional[List["NetworkComminglingTransactionEvent"]] = attrs.field()
    """
    A list of network commingling transaction events.
    """

    pay_with_amazon_event_list: Optional[List["PayWithAmazonEvent"]] = attrs.field()
    """
    A list of events related to the seller's Pay with Amazon account.
    """

    product_ads_payment_event_list: Optional[List["ProductAdsPaymentEvent"]] = attrs.field()
    """
    A list of sponsored products payment events.
    """

    refund_event_list: Optional[List["ShipmentEvent"]] = attrs.field()
    """
    A list of shipment event information.
    """

    removal_shipment_adjustment_event_list: Optional[List["RemovalShipmentAdjustmentEvent"]] = attrs.field()
    """
    A comma-delimited list of Removal shipmentAdjustment details for FBA inventory.
    """

    removal_shipment_event_list: Optional[List["RemovalShipmentEvent"]] = attrs.field()
    """
    A list of removal shipment event information.
    """

    rental_transaction_event_list: Optional[List["RentalTransactionEvent"]] = attrs.field()
    """
    A list of rental transaction event information.
    """

    retrocharge_event_list: Optional[List["RetrochargeEvent"]] = attrs.field()
    """
    A list of information about Retrocharge or RetrochargeReversal events.
    """

    safetreimbursement_event_list: Optional[List["SAFETReimbursementEvent"]] = attrs.field()
    """
    A list of SAFETReimbursementEvents.
    """

    seller_deal_payment_event_list: Optional[List["SellerDealPaymentEvent"]] = attrs.field()
    """
    A list of payment events for deal-related fees.
    """

    seller_review_enrollment_payment_event_list: Optional[List["SellerReviewEnrollmentPaymentEvent"]] = attrs.field()
    """
    A list of information about fee events for the Early Reviewer Program.
    """

    service_fee_event_list: Optional[List["ServiceFeeEvent"]] = attrs.field()
    """
    A list of information about service fee events.
    """

    service_provider_credit_event_list: Optional[List["SolutionProviderCreditEvent"]] = attrs.field()
    """
    A list of information about solution provider credits.
    """

    shipment_event_list: Optional[List["ShipmentEvent"]] = attrs.field()
    """
    A list of shipment event information.
    """

    shipment_settle_event_list: Optional[List["ShipmentEvent"]] = attrs.field()
    """
    A list of information about shipment settle financial events.
    """

    tax_withholding_event_list: Optional[List["TaxWithholdingEvent"]] = attrs.field()
    """
    List of TaxWithholding events.
    """

    trial_shipment_event_list: Optional[List["TrialShipmentEvent"]] = attrs.field()
    """
    A list of information about trial shipment financial events.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ImagingServicesFeeEvent:
    """
    A fee event related to Amazon Imaging services.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item for which the imaging service was requested.
    """

    fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    imaging_request_billing_item_id: Optional[str] = attrs.field()
    """
    The identifier for the imaging services request.
    """

    posted_date: Optional["Date"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListFinancialEventGroupsPayload:
    """
    The payload for the listFinancialEventGroups operation.
    """

    financial_event_group_list: Optional[List["FinancialEventGroup"]] = attrs.field()
    """
    A list of financial event group information.
    """

    next_token: Optional[str] = attrs.field()
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListFinancialEventGroupsResponse:
    """
    The response schema for the listFinancialEventGroups operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ListFinancialEventGroupsPayload"] = attrs.field()
    """
    The payload for the listFinancialEventGroups operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListFinancialEventsPayload:
    """
    The payload for the listFinancialEvents operation.
    """

    financial_events: Optional["FinancialEvents"] = attrs.field()
    """
    Contains all information related to a financial event.
    """

    next_token: Optional[str] = attrs.field()
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ListFinancialEventsResponse:
    """
    The response schema for the listFinancialEvents operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ListFinancialEventsPayload"] = attrs.field()
    """
    The payload for the listFinancialEvents operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LoanServicingEvent:
    """
    A loan advance, loan payment, or loan refund.
    """

    loan_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    source_business_event_type: Optional[str] = attrs.field()
    """
    The type of event.
        Possible values:
        * LoanAdvance
        * LoanPayment
        * LoanRefund
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NetworkComminglingTransactionEvent:
    """
    A network commingling transaction event.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the swapped item.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    The marketplace in which the event took place.
    """

    net_co_transaction_id: Optional[str] = attrs.field()
    """
    The identifier for the network item swap.
    """

    posted_date: Optional["Date"] = attrs.field()

    swap_reason: Optional[str] = attrs.field()
    """
    The reason for the network item swap.
    """

    tax_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    tax_exclusive_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    transaction_type: Optional[str] = attrs.field()
    """
    The type of network item swap.
        Possible values:
        * NetCo - A Fulfillment by Amazon inventory pooling transaction. Available only in the India marketplace.
        * ComminglingVAT - A commingling VAT transaction. Available only in the UK, Spain, France, Germany, and Italy marketplaces.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PayWithAmazonEvent:
    """
    An event related to the seller's Pay with Amazon account.
    """

    amount_description: Optional[str] = attrs.field()
    """
    A short description of this payment event.
    """

    business_object_type: Optional[str] = attrs.field()
    """
    The type of business object.
    """

    charge: Optional["ChargeComponent"] = attrs.field()
    """
    A charge on the seller's account.
        Possible values:
        * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered.
        * Tax - The tax collected by the seller on the Principal.
        * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal.
        * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge.
        * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge.
        * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges.
        * Discount - The promotional discount for an order item.
        * TaxDiscount - The tax amount deducted for promotional rebates.
        * CODItemCharge - The COD charge for an order item.
        * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge.
        * CODOrderCharge - The COD charge for an order.
        * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge.
        * CODShippingCharge - Shipping charges for a COD order.
        * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge.
        * ShippingCharge - The shipping charge.
        * ShippingTax - The tax collected by the seller on a ShippingCharge.
        * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience.
        * Giftwrap - The gift wrap charge.
        * GiftwrapTax - The tax collected by the seller on a Giftwrap charge.
        * RestockingFee - The charge applied to the buyer when returning a product in certain categories.
        * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault.
        * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction.
        * GenericDeduction - A generic bad debt deduction.
        * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item.
        * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.
        * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program.
        * SAFE-TReimbursement - The SAFE-T claim amount for the item.
        * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).
        * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).
        * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).
        * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
    """

    fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    fulfillment_channel: Optional[str] = attrs.field()
    """
    The fulfillment channel.
        Possible values:
        * AFN - Amazon Fulfillment Network (Fulfillment by Amazon)
        * MFN - Merchant Fulfillment Network (self-fulfilled)
    """

    payment_amount_type: Optional[str] = attrs.field()
    """
    The type of payment.
        Possible values:
        * Sales
    """

    sales_channel: Optional[str] = attrs.field()
    """
    The sales channel for the transaction.
    """

    seller_order_id: Optional[str] = attrs.field()
    """
    An order identifier that is specified by the seller.
    """

    store_name: Optional[str] = attrs.field()
    """
    The store name where the event occurred.
    """

    transaction_posted_date: Optional["Date"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProductAdsPaymentEvent:
    """
    A Sponsored Products payment event.
    """

    base_value: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    invoice_id: Optional[str] = attrs.field()
    """
    Identifier for the invoice that the transaction appears in.
    """

    posted_date: Optional["Date"] = attrs.field()

    tax_value: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    transaction_type: Optional[str] = attrs.field()
    """
    Indicates if the transaction is for a charge or a refund.
        Possible values:
        * charge - Charge
        * refund - Refund
    """

    transaction_value: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Promotion:
    """
    A promotion applied to an item.
    """

    promotion_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    promotion_id: Optional[str] = attrs.field()
    """
    The seller-specified identifier for the promotion.
    """

    promotion_type: Optional[str] = attrs.field()
    """
    The type of promotion.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RemovalShipmentAdjustmentEvent:
    """
    A financial adjustment event for FBA liquidated inventory. A positive value indicates money owed to Amazon by the buyer (for example, when the charge was incorrectly calculated as less than it should be). A negative value indicates a full or partial refund owed to the buyer (for example, when the buyer receives damaged items or fewer items than ordered).
    """

    adjustment_event_id: Optional[str] = attrs.field()
    """
    The unique identifier for the adjustment event.
    """

    merchant_order_id: Optional[str] = attrs.field()
    """
    The merchant removal orderId.
    """

    order_id: Optional[str] = attrs.field()
    """
    The orderId for shipping inventory.
    """

    posted_date: Optional["Date"] = attrs.field()

    removal_shipment_item_adjustment_list: Optional[List["RemovalShipmentItemAdjustment"]] = attrs.field()
    """
    A comma-delimited list of Removal shipmentItemAdjustment details for FBA inventory.
    """

    transaction_type: Optional[str] = attrs.field()
    """
    The type of removal order.
        Possible values:
        * WHOLESALE_LIQUIDATION.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RemovalShipmentEvent:
    """
    A removal shipment event for a removal order.
    """

    merchant_order_id: Optional[str] = attrs.field()
    """
    The merchant removal orderId.
    """

    order_id: Optional[str] = attrs.field()
    """
    The identifier for the removal shipment order.
    """

    posted_date: Optional["Date"] = attrs.field()

    removal_shipment_item_list: Optional[List["RemovalShipmentItem"]] = attrs.field()
    """
    A list of information about removal shipment items.
    """

    transaction_type: Optional[str] = attrs.field()
    """
    The type of removal order.
        Possible values:
        * WHOLESALE_LIQUIDATION
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RemovalShipmentItem:
    """
    Item-level information for a removal shipment.
    """

    fee_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    fulfillment_network_sku: Optional[str] = attrs.field()
    """
    The Amazon fulfillment network SKU for the item.
    """

    quantity: Optional[int] = attrs.field()
    """
    The quantity of the item.

    Extra fields:
    {'schema_format': 'int32'}
    """

    removal_shipment_item_id: Optional[str] = attrs.field()
    """
    An identifier for an item in a removal shipment.
    """

    revenue: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    tax_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    tax_collection_model: Optional[str] = attrs.field()
    """
    The tax collection model applied to the item.
        Possible values:
        * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.
        * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
    """

    tax_withheld: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RemovalShipmentItemAdjustment:
    """
    Item-level information for a removal shipment item adjustment.
    """

    adjusted_quantity: Optional[int] = attrs.field()
    """
    Adjusted quantity of removal shipmentItemAdjustment items.

    Extra fields:
    {'schema_format': 'int32'}
    """

    fulfillment_network_sku: Optional[str] = attrs.field()
    """
    The Amazon fulfillment network SKU for the item.
    """

    removal_shipment_item_id: Optional[str] = attrs.field()
    """
    An identifier for an item in a removal shipment.
    """

    revenue_adjustment: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    tax_amount_adjustment: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    tax_collection_model: Optional[str] = attrs.field()
    """
    The tax collection model applied to the item.
        Possible values:
        * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.
        * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
    """

    tax_withheld_adjustment: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RentalTransactionEvent:
    """
    An event related to a rental transaction.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    An Amazon-defined identifier for an order.
    """

    extension_length: Optional[int] = attrs.field()
    """
    The number of days that the buyer extended an already rented item. This value is only returned for RentalCustomerPayment-Extension and RentalCustomerRefund-Extension events.

    Extra fields:
    {'schema_format': 'int32'}
    """

    marketplace_name: Optional[str] = attrs.field()
    """
    The name of the marketplace.
    """

    posted_date: Optional["Date"] = attrs.field()

    rental_charge_list: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """

    rental_event_type: Optional[str] = attrs.field()
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

    rental_fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    rental_initial_value: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    rental_reimbursement: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    rental_tax_withheld_list: Optional[List["TaxWithheldComponent"]] = attrs.field()
    """
    A list of information about taxes withheld.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrochargeEvent:
    """
    A retrocharge or retrocharge reversal.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    An Amazon-defined identifier for an order.
    """

    base_tax: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    marketplace_name: Optional[str] = attrs.field()
    """
    The name of the marketplace where the retrocharge event occurred.
    """

    posted_date: Optional["Date"] = attrs.field()

    retrocharge_event_type: Optional[str] = attrs.field()
    """
    The type of event.
        Possible values:
        * Retrocharge
        * RetrochargeReversal
    """

    retrocharge_tax_withheld_list: Optional[List["TaxWithheldComponent"]] = attrs.field()
    """
    A list of information about taxes withheld.
    """

    shipping_tax: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SAFETReimbursementEvent:
    """
    A SAFE-T claim reimbursement on the seller's account.
    """

    posted_date: Optional["Date"] = attrs.field()

    reason_code: Optional[str] = attrs.field()
    """
    Indicates why the seller was reimbursed.
    """

    reimbursed_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    safetclaim_id: Optional[str] = attrs.field()
    """
    A SAFE-T claim identifier.
    """

    safetreimbursement_item_list: Optional[List["SAFETReimbursementItem"]] = attrs.field()
    """
    A list of SAFETReimbursementItems.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SAFETReimbursementItem:
    """
    An item from a SAFE-T claim reimbursement.
    """

    item_charge_list: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """

    product_description: Optional[str] = attrs.field()
    """
    The description of the item as shown on the product detail page on the retail website.
    """

    quantity: Optional[str] = attrs.field()
    """
    The number of units of the item being reimbursed.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerDealPaymentEvent:
    """
    An event linked to the payment of a fee related to the specified deal.
    """

    deal_description: Optional[str] = attrs.field()
    """
    The internal description of the deal.
    """

    deal_id: Optional[str] = attrs.field()
    """
    The unique identifier of the deal.
    """

    event_type: Optional[str] = attrs.field()
    """
    The type of event: SellerDealComplete.
    """

    fee_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    fee_type: Optional[str] = attrs.field()
    """
    The type of fee: RunLightningDealFee.
    """

    posted_date: Optional["Date"] = attrs.field()

    tax_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    total_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerReviewEnrollmentPaymentEvent:
    """
    A fee payment event for the Early Reviewer Program.
    """

    charge_component: Optional["ChargeComponent"] = attrs.field()
    """
    A charge on the seller's account.
        Possible values:
        * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered.
        * Tax - The tax collected by the seller on the Principal.
        * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal.
        * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge.
        * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge.
        * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges.
        * Discount - The promotional discount for an order item.
        * TaxDiscount - The tax amount deducted for promotional rebates.
        * CODItemCharge - The COD charge for an order item.
        * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge.
        * CODOrderCharge - The COD charge for an order.
        * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge.
        * CODShippingCharge - Shipping charges for a COD order.
        * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge.
        * ShippingCharge - The shipping charge.
        * ShippingTax - The tax collected by the seller on a ShippingCharge.
        * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience.
        * Giftwrap - The gift wrap charge.
        * GiftwrapTax - The tax collected by the seller on a Giftwrap charge.
        * RestockingFee - The charge applied to the buyer when returning a product in certain categories.
        * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault.
        * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction.
        * GenericDeduction - A generic bad debt deduction.
        * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item.
        * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.
        * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program.
        * SAFE-TReimbursement - The SAFE-T claim amount for the item.
        * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).
        * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).
        * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).
        * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
    """

    enrollment_id: Optional[str] = attrs.field()
    """
    An enrollment identifier.
    """

    fee_component: Optional["FeeComponent"] = attrs.field()
    """
    A fee associated with the event.
    """

    parent_asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item that was enrolled in the Early Reviewer Program.
    """

    posted_date: Optional["Date"] = attrs.field()

    total_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceFeeEvent:
    """
    A service fee on the seller's account.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    An Amazon-defined identifier for an order.
    """

    fee_description: Optional[str] = attrs.field()
    """
    A short description of the service fee event.
    """

    fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    fee_reason: Optional[str] = attrs.field()
    """
    A short description of the service fee reason.
    """

    fn_sku: Optional[str] = attrs.field()
    """
    A unique identifier assigned by Amazon to products stored in and fulfilled from an Amazon fulfillment center.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentEvent:
    """
    A shipment, refund, guarantee claim, or chargeback.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    An Amazon-defined identifier for an order.
    """

    direct_payment_list: Optional[List["DirectPayment"]] = attrs.field()
    """
    A list of direct payment information.
    """

    marketplace_name: Optional[str] = attrs.field()
    """
    The name of the marketplace where the event occurred.
    """

    order_charge_adjustment_list: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """

    order_charge_list: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """

    order_fee_adjustment_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    order_fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    posted_date: Optional["Date"] = attrs.field()

    seller_order_id: Optional[str] = attrs.field()
    """
    A seller-defined identifier for an order.
    """

    shipment_fee_adjustment_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    shipment_fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    shipment_item_adjustment_list: Optional[List["ShipmentItem"]] = attrs.field()
    """
    A list of shipment items.
    """

    shipment_item_list: Optional[List["ShipmentItem"]] = attrs.field()
    """
    A list of shipment items.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentItem:
    """
    An item of a shipment, refund, guarantee claim, or chargeback.
    """

    cost_of_points_granted: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    cost_of_points_returned: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    item_charge_adjustment_list: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """

    item_charge_list: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """

    item_fee_adjustment_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    item_fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    item_tax_withheld_list: Optional[List["TaxWithheldComponent"]] = attrs.field()
    """
    A list of information about taxes withheld.
    """

    order_adjustment_item_id: Optional[str] = attrs.field()
    """
    An Amazon-defined order adjustment identifier defined for refunds, guarantee claims, and chargeback events.
    """

    order_item_id: Optional[str] = attrs.field()
    """
    An Amazon-defined order item identifier.
    """

    promotion_adjustment_list: Optional[List["Promotion"]] = attrs.field()
    """
    A list of promotions.
    """

    promotion_list: Optional[List["Promotion"]] = attrs.field()
    """
    A list of promotions.
    """

    quantity_shipped: Optional[int] = attrs.field()
    """
    The number of items shipped.

    Extra fields:
    {'schema_format': 'int32'}
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SolutionProviderCreditEvent:
    """
    A credit given to a solution provider.
    """

    marketplace_country_code: Optional[str] = attrs.field()
    """
    The two-letter country code of the country associated with the marketplace where the order was placed.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    The identifier of the marketplace where the order was placed.
    """

    provider_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier of the solution provider.
    """

    provider_store_name: Optional[str] = attrs.field()
    """
    The store name where the payment event occurred.
    """

    provider_transaction_type: Optional[str] = attrs.field()
    """
    The transaction type.
    """

    seller_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier of the seller.
    """

    seller_order_id: Optional[str] = attrs.field()
    """
    A seller-defined identifier for an order.
    """

    seller_store_name: Optional[str] = attrs.field()
    """
    The store name where the payment event occurred.
    """

    transaction_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    transaction_creation_date: Optional["Date"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxWithheldComponent:
    """
    Information about the taxes withheld.
    """

    tax_collection_model: Optional[str] = attrs.field()
    """
    The tax collection model applied to the item.
        Possible values:
        * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.
        * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.
    """

    taxes_withheld: Optional[List["ChargeComponent"]] = attrs.field()
    """
    A list of charge information on the seller's account.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxWithholdingEvent:
    """
    A TaxWithholding event on seller's account.
    """

    base_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """

    posted_date: Optional["Date"] = attrs.field()

    tax_withholding_period: Optional["TaxWithholdingPeriod"] = attrs.field()
    """
    Period which taxwithholding on seller's account is calculated.
    """

    withheld_amount: Optional["Currency"] = attrs.field()
    """
    A currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxWithholdingPeriod:
    """
    Period which taxwithholding on seller's account is calculated.
    """

    end_date: Optional["Date"] = attrs.field()

    start_date: Optional["Date"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrialShipmentEvent:
    """
    An event related to a trial shipment.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    An Amazon-defined identifier for an order.
    """

    fee_list: Optional[List["FeeComponent"]] = attrs.field()
    """
    A list of fee component information.
    """

    financial_event_group_id: Optional[str] = attrs.field()
    """
    The identifier of the financial event group.
    """

    posted_date: Optional["Date"] = attrs.field()

    sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.
    """


class FinancesV0Client(BaseClient):
    def list_financial_event_groups(
        self,
        max_results_per_page: int = None,
        financial_event_group_started_before: datetime = None,
        financial_event_group_started_after: datetime = None,
        next_token: str = None,
    ) -> Union[ListFinancialEventGroupsResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_financial_event_groups_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_financial_event_groups_params = (  # name, param in
        ("MaxResultsPerPage", "query"),
        ("FinancialEventGroupStartedBefore", "query"),
        ("FinancialEventGroupStartedAfter", "query"),
        ("NextToken", "query"),
    )

    _list_financial_event_groups_responses = {
        (200, "application/json"): ListFinancialEventGroupsResponse,
        (400, "application/json"): ListFinancialEventGroupsResponse,
        (403, "application/json"): ListFinancialEventGroupsResponse,
        (404, "application/json"): ListFinancialEventGroupsResponse,
        (429, "application/json"): ListFinancialEventGroupsResponse,
        (500, "application/json"): ListFinancialEventGroupsResponse,
        (503, "application/json"): ListFinancialEventGroupsResponse,
    }

    def list_financial_events(
        self,
        max_results_per_page: int = None,
        posted_after: datetime = None,
        posted_before: datetime = None,
        next_token: str = None,
    ) -> Union[ListFinancialEventsResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_financial_events_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_financial_events_params = (  # name, param in
        ("MaxResultsPerPage", "query"),
        ("PostedAfter", "query"),
        ("PostedBefore", "query"),
        ("NextToken", "query"),
    )

    _list_financial_events_responses = {
        (200, "application/json"): ListFinancialEventsResponse,
        (400, "application/json"): ListFinancialEventsResponse,
        (403, "application/json"): ListFinancialEventsResponse,
        (404, "application/json"): ListFinancialEventsResponse,
        (429, "application/json"): ListFinancialEventsResponse,
        (500, "application/json"): ListFinancialEventsResponse,
        (503, "application/json"): ListFinancialEventsResponse,
    }

    def list_financial_events_by_group_id(
        self,
        event_group_id: str,
        max_results_per_page: int = None,
        next_token: str = None,
    ) -> Union[ListFinancialEventsResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_financial_events_by_group_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_financial_events_by_group_id_params = (  # name, param in
        ("MaxResultsPerPage", "query"),
        ("eventGroupId", "path"),
        ("NextToken", "query"),
    )

    _list_financial_events_by_group_id_responses = {
        (200, "application/json"): ListFinancialEventsResponse,
        (400, "application/json"): ListFinancialEventsResponse,
        (403, "application/json"): ListFinancialEventsResponse,
        (404, "application/json"): ListFinancialEventsResponse,
        (429, "application/json"): ListFinancialEventsResponse,
        (500, "application/json"): ListFinancialEventsResponse,
        (503, "application/json"): ListFinancialEventsResponse,
    }

    def list_financial_events_by_order_id(
        self,
        order_id: str,
        max_results_per_page: int = None,
        next_token: str = None,
    ) -> Union[ListFinancialEventsResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._list_financial_events_by_order_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _list_financial_events_by_order_id_params = (  # name, param in
        ("orderId", "path"),
        ("MaxResultsPerPage", "query"),
        ("NextToken", "query"),
    )

    _list_financial_events_by_order_id_responses = {
        (200, "application/json"): ListFinancialEventsResponse,
        (400, "application/json"): ListFinancialEventsResponse,
        (403, "application/json"): ListFinancialEventsResponse,
        (404, "application/json"): ListFinancialEventsResponse,
        (429, "application/json"): ListFinancialEventsResponse,
        (500, "application/json"): ListFinancialEventsResponse,
        (503, "application/json"): ListFinancialEventsResponse,
    }
