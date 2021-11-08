from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


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


class ASINInboundGuidance:
    """
    Reasons why a given ASIN is not recommended for shipment to Amazon's fulfillment network.
    """

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
    """
    Item preparation instructions to help with item sourcing decisions.
    """

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
    """ """

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
    """
    The fees for Amazon to prep goods for shipment.
    """

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
    """
    The monetary value.
    """

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
    """
    The manual processing fee per unit and total fee for a shipment.
    """

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
    """ """

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
    """
    The response schema for the confirmPreorder operation.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransportResult" in data:
            self.TransportResult: TransportResult = TransportResult(data["TransportResult"])
        else:
            self.TransportResult: TransportResult = None


class ConfirmTransportResponse:
    """
    The response schema for the confirmTransport operation.
    """

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
    """
    Contact information for the person in the seller's organization who is responsible for a Less Than Truckload/Full Truckload (LTL/FTL) shipment.
    """

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
    """
    The request schema for the createInboundShipmentPlan operation.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "InboundShipmentPlans" in data:
            self.InboundShipmentPlans: InboundShipmentPlanList = InboundShipmentPlanList(data["InboundShipmentPlans"])
        else:
            self.InboundShipmentPlans: InboundShipmentPlanList = None


class CreateInboundShipmentPlanResponse:
    """
    The response schema for the createInboundShipmentPlan operation.
    """

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
    """
    The request schema for an inbound shipment.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentId" in data:
            self.ShipmentId: str = str(data["ShipmentId"])
        else:
            self.ShipmentId: str = None


class InboundShipmentResponse:
    """
    The response schema for this operation.
    """

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
    """
    The dimension values and unit of measurement.
    """

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
    """
    The response schema for the estimateTransport operation.
    """

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
    """
    The response schema for the getBillOfLading operation.
    """

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
    """ """

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
    """
    The response schema for the getInboundGuidance operation.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DownloadURL" in data:
            self.DownloadURL: str = str(data["DownloadURL"])
        else:
            self.DownloadURL: str = None


class BillOfLadingDownloadURL:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DownloadURL" in data:
            self.DownloadURL: str = str(data["DownloadURL"])
        else:
            self.DownloadURL: str = None


class GetLabelsResponse:
    """
    The response schema for the getLabels operation.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentContainsPreorderableItems" in data:
            self.ShipmentContainsPreorderableItems: bool = convert_bool(data["ShipmentContainsPreorderableItems"])
        else:
            self.ShipmentContainsPreorderableItems: bool = None
        if "ShipmentConfirmedForPreorder" in data:
            self.ShipmentConfirmedForPreorder: bool = convert_bool(data["ShipmentConfirmedForPreorder"])
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
    """
    The response schema for the getPreorderInfo operation.
    """

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
    """ """

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
    """
    The response schema for the getPrepInstructions operation.
    """

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
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TransportContent" in data:
            self.TransportContent: TransportContent = TransportContent(data["TransportContent"])
        else:
            self.TransportContent: TransportContent = None


class GetTransportDetailsResponse:
    """
    The response schema for the getTransportDetails operation.
    """

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
    """
    Inbound shipment information used to create and update inbound shipments.
    """

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
            self.AreCasesRequired: bool = convert_bool(data["AreCasesRequired"])
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
    """
    Information about the seller's inbound shipments. Returned by the listInboundShipments operation.
    """

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
            self.AreCasesRequired: bool = convert_bool(data["AreCasesRequired"])
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
    """
    Item information for an inbound shipment. Submitted with a call to the createInboundShipment or updateInboundShipment operation.
    """

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
    """
    Inbound shipment information used to create an inbound shipment. Returned by the createInboundShipmentPlan operation.
    """

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
    """
    Item information used to create an inbound shipment. Returned by the createInboundShipmentPlan operation.
    """

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
    """
    Item information for creating an inbound shipment plan. Submitted with a call to the createInboundShipmentPlan operation.
    """

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
    """ """

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
    """ """

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
    """ """

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
    """
    The response schema for the getShipmentItems operation.
    """

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
    """ """

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
    """
    The response schema for the getShipments operation.
    """

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
    """
    Information that you provide to Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by a carrier that has not partnered with Amazon.
    """

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
    """
    Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment shipped by a carrier that has not partnered with Amazon.
    """

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
    """
    Information that you provide to Amazon about a Small Parcel shipment shipped by a carrier that has not partnered with Amazon.
    """

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
    """
    Information returned by Amazon about a Small Parcel shipment by a carrier that has not partnered with Amazon.
    """

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
    """
    The tracking number of the package, provided by the carrier.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "TrackingId" in data:
            self.TrackingId: TrackingId = TrackingId(data["TrackingId"])
        else:
            self.TrackingId: TrackingId = None


class NonPartneredSmallParcelPackageOutput:
    """
    Carrier, tracking number, and status information for the package.
    """

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
    """
    Pallet information.
    """

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
            self.IsStacked: bool = convert_bool(data["IsStacked"])
        else:
            self.IsStacked: bool = None


class PartneredEstimate:
    """
    The estimated shipping cost for a shipment using an Amazon-partnered carrier.
    """

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
    """
    Information that is required by an Amazon-partnered carrier to ship a Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.
    """

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
    """
    Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by an Amazon-partnered carrier.
    """

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
            self.IsBillOfLadingAvailable: bool = convert_bool(data["IsBillOfLadingAvailable"])
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
    """
    Information that is required by an Amazon-partnered carrier to ship a Small Parcel inbound shipment.
    """

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
    """
    Information returned by Amazon about a Small Parcel shipment by an Amazon-partnered carrier.
    """

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
    """
    Dimension and weight information for the package.
    """

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
    """
    Dimension, weight, and shipping information for the package.
    """

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
    """
    Preparation instructions and who is responsible for the preparation.
    """

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
    """
    The request schema for a putTransportDetails operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IsPartnered" in data:
            self.IsPartnered: bool = convert_bool(data["IsPartnered"])
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
    """
    Workflow status for a shipment with an Amazon-partnered carrier.
    """

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
    """
    Reasons why a given seller SKU is not recommended for shipment to Amazon's fulfillment network.
    """

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
    """
    Labeling requirements and item preparation instructions to help you prepare items for shipment to Amazon's fulfillment network.
    """

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
    """
    Inbound shipment information, including carrier details, shipment status, and the workflow status for a request for shipment with an Amazon-partnered carrier.
    """

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
    """
    Information required to create an Amazon-partnered carrier shipping estimate, or to alert the Amazon fulfillment center to the arrival of an inbound shipment by a non-Amazon-partnered carrier.
    """

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
    """
    Inbound shipment information, including carrier details and shipment status.
    """

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
    """
    The shipping identifier, information about whether the shipment is by an Amazon-partnered carrier, and information about whether the shipment is Small Parcel or Less Than Truckload/Full Truckload (LTL/FTL).
    """

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
            self.IsPartnered: bool = convert_bool(data["IsPartnered"])
        else:
            self.IsPartnered: bool = None
        if "ShipmentType" in data:
            self.ShipmentType: ShipmentType = ShipmentType(data["ShipmentType"])
        else:
            self.ShipmentType: ShipmentType = None


class TransportResult:
    """
    The workflow status for a shipment with an Amazon-partnered carrier.
    """

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
    """
    The response schema for the voidTransport operation.
    """

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
    """
    The weight of the package.
    """

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
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class ASINInboundGuidanceList(list, _List["ASINInboundGuidance"]):
    """
    A list of ASINs and their associated inbound guidance.
    """

    def __init__(self, data):
        super().__init__([ASINInboundGuidance(datum) for datum in data])
        self.data = data


class ASINPrepInstructionsList(list, _List["ASINPrepInstructions"]):
    """
    A list of item preparation instructions.
    """

    def __init__(self, data):
        super().__init__([ASINPrepInstructions(datum) for datum in data])
        self.data = data


class AmazonPrepFeesDetailsList(list, _List["AmazonPrepFeesDetails"]):
    """
    A list of preparation instructions and fees for Amazon to prep goods for shipment.
    """

    def __init__(self, data):
        super().__init__([AmazonPrepFeesDetails(datum) for datum in data])
        self.data = data


class GuidanceReasonList(list, _List["GuidanceReason"]):
    """
    A list of inbound guidance reason information.
    """

    def __init__(self, data):
        super().__init__([GuidanceReason(datum) for datum in data])
        self.data = data


class InboundShipmentItemList(list, _List["InboundShipmentItem"]):
    """
    A list of inbound shipment item information.
    """

    def __init__(self, data):
        super().__init__([InboundShipmentItem(datum) for datum in data])
        self.data = data


class InboundShipmentList(list, _List["InboundShipmentInfo"]):
    """
    A list of inbound shipment information.
    """

    def __init__(self, data):
        super().__init__([InboundShipmentInfo(datum) for datum in data])
        self.data = data


class InboundShipmentPlanItemList(list, _List["InboundShipmentPlanItem"]):
    """
    A list of inbound shipment plan item information.
    """

    def __init__(self, data):
        super().__init__([InboundShipmentPlanItem(datum) for datum in data])
        self.data = data


class InboundShipmentPlanList(list, _List["InboundShipmentPlan"]):
    """
    A list of inbound shipment plan information
    """

    def __init__(self, data):
        super().__init__([InboundShipmentPlan(datum) for datum in data])
        self.data = data


class InboundShipmentPlanRequestItemList(list, _List["InboundShipmentPlanRequestItem"]):
    """ """

    def __init__(self, data):
        super().__init__([InboundShipmentPlanRequestItem(datum) for datum in data])
        self.data = data


class InvalidASINList(list, _List["InvalidASIN"]):
    """
    A list of invalid ASIN values and the reasons they are invalid.
    """

    def __init__(self, data):
        super().__init__([InvalidASIN(datum) for datum in data])
        self.data = data


class InvalidSKUList(list, _List["InvalidSKU"]):
    """
    A list of invalid SKU values and the reason they are invalid.
    """

    def __init__(self, data):
        super().__init__([InvalidSKU(datum) for datum in data])
        self.data = data


class NonPartneredSmallParcelPackageInputList(list, _List["NonPartneredSmallParcelPackageInput"]):
    """
    A list of package tracking information.
    """

    def __init__(self, data):
        super().__init__([NonPartneredSmallParcelPackageInput(datum) for datum in data])
        self.data = data


class NonPartneredSmallParcelPackageOutputList(list, _List["NonPartneredSmallParcelPackageOutput"]):
    """
    A list of packages, including carrier, tracking number, and status information for each package.
    """

    def __init__(self, data):
        super().__init__([NonPartneredSmallParcelPackageOutput(datum) for datum in data])
        self.data = data


class PalletList(list, _List["Pallet"]):
    """
    A list of pallet information.
    """

    def __init__(self, data):
        super().__init__([Pallet(datum) for datum in data])
        self.data = data


class PartneredSmallParcelPackageInputList(list, _List["PartneredSmallParcelPackageInput"]):
    """
    A list of dimensions and weight information for packages.
    """

    def __init__(self, data):
        super().__init__([PartneredSmallParcelPackageInput(datum) for datum in data])
        self.data = data


class PartneredSmallParcelPackageOutputList(list, _List["PartneredSmallParcelPackageOutput"]):
    """
    A list of packages, including shipping information from the Amazon-partnered carrier.
    """

    def __init__(self, data):
        super().__init__([PartneredSmallParcelPackageOutput(datum) for datum in data])
        self.data = data


class PrepDetailsList(list, _List["PrepDetails"]):
    """
    A list of preparation instructions and who is responsible for that preparation.
    """

    def __init__(self, data):
        super().__init__([PrepDetails(datum) for datum in data])
        self.data = data


class PrepInstructionList(list, _List["PrepInstruction"]):
    """
    A list of preparation instructions to help with item sourcing decisions.
    """

    def __init__(self, data):
        super().__init__([PrepInstruction(datum) for datum in data])
        self.data = data


class SKUInboundGuidanceList(list, _List["SKUInboundGuidance"]):
    """
    A list of SKU inbound guidance information.
    """

    def __init__(self, data):
        super().__init__([SKUInboundGuidance(datum) for datum in data])
        self.data = data


class SKUPrepInstructionsList(list, _List["SKUPrepInstructions"]):
    """
    A list of SKU labeling requirements and item preparation instructions.
    """

    def __init__(self, data):
        super().__init__([SKUPrepInstructions(datum) for datum in data])
        self.data = data


class BarcodeInstruction(str):
    """
    Labeling requirements for the item. For more information about FBA labeling requirements, see the Seller Central Help for your marketplace.
    """


class BigDecimalType(float):
    """ """


class BoxContentsSource(str):
    """
    Where the seller provided box contents information for a shipment.
    """


class Condition(str):
    """
    The condition of the item.
    """


class CurrencyCode(str):
    """
    The currency code.
    """


class DateStringType(str):
    """ """


class ErrorReason(str):
    """
    The reason that the ASIN is invalid.
    """


class GuidanceReason(str):
    """
    A reason for the current inbound guidance for an item.
    """


class InboundGuidance(str):
    """
    Specific inbound guidance for an item.
    """


class IntendedBoxContentsSource(str):
    """
    How the seller intends to provide box contents information for a shipment.
    """


class LabelPrepPreference(str):
    """
    The preference for label preparation for an inbound shipment.
    """


class LabelPrepType(str):
    """
    The type of label preparation that is required for the inbound shipment.
    """


class PackageStatus(str):
    """
    The shipment status of the package.
    """


class PrepGuidance(str):
    """
    Item preparation instructions.
    """


class PrepInstruction(str):
    """
    Preparation instructions for shipping an item to Amazon's fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network, see the Seller Central Help for your marketplace.
    """


class PrepOwner(str):
    """
    Indicates who will prepare the item.
    """


class ProNumber(str):
    """
    The PRO number ("progressive number" or "progressive ID") assigned to the shipment by the carrier.
    """


class Quantity(int):
    """
    The item quantity.
    """


class SellerFreightClass(str):
    """
    The freight class of the shipment. For information about determining the freight class, contact the carrier.
    """


class ShipmentStatus(str):
    """
    Indicates the status of the inbound shipment. When used with the createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment operation, possible values are WORKING, SHIPPED or CANCELLED.
    """


class ShipmentType(str):
    """
    Specifies the carrier shipment type in a putTransportDetails request.
    """


class TimeStampStringType(str):
    """ """


class TrackingId(str):
    """
    The tracking number of the package, provided by the carrier.
    """


class TransportStatus(str):
    """
    Indicates the status of the Amazon-partnered carrier shipment.
    """


class UnitOfMeasurement(str):
    """
    Indicates the unit of measurement.
    """


class UnitOfWeight(str):
    """
    Indicates the unit of weight.
    """


class UnsignedIntType(int):
    """ """


class FulfillmentInboundV0Client(__BaseClient):
    def getInboundGuidance(
        self,
        MarketplaceId: str,
        SellerSKUList: _List[str] = None,
        ASINList: _List[str] = None,
    ):
        """
                Returns information that lets a seller know if Amazon recommends sending an item to a given marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not recommended, at their discretion.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/itemsGuidance".format()
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if SellerSKUList is not None:
            params["SellerSKUList"] = ",".join(map(str, SellerSKUList))
        if ASINList is not None:
            params["ASINList"] = ",".join(map(str, ASINList))
        response = self.request(url, method="GET", params=params)
        return {
            200: GetInboundGuidanceResponse,
            400: GetInboundGuidanceResponse,
            401: GetInboundGuidanceResponse,
            403: GetInboundGuidanceResponse,
            404: GetInboundGuidanceResponse,
            429: GetInboundGuidanceResponse,
            500: GetInboundGuidanceResponse,
            503: GetInboundGuidanceResponse,
        }[response.status_code](self._get_response_json(response))

    def createInboundShipmentPlan(
        self,
        data: CreateInboundShipmentPlanRequest,
    ):
        """
                Returns one or more inbound shipment plans, which provide the information you need to create one or more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be required so that items can be optimally placed in Amazon's fulfillment network—for example, positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be created with the same Amazon fulfillment center destination if the two shipment plans require different processing—for example, items that require labels must be shipped separately from stickerless, commingled inventory.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/plans".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: CreateInboundShipmentPlanResponse,
            400: CreateInboundShipmentPlanResponse,
            401: CreateInboundShipmentPlanResponse,
            403: CreateInboundShipmentPlanResponse,
            404: CreateInboundShipmentPlanResponse,
            429: CreateInboundShipmentPlanResponse,
            500: CreateInboundShipmentPlanResponse,
            503: CreateInboundShipmentPlanResponse,
        }[response.status_code](self._get_response_json(response))

    def updateInboundShipment(
        self,
        shipmentId: str,
    ):
        """
                Updates or removes items from the inbound shipment identified by the specified shipment identifier. Adding new items is not supported.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="PUT", data=params)
        return {
            200: InboundShipmentResponse,
            400: InboundShipmentResponse,
            401: InboundShipmentResponse,
            403: InboundShipmentResponse,
            404: InboundShipmentResponse,
            429: InboundShipmentResponse,
            500: InboundShipmentResponse,
            503: InboundShipmentResponse,
        }[response.status_code](self._get_response_json(response))

    def createInboundShipment(
        self,
        data: InboundShipmentRequest,
        shipmentId: str,
    ):
        """
                Returns a new inbound shipment based on the specified shipmentId that was returned by the createInboundShipmentPlan operation.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: InboundShipmentResponse,
            400: InboundShipmentResponse,
            401: InboundShipmentResponse,
            403: InboundShipmentResponse,
            404: InboundShipmentResponse,
            429: InboundShipmentResponse,
            500: InboundShipmentResponse,
            503: InboundShipmentResponse,
        }[response.status_code](self._get_response_json(response))

    def getPreorderInfo(
        self,
        shipmentId: str,
        MarketplaceId: str,
    ):
        """
                Returns pre-order information, including dates, that a seller needs before confirming a shipment for pre-order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder".format(
            shipmentId=shipmentId,
        )
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPreorderInfoResponse,
            400: GetPreorderInfoResponse,
            401: GetPreorderInfoResponse,
            403: GetPreorderInfoResponse,
            404: GetPreorderInfoResponse,
            429: GetPreorderInfoResponse,
            500: GetPreorderInfoResponse,
            503: GetPreorderInfoResponse,
        }[response.status_code](self._get_response_json(response))

    def confirmPreorder(
        self,
        shipmentId: str,
        NeedByDate: str,
        MarketplaceId: str,
    ):
        """
                Returns information needed to confirm a shipment for pre-order. Call this operation after calling the getPreorderInfo operation to get the NeedByDate value and other pre-order information about the shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder/confirm".format(
            shipmentId=shipmentId,
        )
        params = {}
        if NeedByDate is not None:
            params["NeedByDate"] = NeedByDate
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        response = self.request(url, method="PUT", data=params)
        return {
            200: ConfirmPreorderResponse,
            400: ConfirmPreorderResponse,
            401: ConfirmPreorderResponse,
            403: ConfirmPreorderResponse,
            404: ConfirmPreorderResponse,
            429: ConfirmPreorderResponse,
            500: ConfirmPreorderResponse,
            503: ConfirmPreorderResponse,
        }[response.status_code](self._get_response_json(response))

    def getPrepInstructions(
        self,
        ShipToCountryCode: str,
        SellerSKUList: _List[str] = None,
        ASINList: _List[str] = None,
    ):
        """
                Returns labeling requirements and item preparation instructions to help prepare items for shipment to Amazon's fulfillment network.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/prepInstructions".format()
        params = {}
        if ShipToCountryCode is not None:
            params["ShipToCountryCode"] = ShipToCountryCode
        if SellerSKUList is not None:
            params["SellerSKUList"] = ",".join(map(str, SellerSKUList))
        if ASINList is not None:
            params["ASINList"] = ",".join(map(str, ASINList))
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPrepInstructionsResponse,
            400: GetPrepInstructionsResponse,
            401: GetPrepInstructionsResponse,
            403: GetPrepInstructionsResponse,
            404: GetPrepInstructionsResponse,
            429: GetPrepInstructionsResponse,
            500: GetPrepInstructionsResponse,
            503: GetPrepInstructionsResponse,
        }[response.status_code](self._get_response_json(response))

    def getTransportDetails(
        self,
        shipmentId: str,
    ):
        """
                Returns current transportation information about an inbound shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetTransportDetailsResponse,
            400: GetTransportDetailsResponse,
            401: GetTransportDetailsResponse,
            403: GetTransportDetailsResponse,
            404: GetTransportDetailsResponse,
            429: GetTransportDetailsResponse,
            500: GetTransportDetailsResponse,
            503: GetTransportDetailsResponse,
        }[response.status_code](self._get_response_json(response))

    def putTransportDetails(
        self,
        shipmentId: str,
    ):
        """
                Sends transportation information to Amazon about an inbound shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="PUT", data=params)
        return {
            200: PutTransportDetailsResponse,
            400: PutTransportDetailsResponse,
            401: PutTransportDetailsResponse,
            403: PutTransportDetailsResponse,
            404: PutTransportDetailsResponse,
            429: PutTransportDetailsResponse,
            500: PutTransportDetailsResponse,
            503: PutTransportDetailsResponse,
        }[response.status_code](self._get_response_json(response))

    def voidTransport(
        self,
        shipmentId: str,
    ):
        """
                Cancels a previously-confirmed request to ship an inbound shipment using an Amazon-partnered carrier.
        To be successful, you must call this operation before the VoidDeadline date that is returned by the getTransportDetails operation.
        Important: The VoidDeadline date is 24 hours after you confirm a Small Parcel shipment transportation request or one hour after you confirm a Less Than Truckload/Full Truckload (LTL/FTL) shipment transportation request. After the void deadline passes, your account will be charged for the shipping cost.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/void".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: VoidTransportResponse,
            400: VoidTransportResponse,
            401: VoidTransportResponse,
            403: VoidTransportResponse,
            404: VoidTransportResponse,
            429: VoidTransportResponse,
            500: VoidTransportResponse,
            503: VoidTransportResponse,
        }[response.status_code](self._get_response_json(response))

    def estimateTransport(
        self,
        shipmentId: str,
    ):
        """
                Initiates the process of estimating the shipping cost for an inbound shipment by an Amazon-partnered carrier.
        Prior to calling the estimateTransport operation, you must call the putTransportDetails operation to provide Amazon with the transportation information for the inbound shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/estimate".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: EstimateTransportResponse,
            400: EstimateTransportResponse,
            401: EstimateTransportResponse,
            403: EstimateTransportResponse,
            404: EstimateTransportResponse,
            429: EstimateTransportResponse,
            500: EstimateTransportResponse,
            503: EstimateTransportResponse,
        }[response.status_code](self._get_response_json(response))

    def confirmTransport(
        self,
        shipmentId: str,
    ):
        """
                Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the inbound shipment.
        Prior to calling the confirmTransport operation, you should call the getTransportDetails operation to get the Amazon-partnered shipping estimate.
        Important: After confirming the transportation request, if the seller decides that they do not want the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours after confirming a transportation request to void the transportation request. For a Less Than Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a transportation request to void it. After the grace period has expired the seller's account will be charged for the shipping cost.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/confirm".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            200: ConfirmTransportResponse,
            400: ConfirmTransportResponse,
            401: ConfirmTransportResponse,
            403: ConfirmTransportResponse,
            404: ConfirmTransportResponse,
            429: ConfirmTransportResponse,
            500: ConfirmTransportResponse,
            503: ConfirmTransportResponse,
        }[response.status_code](self._get_response_json(response))

    def getLabels(
        self,
        shipmentId: str,
        PageType: str,
        LabelType: str,
        NumberOfPackages: int = None,
        PackageLabelsToPrint: _List[str] = None,
        NumberOfPallets: int = None,
        PageSize: int = None,
        PageStartIndex: int = None,
    ):
        """
                Returns package/pallet labels for faster and more accurate shipment processing at the Amazon fulfillment center.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/labels".format(
            shipmentId=shipmentId,
        )
        params = {}
        if PageType is not None:
            params["PageType"] = PageType
        if LabelType is not None:
            params["LabelType"] = LabelType
        if NumberOfPackages is not None:
            params["NumberOfPackages"] = NumberOfPackages
        if PackageLabelsToPrint is not None:
            params["PackageLabelsToPrint"] = ",".join(map(str, PackageLabelsToPrint))
        if NumberOfPallets is not None:
            params["NumberOfPallets"] = NumberOfPallets
        if PageSize is not None:
            params["PageSize"] = PageSize
        if PageStartIndex is not None:
            params["PageStartIndex"] = PageStartIndex
        response = self.request(url, method="GET", params=params)
        return {
            200: GetLabelsResponse,
            400: GetLabelsResponse,
            401: GetLabelsResponse,
            403: GetLabelsResponse,
            404: GetLabelsResponse,
            429: GetLabelsResponse,
            500: GetLabelsResponse,
            503: GetLabelsResponse,
        }[response.status_code](self._get_response_json(response))

    def getBillOfLading(
        self,
        shipmentId: str,
    ):
        """
                Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/billOfLading".format(
            shipmentId=shipmentId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetBillOfLadingResponse,
            400: GetBillOfLadingResponse,
            401: GetBillOfLadingResponse,
            403: GetBillOfLadingResponse,
            404: GetBillOfLadingResponse,
            429: GetBillOfLadingResponse,
            500: GetBillOfLadingResponse,
            503: GetBillOfLadingResponse,
        }[response.status_code](self._get_response_json(response))

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
        """
                Returns a list of inbound shipments based on criteria that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments".format()
        params = {}
        if ShipmentStatusList is not None:
            params["ShipmentStatusList"] = ",".join(map(str, ShipmentStatusList))
        if ShipmentIdList is not None:
            params["ShipmentIdList"] = ",".join(map(str, ShipmentIdList))
        if LastUpdatedAfter is not None:
            params["LastUpdatedAfter"] = LastUpdatedAfter
        if LastUpdatedBefore is not None:
            params["LastUpdatedBefore"] = LastUpdatedBefore
        if QueryType is not None:
            params["QueryType"] = QueryType
        if NextToken is not None:
            params["NextToken"] = NextToken
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShipmentsResponse,
            400: GetShipmentsResponse,
            401: GetShipmentsResponse,
            403: GetShipmentsResponse,
            404: GetShipmentsResponse,
            429: GetShipmentsResponse,
            500: GetShipmentsResponse,
            503: GetShipmentsResponse,
        }[response.status_code](self._get_response_json(response))

    def getShipmentItemsByShipmentId(
        self,
        shipmentId: str,
        MarketplaceId: str,
    ):
        """
                Returns a list of items in a specified inbound shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/items".format(
            shipmentId=shipmentId,
        )
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShipmentItemsResponse,
            400: GetShipmentItemsResponse,
            401: GetShipmentItemsResponse,
            403: GetShipmentItemsResponse,
            404: GetShipmentItemsResponse,
            429: GetShipmentItemsResponse,
            500: GetShipmentItemsResponse,
            503: GetShipmentItemsResponse,
        }[response.status_code](self._get_response_json(response))

    def getShipmentItems(
        self,
        QueryType: str,
        MarketplaceId: str,
        LastUpdatedAfter: str = None,
        LastUpdatedBefore: str = None,
        NextToken: str = None,
    ):
        """
                Returns a list of items in a specified inbound shipment, or a list of items that were updated within a specified time frame.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/fba/inbound/v0/shipmentItems".format()
        params = {}
        if LastUpdatedAfter is not None:
            params["LastUpdatedAfter"] = LastUpdatedAfter
        if LastUpdatedBefore is not None:
            params["LastUpdatedBefore"] = LastUpdatedBefore
        if QueryType is not None:
            params["QueryType"] = QueryType
        if NextToken is not None:
            params["NextToken"] = NextToken
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetShipmentItemsResponse,
            400: GetShipmentItemsResponse,
            401: GetShipmentItemsResponse,
            403: GetShipmentItemsResponse,
            404: GetShipmentItemsResponse,
            429: GetShipmentItemsResponse,
            500: GetShipmentItemsResponse,
            503: GetShipmentItemsResponse,
        }[response.status_code](self._get_response_json(response))
