from .base import BaseClient as __BaseClient
from typing import List as _List


class AdjustmentEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "ChargeType" in data:
            self.ChargeType: str = str(data["ChargeType"])
        else:
            self.ChargeType: str = None
        if "ChargeAmount" in data:
            self.ChargeAmount: Currency = Currency(data["ChargeAmount"])
        else:
            self.ChargeAmount: Currency = None


class ChargeInstrument:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None
        if "CurrencyAmount" in data:
            self.CurrencyAmount: BigDecimal = BigDecimal(data["CurrencyAmount"])
        else:
            self.CurrencyAmount: BigDecimal = None


class DebtRecoveryEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "DirectPaymentType" in data:
            self.DirectPaymentType: str = str(data["DirectPaymentType"])
        else:
            self.DirectPaymentType: str = None
        if "DirectPaymentAmount" in data:
            self.DirectPaymentAmount: Currency = Currency(data["DirectPaymentAmount"])
        else:
            self.DirectPaymentAmount: Currency = None


class FBALiquidationEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "FeeType" in data:
            self.FeeType: str = str(data["FeeType"])
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: Currency = Currency(data["FeeAmount"])
        else:
            self.FeeAmount: Currency = None


class FinancialEventGroup:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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


class ImagingServicesFeeEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: ListFinancialEventGroupsPayload = ListFinancialEventGroupsPayload(data["payload"])
        else:
            self.payload: ListFinancialEventGroupsPayload = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ListFinancialEventsPayload:
    def __init__(self, data):
        super().__init__()
        if "NextToken" in data:
            self.NextToken: str = str(data["NextToken"])
        else:
            self.NextToken: str = None
        if "FinancialEvents" in data:
            self.FinancialEvents: FinancialEvents = FinancialEvents(data["FinancialEvents"])
        else:
            self.FinancialEvents: FinancialEvents = None


class ListFinancialEventsResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: ListFinancialEventsPayload = ListFinancialEventsPayload(data["payload"])
        else:
            self.payload: ListFinancialEventsPayload = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class LoanServicingEvent:
    def __init__(self, data):
        super().__init__()
        if "LoanAmount" in data:
            self.LoanAmount: Currency = Currency(data["LoanAmount"])
        else:
            self.LoanAmount: Currency = None
        if "SourceBusinessEventType" in data:
            self.SourceBusinessEventType: str = str(data["SourceBusinessEventType"])
        else:
            self.SourceBusinessEventType: str = None


class NetworkComminglingTransactionEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
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
    def __init__(self, data):
        super().__init__()
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


class RentalTransactionEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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


class TDSReimbursementEvent:
    def __init__(self, data):
        super().__init__()
        if "PostedDate" in data:
            self.PostedDate: Date = Date(data["PostedDate"])
        else:
            self.PostedDate: Date = None
        if "TdsOrderId" in data:
            self.TdsOrderId: str = str(data["TdsOrderId"])
        else:
            self.TdsOrderId: str = None
        if "ReimbursedAmount" in data:
            self.ReimbursedAmount: Currency = Currency(data["ReimbursedAmount"])
        else:
            self.ReimbursedAmount: Currency = None


class TaxWithheldComponent:
    def __init__(self, data):
        super().__init__()
        if "TaxCollectionModel" in data:
            self.TaxCollectionModel: str = str(data["TaxCollectionModel"])
        else:
            self.TaxCollectionModel: str = None
        if "TaxesWithheld" in data:
            self.TaxesWithheld: ChargeComponentList = ChargeComponentList(data["TaxesWithheld"])
        else:
            self.TaxesWithheld: ChargeComponentList = None


class TrialShipmentEvent:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__([AdjustmentEvent(datum) for datum in data])


class AdjustmentItemList(list, _List["AdjustmentItem"]):
    def __init__(self, data):
        super().__init__([AdjustmentItem(datum) for datum in data])


class AffordabilityExpenseEventList(list, _List["AffordabilityExpenseEvent"]):
    def __init__(self, data):
        super().__init__([AffordabilityExpenseEvent(datum) for datum in data])


class ChargeComponentList(list, _List["ChargeComponent"]):
    def __init__(self, data):
        super().__init__([ChargeComponent(datum) for datum in data])


class ChargeInstrumentList(list, _List["ChargeInstrument"]):
    def __init__(self, data):
        super().__init__([ChargeInstrument(datum) for datum in data])


class CouponPaymentEventList(list, _List["CouponPaymentEvent"]):
    def __init__(self, data):
        super().__init__([CouponPaymentEvent(datum) for datum in data])


class DebtRecoveryEventList(list, _List["DebtRecoveryEvent"]):
    def __init__(self, data):
        super().__init__([DebtRecoveryEvent(datum) for datum in data])


class DebtRecoveryItemList(list, _List["DebtRecoveryItem"]):
    def __init__(self, data):
        super().__init__([DebtRecoveryItem(datum) for datum in data])


class DirectPaymentList(list, _List["DirectPayment"]):
    def __init__(self, data):
        super().__init__([DirectPayment(datum) for datum in data])


class FBALiquidationEventList(list, _List["FBALiquidationEvent"]):
    def __init__(self, data):
        super().__init__([FBALiquidationEvent(datum) for datum in data])


class FeeComponentList(list, _List["FeeComponent"]):
    def __init__(self, data):
        super().__init__([FeeComponent(datum) for datum in data])


class FinancialEventGroupList(list, _List["FinancialEventGroup"]):
    def __init__(self, data):
        super().__init__([FinancialEventGroup(datum) for datum in data])


class ImagingServicesFeeEventList(list, _List["ImagingServicesFeeEvent"]):
    def __init__(self, data):
        super().__init__([ImagingServicesFeeEvent(datum) for datum in data])


class LoanServicingEventList(list, _List["LoanServicingEvent"]):
    def __init__(self, data):
        super().__init__([LoanServicingEvent(datum) for datum in data])


class NetworkComminglingTransactionEventList(list, _List["NetworkComminglingTransactionEvent"]):
    def __init__(self, data):
        super().__init__([NetworkComminglingTransactionEvent(datum) for datum in data])


class PayWithAmazonEventList(list, _List["PayWithAmazonEvent"]):
    def __init__(self, data):
        super().__init__([PayWithAmazonEvent(datum) for datum in data])


class ProductAdsPaymentEventList(list, _List["ProductAdsPaymentEvent"]):
    def __init__(self, data):
        super().__init__([ProductAdsPaymentEvent(datum) for datum in data])


class PromotionList(list, _List["Promotion"]):
    def __init__(self, data):
        super().__init__([Promotion(datum) for datum in data])


class RemovalShipmentEventList(list, _List["RemovalShipmentEvent"]):
    def __init__(self, data):
        super().__init__([RemovalShipmentEvent(datum) for datum in data])


class RemovalShipmentItemList(list, _List["RemovalShipmentItem"]):
    def __init__(self, data):
        super().__init__([RemovalShipmentItem(datum) for datum in data])


class RentalTransactionEventList(list, _List["RentalTransactionEvent"]):
    def __init__(self, data):
        super().__init__([RentalTransactionEvent(datum) for datum in data])


class RetrochargeEventList(list, _List["RetrochargeEvent"]):
    def __init__(self, data):
        super().__init__([RetrochargeEvent(datum) for datum in data])


class SAFETReimbursementEventList(list, _List["SAFETReimbursementEvent"]):
    def __init__(self, data):
        super().__init__([SAFETReimbursementEvent(datum) for datum in data])


class SAFETReimbursementItemList(list, _List["SAFETReimbursementItem"]):
    def __init__(self, data):
        super().__init__([SAFETReimbursementItem(datum) for datum in data])


class SellerDealPaymentEventList(list, _List["SellerDealPaymentEvent"]):
    def __init__(self, data):
        super().__init__([SellerDealPaymentEvent(datum) for datum in data])


class SellerReviewEnrollmentPaymentEventList(list, _List["SellerReviewEnrollmentPaymentEvent"]):
    def __init__(self, data):
        super().__init__([SellerReviewEnrollmentPaymentEvent(datum) for datum in data])


class ServiceFeeEventList(list, _List["ServiceFeeEvent"]):
    def __init__(self, data):
        super().__init__([ServiceFeeEvent(datum) for datum in data])


class ShipmentEventList(list, _List["ShipmentEvent"]):
    def __init__(self, data):
        super().__init__([ShipmentEvent(datum) for datum in data])


class ShipmentItemList(list, _List["ShipmentItem"]):
    def __init__(self, data):
        super().__init__([ShipmentItem(datum) for datum in data])


class SolutionProviderCreditEventList(list, _List["SolutionProviderCreditEvent"]):
    def __init__(self, data):
        super().__init__([SolutionProviderCreditEvent(datum) for datum in data])


class TDSReimbursementEventList(list, _List["TDSReimbursementEvent"]):
    def __init__(self, data):
        super().__init__([TDSReimbursementEvent(datum) for datum in data])


class TaxWithheldComponentList(list, _List["TaxWithheldComponent"]):
    def __init__(self, data):
        super().__init__([TaxWithheldComponent(datum) for datum in data])


class TrialShipmentEventList(list, _List["TrialShipmentEvent"]):
    def __init__(self, data):
        super().__init__([TrialShipmentEvent(datum) for datum in data])


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])


BigDecimal = float
Date = str


class FinancesClient(__BaseClient):
    def listFinancialEventGroups(
        self,
        MaxResultsPerPage: int = None,
        FinancialEventGroupStartedBefore: str = None,
        FinancialEventGroupStartedAfter: str = None,
        NextToken: str = None,
    ):
        url = "/finances/v0/financialEventGroups".format()
        data = {}
        if MaxResultsPerPage is not None:
            data["MaxResultsPerPage"] = (MaxResultsPerPage,)
        if FinancialEventGroupStartedBefore is not None:
            data["FinancialEventGroupStartedBefore"] = (FinancialEventGroupStartedBefore,)
        if FinancialEventGroupStartedAfter is not None:
            data["FinancialEventGroupStartedAfter"] = (FinancialEventGroupStartedAfter,)
        if NextToken is not None:
            data["NextToken"] = (NextToken,)
        response = self.request(url, method="GET", params=data)
        return {
            200: ListFinancialEventGroupsResponse,
            400: ListFinancialEventGroupsResponse,
            403: ListFinancialEventGroupsResponse,
            404: ListFinancialEventGroupsResponse,
            429: ListFinancialEventGroupsResponse,
            500: ListFinancialEventGroupsResponse,
            503: ListFinancialEventGroupsResponse,
        }[response.status_code](response.json())

    def listFinancialEventsByGroupId(
        self,
        eventGroupId: str,
        MaxResultsPerPage: int = None,
        NextToken: str = None,
    ):
        url = "/finances/v0/financialEventGroups/{eventGroupId}/financialEvents".format(
            eventGroupId=eventGroupId,
        )
        data = {}
        if MaxResultsPerPage is not None:
            data["MaxResultsPerPage"] = (MaxResultsPerPage,)
        if NextToken is not None:
            data["NextToken"] = (NextToken,)
        response = self.request(url, method="GET", params=data)
        return {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }[response.status_code](response.json())

    def listFinancialEventsByOrderId(
        self,
        orderId: str,
        MaxResultsPerPage: int = None,
        NextToken: str = None,
    ):
        url = "/finances/v0/orders/{orderId}/financialEvents".format(
            orderId=orderId,
        )
        data = {}
        if MaxResultsPerPage is not None:
            data["MaxResultsPerPage"] = (MaxResultsPerPage,)
        if NextToken is not None:
            data["NextToken"] = (NextToken,)
        response = self.request(url, method="GET", params=data)
        return {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }[response.status_code](response.json())

    def listFinancialEvents(
        self,
        MaxResultsPerPage: int = None,
        PostedAfter: str = None,
        PostedBefore: str = None,
        NextToken: str = None,
    ):
        url = "/finances/v0/financialEvents".format()
        data = {}
        if MaxResultsPerPage is not None:
            data["MaxResultsPerPage"] = (MaxResultsPerPage,)
        if PostedAfter is not None:
            data["PostedAfter"] = (PostedAfter,)
        if PostedBefore is not None:
            data["PostedBefore"] = (PostedBefore,)
        if NextToken is not None:
            data["NextToken"] = (NextToken,)
        response = self.request(url, method="GET", params=data)
        return {
            200: ListFinancialEventsResponse,
            400: ListFinancialEventsResponse,
            403: ListFinancialEventsResponse,
            404: ListFinancialEventsResponse,
            429: ListFinancialEventsResponse,
            500: ListFinancialEventsResponse,
            503: ListFinancialEventsResponse,
        }[response.status_code](response.json())
