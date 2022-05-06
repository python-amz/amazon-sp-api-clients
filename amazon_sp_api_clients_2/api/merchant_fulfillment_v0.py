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

    additional_input_field_name: str = attrs.field(
        kw_only=True,
    )
    """
    The field name.
    """

    seller_input_definition: "SellerInputDefinition" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AdditionalInputsList:

    pass


@attrs.define
class AdditionalSellerInput:

    data_type: str = attrs.field(
        kw_only=True,
    )
    """
    The data type of the additional information.
    """

    value_as_boolean: bool = attrs.field(
        kw_only=True,
    )
    """
    The value when the data type is boolean.
    """

    value_as_integer: int = attrs.field(
        kw_only=True,
    )
    """
    The value when the data type is integer.
    """

    value_as_string: str = attrs.field(
        kw_only=True,
    )
    """
    The value when the data type is string.
    """

    value_as_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value_as_currency: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value_as_dimension: "Length" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value_as_timestamp: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value_as_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AdditionalSellerInputs:

    additional_input_field_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the additional input field.
    """

    additional_seller_input: "AdditionalSellerInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AdditionalSellerInputsList:

    pass


@attrs.define
class Address:

    address_line1: "AddressLine1" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    address_line2: "AddressLine2" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    address_line3: "AddressLine3" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    city: "City" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    country_code: "CountryCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    district_or_county: "DistrictOrCounty" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    email: "EmailAddress" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    name: "AddressName" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    phone: "PhoneNumber" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    postal_code: "PostalCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    state_or_province_code: "StateOrProvinceCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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

    carrier_will_pick_up_option: "CarrierWillPickUpOption" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    charge: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AvailableCarrierWillPickUpOptionsList:

    pass


@attrs.define
class AvailableDeliveryExperienceOption:

    charge: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    delivery_experience_option: "DeliveryExperienceOption" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AvailableDeliveryExperienceOptionsList:

    pass


@attrs.define
class AvailableFormatOptionsForLabelList:

    pass


@attrs.define
class AvailableShippingServiceOptions:

    available_carrier_will_pick_up_options: "AvailableCarrierWillPickUpOptionsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    available_delivery_experience_options: "AvailableDeliveryExperienceOptionsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CancelShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CarrierWillPickUpOption:

    pass


@attrs.define
class City:

    pass


@attrs.define
class Constraint:

    validation_reg_ex: str = attrs.field(
        kw_only=True,
    )
    """
    A regular expression.
    """

    validation_string: str = attrs.field(
        kw_only=True,
    )
    """
    A validation string.
    """

    pass


@attrs.define
class Constraints:

    pass


@attrs.define
class CountryCode:

    pass


@attrs.define
class CreateShipmentRequest:

    shipping_service_offer_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies a shipping service order made by a carrier.
    """

    hazmat_type: "HazmatType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_format_option: "LabelFormatOptionRequest" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_level_seller_inputs_list: "AdditionalSellerInputsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_request_details: "ShipmentRequestDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CurrencyAmount:

    amount: Union[float, int] = attrs.field(
        kw_only=True,
    )
    """
    The currency amount.

    Extra fields:
    {'schema_format': 'double'}
    """

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three-digit currency code in ISO 4217 format.

    Extra fields:
    {'maxLength': 3}
    """

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

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occured.
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
class FileContents:

    checksum: str = attrs.field(
        kw_only=True,
    )
    """
    An MD5 hash to validate the PDF document data, in the form of a Base64-encoded string.
    """

    contents: str = attrs.field(
        kw_only=True,
    )
    """
    Data for printing labels, in the form of a Base64-encoded, GZip-compressed string.
    """

    file_type: "FileType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class FileType:

    pass


@attrs.define
class GetAdditionalSellerInputsRequest:

    order_id: "AmazonOrderId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetAdditionalSellerInputsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetAdditionalSellerInputsResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetAdditionalSellerInputsResult:

    item_level_fields_list: "ItemLevelFieldsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_level_fields: "AdditionalInputsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetEligibleShipmentServicesRequest:

    shipment_request_details: "ShipmentRequestDetails" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_offering_filter: "ShippingOfferingFilter" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetEligibleShipmentServicesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetEligibleShipmentServicesResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetEligibleShipmentServicesResult:

    rejected_shipping_service_list: "RejectedShippingServiceList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service_list: "ShippingServiceList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    temporarily_unavailable_carrier_list: "TemporarilyUnavailableCarrierList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    terms_and_conditions_not_accepted_carrier_list: "TermsAndConditionsNotAcceptedCarrierList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class HazmatType:

    pass


@attrs.define
class InputTargetType:

    pass


@attrs.define
class Item:

    item_description: "ItemDescription" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_level_seller_inputs_list: "AdditionalSellerInputsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    order_item_id: "OrderItemId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    transparency_code_list: "TransparencyCodeList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ItemDescription:

    pass


@attrs.define
class ItemLevelFields:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    additional_inputs: "AdditionalInputsList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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

    custom_text_for_label: "CustomTextForLabel" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    dimensions: "LabelDimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    file_contents: "FileContents" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_format: "LabelFormat" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_id_for_label: "StandardIdForLabel" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LabelCustomization:

    custom_text_for_label: "CustomTextForLabel" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    standard_id_for_label: "StandardIdForLabel" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LabelDimension:

    pass


@attrs.define
class LabelDimensions:

    length: "LabelDimension" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    unit: "UnitOfLength" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    width: "LabelDimension" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LabelFormat:

    pass


@attrs.define
class LabelFormatList:

    pass


@attrs.define
class LabelFormatOption:

    include_packing_slip_with_label: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, include a packing slip with the label.
    """

    label_format: "LabelFormat" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LabelFormatOptionRequest:

    include_packing_slip_with_label: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, include a packing slip with the label.
    """

    pass


@attrs.define
class Length:

    value: Union[float, int] = attrs.field(
        kw_only=True,
    )
    """
    The value in units.
    """

    unit: "UnitOfLength" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class OrderItemId:

    pass


@attrs.define
class PackageDimension:

    pass


@attrs.define
class PackageDimensions:

    height: "PackageDimension" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    length: "PackageDimension" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    predefined_package_dimensions: "PredefinedPackageDimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    unit: "UnitOfLength" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    width: "PackageDimension" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The rejected shipping carrier name. e.g. USPS
    """

    rejection_reason_code: str = attrs.field(
        kw_only=True,
    )
    """
    A reason code meant to be consumed programatically. e.g. CARRIER_CANNOT_SHIP_TO_POBOX
    """

    rejection_reason_message: str = attrs.field(
        kw_only=True,
    )
    """
    A localized human readable description of the rejected reason.
    """

    shipping_service_name: str = attrs.field(
        kw_only=True,
    )
    """
    The rejected shipping service localized name. e.g. FedEx Standard Overnight
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RejectedShippingServiceList:

    pass


@attrs.define
class RestrictedSetValues:

    pass


@attrs.define
class SellerInputDefinition:

    data_type: str = attrs.field(
        kw_only=True,
    )
    """
    The data type of the additional input field.
    """

    input_display_text: str = attrs.field(
        kw_only=True,
    )
    """
    The display text for the additional input field.
    """

    is_required: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the additional input field is required.
    """

    constraints: "Constraints" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    input_target: "InputTargetType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    restricted_set_values: "RestrictedSetValues" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    stored_value: "AdditionalSellerInput" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SellerOrderId:

    pass


@attrs.define
class Shipment:

    amazon_order_id: "AmazonOrderId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    created_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    insurance: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_list: "ItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label: "Label" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    last_updated_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    package_dimensions: "PackageDimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_order_id: "SellerOrderId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service: "ShippingService" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    status: "ShipmentStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tracking_id: "TrackingId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentId:

    pass


@attrs.define
class ShipmentRequestDetails:

    amazon_order_id: "AmazonOrderId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_list: "ItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_customization: "LabelCustomization" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    must_arrive_by_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    package_dimensions: "PackageDimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    seller_order_id: "SellerOrderId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service_options: "ShippingServiceOptions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentStatus:

    pass


@attrs.define
class ShippingOfferingFilter:

    include_complex_shipping_options: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, include complex shipping options.
    """

    include_packing_slip_with_label: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, include a packing slip with the label.
    """

    carrier_will_pick_up: "CarrierWillPickUpOption" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    delivery_experience: "DeliveryExperienceOption" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShippingService:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """

    requires_additional_seller_inputs: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, additional seller inputs are required.
    """

    shipping_service_name: str = attrs.field(
        kw_only=True,
    )
    """
    A plain text representation of a carrier's shipping service. For example, "UPS Ground" or "FedEx Standard Overnight".
    """

    shipping_service_offer_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon-defined shipping service offer identifier.
    """

    available_format_options_for_label: "AvailableFormatOptionsForLabelList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    available_label_formats: "LabelFormatList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    available_shipping_service_options: "AvailableShippingServiceOptions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    earliest_estimated_delivery_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    latest_estimated_delivery_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rate: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_service_options: "ShippingServiceOptions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShippingServiceIdentifier:

    pass


@attrs.define
class ShippingServiceList:

    pass


@attrs.define
class ShippingServiceOptions:

    carrier_will_pick_up: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the carrier will pick up the package.
        Note: Scheduled carrier pickup is available only using Dynamex (US), DPD (UK), and Royal Mail (UK).
    """

    carrier_will_pick_up_option: "CarrierWillPickUpOption" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    declared_value: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    delivery_experience: "DeliveryExperienceType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_format: "LabelFormat" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StandardIdForLabel:

    pass


@attrs.define
class StateOrProvinceCode:

    pass


@attrs.define
class TemporarilyUnavailableCarrier:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """

    pass


@attrs.define
class TemporarilyUnavailableCarrierList:

    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrier:

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """

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

    unit: "UnitOfWeight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value: "WeightValue" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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
        shipment_request_details: dict[str, Any],
        shipping_service_id: str,
        shipping_service_offer_id: str = None,
        hazmat_type: Union[Literal["None"], Literal["LQHazmat"]] = None,
        label_format_option: dict[str, Any] = None,
        shipment_level_seller_inputs_list: list["AdditionalSellerInputs"] = None,
    ):
        """
        Create a shipment with the information provided.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_request_details: Shipment information required for requesting shipping service offers or for creating a shipment.
            shipping_service_id: An Amazon-defined shipping service identifier.
            shipping_service_offer_id: Identifies a shipping service order made by a carrier.
            hazmat_type: Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
            label_format_option: Whether to include a packing slip.
            shipment_level_seller_inputs_list: A list of additional seller input pairs required to purchase shipping.
        """
        url = "/mfn/v0/shipments"
        values = (
            shipment_request_details,
            shipping_service_id,
            shipping_service_offer_id,
            hazmat_type,
            label_format_option,
            shipment_level_seller_inputs_list,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_shipment_params)
        return response

    _create_shipment_params = (  # name, param in
        ("ShipmentRequestDetails", "body"),
        ("ShippingServiceId", "body"),
        ("ShippingServiceOfferId", "body"),
        ("HazmatType", "body"),
        ("LabelFormatOption", "body"),
        ("ShipmentLevelSellerInputsList", "body"),
    )

    def get_additional_seller_inputs(
        self,
        shipping_service_id: str,
        ship_from_address: dict[str, Any],
        order_id: str,
    ):
        """
        Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipping_service_id: An Amazon-defined shipping service identifier.
            ship_from_address: The postal address information.
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/mfn/v0/additionalSellerInputs"
        values = (
            shipping_service_id,
            ship_from_address,
            order_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_additional_seller_inputs_params)
        return response

    _get_additional_seller_inputs_params = (  # name, param in
        ("ShippingServiceId", "body"),
        ("ShipFromAddress", "body"),
        ("OrderId", "body"),
    )

    def get_additional_seller_inputs_old(
        self,
        shipping_service_id: str,
        ship_from_address: dict[str, Any],
        order_id: str,
    ):
        """
        Get a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipping_service_id: An Amazon-defined shipping service identifier.
            ship_from_address: The postal address information.
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
        """
        url = "/mfn/v0/sellerInputs"
        values = (
            shipping_service_id,
            ship_from_address,
            order_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_additional_seller_inputs_old_params)
        return response

    _get_additional_seller_inputs_old_params = (  # name, param in
        ("ShippingServiceId", "body"),
        ("ShipFromAddress", "body"),
        ("OrderId", "body"),
    )

    def get_eligible_shipment_services(
        self,
        shipment_request_details: dict[str, Any],
        shipping_offering_filter: dict[str, Any] = None,
    ):
        """
        Returns a list of shipping service offers that satisfy the specified shipment request details.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_request_details: Shipment information required for requesting shipping service offers or for creating a shipment.
            shipping_offering_filter: Filter for use when requesting eligible shipping services.
        """
        url = "/mfn/v0/eligibleShippingServices"
        values = (
            shipment_request_details,
            shipping_offering_filter,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_eligible_shipment_services_params)
        return response

    _get_eligible_shipment_services_params = (  # name, param in
        ("ShipmentRequestDetails", "body"),
        ("ShippingOfferingFilter", "body"),
    )

    def get_eligible_shipment_services_old(
        self,
        shipment_request_details: dict[str, Any],
        shipping_offering_filter: dict[str, Any] = None,
    ):
        """
        Returns a list of shipping service offers that satisfy the specified shipment request details.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_request_details: Shipment information required for requesting shipping service offers or for creating a shipment.
            shipping_offering_filter: Filter for use when requesting eligible shipping services.
        """
        url = "/mfn/v0/eligibleServices"
        values = (
            shipment_request_details,
            shipping_offering_filter,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_eligible_shipment_services_old_params)
        return response

    _get_eligible_shipment_services_old_params = (  # name, param in
        ("ShipmentRequestDetails", "body"),
        ("ShippingOfferingFilter", "body"),
    )

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
