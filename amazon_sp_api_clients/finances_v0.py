from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class AdjustmentEvent:
    """
    An adjustment to the seller's account.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AdjustmentType" in data:
            self.AdjustmentType: str = str(data["AdjustmentType"])
        else:
            self.AdjustmentType: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "AdjustmentAmount" in data:
            self.AdjustmentAmount: Currency = Currency(data["AdjustmentAmount"])
        else:
            self.AdjustmentAmount: Currency = None
        if "AdjustmentItemList" in data:
            self.AdjustmentItemList: AdjustmentItemList = AdjustmentItemList(data["AdjustmentItemList"])
        else:
            self.AdjustmentItemList: AdjustmentItemList = None


class AdjustmentItem:
    """
    An item in an adjustment to the seller's account.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Quantity" in data:
            self.Quantity: str = str(data["Quantity"])
        else:
            self.Quantity: str = None
        if "PerUnitAmount" in data:
            self.PerUnitAmount: Currency = Currency(data["PerUnitAmount"])
        else:
            self.PerUnitAmount: Currency = None
        if "TotalAmount" in data:
            self.TotalAmount: Currency = Currency(data["TotalAmount"])
        else:
            self.TotalAmount: Currency = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "FnSKU" in data:
            self.FnSKU: str = str(data["FnSKU"])
        else:
            self.FnSKU: str = None
        if "ProductDescription" in data:
            self.ProductDescription: str = str(data["ProductDescription"])
        else:
            self.ProductDescription: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None


class AffordabilityExpenseEvent:
    """
    An expense related to an affordability promotion.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "TransactionType" in data:
            self.TransactionType: str = str(data["TransactionType"])
        else:
            self.TransactionType: str = None
        if "BaseExpense" in data:
            self.BaseExpense: Currency = Currency(data["BaseExpense"])
        else:
            self.BaseExpense: Currency = None
        if "TaxTypeCGST" in data:
            self.TaxTypeCGST: Currency = Currency(data["TaxTypeCGST"])
        else:
            self.TaxTypeCGST: Currency = None
        if "TaxTypeSGST" in data:
            self.TaxTypeSGST: Currency = Currency(data["TaxTypeSGST"])
        else:
            self.TaxTypeSGST: Currency = None
        if "TaxTypeIGST" in data:
            self.TaxTypeIGST: Currency = Currency(data["TaxTypeIGST"])
        else:
            self.TaxTypeIGST: Currency = None
        if "TotalExpense" in data:
            self.TotalExpense: Currency = Currency(data["TotalExpense"])
        else:
            self.TotalExpense: Currency = None


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

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ChargeType" in data:
            self.ChargeType: str = str(data["ChargeType"])
        else:
            self.ChargeType: str = None
        if "ChargeAmount" in data:
            self.ChargeAmount: Currency = Currency(data["ChargeAmount"])
        else:
            self.ChargeAmount: Currency = None


class ChargeInstrument:
    """
    A payment instrument.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Description" in data:
            self.Description: str = str(data["Description"])
        else:
            self.Description: str = None
        if "Tail" in data:
            self.Tail: str = str(data["Tail"])
        else:
            self.Tail: str = None
        if "Amount" in data:
            self.Amount: Currency = Currency(data["Amount"])
        else:
            self.Amount: Currency = None


class CouponPaymentEvent:
    """
    An event related to coupon payments.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "CouponId" in data:
            self.CouponId: str = str(data["CouponId"])
        else:
            self.CouponId: str = None
        if "SellerCouponDescription" in data:
            self.SellerCouponDescription: str = str(data["SellerCouponDescription"])
        else:
            self.SellerCouponDescription: str = None
        if "ClipOrRedemptionCount" in data:
            self.ClipOrRedemptionCount: int = int(data["ClipOrRedemptionCount"])
        else:
            self.ClipOrRedemptionCount: int = None
        if "PaymentEventId" in data:
            self.PaymentEventId: str = str(data["PaymentEventId"])
        else:
            self.PaymentEventId: str = None
        if "FeeComponent" in data:
            self.FeeComponent: FeeComponent = FeeComponent(data["FeeComponent"])
        else:
            self.FeeComponent: FeeComponent = None
        if "ChargeComponent" in data:
            self.ChargeComponent: ChargeComponent = ChargeComponent(data["ChargeComponent"])
        else:
            self.ChargeComponent: ChargeComponent = None
        if "TotalAmount" in data:
            self.TotalAmount: Currency = Currency(data["TotalAmount"])
        else:
            self.TotalAmount: Currency = None


class Currency:
    """
    A currency type and amount.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None
        if "CurrencyAmount" in data:
            self.CurrencyAmount: BigDecimal = BigDecimal(data["CurrencyAmount"])
        else:
            self.CurrencyAmount: BigDecimal = None


class DebtRecoveryEvent:
    """
    A debt payment or debt adjustment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DebtRecoveryType" in data:
            self.DebtRecoveryType: str = str(data["DebtRecoveryType"])
        else:
            self.DebtRecoveryType: str = None
        if "RecoveryAmount" in data:
            self.RecoveryAmount: Currency = Currency(data["RecoveryAmount"])
        else:
            self.RecoveryAmount: Currency = None
        if "OverPaymentCredit" in data:
            self.OverPaymentCredit: Currency = Currency(data["OverPaymentCredit"])
        else:
            self.OverPaymentCredit: Currency = None
        if "DebtRecoveryItemList" in data:
            self.DebtRecoveryItemList: DebtRecoveryItemList = DebtRecoveryItemList(data["DebtRecoveryItemList"])
        else:
            self.DebtRecoveryItemList: DebtRecoveryItemList = None
        if "ChargeInstrumentList" in data:
            self.ChargeInstrumentList: ChargeInstrumentList = ChargeInstrumentList(data["ChargeInstrumentList"])
        else:
            self.ChargeInstrumentList: ChargeInstrumentList = None


class DebtRecoveryItem:
    """
    An item of a debt payment or debt adjustment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "RecoveryAmount" in data:
            self.RecoveryAmount: Currency = Currency(data["RecoveryAmount"])
        else:
            self.RecoveryAmount: Currency = None
        if "OriginalAmount" in data:
            self.OriginalAmount: Currency = Currency(data["OriginalAmount"])
        else:
            self.OriginalAmount: Currency = None
        if "GroupBeginDate" in data:
            self.GroupBeginDate: Date = Date(data["GroupBeginDate"])
        else:
            self.GroupBeginDate: Date = None
        if "GroupEndDate" in data:
            self.GroupEndDate: Date = Date(data["GroupEndDate"])
        else:
            self.GroupEndDate: Date = None


class DirectPayment:
    """
    A payment made directly to a seller.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DirectPaymentType" in data:
            self.DirectPaymentType: str = str(data["DirectPaymentType"])
        else:
            self.DirectPaymentType: str = None
        if "DirectPaymentAmount" in data:
            self.DirectPaymentAmount: Currency = Currency(data["DirectPaymentAmount"])
        else:
            self.DirectPaymentAmount: Currency = None


class FBALiquidationEvent:
    """
    A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US marketplace.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "OriginalRemovalOrderId" in data:
            self.OriginalRemovalOrderId: str = str(data["OriginalRemovalOrderId"])
        else:
            self.OriginalRemovalOrderId: str = None
        if "LiquidationProceedsAmount" in data:
            self.LiquidationProceedsAmount: Currency = Currency(data["LiquidationProceedsAmount"])
        else:
            self.LiquidationProceedsAmount: Currency = None
        if "LiquidationFeeAmount" in data:
            self.LiquidationFeeAmount: Currency = Currency(data["LiquidationFeeAmount"])
        else:
            self.LiquidationFeeAmount: Currency = None


class FeeComponent:
    """
    A fee associated with the event.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "FeeType" in data:
            self.FeeType: str = str(data["FeeType"])
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: Currency = Currency(data["FeeAmount"])
        else:
            self.FeeAmount: Currency = None


class FinancialEventGroup:
    """
    Information related to a financial event group.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "FinancialEventGroupId" in data:
            self.FinancialEventGroupId: str = str(data["FinancialEventGroupId"])
        else:
            self.FinancialEventGroupId: str = None
        if "ProcessingStatus" in data:
            self.ProcessingStatus: str = str(data["ProcessingStatus"])
        else:
            self.ProcessingStatus: str = None
        if "FundTransferStatus" in data:
            self.FundTransferStatus: str = str(data["FundTransferStatus"])
        else:
            self.FundTransferStatus: str = None
        if "OriginalTotal" in data:
            self.OriginalTotal: Currency = Currency(data["OriginalTotal"])
        else:
            self.OriginalTotal: Currency = None
        if "ConvertedTotal" in data:
            self.ConvertedTotal: Currency = Currency(data["ConvertedTotal"])
        else:
            self.ConvertedTotal: Currency = None
        if "FundTransferDate" in data:
            self.FundTransferDate: Date = Date(data["FundTransferDate"])
        else:
            self.FundTransferDate: Date = None
        if "TraceId" in data:
            self.TraceId: str = str(data["TraceId"])
        else:
            self.TraceId: str = None
        if "AccountTail" in data:
            self.AccountTail: str = str(data["AccountTail"])
        else:
            self.AccountTail: str = None
        if "BeginningBalance" in data:
            self.BeginningBalance: Currency = Currency(data["BeginningBalance"])
        else:
            self.BeginningBalance: Currency = None
        if "FinancialEventGroupStart" in data:
            self.FinancialEventGroupStart: Date = Date(data["FinancialEventGroupStart"])
        else:
            self.FinancialEventGroupStart: Date = None
        if "FinancialEventGroupEnd" in data:
            self.FinancialEventGroupEnd: Date = Date(data["FinancialEventGroupEnd"])
        else:
            self.FinancialEventGroupEnd: Date = None


class FinancialEvents:
    """
    Contains all information related to a financial event.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentEventList" in data:
            self.ShipmentEventList: ShipmentEventList = ShipmentEventList(data["ShipmentEventList"])
        else:
            self.ShipmentEventList: ShipmentEventList = None
        if "RefundEventList" in data:
            self.RefundEventList: ShipmentEventList = ShipmentEventList(data["RefundEventList"])
        else:
            self.RefundEventList: ShipmentEventList = None
        if "GuaranteeClaimEventList" in data:
            self.GuaranteeClaimEventList: ShipmentEventList = ShipmentEventList(data["GuaranteeClaimEventList"])
        else:
            self.GuaranteeClaimEventList: ShipmentEventList = None
        if "ChargebackEventList" in data:
            self.ChargebackEventList: ShipmentEventList = ShipmentEventList(data["ChargebackEventList"])
        else:
            self.ChargebackEventList: ShipmentEventList = None
        if "PayWithAmazonEventList" in data:
            self.PayWithAmazonEventList: PayWithAmazonEventList = PayWithAmazonEventList(data["PayWithAmazonEventList"])
        else:
            self.PayWithAmazonEventList: PayWithAmazonEventList = None
        if "ServiceProviderCreditEventList" in data:
            self.ServiceProviderCreditEventList: SolutionProviderCreditEventList = SolutionProviderCreditEventList(
                data["ServiceProviderCreditEventList"]
            )
        else:
            self.ServiceProviderCreditEventList: SolutionProviderCreditEventList = None
        if "RetrochargeEventList" in data:
            self.RetrochargeEventList: RetrochargeEventList = RetrochargeEventList(data["RetrochargeEventList"])
        else:
            self.RetrochargeEventList: RetrochargeEventList = None
        if "RentalTransactionEventList" in data:
            self.RentalTransactionEventList: RentalTransactionEventList = RentalTransactionEventList(
                data["RentalTransactionEventList"]
            )
        else:
            self.RentalTransactionEventList: RentalTransactionEventList = None
        if "ProductAdsPaymentEventList" in data:
            self.ProductAdsPaymentEventList: ProductAdsPaymentEventList = ProductAdsPaymentEventList(
                data["ProductAdsPaymentEventList"]
            )
        else:
            self.ProductAdsPaymentEventList: ProductAdsPaymentEventList = None
        if "ServiceFeeEventList" in data:
            self.ServiceFeeEventList: ServiceFeeEventList = ServiceFeeEventList(data["ServiceFeeEventList"])
        else:
            self.ServiceFeeEventList: ServiceFeeEventList = None
        if "SellerDealPaymentEventList" in data:
            self.SellerDealPaymentEventList: SellerDealPaymentEventList = SellerDealPaymentEventList(
                data["SellerDealPaymentEventList"]
            )
        else:
            self.SellerDealPaymentEventList: SellerDealPaymentEventList = None
        if "DebtRecoveryEventList" in data:
            self.DebtRecoveryEventList: DebtRecoveryEventList = DebtRecoveryEventList(data["DebtRecoveryEventList"])
        else:
            self.DebtRecoveryEventList: DebtRecoveryEventList = None
        if "LoanServicingEventList" in data:
            self.LoanServicingEventList: LoanServicingEventList = LoanServicingEventList(data["LoanServicingEventList"])
        else:
            self.LoanServicingEventList: LoanServicingEventList = None
        if "AdjustmentEventList" in data:
            self.AdjustmentEventList: AdjustmentEventList = AdjustmentEventList(data["AdjustmentEventList"])
        else:
            self.AdjustmentEventList: AdjustmentEventList = None
        if "SAFETReimbursementEventList" in data:
            self.SAFETReimbursementEventList: SAFETReimbursementEventList = SAFETReimbursementEventList(
                data["SAFETReimbursementEventList"]
            )
        else:
            self.SAFETReimbursementEventList: SAFETReimbursementEventList = None
        if "SellerReviewEnrollmentPaymentEventList" in data:
            self.SellerReviewEnrollmentPaymentEventList: SellerReviewEnrollmentPaymentEventList = (
                SellerReviewEnrollmentPaymentEventList(data["SellerReviewEnrollmentPaymentEventList"])
            )
        else:
            self.SellerReviewEnrollmentPaymentEventList: SellerReviewEnrollmentPaymentEventList = None
        if "FBALiquidationEventList" in data:
            self.FBALiquidationEventList: FBALiquidationEventList = FBALiquidationEventList(
                data["FBALiquidationEventList"]
            )
        else:
            self.FBALiquidationEventList: FBALiquidationEventList = None
        if "CouponPaymentEventList" in data:
            self.CouponPaymentEventList: CouponPaymentEventList = CouponPaymentEventList(data["CouponPaymentEventList"])
        else:
            self.CouponPaymentEventList: CouponPaymentEventList = None
        if "ImagingServicesFeeEventList" in data:
            self.ImagingServicesFeeEventList: ImagingServicesFeeEventList = ImagingServicesFeeEventList(
                data["ImagingServicesFeeEventList"]
            )
        else:
            self.ImagingServicesFeeEventList: ImagingServicesFeeEventList = None
        if "NetworkComminglingTransactionEventList" in data:
            self.NetworkComminglingTransactionEventList: NetworkComminglingTransactionEventList = (
                NetworkComminglingTransactionEventList(data["NetworkComminglingTransactionEventList"])
            )
        else:
            self.NetworkComminglingTransactionEventList: NetworkComminglingTransactionEventList = None
        if "AffordabilityExpenseEventList" in data:
            self.AffordabilityExpenseEventList: AffordabilityExpenseEventList = AffordabilityExpenseEventList(
                data["AffordabilityExpenseEventList"]
            )
        else:
            self.AffordabilityExpenseEventList: AffordabilityExpenseEventList = None
        if "AffordabilityExpenseReversalEventList" in data:
            self.AffordabilityExpenseReversalEventList: AffordabilityExpenseEventList = AffordabilityExpenseEventList(
                data["AffordabilityExpenseReversalEventList"]
            )
        else:
            self.AffordabilityExpenseReversalEventList: AffordabilityExpenseEventList = None
        if "TrialShipmentEventList" in data:
            self.TrialShipmentEventList: TrialShipmentEventList = TrialShipmentEventList(data["TrialShipmentEventList"])
        else:
            self.TrialShipmentEventList: TrialShipmentEventList = None
        if "ShipmentSettleEventList" in data:
            self.ShipmentSettleEventList: ShipmentSettleEventList = ShipmentSettleEventList(
                data["ShipmentSettleEventList"]
            )
        else:
            self.ShipmentSettleEventList: ShipmentSettleEventList = None
        if "TaxWithholdingEventList" in data:
            self.TaxWithholdingEventList: TaxWithholdingEventList = TaxWithholdingEventList(
                data["TaxWithholdingEventList"]
            )
        else:
            self.TaxWithholdingEventList: TaxWithholdingEventList = None
        if "RemovalShipmentEventList" in data:
            self.RemovalShipmentEventList: RemovalShipmentEventList = RemovalShipmentEventList(
                data["RemovalShipmentEventList"]
            )
        else:
            self.RemovalShipmentEventList: RemovalShipmentEventList = None
        if "RemovalShipmentAdjustmentEventList" in data:
            self.RemovalShipmentAdjustmentEventList: RemovalShipmentAdjustmentEventList = (
                RemovalShipmentAdjustmentEventList(data["RemovalShipmentAdjustmentEventList"])
            )
        else:
            self.RemovalShipmentAdjustmentEventList: RemovalShipmentAdjustmentEventList = None


class ImagingServicesFeeEvent:
    """
    A fee event related to Amazon Imaging services.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ImagingRequestBillingItemID" in data:
            self.ImagingRequestBillingItemID: str = str(data["ImagingRequestBillingItemID"])
        else:
            self.ImagingRequestBillingItemID: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = FeeComponentList(data["FeeList"])
        else:
            self.FeeList: FeeComponentList = None


class ListFinancialEventGroupsPayload:
    """
    The payload for the listFinancialEventGroups operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "NextToken" in data:
            self.NextToken: str = str(data["NextToken"])
        else:
            self.NextToken: str = None
        if "FinancialEventGroupList" in data:
            self.FinancialEventGroupList: FinancialEventGroupList = FinancialEventGroupList(
                data["FinancialEventGroupList"]
            )
        else:
            self.FinancialEventGroupList: FinancialEventGroupList = None


class ListFinancialEventGroupsResponse:
    """
    The response schema for the listFinancialEventGroups operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ListFinancialEventGroupsPayload = ListFinancialEventGroupsPayload(data["payload"])
        else:
            self.payload: ListFinancialEventGroupsPayload = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ListFinancialEventsPayload:
    """
    The payload for the listFinancialEvents operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "NextToken" in data:
            self.NextToken: str = str(data["NextToken"])
        else:
            self.NextToken: str = None
        if "FinancialEvents" in data:
            self.FinancialEvents: FinancialEvents = FinancialEvents(data["FinancialEvents"])
        else:
            self.FinancialEvents: FinancialEvents = None


class ListFinancialEventsResponse:
    """
    The response schema for the listFinancialEvents operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ListFinancialEventsPayload = ListFinancialEventsPayload(data["payload"])
        else:
            self.payload: ListFinancialEventsPayload = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class LoanServicingEvent:
    """
    A loan advance, loan payment, or loan refund.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "LoanAmount" in data:
            self.LoanAmount: Currency = Currency(data["LoanAmount"])
        else:
            self.LoanAmount: Currency = None
        if "SourceBusinessEventType" in data:
            self.SourceBusinessEventType: str = str(data["SourceBusinessEventType"])
        else:
            self.SourceBusinessEventType: str = None


class NetworkComminglingTransactionEvent:
    """
    A network commingling transaction event.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransactionType" in data:
            self.TransactionType: str = str(data["TransactionType"])
        else:
            self.TransactionType: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "NetCoTransactionID" in data:
            self.NetCoTransactionID: str = str(data["NetCoTransactionID"])
        else:
            self.NetCoTransactionID: str = None
        if "SwapReason" in data:
            self.SwapReason: str = str(data["SwapReason"])
        else:
            self.SwapReason: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "TaxExclusiveAmount" in data:
            self.TaxExclusiveAmount: Currency = Currency(data["TaxExclusiveAmount"])
        else:
            self.TaxExclusiveAmount: Currency = None
        if "TaxAmount" in data:
            self.TaxAmount: Currency = Currency(data["TaxAmount"])
        else:
            self.TaxAmount: Currency = None


class PayWithAmazonEvent:
    """
    An event related to the seller's Pay with Amazon account.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerOrderId" in data:
            self.SellerOrderId: str = str(data["SellerOrderId"])
        else:
            self.SellerOrderId: str = None
        if "TransactionPostedDate" in data:
            self.TransactionPostedDate: Date = Date(data["TransactionPostedDate"])
        else:
            self.TransactionPostedDate: Date = None
        if "BusinessObjectType" in data:
            self.BusinessObjectType: str = str(data["BusinessObjectType"])
        else:
            self.BusinessObjectType: str = None
        if "SalesChannel" in data:
            self.SalesChannel: str = str(data["SalesChannel"])
        else:
            self.SalesChannel: str = None
        if "Charge" in data:
            self.Charge: ChargeComponent = ChargeComponent(data["Charge"])
        else:
            self.Charge: ChargeComponent = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = FeeComponentList(data["FeeList"])
        else:
            self.FeeList: FeeComponentList = None
        if "PaymentAmountType" in data:
            self.PaymentAmountType: str = str(data["PaymentAmountType"])
        else:
            self.PaymentAmountType: str = None
        if "AmountDescription" in data:
            self.AmountDescription: str = str(data["AmountDescription"])
        else:
            self.AmountDescription: str = None
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = str(data["FulfillmentChannel"])
        else:
            self.FulfillmentChannel: str = None
        if "StoreName" in data:
            self.StoreName: str = str(data["StoreName"])
        else:
            self.StoreName: str = None


class ProductAdsPaymentEvent:
    """
    A Sponsored Products payment event.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "postedDate" in data:
            self.postedDate: Date = Date(data["postedDate"])
        else:
            self.postedDate: Date = None
        if "transactionType" in data:
            self.transactionType: str = str(data["transactionType"])
        else:
            self.transactionType: str = None
        if "invoiceId" in data:
            self.invoiceId: str = str(data["invoiceId"])
        else:
            self.invoiceId: str = None
        if "baseValue" in data:
            self.baseValue: Currency = Currency(data["baseValue"])
        else:
            self.baseValue: Currency = None
        if "taxValue" in data:
            self.taxValue: Currency = Currency(data["taxValue"])
        else:
            self.taxValue: Currency = None
        if "transactionValue" in data:
            self.transactionValue: Currency = Currency(data["transactionValue"])
        else:
            self.transactionValue: Currency = None


class Promotion:
    """
    A promotion applied to an item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PromotionType" in data:
            self.PromotionType: str = str(data["PromotionType"])
        else:
            self.PromotionType: str = None
        if "PromotionId" in data:
            self.PromotionId: str = str(data["PromotionId"])
        else:
            self.PromotionId: str = None
        if "PromotionAmount" in data:
            self.PromotionAmount: Currency = Currency(data["PromotionAmount"])
        else:
            self.PromotionAmount: Currency = None


class RemovalShipmentEvent:
    """
    A removal shipment event for a removal order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "MerchantOrderId" in data:
            self.MerchantOrderId: str = str(data["MerchantOrderId"])
        else:
            self.MerchantOrderId: str = None
        if "OrderId" in data:
            self.OrderId: str = str(data["OrderId"])
        else:
            self.OrderId: str = None
        if "TransactionType" in data:
            self.TransactionType: str = str(data["TransactionType"])
        else:
            self.TransactionType: str = None
        if "RemovalShipmentItemList" in data:
            self.RemovalShipmentItemList: RemovalShipmentItemList = RemovalShipmentItemList(
                data["RemovalShipmentItemList"]
            )
        else:
            self.RemovalShipmentItemList: RemovalShipmentItemList = None


class RemovalShipmentItem:
    """
    Item-level information for a removal shipment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "RemovalShipmentItemId" in data:
            self.RemovalShipmentItemId: str = str(data["RemovalShipmentItemId"])
        else:
            self.RemovalShipmentItemId: str = None
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = str(data["TaxCollectionModel"])
        else:
            self.TaxCollectionModel: str = None
        if "FulfillmentNetworkSKU" in data:
            self.FulfillmentNetworkSKU: str = str(data["FulfillmentNetworkSKU"])
        else:
            self.FulfillmentNetworkSKU: str = None
        if "Quantity" in data:
            self.Quantity: int = int(data["Quantity"])
        else:
            self.Quantity: int = None
        if "Revenue" in data:
            self.Revenue: Currency = Currency(data["Revenue"])
        else:
            self.Revenue: Currency = None
        if "FeeAmount" in data:
            self.FeeAmount: Currency = Currency(data["FeeAmount"])
        else:
            self.FeeAmount: Currency = None
        if "TaxAmount" in data:
            self.TaxAmount: Currency = Currency(data["TaxAmount"])
        else:
            self.TaxAmount: Currency = None
        if "TaxWithheld" in data:
            self.TaxWithheld: Currency = Currency(data["TaxWithheld"])
        else:
            self.TaxWithheld: Currency = None


class RemovalShipmentAdjustmentEvent:
    """
        A financial adjustment event for FBA liquidated inventory.
    Possible adjustment:
    * Positive values - Buyer needs to pay more amount to Amazon. E.g. charge was wrongly calculated 0$ instead of 100$ due to system error.
    * Negative Values - Buyer get refund. E.g. Buyer receives less items or damaged items and as part of their adjustment buyer gets refund.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "AdjustmentEventId" in data:
            self.AdjustmentEventId: str = str(data["AdjustmentEventId"])
        else:
            self.AdjustmentEventId: str = None
        if "MerchantOrderId" in data:
            self.MerchantOrderId: str = str(data["MerchantOrderId"])
        else:
            self.MerchantOrderId: str = None
        if "OrderId" in data:
            self.OrderId: str = str(data["OrderId"])
        else:
            self.OrderId: str = None
        if "TransactionType" in data:
            self.TransactionType: str = str(data["TransactionType"])
        else:
            self.TransactionType: str = None
        if "RemovalShipmentItemAdjustmentList" in data:
            self.RemovalShipmentItemAdjustmentList: _List[RemovalShipmentItemAdjustment] = [
                RemovalShipmentItemAdjustment(datum) for datum in data["RemovalShipmentItemAdjustmentList"]
            ]
        else:
            self.RemovalShipmentItemAdjustmentList: _List[RemovalShipmentItemAdjustment] = []


class RemovalShipmentItemAdjustment:
    """
    Item-level information for a removal shipment item adjustment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "RemovalShipmentItemId" in data:
            self.RemovalShipmentItemId: str = str(data["RemovalShipmentItemId"])
        else:
            self.RemovalShipmentItemId: str = None
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = str(data["TaxCollectionModel"])
        else:
            self.TaxCollectionModel: str = None
        if "FulfillmentNetworkSKU" in data:
            self.FulfillmentNetworkSKU: str = str(data["FulfillmentNetworkSKU"])
        else:
            self.FulfillmentNetworkSKU: str = None
        if "AdjustedQuantity" in data:
            self.AdjustedQuantity: int = int(data["AdjustedQuantity"])
        else:
            self.AdjustedQuantity: int = None
        if "RevenueAdjustment" in data:
            self.RevenueAdjustment: Currency = Currency(data["RevenueAdjustment"])
        else:
            self.RevenueAdjustment: Currency = None
        if "TaxAmountAdjustment" in data:
            self.TaxAmountAdjustment: Currency = Currency(data["TaxAmountAdjustment"])
        else:
            self.TaxAmountAdjustment: Currency = None
        if "TaxWithheldAdjustment" in data:
            self.TaxWithheldAdjustment: Currency = Currency(data["TaxWithheldAdjustment"])
        else:
            self.TaxWithheldAdjustment: Currency = None


class RentalTransactionEvent:
    """
    An event related to a rental transaction.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "RentalEventType" in data:
            self.RentalEventType: str = str(data["RentalEventType"])
        else:
            self.RentalEventType: str = None
        if "ExtensionLength" in data:
            self.ExtensionLength: int = int(data["ExtensionLength"])
        else:
            self.ExtensionLength: int = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "RentalChargeList" in data:
            self.RentalChargeList: ChargeComponentList = ChargeComponentList(data["RentalChargeList"])
        else:
            self.RentalChargeList: ChargeComponentList = None
        if "RentalFeeList" in data:
            self.RentalFeeList: FeeComponentList = FeeComponentList(data["RentalFeeList"])
        else:
            self.RentalFeeList: FeeComponentList = None
        if "MarketplaceName" in data:
            self.MarketplaceName: str = str(data["MarketplaceName"])
        else:
            self.MarketplaceName: str = None
        if "RentalInitialValue" in data:
            self.RentalInitialValue: Currency = Currency(data["RentalInitialValue"])
        else:
            self.RentalInitialValue: Currency = None
        if "RentalReimbursement" in data:
            self.RentalReimbursement: Currency = Currency(data["RentalReimbursement"])
        else:
            self.RentalReimbursement: Currency = None
        if "RentalTaxWithheldList" in data:
            self.RentalTaxWithheldList: TaxWithheldComponentList = TaxWithheldComponentList(
                data["RentalTaxWithheldList"]
            )
        else:
            self.RentalTaxWithheldList: TaxWithheldComponentList = None


class RetrochargeEvent:
    """
    A retrocharge or retrocharge reversal.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "RetrochargeEventType" in data:
            self.RetrochargeEventType: str = str(data["RetrochargeEventType"])
        else:
            self.RetrochargeEventType: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "BaseTax" in data:
            self.BaseTax: Currency = Currency(data["BaseTax"])
        else:
            self.BaseTax: Currency = None
        if "ShippingTax" in data:
            self.ShippingTax: Currency = Currency(data["ShippingTax"])
        else:
            self.ShippingTax: Currency = None
        if "MarketplaceName" in data:
            self.MarketplaceName: str = str(data["MarketplaceName"])
        else:
            self.MarketplaceName: str = None
        if "RetrochargeTaxWithheldList" in data:
            self.RetrochargeTaxWithheldList: TaxWithheldComponentList = TaxWithheldComponentList(
                data["RetrochargeTaxWithheldList"]
            )
        else:
            self.RetrochargeTaxWithheldList: TaxWithheldComponentList = None


class SAFETReimbursementEvent:
    """
    A SAFE-T claim reimbursement on the seller's account.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "SAFETClaimId" in data:
            self.SAFETClaimId: str = str(data["SAFETClaimId"])
        else:
            self.SAFETClaimId: str = None
        if "ReimbursedAmount" in data:
            self.ReimbursedAmount: Currency = Currency(data["ReimbursedAmount"])
        else:
            self.ReimbursedAmount: Currency = None
        if "ReasonCode" in data:
            self.ReasonCode: str = str(data["ReasonCode"])
        else:
            self.ReasonCode: str = None
        if "SAFETReimbursementItemList" in data:
            self.SAFETReimbursementItemList: SAFETReimbursementItemList = SAFETReimbursementItemList(
                data["SAFETReimbursementItemList"]
            )
        else:
            self.SAFETReimbursementItemList: SAFETReimbursementItemList = None


class SAFETReimbursementItem:
    """
    An item from a SAFE-T claim reimbursement.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemChargeList" in data:
            self.itemChargeList: ChargeComponentList = ChargeComponentList(data["itemChargeList"])
        else:
            self.itemChargeList: ChargeComponentList = None
        if "productDescription" in data:
            self.productDescription: str = str(data["productDescription"])
        else:
            self.productDescription: str = None
        if "quantity" in data:
            self.quantity: str = str(data["quantity"])
        else:
            self.quantity: str = None


class SellerDealPaymentEvent:
    """
    An event linked to the payment of a fee related to the specified deal.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "postedDate" in data:
            self.postedDate: Date = Date(data["postedDate"])
        else:
            self.postedDate: Date = None
        if "dealId" in data:
            self.dealId: str = str(data["dealId"])
        else:
            self.dealId: str = None
        if "dealDescription" in data:
            self.dealDescription: str = str(data["dealDescription"])
        else:
            self.dealDescription: str = None
        if "eventType" in data:
            self.eventType: str = str(data["eventType"])
        else:
            self.eventType: str = None
        if "feeType" in data:
            self.feeType: str = str(data["feeType"])
        else:
            self.feeType: str = None
        if "feeAmount" in data:
            self.feeAmount: Currency = Currency(data["feeAmount"])
        else:
            self.feeAmount: Currency = None
        if "taxAmount" in data:
            self.taxAmount: Currency = Currency(data["taxAmount"])
        else:
            self.taxAmount: Currency = None
        if "totalAmount" in data:
            self.totalAmount: Currency = Currency(data["totalAmount"])
        else:
            self.totalAmount: Currency = None


class SellerReviewEnrollmentPaymentEvent:
    """
    A fee payment event for the Early Reviewer Program.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "EnrollmentId" in data:
            self.EnrollmentId: str = str(data["EnrollmentId"])
        else:
            self.EnrollmentId: str = None
        if "ParentASIN" in data:
            self.ParentASIN: str = str(data["ParentASIN"])
        else:
            self.ParentASIN: str = None
        if "FeeComponent" in data:
            self.FeeComponent: FeeComponent = FeeComponent(data["FeeComponent"])
        else:
            self.FeeComponent: FeeComponent = None
        if "ChargeComponent" in data:
            self.ChargeComponent: ChargeComponent = ChargeComponent(data["ChargeComponent"])
        else:
            self.ChargeComponent: ChargeComponent = None
        if "TotalAmount" in data:
            self.TotalAmount: Currency = Currency(data["TotalAmount"])
        else:
            self.TotalAmount: Currency = None


class ServiceFeeEvent:
    """
    A service fee on the seller's account.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "FeeReason" in data:
            self.FeeReason: str = str(data["FeeReason"])
        else:
            self.FeeReason: str = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = FeeComponentList(data["FeeList"])
        else:
            self.FeeList: FeeComponentList = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "FnSKU" in data:
            self.FnSKU: str = str(data["FnSKU"])
        else:
            self.FnSKU: str = None
        if "FeeDescription" in data:
            self.FeeDescription: str = str(data["FeeDescription"])
        else:
            self.FeeDescription: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None


class ShipmentEvent:
    """
    A shipment, refund, guarantee claim, or chargeback.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "SellerOrderId" in data:
            self.SellerOrderId: str = str(data["SellerOrderId"])
        else:
            self.SellerOrderId: str = None
        if "MarketplaceName" in data:
            self.MarketplaceName: str = str(data["MarketplaceName"])
        else:
            self.MarketplaceName: str = None
        if "OrderChargeList" in data:
            self.OrderChargeList: ChargeComponentList = ChargeComponentList(data["OrderChargeList"])
        else:
            self.OrderChargeList: ChargeComponentList = None
        if "OrderChargeAdjustmentList" in data:
            self.OrderChargeAdjustmentList: ChargeComponentList = ChargeComponentList(data["OrderChargeAdjustmentList"])
        else:
            self.OrderChargeAdjustmentList: ChargeComponentList = None
        if "ShipmentFeeList" in data:
            self.ShipmentFeeList: FeeComponentList = FeeComponentList(data["ShipmentFeeList"])
        else:
            self.ShipmentFeeList: FeeComponentList = None
        if "ShipmentFeeAdjustmentList" in data:
            self.ShipmentFeeAdjustmentList: FeeComponentList = FeeComponentList(data["ShipmentFeeAdjustmentList"])
        else:
            self.ShipmentFeeAdjustmentList: FeeComponentList = None
        if "OrderFeeList" in data:
            self.OrderFeeList: FeeComponentList = FeeComponentList(data["OrderFeeList"])
        else:
            self.OrderFeeList: FeeComponentList = None
        if "OrderFeeAdjustmentList" in data:
            self.OrderFeeAdjustmentList: FeeComponentList = FeeComponentList(data["OrderFeeAdjustmentList"])
        else:
            self.OrderFeeAdjustmentList: FeeComponentList = None
        if "DirectPaymentList" in data:
            self.DirectPaymentList: DirectPaymentList = DirectPaymentList(data["DirectPaymentList"])
        else:
            self.DirectPaymentList: DirectPaymentList = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "ShipmentItemList" in data:
            self.ShipmentItemList: ShipmentItemList = ShipmentItemList(data["ShipmentItemList"])
        else:
            self.ShipmentItemList: ShipmentItemList = None
        if "ShipmentItemAdjustmentList" in data:
            self.ShipmentItemAdjustmentList: ShipmentItemList = ShipmentItemList(data["ShipmentItemAdjustmentList"])
        else:
            self.ShipmentItemAdjustmentList: ShipmentItemList = None


class ShipmentItem:
    """
    An item of a shipment, refund, guarantee claim, or chargeback.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "OrderItemId" in data:
            self.OrderItemId: str = str(data["OrderItemId"])
        else:
            self.OrderItemId: str = None
        if "OrderAdjustmentItemId" in data:
            self.OrderAdjustmentItemId: str = str(data["OrderAdjustmentItemId"])
        else:
            self.OrderAdjustmentItemId: str = None
        if "QuantityShipped" in data:
            self.QuantityShipped: int = int(data["QuantityShipped"])
        else:
            self.QuantityShipped: int = None
        if "ItemChargeList" in data:
            self.ItemChargeList: ChargeComponentList = ChargeComponentList(data["ItemChargeList"])
        else:
            self.ItemChargeList: ChargeComponentList = None
        if "ItemChargeAdjustmentList" in data:
            self.ItemChargeAdjustmentList: ChargeComponentList = ChargeComponentList(data["ItemChargeAdjustmentList"])
        else:
            self.ItemChargeAdjustmentList: ChargeComponentList = None
        if "ItemFeeList" in data:
            self.ItemFeeList: FeeComponentList = FeeComponentList(data["ItemFeeList"])
        else:
            self.ItemFeeList: FeeComponentList = None
        if "ItemFeeAdjustmentList" in data:
            self.ItemFeeAdjustmentList: FeeComponentList = FeeComponentList(data["ItemFeeAdjustmentList"])
        else:
            self.ItemFeeAdjustmentList: FeeComponentList = None
        if "ItemTaxWithheldList" in data:
            self.ItemTaxWithheldList: TaxWithheldComponentList = TaxWithheldComponentList(data["ItemTaxWithheldList"])
        else:
            self.ItemTaxWithheldList: TaxWithheldComponentList = None
        if "PromotionList" in data:
            self.PromotionList: PromotionList = PromotionList(data["PromotionList"])
        else:
            self.PromotionList: PromotionList = None
        if "PromotionAdjustmentList" in data:
            self.PromotionAdjustmentList: PromotionList = PromotionList(data["PromotionAdjustmentList"])
        else:
            self.PromotionAdjustmentList: PromotionList = None
        if "CostOfPointsGranted" in data:
            self.CostOfPointsGranted: Currency = Currency(data["CostOfPointsGranted"])
        else:
            self.CostOfPointsGranted: Currency = None
        if "CostOfPointsReturned" in data:
            self.CostOfPointsReturned: Currency = Currency(data["CostOfPointsReturned"])
        else:
            self.CostOfPointsReturned: Currency = None


class SolutionProviderCreditEvent:
    """
    A credit given to a solution provider.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ProviderTransactionType" in data:
            self.ProviderTransactionType: str = str(data["ProviderTransactionType"])
        else:
            self.ProviderTransactionType: str = None
        if "SellerOrderId" in data:
            self.SellerOrderId: str = str(data["SellerOrderId"])
        else:
            self.SellerOrderId: str = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "MarketplaceCountryCode" in data:
            self.MarketplaceCountryCode: str = str(data["MarketplaceCountryCode"])
        else:
            self.MarketplaceCountryCode: str = None
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "SellerStoreName" in data:
            self.SellerStoreName: str = str(data["SellerStoreName"])
        else:
            self.SellerStoreName: str = None
        if "ProviderId" in data:
            self.ProviderId: str = str(data["ProviderId"])
        else:
            self.ProviderId: str = None
        if "ProviderStoreName" in data:
            self.ProviderStoreName: str = str(data["ProviderStoreName"])
        else:
            self.ProviderStoreName: str = None
        if "TransactionAmount" in data:
            self.TransactionAmount: Currency = Currency(data["TransactionAmount"])
        else:
            self.TransactionAmount: Currency = None
        if "TransactionCreationDate" in data:
            self.TransactionCreationDate: Date = Date(data["TransactionCreationDate"])
        else:
            self.TransactionCreationDate: Date = None


class TaxWithholdingPeriod:
    """
    Period which taxwithholding on seller's account is calculated.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "StartDate" in data:
            self.StartDate: Date = Date(data["StartDate"])
        else:
            self.StartDate: Date = None
        if "EndDate" in data:
            self.EndDate: Date = Date(data["EndDate"])
        else:
            self.EndDate: Date = None


class TaxWithholdingEvent:
    """
    A TaxWithholding event on seller's account.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "BaseAmount" in data:
            self.BaseAmount: Currency = Currency(data["BaseAmount"])
        else:
            self.BaseAmount: Currency = None
        if "WithheldAmount" in data:
            self.WithheldAmount: Currency = Currency(data["WithheldAmount"])
        else:
            self.WithheldAmount: Currency = None
        if "TaxWithholdingPeriod" in data:
            self.TaxWithholdingPeriod: TaxWithholdingPeriod = TaxWithholdingPeriod(data["TaxWithholdingPeriod"])
        else:
            self.TaxWithholdingPeriod: TaxWithholdingPeriod = None


class TaxWithheldComponent:
    """
    Information about the taxes withheld.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = str(data["TaxCollectionModel"])
        else:
            self.TaxCollectionModel: str = None
        if "TaxesWithheld" in data:
            self.TaxesWithheld: ChargeComponentList = ChargeComponentList(data["TaxesWithheld"])
        else:
            self.TaxesWithheld: ChargeComponentList = None


class TrialShipmentEvent:
    """
    An event related to a trial shipment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = str(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: str = None
        if "FinancialEventGroupId" in data:
            self.FinancialEventGroupId: str = str(data["FinancialEventGroupId"])
        else:
            self.FinancialEventGroupId: str = None
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "SKU" in data:
            self.SKU: str = str(data["SKU"])
        else:
            self.SKU: str = None
        if "FeeList" in data:
            self.FeeList: FeeComponentList = FeeComponentList(data["FeeList"])
        else:
            self.FeeList: FeeComponentList = None


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
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
        return {
            200: ListFinancialEventGroupsResponse,
            400: ListFinancialEventGroupsResponse,
            403: ListFinancialEventGroupsResponse,
            404: ListFinancialEventGroupsResponse,
            429: ListFinancialEventGroupsResponse,
            500: ListFinancialEventGroupsResponse,
            503: ListFinancialEventGroupsResponse,
        }[response.status_code](self._get_response_json(response))

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
        return {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }[response.status_code](self._get_response_json(response))

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
        return {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }[response.status_code](self._get_response_json(response))

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
        return {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }[response.status_code](self._get_response_json(response))
