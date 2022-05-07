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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalInputs:
    """
    Maps the additional seller input to the definition. The key to the map is the field name.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _additional_inputs_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AdditionalInputs(**data)

    additional_input_field_name: Optional[str] = attrs.field()
    """
    The field name.
    """

    seller_input_definition: Optional["SellerInputDefinition"] = attrs.field()
    """
    Specifies characteristics that apply to a seller input.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalSellerInput:
    """
    Additional information required to purchase shipping.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _additional_seller_input_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AdditionalSellerInput(**data)

    data_type: Optional[str] = attrs.field()
    """
    The data type of the additional information.
    """

    value_as_address: Optional["Address"] = attrs.field()
    """
    The postal address information.
    """

    value_as_boolean: Optional[bool] = attrs.field()
    """
    The value when the data type is boolean.
    """

    value_as_currency: Optional["CurrencyAmount"] = attrs.field()
    """
    Currency type and amount.
    """

    value_as_dimension: Optional["Length"] = attrs.field()
    """
    The length.
    """

    value_as_integer: Optional[int] = attrs.field()
    """
    The value when the data type is integer.
    """

    value_as_string: Optional[str] = attrs.field()
    """
    The value when the data type is string.
    """

    value_as_timestamp: Optional["Timestamp"] = attrs.field()

    value_as_weight: Optional["Weight"] = attrs.field()
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalSellerInputs:
    """
    An additional set of seller inputs required to purchase shipping.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _additional_seller_inputs_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AdditionalSellerInputs(**data)

    additional_input_field_name: str = attrs.field()
    """
    The name of the additional input field.
    """

    additional_seller_input: "AdditionalSellerInput" = attrs.field()
    """
    Additional information required to purchase shipping.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    The postal address information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Address(**data)

    address_line1: "AddressLine1" = attrs.field()
    """
    The street address information.
    """

    address_line2: Optional["AddressLine2"] = attrs.field(
        default=None,
    )
    """
    Additional street address information.
    """

    address_line3: Optional["AddressLine3"] = attrs.field(
        default=None,
    )
    """
    Additional street address information.
    """

    city: "City" = attrs.field()
    """
    The city.
    """

    country_code: "CountryCode" = attrs.field()
    """
    The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
    """

    district_or_county: Optional["DistrictOrCounty"] = attrs.field(
        default=None,
    )
    """
    The district or county.
    """

    email: "EmailAddress" = attrs.field()
    """
    The email address.
    """

    name: "AddressName" = attrs.field()
    """
    The name of the addressee, or business name.
    """

    phone: "PhoneNumber" = attrs.field()
    """
    The phone number.
    """

    postal_code: "PostalCode" = attrs.field()
    """
    The zip code or postal code.
    """

    state_or_province_code: Optional["StateOrProvinceCode"] = attrs.field(
        default=None,
    )
    """
    The state or province code. **Note.** Required in the Canada, US, and UK marketplaces. Also required for shipments originating from China.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressLine1:
    """
    The street address information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_line1_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AddressLine1(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressLine2:
    """
    Additional street address information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_line2_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AddressLine2(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressLine3:
    """
    Additional street address information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_line3_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AddressLine3(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressName:
    """
    The name of the addressee, or business name.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AddressName(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AmazonOrderId:
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _amazon_order_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AmazonOrderId(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableCarrierWillPickUpOption:
    """
    Indicates whether the carrier will pick up the package, and what fee is charged, if any.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _available_carrier_will_pick_up_option_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AvailableCarrierWillPickUpOption(**data)

    carrier_will_pick_up_option: "CarrierWillPickUpOption" = attrs.field()
    """
    Carrier will pick up option.
    """

    charge: "CurrencyAmount" = attrs.field()
    """
    Currency type and amount.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableDeliveryExperienceOption:
    """
    The available delivery confirmation options, and the fee charged, if any.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _available_delivery_experience_option_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AvailableDeliveryExperienceOption(**data)

    charge: "CurrencyAmount" = attrs.field()
    """
    Currency type and amount.
    """

    delivery_experience_option: "DeliveryExperienceOption" = attrs.field()
    """
    The delivery confirmation level.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableShippingServiceOptions:
    """
    The available shipping service options.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _available_shipping_service_options_name_convert
        data = {name_convert[k]: v for k, v in data}
        return AvailableShippingServiceOptions(**data)

    available_carrier_will_pick_up_options: List["AvailableCarrierWillPickUpOption"] = attrs.field()
    """
    List of available carrier pickup options.
    """

    available_delivery_experience_options: List["AvailableDeliveryExperienceOption"] = attrs.field()
    """
    List of available delivery experience options.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelShipmentResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _cancel_shipment_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CancelShipmentResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Shipment"] = attrs.field()
    """
    The details of a shipment, including the shipment status.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CarrierWillPickUpOption:
    """
    Carrier will pick up option.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _carrier_will_pick_up_option_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CarrierWillPickUpOption(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class City:
    """
    The city.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _city_name_convert
        data = {name_convert[k]: v for k, v in data}
        return City(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Constraint:
    """
    A validation constraint.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _constraint_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Constraint(**data)

    validation_reg_ex: Optional[str] = attrs.field(
        default=None,
    )
    """
    A regular expression.
    """

    validation_string: str = attrs.field()
    """
    A validation string.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CountryCode:
    """
    The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _country_code_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CountryCode(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentRequest:
    """
    Request schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_shipment_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateShipmentRequest(**data)

    hazmat_type: Optional["HazmatType"] = attrs.field(
        default=None,
    )
    """
    Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
    """

    label_format_option: Optional["LabelFormatOptionRequest"] = attrs.field(
        default=None,
    )
    """
    Whether to include a packing slip.
    """

    shipment_level_seller_inputs_list: Optional[List["AdditionalSellerInputs"]] = attrs.field(
        default=None,
    )
    """
    A list of additional seller input pairs required to purchase shipping.
    """

    shipment_request_details: "ShipmentRequestDetails" = attrs.field()
    """
    Shipment information required for requesting shipping service offers or for creating a shipment.
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    """
    An Amazon-defined shipping service identifier.
    """

    shipping_service_offer_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    Identifies a shipping service order made by a carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _create_shipment_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CreateShipmentResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Shipment"] = attrs.field()
    """
    The details of a shipment, including the shipment status.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CurrencyAmount:
    """
    Currency type and amount.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _currency_amount_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CurrencyAmount(**data)

    amount: float = attrs.field()
    """
    The currency amount.

    Extra fields:
    {'schema_format': 'double'}
    """

    currency_code: str = attrs.field()
    """
    Three-digit currency code in ISO 4217 format.

    Extra fields:
    {'maxLength': 3}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CustomTextForLabel:
    """
    Custom text to print on the label.
        Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support CustomTextForLabel.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _custom_text_for_label_name_convert
        data = {name_convert[k]: v for k, v in data}
        return CustomTextForLabel(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeliveryExperienceOption:
    """
    The delivery confirmation level.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _delivery_experience_option_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DeliveryExperienceOption(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeliveryExperienceType:
    """
    The delivery confirmation level.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _delivery_experience_type_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DeliveryExperienceType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DistrictOrCounty:
    """
    The district or county.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _district_or_county_name_convert
        data = {name_convert[k]: v for k, v in data}
        return DistrictOrCounty(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class EmailAddress:
    """
    The email address.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _email_address_name_convert
        data = {name_convert[k]: v for k, v in data}
        return EmailAddress(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FileContents:
    """
    The document data and checksum.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _file_contents_name_convert
        data = {name_convert[k]: v for k, v in data}
        return FileContents(**data)

    checksum: str = attrs.field()
    """
    An MD5 hash to validate the PDF document data, in the form of a Base64-encoded string.
    """

    contents: str = attrs.field()
    """
    Data for printing labels, in the form of a Base64-encoded, GZip-compressed string.
    """

    file_type: "FileType" = attrs.field()
    """
    The file type for a label.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FileType:
    """
    The file type for a label.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _file_type_name_convert
        data = {name_convert[k]: v for k, v in data}
        return FileType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAdditionalSellerInputsRequest:
    """
    Request schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_additional_seller_inputs_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetAdditionalSellerInputsRequest(**data)

    order_id: "AmazonOrderId" = attrs.field()
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    ship_from_address: "Address" = attrs.field()
    """
    The postal address information.
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    """
    An Amazon-defined shipping service identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAdditionalSellerInputsResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_additional_seller_inputs_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetAdditionalSellerInputsResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetAdditionalSellerInputsResult"] = attrs.field()
    """
    The payload for the getAdditionalSellerInputs operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAdditionalSellerInputsResult:
    """
    The payload for the getAdditionalSellerInputs operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_additional_seller_inputs_result_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetAdditionalSellerInputsResult(**data)

    item_level_fields_list: Optional[List["ItemLevelFields"]] = attrs.field()
    """
    A list of item level fields.
    """

    shipment_level_fields: Optional[List["AdditionalInputs"]] = attrs.field()
    """
    A list of additional inputs.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetEligibleShipmentServicesRequest:
    """
    Request schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_eligible_shipment_services_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetEligibleShipmentServicesRequest(**data)

    shipment_request_details: "ShipmentRequestDetails" = attrs.field()
    """
    Shipment information required for requesting shipping service offers or for creating a shipment.
    """

    shipping_offering_filter: Optional["ShippingOfferingFilter"] = attrs.field(
        default=None,
    )
    """
    Filter for use when requesting eligible shipping services.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetEligibleShipmentServicesResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_eligible_shipment_services_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetEligibleShipmentServicesResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetEligibleShipmentServicesResult"] = attrs.field()
    """
    The payload for the getEligibleShipmentServices operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetEligibleShipmentServicesResult:
    """
    The payload for the getEligibleShipmentServices operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_eligible_shipment_services_result_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetEligibleShipmentServicesResult(**data)

    rejected_shipping_service_list: Optional[List["RejectedShippingService"]] = attrs.field(
        default=None,
    )
    """
    List of services that were for some reason unavailable for this request
    """

    shipping_service_list: List["ShippingService"] = attrs.field()
    """
    A list of shipping services offers.
    """

    temporarily_unavailable_carrier_list: Optional[List["TemporarilyUnavailableCarrier"]] = attrs.field(
        default=None,
    )
    """
    A list of temporarily unavailable carriers.
    """

    terms_and_conditions_not_accepted_carrier_list: Optional[
        List["TermsAndConditionsNotAcceptedCarrier"]
    ] = attrs.field(
        default=None,
    )
    """
    List of carriers whose terms and conditions were not accepted by the seller.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentResponse:
    """
    Response schema.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_shipment_response_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GetShipmentResponse(**data)

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Shipment"] = attrs.field()
    """
    The details of a shipment, including the shipment status.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class HazmatType:
    """
    Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _hazmat_type_name_convert
        data = {name_convert[k]: v for k, v in data}
        return HazmatType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class InputTargetType:
    """
    Indicates whether the additional seller input is at the item or shipment level.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _input_target_type_name_convert
        data = {name_convert[k]: v for k, v in data}
        return InputTargetType(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    An Amazon order item identifier and a quantity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Item(**data)

    item_description: Optional["ItemDescription"] = attrs.field(
        default=None,
    )
    """
    The description of the item.
    """

    item_level_seller_inputs_list: Optional[List["AdditionalSellerInputs"]] = attrs.field(
        default=None,
    )
    """
    A list of additional seller input pairs required to purchase shipping.
    """

    item_weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """

    order_item_id: "OrderItemId" = attrs.field()
    """
    An Amazon-defined identifier for an individual item in an order.
    """

    quantity: "ItemQuantity" = attrs.field()
    """
    The number of items.
    """

    transparency_code_list: Optional[List["TransparencyCode"]] = attrs.field(
        default=None,
    )
    """
    A list of transparency codes.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDescription:
    """
    The description of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_description_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ItemDescription(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemLevelFields:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_level_fields_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ItemLevelFields(**data)

    additional_inputs: List["AdditionalInputs"] = attrs.field()
    """
    A list of additional inputs.
    """

    asin: str = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    The number of items.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_quantity_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ItemQuantity(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Label:
    """
    Data for creating a shipping label and dimensions for printing the label.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Label(**data)

    custom_text_for_label: Optional["CustomTextForLabel"] = attrs.field(
        default=None,
    )
    """
    Custom text to print on the label.
        Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support CustomTextForLabel.
    """

    dimensions: "LabelDimensions" = attrs.field()
    """
    Dimensions for printing a shipping label.
    """

    file_contents: "FileContents" = attrs.field()
    """
    The document data and checksum.
    """

    label_format: Optional["LabelFormat"] = attrs.field(
        default=None,
    )
    """
    The label format.
    """

    standard_id_for_label: Optional["StandardIdForLabel"] = attrs.field(
        default=None,
    )
    """
    The type of standard identifier to print on the label.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelCustomization:
    """
    Custom text for shipping labels.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_customization_name_convert
        data = {name_convert[k]: v for k, v in data}
        return LabelCustomization(**data)

    custom_text_for_label: Optional["CustomTextForLabel"] = attrs.field()
    """
    Custom text to print on the label.
        Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support CustomTextForLabel.
    """

    standard_id_for_label: Optional["StandardIdForLabel"] = attrs.field()
    """
    The type of standard identifier to print on the label.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelDimension:
    """
    A label dimension.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_dimension_name_convert
        data = {name_convert[k]: v for k, v in data}
        return LabelDimension(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelDimensions:
    """
    Dimensions for printing a shipping label.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_dimensions_name_convert
        data = {name_convert[k]: v for k, v in data}
        return LabelDimensions(**data)

    length: "LabelDimension" = attrs.field()
    """
    A label dimension.
    """

    unit: "UnitOfLength" = attrs.field()
    """
    The unit of length.
    """

    width: "LabelDimension" = attrs.field()
    """
    A label dimension.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormat:
    """
    The label format.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_format_name_convert
        data = {name_convert[k]: v for k, v in data}
        return LabelFormat(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormatOption:
    """
    The label format details and whether to include a packing slip.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_format_option_name_convert
        data = {name_convert[k]: v for k, v in data}
        return LabelFormatOption(**data)

    include_packing_slip_with_label: Optional[bool] = attrs.field()
    """
    When true, include a packing slip with the label.
    """

    label_format: Optional["LabelFormat"] = attrs.field()
    """
    The label format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormatOptionRequest:
    """
    Whether to include a packing slip.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _label_format_option_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return LabelFormatOptionRequest(**data)

    include_packing_slip_with_label: Optional[bool] = attrs.field()
    """
    When true, include a packing slip with the label.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Length:
    """
    The length.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _length_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Length(**data)

    unit: Optional["UnitOfLength"] = attrs.field()
    """
    The unit of length.
    """

    value: Optional[float] = attrs.field()
    """
    The value in units.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemId:
    """
    An Amazon-defined identifier for an individual item in an order.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_item_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderItemId(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackageDimension:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _package_dimension_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PackageDimension(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackageDimensions:
    """
    The dimensions of a package contained in a shipment.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _package_dimensions_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PackageDimensions(**data)

    height: Optional["PackageDimension"] = attrs.field()

    length: Optional["PackageDimension"] = attrs.field()

    predefined_package_dimensions: Optional["PredefinedPackageDimensions"] = attrs.field()
    """
    An enumeration of predefined parcel tokens. If you specify a PredefinedPackageDimensions token, you are not obligated to use a branded package from a carrier. For example, if you specify the FedEx_Box_10kg token, you do not have to use that particular package from FedEx. You are only obligated to use a box that matches the dimensions specified by the token.
        Note: Please note that carriers can have restrictions on the type of package allowed for certain ship methods. Check the carrier website for all details. Example: Flat rate pricing is available when materials are sent by USPS in a USPS-produced Flat Rate Envelope or Box.
    """

    unit: Optional["UnitOfLength"] = attrs.field()
    """
    The unit of length.
    """

    width: Optional["PackageDimension"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PhoneNumber:
    """
    The phone number.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _phone_number_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PhoneNumber(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostalCode:
    """
    The zip code or postal code.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _postal_code_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PostalCode(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PredefinedPackageDimensions:
    """
    An enumeration of predefined parcel tokens. If you specify a PredefinedPackageDimensions token, you are not obligated to use a branded package from a carrier. For example, if you specify the FedEx_Box_10kg token, you do not have to use that particular package from FedEx. You are only obligated to use a box that matches the dimensions specified by the token.
        Note: Please note that carriers can have restrictions on the type of package allowed for certain ship methods. Check the carrier website for all details. Example: Flat rate pricing is available when materials are sent by USPS in a USPS-produced Flat Rate Envelope or Box.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _predefined_package_dimensions_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PredefinedPackageDimensions(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RejectedShippingService:
    """
    Information about a rejected shipping service
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _rejected_shipping_service_name_convert
        data = {name_convert[k]: v for k, v in data}
        return RejectedShippingService(**data)

    carrier_name: str = attrs.field()
    """
    The rejected shipping carrier name. e.g. USPS
    """

    rejection_reason_code: str = attrs.field()
    """
    A reason code meant to be consumed programatically. e.g. CARRIER_CANNOT_SHIP_TO_POBOX
    """

    rejection_reason_message: Optional[str] = attrs.field(
        default=None,
    )
    """
    A localized human readable description of the rejected reason.
    """

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    """
    An Amazon-defined shipping service identifier.
    """

    shipping_service_name: str = attrs.field()
    """
    The rejected shipping service localized name. e.g. FedEx Standard Overnight
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerInputDefinition:
    """
    Specifies characteristics that apply to a seller input.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _seller_input_definition_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SellerInputDefinition(**data)

    constraints: List["Constraint"] = attrs.field()
    """
    List of constraints.
    """

    data_type: str = attrs.field()
    """
    The data type of the additional input field.
    """

    input_display_text: str = attrs.field()
    """
    The display text for the additional input field.
    """

    input_target: Optional["InputTargetType"] = attrs.field(
        default=None,
    )
    """
    Indicates whether the additional seller input is at the item or shipment level.
    """

    is_required: bool = attrs.field()
    """
    When true, the additional input field is required.
    """

    restricted_set_values: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The set of fixed values in an additional seller input.
    """

    stored_value: "AdditionalSellerInput" = attrs.field()
    """
    Additional information required to purchase shipping.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerOrderId:
    """
    A seller-defined order identifier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _seller_order_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SellerOrderId(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Shipment:
    """
    The details of a shipment, including the shipment status.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Shipment(**data)

    amazon_order_id: "AmazonOrderId" = attrs.field()
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    created_date: "Timestamp" = attrs.field()

    insurance: "CurrencyAmount" = attrs.field()
    """
    Currency type and amount.
    """

    item_list: List["Item"] = attrs.field()
    """
    The list of items to be included in a shipment.
    """

    label: "Label" = attrs.field()
    """
    Data for creating a shipping label and dimensions for printing the label.
    """

    last_updated_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    package_dimensions: "PackageDimensions" = attrs.field()
    """
    The dimensions of a package contained in a shipment.
    """

    seller_order_id: Optional["SellerOrderId"] = attrs.field(
        default=None,
    )
    """
    A seller-defined order identifier.
    """

    ship_from_address: "Address" = attrs.field()
    """
    The postal address information.
    """

    ship_to_address: "Address" = attrs.field()
    """
    The postal address information.
    """

    shipment_id: "ShipmentId" = attrs.field()
    """
    An Amazon-defined shipment identifier.
    """

    shipping_service: "ShippingService" = attrs.field()
    """
    A shipping service offer made by a carrier.
    """

    status: "ShipmentStatus" = attrs.field()
    """
    The shipment status.
    """

    tracking_id: Optional["TrackingId"] = attrs.field(
        default=None,
    )
    """
    The shipment tracking identifier provided by the carrier.
    """

    weight: "Weight" = attrs.field()
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentId:
    """
    An Amazon-defined shipment identifier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShipmentId(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentRequestDetails:
    """
    Shipment information required for requesting shipping service offers or for creating a shipment.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_request_details_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShipmentRequestDetails(**data)

    amazon_order_id: "AmazonOrderId" = attrs.field()
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    item_list: List["Item"] = attrs.field()
    """
    The list of items to be included in a shipment.
    """

    label_customization: Optional["LabelCustomization"] = attrs.field(
        default=None,
    )
    """
    Custom text for shipping labels.
    """

    must_arrive_by_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    package_dimensions: "PackageDimensions" = attrs.field()
    """
    The dimensions of a package contained in a shipment.
    """

    seller_order_id: Optional["SellerOrderId"] = attrs.field(
        default=None,
    )
    """
    A seller-defined order identifier.
    """

    ship_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    ship_from_address: "Address" = attrs.field()
    """
    The postal address information.
    """

    shipping_service_options: "ShippingServiceOptions" = attrs.field()
    """
    Extra services provided by a carrier.
    """

    weight: "Weight" = attrs.field()
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentStatus:
    """
    The shipment status.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_status_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShipmentStatus(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingOfferingFilter:
    """
    Filter for use when requesting eligible shipping services.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipping_offering_filter_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShippingOfferingFilter(**data)

    carrier_will_pick_up: Optional["CarrierWillPickUpOption"] = attrs.field()
    """
    Carrier will pick up option.
    """

    delivery_experience: Optional["DeliveryExperienceOption"] = attrs.field()
    """
    The delivery confirmation level.
    """

    include_complex_shipping_options: Optional[bool] = attrs.field()
    """
    When true, include complex shipping options.
    """

    include_packing_slip_with_label: Optional[bool] = attrs.field()
    """
    When true, include a packing slip with the label.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingService:
    """
    A shipping service offer made by a carrier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipping_service_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShippingService(**data)

    available_format_options_for_label: Optional[List["LabelFormatOption"]] = attrs.field(
        default=None,
    )
    """
    The available label formats.
    """

    available_label_formats: Optional[List["LabelFormat"]] = attrs.field(
        default=None,
    )
    """
    List of label formats.
    """

    available_shipping_service_options: Optional["AvailableShippingServiceOptions"] = attrs.field(
        default=None,
    )
    """
    The available shipping service options.
    """

    carrier_name: str = attrs.field()
    """
    The name of the carrier.
    """

    earliest_estimated_delivery_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    latest_estimated_delivery_date: Optional["Timestamp"] = attrs.field(
        default=None,
    )

    rate: "CurrencyAmount" = attrs.field()
    """
    Currency type and amount.
    """

    requires_additional_seller_inputs: bool = attrs.field()
    """
    When true, additional seller inputs are required.
    """

    ship_date: "Timestamp" = attrs.field()

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    """
    An Amazon-defined shipping service identifier.
    """

    shipping_service_name: str = attrs.field()
    """
    A plain text representation of a carrier's shipping service. For example, "UPS Ground" or "FedEx Standard Overnight".
    """

    shipping_service_offer_id: str = attrs.field()
    """
    An Amazon-defined shipping service offer identifier.
    """

    shipping_service_options: "ShippingServiceOptions" = attrs.field()
    """
    Extra services provided by a carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingServiceIdentifier:
    """
    An Amazon-defined shipping service identifier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipping_service_identifier_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShippingServiceIdentifier(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingServiceOptions:
    """
    Extra services provided by a carrier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipping_service_options_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ShippingServiceOptions(**data)

    carrier_will_pick_up: bool = attrs.field()
    """
    When true, the carrier will pick up the package.
        Note: Scheduled carrier pickup is available only using Dynamex (US), DPD (UK), and Royal Mail (UK).
    """

    carrier_will_pick_up_option: Optional["CarrierWillPickUpOption"] = attrs.field(
        default=None,
    )
    """
    Carrier will pick up option.
    """

    declared_value: Optional["CurrencyAmount"] = attrs.field(
        default=None,
    )
    """
    Currency type and amount.
    """

    delivery_experience: "DeliveryExperienceType" = attrs.field()
    """
    The delivery confirmation level.
    """

    label_format: Optional["LabelFormat"] = attrs.field(
        default=None,
    )
    """
    The label format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardIdForLabel:
    """
    The type of standard identifier to print on the label.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _standard_id_for_label_name_convert
        data = {name_convert[k]: v for k, v in data}
        return StandardIdForLabel(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class StateOrProvinceCode:
    """
    The state or province code. **Note.** Required in the Canada, US, and UK marketplaces. Also required for shipments originating from China.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _state_or_province_code_name_convert
        data = {name_convert[k]: v for k, v in data}
        return StateOrProvinceCode(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TemporarilyUnavailableCarrier:
    """
    A carrier who is temporarily unavailable, most likely due to a service outage experienced by the carrier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _temporarily_unavailable_carrier_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TemporarilyUnavailableCarrier(**data)

    carrier_name: str = attrs.field()
    """
    The name of the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TermsAndConditionsNotAcceptedCarrier:
    """
    A carrier whose terms and conditions have not been accepted by the seller.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _terms_and_conditions_not_accepted_carrier_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TermsAndConditionsNotAcceptedCarrier(**data)

    carrier_name: str = attrs.field()
    """
    The name of the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Timestamp:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _timestamp_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Timestamp(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingId:
    """
    The shipment tracking identifier provided by the carrier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tracking_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TrackingId(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransparencyCode:
    """
    The Transparency code associated with the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transparency_code_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TransparencyCode(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnitOfLength:
    """
    The unit of length.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _unit_of_length_name_convert
        data = {name_convert[k]: v for k, v in data}
        return UnitOfLength(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnitOfWeight:
    """
    The unit of weight.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _unit_of_weight_name_convert
        data = {name_convert[k]: v for k, v in data}
        return UnitOfWeight(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _weight_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Weight(**data)

    unit: "UnitOfWeight" = attrs.field()
    """
    The unit of weight.
    """

    value: "WeightValue" = attrs.field()
    """
    The weight value.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class WeightValue:
    """
    The weight value.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _weight_value_name_convert
        data = {name_convert[k]: v for k, v in data}
        return WeightValue(**data)

    pass


_additional_inputs_name_convert = {
    "AdditionalInputFieldName": "additional_input_field_name",
    "SellerInputDefinition": "seller_input_definition",
}

_additional_seller_input_name_convert = {
    "DataType": "data_type",
    "ValueAsAddress": "value_as_address",
    "ValueAsBoolean": "value_as_boolean",
    "ValueAsCurrency": "value_as_currency",
    "ValueAsDimension": "value_as_dimension",
    "ValueAsInteger": "value_as_integer",
    "ValueAsString": "value_as_string",
    "ValueAsTimestamp": "value_as_timestamp",
    "ValueAsWeight": "value_as_weight",
}

_additional_seller_inputs_name_convert = {
    "AdditionalInputFieldName": "additional_input_field_name",
    "AdditionalSellerInput": "additional_seller_input",
}

_address_name_convert = {
    "AddressLine1": "address_line1",
    "AddressLine2": "address_line2",
    "AddressLine3": "address_line3",
    "City": "city",
    "CountryCode": "country_code",
    "DistrictOrCounty": "district_or_county",
    "Email": "email",
    "Name": "name",
    "Phone": "phone",
    "PostalCode": "postal_code",
    "StateOrProvinceCode": "state_or_province_code",
}

_address_line1_name_convert = {}

_address_line2_name_convert = {}

_address_line3_name_convert = {}

_address_name_name_convert = {}

_amazon_order_id_name_convert = {}

_available_carrier_will_pick_up_option_name_convert = {
    "CarrierWillPickUpOption": "carrier_will_pick_up_option",
    "Charge": "charge",
}

_available_delivery_experience_option_name_convert = {
    "Charge": "charge",
    "DeliveryExperienceOption": "delivery_experience_option",
}

_available_shipping_service_options_name_convert = {
    "AvailableCarrierWillPickUpOptions": "available_carrier_will_pick_up_options",
    "AvailableDeliveryExperienceOptions": "available_delivery_experience_options",
}

_cancel_shipment_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_carrier_will_pick_up_option_name_convert = {}

_city_name_convert = {}

_constraint_name_convert = {
    "ValidationRegEx": "validation_reg_ex",
    "ValidationString": "validation_string",
}

_country_code_name_convert = {}

_create_shipment_request_name_convert = {
    "HazmatType": "hazmat_type",
    "LabelFormatOption": "label_format_option",
    "ShipmentLevelSellerInputsList": "shipment_level_seller_inputs_list",
    "ShipmentRequestDetails": "shipment_request_details",
    "ShippingServiceId": "shipping_service_id",
    "ShippingServiceOfferId": "shipping_service_offer_id",
}

_create_shipment_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_currency_amount_name_convert = {
    "Amount": "amount",
    "CurrencyCode": "currency_code",
}

_custom_text_for_label_name_convert = {}

_delivery_experience_option_name_convert = {}

_delivery_experience_type_name_convert = {}

_district_or_county_name_convert = {}

_email_address_name_convert = {}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_file_contents_name_convert = {
    "Checksum": "checksum",
    "Contents": "contents",
    "FileType": "file_type",
}

_file_type_name_convert = {}

_get_additional_seller_inputs_request_name_convert = {
    "OrderId": "order_id",
    "ShipFromAddress": "ship_from_address",
    "ShippingServiceId": "shipping_service_id",
}

_get_additional_seller_inputs_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_additional_seller_inputs_result_name_convert = {
    "ItemLevelFieldsList": "item_level_fields_list",
    "ShipmentLevelFields": "shipment_level_fields",
}

_get_eligible_shipment_services_request_name_convert = {
    "ShipmentRequestDetails": "shipment_request_details",
    "ShippingOfferingFilter": "shipping_offering_filter",
}

_get_eligible_shipment_services_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_eligible_shipment_services_result_name_convert = {
    "RejectedShippingServiceList": "rejected_shipping_service_list",
    "ShippingServiceList": "shipping_service_list",
    "TemporarilyUnavailableCarrierList": "temporarily_unavailable_carrier_list",
    "TermsAndConditionsNotAcceptedCarrierList": "terms_and_conditions_not_accepted_carrier_list",
}

_get_shipment_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_hazmat_type_name_convert = {}

_input_target_type_name_convert = {}

_item_name_convert = {
    "ItemDescription": "item_description",
    "ItemLevelSellerInputsList": "item_level_seller_inputs_list",
    "ItemWeight": "item_weight",
    "OrderItemId": "order_item_id",
    "Quantity": "quantity",
    "TransparencyCodeList": "transparency_code_list",
}

_item_description_name_convert = {}

_item_level_fields_name_convert = {
    "AdditionalInputs": "additional_inputs",
    "Asin": "asin",
}

_item_quantity_name_convert = {}

_label_name_convert = {
    "CustomTextForLabel": "custom_text_for_label",
    "Dimensions": "dimensions",
    "FileContents": "file_contents",
    "LabelFormat": "label_format",
    "StandardIdForLabel": "standard_id_for_label",
}

_label_customization_name_convert = {
    "CustomTextForLabel": "custom_text_for_label",
    "StandardIdForLabel": "standard_id_for_label",
}

_label_dimension_name_convert = {}

_label_dimensions_name_convert = {
    "Length": "length",
    "Unit": "unit",
    "Width": "width",
}

_label_format_name_convert = {}

_label_format_option_name_convert = {
    "IncludePackingSlipWithLabel": "include_packing_slip_with_label",
    "LabelFormat": "label_format",
}

_label_format_option_request_name_convert = {
    "IncludePackingSlipWithLabel": "include_packing_slip_with_label",
}

_length_name_convert = {
    "unit": "unit",
    "value": "value",
}

_order_item_id_name_convert = {}

_package_dimension_name_convert = {}

_package_dimensions_name_convert = {
    "Height": "height",
    "Length": "length",
    "PredefinedPackageDimensions": "predefined_package_dimensions",
    "Unit": "unit",
    "Width": "width",
}

_phone_number_name_convert = {}

_postal_code_name_convert = {}

_predefined_package_dimensions_name_convert = {}

_rejected_shipping_service_name_convert = {
    "CarrierName": "carrier_name",
    "RejectionReasonCode": "rejection_reason_code",
    "RejectionReasonMessage": "rejection_reason_message",
    "ShippingServiceId": "shipping_service_id",
    "ShippingServiceName": "shipping_service_name",
}

_seller_input_definition_name_convert = {
    "Constraints": "constraints",
    "DataType": "data_type",
    "InputDisplayText": "input_display_text",
    "InputTarget": "input_target",
    "IsRequired": "is_required",
    "RestrictedSetValues": "restricted_set_values",
    "StoredValue": "stored_value",
}

_seller_order_id_name_convert = {}

_shipment_name_convert = {
    "AmazonOrderId": "amazon_order_id",
    "CreatedDate": "created_date",
    "Insurance": "insurance",
    "ItemList": "item_list",
    "Label": "label",
    "LastUpdatedDate": "last_updated_date",
    "PackageDimensions": "package_dimensions",
    "SellerOrderId": "seller_order_id",
    "ShipFromAddress": "ship_from_address",
    "ShipToAddress": "ship_to_address",
    "ShipmentId": "shipment_id",
    "ShippingService": "shipping_service",
    "Status": "status",
    "TrackingId": "tracking_id",
    "Weight": "weight",
}

_shipment_id_name_convert = {}

_shipment_request_details_name_convert = {
    "AmazonOrderId": "amazon_order_id",
    "ItemList": "item_list",
    "LabelCustomization": "label_customization",
    "MustArriveByDate": "must_arrive_by_date",
    "PackageDimensions": "package_dimensions",
    "SellerOrderId": "seller_order_id",
    "ShipDate": "ship_date",
    "ShipFromAddress": "ship_from_address",
    "ShippingServiceOptions": "shipping_service_options",
    "Weight": "weight",
}

_shipment_status_name_convert = {}

_shipping_offering_filter_name_convert = {
    "CarrierWillPickUp": "carrier_will_pick_up",
    "DeliveryExperience": "delivery_experience",
    "IncludeComplexShippingOptions": "include_complex_shipping_options",
    "IncludePackingSlipWithLabel": "include_packing_slip_with_label",
}

_shipping_service_name_convert = {
    "AvailableFormatOptionsForLabel": "available_format_options_for_label",
    "AvailableLabelFormats": "available_label_formats",
    "AvailableShippingServiceOptions": "available_shipping_service_options",
    "CarrierName": "carrier_name",
    "EarliestEstimatedDeliveryDate": "earliest_estimated_delivery_date",
    "LatestEstimatedDeliveryDate": "latest_estimated_delivery_date",
    "Rate": "rate",
    "RequiresAdditionalSellerInputs": "requires_additional_seller_inputs",
    "ShipDate": "ship_date",
    "ShippingServiceId": "shipping_service_id",
    "ShippingServiceName": "shipping_service_name",
    "ShippingServiceOfferId": "shipping_service_offer_id",
    "ShippingServiceOptions": "shipping_service_options",
}

_shipping_service_identifier_name_convert = {}

_shipping_service_options_name_convert = {
    "CarrierWillPickUp": "carrier_will_pick_up",
    "CarrierWillPickUpOption": "carrier_will_pick_up_option",
    "DeclaredValue": "declared_value",
    "DeliveryExperience": "delivery_experience",
    "LabelFormat": "label_format",
}

_standard_id_for_label_name_convert = {}

_state_or_province_code_name_convert = {}

_temporarily_unavailable_carrier_name_convert = {
    "CarrierName": "carrier_name",
}

_terms_and_conditions_not_accepted_carrier_name_convert = {
    "CarrierName": "carrier_name",
}

_timestamp_name_convert = {}

_tracking_id_name_convert = {}

_transparency_code_name_convert = {}

_unit_of_length_name_convert = {}

_unit_of_weight_name_convert = {}

_weight_name_convert = {
    "Unit": "unit",
    "Value": "value",
}

_weight_value_name_convert = {}


class MerchantFulfillmentV0Client(BaseClient):
    def cancel_shipment(
        self,
        shipment_id: str,
    ) -> Union[CancelShipmentResponse]:
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
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._cancel_shipment_params,
            self._cancel_shipment_responses,
        )
        return response

    _cancel_shipment_params = (("shipmentId", "path"),)  # name, param in

    _cancel_shipment_responses = {
        200: CancelShipmentResponse,
        400: CancelShipmentResponse,
        401: CancelShipmentResponse,
        403: CancelShipmentResponse,
        404: CancelShipmentResponse,
        429: CancelShipmentResponse,
        500: CancelShipmentResponse,
        503: CancelShipmentResponse,
    }

    def cancel_shipment_old(
        self,
        shipment_id: str,
    ) -> Union[CancelShipmentResponse]:
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
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._cancel_shipment_old_params,
            self._cancel_shipment_old_responses,
        )
        return response

    _cancel_shipment_old_params = (("shipmentId", "path"),)  # name, param in

    _cancel_shipment_old_responses = {
        200: CancelShipmentResponse,
        400: CancelShipmentResponse,
        401: CancelShipmentResponse,
        403: CancelShipmentResponse,
        404: CancelShipmentResponse,
        429: CancelShipmentResponse,
        500: CancelShipmentResponse,
        503: CancelShipmentResponse,
    }

    def create_shipment(
        self,
        shipment_request_details: Dict[str, Any],
        shipping_service_id: str,
        hazmat_type: Union[Literal["None"], Literal["LQHazmat"]] = None,
        label_format_option: Dict[str, Any] = None,
        shipment_level_seller_inputs_list: List["AdditionalSellerInputs"] = None,
        shipping_service_offer_id: str = None,
    ) -> Union[CreateShipmentResponse]:
        """
        Create a shipment with the information provided.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            hazmat_type: Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
            label_format_option: Whether to include a packing slip.
            shipment_level_seller_inputs_list: A list of additional seller input pairs required to purchase shipping.
            shipment_request_details: Shipment information required for requesting shipping service offers or for creating a shipment.
            shipping_service_id: An Amazon-defined shipping service identifier.
            shipping_service_offer_id: Identifies a shipping service order made by a carrier.
        """
        url = "/mfn/v0/shipments"
        values = (
            hazmat_type,
            label_format_option,
            shipment_level_seller_inputs_list,
            shipment_request_details,
            shipping_service_id,
            shipping_service_offer_id,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_shipment_params,
            self._create_shipment_responses,
        )
        return response

    _create_shipment_params = (  # name, param in
        ("HazmatType", "body"),
        ("LabelFormatOption", "body"),
        ("ShipmentLevelSellerInputsList", "body"),
        ("ShipmentRequestDetails", "body"),
        ("ShippingServiceId", "body"),
        ("ShippingServiceOfferId", "body"),
    )

    _create_shipment_responses = {
        200: CreateShipmentResponse,
        400: CreateShipmentResponse,
        401: CreateShipmentResponse,
        403: CreateShipmentResponse,
        404: CreateShipmentResponse,
        429: CreateShipmentResponse,
        500: CreateShipmentResponse,
        503: CreateShipmentResponse,
    }

    def get_additional_seller_inputs(
        self,
        order_id: str,
        ship_from_address: Dict[str, Any],
        shipping_service_id: str,
    ) -> Union[GetAdditionalSellerInputsResponse]:
        """
        Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            ship_from_address: The postal address information.
            shipping_service_id: An Amazon-defined shipping service identifier.
        """
        url = "/mfn/v0/additionalSellerInputs"
        values = (
            order_id,
            ship_from_address,
            shipping_service_id,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_additional_seller_inputs_params,
            self._get_additional_seller_inputs_responses,
        )
        return response

    _get_additional_seller_inputs_params = (  # name, param in
        ("OrderId", "body"),
        ("ShipFromAddress", "body"),
        ("ShippingServiceId", "body"),
    )

    _get_additional_seller_inputs_responses = {
        200: GetAdditionalSellerInputsResponse,
        400: GetAdditionalSellerInputsResponse,
        401: GetAdditionalSellerInputsResponse,
        403: GetAdditionalSellerInputsResponse,
        404: GetAdditionalSellerInputsResponse,
        429: GetAdditionalSellerInputsResponse,
        500: GetAdditionalSellerInputsResponse,
        503: GetAdditionalSellerInputsResponse,
    }

    def get_additional_seller_inputs_old(
        self,
        order_id: str,
        ship_from_address: Dict[str, Any],
        shipping_service_id: str,
    ) -> Union[GetAdditionalSellerInputsResponse]:
        """
        Get a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: An Amazon-defined order identifier, in 3-7-7 format.
            ship_from_address: The postal address information.
            shipping_service_id: An Amazon-defined shipping service identifier.
        """
        url = "/mfn/v0/sellerInputs"
        values = (
            order_id,
            ship_from_address,
            shipping_service_id,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_additional_seller_inputs_old_params,
            self._get_additional_seller_inputs_old_responses,
        )
        return response

    _get_additional_seller_inputs_old_params = (  # name, param in
        ("OrderId", "body"),
        ("ShipFromAddress", "body"),
        ("ShippingServiceId", "body"),
    )

    _get_additional_seller_inputs_old_responses = {
        200: GetAdditionalSellerInputsResponse,
        400: GetAdditionalSellerInputsResponse,
        401: GetAdditionalSellerInputsResponse,
        403: GetAdditionalSellerInputsResponse,
        404: GetAdditionalSellerInputsResponse,
        429: GetAdditionalSellerInputsResponse,
        500: GetAdditionalSellerInputsResponse,
        503: GetAdditionalSellerInputsResponse,
    }

    def get_eligible_shipment_services(
        self,
        shipment_request_details: Dict[str, Any],
        shipping_offering_filter: Dict[str, Any] = None,
    ) -> Union[GetEligibleShipmentServicesResponse]:
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_eligible_shipment_services_params,
            self._get_eligible_shipment_services_responses,
        )
        return response

    _get_eligible_shipment_services_params = (  # name, param in
        ("ShipmentRequestDetails", "body"),
        ("ShippingOfferingFilter", "body"),
    )

    _get_eligible_shipment_services_responses = {
        200: GetEligibleShipmentServicesResponse,
        400: GetEligibleShipmentServicesResponse,
        401: GetEligibleShipmentServicesResponse,
        403: GetEligibleShipmentServicesResponse,
        404: GetEligibleShipmentServicesResponse,
        429: GetEligibleShipmentServicesResponse,
        500: GetEligibleShipmentServicesResponse,
        503: GetEligibleShipmentServicesResponse,
    }

    def get_eligible_shipment_services_old(
        self,
        shipment_request_details: Dict[str, Any],
        shipping_offering_filter: Dict[str, Any] = None,
    ) -> Union[GetEligibleShipmentServicesResponse]:
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_eligible_shipment_services_old_params,
            self._get_eligible_shipment_services_old_responses,
        )
        return response

    _get_eligible_shipment_services_old_params = (  # name, param in
        ("ShipmentRequestDetails", "body"),
        ("ShippingOfferingFilter", "body"),
    )

    _get_eligible_shipment_services_old_responses = {
        200: GetEligibleShipmentServicesResponse,
        400: GetEligibleShipmentServicesResponse,
        401: GetEligibleShipmentServicesResponse,
        403: GetEligibleShipmentServicesResponse,
        404: GetEligibleShipmentServicesResponse,
        429: GetEligibleShipmentServicesResponse,
        500: GetEligibleShipmentServicesResponse,
        503: GetEligibleShipmentServicesResponse,
    }

    def get_shipment(
        self,
        shipment_id: str,
    ) -> Union[GetShipmentResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipment_params,
            self._get_shipment_responses,
        )
        return response

    _get_shipment_params = (("shipmentId", "path"),)  # name, param in

    _get_shipment_responses = {
        200: GetShipmentResponse,
        400: GetShipmentResponse,
        401: GetShipmentResponse,
        403: GetShipmentResponse,
        404: GetShipmentResponse,
        429: GetShipmentResponse,
        500: GetShipmentResponse,
        503: GetShipmentResponse,
    }
