"""
Selling Partner API for Merchant Fulfillment
=============================================================================================

The Selling Partner API for Merchant Fulfillment helps you build applications that let sellers purchase shipping for non-Prime and Prime orders using Amazon’s Buy Shipping Services.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class AdditionalInputs:

    additional_input_field_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    seller_input_definition: dict[str, Any]
    # {'ref': '#/components/schemas/SellerInputDefinition', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class AdditionalInputsList:

    pass


@attrs.define
class AdditionalSellerInput:

    data_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_boolean: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_integer: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_string: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    value_as_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_currency: dict[str, Any]
    # {'ref': '#/components/schemas/CurrencyAmount', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_dimension: dict[str, Any]
    # {'ref': '#/components/schemas/Length', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_timestamp: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value_as_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class AdditionalSellerInputs:

    additional_input_field_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    additional_seller_input: dict[str, Any]
    # {'ref': '#/components/schemas/AdditionalSellerInput', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class AdditionalSellerInputsList:

    pass


@attrs.define
class Address:

    address_line1: str
    # {'ref': '#/components/schemas/AddressLine1', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    address_line2: str
    # {'ref': '#/components/schemas/AddressLine2', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    address_line3: str
    # {'ref': '#/components/schemas/AddressLine3', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    city: str
    # {'ref': '#/components/schemas/City', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    country_code: str
    # {'ref': '#/components/schemas/CountryCode', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    district_or_county: str
    # {'ref': '#/components/schemas/DistrictOrCounty', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    email: str
    # {'ref': '#/components/schemas/EmailAddress', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    name: str
    # {'ref': '#/components/schemas/AddressName', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    phone: str
    # {'ref': '#/components/schemas/PhoneNumber', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    postal_code: str
    # {'ref': '#/components/schemas/PostalCode', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    state_or_province_code: str
    # {'ref': '#/components/schemas/StateOrProvinceCode', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class AddressLine1:

    pass


@attrs.define
class AddressLine2:

    pass


@attrs.define
class AddressLine3:

    pass


@attrs.define
class AddressName:

    pass


@attrs.define
class AmazonOrderId:

    pass


@attrs.define
class AvailableCarrierWillPickUpOption:

    carrier_will_pick_up_option: Union[
        Literal["CarrierWillPickUp"], Literal["ShipperWillDropOff"], Literal["NoPreference"]
    ]
    # {'ref': '#/components/schemas/CarrierWillPickUpOption', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    charge: dict[str, Any]
    # {'ref': '#/components/schemas/CurrencyAmount', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class AvailableCarrierWillPickUpOptionsList:

    pass


@attrs.define
class AvailableDeliveryExperienceOption:

    charge: dict[str, Any]
    # {'ref': '#/components/schemas/CurrencyAmount', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    delivery_experience_option: Union[
        Literal["DeliveryConfirmationWithAdultSignature"],
        Literal["DeliveryConfirmationWithSignature"],
        Literal["DeliveryConfirmationWithoutSignature"],
        Literal["NoTracking"],
        Literal["NoPreference"],
    ]
    # {'ref': '#/components/schemas/DeliveryExperienceOption', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class AvailableDeliveryExperienceOptionsList:

    pass


@attrs.define
class AvailableFormatOptionsForLabelList:

    pass


@attrs.define
class AvailableShippingServiceOptions:

    available_carrier_will_pick_up_options: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AvailableCarrierWillPickUpOptionsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    available_delivery_experience_options: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AvailableDeliveryExperienceOptionsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class CancelShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Shipment', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class CarrierWillPickUpOption:

    pass


@attrs.define
class City:

    pass


@attrs.define
class Constraint:

    validation_reg_ex: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    validation_string: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    pass


@attrs.define
class Constraints:

    pass


@attrs.define
class CountryCode:

    pass


@attrs.define
class CreateShipmentRequest:

    shipping_service_offer_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    hazmat_type: Union[Literal["None"], Literal["LQHazmat"]]
    # {'ref': '#/components/schemas/HazmatType', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    label_format_option: dict[str, Any]
    # {'ref': '#/components/schemas/LabelFormatOptionRequest', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipment_level_seller_inputs_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AdditionalSellerInputsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipment_request_details: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentRequestDetails', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_id: str
    # {'ref': '#/components/schemas/ShippingServiceIdentifier', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class CreateShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Shipment', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class CurrencyAmount:

    amount: Union[float, int]
    # {'type': 'number', 'schema_format': 'double', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    currency_code: str
    # {'type': 'string', 'maxLength': 3, 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    pass


@attrs.define
class CustomTextForLabel:

    pass


@attrs.define
class DeliveryExperienceOption:

    pass


@attrs.define
class DeliveryExperienceType:

    pass


@attrs.define
class DistrictOrCounty:

    pass


@attrs.define
class EmailAddress:

    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FileContents:

    checksum: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    contents: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    file_type: Union[Literal["application/pdf"], Literal["application/zpl"], Literal["image/png"]]
    # {'ref': '#/components/schemas/FileType', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class FileType:

    pass


@attrs.define
class GetAdditionalSellerInputsRequest:

    order_id: str
    # {'ref': '#/components/schemas/AmazonOrderId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    ship_from_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_id: str
    # {'ref': '#/components/schemas/ShippingServiceIdentifier', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class GetAdditionalSellerInputsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetAdditionalSellerInputsResult', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class GetAdditionalSellerInputsResult:

    item_level_fields_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ItemLevelFieldsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipment_level_fields: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AdditionalInputsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class GetEligibleShipmentServicesRequest:

    shipment_request_details: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentRequestDetails', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_offering_filter: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingOfferingFilter', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class GetEligibleShipmentServicesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetEligibleShipmentServicesResult', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class GetEligibleShipmentServicesResult:

    rejected_shipping_service_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RejectedShippingServiceList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShippingServiceList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    temporarily_unavailable_carrier_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TemporarilyUnavailableCarrierList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    terms_and_conditions_not_accepted_carrier_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TermsAndConditionsNotAcceptedCarrierList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class GetShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Shipment', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class HazmatType:

    pass


@attrs.define
class InputTargetType:

    pass


@attrs.define
class Item:

    item_description: str
    # {'ref': '#/components/schemas/ItemDescription', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    item_level_seller_inputs_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AdditionalSellerInputsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    item_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    order_item_id: str
    # {'ref': '#/components/schemas/OrderItemId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    quantity: int
    # {'ref': '#/components/schemas/ItemQuantity', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    transparency_code_list: list[str]
    # {'ref': '#/components/schemas/TransparencyCodeList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class ItemDescription:

    pass


@attrs.define
class ItemLevelFields:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    additional_inputs: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AdditionalInputsList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class ItemLevelFieldsList:

    pass


@attrs.define
class ItemList:

    pass


@attrs.define
class ItemQuantity:

    pass


@attrs.define
class Label:

    custom_text_for_label: str
    # {'ref': '#/components/schemas/CustomTextForLabel', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/LabelDimensions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    file_contents: dict[str, Any]
    # {'ref': '#/components/schemas/FileContents', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    label_format: Union[
        Literal["PDF"], Literal["PNG"], Literal["ZPL203"], Literal["ZPL300"], Literal["ShippingServiceDefault"]
    ]
    # {'ref': '#/components/schemas/LabelFormat', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    standard_id_for_label: Union[Literal["AmazonOrderId"]]
    # {'ref': '#/components/schemas/StandardIdForLabel', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class LabelCustomization:

    custom_text_for_label: str
    # {'ref': '#/components/schemas/CustomTextForLabel', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    standard_id_for_label: Union[Literal["AmazonOrderId"]]
    # {'ref': '#/components/schemas/StandardIdForLabel', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class LabelDimension:

    pass


@attrs.define
class LabelDimensions:

    length: Union[float, int]
    # {'ref': '#/components/schemas/LabelDimension', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    unit: Union[Literal["inches"], Literal["centimeters"]]
    # {'ref': '#/components/schemas/UnitOfLength', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    width: Union[float, int]
    # {'ref': '#/components/schemas/LabelDimension', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class LabelFormat:

    pass


@attrs.define
class LabelFormatList:

    pass


@attrs.define
class LabelFormatOption:

    include_packing_slip_with_label: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    label_format: Union[
        Literal["PDF"], Literal["PNG"], Literal["ZPL203"], Literal["ZPL300"], Literal["ShippingServiceDefault"]
    ]
    # {'ref': '#/components/schemas/LabelFormat', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class LabelFormatOptionRequest:

    include_packing_slip_with_label: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    pass


@attrs.define
class Length:

    value: Union[float, int]
    # {'type': 'number', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    unit: Union[Literal["inches"], Literal["centimeters"]]
    # {'ref': '#/components/schemas/UnitOfLength', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class OrderItemId:

    pass


@attrs.define
class PackageDimension:

    pass


@attrs.define
class PackageDimensions:

    height: Union[float, int]
    # {'ref': '#/components/schemas/PackageDimension', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    length: Union[float, int]
    # {'ref': '#/components/schemas/PackageDimension', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    predefined_package_dimensions: Union[
        Literal["FedEx_Box_10kg"],
        Literal["FedEx_Box_25kg"],
        Literal["FedEx_Box_Extra_Large_1"],
        Literal["FedEx_Box_Extra_Large_2"],
        Literal["FedEx_Box_Large_1"],
        Literal["FedEx_Box_Large_2"],
        Literal["FedEx_Box_Medium_1"],
        Literal["FedEx_Box_Medium_2"],
        Literal["FedEx_Box_Small_1"],
        Literal["FedEx_Box_Small_2"],
        Literal["FedEx_Envelope"],
        Literal["FedEx_Padded_Pak"],
        Literal["FedEx_Pak_1"],
        Literal["FedEx_Pak_2"],
        Literal["FedEx_Tube"],
        Literal["FedEx_XL_Pak"],
        Literal["UPS_Box_10kg"],
        Literal["UPS_Box_25kg"],
        Literal["UPS_Express_Box"],
        Literal["UPS_Express_Box_Large"],
        Literal["UPS_Express_Box_Medium"],
        Literal["UPS_Express_Box_Small"],
        Literal["UPS_Express_Envelope"],
        Literal["UPS_Express_Hard_Pak"],
        Literal["UPS_Express_Legal_Envelope"],
        Literal["UPS_Express_Pak"],
        Literal["UPS_Express_Tube"],
        Literal["UPS_Laboratory_Pak"],
        Literal["UPS_Pad_Pak"],
        Literal["UPS_Pallet"],
        Literal["USPS_Card"],
        Literal["USPS_Flat"],
        Literal["USPS_FlatRateCardboardEnvelope"],
        Literal["USPS_FlatRateEnvelope"],
        Literal["USPS_FlatRateGiftCardEnvelope"],
        Literal["USPS_FlatRateLegalEnvelope"],
        Literal["USPS_FlatRatePaddedEnvelope"],
        Literal["USPS_FlatRateWindowEnvelope"],
        Literal["USPS_LargeFlatRateBoardGameBox"],
        Literal["USPS_LargeFlatRateBox"],
        Literal["USPS_Letter"],
        Literal["USPS_MediumFlatRateBox1"],
        Literal["USPS_MediumFlatRateBox2"],
        Literal["USPS_RegionalRateBoxA1"],
        Literal["USPS_RegionalRateBoxA2"],
        Literal["USPS_RegionalRateBoxB1"],
        Literal["USPS_RegionalRateBoxB2"],
        Literal["USPS_RegionalRateBoxC"],
        Literal["USPS_SmallFlatRateBox"],
        Literal["USPS_SmallFlatRateEnvelope"],
    ]
    # {'ref': '#/components/schemas/PredefinedPackageDimensions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    unit: Union[Literal["inches"], Literal["centimeters"]]
    # {'ref': '#/components/schemas/UnitOfLength', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    width: Union[float, int]
    # {'ref': '#/components/schemas/PackageDimension', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class PhoneNumber:

    pass


@attrs.define
class PostalCode:

    pass


@attrs.define
class PredefinedPackageDimensions:

    pass


@attrs.define
class RejectedShippingService:

    carrier_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    rejection_reason_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    rejection_reason_message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    shipping_service_id: str
    # {'ref': '#/components/schemas/ShippingServiceIdentifier', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class RejectedShippingServiceList:

    pass


@attrs.define
class RestrictedSetValues:

    pass


@attrs.define
class SellerInputDefinition:

    data_type: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    input_display_text: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    is_required: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    constraints: list[dict[str, Any]]
    # {'ref': '#/components/schemas/Constraints', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    input_target: Union[Literal["SHIPMENT_LEVEL"], Literal["ITEM_LEVEL"]]
    # {'ref': '#/components/schemas/InputTargetType', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    restricted_set_values: list[str]
    # {'ref': '#/components/schemas/RestrictedSetValues', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    stored_value: dict[str, Any]
    # {'ref': '#/components/schemas/AdditionalSellerInput', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class SellerOrderId:

    pass


@attrs.define
class Shipment:

    amazon_order_id: str
    # {'ref': '#/components/schemas/AmazonOrderId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    created_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    insurance: dict[str, Any]
    # {'ref': '#/components/schemas/CurrencyAmount', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ItemList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    label: dict[str, Any]
    # {'ref': '#/components/schemas/Label', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    last_updated_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    package_dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/PackageDimensions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    seller_order_id: str
    # {'ref': '#/components/schemas/SellerOrderId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    ship_from_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    ship_to_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipment_id: str
    # {'ref': '#/components/schemas/ShipmentId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingService', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    status: Union[Literal["Purchased"], Literal["RefundPending"], Literal["RefundRejected"], Literal["RefundApplied"]]
    # {'ref': '#/components/schemas/ShipmentStatus', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    tracking_id: str
    # {'ref': '#/components/schemas/TrackingId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class ShipmentId:

    pass


@attrs.define
class ShipmentRequestDetails:

    amazon_order_id: str
    # {'ref': '#/components/schemas/AmazonOrderId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    item_list: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ItemList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    label_customization: dict[str, Any]
    # {'ref': '#/components/schemas/LabelCustomization', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    must_arrive_by_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    package_dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/PackageDimensions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    seller_order_id: str
    # {'ref': '#/components/schemas/SellerOrderId', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    ship_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    ship_from_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_options: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingServiceOptions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class ShipmentStatus:

    pass


@attrs.define
class ShippingOfferingFilter:

    include_complex_shipping_options: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    include_packing_slip_with_label: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    carrier_will_pick_up: Union[Literal["CarrierWillPickUp"], Literal["ShipperWillDropOff"], Literal["NoPreference"]]
    # {'ref': '#/components/schemas/CarrierWillPickUpOption', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    delivery_experience: Union[
        Literal["DeliveryConfirmationWithAdultSignature"],
        Literal["DeliveryConfirmationWithSignature"],
        Literal["DeliveryConfirmationWithoutSignature"],
        Literal["NoTracking"],
        Literal["NoPreference"],
    ]
    # {'ref': '#/components/schemas/DeliveryExperienceOption', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class ShippingService:

    carrier_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    requires_additional_seller_inputs: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_offer_id: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    available_format_options_for_label: list[dict[str, Any]]
    # {'ref': '#/components/schemas/AvailableFormatOptionsForLabelList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    available_label_formats: list[
        Union[Literal["PDF"], Literal["PNG"], Literal["ZPL203"], Literal["ZPL300"], Literal["ShippingServiceDefault"]]
    ]
    # {'ref': '#/components/schemas/LabelFormatList', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    available_shipping_service_options: dict[str, Any]
    # {'ref': '#/components/schemas/AvailableShippingServiceOptions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    earliest_estimated_delivery_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    latest_estimated_delivery_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    rate: dict[str, Any]
    # {'ref': '#/components/schemas/CurrencyAmount', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    ship_date: str
    # {'ref': '#/components/schemas/Timestamp', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_id: str
    # {'ref': '#/components/schemas/ShippingServiceIdentifier', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    shipping_service_options: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingServiceOptions', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class ShippingServiceIdentifier:

    pass


@attrs.define
class ShippingServiceList:

    pass


@attrs.define
class ShippingServiceOptions:

    carrier_will_pick_up: bool
    # {'type': 'boolean', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    carrier_will_pick_up_option: Union[
        Literal["CarrierWillPickUp"], Literal["ShipperWillDropOff"], Literal["NoPreference"]
    ]
    # {'ref': '#/components/schemas/CarrierWillPickUpOption', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    declared_value: dict[str, Any]
    # {'ref': '#/components/schemas/CurrencyAmount', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    delivery_experience: Union[
        Literal["DeliveryConfirmationWithAdultSignature"],
        Literal["DeliveryConfirmationWithSignature"],
        Literal["DeliveryConfirmationWithoutSignature"],
        Literal["NoTracking"],
    ]
    # {'ref': '#/components/schemas/DeliveryExperienceType', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    label_format: Union[
        Literal["PDF"], Literal["PNG"], Literal["ZPL203"], Literal["ZPL300"], Literal["ShippingServiceDefault"]
    ]
    # {'ref': '#/components/schemas/LabelFormat', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class StandardIdForLabel:

    pass


@attrs.define
class StateOrProvinceCode:

    pass


@attrs.define
class TemporarilyUnavailableCarrier:

    carrier_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    pass


@attrs.define
class TemporarilyUnavailableCarrierList:

    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrier:

    carrier_name: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}

    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrierList:

    pass


@attrs.define
class Timestamp:

    pass


@attrs.define
class TrackingId:

    pass


@attrs.define
class TransparencyCode:

    pass


@attrs.define
class TransparencyCodeList:

    pass


@attrs.define
class UnitOfLength:

    pass


@attrs.define
class UnitOfWeight:

    pass


@attrs.define
class Weight:

    unit: Union[Literal["oz"], Literal["g"]]
    # {'ref': '#/components/schemas/UnitOfWeight', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    value: Union[float, int]
    # {'ref': '#/components/schemas/WeightValue', 'generator': <__mp_main__.Generator object at 0x000001E786213040>}
    pass


@attrs.define
class WeightValue:

    pass


class MerchantFulfillmentV0Client(BaseClient):
    def cancel_shipment(
        self,
        shipment_id: str,
    ):
        """
        Cancel the shipment indicated by the specified shipment identifier.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The Amazon-defined shipment identifier for the shipment to cancel.
        """
        url = "/mfn/v0/shipments/{shipmentId}"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "DELETE", values, self._cancel_shipment_params)
        return response

    _cancel_shipment_params = (("shipmentId", "path"),)  # name, param in

    def cancel_shipment_old(
        self,
        shipment_id: str,
    ):
        """
        Cancel the shipment indicated by the specified shipment identifer.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The Amazon-defined shipment identifier for the shipment to cancel.
        """
        url = "/mfn/v0/shipments/{shipmentId}/cancel"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "PUT", values, self._cancel_shipment_old_params)
        return response

    _cancel_shipment_old_params = (("shipmentId", "path"),)  # name, param in

    def create_shipment(
        self,
    ):
        """
        Create a shipment with the information provided.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/mfn/v0/shipments"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_shipment_params)
        return response

    _create_shipment_params = ()  # name, param in

    def get_additional_seller_inputs(
        self,
    ):
        """
        Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/mfn/v0/additionalSellerInputs"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_additional_seller_inputs_params)
        return response

    _get_additional_seller_inputs_params = ()  # name, param in

    def get_additional_seller_inputs_old(
        self,
    ):
        """
        Get a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/mfn/v0/sellerInputs"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_additional_seller_inputs_old_params)
        return response

    _get_additional_seller_inputs_old_params = ()  # name, param in

    def get_eligible_shipment_services(
        self,
    ):
        """
        Returns a list of shipping service offers that satisfy the specified shipment request details.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/mfn/v0/eligibleShippingServices"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_eligible_shipment_services_params)
        return response

    _get_eligible_shipment_services_params = ()  # name, param in

    def get_eligible_shipment_services_old(
        self,
    ):
        """
        Returns a list of shipping service offers that satisfy the specified shipment request details.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/mfn/v0/eligibleServices"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_eligible_shipment_services_old_params)
        return response

    _get_eligible_shipment_services_old_params = ()  # name, param in

    def get_shipment(
        self,
        shipment_id: str,
    ):
        """
        Returns the shipment information for an existing shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The Amazon-defined shipment identifier for the shipment.
        """
        url = "/mfn/v0/shipments/{shipmentId}"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_params)
        return response

    _get_shipment_params = (("shipmentId", "path"),)  # name, param in
