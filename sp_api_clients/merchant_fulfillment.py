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


class LabelFormatOptionRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IncludePackingSlipWithLabel" in data:
            self.IncludePackingSlipWithLabel: bool = bool(data["IncludePackingSlipWithLabel"])
        else:
            self.IncludePackingSlipWithLabel: bool = None


class LabelFormatOption:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IncludePackingSlipWithLabel" in data:
            self.IncludePackingSlipWithLabel: bool = bool(data["IncludePackingSlipWithLabel"])
        else:
            self.IncludePackingSlipWithLabel: bool = None
        if "LabelFormat" in data:
            self.LabelFormat: LabelFormat = LabelFormat(data["LabelFormat"])
        else:
            self.LabelFormat: LabelFormat = None


class AvailableCarrierWillPickUpOption:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierWillPickUpOption" in data:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = CarrierWillPickUpOption(
                data["CarrierWillPickUpOption"]
            )
        else:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = None
        if "Charge" in data:
            self.Charge: CurrencyAmount = CurrencyAmount(data["Charge"])
        else:
            self.Charge: CurrencyAmount = None


class AvailableDeliveryExperienceOption:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DeliveryExperienceOption" in data:
            self.DeliveryExperienceOption: DeliveryExperienceOption = DeliveryExperienceOption(
                data["DeliveryExperienceOption"]
            )
        else:
            self.DeliveryExperienceOption: DeliveryExperienceOption = None
        if "Charge" in data:
            self.Charge: CurrencyAmount = CurrencyAmount(data["Charge"])
        else:
            self.Charge: CurrencyAmount = None


class AvailableShippingServiceOptions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AvailableCarrierWillPickUpOptions" in data:
            self.AvailableCarrierWillPickUpOptions: AvailableCarrierWillPickUpOptionsList = (
                AvailableCarrierWillPickUpOptionsList(data["AvailableCarrierWillPickUpOptions"])
            )
        else:
            self.AvailableCarrierWillPickUpOptions: AvailableCarrierWillPickUpOptionsList = None
        if "AvailableDeliveryExperienceOptions" in data:
            self.AvailableDeliveryExperienceOptions: AvailableDeliveryExperienceOptionsList = (
                AvailableDeliveryExperienceOptionsList(data["AvailableDeliveryExperienceOptions"])
            )
        else:
            self.AvailableDeliveryExperienceOptions: AvailableDeliveryExperienceOptionsList = None


class Constraint:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ValidationRegEx" in data:
            self.ValidationRegEx: str = str(data["ValidationRegEx"])
        else:
            self.ValidationRegEx: str = None
        if "ValidationString" in data:
            self.ValidationString: str = str(data["ValidationString"])
        else:
            self.ValidationString: str = None


class AdditionalInputs:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AdditionalInputFieldName" in data:
            self.AdditionalInputFieldName: str = str(data["AdditionalInputFieldName"])
        else:
            self.AdditionalInputFieldName: str = None
        if "SellerInputDefinition" in data:
            self.SellerInputDefinition: SellerInputDefinition = SellerInputDefinition(data["SellerInputDefinition"])
        else:
            self.SellerInputDefinition: SellerInputDefinition = None


class SellerInputDefinition:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IsRequired" in data:
            self.IsRequired: bool = bool(data["IsRequired"])
        else:
            self.IsRequired: bool = None
        if "DataType" in data:
            self.DataType: str = str(data["DataType"])
        else:
            self.DataType: str = None
        if "Constraints" in data:
            self.Constraints: Constraints = Constraints(data["Constraints"])
        else:
            self.Constraints: Constraints = None
        if "InputDisplayText" in data:
            self.InputDisplayText: str = str(data["InputDisplayText"])
        else:
            self.InputDisplayText: str = None
        if "InputTarget" in data:
            self.InputTarget: InputTargetType = InputTargetType(data["InputTarget"])
        else:
            self.InputTarget: InputTargetType = None
        if "StoredValue" in data:
            self.StoredValue: AdditionalSellerInput = AdditionalSellerInput(data["StoredValue"])
        else:
            self.StoredValue: AdditionalSellerInput = None
        if "RestrictedSetValues" in data:
            self.RestrictedSetValues: RestrictedSetValues = RestrictedSetValues(data["RestrictedSetValues"])
        else:
            self.RestrictedSetValues: RestrictedSetValues = None


class AdditionalSellerInput:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DataType" in data:
            self.DataType: str = str(data["DataType"])
        else:
            self.DataType: str = None
        if "ValueAsString" in data:
            self.ValueAsString: str = str(data["ValueAsString"])
        else:
            self.ValueAsString: str = None
        if "ValueAsBoolean" in data:
            self.ValueAsBoolean: bool = bool(data["ValueAsBoolean"])
        else:
            self.ValueAsBoolean: bool = None
        if "ValueAsInteger" in data:
            self.ValueAsInteger: int = int(data["ValueAsInteger"])
        else:
            self.ValueAsInteger: int = None
        if "ValueAsTimestamp" in data:
            self.ValueAsTimestamp: Timestamp = Timestamp(data["ValueAsTimestamp"])
        else:
            self.ValueAsTimestamp: Timestamp = None
        if "ValueAsAddress" in data:
            self.ValueAsAddress: Address = Address(data["ValueAsAddress"])
        else:
            self.ValueAsAddress: Address = None
        if "ValueAsWeight" in data:
            self.ValueAsWeight: Weight = Weight(data["ValueAsWeight"])
        else:
            self.ValueAsWeight: Weight = None
        if "ValueAsDimension" in data:
            self.ValueAsDimension: Length = Length(data["ValueAsDimension"])
        else:
            self.ValueAsDimension: Length = None
        if "ValueAsCurrency" in data:
            self.ValueAsCurrency: CurrencyAmount = CurrencyAmount(data["ValueAsCurrency"])
        else:
            self.ValueAsCurrency: CurrencyAmount = None


class AdditionalSellerInputs:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AdditionalInputFieldName" in data:
            self.AdditionalInputFieldName: str = str(data["AdditionalInputFieldName"])
        else:
            self.AdditionalInputFieldName: str = None
        if "AdditionalSellerInput" in data:
            self.AdditionalSellerInput: AdditionalSellerInput = AdditionalSellerInput(data["AdditionalSellerInput"])
        else:
            self.AdditionalSellerInput: AdditionalSellerInput = None


class Address:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Name" in data:
            self.Name: AddressName = AddressName(data["Name"])
        else:
            self.Name: AddressName = None
        if "AddressLine1" in data:
            self.AddressLine1: AddressLine1 = AddressLine1(data["AddressLine1"])
        else:
            self.AddressLine1: AddressLine1 = None
        if "AddressLine2" in data:
            self.AddressLine2: AddressLine2 = AddressLine2(data["AddressLine2"])
        else:
            self.AddressLine2: AddressLine2 = None
        if "AddressLine3" in data:
            self.AddressLine3: AddressLine3 = AddressLine3(data["AddressLine3"])
        else:
            self.AddressLine3: AddressLine3 = None
        if "DistrictOrCounty" in data:
            self.DistrictOrCounty: DistrictOrCounty = DistrictOrCounty(data["DistrictOrCounty"])
        else:
            self.DistrictOrCounty: DistrictOrCounty = None
        if "Email" in data:
            self.Email: EmailAddress = EmailAddress(data["Email"])
        else:
            self.Email: EmailAddress = None
        if "City" in data:
            self.City: City = City(data["City"])
        else:
            self.City: City = None
        if "StateOrProvinceCode" in data:
            self.StateOrProvinceCode: StateOrProvinceCode = StateOrProvinceCode(data["StateOrProvinceCode"])
        else:
            self.StateOrProvinceCode: StateOrProvinceCode = None
        if "PostalCode" in data:
            self.PostalCode: PostalCode = PostalCode(data["PostalCode"])
        else:
            self.PostalCode: PostalCode = None
        if "CountryCode" in data:
            self.CountryCode: CountryCode = CountryCode(data["CountryCode"])
        else:
            self.CountryCode: CountryCode = None
        if "Phone" in data:
            self.Phone: PhoneNumber = PhoneNumber(data["Phone"])
        else:
            self.Phone: PhoneNumber = None


class CancelShipmentResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Shipment = Shipment(data["payload"])
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateShipmentRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentRequestDetails" in data:
            self.ShipmentRequestDetails: ShipmentRequestDetails = ShipmentRequestDetails(data["ShipmentRequestDetails"])
        else:
            self.ShipmentRequestDetails: ShipmentRequestDetails = None
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = ShippingServiceIdentifier(data["ShippingServiceId"])
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "ShippingServiceOfferId" in data:
            self.ShippingServiceOfferId: str = str(data["ShippingServiceOfferId"])
        else:
            self.ShippingServiceOfferId: str = None
        if "HazmatType" in data:
            self.HazmatType: HazmatType = HazmatType(data["HazmatType"])
        else:
            self.HazmatType: HazmatType = None
        if "LabelFormatOption" in data:
            self.LabelFormatOption: LabelFormatOptionRequest = LabelFormatOptionRequest(data["LabelFormatOption"])
        else:
            self.LabelFormatOption: LabelFormatOptionRequest = None
        if "ShipmentLevelSellerInputsList" in data:
            self.ShipmentLevelSellerInputsList: AdditionalSellerInputsList = AdditionalSellerInputsList(
                data["ShipmentLevelSellerInputsList"]
            )
        else:
            self.ShipmentLevelSellerInputsList: AdditionalSellerInputsList = None


class CreateShipmentResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Shipment = Shipment(data["payload"])
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ItemLevelFields:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Asin" in data:
            self.Asin: str = str(data["Asin"])
        else:
            self.Asin: str = None
        if "AdditionalInputs" in data:
            self.AdditionalInputs: AdditionalInputsList = AdditionalInputsList(data["AdditionalInputs"])
        else:
            self.AdditionalInputs: AdditionalInputsList = None


class GetAdditionalSellerInputsRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = ShippingServiceIdentifier(data["ShippingServiceId"])
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = Address(data["ShipFromAddress"])
        else:
            self.ShipFromAddress: Address = None
        if "OrderId" in data:
            self.OrderId: AmazonOrderId = AmazonOrderId(data["OrderId"])
        else:
            self.OrderId: AmazonOrderId = None


class GetAdditionalSellerInputsResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentLevelFields" in data:
            self.ShipmentLevelFields: AdditionalInputsList = AdditionalInputsList(data["ShipmentLevelFields"])
        else:
            self.ShipmentLevelFields: AdditionalInputsList = None
        if "ItemLevelFieldsList" in data:
            self.ItemLevelFieldsList: ItemLevelFieldsList = ItemLevelFieldsList(data["ItemLevelFieldsList"])
        else:
            self.ItemLevelFieldsList: ItemLevelFieldsList = None


class GetAdditionalSellerInputsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetAdditionalSellerInputsResult = GetAdditionalSellerInputsResult(data["payload"])
        else:
            self.payload: GetAdditionalSellerInputsResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CurrencyAmount:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: float = float(data["Amount"])
        else:
            self.Amount: float = None


class FileContents:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Contents" in data:
            self.Contents: str = str(data["Contents"])
        else:
            self.Contents: str = None
        if "FileType" in data:
            self.FileType: FileType = FileType(data["FileType"])
        else:
            self.FileType: FileType = None
        if "Checksum" in data:
            self.Checksum: str = str(data["Checksum"])
        else:
            self.Checksum: str = None


class GetEligibleShipmentServicesRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentRequestDetails" in data:
            self.ShipmentRequestDetails: ShipmentRequestDetails = ShipmentRequestDetails(data["ShipmentRequestDetails"])
        else:
            self.ShipmentRequestDetails: ShipmentRequestDetails = None
        if "ShippingOfferingFilter" in data:
            self.ShippingOfferingFilter: ShippingOfferingFilter = ShippingOfferingFilter(data["ShippingOfferingFilter"])
        else:
            self.ShippingOfferingFilter: ShippingOfferingFilter = None


class GetEligibleShipmentServicesResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: GetEligibleShipmentServicesResult = GetEligibleShipmentServicesResult(data["payload"])
        else:
            self.payload: GetEligibleShipmentServicesResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetEligibleShipmentServicesResult:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShippingServiceList" in data:
            self.ShippingServiceList: ShippingServiceList = ShippingServiceList(data["ShippingServiceList"])
        else:
            self.ShippingServiceList: ShippingServiceList = None
        if "RejectedShippingServiceList" in data:
            self.RejectedShippingServiceList: RejectedShippingServiceList = RejectedShippingServiceList(
                data["RejectedShippingServiceList"]
            )
        else:
            self.RejectedShippingServiceList: RejectedShippingServiceList = None
        if "TemporarilyUnavailableCarrierList" in data:
            self.TemporarilyUnavailableCarrierList: TemporarilyUnavailableCarrierList = (
                TemporarilyUnavailableCarrierList(data["TemporarilyUnavailableCarrierList"])
            )
        else:
            self.TemporarilyUnavailableCarrierList: TemporarilyUnavailableCarrierList = None
        if "TermsAndConditionsNotAcceptedCarrierList" in data:
            self.TermsAndConditionsNotAcceptedCarrierList: TermsAndConditionsNotAcceptedCarrierList = (
                TermsAndConditionsNotAcceptedCarrierList(data["TermsAndConditionsNotAcceptedCarrierList"])
            )
        else:
            self.TermsAndConditionsNotAcceptedCarrierList: TermsAndConditionsNotAcceptedCarrierList = None


class GetShipmentResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Shipment = Shipment(data["payload"])
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Item:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "OrderItemId" in data:
            self.OrderItemId: OrderItemId = OrderItemId(data["OrderItemId"])
        else:
            self.OrderItemId: OrderItemId = None
        if "Quantity" in data:
            self.Quantity: ItemQuantity = ItemQuantity(data["Quantity"])
        else:
            self.Quantity: ItemQuantity = None
        if "ItemWeight" in data:
            self.ItemWeight: Weight = Weight(data["ItemWeight"])
        else:
            self.ItemWeight: Weight = None
        if "ItemDescription" in data:
            self.ItemDescription: ItemDescription = ItemDescription(data["ItemDescription"])
        else:
            self.ItemDescription: ItemDescription = None
        if "TransparencyCodeList" in data:
            self.TransparencyCodeList: TransparencyCodeList = TransparencyCodeList(data["TransparencyCodeList"])
        else:
            self.TransparencyCodeList: TransparencyCodeList = None
        if "ItemLevelSellerInputsList" in data:
            self.ItemLevelSellerInputsList: AdditionalSellerInputsList = AdditionalSellerInputsList(
                data["ItemLevelSellerInputsList"]
            )
        else:
            self.ItemLevelSellerInputsList: AdditionalSellerInputsList = None


class Label:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CustomTextForLabel" in data:
            self.CustomTextForLabel: CustomTextForLabel = CustomTextForLabel(data["CustomTextForLabel"])
        else:
            self.CustomTextForLabel: CustomTextForLabel = None
        if "Dimensions" in data:
            self.Dimensions: LabelDimensions = LabelDimensions(data["Dimensions"])
        else:
            self.Dimensions: LabelDimensions = None
        if "FileContents" in data:
            self.FileContents: FileContents = FileContents(data["FileContents"])
        else:
            self.FileContents: FileContents = None
        if "LabelFormat" in data:
            self.LabelFormat: LabelFormat = LabelFormat(data["LabelFormat"])
        else:
            self.LabelFormat: LabelFormat = None
        if "StandardIdForLabel" in data:
            self.StandardIdForLabel: StandardIdForLabel = StandardIdForLabel(data["StandardIdForLabel"])
        else:
            self.StandardIdForLabel: StandardIdForLabel = None


class LabelCustomization:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CustomTextForLabel" in data:
            self.CustomTextForLabel: CustomTextForLabel = CustomTextForLabel(data["CustomTextForLabel"])
        else:
            self.CustomTextForLabel: CustomTextForLabel = None
        if "StandardIdForLabel" in data:
            self.StandardIdForLabel: StandardIdForLabel = StandardIdForLabel(data["StandardIdForLabel"])
        else:
            self.StandardIdForLabel: StandardIdForLabel = None


class LabelDimensions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Length" in data:
            self.Length: LabelDimension = LabelDimension(data["Length"])
        else:
            self.Length: LabelDimension = None
        if "Width" in data:
            self.Width: LabelDimension = LabelDimension(data["Width"])
        else:
            self.Width: LabelDimension = None
        if "Unit" in data:
            self.Unit: UnitOfLength = UnitOfLength(data["Unit"])
        else:
            self.Unit: UnitOfLength = None


class Length:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "value" in data:
            self.value: float = float(data["value"])
        else:
            self.value: float = None
        if "unit" in data:
            self.unit: UnitOfLength = UnitOfLength(data["unit"])
        else:
            self.unit: UnitOfLength = None


class PackageDimensions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Length" in data:
            self.Length: PackageDimension = PackageDimension(data["Length"])
        else:
            self.Length: PackageDimension = None
        if "Width" in data:
            self.Width: PackageDimension = PackageDimension(data["Width"])
        else:
            self.Width: PackageDimension = None
        if "Height" in data:
            self.Height: PackageDimension = PackageDimension(data["Height"])
        else:
            self.Height: PackageDimension = None
        if "Unit" in data:
            self.Unit: UnitOfLength = UnitOfLength(data["Unit"])
        else:
            self.Unit: UnitOfLength = None
        if "PredefinedPackageDimensions" in data:
            self.PredefinedPackageDimensions: PredefinedPackageDimensions = PredefinedPackageDimensions(
                data["PredefinedPackageDimensions"]
            )
        else:
            self.PredefinedPackageDimensions: PredefinedPackageDimensions = None


class Shipment:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShipmentId" in data:
            self.ShipmentId: ShipmentId = ShipmentId(data["ShipmentId"])
        else:
            self.ShipmentId: ShipmentId = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: AmazonOrderId = AmazonOrderId(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: AmazonOrderId = None
        if "SellerOrderId" in data:
            self.SellerOrderId: SellerOrderId = SellerOrderId(data["SellerOrderId"])
        else:
            self.SellerOrderId: SellerOrderId = None
        if "ItemList" in data:
            self.ItemList: ItemList = ItemList(data["ItemList"])
        else:
            self.ItemList: ItemList = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = Address(data["ShipFromAddress"])
        else:
            self.ShipFromAddress: Address = None
        if "ShipToAddress" in data:
            self.ShipToAddress: Address = Address(data["ShipToAddress"])
        else:
            self.ShipToAddress: Address = None
        if "PackageDimensions" in data:
            self.PackageDimensions: PackageDimensions = PackageDimensions(data["PackageDimensions"])
        else:
            self.PackageDimensions: PackageDimensions = None
        if "Weight" in data:
            self.Weight: Weight = Weight(data["Weight"])
        else:
            self.Weight: Weight = None
        if "Insurance" in data:
            self.Insurance: CurrencyAmount = CurrencyAmount(data["Insurance"])
        else:
            self.Insurance: CurrencyAmount = None
        if "ShippingService" in data:
            self.ShippingService: ShippingService = ShippingService(data["ShippingService"])
        else:
            self.ShippingService: ShippingService = None
        if "Label" in data:
            self.Label: Label = Label(data["Label"])
        else:
            self.Label: Label = None
        if "Status" in data:
            self.Status: ShipmentStatus = ShipmentStatus(data["Status"])
        else:
            self.Status: ShipmentStatus = None
        if "TrackingId" in data:
            self.TrackingId: TrackingId = TrackingId(data["TrackingId"])
        else:
            self.TrackingId: TrackingId = None
        if "CreatedDate" in data:
            self.CreatedDate: Timestamp = Timestamp(data["CreatedDate"])
        else:
            self.CreatedDate: Timestamp = None
        if "LastUpdatedDate" in data:
            self.LastUpdatedDate: Timestamp = Timestamp(data["LastUpdatedDate"])
        else:
            self.LastUpdatedDate: Timestamp = None


class ShipmentRequestDetails:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "AmazonOrderId" in data:
            self.AmazonOrderId: AmazonOrderId = AmazonOrderId(data["AmazonOrderId"])
        else:
            self.AmazonOrderId: AmazonOrderId = None
        if "SellerOrderId" in data:
            self.SellerOrderId: SellerOrderId = SellerOrderId(data["SellerOrderId"])
        else:
            self.SellerOrderId: SellerOrderId = None
        if "ItemList" in data:
            self.ItemList: ItemList = ItemList(data["ItemList"])
        else:
            self.ItemList: ItemList = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = Address(data["ShipFromAddress"])
        else:
            self.ShipFromAddress: Address = None
        if "PackageDimensions" in data:
            self.PackageDimensions: PackageDimensions = PackageDimensions(data["PackageDimensions"])
        else:
            self.PackageDimensions: PackageDimensions = None
        if "Weight" in data:
            self.Weight: Weight = Weight(data["Weight"])
        else:
            self.Weight: Weight = None
        if "MustArriveByDate" in data:
            self.MustArriveByDate: Timestamp = Timestamp(data["MustArriveByDate"])
        else:
            self.MustArriveByDate: Timestamp = None
        if "ShipDate" in data:
            self.ShipDate: Timestamp = Timestamp(data["ShipDate"])
        else:
            self.ShipDate: Timestamp = None
        if "ShippingServiceOptions" in data:
            self.ShippingServiceOptions: ShippingServiceOptions = ShippingServiceOptions(data["ShippingServiceOptions"])
        else:
            self.ShippingServiceOptions: ShippingServiceOptions = None
        if "LabelCustomization" in data:
            self.LabelCustomization: LabelCustomization = LabelCustomization(data["LabelCustomization"])
        else:
            self.LabelCustomization: LabelCustomization = None


class ShippingOfferingFilter:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "IncludePackingSlipWithLabel" in data:
            self.IncludePackingSlipWithLabel: bool = bool(data["IncludePackingSlipWithLabel"])
        else:
            self.IncludePackingSlipWithLabel: bool = None
        if "IncludeComplexShippingOptions" in data:
            self.IncludeComplexShippingOptions: bool = bool(data["IncludeComplexShippingOptions"])
        else:
            self.IncludeComplexShippingOptions: bool = None
        if "CarrierWillPickUp" in data:
            self.CarrierWillPickUp: CarrierWillPickUpOption = CarrierWillPickUpOption(data["CarrierWillPickUp"])
        else:
            self.CarrierWillPickUp: CarrierWillPickUpOption = None
        if "DeliveryExperience" in data:
            self.DeliveryExperience: DeliveryExperienceOption = DeliveryExperienceOption(data["DeliveryExperience"])
        else:
            self.DeliveryExperience: DeliveryExperienceOption = None


class ShippingService:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ShippingServiceName" in data:
            self.ShippingServiceName: str = str(data["ShippingServiceName"])
        else:
            self.ShippingServiceName: str = None
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = ShippingServiceIdentifier(data["ShippingServiceId"])
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "ShippingServiceOfferId" in data:
            self.ShippingServiceOfferId: str = str(data["ShippingServiceOfferId"])
        else:
            self.ShippingServiceOfferId: str = None
        if "ShipDate" in data:
            self.ShipDate: Timestamp = Timestamp(data["ShipDate"])
        else:
            self.ShipDate: Timestamp = None
        if "EarliestEstimatedDeliveryDate" in data:
            self.EarliestEstimatedDeliveryDate: Timestamp = Timestamp(data["EarliestEstimatedDeliveryDate"])
        else:
            self.EarliestEstimatedDeliveryDate: Timestamp = None
        if "LatestEstimatedDeliveryDate" in data:
            self.LatestEstimatedDeliveryDate: Timestamp = Timestamp(data["LatestEstimatedDeliveryDate"])
        else:
            self.LatestEstimatedDeliveryDate: Timestamp = None
        if "Rate" in data:
            self.Rate: CurrencyAmount = CurrencyAmount(data["Rate"])
        else:
            self.Rate: CurrencyAmount = None
        if "ShippingServiceOptions" in data:
            self.ShippingServiceOptions: ShippingServiceOptions = ShippingServiceOptions(data["ShippingServiceOptions"])
        else:
            self.ShippingServiceOptions: ShippingServiceOptions = None
        if "AvailableShippingServiceOptions" in data:
            self.AvailableShippingServiceOptions: AvailableShippingServiceOptions = AvailableShippingServiceOptions(
                data["AvailableShippingServiceOptions"]
            )
        else:
            self.AvailableShippingServiceOptions: AvailableShippingServiceOptions = None
        if "AvailableLabelFormats" in data:
            self.AvailableLabelFormats: LabelFormatList = LabelFormatList(data["AvailableLabelFormats"])
        else:
            self.AvailableLabelFormats: LabelFormatList = None
        if "AvailableFormatOptionsForLabel" in data:
            self.AvailableFormatOptionsForLabel: AvailableFormatOptionsForLabelList = (
                AvailableFormatOptionsForLabelList(data["AvailableFormatOptionsForLabel"])
            )
        else:
            self.AvailableFormatOptionsForLabel: AvailableFormatOptionsForLabelList = None
        if "RequiresAdditionalSellerInputs" in data:
            self.RequiresAdditionalSellerInputs: bool = bool(data["RequiresAdditionalSellerInputs"])
        else:
            self.RequiresAdditionalSellerInputs: bool = None


class ShippingServiceOptions:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "DeliveryExperience" in data:
            self.DeliveryExperience: DeliveryExperienceType = DeliveryExperienceType(data["DeliveryExperience"])
        else:
            self.DeliveryExperience: DeliveryExperienceType = None
        if "DeclaredValue" in data:
            self.DeclaredValue: CurrencyAmount = CurrencyAmount(data["DeclaredValue"])
        else:
            self.DeclaredValue: CurrencyAmount = None
        if "CarrierWillPickUp" in data:
            self.CarrierWillPickUp: bool = bool(data["CarrierWillPickUp"])
        else:
            self.CarrierWillPickUp: bool = None
        if "CarrierWillPickUpOption" in data:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = CarrierWillPickUpOption(
                data["CarrierWillPickUpOption"]
            )
        else:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = None
        if "LabelFormat" in data:
            self.LabelFormat: LabelFormat = LabelFormat(data["LabelFormat"])
        else:
            self.LabelFormat: LabelFormat = None


class RejectedShippingService:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None
        if "ShippingServiceName" in data:
            self.ShippingServiceName: str = str(data["ShippingServiceName"])
        else:
            self.ShippingServiceName: str = None
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = ShippingServiceIdentifier(data["ShippingServiceId"])
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "RejectionReasonCode" in data:
            self.RejectionReasonCode: str = str(data["RejectionReasonCode"])
        else:
            self.RejectionReasonCode: str = None
        if "RejectionReasonMessage" in data:
            self.RejectionReasonMessage: str = str(data["RejectionReasonMessage"])
        else:
            self.RejectionReasonMessage: str = None


class TemporarilyUnavailableCarrier:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None


class TermsAndConditionsNotAcceptedCarrier:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "CarrierName" in data:
            self.CarrierName: str = str(data["CarrierName"])
        else:
            self.CarrierName: str = None


class Weight:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Value" in data:
            self.Value: WeightValue = WeightValue(data["Value"])
        else:
            self.Value: WeightValue = None
        if "Unit" in data:
            self.Unit: UnitOfWeight = UnitOfWeight(data["Unit"])
        else:
            self.Unit: UnitOfWeight = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class AvailableCarrierWillPickUpOptionsList(list, _List["AvailableCarrierWillPickUpOption"]):
    def __init__(self, data):
        super().__init__([AvailableCarrierWillPickUpOption(datum) for datum in data])
        self.data = data


class AvailableDeliveryExperienceOptionsList(list, _List["AvailableDeliveryExperienceOption"]):
    def __init__(self, data):
        super().__init__([AvailableDeliveryExperienceOption(datum) for datum in data])
        self.data = data


class AvailableFormatOptionsForLabelList(list, _List["LabelFormatOption"]):
    def __init__(self, data):
        super().__init__([LabelFormatOption(datum) for datum in data])
        self.data = data


class Constraints(list, _List["Constraint"]):
    def __init__(self, data):
        super().__init__([Constraint(datum) for datum in data])
        self.data = data


class AdditionalInputsList(list, _List["AdditionalInputs"]):
    def __init__(self, data):
        super().__init__([AdditionalInputs(datum) for datum in data])
        self.data = data


class AdditionalSellerInputsList(list, _List["AdditionalSellerInputs"]):
    def __init__(self, data):
        super().__init__([AdditionalSellerInputs(datum) for datum in data])
        self.data = data


class ItemLevelFieldsList(list, _List["ItemLevelFields"]):
    def __init__(self, data):
        super().__init__([ItemLevelFields(datum) for datum in data])
        self.data = data


class ItemList(list, _List["Item"]):
    def __init__(self, data):
        super().__init__([Item(datum) for datum in data])
        self.data = data


class LabelFormatList(list, _List["LabelFormat"]):
    def __init__(self, data):
        super().__init__([LabelFormat(datum) for datum in data])
        self.data = data


class RestrictedSetValues(list, _List["str"]):
    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ShippingServiceList(list, _List["ShippingService"]):
    def __init__(self, data):
        super().__init__([ShippingService(datum) for datum in data])
        self.data = data


class RejectedShippingServiceList(list, _List["RejectedShippingService"]):
    def __init__(self, data):
        super().__init__([RejectedShippingService(datum) for datum in data])
        self.data = data


class TemporarilyUnavailableCarrierList(list, _List["TemporarilyUnavailableCarrier"]):
    def __init__(self, data):
        super().__init__([TemporarilyUnavailableCarrier(datum) for datum in data])
        self.data = data


class TermsAndConditionsNotAcceptedCarrierList(list, _List["TermsAndConditionsNotAcceptedCarrier"]):
    def __init__(self, data):
        super().__init__([TermsAndConditionsNotAcceptedCarrier(datum) for datum in data])
        self.data = data


class TransparencyCodeList(list, _List["TransparencyCode"]):
    def __init__(self, data):
        super().__init__([TransparencyCode(datum) for datum in data])
        self.data = data


InputTargetType = str
AddressLine1 = str
AddressLine2 = str
AddressLine3 = str
AddressName = str
AmazonOrderId = str
City = str
CountryCode = str
CustomTextForLabel = str
DeliveryExperienceType = str
DistrictOrCounty = str
EmailAddress = str
FileType = str
HazmatType = str
ItemQuantity = int
ItemDescription = str
LabelDimension = float
LabelFormat = str
OrderItemId = str
PackageDimension = float
PhoneNumber = str
PostalCode = str
PredefinedPackageDimensions = str
SellerOrderId = str
ShipmentId = str
ShipmentStatus = str
DeliveryExperienceOption = str
ShippingServiceIdentifier = str
CarrierWillPickUpOption = str
StandardIdForLabel = str
StateOrProvinceCode = str
Timestamp = str
TrackingId = str
TransparencyCode = str
UnitOfLength = str
UnitOfWeight = str
WeightValue = float
AvailableFormatOptionsForLabel = AvailableFormatOptionsForLabelList


class MerchantFulfillmentClient(__BaseClient):
    def getEligibleShipmentServicesOld(
        self,
    ):
        url = "/mfn/v0/eligibleServices".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetEligibleShipmentServicesResponse,
            400: GetEligibleShipmentServicesResponse,
            401: GetEligibleShipmentServicesResponse,
            403: GetEligibleShipmentServicesResponse,
            404: GetEligibleShipmentServicesResponse,
            429: GetEligibleShipmentServicesResponse,
            500: GetEligibleShipmentServicesResponse,
            503: GetEligibleShipmentServicesResponse,
        }[response.status_code](response.json())

    def getEligibleShipmentServices(
        self,
    ):
        url = "/mfn/v0/eligibleShippingServices".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetEligibleShipmentServicesResponse,
            400: GetEligibleShipmentServicesResponse,
            401: GetEligibleShipmentServicesResponse,
            403: GetEligibleShipmentServicesResponse,
            404: GetEligibleShipmentServicesResponse,
            429: GetEligibleShipmentServicesResponse,
            500: GetEligibleShipmentServicesResponse,
            503: GetEligibleShipmentServicesResponse,
        }[response.status_code](response.json())

    def getShipment(
        self,
        shipmentId: str,
    ):
        url = "/mfn/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="GET", params=data)
        return {
            200: GetShipmentResponse,
            400: GetShipmentResponse,
            401: GetShipmentResponse,
            403: GetShipmentResponse,
            404: GetShipmentResponse,
            429: GetShipmentResponse,
            500: GetShipmentResponse,
            503: GetShipmentResponse,
        }[response.status_code](response.json())

    def cancelShipment(
        self,
        shipmentId: str,
    ):
        url = "/mfn/v0/shipments/{shipmentId}".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="DELETE", data=data)
        return {
            200: CancelShipmentResponse,
            400: CancelShipmentResponse,
            401: CancelShipmentResponse,
            403: CancelShipmentResponse,
            404: CancelShipmentResponse,
            429: CancelShipmentResponse,
            500: CancelShipmentResponse,
            503: CancelShipmentResponse,
        }[response.status_code](response.json())

    def cancelShipmentOld(
        self,
        shipmentId: str,
    ):
        url = "/mfn/v0/shipments/{shipmentId}/cancel".format(
            shipmentId=shipmentId,
        )
        data = {}
        response = self.request(url, method="PUT", data=data)
        return {
            200: CancelShipmentResponse,
            400: CancelShipmentResponse,
            401: CancelShipmentResponse,
            403: CancelShipmentResponse,
            404: CancelShipmentResponse,
            429: CancelShipmentResponse,
            500: CancelShipmentResponse,
            503: CancelShipmentResponse,
        }[response.status_code](response.json())

    def createShipment(
        self,
    ):
        url = "/mfn/v0/shipments".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: CreateShipmentResponse,
            400: CreateShipmentResponse,
            401: CreateShipmentResponse,
            403: CreateShipmentResponse,
            404: CreateShipmentResponse,
            429: CreateShipmentResponse,
            500: CreateShipmentResponse,
            503: CreateShipmentResponse,
        }[response.status_code](response.json())

    def getAdditionalSellerInputsOld(
        self,
    ):
        url = "/mfn/v0/sellerInputs".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetAdditionalSellerInputsResponse,
            400: GetAdditionalSellerInputsResponse,
            401: GetAdditionalSellerInputsResponse,
            403: GetAdditionalSellerInputsResponse,
            404: GetAdditionalSellerInputsResponse,
            429: GetAdditionalSellerInputsResponse,
            500: GetAdditionalSellerInputsResponse,
            503: GetAdditionalSellerInputsResponse,
        }[response.status_code](response.json())

    def getAdditionalSellerInputs(
        self,
    ):
        url = "/mfn/v0/additionalSellerInputs".format()
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetAdditionalSellerInputsResponse,
            400: GetAdditionalSellerInputsResponse,
            401: GetAdditionalSellerInputsResponse,
            403: GetAdditionalSellerInputsResponse,
            404: GetAdditionalSellerInputsResponse,
            429: GetAdditionalSellerInputsResponse,
            500: GetAdditionalSellerInputsResponse,
            503: GetAdditionalSellerInputsResponse,
        }[response.status_code](response.json())
