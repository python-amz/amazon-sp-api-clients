from .base import BaseClient as __BaseClient
from typing import List as _List


class Error:
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


class ASINInboundGuidance:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "InboundGuidance" in data:
            self.InboundGuidance: InboundGuidance = InboundGuidance(data["InboundGuidance"])
        else:
            self.InboundGuidance: InboundGuidance = None
        if "GuidanceReasonList" in data:
            self.GuidanceReasonList: GuidanceReasonList = GuidanceReasonList(data["GuidanceReasonList"])
        else:
            self.GuidanceReasonList: GuidanceReasonList = None


class ASINPrepInstructions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "BarcodeInstruction" in data:
            self.BarcodeInstruction: BarcodeInstruction = BarcodeInstruction(data["BarcodeInstruction"])
        else:
            self.BarcodeInstruction: BarcodeInstruction = None
        if "PrepGuidance" in data:
            self.PrepGuidance: PrepGuidance = PrepGuidance(data["PrepGuidance"])
        else:
            self.PrepGuidance: PrepGuidance = None
        if "PrepInstructionList" in data:
            self.PrepInstructionList: PrepInstructionList = PrepInstructionList(data["PrepInstructionList"])
        else:
            self.PrepInstructionList: PrepInstructionList = None


class Address:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Name" in data:
            self.Name: str = str(data["Name"])
        else:
            self.Name: str = None
        if "AddressLine1" in data:
            self.AddressLine1: str = str(data["AddressLine1"])
        else:
            self.AddressLine1: str = None
        if "AddressLine2" in data:
            self.AddressLine2: str = str(data["AddressLine2"])
        else:
            self.AddressLine2: str = None
        if "DistrictOrCounty" in data:
            self.DistrictOrCounty: str = str(data["DistrictOrCounty"])
        else:
            self.DistrictOrCounty: str = None
        if "City" in data:
            self.City: str = str(data["City"])
        else:
            self.City: str = None
        if "StateOrProvinceCode" in data:
            self.StateOrProvinceCode: str = str(data["StateOrProvinceCode"])
        else:
            self.StateOrProvinceCode: str = None
        if "CountryCode" in data:
            self.CountryCode: str = str(data["CountryCode"])
        else:
            self.CountryCode: str = None
        if "PostalCode" in data:
            self.PostalCode: str = str(data["PostalCode"])
        else:
            self.PostalCode: str = None


class AmazonPrepFeesDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PrepInstruction" in data:
            self.PrepInstruction: PrepInstruction = PrepInstruction(data["PrepInstruction"])
        else:
            self.PrepInstruction: PrepInstruction = None
        if "FeePerUnit" in data:
            self.FeePerUnit: Amount = Amount(data["FeePerUnit"])
        else:
            self.FeePerUnit: Amount = None


class Amount:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CurrencyCode" in data:
            self.CurrencyCode: CurrencyCode = CurrencyCode(data["CurrencyCode"])
        else:
            self.CurrencyCode: CurrencyCode = None
        if "Value" in data:
            self.Value: BigDecimalType = BigDecimalType(data["Value"])
        else:
            self.Value: BigDecimalType = None


class BoxContentsFeeDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TotalUnits" in data:
            self.TotalUnits: Quantity = Quantity(data["TotalUnits"])
        else:
            self.TotalUnits: Quantity = None
        if "FeePerUnit" in data:
            self.FeePerUnit: Amount = Amount(data["FeePerUnit"])
        else:
            self.FeePerUnit: Amount = None
        if "TotalFee" in data:
            self.TotalFee: Amount = Amount(data["TotalFee"])
        else:
            self.TotalFee: Amount = None


class ConfirmPreorderResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ConfirmedNeedByDate" in data:
            self.ConfirmedNeedByDate: DateStringType = DateStringType(data["ConfirmedNeedByDate"])
        else:
            self.ConfirmedNeedByDate: DateStringType = None
        if "ConfirmedFulfillableDate" in data:
            self.ConfirmedFulfillableDate: DateStringType = DateStringType(data["ConfirmedFulfillableDate"])
        else:
            self.ConfirmedFulfillableDate: DateStringType = None


class ConfirmPreorderResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ConfirmPreorderResult = ConfirmPreorderResult(data["payload"])
        else:
            self.payload: ConfirmPreorderResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CommonTransportResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransportResult" in data:
            self.TransportResult: TransportResult = TransportResult(data["TransportResult"])
        else:
            self.TransportResult: TransportResult = None


class ConfirmTransportResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CommonTransportResult = CommonTransportResult(data["payload"])
        else:
            self.payload: CommonTransportResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Contact:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Name" in data:
            self.Name: str = str(data["Name"])
        else:
            self.Name: str = None
        if "Phone" in data:
            self.Phone: str = str(data["Phone"])
        else:
            self.Phone: str = None
        if "Email" in data:
            self.Email: str = str(data["Email"])
        else:
            self.Email: str = None
        if "Fax" in data:
            self.Fax: str = str(data["Fax"])
        else:
            self.Fax: str = None


class CreateInboundShipmentPlanRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = Address(data["ShipFromAddress"])
        else:
            self.ShipFromAddress: Address = None
        if "LabelPrepPreference" in data:
            self.LabelPrepPreference: LabelPrepPreference = LabelPrepPreference(data["LabelPrepPreference"])
        else:
            self.LabelPrepPreference: LabelPrepPreference = None
        if "ShipToCountryCode" in data:
            self.ShipToCountryCode: str = str(data["ShipToCountryCode"])
        else:
            self.ShipToCountryCode: str = None
        if "ShipToCountrySubdivisionCode" in data:
            self.ShipToCountrySubdivisionCode: str = str(data["ShipToCountrySubdivisionCode"])
        else:
            self.ShipToCountrySubdivisionCode: str = None
        if "InboundShipmentPlanRequestItems" in data:
            self.InboundShipmentPlanRequestItems: InboundShipmentPlanRequestItemList = (
                InboundShipmentPlanRequestItemList(data["InboundShipmentPlanRequestItems"])
            )
        else:
            self.InboundShipmentPlanRequestItems: InboundShipmentPlanRequestItemList = None


class CreateInboundShipmentPlanResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "InboundShipmentPlans" in data:
            self.InboundShipmentPlans: InboundShipmentPlanList = InboundShipmentPlanList(data["InboundShipmentPlans"])
        else:
            self.InboundShipmentPlans: InboundShipmentPlanList = None


class CreateInboundShipmentPlanResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateInboundShipmentPlanResult = CreateInboundShipmentPlanResult(data["payload"])
        else:
            self.payload: CreateInboundShipmentPlanResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class InboundShipmentRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "InboundShipmentHeader" in data:
            self.InboundShipmentHeader: InboundShipmentHeader = InboundShipmentHeader(data["InboundShipmentHeader"])
        else:
            self.InboundShipmentHeader: InboundShipmentHeader = None
        if "InboundShipmentItems" in data:
            self.InboundShipmentItems: InboundShipmentItemList = InboundShipmentItemList(data["InboundShipmentItems"])
        else:
            self.InboundShipmentItems: InboundShipmentItemList = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None


class InboundShipmentResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentId" in data:
            self.ShipmentId: str = str(data["ShipmentId"])
        else:
            self.ShipmentId: str = None


class InboundShipmentResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: InboundShipmentResult = InboundShipmentResult(data["payload"])
        else:
            self.payload: InboundShipmentResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Dimensions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Length" in data:
            self.Length: BigDecimalType = BigDecimalType(data["Length"])
        else:
            self.Length: BigDecimalType = None
        if "Width" in data:
            self.Width: BigDecimalType = BigDecimalType(data["Width"])
        else:
            self.Width: BigDecimalType = None
        if "Height" in data:
            self.Height: BigDecimalType = BigDecimalType(data["Height"])
        else:
            self.Height: BigDecimalType = None
        if "Unit" in data:
            self.Unit: UnitOfMeasurement = UnitOfMeasurement(data["Unit"])
        else:
            self.Unit: UnitOfMeasurement = None


class EstimateTransportResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CommonTransportResult = CommonTransportResult(data["payload"])
        else:
            self.payload: CommonTransportResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetBillOfLadingResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: BillOfLadingDownloadURL = BillOfLadingDownloadURL(data["payload"])
        else:
            self.payload: BillOfLadingDownloadURL = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetInboundGuidanceResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SKUInboundGuidanceList" in data:
            self.SKUInboundGuidanceList: SKUInboundGuidanceList = SKUInboundGuidanceList(data["SKUInboundGuidanceList"])
        else:
            self.SKUInboundGuidanceList: SKUInboundGuidanceList = None
        if "InvalidSKUList" in data:
            self.InvalidSKUList: InvalidSKUList = InvalidSKUList(data["InvalidSKUList"])
        else:
            self.InvalidSKUList: InvalidSKUList = None
        if "ASINInboundGuidanceList" in data:
            self.ASINInboundGuidanceList: ASINInboundGuidanceList = ASINInboundGuidanceList(
                data["ASINInboundGuidanceList"]
            )
        else:
            self.ASINInboundGuidanceList: ASINInboundGuidanceList = None
        if "InvalidASINList" in data:
            self.InvalidASINList: InvalidASINList = InvalidASINList(data["InvalidASINList"])
        else:
            self.InvalidASINList: InvalidASINList = None


class GetInboundGuidanceResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetInboundGuidanceResult = GetInboundGuidanceResult(data["payload"])
        else:
            self.payload: GetInboundGuidanceResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class LabelDownloadURL:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DownloadURL" in data:
            self.DownloadURL: str = str(data["DownloadURL"])
        else:
            self.DownloadURL: str = None


class BillOfLadingDownloadURL:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DownloadURL" in data:
            self.DownloadURL: str = str(data["DownloadURL"])
        else:
            self.DownloadURL: str = None


class GetLabelsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: LabelDownloadURL = LabelDownloadURL(data["payload"])
        else:
            self.payload: LabelDownloadURL = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetPreorderInfoResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentContainsPreorderableItems" in data:
            self.ShipmentContainsPreorderableItems: bool = bool(data["ShipmentContainsPreorderableItems"])
        else:
            self.ShipmentContainsPreorderableItems: bool = None
        if "ShipmentConfirmedForPreorder" in data:
            self.ShipmentConfirmedForPreorder: bool = bool(data["ShipmentConfirmedForPreorder"])
        else:
            self.ShipmentConfirmedForPreorder: bool = None
        if "NeedByDate" in data:
            self.NeedByDate: DateStringType = DateStringType(data["NeedByDate"])
        else:
            self.NeedByDate: DateStringType = None
        if "ConfirmedFulfillableDate" in data:
            self.ConfirmedFulfillableDate: DateStringType = DateStringType(data["ConfirmedFulfillableDate"])
        else:
            self.ConfirmedFulfillableDate: DateStringType = None


class GetPreorderInfoResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetPreorderInfoResult = GetPreorderInfoResult(data["payload"])
        else:
            self.payload: GetPreorderInfoResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetPrepInstructionsResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SKUPrepInstructionsList" in data:
            self.SKUPrepInstructionsList: SKUPrepInstructionsList = SKUPrepInstructionsList(
                data["SKUPrepInstructionsList"]
            )
        else:
            self.SKUPrepInstructionsList: SKUPrepInstructionsList = None
        if "InvalidSKUList" in data:
            self.InvalidSKUList: InvalidSKUList = InvalidSKUList(data["InvalidSKUList"])
        else:
            self.InvalidSKUList: InvalidSKUList = None
        if "ASINPrepInstructionsList" in data:
            self.ASINPrepInstructionsList: ASINPrepInstructionsList = ASINPrepInstructionsList(
                data["ASINPrepInstructionsList"]
            )
        else:
            self.ASINPrepInstructionsList: ASINPrepInstructionsList = None
        if "InvalidASINList" in data:
            self.InvalidASINList: InvalidASINList = InvalidASINList(data["InvalidASINList"])
        else:
            self.InvalidASINList: InvalidASINList = None


class GetPrepInstructionsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetPrepInstructionsResult = GetPrepInstructionsResult(data["payload"])
        else:
            self.payload: GetPrepInstructionsResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetTransportDetailsResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransportContent" in data:
            self.TransportContent: TransportContent = TransportContent(data["TransportContent"])
        else:
            self.TransportContent: TransportContent = None


class GetTransportDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetTransportDetailsResult = GetTransportDetailsResult(data["payload"])
        else:
            self.payload: GetTransportDetailsResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class InboundShipmentHeader:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentName" in data:
            self.ShipmentName: str = str(data["ShipmentName"])
        else:
            self.ShipmentName: str = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = Address(data["ShipFromAddress"])
        else:
            self.ShipFromAddress: Address = None
        if "DestinationFulfillmentCenterId" in data:
            self.DestinationFulfillmentCenterId: str = str(data["DestinationFulfillmentCenterId"])
        else:
            self.DestinationFulfillmentCenterId: str = None
        if "AreCasesRequired" in data:
            self.AreCasesRequired: bool = bool(data["AreCasesRequired"])
        else:
            self.AreCasesRequired: bool = None
        if "ShipmentStatus" in data:
            self.ShipmentStatus: ShipmentStatus = ShipmentStatus(data["ShipmentStatus"])
        else:
            self.ShipmentStatus: ShipmentStatus = None
        if "LabelPrepPreference" in data:
            self.LabelPrepPreference: LabelPrepPreference = LabelPrepPreference(data["LabelPrepPreference"])
        else:
            self.LabelPrepPreference: LabelPrepPreference = None
        if "IntendedBoxContentsSource" in data:
            self.IntendedBoxContentsSource: IntendedBoxContentsSource = IntendedBoxContentsSource(
                data["IntendedBoxContentsSource"]
            )
        else:
            self.IntendedBoxContentsSource: IntendedBoxContentsSource = None


class InboundShipmentInfo:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentId" in data:
            self.ShipmentId: str = str(data["ShipmentId"])
        else:
            self.ShipmentId: str = None
        if "ShipmentName" in data:
            self.ShipmentName: str = str(data["ShipmentName"])
        else:
            self.ShipmentName: str = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = Address(data["ShipFromAddress"])
        else:
            self.ShipFromAddress: Address = None
        if "DestinationFulfillmentCenterId" in data:
            self.DestinationFulfillmentCenterId: str = str(data["DestinationFulfillmentCenterId"])
        else:
            self.DestinationFulfillmentCenterId: str = None
        if "ShipmentStatus" in data:
            self.ShipmentStatus: ShipmentStatus = ShipmentStatus(data["ShipmentStatus"])
        else:
            self.ShipmentStatus: ShipmentStatus = None
        if "LabelPrepType" in data:
            self.LabelPrepType: LabelPrepType = LabelPrepType(data["LabelPrepType"])
        else:
            self.LabelPrepType: LabelPrepType = None
        if "AreCasesRequired" in data:
            self.AreCasesRequired: bool = bool(data["AreCasesRequired"])
        else:
            self.AreCasesRequired: bool = None
        if "ConfirmedNeedByDate" in data:
            self.ConfirmedNeedByDate: DateStringType = DateStringType(data["ConfirmedNeedByDate"])
        else:
            self.ConfirmedNeedByDate: DateStringType = None
        if "BoxContentsSource" in data:
            self.BoxContentsSource: BoxContentsSource = BoxContentsSource(data["BoxContentsSource"])
        else:
            self.BoxContentsSource: BoxContentsSource = None
        if "EstimatedBoxContentsFee" in data:
            self.EstimatedBoxContentsFee: BoxContentsFeeDetails = BoxContentsFeeDetails(data["EstimatedBoxContentsFee"])
        else:
            self.EstimatedBoxContentsFee: BoxContentsFeeDetails = None


class InboundShipmentItem:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentId" in data:
            self.ShipmentId: str = str(data["ShipmentId"])
        else:
            self.ShipmentId: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "FulfillmentNetworkSKU" in data:
            self.FulfillmentNetworkSKU: str = str(data["FulfillmentNetworkSKU"])
        else:
            self.FulfillmentNetworkSKU: str = None
        if "QuantityShipped" in data:
            self.QuantityShipped: Quantity = Quantity(data["QuantityShipped"])
        else:
            self.QuantityShipped: Quantity = None
        if "QuantityReceived" in data:
            self.QuantityReceived: Quantity = Quantity(data["QuantityReceived"])
        else:
            self.QuantityReceived: Quantity = None
        if "QuantityInCase" in data:
            self.QuantityInCase: Quantity = Quantity(data["QuantityInCase"])
        else:
            self.QuantityInCase: Quantity = None
        if "ReleaseDate" in data:
            self.ReleaseDate: DateStringType = DateStringType(data["ReleaseDate"])
        else:
            self.ReleaseDate: DateStringType = None
        if "PrepDetailsList" in data:
            self.PrepDetailsList: PrepDetailsList = PrepDetailsList(data["PrepDetailsList"])
        else:
            self.PrepDetailsList: PrepDetailsList = None


class InboundShipmentPlan:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentId" in data:
            self.ShipmentId: str = str(data["ShipmentId"])
        else:
            self.ShipmentId: str = None
        if "DestinationFulfillmentCenterId" in data:
            self.DestinationFulfillmentCenterId: str = str(data["DestinationFulfillmentCenterId"])
        else:
            self.DestinationFulfillmentCenterId: str = None
        if "ShipToAddress" in data:
            self.ShipToAddress: Address = Address(data["ShipToAddress"])
        else:
            self.ShipToAddress: Address = None
        if "LabelPrepType" in data:
            self.LabelPrepType: LabelPrepType = LabelPrepType(data["LabelPrepType"])
        else:
            self.LabelPrepType: LabelPrepType = None
        if "Items" in data:
            self.Items: InboundShipmentPlanItemList = InboundShipmentPlanItemList(data["Items"])
        else:
            self.Items: InboundShipmentPlanItemList = None
        if "EstimatedBoxContentsFee" in data:
            self.EstimatedBoxContentsFee: BoxContentsFeeDetails = BoxContentsFeeDetails(data["EstimatedBoxContentsFee"])
        else:
            self.EstimatedBoxContentsFee: BoxContentsFeeDetails = None


class InboundShipmentPlanItem:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "FulfillmentNetworkSKU" in data:
            self.FulfillmentNetworkSKU: str = str(data["FulfillmentNetworkSKU"])
        else:
            self.FulfillmentNetworkSKU: str = None
        if "Quantity" in data:
            self.Quantity: Quantity = Quantity(data["Quantity"])
        else:
            self.Quantity: Quantity = None
        if "PrepDetailsList" in data:
            self.PrepDetailsList: PrepDetailsList = PrepDetailsList(data["PrepDetailsList"])
        else:
            self.PrepDetailsList: PrepDetailsList = None


class InboundShipmentPlanRequestItem:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "Condition" in data:
            self.Condition: Condition = Condition(data["Condition"])
        else:
            self.Condition: Condition = None
        if "Quantity" in data:
            self.Quantity: Quantity = Quantity(data["Quantity"])
        else:
            self.Quantity: Quantity = None
        if "QuantityInCase" in data:
            self.QuantityInCase: Quantity = Quantity(data["QuantityInCase"])
        else:
            self.QuantityInCase: Quantity = None
        if "PrepDetailsList" in data:
            self.PrepDetailsList: PrepDetailsList = PrepDetailsList(data["PrepDetailsList"])
        else:
            self.PrepDetailsList: PrepDetailsList = None


class InvalidASIN:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "ErrorReason" in data:
            self.ErrorReason: ErrorReason = ErrorReason(data["ErrorReason"])
        else:
            self.ErrorReason: ErrorReason = None


class InvalidSKU:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "ErrorReason" in data:
            self.ErrorReason: ErrorReason = ErrorReason(data["ErrorReason"])
        else:
            self.ErrorReason: ErrorReason = None


class GetShipmentItemsResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ItemData" in data:
            self.ItemData: InboundShipmentItemList = InboundShipmentItemList(data["ItemData"])
        else:
            self.ItemData: InboundShipmentItemList = None
        if "NextToken" in data:
            self.NextToken: str = str(data["NextToken"])
        else:
            self.NextToken: str = None


class GetShipmentItemsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetShipmentItemsResult = GetShipmentItemsResult(data["payload"])
        else:
            self.payload: GetShipmentItemsResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetShipmentsResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentData" in data:
            self.ShipmentData: InboundShipmentList = InboundShipmentList(data["ShipmentData"])
        else:
            self.ShipmentData: InboundShipmentList = None
        if "NextToken" in data:
            self.NextToken: str = str(data["NextToken"])
        else:
            self.NextToken: str = None


class GetShipmentsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetShipmentsResult = GetShipmentsResult(data["payload"])
        else:
            self.payload: GetShipmentsResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class NonPartneredLtlDataInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "ProNumber" in data:
            self.ProNumber: ProNumber = ProNumber(data["ProNumber"])
        else:
            self.ProNumber: ProNumber = None


class NonPartneredLtlDataOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "ProNumber" in data:
            self.ProNumber: ProNumber = ProNumber(data["ProNumber"])
        else:
            self.ProNumber: ProNumber = None


class NonPartneredSmallParcelDataInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "PackageList" in data:
            self.PackageList: NonPartneredSmallParcelPackageInputList = NonPartneredSmallParcelPackageInputList(
                data["PackageList"]
            )
        else:
            self.PackageList: NonPartneredSmallParcelPackageInputList = None


class NonPartneredSmallParcelDataOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PackageList" in data:
            self.PackageList: NonPartneredSmallParcelPackageOutputList = NonPartneredSmallParcelPackageOutputList(
                data["PackageList"]
            )
        else:
            self.PackageList: NonPartneredSmallParcelPackageOutputList = None


class NonPartneredSmallParcelPackageInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TrackingId" in data:
            self.TrackingId: TrackingId = TrackingId(data["TrackingId"])
        else:
            self.TrackingId: TrackingId = None


class NonPartneredSmallParcelPackageOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "TrackingId" in data:
            self.TrackingId: TrackingId = TrackingId(data["TrackingId"])
        else:
            self.TrackingId: TrackingId = None
        if "PackageStatus" in data:
            self.PackageStatus: PackageStatus = PackageStatus(data["PackageStatus"])
        else:
            self.PackageStatus: PackageStatus = None


class Pallet:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Dimensions" in data:
            self.Dimensions: Dimensions = Dimensions(data["Dimensions"])
        else:
            self.Dimensions: Dimensions = None
        if "Weight" in data:
            self.Weight: Weight = Weight(data["Weight"])
        else:
            self.Weight: Weight = None
        if "IsStacked" in data:
            self.IsStacked: bool = bool(data["IsStacked"])
        else:
            self.IsStacked: bool = None


class PartneredEstimate:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Amount" in data:
            self.Amount: Amount = Amount(data["Amount"])
        else:
            self.Amount: Amount = None
        if "ConfirmDeadline" in data:
            self.ConfirmDeadline: TimeStampStringType = TimeStampStringType(data["ConfirmDeadline"])
        else:
            self.ConfirmDeadline: TimeStampStringType = None
        if "VoidDeadline" in data:
            self.VoidDeadline: TimeStampStringType = TimeStampStringType(data["VoidDeadline"])
        else:
            self.VoidDeadline: TimeStampStringType = None


class PartneredLtlDataInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Contact" in data:
            self.Contact: Contact = Contact(data["Contact"])
        else:
            self.Contact: Contact = None
        if "BoxCount" in data:
            self.BoxCount: UnsignedIntType = UnsignedIntType(data["BoxCount"])
        else:
            self.BoxCount: UnsignedIntType = None
        if "SellerFreightClass" in data:
            self.SellerFreightClass: SellerFreightClass = SellerFreightClass(data["SellerFreightClass"])
        else:
            self.SellerFreightClass: SellerFreightClass = None
        if "FreightReadyDate" in data:
            self.FreightReadyDate: DateStringType = DateStringType(data["FreightReadyDate"])
        else:
            self.FreightReadyDate: DateStringType = None
        if "PalletList" in data:
            self.PalletList: PalletList = PalletList(data["PalletList"])
        else:
            self.PalletList: PalletList = None
        if "TotalWeight" in data:
            self.TotalWeight: Weight = Weight(data["TotalWeight"])
        else:
            self.TotalWeight: Weight = None
        if "SellerDeclaredValue" in data:
            self.SellerDeclaredValue: Amount = Amount(data["SellerDeclaredValue"])
        else:
            self.SellerDeclaredValue: Amount = None


class PartneredLtlDataOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Contact" in data:
            self.Contact: Contact = Contact(data["Contact"])
        else:
            self.Contact: Contact = None
        if "BoxCount" in data:
            self.BoxCount: UnsignedIntType = UnsignedIntType(data["BoxCount"])
        else:
            self.BoxCount: UnsignedIntType = None
        if "SellerFreightClass" in data:
            self.SellerFreightClass: SellerFreightClass = SellerFreightClass(data["SellerFreightClass"])
        else:
            self.SellerFreightClass: SellerFreightClass = None
        if "FreightReadyDate" in data:
            self.FreightReadyDate: DateStringType = DateStringType(data["FreightReadyDate"])
        else:
            self.FreightReadyDate: DateStringType = None
        if "PalletList" in data:
            self.PalletList: PalletList = PalletList(data["PalletList"])
        else:
            self.PalletList: PalletList = None
        if "TotalWeight" in data:
            self.TotalWeight: Weight = Weight(data["TotalWeight"])
        else:
            self.TotalWeight: Weight = None
        if "SellerDeclaredValue" in data:
            self.SellerDeclaredValue: Amount = Amount(data["SellerDeclaredValue"])
        else:
            self.SellerDeclaredValue: Amount = None
        if "AmazonCalculatedValue" in data:
            self.AmazonCalculatedValue: Amount = Amount(data["AmazonCalculatedValue"])
        else:
            self.AmazonCalculatedValue: Amount = None
        if "PreviewPickupDate" in data:
            self.PreviewPickupDate: DateStringType = DateStringType(data["PreviewPickupDate"])
        else:
            self.PreviewPickupDate: DateStringType = None
        if "PreviewDeliveryDate" in data:
            self.PreviewDeliveryDate: DateStringType = DateStringType(data["PreviewDeliveryDate"])
        else:
            self.PreviewDeliveryDate: DateStringType = None
        if "PreviewFreightClass" in data:
            self.PreviewFreightClass: SellerFreightClass = SellerFreightClass(data["PreviewFreightClass"])
        else:
            self.PreviewFreightClass: SellerFreightClass = None
        if "AmazonReferenceId" in data:
            self.AmazonReferenceId: str = str(data["AmazonReferenceId"])
        else:
            self.AmazonReferenceId: str = None
        if "IsBillOfLadingAvailable" in data:
            self.IsBillOfLadingAvailable: bool = bool(data["IsBillOfLadingAvailable"])
        else:
            self.IsBillOfLadingAvailable: bool = None
        if "PartneredEstimate" in data:
            self.PartneredEstimate: PartneredEstimate = PartneredEstimate(data["PartneredEstimate"])
        else:
            self.PartneredEstimate: PartneredEstimate = None
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None


class PartneredSmallParcelDataInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PackageList" in data:
            self.PackageList: PartneredSmallParcelPackageInputList = PartneredSmallParcelPackageInputList(
                data["PackageList"]
            )
        else:
            self.PackageList: PartneredSmallParcelPackageInputList = None
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None


class PartneredSmallParcelDataOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PackageList" in data:
            self.PackageList: PartneredSmallParcelPackageOutputList = PartneredSmallParcelPackageOutputList(
                data["PackageList"]
            )
        else:
            self.PackageList: PartneredSmallParcelPackageOutputList = None
        if "PartneredEstimate" in data:
            self.PartneredEstimate: PartneredEstimate = PartneredEstimate(data["PartneredEstimate"])
        else:
            self.PartneredEstimate: PartneredEstimate = None


class PartneredSmallParcelPackageInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Dimensions" in data:
            self.Dimensions: Dimensions = Dimensions(data["Dimensions"])
        else:
            self.Dimensions: Dimensions = None
        if "Weight" in data:
            self.Weight: Weight = Weight(data["Weight"])
        else:
            self.Weight: Weight = None


class PartneredSmallParcelPackageOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Dimensions" in data:
            self.Dimensions: Dimensions = Dimensions(data["Dimensions"])
        else:
            self.Dimensions: Dimensions = None
        if "Weight" in data:
            self.Weight: Weight = Weight(data["Weight"])
        else:
            self.Weight: Weight = None
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "TrackingId" in data:
            self.TrackingId: TrackingId = TrackingId(data["TrackingId"])
        else:
            self.TrackingId: TrackingId = None
        if "PackageStatus" in data:
            self.PackageStatus: PackageStatus = PackageStatus(data["PackageStatus"])
        else:
            self.PackageStatus: PackageStatus = None


class PrepDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PrepInstruction" in data:
            self.PrepInstruction: PrepInstruction = PrepInstruction(data["PrepInstruction"])
        else:
            self.PrepInstruction: PrepInstruction = None
        if "PrepOwner" in data:
            self.PrepOwner: PrepOwner = PrepOwner(data["PrepOwner"])
        else:
            self.PrepOwner: PrepOwner = None


class PutTransportDetailsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IsPartnered" in data:
            self.IsPartnered: bool = bool(data["IsPartnered"])
        else:
            self.IsPartnered: bool = None
        if "ShipmentType" in data:
            self.ShipmentType: ShipmentType = ShipmentType(data["ShipmentType"])
        else:
            self.ShipmentType: ShipmentType = None
        if "TransportDetails" in data:
            self.TransportDetails: TransportDetailInput = TransportDetailInput(data["TransportDetails"])
        else:
            self.TransportDetails: TransportDetailInput = None


class PutTransportDetailsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CommonTransportResult = CommonTransportResult(data["payload"])
        else:
            self.payload: CommonTransportResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class SKUInboundGuidance:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "InboundGuidance" in data:
            self.InboundGuidance: InboundGuidance = InboundGuidance(data["InboundGuidance"])
        else:
            self.InboundGuidance: InboundGuidance = None
        if "GuidanceReasonList" in data:
            self.GuidanceReasonList: GuidanceReasonList = GuidanceReasonList(data["GuidanceReasonList"])
        else:
            self.GuidanceReasonList: GuidanceReasonList = None


class SKUPrepInstructions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None
        if "BarcodeInstruction" in data:
            self.BarcodeInstruction: BarcodeInstruction = BarcodeInstruction(data["BarcodeInstruction"])
        else:
            self.BarcodeInstruction: BarcodeInstruction = None
        if "PrepGuidance" in data:
            self.PrepGuidance: PrepGuidance = PrepGuidance(data["PrepGuidance"])
        else:
            self.PrepGuidance: PrepGuidance = None
        if "PrepInstructionList" in data:
            self.PrepInstructionList: PrepInstructionList = PrepInstructionList(data["PrepInstructionList"])
        else:
            self.PrepInstructionList: PrepInstructionList = None
        if "AmazonPrepFeesDetailsList" in data:
            self.AmazonPrepFeesDetailsList: AmazonPrepFeesDetailsList = AmazonPrepFeesDetailsList(
                data["AmazonPrepFeesDetailsList"]
            )
        else:
            self.AmazonPrepFeesDetailsList: AmazonPrepFeesDetailsList = None


class TransportContent:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransportHeader" in data:
            self.TransportHeader: TransportHeader = TransportHeader(data["TransportHeader"])
        else:
            self.TransportHeader: TransportHeader = None
        if "TransportDetails" in data:
            self.TransportDetails: TransportDetailOutput = TransportDetailOutput(data["TransportDetails"])
        else:
            self.TransportDetails: TransportDetailOutput = None
        if "TransportResult" in data:
            self.TransportResult: TransportResult = TransportResult(data["TransportResult"])
        else:
            self.TransportResult: TransportResult = None


class TransportDetailInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PartneredSmallParcelData" in data:
            self.PartneredSmallParcelData: PartneredSmallParcelDataInput = PartneredSmallParcelDataInput(
                data["PartneredSmallParcelData"]
            )
        else:
            self.PartneredSmallParcelData: PartneredSmallParcelDataInput = None
        if "NonPartneredSmallParcelData" in data:
            self.NonPartneredSmallParcelData: NonPartneredSmallParcelDataInput = NonPartneredSmallParcelDataInput(
                data["NonPartneredSmallParcelData"]
            )
        else:
            self.NonPartneredSmallParcelData: NonPartneredSmallParcelDataInput = None
        if "PartneredLtlData" in data:
            self.PartneredLtlData: PartneredLtlDataInput = PartneredLtlDataInput(data["PartneredLtlData"])
        else:
            self.PartneredLtlData: PartneredLtlDataInput = None
        if "NonPartneredLtlData" in data:
            self.NonPartneredLtlData: NonPartneredLtlDataInput = NonPartneredLtlDataInput(data["NonPartneredLtlData"])
        else:
            self.NonPartneredLtlData: NonPartneredLtlDataInput = None


class TransportDetailOutput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "PartneredSmallParcelData" in data:
            self.PartneredSmallParcelData: PartneredSmallParcelDataOutput = PartneredSmallParcelDataOutput(
                data["PartneredSmallParcelData"]
            )
        else:
            self.PartneredSmallParcelData: PartneredSmallParcelDataOutput = None
        if "NonPartneredSmallParcelData" in data:
            self.NonPartneredSmallParcelData: NonPartneredSmallParcelDataOutput = NonPartneredSmallParcelDataOutput(
                data["NonPartneredSmallParcelData"]
            )
        else:
            self.NonPartneredSmallParcelData: NonPartneredSmallParcelDataOutput = None
        if "PartneredLtlData" in data:
            self.PartneredLtlData: PartneredLtlDataOutput = PartneredLtlDataOutput(data["PartneredLtlData"])
        else:
            self.PartneredLtlData: PartneredLtlDataOutput = None
        if "NonPartneredLtlData" in data:
            self.NonPartneredLtlData: NonPartneredLtlDataOutput = NonPartneredLtlDataOutput(data["NonPartneredLtlData"])
        else:
            self.NonPartneredLtlData: NonPartneredLtlDataOutput = None


class TransportHeader:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "ShipmentId" in data:
            self.ShipmentId: str = str(data["ShipmentId"])
        else:
            self.ShipmentId: str = None
        if "IsPartnered" in data:
            self.IsPartnered: bool = bool(data["IsPartnered"])
        else:
            self.IsPartnered: bool = None
        if "ShipmentType" in data:
            self.ShipmentType: ShipmentType = ShipmentType(data["ShipmentType"])
        else:
            self.ShipmentType: ShipmentType = None


class TransportResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransportStatus" in data:
            self.TransportStatus: TransportStatus = TransportStatus(data["TransportStatus"])
        else:
            self.TransportStatus: TransportStatus = None
        if "ErrorCode" in data:
            self.ErrorCode: str = str(data["ErrorCode"])
        else:
            self.ErrorCode: str = None
        if "ErrorDescription" in data:
            self.ErrorDescription: str = str(data["ErrorDescription"])
        else:
            self.ErrorDescription: str = None


class VoidTransportResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CommonTransportResult = CommonTransportResult(data["payload"])
        else:
            self.payload: CommonTransportResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Weight:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Value" in data:
            self.Value: BigDecimalType = BigDecimalType(data["Value"])
        else:
            self.Value: BigDecimalType = None
        if "Unit" in data:
            self.Unit: UnitOfWeight = UnitOfWeight(data["Unit"])
        else:
            self.Unit: UnitOfWeight = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class ASINInboundGuidanceList(list, _List["ASINInboundGuidance"]):
    def __init__(self, data):
        super().__init__([ASINInboundGuidance(datum) for datum in data])
        self.data = data


class ASINPrepInstructionsList(list, _List["ASINPrepInstructions"]):
    def __init__(self, data):
        super().__init__([ASINPrepInstructions(datum) for datum in data])
        self.data = data


class AmazonPrepFeesDetailsList(list, _List["AmazonPrepFeesDetails"]):
    def __init__(self, data):
        super().__init__([AmazonPrepFeesDetails(datum) for datum in data])
        self.data = data


class GuidanceReasonList(list, _List["GuidanceReason"]):
    def __init__(self, data):
        super().__init__([GuidanceReason(datum) for datum in data])
        self.data = data


class InboundShipmentItemList(list, _List["InboundShipmentItem"]):
    def __init__(self, data):
        super().__init__([InboundShipmentItem(datum) for datum in data])
        self.data = data


class InboundShipmentList(list, _List["InboundShipmentInfo"]):
    def __init__(self, data):
        super().__init__([InboundShipmentInfo(datum) for datum in data])
        self.data = data


class InboundShipmentPlanItemList(list, _List["InboundShipmentPlanItem"]):
    def __init__(self, data):
        super().__init__([InboundShipmentPlanItem(datum) for datum in data])
        self.data = data


class InboundShipmentPlanList(list, _List["InboundShipmentPlan"]):
    def __init__(self, data):
        super().__init__([InboundShipmentPlan(datum) for datum in data])
        self.data = data


class InboundShipmentPlanRequestItemList(list, _List["InboundShipmentPlanRequestItem"]):
    def __init__(self, data):
        super().__init__([InboundShipmentPlanRequestItem(datum) for datum in data])
        self.data = data


class InvalidASINList(list, _List["InvalidASIN"]):
    def __init__(self, data):
        super().__init__([InvalidASIN(datum) for datum in data])
        self.data = data


class InvalidSKUList(list, _List["InvalidSKU"]):
    def __init__(self, data):
        super().__init__([InvalidSKU(datum) for datum in data])
        self.data = data


class NonPartneredSmallParcelPackageInputList(list, _List["NonPartneredSmallParcelPackageInput"]):
    def __init__(self, data):
        super().__init__([NonPartneredSmallParcelPackageInput(datum) for datum in data])
        self.data = data


class NonPartneredSmallParcelPackageOutputList(list, _List["NonPartneredSmallParcelPackageOutput"]):
    def __init__(self, data):
        super().__init__([NonPartneredSmallParcelPackageOutput(datum) for datum in data])
        self.data = data


class PalletList(list, _List["Pallet"]):
    def __init__(self, data):
        super().__init__([Pallet(datum) for datum in data])
        self.data = data


class PartneredSmallParcelPackageInputList(list, _List["PartneredSmallParcelPackageInput"]):
    def __init__(self, data):
        super().__init__([PartneredSmallParcelPackageInput(datum) for datum in data])
        self.data = data


class PartneredSmallParcelPackageOutputList(list, _List["PartneredSmallParcelPackageOutput"]):
    def __init__(self, data):
        super().__init__([PartneredSmallParcelPackageOutput(datum) for datum in data])
        self.data = data


class PrepDetailsList(list, _List["PrepDetails"]):
    def __init__(self, data):
        super().__init__([PrepDetails(datum) for datum in data])
        self.data = data


class PrepInstructionList(list, _List["PrepInstruction"]):
    def __init__(self, data):
        super().__init__([PrepInstruction(datum) for datum in data])
        self.data = data


class SKUInboundGuidanceList(list, _List["SKUInboundGuidance"]):
    def __init__(self, data):
        super().__init__([SKUInboundGuidance(datum) for datum in data])
        self.data = data


class SKUPrepInstructionsList(list, _List["SKUPrepInstructions"]):
    def __init__(self, data):
        super().__init__([SKUPrepInstructions(datum) for datum in data])
        self.data = data


BarcodeInstruction = str
BigDecimalType = float
BoxContentsSource = str
Condition = str
CurrencyCode = str
DateStringType = str
ErrorReason = str
GuidanceReason = str
InboundGuidance = str
IntendedBoxContentsSource = str
LabelPrepPreference = str
LabelPrepType = str
PackageStatus = str
PrepGuidance = str
PrepInstruction = str
PrepOwner = str
ProNumber = str
Quantity = int
SellerFreightClass = str
ShipmentStatus = str
ShipmentType = str
TimeStampStringType = str
TrackingId = str
TransportStatus = str
UnitOfMeasurement = str
UnitOfWeight = str
UnsignedIntType = int


class FulfillmentInboundClient(__BaseClient):
    def getInboundGuidance(
        self,
        MarketplaceId: str,
        SellerSKUList: _List[str] = None,
        ASINList: _List[str] = None,
    ):
        url = "/fba/inbound/v0/itemsGuidance".format()
        data = {}
        if MarketplaceId is not None:
            data["MarketplaceId"] = (MarketplaceId,)
        if SellerSKUList is not None:
            data["SellerSKUList"] = ",".join(map(str, SellerSKUList))
        if ASINList is not None:
            data["ASINList"] = ",".join(map(str, ASINList))
        response = self.request(url, method="GET", params=data)
        return {
            200: GetInboundGuidanceResponse,
            400: GetInboundGuidanceResponse,
            401: GetInboundGuidanceResponse,
            403: GetInboundGuidanceResponse,
            404: GetInboundGuidanceResponse,
            429: GetInboundGuidanceResponse,
            500: GetInboundGuidanceResponse,
            503: GetInboundGuidanceResponse,
        }[response.status_code](response.json())

    def createInboundShipmentPlan(
        self,
    ):
        url = "/fba/inbound/v0/plans".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: CreateInboundShipmentPlanResponse,
            400: CreateInboundShipmentPlanResponse,
            401: CreateInboundShipmentPlanResponse,
            403: CreateInboundShipmentPlanResponse,
            404: CreateInboundShipmentPlanResponse,
            429: CreateInboundShipmentPlanResponse,
            500: CreateInboundShipmentPlanResponse,
            503: CreateInboundShipmentPlanResponse,
        }[response.status_code](response.json())

    def updateInboundShipment(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
            200: InboundShipmentResponse,
            400: InboundShipmentResponse,
            401: InboundShipmentResponse,
            403: InboundShipmentResponse,
            404: InboundShipmentResponse,
            429: InboundShipmentResponse,
            500: InboundShipmentResponse,
            503: InboundShipmentResponse,
        }[response.status_code](response.json())

    def createInboundShipment(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: InboundShipmentResponse,
            400: InboundShipmentResponse,
            401: InboundShipmentResponse,
            403: InboundShipmentResponse,
            404: InboundShipmentResponse,
            429: InboundShipmentResponse,
            500: InboundShipmentResponse,
            503: InboundShipmentResponse,
        }[response.status_code](response.json())

    def getPreorderInfo(
        self,
        shipmentId: str,
        MarketplaceId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder".format(
            shipmentId=shipmentId,
        )
        data = {}
        if MarketplaceId is not None:
            data["MarketplaceId"] = (MarketplaceId,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetPreorderInfoResponse,
            400: GetPreorderInfoResponse,
            401: GetPreorderInfoResponse,
            403: GetPreorderInfoResponse,
            404: GetPreorderInfoResponse,
            429: GetPreorderInfoResponse,
            500: GetPreorderInfoResponse,
            503: GetPreorderInfoResponse,
        }[response.status_code](response.json())

    def confirmPreorder(
        self,
        shipmentId: str,
        NeedByDate: str,
        MarketplaceId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder/confirm".format(
            shipmentId=shipmentId,
        )
        data = {}
        if NeedByDate is not None:
            data["NeedByDate"] = (NeedByDate,)
        if MarketplaceId is not None:
            data["MarketplaceId"] = (MarketplaceId,)
        response = self.request(url, method="PUT", data=data)
        return {
            200: ConfirmPreorderResponse,
            400: ConfirmPreorderResponse,
            401: ConfirmPreorderResponse,
            403: ConfirmPreorderResponse,
            404: ConfirmPreorderResponse,
            429: ConfirmPreorderResponse,
            500: ConfirmPreorderResponse,
            503: ConfirmPreorderResponse,
        }[response.status_code](response.json())

    def getPrepInstructions(
        self,
        ShipToCountryCode: str,
        SellerSKUList: _List[str] = None,
        ASINList: _List[str] = None,
    ):
        url = "/fba/inbound/v0/prepInstructions".format()
        data = {}
        if ShipToCountryCode is not None:
            data["ShipToCountryCode"] = (ShipToCountryCode,)
        if SellerSKUList is not None:
            data["SellerSKUList"] = ",".join(map(str, SellerSKUList))
        if ASINList is not None:
            data["ASINList"] = ",".join(map(str, ASINList))
        response = self.request(url, method="GET", params=data)
        return {
            200: GetPrepInstructionsResponse,
            400: GetPrepInstructionsResponse,
            401: GetPrepInstructionsResponse,
            403: GetPrepInstructionsResponse,
            404: GetPrepInstructionsResponse,
            429: GetPrepInstructionsResponse,
            500: GetPrepInstructionsResponse,
            503: GetPrepInstructionsResponse,
        }[response.status_code](response.json())

    def getTransportDetails(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="GET", params=data)
        return {
            200: GetTransportDetailsResponse,
            400: GetTransportDetailsResponse,
            401: GetTransportDetailsResponse,
            403: GetTransportDetailsResponse,
            404: GetTransportDetailsResponse,
            429: GetTransportDetailsResponse,
            500: GetTransportDetailsResponse,
            503: GetTransportDetailsResponse,
        }[response.status_code](response.json())

    def putTransportDetails(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
            200: PutTransportDetailsResponse,
            400: PutTransportDetailsResponse,
            401: PutTransportDetailsResponse,
            403: PutTransportDetailsResponse,
            404: PutTransportDetailsResponse,
            429: PutTransportDetailsResponse,
            500: PutTransportDetailsResponse,
            503: PutTransportDetailsResponse,
        }[response.status_code](response.json())

    def voidTransport(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/void".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: VoidTransportResponse,
            400: VoidTransportResponse,
            401: VoidTransportResponse,
            403: VoidTransportResponse,
            404: VoidTransportResponse,
            429: VoidTransportResponse,
            500: VoidTransportResponse,
            503: VoidTransportResponse,
        }[response.status_code](response.json())

    def estimateTransport(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/estimate".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: EstimateTransportResponse,
            400: EstimateTransportResponse,
            401: EstimateTransportResponse,
            403: EstimateTransportResponse,
            404: EstimateTransportResponse,
            429: EstimateTransportResponse,
            500: EstimateTransportResponse,
            503: EstimateTransportResponse,
        }[response.status_code](response.json())

    def confirmTransport(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/confirm".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: ConfirmTransportResponse,
            400: ConfirmTransportResponse,
            401: ConfirmTransportResponse,
            403: ConfirmTransportResponse,
            404: ConfirmTransportResponse,
            429: ConfirmTransportResponse,
            500: ConfirmTransportResponse,
            503: ConfirmTransportResponse,
        }[response.status_code](response.json())

    def getLabels(
        self,
        shipmentId: str,
        PageType: str,
        LabelType: str,
        NumberOfPackages: int = None,
        PackageLabelsToPrint: _List[str] = None,
        NumberOfPallets: int = None,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/labels".format(
            shipmentId=shipmentId,
        )
        data = {}
        if PageType is not None:
            data["PageType"] = (PageType,)
        if LabelType is not None:
            data["LabelType"] = (LabelType,)
        if NumberOfPackages is not None:
            data["NumberOfPackages"] = (NumberOfPackages,)
        if PackageLabelsToPrint is not None:
            data["PackageLabelsToPrint"] = ",".join(map(str, PackageLabelsToPrint))
        if NumberOfPallets is not None:
            data["NumberOfPallets"] = (NumberOfPallets,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetLabelsResponse,
            400: GetLabelsResponse,
            401: GetLabelsResponse,
            403: GetLabelsResponse,
            404: GetLabelsResponse,
            429: GetLabelsResponse,
            500: GetLabelsResponse,
            503: GetLabelsResponse,
        }[response.status_code](response.json())

    def getBillOfLading(
        self,
        shipmentId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/billOfLading".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="GET", params=data)
        return {
            200: GetBillOfLadingResponse,
            400: GetBillOfLadingResponse,
            401: GetBillOfLadingResponse,
            403: GetBillOfLadingResponse,
            404: GetBillOfLadingResponse,
            429: GetBillOfLadingResponse,
            500: GetBillOfLadingResponse,
            503: GetBillOfLadingResponse,
        }[response.status_code](response.json())

    def getShipments(
        self,
        QueryType: str,
        MarketplaceId: str,
        ShipmentStatusList: _List[str] = None,
        ShipmentIdList: _List[str] = None,
        LastUpdatedAfter: str = None,
        LastUpdatedBefore: str = None,
        NextToken: str = None,
    ):
        url = "/fba/inbound/v0/shipments".format()
        data = {}
        if ShipmentStatusList is not None:
            data["ShipmentStatusList"] = ",".join(map(str, ShipmentStatusList))
        if ShipmentIdList is not None:
            data["ShipmentIdList"] = ",".join(map(str, ShipmentIdList))
        if LastUpdatedAfter is not None:
            data["LastUpdatedAfter"] = (LastUpdatedAfter,)
        if LastUpdatedBefore is not None:
            data["LastUpdatedBefore"] = (LastUpdatedBefore,)
        if QueryType is not None:
            data["QueryType"] = (QueryType,)
        if NextToken is not None:
            data["NextToken"] = (NextToken,)
        if MarketplaceId is not None:
            data["MarketplaceId"] = (MarketplaceId,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetShipmentsResponse,
            400: GetShipmentsResponse,
            401: GetShipmentsResponse,
            403: GetShipmentsResponse,
            404: GetShipmentsResponse,
            429: GetShipmentsResponse,
            500: GetShipmentsResponse,
            503: GetShipmentsResponse,
        }[response.status_code](response.json())

    def getShipmentItemsByShipmentId(
        self,
        shipmentId: str,
        MarketplaceId: str,
    ):
        url = "/fba/inbound/v0/shipments/{shipmentId}/items".format(
            shipmentId=shipmentId,
        )
        data = {}
        if MarketplaceId is not None:
            data["MarketplaceId"] = (MarketplaceId,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetShipmentItemsResponse,
            400: GetShipmentItemsResponse,
            401: GetShipmentItemsResponse,
            403: GetShipmentItemsResponse,
            404: GetShipmentItemsResponse,
            429: GetShipmentItemsResponse,
            500: GetShipmentItemsResponse,
            503: GetShipmentItemsResponse,
        }[response.status_code](response.json())

    def getShipmentItems(
        self,
        QueryType: str,
        MarketplaceId: str,
        LastUpdatedAfter: str = None,
        LastUpdatedBefore: str = None,
        NextToken: str = None,
    ):
        url = "/fba/inbound/v0/shipmentItems".format()
        data = {}
        if LastUpdatedAfter is not None:
            data["LastUpdatedAfter"] = (LastUpdatedAfter,)
        if LastUpdatedBefore is not None:
            data["LastUpdatedBefore"] = (LastUpdatedBefore,)
        if QueryType is not None:
            data["QueryType"] = (QueryType,)
        if NextToken is not None:
            data["NextToken"] = (NextToken,)
        if MarketplaceId is not None:
            data["MarketplaceId"] = (MarketplaceId,)
        response = self.request(url, method="GET", params=data)
        return {
            200: GetShipmentItemsResponse,
            400: GetShipmentItemsResponse,
            401: GetShipmentItemsResponse,
            403: GetShipmentItemsResponse,
            404: GetShipmentItemsResponse,
            429: GetShipmentItemsResponse,
            500: GetShipmentItemsResponse,
            503: GetShipmentItemsResponse,
        }[response.status_code](response.json())
