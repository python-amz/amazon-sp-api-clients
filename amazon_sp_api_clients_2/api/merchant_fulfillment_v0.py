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

    seller_input_definition: "SellerInputDefinition"
    pass


@attrs.define
class AdditionalInputsList:

    pass


@attrs.define
class AdditionalSellerInput:

    data_type: str
    value_as_boolean: bool
    value_as_integer: int
    value_as_string: str

    value_as_address: "Address"
    value_as_currency: "CurrencyAmount"
    value_as_dimension: "Length"
    value_as_timestamp: "Timestamp"
    value_as_weight: "Weight"
    pass


@attrs.define
class AdditionalSellerInputs:

    additional_input_field_name: str

    additional_seller_input: "AdditionalSellerInput"
    pass


@attrs.define
class AdditionalSellerInputsList:

    pass


@attrs.define
class Address:

    address_line1: "AddressLine1"
    address_line2: "AddressLine2"
    address_line3: "AddressLine3"
    city: "City"
    country_code: "CountryCode"
    district_or_county: "DistrictOrCounty"
    email: "EmailAddress"
    name: "AddressName"
    phone: "PhoneNumber"
    postal_code: "PostalCode"
    state_or_province_code: "StateOrProvinceCode"
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

    carrier_will_pick_up_option: "CarrierWillPickUpOption"
    charge: "CurrencyAmount"
    pass


@attrs.define
class AvailableCarrierWillPickUpOptionsList:

    pass


@attrs.define
class AvailableDeliveryExperienceOption:

    charge: "CurrencyAmount"
    delivery_experience_option: "DeliveryExperienceOption"
    pass


@attrs.define
class AvailableDeliveryExperienceOptionsList:

    pass


@attrs.define
class AvailableFormatOptionsForLabelList:

    pass


@attrs.define
class AvailableShippingServiceOptions:

    available_carrier_will_pick_up_options: "AvailableCarrierWillPickUpOptionsList"
    available_delivery_experience_options: "AvailableDeliveryExperienceOptionsList"
    pass


@attrs.define
class CancelShipmentResponse:

    errors: "ErrorList"
    payload: "Shipment"
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
    validation_string: str

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

    hazmat_type: "HazmatType"
    label_format_option: "LabelFormatOptionRequest"
    shipment_level_seller_inputs_list: "AdditionalSellerInputsList"
    shipment_request_details: "ShipmentRequestDetails"
    shipping_service_id: "ShippingServiceIdentifier"
    pass


@attrs.define
class CreateShipmentResponse:

    errors: "ErrorList"
    payload: "Shipment"
    pass


@attrs.define
class CurrencyAmount:

    amount: Union[float, int]
    # {'schema_format': 'double'}
    currency_code: str
    # {'maxLength': 3}

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
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FileContents:

    checksum: str
    contents: str

    file_type: "FileType"
    pass


@attrs.define
class FileType:

    pass


@attrs.define
class GetAdditionalSellerInputsRequest:

    order_id: "AmazonOrderId"
    ship_from_address: "Address"
    shipping_service_id: "ShippingServiceIdentifier"
    pass


@attrs.define
class GetAdditionalSellerInputsResponse:

    errors: "ErrorList"
    payload: "GetAdditionalSellerInputsResult"
    pass


@attrs.define
class GetAdditionalSellerInputsResult:

    item_level_fields_list: "ItemLevelFieldsList"
    shipment_level_fields: "AdditionalInputsList"
    pass


@attrs.define
class GetEligibleShipmentServicesRequest:

    shipment_request_details: "ShipmentRequestDetails"
    shipping_offering_filter: "ShippingOfferingFilter"
    pass


@attrs.define
class GetEligibleShipmentServicesResponse:

    errors: "ErrorList"
    payload: "GetEligibleShipmentServicesResult"
    pass


@attrs.define
class GetEligibleShipmentServicesResult:

    rejected_shipping_service_list: "RejectedShippingServiceList"
    shipping_service_list: "ShippingServiceList"
    temporarily_unavailable_carrier_list: "TemporarilyUnavailableCarrierList"
    terms_and_conditions_not_accepted_carrier_list: "TermsAndConditionsNotAcceptedCarrierList"
    pass


@attrs.define
class GetShipmentResponse:

    errors: "ErrorList"
    payload: "Shipment"
    pass


@attrs.define
class HazmatType:

    pass


@attrs.define
class InputTargetType:

    pass


@attrs.define
class Item:

    item_description: "ItemDescription"
    item_level_seller_inputs_list: "AdditionalSellerInputsList"
    item_weight: "Weight"
    order_item_id: "OrderItemId"
    quantity: "ItemQuantity"
    transparency_code_list: "TransparencyCodeList"
    pass


@attrs.define
class ItemDescription:

    pass


@attrs.define
class ItemLevelFields:

    asin: str

    additional_inputs: "AdditionalInputsList"
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

    custom_text_for_label: "CustomTextForLabel"
    dimensions: "LabelDimensions"
    file_contents: "FileContents"
    label_format: "LabelFormat"
    standard_id_for_label: "StandardIdForLabel"
    pass


@attrs.define
class LabelCustomization:

    custom_text_for_label: "CustomTextForLabel"
    standard_id_for_label: "StandardIdForLabel"
    pass


@attrs.define
class LabelDimension:

    pass


@attrs.define
class LabelDimensions:

    length: "LabelDimension"
    unit: "UnitOfLength"
    width: "LabelDimension"
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

    label_format: "LabelFormat"
    pass


@attrs.define
class LabelFormatOptionRequest:

    include_packing_slip_with_label: bool

    pass


@attrs.define
class Length:

    value: Union[float, int]

    unit: "UnitOfLength"
    pass


@attrs.define
class OrderItemId:

    pass


@attrs.define
class PackageDimension:

    pass


@attrs.define
class PackageDimensions:

    height: "PackageDimension"
    length: "PackageDimension"
    predefined_package_dimensions: "PredefinedPackageDimensions"
    unit: "UnitOfLength"
    width: "PackageDimension"
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
    rejection_reason_code: str
    rejection_reason_message: str
    shipping_service_name: str

    shipping_service_id: "ShippingServiceIdentifier"
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
    input_display_text: str
    is_required: bool

    constraints: "Constraints"
    input_target: "InputTargetType"
    restricted_set_values: "RestrictedSetValues"
    stored_value: "AdditionalSellerInput"
    pass


@attrs.define
class SellerOrderId:

    pass


@attrs.define
class Shipment:

    amazon_order_id: "AmazonOrderId"
    created_date: "Timestamp"
    insurance: "CurrencyAmount"
    item_list: "ItemList"
    label: "Label"
    last_updated_date: "Timestamp"
    package_dimensions: "PackageDimensions"
    seller_order_id: "SellerOrderId"
    ship_from_address: "Address"
    ship_to_address: "Address"
    shipment_id: "ShipmentId"
    shipping_service: "ShippingService"
    status: "ShipmentStatus"
    tracking_id: "TrackingId"
    weight: "Weight"
    pass


@attrs.define
class ShipmentId:

    pass


@attrs.define
class ShipmentRequestDetails:

    amazon_order_id: "AmazonOrderId"
    item_list: "ItemList"
    label_customization: "LabelCustomization"
    must_arrive_by_date: "Timestamp"
    package_dimensions: "PackageDimensions"
    seller_order_id: "SellerOrderId"
    ship_date: "Timestamp"
    ship_from_address: "Address"
    shipping_service_options: "ShippingServiceOptions"
    weight: "Weight"
    pass


@attrs.define
class ShipmentStatus:

    pass


@attrs.define
class ShippingOfferingFilter:

    include_complex_shipping_options: bool
    include_packing_slip_with_label: bool

    carrier_will_pick_up: "CarrierWillPickUpOption"
    delivery_experience: "DeliveryExperienceOption"
    pass


@attrs.define
class ShippingService:

    carrier_name: str
    requires_additional_seller_inputs: bool
    shipping_service_name: str
    shipping_service_offer_id: str

    available_format_options_for_label: "AvailableFormatOptionsForLabelList"
    available_label_formats: "LabelFormatList"
    available_shipping_service_options: "AvailableShippingServiceOptions"
    earliest_estimated_delivery_date: "Timestamp"
    latest_estimated_delivery_date: "Timestamp"
    rate: "CurrencyAmount"
    ship_date: "Timestamp"
    shipping_service_id: "ShippingServiceIdentifier"
    shipping_service_options: "ShippingServiceOptions"
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

    carrier_will_pick_up_option: "CarrierWillPickUpOption"
    declared_value: "CurrencyAmount"
    delivery_experience: "DeliveryExperienceType"
    label_format: "LabelFormat"
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

    pass


@attrs.define
class TemporarilyUnavailableCarrierList:

    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrier:

    carrier_name: str

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

    unit: "UnitOfWeight"
    value: "WeightValue"
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
