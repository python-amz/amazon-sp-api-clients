from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


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


class LabelFormatOptionRequest(__BaseDictObject):
    """
    Whether to include a packing slip.
    """

    def __init__(self, data):
        super().__init__(data)
        if "IncludePackingSlipWithLabel" in data:
            self.IncludePackingSlipWithLabel: bool = self._get_value(convert_bool, "IncludePackingSlipWithLabel")
        else:
            self.IncludePackingSlipWithLabel: bool = None


class LabelFormatOption(__BaseDictObject):
    """
    The label format details and whether to include a packing slip.
    """

    def __init__(self, data):
        super().__init__(data)
        if "IncludePackingSlipWithLabel" in data:
            self.IncludePackingSlipWithLabel: bool = self._get_value(convert_bool, "IncludePackingSlipWithLabel")
        else:
            self.IncludePackingSlipWithLabel: bool = None
        if "LabelFormat" in data:
            self.LabelFormat: LabelFormat = self._get_value(LabelFormat, "LabelFormat")
        else:
            self.LabelFormat: LabelFormat = None


class AvailableCarrierWillPickUpOption(__BaseDictObject):
    """
    Indicates whether the carrier will pick up the package, and what fee is charged, if any.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CarrierWillPickUpOption" in data:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = self._get_value(
                CarrierWillPickUpOption, "CarrierWillPickUpOption"
            )
        else:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = None
        if "Charge" in data:
            self.Charge: CurrencyAmount = self._get_value(CurrencyAmount, "Charge")
        else:
            self.Charge: CurrencyAmount = None


class AvailableDeliveryExperienceOption(__BaseDictObject):
    """
    The available delivery confirmation options, and the fee charged, if any.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DeliveryExperienceOption" in data:
            self.DeliveryExperienceOption: DeliveryExperienceOption = self._get_value(
                DeliveryExperienceOption, "DeliveryExperienceOption"
            )
        else:
            self.DeliveryExperienceOption: DeliveryExperienceOption = None
        if "Charge" in data:
            self.Charge: CurrencyAmount = self._get_value(CurrencyAmount, "Charge")
        else:
            self.Charge: CurrencyAmount = None


class AvailableShippingServiceOptions(__BaseDictObject):
    """
    The available shipping service options.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AvailableCarrierWillPickUpOptions" in data:
            self.AvailableCarrierWillPickUpOptions: AvailableCarrierWillPickUpOptionsList = self._get_value(
                AvailableCarrierWillPickUpOptionsList, "AvailableCarrierWillPickUpOptions"
            )
        else:
            self.AvailableCarrierWillPickUpOptions: AvailableCarrierWillPickUpOptionsList = None
        if "AvailableDeliveryExperienceOptions" in data:
            self.AvailableDeliveryExperienceOptions: AvailableDeliveryExperienceOptionsList = self._get_value(
                AvailableDeliveryExperienceOptionsList, "AvailableDeliveryExperienceOptions"
            )
        else:
            self.AvailableDeliveryExperienceOptions: AvailableDeliveryExperienceOptionsList = None


class Constraint(__BaseDictObject):
    """
    A validation constraint.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ValidationRegEx" in data:
            self.ValidationRegEx: str = self._get_value(str, "ValidationRegEx")
        else:
            self.ValidationRegEx: str = None
        if "ValidationString" in data:
            self.ValidationString: str = self._get_value(str, "ValidationString")
        else:
            self.ValidationString: str = None


class AdditionalInputs(__BaseDictObject):
    """
    Maps the additional seller input to the definition. The key to the map is the field name.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AdditionalInputFieldName" in data:
            self.AdditionalInputFieldName: str = self._get_value(str, "AdditionalInputFieldName")
        else:
            self.AdditionalInputFieldName: str = None
        if "SellerInputDefinition" in data:
            self.SellerInputDefinition: SellerInputDefinition = self._get_value(
                SellerInputDefinition, "SellerInputDefinition"
            )
        else:
            self.SellerInputDefinition: SellerInputDefinition = None


class SellerInputDefinition(__BaseDictObject):
    """
    Specifies characteristics that apply to a seller input.
    """

    def __init__(self, data):
        super().__init__(data)
        if "IsRequired" in data:
            self.IsRequired: bool = self._get_value(convert_bool, "IsRequired")
        else:
            self.IsRequired: bool = None
        if "DataType" in data:
            self.DataType: str = self._get_value(str, "DataType")
        else:
            self.DataType: str = None
        if "Constraints" in data:
            self.Constraints: Constraints = self._get_value(Constraints, "Constraints")
        else:
            self.Constraints: Constraints = None
        if "InputDisplayText" in data:
            self.InputDisplayText: str = self._get_value(str, "InputDisplayText")
        else:
            self.InputDisplayText: str = None
        if "InputTarget" in data:
            self.InputTarget: InputTargetType = self._get_value(InputTargetType, "InputTarget")
        else:
            self.InputTarget: InputTargetType = None
        if "StoredValue" in data:
            self.StoredValue: AdditionalSellerInput = self._get_value(AdditionalSellerInput, "StoredValue")
        else:
            self.StoredValue: AdditionalSellerInput = None
        if "RestrictedSetValues" in data:
            self.RestrictedSetValues: RestrictedSetValues = self._get_value(RestrictedSetValues, "RestrictedSetValues")
        else:
            self.RestrictedSetValues: RestrictedSetValues = None


class AdditionalSellerInput(__BaseDictObject):
    """
    Additional information required to purchase shipping.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DataType" in data:
            self.DataType: str = self._get_value(str, "DataType")
        else:
            self.DataType: str = None
        if "ValueAsString" in data:
            self.ValueAsString: str = self._get_value(str, "ValueAsString")
        else:
            self.ValueAsString: str = None
        if "ValueAsBoolean" in data:
            self.ValueAsBoolean: bool = self._get_value(convert_bool, "ValueAsBoolean")
        else:
            self.ValueAsBoolean: bool = None
        if "ValueAsInteger" in data:
            self.ValueAsInteger: int = self._get_value(int, "ValueAsInteger")
        else:
            self.ValueAsInteger: int = None
        if "ValueAsTimestamp" in data:
            self.ValueAsTimestamp: Timestamp = self._get_value(Timestamp, "ValueAsTimestamp")
        else:
            self.ValueAsTimestamp: Timestamp = None
        if "ValueAsAddress" in data:
            self.ValueAsAddress: Address = self._get_value(Address, "ValueAsAddress")
        else:
            self.ValueAsAddress: Address = None
        if "ValueAsWeight" in data:
            self.ValueAsWeight: Weight = self._get_value(Weight, "ValueAsWeight")
        else:
            self.ValueAsWeight: Weight = None
        if "ValueAsDimension" in data:
            self.ValueAsDimension: Length = self._get_value(Length, "ValueAsDimension")
        else:
            self.ValueAsDimension: Length = None
        if "ValueAsCurrency" in data:
            self.ValueAsCurrency: CurrencyAmount = self._get_value(CurrencyAmount, "ValueAsCurrency")
        else:
            self.ValueAsCurrency: CurrencyAmount = None


class AdditionalSellerInputs(__BaseDictObject):
    """
    An additional set of seller inputs required to purchase shipping.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AdditionalInputFieldName" in data:
            self.AdditionalInputFieldName: str = self._get_value(str, "AdditionalInputFieldName")
        else:
            self.AdditionalInputFieldName: str = None
        if "AdditionalSellerInput" in data:
            self.AdditionalSellerInput: AdditionalSellerInput = self._get_value(
                AdditionalSellerInput, "AdditionalSellerInput"
            )
        else:
            self.AdditionalSellerInput: AdditionalSellerInput = None


class Address(__BaseDictObject):
    """
    The postal address information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Name" in data:
            self.Name: AddressName = self._get_value(AddressName, "Name")
        else:
            self.Name: AddressName = None
        if "AddressLine1" in data:
            self.AddressLine1: AddressLine1 = self._get_value(AddressLine1, "AddressLine1")
        else:
            self.AddressLine1: AddressLine1 = None
        if "AddressLine2" in data:
            self.AddressLine2: AddressLine2 = self._get_value(AddressLine2, "AddressLine2")
        else:
            self.AddressLine2: AddressLine2 = None
        if "AddressLine3" in data:
            self.AddressLine3: AddressLine3 = self._get_value(AddressLine3, "AddressLine3")
        else:
            self.AddressLine3: AddressLine3 = None
        if "DistrictOrCounty" in data:
            self.DistrictOrCounty: DistrictOrCounty = self._get_value(DistrictOrCounty, "DistrictOrCounty")
        else:
            self.DistrictOrCounty: DistrictOrCounty = None
        if "Email" in data:
            self.Email: EmailAddress = self._get_value(EmailAddress, "Email")
        else:
            self.Email: EmailAddress = None
        if "City" in data:
            self.City: City = self._get_value(City, "City")
        else:
            self.City: City = None
        if "StateOrProvinceCode" in data:
            self.StateOrProvinceCode: StateOrProvinceCode = self._get_value(StateOrProvinceCode, "StateOrProvinceCode")
        else:
            self.StateOrProvinceCode: StateOrProvinceCode = None
        if "PostalCode" in data:
            self.PostalCode: PostalCode = self._get_value(PostalCode, "PostalCode")
        else:
            self.PostalCode: PostalCode = None
        if "CountryCode" in data:
            self.CountryCode: CountryCode = self._get_value(CountryCode, "CountryCode")
        else:
            self.CountryCode: CountryCode = None
        if "Phone" in data:
            self.Phone: PhoneNumber = self._get_value(PhoneNumber, "Phone")
        else:
            self.Phone: PhoneNumber = None


class CancelShipmentResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Shipment = self._get_value(Shipment, "payload")
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CreateShipmentRequest(__BaseDictObject):
    """
    Request schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShipmentRequestDetails" in data:
            self.ShipmentRequestDetails: ShipmentRequestDetails = self._get_value(
                ShipmentRequestDetails, "ShipmentRequestDetails"
            )
        else:
            self.ShipmentRequestDetails: ShipmentRequestDetails = None
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = self._get_value(
                ShippingServiceIdentifier, "ShippingServiceId"
            )
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "ShippingServiceOfferId" in data:
            self.ShippingServiceOfferId: str = self._get_value(str, "ShippingServiceOfferId")
        else:
            self.ShippingServiceOfferId: str = None
        if "HazmatType" in data:
            self.HazmatType: HazmatType = self._get_value(HazmatType, "HazmatType")
        else:
            self.HazmatType: HazmatType = None
        if "LabelFormatOption" in data:
            self.LabelFormatOption: LabelFormatOptionRequest = self._get_value(
                LabelFormatOptionRequest, "LabelFormatOption"
            )
        else:
            self.LabelFormatOption: LabelFormatOptionRequest = None
        if "ShipmentLevelSellerInputsList" in data:
            self.ShipmentLevelSellerInputsList: AdditionalSellerInputsList = self._get_value(
                AdditionalSellerInputsList, "ShipmentLevelSellerInputsList"
            )
        else:
            self.ShipmentLevelSellerInputsList: AdditionalSellerInputsList = None


class CreateShipmentResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Shipment = self._get_value(Shipment, "payload")
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ItemLevelFields(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "Asin" in data:
            self.Asin: str = self._get_value(str, "Asin")
        else:
            self.Asin: str = None
        if "AdditionalInputs" in data:
            self.AdditionalInputs: AdditionalInputsList = self._get_value(AdditionalInputsList, "AdditionalInputs")
        else:
            self.AdditionalInputs: AdditionalInputsList = None


class GetAdditionalSellerInputsRequest(__BaseDictObject):
    """
    Request schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = self._get_value(
                ShippingServiceIdentifier, "ShippingServiceId"
            )
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = self._get_value(Address, "ShipFromAddress")
        else:
            self.ShipFromAddress: Address = None
        if "OrderId" in data:
            self.OrderId: AmazonOrderId = self._get_value(AmazonOrderId, "OrderId")
        else:
            self.OrderId: AmazonOrderId = None


class GetAdditionalSellerInputsResult(__BaseDictObject):
    """
    The payload for the getAdditionalSellerInputs operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShipmentLevelFields" in data:
            self.ShipmentLevelFields: AdditionalInputsList = self._get_value(
                AdditionalInputsList, "ShipmentLevelFields"
            )
        else:
            self.ShipmentLevelFields: AdditionalInputsList = None
        if "ItemLevelFieldsList" in data:
            self.ItemLevelFieldsList: ItemLevelFieldsList = self._get_value(ItemLevelFieldsList, "ItemLevelFieldsList")
        else:
            self.ItemLevelFieldsList: ItemLevelFieldsList = None


class GetAdditionalSellerInputsResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetAdditionalSellerInputsResult = self._get_value(GetAdditionalSellerInputsResult, "payload")
        else:
            self.payload: GetAdditionalSellerInputsResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CurrencyAmount(__BaseDictObject):
    """
    Currency type and amount.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: float = self._get_value(float, "Amount")
        else:
            self.Amount: float = None


class FileContents(__BaseDictObject):
    """
    The document data and checksum.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Contents" in data:
            self.Contents: str = self._get_value(str, "Contents")
        else:
            self.Contents: str = None
        if "FileType" in data:
            self.FileType: FileType = self._get_value(FileType, "FileType")
        else:
            self.FileType: FileType = None
        if "Checksum" in data:
            self.Checksum: str = self._get_value(str, "Checksum")
        else:
            self.Checksum: str = None


class GetEligibleShipmentServicesRequest(__BaseDictObject):
    """
    Request schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShipmentRequestDetails" in data:
            self.ShipmentRequestDetails: ShipmentRequestDetails = self._get_value(
                ShipmentRequestDetails, "ShipmentRequestDetails"
            )
        else:
            self.ShipmentRequestDetails: ShipmentRequestDetails = None
        if "ShippingOfferingFilter" in data:
            self.ShippingOfferingFilter: ShippingOfferingFilter = self._get_value(
                ShippingOfferingFilter, "ShippingOfferingFilter"
            )
        else:
            self.ShippingOfferingFilter: ShippingOfferingFilter = None


class GetEligibleShipmentServicesResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetEligibleShipmentServicesResult = self._get_value(
                GetEligibleShipmentServicesResult, "payload"
            )
        else:
            self.payload: GetEligibleShipmentServicesResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetEligibleShipmentServicesResult(__BaseDictObject):
    """
    The payload for the getEligibleShipmentServices operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShippingServiceList" in data:
            self.ShippingServiceList: ShippingServiceList = self._get_value(ShippingServiceList, "ShippingServiceList")
        else:
            self.ShippingServiceList: ShippingServiceList = None
        if "RejectedShippingServiceList" in data:
            self.RejectedShippingServiceList: RejectedShippingServiceList = self._get_value(
                RejectedShippingServiceList, "RejectedShippingServiceList"
            )
        else:
            self.RejectedShippingServiceList: RejectedShippingServiceList = None
        if "TemporarilyUnavailableCarrierList" in data:
            self.TemporarilyUnavailableCarrierList: TemporarilyUnavailableCarrierList = self._get_value(
                TemporarilyUnavailableCarrierList, "TemporarilyUnavailableCarrierList"
            )
        else:
            self.TemporarilyUnavailableCarrierList: TemporarilyUnavailableCarrierList = None
        if "TermsAndConditionsNotAcceptedCarrierList" in data:
            self.TermsAndConditionsNotAcceptedCarrierList: TermsAndConditionsNotAcceptedCarrierList = self._get_value(
                TermsAndConditionsNotAcceptedCarrierList, "TermsAndConditionsNotAcceptedCarrierList"
            )
        else:
            self.TermsAndConditionsNotAcceptedCarrierList: TermsAndConditionsNotAcceptedCarrierList = None


class GetShipmentResponse(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Shipment = self._get_value(Shipment, "payload")
        else:
            self.payload: Shipment = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Item(__BaseDictObject):
    """
    An Amazon order item identifier and a quantity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItemId" in data:
            self.OrderItemId: OrderItemId = self._get_value(OrderItemId, "OrderItemId")
        else:
            self.OrderItemId: OrderItemId = None
        if "Quantity" in data:
            self.Quantity: ItemQuantity = self._get_value(ItemQuantity, "Quantity")
        else:
            self.Quantity: ItemQuantity = None
        if "ItemWeight" in data:
            self.ItemWeight: Weight = self._get_value(Weight, "ItemWeight")
        else:
            self.ItemWeight: Weight = None
        if "ItemDescription" in data:
            self.ItemDescription: ItemDescription = self._get_value(ItemDescription, "ItemDescription")
        else:
            self.ItemDescription: ItemDescription = None
        if "TransparencyCodeList" in data:
            self.TransparencyCodeList: TransparencyCodeList = self._get_value(
                TransparencyCodeList, "TransparencyCodeList"
            )
        else:
            self.TransparencyCodeList: TransparencyCodeList = None
        if "ItemLevelSellerInputsList" in data:
            self.ItemLevelSellerInputsList: AdditionalSellerInputsList = self._get_value(
                AdditionalSellerInputsList, "ItemLevelSellerInputsList"
            )
        else:
            self.ItemLevelSellerInputsList: AdditionalSellerInputsList = None


class Label(__BaseDictObject):
    """
    Data for creating a shipping label and dimensions for printing the label.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CustomTextForLabel" in data:
            self.CustomTextForLabel: CustomTextForLabel = self._get_value(CustomTextForLabel, "CustomTextForLabel")
        else:
            self.CustomTextForLabel: CustomTextForLabel = None
        if "Dimensions" in data:
            self.Dimensions: LabelDimensions = self._get_value(LabelDimensions, "Dimensions")
        else:
            self.Dimensions: LabelDimensions = None
        if "FileContents" in data:
            self.FileContents: FileContents = self._get_value(FileContents, "FileContents")
        else:
            self.FileContents: FileContents = None
        if "LabelFormat" in data:
            self.LabelFormat: LabelFormat = self._get_value(LabelFormat, "LabelFormat")
        else:
            self.LabelFormat: LabelFormat = None
        if "StandardIdForLabel" in data:
            self.StandardIdForLabel: StandardIdForLabel = self._get_value(StandardIdForLabel, "StandardIdForLabel")
        else:
            self.StandardIdForLabel: StandardIdForLabel = None


class LabelCustomization(__BaseDictObject):
    """
    Custom text for shipping labels.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CustomTextForLabel" in data:
            self.CustomTextForLabel: CustomTextForLabel = self._get_value(CustomTextForLabel, "CustomTextForLabel")
        else:
            self.CustomTextForLabel: CustomTextForLabel = None
        if "StandardIdForLabel" in data:
            self.StandardIdForLabel: StandardIdForLabel = self._get_value(StandardIdForLabel, "StandardIdForLabel")
        else:
            self.StandardIdForLabel: StandardIdForLabel = None


class LabelDimensions(__BaseDictObject):
    """
    Dimensions for printing a shipping label.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Length" in data:
            self.Length: LabelDimension = self._get_value(LabelDimension, "Length")
        else:
            self.Length: LabelDimension = None
        if "Width" in data:
            self.Width: LabelDimension = self._get_value(LabelDimension, "Width")
        else:
            self.Width: LabelDimension = None
        if "Unit" in data:
            self.Unit: UnitOfLength = self._get_value(UnitOfLength, "Unit")
        else:
            self.Unit: UnitOfLength = None


class Length(__BaseDictObject):
    """
    The length.
    """

    def __init__(self, data):
        super().__init__(data)
        if "value" in data:
            self.value: float = self._get_value(float, "value")
        else:
            self.value: float = None
        if "unit" in data:
            self.unit: UnitOfLength = self._get_value(UnitOfLength, "unit")
        else:
            self.unit: UnitOfLength = None


class PackageDimensions(__BaseDictObject):
    """
    The dimensions of a package contained in a shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Length" in data:
            self.Length: PackageDimension = self._get_value(PackageDimension, "Length")
        else:
            self.Length: PackageDimension = None
        if "Width" in data:
            self.Width: PackageDimension = self._get_value(PackageDimension, "Width")
        else:
            self.Width: PackageDimension = None
        if "Height" in data:
            self.Height: PackageDimension = self._get_value(PackageDimension, "Height")
        else:
            self.Height: PackageDimension = None
        if "Unit" in data:
            self.Unit: UnitOfLength = self._get_value(UnitOfLength, "Unit")
        else:
            self.Unit: UnitOfLength = None
        if "PredefinedPackageDimensions" in data:
            self.PredefinedPackageDimensions: PredefinedPackageDimensions = self._get_value(
                PredefinedPackageDimensions, "PredefinedPackageDimensions"
            )
        else:
            self.PredefinedPackageDimensions: PredefinedPackageDimensions = None


class Shipment(__BaseDictObject):
    """
    The details of a shipment, including the shipment status.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShipmentId" in data:
            self.ShipmentId: ShipmentId = self._get_value(ShipmentId, "ShipmentId")
        else:
            self.ShipmentId: ShipmentId = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: AmazonOrderId = self._get_value(AmazonOrderId, "AmazonOrderId")
        else:
            self.AmazonOrderId: AmazonOrderId = None
        if "SellerOrderId" in data:
            self.SellerOrderId: SellerOrderId = self._get_value(SellerOrderId, "SellerOrderId")
        else:
            self.SellerOrderId: SellerOrderId = None
        if "ItemList" in data:
            self.ItemList: ItemList = self._get_value(ItemList, "ItemList")
        else:
            self.ItemList: ItemList = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = self._get_value(Address, "ShipFromAddress")
        else:
            self.ShipFromAddress: Address = None
        if "ShipToAddress" in data:
            self.ShipToAddress: Address = self._get_value(Address, "ShipToAddress")
        else:
            self.ShipToAddress: Address = None
        if "PackageDimensions" in data:
            self.PackageDimensions: PackageDimensions = self._get_value(PackageDimensions, "PackageDimensions")
        else:
            self.PackageDimensions: PackageDimensions = None
        if "Weight" in data:
            self.Weight: Weight = self._get_value(Weight, "Weight")
        else:
            self.Weight: Weight = None
        if "Insurance" in data:
            self.Insurance: CurrencyAmount = self._get_value(CurrencyAmount, "Insurance")
        else:
            self.Insurance: CurrencyAmount = None
        if "ShippingService" in data:
            self.ShippingService: ShippingService = self._get_value(ShippingService, "ShippingService")
        else:
            self.ShippingService: ShippingService = None
        if "Label" in data:
            self.Label: Label = self._get_value(Label, "Label")
        else:
            self.Label: Label = None
        if "Status" in data:
            self.Status: ShipmentStatus = self._get_value(ShipmentStatus, "Status")
        else:
            self.Status: ShipmentStatus = None
        if "TrackingId" in data:
            self.TrackingId: TrackingId = self._get_value(TrackingId, "TrackingId")
        else:
            self.TrackingId: TrackingId = None
        if "CreatedDate" in data:
            self.CreatedDate: Timestamp = self._get_value(Timestamp, "CreatedDate")
        else:
            self.CreatedDate: Timestamp = None
        if "LastUpdatedDate" in data:
            self.LastUpdatedDate: Timestamp = self._get_value(Timestamp, "LastUpdatedDate")
        else:
            self.LastUpdatedDate: Timestamp = None


class ShipmentRequestDetails(__BaseDictObject):
    """
    Shipment information required for requesting shipping service offers or for creating a shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: AmazonOrderId = self._get_value(AmazonOrderId, "AmazonOrderId")
        else:
            self.AmazonOrderId: AmazonOrderId = None
        if "SellerOrderId" in data:
            self.SellerOrderId: SellerOrderId = self._get_value(SellerOrderId, "SellerOrderId")
        else:
            self.SellerOrderId: SellerOrderId = None
        if "ItemList" in data:
            self.ItemList: ItemList = self._get_value(ItemList, "ItemList")
        else:
            self.ItemList: ItemList = None
        if "ShipFromAddress" in data:
            self.ShipFromAddress: Address = self._get_value(Address, "ShipFromAddress")
        else:
            self.ShipFromAddress: Address = None
        if "PackageDimensions" in data:
            self.PackageDimensions: PackageDimensions = self._get_value(PackageDimensions, "PackageDimensions")
        else:
            self.PackageDimensions: PackageDimensions = None
        if "Weight" in data:
            self.Weight: Weight = self._get_value(Weight, "Weight")
        else:
            self.Weight: Weight = None
        if "MustArriveByDate" in data:
            self.MustArriveByDate: Timestamp = self._get_value(Timestamp, "MustArriveByDate")
        else:
            self.MustArriveByDate: Timestamp = None
        if "ShipDate" in data:
            self.ShipDate: Timestamp = self._get_value(Timestamp, "ShipDate")
        else:
            self.ShipDate: Timestamp = None
        if "ShippingServiceOptions" in data:
            self.ShippingServiceOptions: ShippingServiceOptions = self._get_value(
                ShippingServiceOptions, "ShippingServiceOptions"
            )
        else:
            self.ShippingServiceOptions: ShippingServiceOptions = None
        if "LabelCustomization" in data:
            self.LabelCustomization: LabelCustomization = self._get_value(LabelCustomization, "LabelCustomization")
        else:
            self.LabelCustomization: LabelCustomization = None


class ShippingOfferingFilter(__BaseDictObject):
    """
    Filter for use when requesting eligible shipping services.
    """

    def __init__(self, data):
        super().__init__(data)
        if "IncludePackingSlipWithLabel" in data:
            self.IncludePackingSlipWithLabel: bool = self._get_value(convert_bool, "IncludePackingSlipWithLabel")
        else:
            self.IncludePackingSlipWithLabel: bool = None
        if "IncludeComplexShippingOptions" in data:
            self.IncludeComplexShippingOptions: bool = self._get_value(convert_bool, "IncludeComplexShippingOptions")
        else:
            self.IncludeComplexShippingOptions: bool = None
        if "CarrierWillPickUp" in data:
            self.CarrierWillPickUp: CarrierWillPickUpOption = self._get_value(
                CarrierWillPickUpOption, "CarrierWillPickUp"
            )
        else:
            self.CarrierWillPickUp: CarrierWillPickUpOption = None
        if "DeliveryExperience" in data:
            self.DeliveryExperience: DeliveryExperienceOption = self._get_value(
                DeliveryExperienceOption, "DeliveryExperience"
            )
        else:
            self.DeliveryExperience: DeliveryExperienceOption = None


class ShippingService(__BaseDictObject):
    """
    A shipping service offer made by a carrier.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ShippingServiceName" in data:
            self.ShippingServiceName: str = self._get_value(str, "ShippingServiceName")
        else:
            self.ShippingServiceName: str = None
        if "CarrierName" in data:
            self.CarrierName: str = self._get_value(str, "CarrierName")
        else:
            self.CarrierName: str = None
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = self._get_value(
                ShippingServiceIdentifier, "ShippingServiceId"
            )
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "ShippingServiceOfferId" in data:
            self.ShippingServiceOfferId: str = self._get_value(str, "ShippingServiceOfferId")
        else:
            self.ShippingServiceOfferId: str = None
        if "ShipDate" in data:
            self.ShipDate: Timestamp = self._get_value(Timestamp, "ShipDate")
        else:
            self.ShipDate: Timestamp = None
        if "EarliestEstimatedDeliveryDate" in data:
            self.EarliestEstimatedDeliveryDate: Timestamp = self._get_value(Timestamp, "EarliestEstimatedDeliveryDate")
        else:
            self.EarliestEstimatedDeliveryDate: Timestamp = None
        if "LatestEstimatedDeliveryDate" in data:
            self.LatestEstimatedDeliveryDate: Timestamp = self._get_value(Timestamp, "LatestEstimatedDeliveryDate")
        else:
            self.LatestEstimatedDeliveryDate: Timestamp = None
        if "Rate" in data:
            self.Rate: CurrencyAmount = self._get_value(CurrencyAmount, "Rate")
        else:
            self.Rate: CurrencyAmount = None
        if "ShippingServiceOptions" in data:
            self.ShippingServiceOptions: ShippingServiceOptions = self._get_value(
                ShippingServiceOptions, "ShippingServiceOptions"
            )
        else:
            self.ShippingServiceOptions: ShippingServiceOptions = None
        if "AvailableShippingServiceOptions" in data:
            self.AvailableShippingServiceOptions: AvailableShippingServiceOptions = self._get_value(
                AvailableShippingServiceOptions, "AvailableShippingServiceOptions"
            )
        else:
            self.AvailableShippingServiceOptions: AvailableShippingServiceOptions = None
        if "AvailableLabelFormats" in data:
            self.AvailableLabelFormats: LabelFormatList = self._get_value(LabelFormatList, "AvailableLabelFormats")
        else:
            self.AvailableLabelFormats: LabelFormatList = None
        if "AvailableFormatOptionsForLabel" in data:
            self.AvailableFormatOptionsForLabel: AvailableFormatOptionsForLabelList = self._get_value(
                AvailableFormatOptionsForLabelList, "AvailableFormatOptionsForLabel"
            )
        else:
            self.AvailableFormatOptionsForLabel: AvailableFormatOptionsForLabelList = None
        if "RequiresAdditionalSellerInputs" in data:
            self.RequiresAdditionalSellerInputs: bool = self._get_value(convert_bool, "RequiresAdditionalSellerInputs")
        else:
            self.RequiresAdditionalSellerInputs: bool = None


class ShippingServiceOptions(__BaseDictObject):
    """
    Extra services provided by a carrier.
    """

    def __init__(self, data):
        super().__init__(data)
        if "DeliveryExperience" in data:
            self.DeliveryExperience: DeliveryExperienceType = self._get_value(
                DeliveryExperienceType, "DeliveryExperience"
            )
        else:
            self.DeliveryExperience: DeliveryExperienceType = None
        if "DeclaredValue" in data:
            self.DeclaredValue: CurrencyAmount = self._get_value(CurrencyAmount, "DeclaredValue")
        else:
            self.DeclaredValue: CurrencyAmount = None
        if "CarrierWillPickUp" in data:
            self.CarrierWillPickUp: bool = self._get_value(convert_bool, "CarrierWillPickUp")
        else:
            self.CarrierWillPickUp: bool = None
        if "CarrierWillPickUpOption" in data:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = self._get_value(
                CarrierWillPickUpOption, "CarrierWillPickUpOption"
            )
        else:
            self.CarrierWillPickUpOption: CarrierWillPickUpOption = None
        if "LabelFormat" in data:
            self.LabelFormat: LabelFormat = self._get_value(LabelFormat, "LabelFormat")
        else:
            self.LabelFormat: LabelFormat = None


class RejectedShippingService(__BaseDictObject):
    """
    Information about a rejected shipping service
    """

    def __init__(self, data):
        super().__init__(data)
        if "CarrierName" in data:
            self.CarrierName: str = self._get_value(str, "CarrierName")
        else:
            self.CarrierName: str = None
        if "ShippingServiceName" in data:
            self.ShippingServiceName: str = self._get_value(str, "ShippingServiceName")
        else:
            self.ShippingServiceName: str = None
        if "ShippingServiceId" in data:
            self.ShippingServiceId: ShippingServiceIdentifier = self._get_value(
                ShippingServiceIdentifier, "ShippingServiceId"
            )
        else:
            self.ShippingServiceId: ShippingServiceIdentifier = None
        if "RejectionReasonCode" in data:
            self.RejectionReasonCode: str = self._get_value(str, "RejectionReasonCode")
        else:
            self.RejectionReasonCode: str = None
        if "RejectionReasonMessage" in data:
            self.RejectionReasonMessage: str = self._get_value(str, "RejectionReasonMessage")
        else:
            self.RejectionReasonMessage: str = None


class TemporarilyUnavailableCarrier(__BaseDictObject):
    """
    A carrier who is temporarily unavailable, most likely due to a service outage experienced by the carrier.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CarrierName" in data:
            self.CarrierName: str = self._get_value(str, "CarrierName")
        else:
            self.CarrierName: str = None


class TermsAndConditionsNotAcceptedCarrier(__BaseDictObject):
    """
    A carrier whose terms and conditions have not been accepted by the seller.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CarrierName" in data:
            self.CarrierName: str = self._get_value(str, "CarrierName")
        else:
            self.CarrierName: str = None


class Weight(__BaseDictObject):
    """
    The weight.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Value" in data:
            self.Value: WeightValue = self._get_value(WeightValue, "Value")
        else:
            self.Value: WeightValue = None
        if "Unit" in data:
            self.Unit: UnitOfWeight = self._get_value(UnitOfWeight, "Unit")
        else:
            self.Unit: UnitOfWeight = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class AvailableCarrierWillPickUpOptionsList(list, _List["AvailableCarrierWillPickUpOption"]):
    """
    List of available carrier pickup options.
    """

    def __init__(self, data):
        super().__init__([AvailableCarrierWillPickUpOption(datum) for datum in data])
        self.data = data


class AvailableDeliveryExperienceOptionsList(list, _List["AvailableDeliveryExperienceOption"]):
    """
    List of available delivery experience options.
    """

    def __init__(self, data):
        super().__init__([AvailableDeliveryExperienceOption(datum) for datum in data])
        self.data = data


class AvailableFormatOptionsForLabelList(list, _List["LabelFormatOption"]):
    """
    The available label formats.
    """

    def __init__(self, data):
        super().__init__([LabelFormatOption(datum) for datum in data])
        self.data = data


class Constraints(list, _List["Constraint"]):
    """
    List of constraints.
    """

    def __init__(self, data):
        super().__init__([Constraint(datum) for datum in data])
        self.data = data


class AdditionalInputsList(list, _List["AdditionalInputs"]):
    """
    A list of additional inputs.
    """

    def __init__(self, data):
        super().__init__([AdditionalInputs(datum) for datum in data])
        self.data = data


class AdditionalSellerInputsList(list, _List["AdditionalSellerInputs"]):
    """
    A list of additional seller input pairs required to purchase shipping.
    """

    def __init__(self, data):
        super().__init__([AdditionalSellerInputs(datum) for datum in data])
        self.data = data


class ItemLevelFieldsList(list, _List["ItemLevelFields"]):
    """
    A list of item level fields.
    """

    def __init__(self, data):
        super().__init__([ItemLevelFields(datum) for datum in data])
        self.data = data


class ItemList(list, _List["Item"]):
    """
    The list of items to be included in a shipment.
    """

    def __init__(self, data):
        super().__init__([Item(datum) for datum in data])
        self.data = data


class LabelFormatList(list, _List["LabelFormat"]):
    """
    List of label formats.
    """

    def __init__(self, data):
        super().__init__([LabelFormat(datum) for datum in data])
        self.data = data


class RestrictedSetValues(list, _List["str"]):
    """
    The set of fixed values in an additional seller input.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ShippingServiceList(list, _List["ShippingService"]):
    """
    A list of shipping services offers.
    """

    def __init__(self, data):
        super().__init__([ShippingService(datum) for datum in data])
        self.data = data


class RejectedShippingServiceList(list, _List["RejectedShippingService"]):
    """
    List of services that were for some reason unavailable for this request
    """

    def __init__(self, data):
        super().__init__([RejectedShippingService(datum) for datum in data])
        self.data = data


class TemporarilyUnavailableCarrierList(list, _List["TemporarilyUnavailableCarrier"]):
    """
    A list of temporarily unavailable carriers.
    """

    def __init__(self, data):
        super().__init__([TemporarilyUnavailableCarrier(datum) for datum in data])
        self.data = data


class TermsAndConditionsNotAcceptedCarrierList(list, _List["TermsAndConditionsNotAcceptedCarrier"]):
    """
    List of carriers whose terms and conditions were not accepted by the seller.
    """

    def __init__(self, data):
        super().__init__([TermsAndConditionsNotAcceptedCarrier(datum) for datum in data])
        self.data = data


class TransparencyCodeList(list, _List["TransparencyCode"]):
    """
    A list of transparency codes.
    """

    def __init__(self, data):
        super().__init__([TransparencyCode(datum) for datum in data])
        self.data = data


class InputTargetType(str):
    """
    Indicates whether the additional seller input is at the item or shipment level.
    """


class AddressLine1(str):
    """
    The street address information.
    """


class AddressLine2(str):
    """
    Additional street address information.
    """


class AddressLine3(str):
    """
    Additional street address information.
    """


class AddressName(str):
    """
    The name of the addressee, or business name.
    """


class AmazonOrderId(str):
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """


class City(str):
    """
    The city.
    """


class CountryCode(str):
    """
    The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
    """


class CustomTextForLabel(str):
    """
        Custom text to print on the label.
    Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support CustomTextForLabel.
    """


class DeliveryExperienceType(str):
    """
    The delivery confirmation level.
    """


class DistrictOrCounty(str):
    """
    The district or county.
    """


class EmailAddress(str):
    """
    The email address.
    """


class FileType(str):
    """
    The file type for a label.
    """


class HazmatType(str):
    """
    Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
    """


class ItemQuantity(int):
    """
    The number of items.
    """


class ItemDescription(str):
    """
    The description of the item.
    """


class LabelDimension(float):
    """
    A label dimension.
    """


class LabelFormat(str):
    """
    The label format.
    """


class OrderItemId(str):
    """
    An Amazon-defined identifier for an individual item in an order.
    """


class PackageDimension(float):
    """ """


class PhoneNumber(str):
    """
    The phone number.
    """


class PostalCode(str):
    """
    The zip code or postal code.
    """


class PredefinedPackageDimensions(str):
    """
        An enumeration of predefined parcel tokens. If you specify a PredefinedPackageDimensions token, you are not obligated to use a branded package from a carrier. For example, if you specify the FedEx_Box_10kg token, you do not have to use that particular package from FedEx. You are only obligated to use a box that matches the dimensions specified by the token.
    Note: Please note that carriers can have restrictions on the type of package allowed for certain ship methods. Check the carrier website for all details. Example: Flat rate pricing is available when materials are sent by USPS in a USPS-produced Flat Rate Envelope or Box.
    """


class SellerOrderId(str):
    """
    A seller-defined order identifier.
    """


class ShipmentId(str):
    """
    An Amazon-defined shipment identifier.
    """


class ShipmentStatus(str):
    """
    The shipment status.
    """


class DeliveryExperienceOption(str):
    """
    The delivery confirmation level.
    """


class ShippingServiceIdentifier(str):
    """
    An Amazon-defined shipping service identifier.
    """


class CarrierWillPickUpOption(str):
    """
    Carrier will pick up option.
    """


class StandardIdForLabel(str):
    """
    The type of standard identifier to print on the label.
    """


class StateOrProvinceCode(str):
    """
    The state or province code. **Note.** Required in the Canada, US, and UK marketplaces. Also required for shipments originating from China.
    """


class Timestamp(str):
    """ """


class TrackingId(str):
    """
    The shipment tracking identifier provided by the carrier.
    """


class TransparencyCode(str):
    """
    The Transparency code associated with the item.
    """


class UnitOfLength(str):
    """
    The unit of length.
    """


class UnitOfWeight(str):
    """
    The unit of weight.
    """


class WeightValue(float):
    """
    The weight value.
    """


class AvailableFormatOptionsForLabel(
    AvailableFormatOptionsForLabelList,
):
    """ """

    def __init__(self, data):
        self.data = data
        super().__init__(data)


class MerchantFulfillmentV0Client(__BaseClient):
    def getEligibleShipmentServicesOld(
        self,
        data: GetEligibleShipmentServicesRequest,
    ):
        """
                Returns a list of shipping service offers that satisfy the specified shipment request details.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/eligibleServices"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetEligibleShipmentServicesResponse,
            400: GetEligibleShipmentServicesResponse,
            401: GetEligibleShipmentServicesResponse,
            403: GetEligibleShipmentServicesResponse,
            404: GetEligibleShipmentServicesResponse,
            429: GetEligibleShipmentServicesResponse,
            500: GetEligibleShipmentServicesResponse,
            503: GetEligibleShipmentServicesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getEligibleShipmentServices(
        self,
        data: GetEligibleShipmentServicesRequest,
    ):
        """
                Returns a list of shipping service offers that satisfy the specified shipment request details.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/eligibleShippingServices"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetEligibleShipmentServicesResponse,
            400: GetEligibleShipmentServicesResponse,
            401: GetEligibleShipmentServicesResponse,
            403: GetEligibleShipmentServicesResponse,
            404: GetEligibleShipmentServicesResponse,
            429: GetEligibleShipmentServicesResponse,
            500: GetEligibleShipmentServicesResponse,
            503: GetEligibleShipmentServicesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getShipment(
        self,
        shipmentId: str,
    ):
        """
                Returns the shipment information for an existing shipment.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/shipments/{shipmentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetShipmentResponse,
            400: GetShipmentResponse,
            401: GetShipmentResponse,
            403: GetShipmentResponse,
            404: GetShipmentResponse,
            429: GetShipmentResponse,
            500: GetShipmentResponse,
            503: GetShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelShipment(
        self,
        shipmentId: str,
    ):
        """
                Cancel the shipment indicated by the specified shipment identifier.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/shipments/{shipmentId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            200: CancelShipmentResponse,
            400: CancelShipmentResponse,
            401: CancelShipmentResponse,
            403: CancelShipmentResponse,
            404: CancelShipmentResponse,
            429: CancelShipmentResponse,
            500: CancelShipmentResponse,
            503: CancelShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def cancelShipmentOld(
        self,
        shipmentId: str,
    ):
        """
                Cancel the shipment indicated by the specified shipment identifer.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/shipments/{shipmentId}/cancel"
        params = {}
        response = self.request(
            path=url,
            method="PUT",
            params=params,
        )
        response_type = {
            200: CancelShipmentResponse,
            400: CancelShipmentResponse,
            401: CancelShipmentResponse,
            403: CancelShipmentResponse,
            404: CancelShipmentResponse,
            429: CancelShipmentResponse,
            500: CancelShipmentResponse,
            503: CancelShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def createShipment(
        self,
        data: CreateShipmentRequest,
    ):
        """
                Create a shipment with the information provided.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/shipments"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: CreateShipmentResponse,
            400: CreateShipmentResponse,
            401: CreateShipmentResponse,
            403: CreateShipmentResponse,
            404: CreateShipmentResponse,
            429: CreateShipmentResponse,
            500: CreateShipmentResponse,
            503: CreateShipmentResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getAdditionalSellerInputsOld(
        self,
        data: GetAdditionalSellerInputsRequest,
    ):
        """
                Get a list of additional seller inputs required for a ship method. This is generally used for international shipping.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/sellerInputs"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetAdditionalSellerInputsResponse,
            400: GetAdditionalSellerInputsResponse,
            401: GetAdditionalSellerInputsResponse,
            403: GetAdditionalSellerInputsResponse,
            404: GetAdditionalSellerInputsResponse,
            429: GetAdditionalSellerInputsResponse,
            500: GetAdditionalSellerInputsResponse,
            503: GetAdditionalSellerInputsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getAdditionalSellerInputs(
        self,
        data: GetAdditionalSellerInputsRequest,
    ):
        """
                Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/mfn/v0/additionalSellerInputs"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetAdditionalSellerInputsResponse,
            400: GetAdditionalSellerInputsResponse,
            401: GetAdditionalSellerInputsResponse,
            403: GetAdditionalSellerInputsResponse,
            404: GetAdditionalSellerInputsResponse,
            429: GetAdditionalSellerInputsResponse,
            500: GetAdditionalSellerInputsResponse,
            503: GetAdditionalSellerInputsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
