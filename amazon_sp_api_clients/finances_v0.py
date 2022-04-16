from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class AdjustmentEvent(__BaseDictObject):
    """
    An adjustment to the seller's account.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AdjustmentType" in data:
            self.AdjustmentType: str = self._get_value(str, "AdjustmentType")
        else:
            self.AdjustmentType: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "AdjustmentAmount" in data:
            self.AdjustmentAmount: Currency = self._get_value(Currency, "AdjustmentAmount")
        else:
            self.AdjustmentAmount: Currency = None
        if "AdjustmentItemList" in data:
            self.AdjustmentItemList: AdjustmentItemList = self._get_value(AdjustmentItemList, "AdjustmentItemList")
        else:
            self.AdjustmentItemList: AdjustmentItemList = None


class AdjustmentItem(__BaseDictObject):
    """
    An item in an adjustment to the seller's account.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Quantity" in data:
            self.Quantity: str = self._get_value(str, "Quantity")
        else:
            self.Quantity: str = None
        if "PerUnitAmount" in data:
            self.PerUnitAmount: Currency = self._get_value(Currency, "PerUnitAmount")
        else:
            self.PerUnitAmount: Currency = None
        if "TotalAmount" in data:
            self.TotalAmount: Currency = self._get_value(Currency, "TotalAmount")
        else:
            self.TotalAmount: Currency = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "FnSKU" in data:
            self.FnSKU: str = self._get_value(str, "FnSKU")
        else:
            self.FnSKU: str = None
        if "ProductDescription" in data:
            self.ProductDescription: str = self._get_value(str, "ProductDescription")
        else:
            self.ProductDescription: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None


class AffordabilityExpenseEvent(__BaseDictObject):
    """
    An expense related to an affordability promotion.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "TransactionType" in data:
            self.TransactionType: str = self._get_value(str, "TransactionType")
        else:
            self.TransactionType: str = None
        if "BaseExpense" in data:
            self.BaseExpense: Currency = self._get_value(Currency, "BaseExpense")
        else:
            self.BaseExpense: Currency = None
        if "TaxTypeCGST" in data:
            self.TaxTypeCGST: Currency = self._get_value(Currency, "TaxTypeCGST")
        else:
            self.TaxTypeCGST: Currency = None
        if "TaxTypeSGST" in data:
            self.TaxTypeSGST: Currency = self._get_value(Currency, "TaxTypeSGST")
        else:
            self.TaxTypeSGST: Currency = None
        if "TaxTypeIGST" in data:
            self.TaxTypeIGST: Currency = self._get_value(Currency, "TaxTypeIGST")
        else:
            self.TaxTypeIGST: Currency = None
        if "TotalExpense" in data:
            self.TotalExpense: Currency = self._get_value(Currency, "TotalExpense")
        else:
            self.TotalExpense: Currency = None


class ChargeComponent(__BaseDictObject):
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

    def __init__(self, data):
        super().__init__(data)
        if "ChargeType" in data:
            self.ChargeType: str = self._get_value(str, "ChargeType")
        else:
            self.ChargeType: str = None
        if "ChargeAmount" in data:
            self.ChargeAmount: Currency = self._get_value(Currency, "ChargeAmount")
        else:
            self.ChargeAmount: Currency = None


class ChargeInstrument(__BaseDictObject):
    """
    A payment instrument.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Description" in data:
            self.Description: str = self._get_value(str, "Description")
        else:
            self.Description: str = None
        if "Tail" in data:
            self.Tail: str = self._get_value(str, "Tail")
        else:
            self.Tail: str = None
        if "Amount" in data:
            self.Amount: Currency = self._get_value(Currency, "Amount")
        else:
            self.Amount: Currency = None


class CouponPaymentEvent(__BaseDictObject):
    """
    An event related to coupon payments.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "CouponId" in data:
            self.CouponId: str = self._get_value(str, "CouponId")
        else:
            self.CouponId: str = None
        if "SellerCouponDescription" in data:
            self.SellerCouponDescription: str = self._get_value(str, "SellerCouponDescription")
        else:
            self.SellerCouponDescription: str = None
        if "ClipOrRedemptionCount" in data:
            self.ClipOrRedemptionCount: int = self._get_value(int, "ClipOrRedemptionCount")
        else:
            self.ClipOrRedemptionCount: int = None
        if "PaymentEventId" in data:
            self.PaymentEventId: str = self._get_value(str, "PaymentEventId")
        else:
            self.PaymentEventId: str = None
        if "FeeComponent" in data:
            self.FeeComponent: FeeComponent = self._get_value(FeeComponent, "FeeComponent")
        else:
            self.FeeComponent: FeeComponent = None
        if "ChargeComponent" in data:
            self.ChargeComponent: ChargeComponent = self._get_value(ChargeComponent, "ChargeComponent")
        else:
            self.ChargeComponent: ChargeComponent = None
        if "TotalAmount" in data:
            self.TotalAmount: Currency = self._get_value(Currency, "TotalAmount")
        else:
            self.TotalAmount: Currency = None


class Currency(__BaseDictObject):
    """
    A currency type and amount.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None
        if "CurrencyAmount" in data:
            self.CurrencyAmount: BigDecimal = self._get_value(BigDecimal, "CurrencyAmount")
        else:
            self.CurrencyAmount: BigDecimal = None


class DebtRecoveryEvent(__BaseDictObject):
    """
    A debt payment or debt adjustment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DebtRecoveryType" in data:
            self.DebtRecoveryType: str = self._get_value(str, "DebtRecoveryType")
        else:
            self.DebtRecoveryType: str = None
        if "RecoveryAmount" in data:
            self.RecoveryAmount: Currency = self._get_value(Currency, "RecoveryAmount")
        else:
            self.RecoveryAmount: Currency = None
        if "OverPaymentCredit" in data:
            self.OverPaymentCredit: Currency = self._get_value(Currency, "OverPaymentCredit")
        else:
            self.OverPaymentCredit: Currency = None
        if "DebtRecoveryItemList" in data:
            self.DebtRecoveryItemList: DebtRecoveryItemList = self._get_value(
                DebtRecoveryItemList, "DebtRecoveryItemList"
            )
        else:
            self.DebtRecoveryItemList: DebtRecoveryItemList = None
        if "ChargeInstrumentList" in data:
            self.ChargeInstrumentList: ChargeInstrumentList = self._get_value(
                ChargeInstrumentList, "ChargeInstrumentList"
            )
        else:
            self.ChargeInstrumentList: ChargeInstrumentList = None


class DebtRecoveryItem(__BaseDictObject):
    """
    An item of a debt payment or debt adjustment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "RecoveryAmount" in data:
            self.RecoveryAmount: Currency = self._get_value(Currency, "RecoveryAmount")
        else:
            self.RecoveryAmount: Currency = None
        if "OriginalAmount" in data:
            self.OriginalAmount: Currency = self._get_value(Currency, "OriginalAmount")
        else:
            self.OriginalAmount: Currency = None
        if "GroupBeginDate" in data:
            self.GroupBeginDate: Date = self._get_value(Date, "GroupBeginDate")
        else:
            self.GroupBeginDate: Date = None
        if "GroupEndDate" in data:
            self.GroupEndDate: Date = self._get_value(Date, "GroupEndDate")
        else:
            self.GroupEndDate: Date = None


class DirectPayment(__BaseDictObject):
    """
    A payment made directly to a seller.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DirectPaymentType" in data:
            self.DirectPaymentType: str = self._get_value(str, "DirectPaymentType")
        else:
            self.DirectPaymentType: str = None
        if "DirectPaymentAmount" in data:
            self.DirectPaymentAmount: Currency = self._get_value(Currency, "DirectPaymentAmount")
        else:
            self.DirectPaymentAmount: Currency = None


class FBALiquidationEvent(__BaseDictObject):
    """
    A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "OriginalRemovalOrderId" in data:
            self.OriginalRemovalOrderId: str = self._get_value(str, "OriginalRemovalOrderId")
        else:
            self.OriginalRemovalOrderId: str = None
        if "LiquidationProceedsAmount" in data:
            self.LiquidationProceedsAmount: Currency = self._get_value(Currency, "LiquidationProceedsAmount")
        else:
            self.LiquidationProceedsAmount: Currency = None
        if "LiquidationFeeAmount" in data:
            self.LiquidationFeeAmount: Currency = self._get_value(Currency, "LiquidationFeeAmount")
        else:
            self.LiquidationFeeAmount: Currency = None


class FeeComponent(__BaseDictObject):
    """
    A fee associated with the event.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FeeType" in data:
            self.FeeType: str = self._get_value(str, "FeeType")
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: Currency = self._get_value(Currency, "FeeAmount")
        else:
            self.FeeAmount: Currency = None


class FinancialEventGroup(__BaseDictObject):
    """
    Information related to a financial event group.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FinancialEventGroupId" in data:
            self.FinancialEventGroupId: str = self._get_value(str, "FinancialEventGroupId")
        else:
            self.FinancialEventGroupId: str = None
        if "ProcessingStatus" in data:
            self.ProcessingStatus: str = self._get_value(str, "ProcessingStatus")
        else:
            self.ProcessingStatus: str = None
        if "FundTransferStatus" in data:
            self.FundTransferStatus: str = self._get_value(str, "FundTransferStatus")
        else:
            self.FundTransferStatus: str = None
        if "OriginalTotal" in data:
            self.OriginalTotal: Currency = self._get_value(Currency, "OriginalTotal")
        else:
            self.OriginalTotal: Currency = None
        if "ConvertedTotal" in data:
            self.ConvertedTotal: Currency = self._get_value(Currency, "ConvertedTotal")
        else:
            self.ConvertedTotal: Currency = None
        if "FundTransferDate" in data:
            self.FundTransferDate: Date = self._get_value(Date, "FundTransferDate")
        else:
            self.FundTransferDate: Date = None
        if "TraceId" in data:
            self.TraceId: str = self._get_value(str, "TraceId")
        else:
            self.TraceId: str = None
        if "AccountTail" in data:
            self.AccountTail: str = self._get_value(str, "AccountTail")
        else:
            self.AccountTail: str = None
        if "BeginningBalance" in data:
            self.BeginningBalance: Currency = self._get_value(Currency, "BeginningBalance")
        else:
            self.BeginningBalance: Currency = None
        if "FinancialEventGroupStart" in data:
            self.FinancialEventGroupStart: Date = self._get_value(Date, "FinancialEventGroupStart")
        else:
            self.FinancialEventGroupStart: Date = None
        if "FinancialEventGroupEnd" in data:
            self.FinancialEventGroupEnd: Date = self._get_value(Date, "FinancialEventGroupEnd")
        else:
            self.FinancialEventGroupEnd: Date = None


class FinancialEvents(__BaseDictObject):
    """
    Contains all information related to a financial event.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShipmentEventList" in data:
            self.ShipmentEventList: ShipmentEventList = self._get_value(ShipmentEventList, "ShipmentEventList")
        else:
            self.ShipmentEventList: ShipmentEventList = None
        if "RefundEventList" in data:
            self.RefundEventList: ShipmentEventList = self._get_value(ShipmentEventList, "RefundEventList")
        else:
            self.RefundEventList: ShipmentEventList = None
        if "GuaranteeClaimEventList" in data:
            self.GuaranteeClaimEventList: ShipmentEventList = self._get_value(
                ShipmentEventList, "GuaranteeClaimEventList"
            )
        else:
            self.GuaranteeClaimEventList: ShipmentEventList = None
        if "ChargebackEventList" in data:
            self.ChargebackEventList: ShipmentEventList = self._get_value(ShipmentEventList, "ChargebackEventList")
        else:
            self.ChargebackEventList: ShipmentEventList = None
        if "PayWithAmazonEventList" in data:
            self.PayWithAmazonEventList: PayWithAmazonEventList = self._get_value(
                PayWithAmazonEventList, "PayWithAmazonEventList"
            )
        else:
            self.PayWithAmazonEventList: PayWithAmazonEventList = None
        if "ServiceProviderCreditEventList" in data:
            self.ServiceProviderCreditEventList: SolutionProviderCreditEventList = self._get_value(
                SolutionProviderCreditEventList, "ServiceProviderCreditEventList"
            )
        else:
            self.ServiceProviderCreditEventList: SolutionProviderCreditEventList = None
        if "RetrochargeEventList" in data:
            self.RetrochargeEventList: RetrochargeEventList = self._get_value(
                RetrochargeEventList, "RetrochargeEventList"
            )
        else:
            self.RetrochargeEventList: RetrochargeEventList = None
        if "RentalTransactionEventList" in data:
            self.RentalTransactionEventList: RentalTransactionEventList = self._get_value(
                RentalTransactionEventList, "RentalTransactionEventList"
            )
        else:
            self.RentalTransactionEventList: RentalTransactionEventList = None
        if "ProductAdsPaymentEventList" in data:
            self.ProductAdsPaymentEventList: ProductAdsPaymentEventList = self._get_value(
                ProductAdsPaymentEventList, "ProductAdsPaymentEventList"
            )
        else:
            self.ProductAdsPaymentEventList: ProductAdsPaymentEventList = None
        if "ServiceFeeEventList" in data:
            self.ServiceFeeEventList: ServiceFeeEventList = self._get_value(ServiceFeeEventList, "ServiceFeeEventList")
        else:
            self.ServiceFeeEventList: ServiceFeeEventList = None
        if "SellerDealPaymentEventList" in data:
            self.SellerDealPaymentEventList: SellerDealPaymentEventList = self._get_value(
                SellerDealPaymentEventList, "SellerDealPaymentEventList"
            )
        else:
            self.SellerDealPaymentEventList: SellerDealPaymentEventList = None
        if "DebtRecoveryEventList" in data:
            self.DebtRecoveryEventList: DebtRecoveryEventList = self._get_value(
                DebtRecoveryEventList, "DebtRecoveryEventList"
            )
        else:
            self.DebtRecoveryEventList: DebtRecoveryEventList = None
        if "LoanServicingEventList" in data:
            self.LoanServicingEventList: LoanServicingEventList = self._get_value(
                LoanServicingEventList, "LoanServicingEventList"
            )
        else:
            self.LoanServicingEventList: LoanServicingEventList = None
        if "AdjustmentEventList" in data:
            self.AdjustmentEventList: AdjustmentEventList = self._get_value(AdjustmentEventList, "AdjustmentEventList")
        else:
            self.AdjustmentEventList: AdjustmentEventList = None
        if "SAFETReimbursementEventList" in data:
            self.SAFETReimbursementEventList: SAFETReimbursementEventList = self._get_value(
                SAFETReimbursementEventList, "SAFETReimbursementEventList"
            )
        else:
            self.SAFETReimbursementEventList: SAFETReimbursementEventList = None
        if "SellerReviewEnrollmentPaymentEventList" in data:
            self.SellerReviewEnrollmentPaymentEventList: SellerReviewEnrollmentPaymentEventList = self._get_value(
                SellerReviewEnrollmentPaymentEventList, "SellerReviewEnrollmentPaymentEventList"
            )
        else:
            self.SellerReviewEnrollmentPaymentEventList: SellerReviewEnrollmentPaymentEventList = None
        if "FBALiquidationEventList" in data:
            self.FBALiquidationEventList: FBALiquidationEventList = self._get_value(
                FBALiquidationEventList, "FBALiquidationEventList"
            )
        else:
            self.FBALiquidationEventList: FBALiquidationEventList = None
        if "CouponPaymentEventList" in data:
            self.CouponPaymentEventList: CouponPaymentEventList = self._get_value(
                CouponPaymentEventList, "CouponPaymentEventList"
            )
        else:
            self.CouponPaymentEventList: CouponPaymentEventList = None
        if "ImagingServicesFeeEventList" in data:
            self.ImagingServicesFeeEventList: ImagingServicesFeeEventList = self._get_value(
                ImagingServicesFeeEventList, "ImagingServicesFeeEventList"
            )
        else:
            self.ImagingServicesFeeEventList: ImagingServicesFeeEventList = None
        if "NetworkComminglingTransactionEventList" in data:
            self.NetworkComminglingTransactionEventList: NetworkComminglingTransactionEventList = self._get_value(
                NetworkComminglingTransactionEventList, "NetworkComminglingTransactionEventList"
            )
        else:
            self.NetworkComminglingTransactionEventList: NetworkComminglingTransactionEventList = None
        if "AffordabilityExpenseEventList" in data:
            self.AffordabilityExpenseEventList: AffordabilityExpenseEventList = self._get_value(
                AffordabilityExpenseEventList, "AffordabilityExpenseEventList"
            )
        else:
            self.AffordabilityExpenseEventList: AffordabilityExpenseEventList = None
        if "AffordabilityExpenseReversalEventList" in data:
            self.AffordabilityExpenseReversalEventList: AffordabilityExpenseEventList = self._get_value(
                AffordabilityExpenseEventList, "AffordabilityExpenseReversalEventList"
            )
        else:
            self.AffordabilityExpenseReversalEventList: AffordabilityExpenseEventList = None
        if "TrialShipmentEventList" in data:
            self.TrialShipmentEventList: TrialShipmentEventList = self._get_value(
                TrialShipmentEventList, "TrialShipmentEventList"
            )
        else:
            self.TrialShipmentEventList: TrialShipmentEventList = None
        if "ShipmentSettleEventList" in data:
            self.ShipmentSettleEventList: ShipmentSettleEventList = self._get_value(
                ShipmentSettleEventList, "ShipmentSettleEventList"
            )
        else:
            self.ShipmentSettleEventList: ShipmentSettleEventList = None
        if "TaxWithholdingEventList" in data:
            self.TaxWithholdingEventList: TaxWithholdingEventList = self._get_value(
                TaxWithholdingEventList, "TaxWithholdingEventList"
            )
        else:
            self.TaxWithholdingEventList: TaxWithholdingEventList = None
        if "RemovalShipmentEventList" in data:
            self.RemovalShipmentEventList: RemovalShipmentEventList = self._get_value(
                RemovalShipmentEventList, "RemovalShipmentEventList"
            )
        else:
            self.RemovalShipmentEventList: RemovalShipmentEventList = None
        if "RemovalShipmentAdjustmentEventList" in data:
            self.RemovalShipmentAdjustmentEventList: RemovalShipmentAdjustmentEventList = self._get_value(
                RemovalShipmentAdjustmentEventList, "RemovalShipmentAdjustmentEventList"
            )
        else:
            self.RemovalShipmentAdjustmentEventList: RemovalShipmentAdjustmentEventList = None


class ImagingServicesFeeEvent(__BaseDictObject):
    """
    A fee event related to Amazon Imaging services.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ImagingRequestBillingItemID" in data:
            self.ImagingRequestBillingItemID: str = self._get_value(str, "ImagingRequestBillingItemID")
        else:
            self.ImagingRequestBillingItemID: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = self._get_value(FeeComponentList, "FeeList")
        else:
            self.FeeList: FeeComponentList = None


class ListFinancialEventGroupsPayload(__BaseDictObject):
    """
    The payload for the listFinancialEventGroups operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "FinancialEventGroupList" in data:
            self.FinancialEventGroupList: FinancialEventGroupList = self._get_value(
                FinancialEventGroupList, "FinancialEventGroupList"
            )
        else:
            self.FinancialEventGroupList: FinancialEventGroupList = None


class ListFinancialEventGroupsResponse(__BaseDictObject):
    """
    The response schema for the listFinancialEventGroups operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ListFinancialEventGroupsPayload = self._get_value(ListFinancialEventGroupsPayload, "payload")
        else:
            self.payload: ListFinancialEventGroupsPayload = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ListFinancialEventsPayload(__BaseDictObject):
    """
    The payload for the listFinancialEvents operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "FinancialEvents" in data:
            self.FinancialEvents: FinancialEvents = self._get_value(FinancialEvents, "FinancialEvents")
        else:
            self.FinancialEvents: FinancialEvents = None


class ListFinancialEventsResponse(__BaseDictObject):
    """
    The response schema for the listFinancialEvents operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ListFinancialEventsPayload = self._get_value(ListFinancialEventsPayload, "payload")
        else:
            self.payload: ListFinancialEventsPayload = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class LoanServicingEvent(__BaseDictObject):
    """
    A loan advance, loan payment, or loan refund.
    """

    def __init__(self, data):
        super().__init__(data)
        if "LoanAmount" in data:
            self.LoanAmount: Currency = self._get_value(Currency, "LoanAmount")
        else:
            self.LoanAmount: Currency = None
        if "SourceBusinessEventType" in data:
            self.SourceBusinessEventType: str = self._get_value(str, "SourceBusinessEventType")
        else:
            self.SourceBusinessEventType: str = None


class NetworkComminglingTransactionEvent(__BaseDictObject):
    """
    A network commingling transaction event.
    """

    def __init__(self, data):
        super().__init__(data)
        if "TransactionType" in data:
            self.TransactionType: str = self._get_value(str, "TransactionType")
        else:
            self.TransactionType: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "NetCoTransactionID" in data:
            self.NetCoTransactionID: str = self._get_value(str, "NetCoTransactionID")
        else:
            self.NetCoTransactionID: str = None
        if "SwapReason" in data:
            self.SwapReason: str = self._get_value(str, "SwapReason")
        else:
            self.SwapReason: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "TaxExclusiveAmount" in data:
            self.TaxExclusiveAmount: Currency = self._get_value(Currency, "TaxExclusiveAmount")
        else:
            self.TaxExclusiveAmount: Currency = None
        if "TaxAmount" in data:
            self.TaxAmount: Currency = self._get_value(Currency, "TaxAmount")
        else:
            self.TaxAmount: Currency = None


class PayWithAmazonEvent(__BaseDictObject):
    """
    An event related to the seller's Pay with Amazon account.
    """

    def __init__(self, data):
        super().__init__(data)
        if "SellerOrderId" in data:
            self.SellerOrderId: str = self._get_value(str, "SellerOrderId")
        else:
            self.SellerOrderId: str = None
        if "TransactionPostedDate" in data:
            self.TransactionPostedDate: Date = self._get_value(Date, "TransactionPostedDate")
        else:
            self.TransactionPostedDate: Date = None
        if "BusinessObjectType" in data:
            self.BusinessObjectType: str = self._get_value(str, "BusinessObjectType")
        else:
            self.BusinessObjectType: str = None
        if "SalesChannel" in data:
            self.SalesChannel: str = self._get_value(str, "SalesChannel")
        else:
            self.SalesChannel: str = None
        if "Charge" in data:
            self.Charge: ChargeComponent = self._get_value(ChargeComponent, "Charge")
        else:
            self.Charge: ChargeComponent = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = self._get_value(FeeComponentList, "FeeList")
        else:
            self.FeeList: FeeComponentList = None
        if "PaymentAmountType" in data:
            self.PaymentAmountType: str = self._get_value(str, "PaymentAmountType")
        else:
            self.PaymentAmountType: str = None
        if "AmountDescription" in data:
            self.AmountDescription: str = self._get_value(str, "AmountDescription")
        else:
            self.AmountDescription: str = None
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = self._get_value(str, "FulfillmentChannel")
        else:
            self.FulfillmentChannel: str = None
        if "StoreName" in data:
            self.StoreName: str = self._get_value(str, "StoreName")
        else:
            self.StoreName: str = None


class ProductAdsPaymentEvent(__BaseDictObject):
    """
    A Sponsored Products payment event.
    """

    def __init__(self, data):
        super().__init__(data)
        if "postedDate" in data:
            self.postedDate: Date = self._get_value(Date, "postedDate")
        else:
            self.postedDate: Date = None
        if "transactionType" in data:
            self.transactionType: str = self._get_value(str, "transactionType")
        else:
            self.transactionType: str = None
        if "invoiceId" in data:
            self.invoiceId: str = self._get_value(str, "invoiceId")
        else:
            self.invoiceId: str = None
        if "baseValue" in data:
            self.baseValue: Currency = self._get_value(Currency, "baseValue")
        else:
            self.baseValue: Currency = None
        if "taxValue" in data:
            self.taxValue: Currency = self._get_value(Currency, "taxValue")
        else:
            self.taxValue: Currency = None
        if "transactionValue" in data:
            self.transactionValue: Currency = self._get_value(Currency, "transactionValue")
        else:
            self.transactionValue: Currency = None


class Promotion(__BaseDictObject):
    """
    A promotion applied to an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PromotionType" in data:
            self.PromotionType: str = self._get_value(str, "PromotionType")
        else:
            self.PromotionType: str = None
        if "PromotionId" in data:
            self.PromotionId: str = self._get_value(str, "PromotionId")
        else:
            self.PromotionId: str = None
        if "PromotionAmount" in data:
            self.PromotionAmount: Currency = self._get_value(Currency, "PromotionAmount")
        else:
            self.PromotionAmount: Currency = None


class RemovalShipmentEvent(__BaseDictObject):
    """
    A removal shipment event for a removal order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "MerchantOrderId" in data:
            self.MerchantOrderId: str = self._get_value(str, "MerchantOrderId")
        else:
            self.MerchantOrderId: str = None
        if "OrderId" in data:
            self.OrderId: str = self._get_value(str, "OrderId")
        else:
            self.OrderId: str = None
        if "TransactionType" in data:
            self.TransactionType: str = self._get_value(str, "TransactionType")
        else:
            self.TransactionType: str = None
        if "RemovalShipmentItemList" in data:
            self.RemovalShipmentItemList: RemovalShipmentItemList = self._get_value(
                RemovalShipmentItemList, "RemovalShipmentItemList"
            )
        else:
            self.RemovalShipmentItemList: RemovalShipmentItemList = None


class RemovalShipmentItem(__BaseDictObject):
    """
    Item-level information for a removal shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "RemovalShipmentItemId" in data:
            self.RemovalShipmentItemId: str = self._get_value(str, "RemovalShipmentItemId")
        else:
            self.RemovalShipmentItemId: str = None
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = self._get_value(str, "TaxCollectionModel")
        else:
            self.TaxCollectionModel: str = None
        if "FulfillmentNetworkSKU" in data:
            self.FulfillmentNetworkSKU: str = self._get_value(str, "FulfillmentNetworkSKU")
        else:
            self.FulfillmentNetworkSKU: str = None
        if "Quantity" in data:
            self.Quantity: int = self._get_value(int, "Quantity")
        else:
            self.Quantity: int = None
        if "Revenue" in data:
            self.Revenue: Currency = self._get_value(Currency, "Revenue")
        else:
            self.Revenue: Currency = None
        if "FeeAmount" in data:
            self.FeeAmount: Currency = self._get_value(Currency, "FeeAmount")
        else:
            self.FeeAmount: Currency = None
        if "TaxAmount" in data:
            self.TaxAmount: Currency = self._get_value(Currency, "TaxAmount")
        else:
            self.TaxAmount: Currency = None
        if "TaxWithheld" in data:
            self.TaxWithheld: Currency = self._get_value(Currency, "TaxWithheld")
        else:
            self.TaxWithheld: Currency = None


class RemovalShipmentAdjustmentEvent(__BaseDictObject):
    """
    A financial adjustment event for FBA liquidated inventory. A positive value indicates money owed to Amazon by the buyer (for example, when the charge was incorrectly calculated as less than it should be). A negative value indicates a full or partial refund owed to the buyer (for example, when the buyer receives damaged items or fewer items than ordered).
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "AdjustmentEventId" in data:
            self.AdjustmentEventId: str = self._get_value(str, "AdjustmentEventId")
        else:
            self.AdjustmentEventId: str = None
        if "MerchantOrderId" in data:
            self.MerchantOrderId: str = self._get_value(str, "MerchantOrderId")
        else:
            self.MerchantOrderId: str = None
        if "OrderId" in data:
            self.OrderId: str = self._get_value(str, "OrderId")
        else:
            self.OrderId: str = None
        if "TransactionType" in data:
            self.TransactionType: str = self._get_value(str, "TransactionType")
        else:
            self.TransactionType: str = None
        if "RemovalShipmentItemAdjustmentList" in data:
            self.RemovalShipmentItemAdjustmentList: _List[RemovalShipmentItemAdjustment] = [
                RemovalShipmentItemAdjustment(datum) for datum in data["RemovalShipmentItemAdjustmentList"]
            ]
        else:
            self.RemovalShipmentItemAdjustmentList: _List[RemovalShipmentItemAdjustment] = []


class RemovalShipmentItemAdjustment(__BaseDictObject):
    """
    Item-level information for a removal shipment item adjustment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "RemovalShipmentItemId" in data:
            self.RemovalShipmentItemId: str = self._get_value(str, "RemovalShipmentItemId")
        else:
            self.RemovalShipmentItemId: str = None
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = self._get_value(str, "TaxCollectionModel")
        else:
            self.TaxCollectionModel: str = None
        if "FulfillmentNetworkSKU" in data:
            self.FulfillmentNetworkSKU: str = self._get_value(str, "FulfillmentNetworkSKU")
        else:
            self.FulfillmentNetworkSKU: str = None
        if "AdjustedQuantity" in data:
            self.AdjustedQuantity: int = self._get_value(int, "AdjustedQuantity")
        else:
            self.AdjustedQuantity: int = None
        if "RevenueAdjustment" in data:
            self.RevenueAdjustment: Currency = self._get_value(Currency, "RevenueAdjustment")
        else:
            self.RevenueAdjustment: Currency = None
        if "TaxAmountAdjustment" in data:
            self.TaxAmountAdjustment: Currency = self._get_value(Currency, "TaxAmountAdjustment")
        else:
            self.TaxAmountAdjustment: Currency = None
        if "TaxWithheldAdjustment" in data:
            self.TaxWithheldAdjustment: Currency = self._get_value(Currency, "TaxWithheldAdjustment")
        else:
            self.TaxWithheldAdjustment: Currency = None


class RentalTransactionEvent(__BaseDictObject):
    """
    An event related to a rental transaction.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "RentalEventType" in data:
            self.RentalEventType: str = self._get_value(str, "RentalEventType")
        else:
            self.RentalEventType: str = None
        if "ExtensionLength" in data:
            self.ExtensionLength: int = self._get_value(int, "ExtensionLength")
        else:
            self.ExtensionLength: int = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "RentalChargeList" in data:
            self.RentalChargeList: ChargeComponentList = self._get_value(ChargeComponentList, "RentalChargeList")
        else:
            self.RentalChargeList: ChargeComponentList = None
        if "RentalFeeList" in data:
            self.RentalFeeList: FeeComponentList = self._get_value(FeeComponentList, "RentalFeeList")
        else:
            self.RentalFeeList: FeeComponentList = None
        if "MarketplaceName" in data:
            self.MarketplaceName: str = self._get_value(str, "MarketplaceName")
        else:
            self.MarketplaceName: str = None
        if "RentalInitialValue" in data:
            self.RentalInitialValue: Currency = self._get_value(Currency, "RentalInitialValue")
        else:
            self.RentalInitialValue: Currency = None
        if "RentalReimbursement" in data:
            self.RentalReimbursement: Currency = self._get_value(Currency, "RentalReimbursement")
        else:
            self.RentalReimbursement: Currency = None
        if "RentalTaxWithheldList" in data:
            self.RentalTaxWithheldList: TaxWithheldComponentList = self._get_value(
                TaxWithheldComponentList, "RentalTaxWithheldList"
            )
        else:
            self.RentalTaxWithheldList: TaxWithheldComponentList = None


class RetrochargeEvent(__BaseDictObject):
    """
    A retrocharge or retrocharge reversal.
    """

    def __init__(self, data):
        super().__init__(data)
        if "RetrochargeEventType" in data:
            self.RetrochargeEventType: str = self._get_value(str, "RetrochargeEventType")
        else:
            self.RetrochargeEventType: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "BaseTax" in data:
            self.BaseTax: Currency = self._get_value(Currency, "BaseTax")
        else:
            self.BaseTax: Currency = None
        if "ShippingTax" in data:
            self.ShippingTax: Currency = self._get_value(Currency, "ShippingTax")
        else:
            self.ShippingTax: Currency = None
        if "MarketplaceName" in data:
            self.MarketplaceName: str = self._get_value(str, "MarketplaceName")
        else:
            self.MarketplaceName: str = None
        if "RetrochargeTaxWithheldList" in data:
            self.RetrochargeTaxWithheldList: TaxWithheldComponentList = self._get_value(
                TaxWithheldComponentList, "RetrochargeTaxWithheldList"
            )
        else:
            self.RetrochargeTaxWithheldList: TaxWithheldComponentList = None


class SAFETReimbursementEvent(__BaseDictObject):
    """
    A SAFE-T claim reimbursement on the seller's account.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "SAFETClaimId" in data:
            self.SAFETClaimId: str = self._get_value(str, "SAFETClaimId")
        else:
            self.SAFETClaimId: str = None
        if "ReimbursedAmount" in data:
            self.ReimbursedAmount: Currency = self._get_value(Currency, "ReimbursedAmount")
        else:
            self.ReimbursedAmount: Currency = None
        if "ReasonCode" in data:
            self.ReasonCode: str = self._get_value(str, "ReasonCode")
        else:
            self.ReasonCode: str = None
        if "SAFETReimbursementItemList" in data:
            self.SAFETReimbursementItemList: SAFETReimbursementItemList = self._get_value(
                SAFETReimbursementItemList, "SAFETReimbursementItemList"
            )
        else:
            self.SAFETReimbursementItemList: SAFETReimbursementItemList = None


class SAFETReimbursementItem(__BaseDictObject):
    """
    An item from a SAFE-T claim reimbursement.
    """

    def __init__(self, data):
        super().__init__(data)
        if "itemChargeList" in data:
            self.itemChargeList: ChargeComponentList = self._get_value(ChargeComponentList, "itemChargeList")
        else:
            self.itemChargeList: ChargeComponentList = None
        if "productDescription" in data:
            self.productDescription: str = self._get_value(str, "productDescription")
        else:
            self.productDescription: str = None
        if "quantity" in data:
            self.quantity: str = self._get_value(str, "quantity")
        else:
            self.quantity: str = None


class SellerDealPaymentEvent(__BaseDictObject):
    """
    An event linked to the payment of a fee related to the specified deal.
    """

    def __init__(self, data):
        super().__init__(data)
        if "postedDate" in data:
            self.postedDate: Date = self._get_value(Date, "postedDate")
        else:
            self.postedDate: Date = None
        if "dealId" in data:
            self.dealId: str = self._get_value(str, "dealId")
        else:
            self.dealId: str = None
        if "dealDescription" in data:
            self.dealDescription: str = self._get_value(str, "dealDescription")
        else:
            self.dealDescription: str = None
        if "eventType" in data:
            self.eventType: str = self._get_value(str, "eventType")
        else:
            self.eventType: str = None
        if "feeType" in data:
            self.feeType: str = self._get_value(str, "feeType")
        else:
            self.feeType: str = None
        if "feeAmount" in data:
            self.feeAmount: Currency = self._get_value(Currency, "feeAmount")
        else:
            self.feeAmount: Currency = None
        if "taxAmount" in data:
            self.taxAmount: Currency = self._get_value(Currency, "taxAmount")
        else:
            self.taxAmount: Currency = None
        if "totalAmount" in data:
            self.totalAmount: Currency = self._get_value(Currency, "totalAmount")
        else:
            self.totalAmount: Currency = None


class SellerReviewEnrollmentPaymentEvent(__BaseDictObject):
    """
    A fee payment event for the Early Reviewer Program.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "EnrollmentId" in data:
            self.EnrollmentId: str = self._get_value(str, "EnrollmentId")
        else:
            self.EnrollmentId: str = None
        if "ParentASIN" in data:
            self.ParentASIN: str = self._get_value(str, "ParentASIN")
        else:
            self.ParentASIN: str = None
        if "FeeComponent" in data:
            self.FeeComponent: FeeComponent = self._get_value(FeeComponent, "FeeComponent")
        else:
            self.FeeComponent: FeeComponent = None
        if "ChargeComponent" in data:
            self.ChargeComponent: ChargeComponent = self._get_value(ChargeComponent, "ChargeComponent")
        else:
            self.ChargeComponent: ChargeComponent = None
        if "TotalAmount" in data:
            self.TotalAmount: Currency = self._get_value(Currency, "TotalAmount")
        else:
            self.TotalAmount: Currency = None


class ServiceFeeEvent(__BaseDictObject):
    """
    A service fee on the seller's account.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "FeeReason" in data:
            self.FeeReason: str = self._get_value(str, "FeeReason")
        else:
            self.FeeReason: str = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = self._get_value(FeeComponentList, "FeeList")
        else:
            self.FeeList: FeeComponentList = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "FnSKU" in data:
            self.FnSKU: str = self._get_value(str, "FnSKU")
        else:
            self.FnSKU: str = None
        if "FeeDescription" in data:
            self.FeeDescription: str = self._get_value(str, "FeeDescription")
        else:
            self.FeeDescription: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None


class ShipmentEvent(__BaseDictObject):
    """
    A shipment, refund, guarantee claim, or chargeback.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "SellerOrderId" in data:
            self.SellerOrderId: str = self._get_value(str, "SellerOrderId")
        else:
            self.SellerOrderId: str = None
        if "MarketplaceName" in data:
            self.MarketplaceName: str = self._get_value(str, "MarketplaceName")
        else:
            self.MarketplaceName: str = None
        if "OrderChargeList" in data:
            self.OrderChargeList: ChargeComponentList = self._get_value(ChargeComponentList, "OrderChargeList")
        else:
            self.OrderChargeList: ChargeComponentList = None
        if "OrderChargeAdjustmentList" in data:
            self.OrderChargeAdjustmentList: ChargeComponentList = self._get_value(
                ChargeComponentList, "OrderChargeAdjustmentList"
            )
        else:
            self.OrderChargeAdjustmentList: ChargeComponentList = None
        if "ShipmentFeeList" in data:
            self.ShipmentFeeList: FeeComponentList = self._get_value(FeeComponentList, "ShipmentFeeList")
        else:
            self.ShipmentFeeList: FeeComponentList = None
        if "ShipmentFeeAdjustmentList" in data:
            self.ShipmentFeeAdjustmentList: FeeComponentList = self._get_value(
                FeeComponentList, "ShipmentFeeAdjustmentList"
            )
        else:
            self.ShipmentFeeAdjustmentList: FeeComponentList = None
        if "OrderFeeList" in data:
            self.OrderFeeList: FeeComponentList = self._get_value(FeeComponentList, "OrderFeeList")
        else:
            self.OrderFeeList: FeeComponentList = None
        if "OrderFeeAdjustmentList" in data:
            self.OrderFeeAdjustmentList: FeeComponentList = self._get_value(FeeComponentList, "OrderFeeAdjustmentList")
        else:
            self.OrderFeeAdjustmentList: FeeComponentList = None
        if "DirectPaymentList" in data:
            self.DirectPaymentList: DirectPaymentList = self._get_value(DirectPaymentList, "DirectPaymentList")
        else:
            self.DirectPaymentList: DirectPaymentList = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "ShipmentItemList" in data:
            self.ShipmentItemList: ShipmentItemList = self._get_value(ShipmentItemList, "ShipmentItemList")
        else:
            self.ShipmentItemList: ShipmentItemList = None
        if "ShipmentItemAdjustmentList" in data:
            self.ShipmentItemAdjustmentList: ShipmentItemList = self._get_value(
                ShipmentItemList, "ShipmentItemAdjustmentList"
            )
        else:
            self.ShipmentItemAdjustmentList: ShipmentItemList = None


class ShipmentItem(__BaseDictObject):
    """
    An item of a shipment, refund, guarantee claim, or chargeback.
    """

    def __init__(self, data):
        super().__init__(data)
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "OrderItemId" in data:
            self.OrderItemId: str = self._get_value(str, "OrderItemId")
        else:
            self.OrderItemId: str = None
        if "OrderAdjustmentItemId" in data:
            self.OrderAdjustmentItemId: str = self._get_value(str, "OrderAdjustmentItemId")
        else:
            self.OrderAdjustmentItemId: str = None
        if "QuantityShipped" in data:
            self.QuantityShipped: int = self._get_value(int, "QuantityShipped")
        else:
            self.QuantityShipped: int = None
        if "ItemChargeList" in data:
            self.ItemChargeList: ChargeComponentList = self._get_value(ChargeComponentList, "ItemChargeList")
        else:
            self.ItemChargeList: ChargeComponentList = None
        if "ItemChargeAdjustmentList" in data:
            self.ItemChargeAdjustmentList: ChargeComponentList = self._get_value(
                ChargeComponentList, "ItemChargeAdjustmentList"
            )
        else:
            self.ItemChargeAdjustmentList: ChargeComponentList = None
        if "ItemFeeList" in data:
            self.ItemFeeList: FeeComponentList = self._get_value(FeeComponentList, "ItemFeeList")
        else:
            self.ItemFeeList: FeeComponentList = None
        if "ItemFeeAdjustmentList" in data:
            self.ItemFeeAdjustmentList: FeeComponentList = self._get_value(FeeComponentList, "ItemFeeAdjustmentList")
        else:
            self.ItemFeeAdjustmentList: FeeComponentList = None
        if "ItemTaxWithheldList" in data:
            self.ItemTaxWithheldList: TaxWithheldComponentList = self._get_value(
                TaxWithheldComponentList, "ItemTaxWithheldList"
            )
        else:
            self.ItemTaxWithheldList: TaxWithheldComponentList = None
        if "PromotionList" in data:
            self.PromotionList: PromotionList = self._get_value(PromotionList, "PromotionList")
        else:
            self.PromotionList: PromotionList = None
        if "PromotionAdjustmentList" in data:
            self.PromotionAdjustmentList: PromotionList = self._get_value(PromotionList, "PromotionAdjustmentList")
        else:
            self.PromotionAdjustmentList: PromotionList = None
        if "CostOfPointsGranted" in data:
            self.CostOfPointsGranted: Currency = self._get_value(Currency, "CostOfPointsGranted")
        else:
            self.CostOfPointsGranted: Currency = None
        if "CostOfPointsReturned" in data:
            self.CostOfPointsReturned: Currency = self._get_value(Currency, "CostOfPointsReturned")
        else:
            self.CostOfPointsReturned: Currency = None


class SolutionProviderCreditEvent(__BaseDictObject):
    """
    A credit given to a solution provider.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ProviderTransactionType" in data:
            self.ProviderTransactionType: str = self._get_value(str, "ProviderTransactionType")
        else:
            self.ProviderTransactionType: str = None
        if "SellerOrderId" in data:
            self.SellerOrderId: str = self._get_value(str, "SellerOrderId")
        else:
            self.SellerOrderId: str = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "MarketplaceCountryCode" in data:
            self.MarketplaceCountryCode: str = self._get_value(str, "MarketplaceCountryCode")
        else:
            self.MarketplaceCountryCode: str = None
        if "SellerId" in data:
            self.SellerId: str = self._get_value(str, "SellerId")
        else:
            self.SellerId: str = None
        if "SellerStoreName" in data:
            self.SellerStoreName: str = self._get_value(str, "SellerStoreName")
        else:
            self.SellerStoreName: str = None
        if "ProviderId" in data:
            self.ProviderId: str = self._get_value(str, "ProviderId")
        else:
            self.ProviderId: str = None
        if "ProviderStoreName" in data:
            self.ProviderStoreName: str = self._get_value(str, "ProviderStoreName")
        else:
            self.ProviderStoreName: str = None
        if "TransactionAmount" in data:
            self.TransactionAmount: Currency = self._get_value(Currency, "TransactionAmount")
        else:
            self.TransactionAmount: Currency = None
        if "TransactionCreationDate" in data:
            self.TransactionCreationDate: Date = self._get_value(Date, "TransactionCreationDate")
        else:
            self.TransactionCreationDate: Date = None


class TaxWithholdingPeriod(__BaseDictObject):
    """
    Period which taxwithholding on seller's account is calculated.
    """

    def __init__(self, data):
        super().__init__(data)
        if "StartDate" in data:
            self.StartDate: Date = self._get_value(Date, "StartDate")
        else:
            self.StartDate: Date = None
        if "EndDate" in data:
            self.EndDate: Date = self._get_value(Date, "EndDate")
        else:
            self.EndDate: Date = None


class TaxWithholdingEvent(__BaseDictObject):
    """
    A TaxWithholding event on seller's account.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "BaseAmount" in data:
            self.BaseAmount: Currency = self._get_value(Currency, "BaseAmount")
        else:
            self.BaseAmount: Currency = None
        if "WithheldAmount" in data:
            self.WithheldAmount: Currency = self._get_value(Currency, "WithheldAmount")
        else:
            self.WithheldAmount: Currency = None
        if "TaxWithholdingPeriod" in data:
            self.TaxWithholdingPeriod: TaxWithholdingPeriod = self._get_value(
                TaxWithholdingPeriod, "TaxWithholdingPeriod"
            )
        else:
            self.TaxWithholdingPeriod: TaxWithholdingPeriod = None


class TaxWithheldComponent(__BaseDictObject):
    """
    Information about the taxes withheld.
    """

    def __init__(self, data):
        super().__init__(data)
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = self._get_value(str, "TaxCollectionModel")
        else:
            self.TaxCollectionModel: str = None
        if "TaxesWithheld" in data:
            self.TaxesWithheld: ChargeComponentList = self._get_value(ChargeComponentList, "TaxesWithheld")
        else:
            self.TaxesWithheld: ChargeComponentList = None


class TrialShipmentEvent(__BaseDictObject):
    """
    An event related to a trial shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "FinancialEventGroupId" in data:
            self.FinancialEventGroupId: str = self._get_value(str, "FinancialEventGroupId")
        else:
            self.FinancialEventGroupId: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = self._get_value(Date, "PostedDate")
        else:
            self.PostedDate: Date = None
        if "SKU" in data:
            self.SKU: str = self._get_value(str, "SKU")
        else:
            self.SKU: str = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = self._get_value(FeeComponentList, "FeeList")
        else:
            self.FeeList: FeeComponentList = None


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class AdjustmentEventList(list, _List["AdjustmentEvent"]):
    """
    A list of adjustment event information for the seller's account.
    """

    def __init__(self, data):
        super().__init__([AdjustmentEvent(datum) for datum in data])
        self.data = data


class AdjustmentItemList(list, _List["AdjustmentItem"]):
    """
    A list of information about items in an adjustment to the seller's account.
    """

    def __init__(self, data):
        super().__init__([AdjustmentItem(datum) for datum in data])
        self.data = data


class AffordabilityExpenseEventList(list, _List["AffordabilityExpenseEvent"]):
    """
    A list of expense information related to an affordability promotion.
    """

    def __init__(self, data):
        super().__init__([AffordabilityExpenseEvent(datum) for datum in data])
        self.data = data


class ChargeComponentList(list, _List["ChargeComponent"]):
    """
    A list of charge information on the seller's account.
    """

    def __init__(self, data):
        super().__init__([ChargeComponent(datum) for datum in data])
        self.data = data


class ChargeInstrumentList(list, _List["ChargeInstrument"]):
    """
    A list of payment instruments.
    """

    def __init__(self, data):
        super().__init__([ChargeInstrument(datum) for datum in data])
        self.data = data


class CouponPaymentEventList(list, _List["CouponPaymentEvent"]):
    """
    A list of coupon payment event information.
    """

    def __init__(self, data):
        super().__init__([CouponPaymentEvent(datum) for datum in data])
        self.data = data


class DebtRecoveryEventList(list, _List["DebtRecoveryEvent"]):
    """
    A list of debt recovery event information.
    """

    def __init__(self, data):
        super().__init__([DebtRecoveryEvent(datum) for datum in data])
        self.data = data


class DebtRecoveryItemList(list, _List["DebtRecoveryItem"]):
    """
    A list of debt recovery item information.
    """

    def __init__(self, data):
        super().__init__([DebtRecoveryItem(datum) for datum in data])
        self.data = data


class DirectPaymentList(list, _List["DirectPayment"]):
    """
    A list of direct payment information.
    """

    def __init__(self, data):
        super().__init__([DirectPayment(datum) for datum in data])
        self.data = data


class FBALiquidationEventList(list, _List["FBALiquidationEvent"]):
    """
    A list of FBA inventory liquidation payment events.
    """

    def __init__(self, data):
        super().__init__([FBALiquidationEvent(datum) for datum in data])
        self.data = data


class FeeComponentList(list, _List["FeeComponent"]):
    """
    A list of fee component information.
    """

    def __init__(self, data):
        super().__init__([FeeComponent(datum) for datum in data])
        self.data = data


class FinancialEventGroupList(list, _List["FinancialEventGroup"]):
    """
    A list of financial event group information.
    """

    def __init__(self, data):
        super().__init__([FinancialEventGroup(datum) for datum in data])
        self.data = data


class ImagingServicesFeeEventList(list, _List["ImagingServicesFeeEvent"]):
    """
    A list of fee events related to Amazon Imaging services.
    """

    def __init__(self, data):
        super().__init__([ImagingServicesFeeEvent(datum) for datum in data])
        self.data = data


class LoanServicingEventList(list, _List["LoanServicingEvent"]):
    """
    A list of loan servicing events.
    """

    def __init__(self, data):
        super().__init__([LoanServicingEvent(datum) for datum in data])
        self.data = data


class NetworkComminglingTransactionEventList(list, _List["NetworkComminglingTransactionEvent"]):
    """
    A list of network commingling transaction events.
    """

    def __init__(self, data):
        super().__init__([NetworkComminglingTransactionEvent(datum) for datum in data])
        self.data = data


class PayWithAmazonEventList(list, _List["PayWithAmazonEvent"]):
    """
    A list of events related to the seller's Pay with Amazon account.
    """

    def __init__(self, data):
        super().__init__([PayWithAmazonEvent(datum) for datum in data])
        self.data = data


class ProductAdsPaymentEventList(list, _List["ProductAdsPaymentEvent"]):
    """
    A list of sponsored products payment events.
    """

    def __init__(self, data):
        super().__init__([ProductAdsPaymentEvent(datum) for datum in data])
        self.data = data


class PromotionList(list, _List["Promotion"]):
    """
    A list of promotions.
    """

    def __init__(self, data):
        super().__init__([Promotion(datum) for datum in data])
        self.data = data


class RemovalShipmentEventList(list, _List["RemovalShipmentEvent"]):
    """
    A list of removal shipment event information.
    """

    def __init__(self, data):
        super().__init__([RemovalShipmentEvent(datum) for datum in data])
        self.data = data


class RemovalShipmentItemList(list, _List["RemovalShipmentItem"]):
    """
    A list of information about removal shipment items.
    """

    def __init__(self, data):
        super().__init__([RemovalShipmentItem(datum) for datum in data])
        self.data = data


class RemovalShipmentAdjustmentEventList(list, _List["RemovalShipmentAdjustmentEvent"]):
    """
    A comma-delimited list of Removal shipmentAdjustment details for FBA inventory.
    """

    def __init__(self, data):
        super().__init__([RemovalShipmentAdjustmentEvent(datum) for datum in data])
        self.data = data


class RentalTransactionEventList(list, _List["RentalTransactionEvent"]):
    """
    A list of rental transaction event information.
    """

    def __init__(self, data):
        super().__init__([RentalTransactionEvent(datum) for datum in data])
        self.data = data


class RetrochargeEventList(list, _List["RetrochargeEvent"]):
    """
    A list of information about Retrocharge or RetrochargeReversal events.
    """

    def __init__(self, data):
        super().__init__([RetrochargeEvent(datum) for datum in data])
        self.data = data


class SAFETReimbursementEventList(list, _List["SAFETReimbursementEvent"]):
    """
    A list of SAFETReimbursementEvents.
    """

    def __init__(self, data):
        super().__init__([SAFETReimbursementEvent(datum) for datum in data])
        self.data = data


class SAFETReimbursementItemList(list, _List["SAFETReimbursementItem"]):
    """
    A list of SAFETReimbursementItems.
    """

    def __init__(self, data):
        super().__init__([SAFETReimbursementItem(datum) for datum in data])
        self.data = data


class SellerDealPaymentEventList(list, _List["SellerDealPaymentEvent"]):
    """
    A list of payment events for deal-related fees.
    """

    def __init__(self, data):
        super().__init__([SellerDealPaymentEvent(datum) for datum in data])
        self.data = data


class SellerReviewEnrollmentPaymentEventList(list, _List["SellerReviewEnrollmentPaymentEvent"]):
    """
    A list of information about fee events for the Early Reviewer Program.
    """

    def __init__(self, data):
        super().__init__([SellerReviewEnrollmentPaymentEvent(datum) for datum in data])
        self.data = data


class ServiceFeeEventList(list, _List["ServiceFeeEvent"]):
    """
    A list of information about service fee events.
    """

    def __init__(self, data):
        super().__init__([ServiceFeeEvent(datum) for datum in data])
        self.data = data


class ShipmentEventList(list, _List["ShipmentEvent"]):
    """
    A list of shipment event information.
    """

    def __init__(self, data):
        super().__init__([ShipmentEvent(datum) for datum in data])
        self.data = data


class ShipmentItemList(list, _List["ShipmentItem"]):
    """
    A list of shipment items.
    """

    def __init__(self, data):
        super().__init__([ShipmentItem(datum) for datum in data])
        self.data = data


class SolutionProviderCreditEventList(list, _List["SolutionProviderCreditEvent"]):
    """
    A list of information about solution provider credits.
    """

    def __init__(self, data):
        super().__init__([SolutionProviderCreditEvent(datum) for datum in data])
        self.data = data


class TaxWithholdingEventList(list, _List["TaxWithholdingEvent"]):
    """
    List of TaxWithholding events.
    """

    def __init__(self, data):
        super().__init__([TaxWithholdingEvent(datum) for datum in data])
        self.data = data


class TaxWithheldComponentList(list, _List["TaxWithheldComponent"]):
    """
    A list of information about taxes withheld.
    """

    def __init__(self, data):
        super().__init__([TaxWithheldComponent(datum) for datum in data])
        self.data = data


class TrialShipmentEventList(list, _List["TrialShipmentEvent"]):
    """
    A list of information about trial shipment financial events.
    """

    def __init__(self, data):
        super().__init__([TrialShipmentEvent(datum) for datum in data])
        self.data = data


class ShipmentSettleEventList(list, _List["ShipmentEvent"]):
    """
    A list of information about shipment settle financial events.
    """

    def __init__(self, data):
        super().__init__([ShipmentEvent(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class BigDecimal(float):
    """ """


class Date(str):
    """ """


class FinancesV0Client(__BaseClient):
    def listFinancialEventGroups(
        self,
        MaxResultsPerPage: int = None,
        FinancialEventGroupStartedBefore: str = None,
        FinancialEventGroupStartedAfter: str = None,
        NextToken: str = None,
    ):
        """
                Returns financial event groups for a given date range.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/finances/v0/financialEventGroups"
        params = {}
        if MaxResultsPerPage is not None:
            params["MaxResultsPerPage"] = MaxResultsPerPage
        if FinancialEventGroupStartedBefore is not None:
            params["FinancialEventGroupStartedBefore"] = FinancialEventGroupStartedBefore
        if FinancialEventGroupStartedAfter is not None:
            params["FinancialEventGroupStartedAfter"] = FinancialEventGroupStartedAfter
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListFinancialEventGroupsResponse,
            400: ListFinancialEventGroupsResponse,
            403: ListFinancialEventGroupsResponse,
            404: ListFinancialEventGroupsResponse,
            429: ListFinancialEventGroupsResponse,
            500: ListFinancialEventGroupsResponse,
            503: ListFinancialEventGroupsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def listFinancialEventsByGroupId(
        self,
        eventGroupId: str,
        MaxResultsPerPage: int = None,
        NextToken: str = None,
    ):
        """
                Returns all financial events for the specified financial event group.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/finances/v0/financialEventGroups/{eventGroupId}/financialEvents"
        params = {}
        if MaxResultsPerPage is not None:
            params["MaxResultsPerPage"] = MaxResultsPerPage
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def listFinancialEventsByOrderId(
        self,
        orderId: str,
        MaxResultsPerPage: int = None,
        NextToken: str = None,
    ):
        """
                Returns all financial events for the specified order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/finances/v0/orders/{orderId}/financialEvents"
        params = {}
        if MaxResultsPerPage is not None:
            params["MaxResultsPerPage"] = MaxResultsPerPage
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def listFinancialEvents(
        self,
        MaxResultsPerPage: int = None,
        PostedAfter: str = None,
        PostedBefore: str = None,
        NextToken: str = None,
    ):
        """
                Returns financial events for the specified data range.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.5 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/finances/v0/financialEvents"
        params = {}
        if MaxResultsPerPage is not None:
            params["MaxResultsPerPage"] = MaxResultsPerPage
        if PostedAfter is not None:
            params["PostedAfter"] = PostedAfter
        if PostedBefore is not None:
            params["PostedBefore"] = PostedBefore
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
