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
from datetime import date, datetime


@attrs.define
class AdditionalInputs:
    """
    Maps the additional seller input to the definition. The key to the map is the field name.
    """

    additional_input_field_name: str = attrs.field(
        kw_only=True,
    )
    """
    The field name.
    """

    seller_input_definition: "SellerInputDefinition" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AdditionalInputsList:
    """
    A list of additional inputs.
    """

    pass


@attrs.define
class AdditionalSellerInput:
    """
    Additional information required to purchase shipping.
    """

    data_type: str = attrs.field(
        kw_only=True,
    )
    """
    The data type of the additional information.
    """

    value_as_address: "Address" = attrs.field(
        kw_only=True,
    )

    value_as_boolean: bool = attrs.field(
        kw_only=True,
    )
    """
    The value when the data type is boolean.
    """

    value_as_currency: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )

    value_as_dimension: "Length" = attrs.field(
        kw_only=True,
    )

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

    value_as_timestamp: "Timestamp" = attrs.field(
        kw_only=True,
    )

    value_as_weight: "Weight" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AdditionalSellerInputs:
    """
    An additional set of seller inputs required to purchase shipping.
    """

    additional_input_field_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the additional input field.
    """

    additional_seller_input: "AdditionalSellerInput" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AdditionalSellerInputsList:
    """
    A list of additional seller input pairs required to purchase shipping.
    """

    pass


@attrs.define
class Address:
    """
    The postal address information.
    """

    address_line1: "AddressLine1" = attrs.field(
        kw_only=True,
    )

    address_line2: "AddressLine2" = attrs.field(
        kw_only=True,
    )

    address_line3: "AddressLine3" = attrs.field(
        kw_only=True,
    )

    city: "City" = attrs.field(
        kw_only=True,
    )

    country_code: "CountryCode" = attrs.field(
        kw_only=True,
    )

    district_or_county: "DistrictOrCounty" = attrs.field(
        kw_only=True,
    )

    email: "EmailAddress" = attrs.field(
        kw_only=True,
    )

    name: "AddressName" = attrs.field(
        kw_only=True,
    )

    phone: "PhoneNumber" = attrs.field(
        kw_only=True,
    )

    postal_code: "PostalCode" = attrs.field(
        kw_only=True,
    )

    state_or_province_code: "StateOrProvinceCode" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AddressLine1:
    """
    The street address information.
    """

    pass


@attrs.define
class AddressLine2:
    """
    Additional street address information.
    """

    pass


@attrs.define
class AddressLine3:
    """
    Additional street address information.
    """

    pass


@attrs.define
class AddressName:
    """
    The name of the addressee, or business name.
    """

    pass


@attrs.define
class AmazonOrderId:
    """
    An Amazon-defined order identifier, in 3-7-7 format.
    """

    pass


@attrs.define
class AvailableCarrierWillPickUpOption:
    """
    Indicates whether the carrier will pick up the package, and what fee is charged, if any.
    """

    carrier_will_pick_up_option: "CarrierWillPickUpOption" = attrs.field(
        kw_only=True,
    )

    charge: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AvailableCarrierWillPickUpOptionsList:
    """
    List of available carrier pickup options.
    """

    pass


@attrs.define
class AvailableDeliveryExperienceOption:
    """
    The available delivery confirmation options, and the fee charged, if any.
    """

    charge: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )

    delivery_experience_option: "DeliveryExperienceOption" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AvailableDeliveryExperienceOptionsList:
    """
    List of available delivery experience options.
    """

    pass


@attrs.define
class AvailableFormatOptionsForLabelList:
    """
    The available label formats.
    """

    pass


@attrs.define
class AvailableShippingServiceOptions:
    """
    The available shipping service options.
    """

    available_carrier_will_pick_up_options: "AvailableCarrierWillPickUpOptionsList" = attrs.field(
        kw_only=True,
    )

    available_delivery_experience_options: "AvailableDeliveryExperienceOptionsList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CancelShipmentResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CarrierWillPickUpOption:
    """
    Carrier will pick up option.
    """

    pass


@attrs.define
class City:
    """
    The city.
    """

    pass


@attrs.define
class Constraint:
    """
    A validation constraint.
    """

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


@attrs.define
class Constraints:
    """
    List of constraints.
    """

    pass


@attrs.define
class CountryCode:
    """
    The country code. A two-character country code, in ISO 3166-1 alpha-2 format.
    """

    pass


@attrs.define
class CreateShipmentRequest:
    """
    Request schema.
    """

    hazmat_type: "HazmatType" = attrs.field(
        kw_only=True,
    )

    label_format_option: "LabelFormatOptionRequest" = attrs.field(
        kw_only=True,
    )

    shipment_level_seller_inputs_list: "AdditionalSellerInputsList" = attrs.field(
        kw_only=True,
    )

    shipment_request_details: "ShipmentRequestDetails" = attrs.field(
        kw_only=True,
    )

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )

    shipping_service_offer_id: str = attrs.field(
        kw_only=True,
    )
    """
    Identifies a shipping service order made by a carrier.
    """


@attrs.define
class CreateShipmentResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CurrencyAmount:
    """
    Currency type and amount.
    """

    amount: float = attrs.field(
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


@attrs.define
class CustomTextForLabel:
    """
        Custom text to print on the label.

    Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support CustomTextForLabel.
    """

    pass


@attrs.define
class DeliveryExperienceOption:
    """
    The delivery confirmation level.
    """

    pass


@attrs.define
class DeliveryExperienceType:
    """
    The delivery confirmation level.
    """

    pass


@attrs.define
class DistrictOrCounty:
    """
    The district or county.
    """

    pass


@attrs.define
class EmailAddress:
    """
    The email address.
    """

    pass


@attrs.define
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

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


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class FileContents:
    """
    The document data and checksum.
    """

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


@attrs.define
class FileType:
    """
    The file type for a label.
    """

    pass


@attrs.define
class GetAdditionalSellerInputsRequest:
    """
    Request schema.
    """

    order_id: "AmazonOrderId" = attrs.field(
        kw_only=True,
    )

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetAdditionalSellerInputsResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "GetAdditionalSellerInputsResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetAdditionalSellerInputsResult:
    """
    The payload for the getAdditionalSellerInputs operation.
    """

    item_level_fields_list: "ItemLevelFieldsList" = attrs.field(
        kw_only=True,
    )

    shipment_level_fields: "AdditionalInputsList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetEligibleShipmentServicesRequest:
    """
    Request schema.
    """

    shipment_request_details: "ShipmentRequestDetails" = attrs.field(
        kw_only=True,
    )

    shipping_offering_filter: "ShippingOfferingFilter" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetEligibleShipmentServicesResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "GetEligibleShipmentServicesResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetEligibleShipmentServicesResult:
    """
    The payload for the getEligibleShipmentServices operation.
    """

    rejected_shipping_service_list: "RejectedShippingServiceList" = attrs.field(
        kw_only=True,
    )

    shipping_service_list: "ShippingServiceList" = attrs.field(
        kw_only=True,
    )

    temporarily_unavailable_carrier_list: "TemporarilyUnavailableCarrierList" = attrs.field(
        kw_only=True,
    )

    terms_and_conditions_not_accepted_carrier_list: "TermsAndConditionsNotAcceptedCarrierList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetShipmentResponse:
    """
    Response schema.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )


@attrs.define
class HazmatType:
    """
    Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials.
    """

    pass


@attrs.define
class InputTargetType:
    """
    Indicates whether the additional seller input is at the item or shipment level.
    """

    pass


@attrs.define
class Item:
    """
    An Amazon order item identifier and a quantity.
    """

    item_description: "ItemDescription" = attrs.field(
        kw_only=True,
    )

    item_level_seller_inputs_list: "AdditionalSellerInputsList" = attrs.field(
        kw_only=True,
    )

    item_weight: "Weight" = attrs.field(
        kw_only=True,
    )

    order_item_id: "OrderItemId" = attrs.field(
        kw_only=True,
    )

    quantity: "ItemQuantity" = attrs.field(
        kw_only=True,
    )

    transparency_code_list: "TransparencyCodeList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ItemDescription:
    """
    The description of the item.
    """

    pass


@attrs.define
class ItemLevelFields:

    additional_inputs: "AdditionalInputsList" = attrs.field(
        kw_only=True,
    )

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """


@attrs.define
class ItemLevelFieldsList:
    """
    A list of item level fields.
    """

    pass


@attrs.define
class ItemList:
    """
    The list of items to be included in a shipment.
    """

    pass


@attrs.define
class ItemQuantity:
    """
    The number of items.
    """

    pass


@attrs.define
class Label:
    """
    Data for creating a shipping label and dimensions for printing the label.
    """

    custom_text_for_label: "CustomTextForLabel" = attrs.field(
        kw_only=True,
    )

    dimensions: "LabelDimensions" = attrs.field(
        kw_only=True,
    )

    file_contents: "FileContents" = attrs.field(
        kw_only=True,
    )

    label_format: "LabelFormat" = attrs.field(
        kw_only=True,
    )

    standard_id_for_label: "StandardIdForLabel" = attrs.field(
        kw_only=True,
    )


@attrs.define
class LabelCustomization:
    """
    Custom text for shipping labels.
    """

    custom_text_for_label: "CustomTextForLabel" = attrs.field(
        kw_only=True,
    )

    standard_id_for_label: "StandardIdForLabel" = attrs.field(
        kw_only=True,
    )


@attrs.define
class LabelDimension:
    """
    A label dimension.
    """

    pass


@attrs.define
class LabelDimensions:
    """
    Dimensions for printing a shipping label.
    """

    length: "LabelDimension" = attrs.field(
        kw_only=True,
    )

    unit: "UnitOfLength" = attrs.field(
        kw_only=True,
    )

    width: "LabelDimension" = attrs.field(
        kw_only=True,
    )


@attrs.define
class LabelFormat:
    """
    The label format.
    """

    pass


@attrs.define
class LabelFormatList:
    """
    List of label formats.
    """

    pass


@attrs.define
class LabelFormatOption:
    """
    The label format details and whether to include a packing slip.
    """

    include_packing_slip_with_label: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, include a packing slip with the label.
    """

    label_format: "LabelFormat" = attrs.field(
        kw_only=True,
    )


@attrs.define
class LabelFormatOptionRequest:
    """
    Whether to include a packing slip.
    """

    include_packing_slip_with_label: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, include a packing slip with the label.
    """


@attrs.define
class Length:
    """
    The length.
    """

    unit: "UnitOfLength" = attrs.field(
        kw_only=True,
    )

    value: float = attrs.field(
        kw_only=True,
    )
    """
    The value in units.
    """


@attrs.define
class OrderItemId:
    """
    An Amazon-defined identifier for an individual item in an order.
    """

    pass


@attrs.define
class PackageDimension:

    pass


@attrs.define
class PackageDimensions:
    """
    The dimensions of a package contained in a shipment.
    """

    height: "PackageDimension" = attrs.field(
        kw_only=True,
    )

    length: "PackageDimension" = attrs.field(
        kw_only=True,
    )

    predefined_package_dimensions: "PredefinedPackageDimensions" = attrs.field(
        kw_only=True,
    )

    unit: "UnitOfLength" = attrs.field(
        kw_only=True,
    )

    width: "PackageDimension" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PhoneNumber:
    """
    The phone number.
    """

    pass


@attrs.define
class PostalCode:
    """
    The zip code or postal code.
    """

    pass


@attrs.define
class PredefinedPackageDimensions:
    """
        An enumeration of predefined parcel tokens. If you specify a PredefinedPackageDimensions token, you are not obligated to use a branded package from a carrier. For example, if you specify the FedEx_Box_10kg token, you do not have to use that particular package from FedEx. You are only obligated to use a box that matches the dimensions specified by the token.

    Note: Please note that carriers can have restrictions on the type of package allowed for certain ship methods. Check the carrier website for all details. Example: Flat rate pricing is available when materials are sent by USPS in a USPS-produced Flat Rate Envelope or Box.
    """

    pass


@attrs.define
class RejectedShippingService:
    """
    Information about a rejected shipping service
    """

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

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )

    shipping_service_name: str = attrs.field(
        kw_only=True,
    )
    """
    The rejected shipping service localized name. e.g. FedEx Standard Overnight
    """


@attrs.define
class RejectedShippingServiceList:
    """
    List of services that were for some reason unavailable for this request
    """

    pass


@attrs.define
class RestrictedSetValues:
    """
    The set of fixed values in an additional seller input.
    """

    pass


@attrs.define
class SellerInputDefinition:
    """
    Specifies characteristics that apply to a seller input.
    """

    constraints: "Constraints" = attrs.field(
        kw_only=True,
    )

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

    input_target: "InputTargetType" = attrs.field(
        kw_only=True,
    )

    is_required: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the additional input field is required.
    """

    restricted_set_values: "RestrictedSetValues" = attrs.field(
        kw_only=True,
    )

    stored_value: "AdditionalSellerInput" = attrs.field(
        kw_only=True,
    )


@attrs.define
class SellerOrderId:
    """
    A seller-defined order identifier.
    """

    pass


@attrs.define
class Shipment:
    """
    The details of a shipment, including the shipment status.
    """

    amazon_order_id: "AmazonOrderId" = attrs.field(
        kw_only=True,
    )

    created_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    insurance: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )

    item_list: "ItemList" = attrs.field(
        kw_only=True,
    )

    label: "Label" = attrs.field(
        kw_only=True,
    )

    last_updated_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    package_dimensions: "PackageDimensions" = attrs.field(
        kw_only=True,
    )

    seller_order_id: "SellerOrderId" = attrs.field(
        kw_only=True,
    )

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )

    ship_to_address: "Address" = attrs.field(
        kw_only=True,
    )

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )

    shipping_service: "ShippingService" = attrs.field(
        kw_only=True,
    )

    status: "ShipmentStatus" = attrs.field(
        kw_only=True,
    )

    tracking_id: "TrackingId" = attrs.field(
        kw_only=True,
    )

    weight: "Weight" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ShipmentId:
    """
    An Amazon-defined shipment identifier.
    """

    pass


@attrs.define
class ShipmentRequestDetails:
    """
    Shipment information required for requesting shipping service offers or for creating a shipment.
    """

    amazon_order_id: "AmazonOrderId" = attrs.field(
        kw_only=True,
    )

    item_list: "ItemList" = attrs.field(
        kw_only=True,
    )

    label_customization: "LabelCustomization" = attrs.field(
        kw_only=True,
    )

    must_arrive_by_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    package_dimensions: "PackageDimensions" = attrs.field(
        kw_only=True,
    )

    seller_order_id: "SellerOrderId" = attrs.field(
        kw_only=True,
    )

    ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    ship_from_address: "Address" = attrs.field(
        kw_only=True,
    )

    shipping_service_options: "ShippingServiceOptions" = attrs.field(
        kw_only=True,
    )

    weight: "Weight" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ShipmentStatus:
    """
    The shipment status.
    """

    pass


@attrs.define
class ShippingOfferingFilter:
    """
    Filter for use when requesting eligible shipping services.
    """

    carrier_will_pick_up: "CarrierWillPickUpOption" = attrs.field(
        kw_only=True,
    )

    delivery_experience: "DeliveryExperienceOption" = attrs.field(
        kw_only=True,
    )

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


@attrs.define
class ShippingService:
    """
    A shipping service offer made by a carrier.
    """

    available_format_options_for_label: "AvailableFormatOptionsForLabelList" = attrs.field(
        kw_only=True,
    )

    available_label_formats: "LabelFormatList" = attrs.field(
        kw_only=True,
    )

    available_shipping_service_options: "AvailableShippingServiceOptions" = attrs.field(
        kw_only=True,
    )

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """

    earliest_estimated_delivery_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    latest_estimated_delivery_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    rate: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )

    requires_additional_seller_inputs: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, additional seller inputs are required.
    """

    ship_date: "Timestamp" = attrs.field(
        kw_only=True,
    )

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field(
        kw_only=True,
    )

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

    shipping_service_options: "ShippingServiceOptions" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ShippingServiceIdentifier:
    """
    An Amazon-defined shipping service identifier.
    """

    pass


@attrs.define
class ShippingServiceList:
    """
    A list of shipping services offers.
    """

    pass


@attrs.define
class ShippingServiceOptions:
    """
    Extra services provided by a carrier.
    """

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

    declared_value: "CurrencyAmount" = attrs.field(
        kw_only=True,
    )

    delivery_experience: "DeliveryExperienceType" = attrs.field(
        kw_only=True,
    )

    label_format: "LabelFormat" = attrs.field(
        kw_only=True,
    )


@attrs.define
class StandardIdForLabel:
    """
    The type of standard identifier to print on the label.
    """

    pass


@attrs.define
class StateOrProvinceCode:
    """
    The state or province code. **Note.** Required in the Canada, US, and UK marketplaces. Also required for shipments originating from China.
    """

    pass


@attrs.define
class TemporarilyUnavailableCarrier:
    """
    A carrier who is temporarily unavailable, most likely due to a service outage experienced by the carrier.
    """

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """


@attrs.define
class TemporarilyUnavailableCarrierList:
    """
    A list of temporarily unavailable carriers.
    """

    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrier:
    """
    A carrier whose terms and conditions have not been accepted by the seller.
    """

    carrier_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the carrier.
    """


@attrs.define
class TermsAndConditionsNotAcceptedCarrierList:
    """
    List of carriers whose terms and conditions were not accepted by the seller.
    """

    pass


@attrs.define
class Timestamp:

    pass


@attrs.define
class TrackingId:
    """
    The shipment tracking identifier provided by the carrier.
    """

    pass


@attrs.define
class TransparencyCode:
    """
    The Transparency code associated with the item.
    """

    pass


@attrs.define
class TransparencyCodeList:
    """
    A list of transparency codes.
    """

    pass


@attrs.define
class UnitOfLength:
    """
    The unit of length.
    """

    pass


@attrs.define
class UnitOfWeight:
    """
    The unit of weight.
    """

    pass


@attrs.define
class Weight:
    """
    The weight.
    """

    unit: "UnitOfWeight" = attrs.field(
        kw_only=True,
    )

    value: "WeightValue" = attrs.field(
        kw_only=True,
    )


@attrs.define
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
