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

    additional_input_field_name: Optional[str] = attrs.field()
    """
    The field name.
    """

    seller_input_definition: Optional["SellerInputDefinition"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalInputsList:
    """
    A list of additional inputs.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalSellerInput:
    """
    Additional information required to purchase shipping.
    """

    data_type: Optional[str] = attrs.field()
    """
    The data type of the additional information.
    """

    value_as_address: Optional["Address"] = attrs.field()

    value_as_boolean: Optional[bool] = attrs.field()
    """
    The value when the data type is boolean.
    """

    value_as_currency: Optional["CurrencyAmount"] = attrs.field()

    value_as_dimension: Optional["Length"] = attrs.field()

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


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalSellerInputs:
    """
    An additional set of seller inputs required to purchase shipping.
    """

    additional_input_field_name: Optional[str] = attrs.field()
    """
    The name of the additional input field.
    """

    additional_seller_input: Optional["AdditionalSellerInput"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AdditionalSellerInputsList:
    """
    A list of additional seller input pairs required to purchase shipping.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    The postal address information.
    """

    address_line1: Optional["AddressLine1"] = attrs.field()

    address_line2: Optional["AddressLine2"] = attrs.field()

    address_line3: Optional["AddressLine3"] = attrs.field()

    city: Optional["City"] = attrs.field()

    country_code: Optional["CountryCode"] = attrs.field()

    district_or_county: Optional["DistrictOrCounty"] = attrs.field()

    email: Optional["EmailAddress"] = attrs.field()

    name: Optional["AddressName"] = attrs.field()

    phone: Optional["PhoneNumber"] = attrs.field()

    postal_code: Optional["PostalCode"] = attrs.field()

    state_or_province_code: Optional["StateOrProvinceCode"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressLine1:
    """
    The street address information.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressLine2:
    """
    Additional street address information.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressLine3:
    """
    Additional street address information.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressName:
    """
    The name of the addressee, or business name.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AmazonOrderId:
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableCarrierWillPickUpOption:
    """
    Indicates whether the carrier will pick up the package, and what fee is charged, if any.
    """

    carrier_will_pick_up_option: Optional["CarrierWillPickUpOption"] = attrs.field()

    charge: Optional["CurrencyAmount"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableCarrierWillPickUpOptionsList:
    """
    List of available carrier pickup options.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableDeliveryExperienceOption:
    """
    The available delivery confirmation options, and the fee charged, if any.
    """

    charge: Optional["CurrencyAmount"] = attrs.field()

    delivery_experience_option: Optional["DeliveryExperienceOption"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableDeliveryExperienceOptionsList:
    """
    List of available delivery experience options.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableFormatOptionsForLabelList:
    """
    The available label formats.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class AvailableShippingServiceOptions:
    """
    The available shipping service options.
    """

    available_carrier_will_pick_up_options: Optional["AvailableCarrierWillPickUpOptionsList"] = attrs.field()

    available_delivery_experience_options: Optional["AvailableDeliveryExperienceOptionsList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelShipmentResponse:
    """
    Response schema.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["Shipment"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CarrierWillPickUpOption:
    """
    Carrier will pick up option.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class City:
    """
    The city.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Constraint:
    """
    A validation constraint.
    """

    validation_reg_ex: Optional[str] = attrs.field()
    """
    A regular expression.
    """

    validation_string: Optional[str] = attrs.field()
    """
    A validation string.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Constraints:
    """
    List of constraints.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CountryCode:
    """
    The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentRequest:
    """
    Request schema.
    """

    hazmat_type: Optional["HazmatType"] = attrs.field()

    label_format_option: Optional["LabelFormatOptionRequest"] = attrs.field()

    shipment_level_seller_inputs_list: Optional["AdditionalSellerInputsList"] = attrs.field()

    shipment_request_details: Optional["ShipmentRequestDetails"] = attrs.field()

    shipping_service_id: Optional["ShippingServiceIdentifier"] = attrs.field()

    shipping_service_offer_id: Optional[str] = attrs.field()
    """
    Identifies a shipping service order made by a carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentResponse:
    """
    Response schema.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["Shipment"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CurrencyAmount:
    """
    Currency type and amount.
    """

    amount: Optional[float] = attrs.field()
    """
    The currency amount.

    Extra fields:
    {'schema_format': 'double'}
    """

    currency_code: Optional[str] = attrs.field()
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

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeliveryExperienceOption:
    """
    The delivery confirmation level.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DeliveryExperienceType:
    """
    The delivery confirmation level.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DistrictOrCounty:
    """
    The district or county.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class EmailAddress:
    """
    The email address.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FileContents:
    """
    The document data and checksum.
    """

    checksum: Optional[str] = attrs.field()
    """
    An MD5 hash to validate the PDF document data, in the form of a Base64-encoded string.
    """

    contents: Optional[str] = attrs.field()
    """
    Data for printing labels, in the form of a Base64-encoded, GZip-compressed string.
    """

    file_type: Optional["FileType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class FileType:
    """
    The file type for a label.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAdditionalSellerInputsRequest:
    """
    Request schema.
    """

    order_id: Optional["AmazonOrderId"] = attrs.field()

    ship_from_address: Optional["Address"] = attrs.field()

    shipping_service_id: Optional["ShippingServiceIdentifier"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAdditionalSellerInputsResponse:
    """
    Response schema.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["GetAdditionalSellerInputsResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAdditionalSellerInputsResult:
    """
    The payload for the getAdditionalSellerInputs operation.
    """

    item_level_fields_list: Optional["ItemLevelFieldsList"] = attrs.field()

    shipment_level_fields: Optional["AdditionalInputsList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetEligibleShipmentServicesRequest:
    """
    Request schema.
    """

    shipment_request_details: Optional["ShipmentRequestDetails"] = attrs.field()

    shipping_offering_filter: Optional["ShippingOfferingFilter"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetEligibleShipmentServicesResponse:
    """
    Response schema.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["GetEligibleShipmentServicesResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetEligibleShipmentServicesResult:
    """
    The payload for the getEligibleShipmentServices operation.
    """

    rejected_shipping_service_list: Optional["RejectedShippingServiceList"] = attrs.field()

    shipping_service_list: Optional["ShippingServiceList"] = attrs.field()

    temporarily_unavailable_carrier_list: Optional["TemporarilyUnavailableCarrierList"] = attrs.field()

    terms_and_conditions_not_accepted_carrier_list: Optional["TermsAndConditionsNotAcceptedCarrierList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentResponse:
    """
    Response schema.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["Shipment"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class HazmatType:
    """
    Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class InputTargetType:
    """
    Indicates whether the additional seller input is at the item or shipment level.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    An Amazon order item identifier and a quantity.
    """

    item_description: Optional["ItemDescription"] = attrs.field()

    item_level_seller_inputs_list: Optional["AdditionalSellerInputsList"] = attrs.field()

    item_weight: Optional["Weight"] = attrs.field()

    order_item_id: Optional["OrderItemId"] = attrs.field()

    quantity: Optional["ItemQuantity"] = attrs.field()

    transparency_code_list: Optional["TransparencyCodeList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemDescription:
    """
    The description of the item.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemLevelFields:

    additional_inputs: Optional["AdditionalInputsList"] = attrs.field()

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemLevelFieldsList:
    """
    A list of item level fields.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemList:
    """
    The list of items to be included in a shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    The number of items.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Label:
    """
    Data for creating a shipping label and dimensions for printing the label.
    """

    custom_text_for_label: Optional["CustomTextForLabel"] = attrs.field()

    dimensions: Optional["LabelDimensions"] = attrs.field()

    file_contents: Optional["FileContents"] = attrs.field()

    label_format: Optional["LabelFormat"] = attrs.field()

    standard_id_for_label: Optional["StandardIdForLabel"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelCustomization:
    """
    Custom text for shipping labels.
    """

    custom_text_for_label: Optional["CustomTextForLabel"] = attrs.field()

    standard_id_for_label: Optional["StandardIdForLabel"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelDimension:
    """
    A label dimension.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelDimensions:
    """
    Dimensions for printing a shipping label.
    """

    length: Optional["LabelDimension"] = attrs.field()

    unit: Optional["UnitOfLength"] = attrs.field()

    width: Optional["LabelDimension"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormat:
    """
    The label format.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormatList:
    """
    List of label formats.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormatOption:
    """
    The label format details and whether to include a packing slip.
    """

    include_packing_slip_with_label: Optional[bool] = attrs.field()
    """
    When true, include a packing slip with the label.
    """

    label_format: Optional["LabelFormat"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelFormatOptionRequest:
    """
    Whether to include a packing slip.
    """

    include_packing_slip_with_label: Optional[bool] = attrs.field()
    """
    When true, include a packing slip with the label.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Length:
    """
    The length.
    """

    unit: Optional["UnitOfLength"] = attrs.field()

    value: Optional[float] = attrs.field()
    """
    The value in units.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderItemId:
    """
    An Amazon-defined identifier for an individual item in an order.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackageDimension:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackageDimensions:
    """
    The dimensions of a package contained in a shipment.
    """

    height: Optional["PackageDimension"] = attrs.field()

    length: Optional["PackageDimension"] = attrs.field()

    predefined_package_dimensions: Optional["PredefinedPackageDimensions"] = attrs.field()

    unit: Optional["UnitOfLength"] = attrs.field()

    width: Optional["PackageDimension"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PhoneNumber:
    """
    The phone number.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostalCode:
    """
    The zip code or postal code.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PredefinedPackageDimensions:
    """
        An enumeration of predefined parcel tokens. If you specify a PredefinedPackageDimensions token, you are not obligated to use a branded package from a carrier. For example, if you specify the FedEx_Box_10kg token, you do not have to use that particular package from FedEx. You are only obligated to use a box that matches the dimensions specified by the token.

    Note: Please note that carriers can have restrictions on the type of package allowed for certain ship methods. Check the carrier website for all details. Example: Flat rate pricing is available when materials are sent by USPS in a USPS-produced Flat Rate Envelope or Box.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RejectedShippingService:
    """
    Information about a rejected shipping service
    """

    carrier_name: Optional[str] = attrs.field()
    """
    The rejected shipping carrier name. e.g. USPS
    """

    rejection_reason_code: Optional[str] = attrs.field()
    """
    A reason code meant to be consumed programatically. e.g. CARRIER_CANNOT_SHIP_TO_POBOX
    """

    rejection_reason_message: Optional[str] = attrs.field()
    """
    A localized human readable description of the rejected reason.
    """

    shipping_service_id: Optional["ShippingServiceIdentifier"] = attrs.field()

    shipping_service_name: Optional[str] = attrs.field()
    """
    The rejected shipping service localized name. e.g. FedEx Standard Overnight
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RejectedShippingServiceList:
    """
    List of services that were for some reason unavailable for this request
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RestrictedSetValues:
    """
    The set of fixed values in an additional seller input.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerInputDefinition:
    """
    Specifies characteristics that apply to a seller input.
    """

    constraints: Optional["Constraints"] = attrs.field()

    data_type: Optional[str] = attrs.field()
    """
    The data type of the additional input field.
    """

    input_display_text: Optional[str] = attrs.field()
    """
    The display text for the additional input field.
    """

    input_target: Optional["InputTargetType"] = attrs.field()

    is_required: Optional[bool] = attrs.field()
    """
    When true, the additional input field is required.
    """

    restricted_set_values: Optional["RestrictedSetValues"] = attrs.field()

    stored_value: Optional["AdditionalSellerInput"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerOrderId:
    """
    A seller-defined order identifier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Shipment:
    """
    The details of a shipment, including the shipment status.
    """

    amazon_order_id: Optional["AmazonOrderId"] = attrs.field()

    created_date: Optional["Timestamp"] = attrs.field()

    insurance: Optional["CurrencyAmount"] = attrs.field()

    item_list: Optional["ItemList"] = attrs.field()

    label: Optional["Label"] = attrs.field()

    last_updated_date: Optional["Timestamp"] = attrs.field()

    package_dimensions: Optional["PackageDimensions"] = attrs.field()

    seller_order_id: Optional["SellerOrderId"] = attrs.field()

    ship_from_address: Optional["Address"] = attrs.field()

    ship_to_address: Optional["Address"] = attrs.field()

    shipment_id: Optional["ShipmentId"] = attrs.field()

    shipping_service: Optional["ShippingService"] = attrs.field()

    status: Optional["ShipmentStatus"] = attrs.field()

    tracking_id: Optional["TrackingId"] = attrs.field()

    weight: Optional["Weight"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentId:
    """
    An Amazon-defined shipment identifier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentRequestDetails:
    """
    Shipment information required for requesting shipping service offers or for creating a shipment.
    """

    amazon_order_id: Optional["AmazonOrderId"] = attrs.field()

    item_list: Optional["ItemList"] = attrs.field()

    label_customization: Optional["LabelCustomization"] = attrs.field()

    must_arrive_by_date: Optional["Timestamp"] = attrs.field()

    package_dimensions: Optional["PackageDimensions"] = attrs.field()

    seller_order_id: Optional["SellerOrderId"] = attrs.field()

    ship_date: Optional["Timestamp"] = attrs.field()

    ship_from_address: Optional["Address"] = attrs.field()

    shipping_service_options: Optional["ShippingServiceOptions"] = attrs.field()

    weight: Optional["Weight"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentStatus:
    """
    The shipment status.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingOfferingFilter:
    """
    Filter for use when requesting eligible shipping services.
    """

    carrier_will_pick_up: Optional["CarrierWillPickUpOption"] = attrs.field()

    delivery_experience: Optional["DeliveryExperienceOption"] = attrs.field()

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

    available_format_options_for_label: Optional["AvailableFormatOptionsForLabelList"] = attrs.field()

    available_label_formats: Optional["LabelFormatList"] = attrs.field()

    available_shipping_service_options: Optional["AvailableShippingServiceOptions"] = attrs.field()

    carrier_name: Optional[str] = attrs.field()
    """
    The name of the carrier.
    """

    earliest_estimated_delivery_date: Optional["Timestamp"] = attrs.field()

    latest_estimated_delivery_date: Optional["Timestamp"] = attrs.field()

    rate: Optional["CurrencyAmount"] = attrs.field()

    requires_additional_seller_inputs: Optional[bool] = attrs.field()
    """
    When true, additional seller inputs are required.
    """

    ship_date: Optional["Timestamp"] = attrs.field()

    shipping_service_id: Optional["ShippingServiceIdentifier"] = attrs.field()

    shipping_service_name: Optional[str] = attrs.field()
    """
    A plain text representation of a carrier's shipping service. For example, "UPS Ground" or "FedEx Standard Overnight".
    """

    shipping_service_offer_id: Optional[str] = attrs.field()
    """
    An Amazon-defined shipping service offer identifier.
    """

    shipping_service_options: Optional["ShippingServiceOptions"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingServiceIdentifier:
    """
    An Amazon-defined shipping service identifier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingServiceList:
    """
    A list of shipping services offers.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingServiceOptions:
    """
    Extra services provided by a carrier.
    """

    carrier_will_pick_up: Optional[bool] = attrs.field()
    """
    When true, the carrier will pick up the package.
        Note: Scheduled carrier pickup is available only using Dynamex (US), DPD (UK), and Royal Mail (UK).
    """

    carrier_will_pick_up_option: Optional["CarrierWillPickUpOption"] = attrs.field()

    declared_value: Optional["CurrencyAmount"] = attrs.field()

    delivery_experience: Optional["DeliveryExperienceType"] = attrs.field()

    label_format: Optional["LabelFormat"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class StandardIdForLabel:
    """
    The type of standard identifier to print on the label.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class StateOrProvinceCode:
    """
    The state or province code. **Note.** Required in the Canada, US, and UK marketplaces. Also required for shipments originating from China.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TemporarilyUnavailableCarrier:
    """
    A carrier who is temporarily unavailable, most likely due to a service outage experienced by the carrier.
    """

    carrier_name: Optional[str] = attrs.field()
    """
    The name of the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TemporarilyUnavailableCarrierList:
    """
    A list of temporarily unavailable carriers.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TermsAndConditionsNotAcceptedCarrier:
    """
    A carrier whose terms and conditions have not been accepted by the seller.
    """

    carrier_name: Optional[str] = attrs.field()
    """
    The name of the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TermsAndConditionsNotAcceptedCarrierList:
    """
    List of carriers whose terms and conditions were not accepted by the seller.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Timestamp:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingId:
    """
    The shipment tracking identifier provided by the carrier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransparencyCode:
    """
    The Transparency code associated with the item.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransparencyCodeList:
    """
    A list of transparency codes.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnitOfLength:
    """
    The unit of length.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnitOfWeight:
    """
    The unit of weight.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight.
    """

    unit: Optional["UnitOfWeight"] = attrs.field()

    value: Optional["WeightValue"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class WeightValue:
    """
    The weight value.
    """

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
        shipment_request_details: Dict[str, Any],
        shipping_service_id: str,
        hazmat_type: Union[Literal["None"], Literal["LQHazmat"]] = None,
        label_format_option: Dict[str, Any] = None,
        shipment_level_seller_inputs_list: List["AdditionalSellerInputs"] = None,
        shipping_service_offer_id: str = None,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._create_shipment_params)
        return response

    _create_shipment_params = (  # name, param in
        ("HazmatType", "body"),
        ("LabelFormatOption", "body"),
        ("ShipmentLevelSellerInputsList", "body"),
        ("ShipmentRequestDetails", "body"),
        ("ShippingServiceId", "body"),
        ("ShippingServiceOfferId", "body"),
    )

    def get_additional_seller_inputs(
        self,
        order_id: str,
        ship_from_address: Dict[str, Any],
        shipping_service_id: str,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._get_additional_seller_inputs_params)
        return response

    _get_additional_seller_inputs_params = (  # name, param in
        ("OrderId", "body"),
        ("ShipFromAddress", "body"),
        ("ShippingServiceId", "body"),
    )

    def get_additional_seller_inputs_old(
        self,
        order_id: str,
        ship_from_address: Dict[str, Any],
        shipping_service_id: str,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._get_additional_seller_inputs_old_params)
        return response

    _get_additional_seller_inputs_old_params = (  # name, param in
        ("OrderId", "body"),
        ("ShipFromAddress", "body"),
        ("ShippingServiceId", "body"),
    )

    def get_eligible_shipment_services(
        self,
        shipment_request_details: Dict[str, Any],
        shipping_offering_filter: Dict[str, Any] = None,
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
        shipment_request_details: Dict[str, Any],
        shipping_offering_filter: Dict[str, Any] = None,
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
