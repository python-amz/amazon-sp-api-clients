"""
Selling Partner API for Merchant Fulfillment
=============================================================================================

The Selling Partner API for Merchant Fulfillment helps you build applications that let sellers purchase shipping for non-Prime and Prime orders using Amazon’s Buy Shipping Services.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Union

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AdditionalInputs:
    additional_input_field_name: str = attrs.field()

    seller_input_definition: "SellerInputDefinition" = attrs.field()
    pass


@attrs.define
class AdditionalInputsList:
    pass


@attrs.define
class AdditionalSellerInput:
    data_type: str = attrs.field()
    value_as_boolean: bool = attrs.field()
    value_as_integer: int = attrs.field()
    value_as_string: str = attrs.field()

    value_as_address: "Address" = attrs.field()
    value_as_currency: "CurrencyAmount" = attrs.field()
    value_as_dimension: "Length" = attrs.field()
    value_as_timestamp: "Timestamp" = attrs.field()
    value_as_weight: "Weight" = attrs.field()
    pass


@attrs.define
class AdditionalSellerInputs:
    additional_input_field_name: str = attrs.field()

    additional_seller_input: "AdditionalSellerInput" = attrs.field()
    pass


@attrs.define
class AdditionalSellerInputsList:
    pass


@attrs.define
class Address:
    address_line1: "AddressLine1" = attrs.field()
    address_line2: "AddressLine2" = attrs.field()
    address_line3: "AddressLine3" = attrs.field()
    city: "City" = attrs.field()
    country_code: "CountryCode" = attrs.field()
    district_or_county: "DistrictOrCounty" = attrs.field()
    email: "EmailAddress" = attrs.field()
    name: "AddressName" = attrs.field()
    phone: "PhoneNumber" = attrs.field()
    postal_code: "PostalCode" = attrs.field()
    state_or_province_code: "StateOrProvinceCode" = attrs.field()
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
    carrier_will_pick_up_option: "CarrierWillPickUpOption" = attrs.field()
    charge: "CurrencyAmount" = attrs.field()
    pass


@attrs.define
class AvailableCarrierWillPickUpOptionsList:
    pass


@attrs.define
class AvailableDeliveryExperienceOption:
    charge: "CurrencyAmount" = attrs.field()
    delivery_experience_option: "DeliveryExperienceOption" = attrs.field()
    pass


@attrs.define
class AvailableDeliveryExperienceOptionsList:
    pass


@attrs.define
class AvailableFormatOptionsForLabelList:
    pass


@attrs.define
class AvailableShippingServiceOptions:
    available_carrier_will_pick_up_options: "AvailableCarrierWillPickUpOptionsList" = attrs.field()
    available_delivery_experience_options: "AvailableDeliveryExperienceOptionsList" = attrs.field()
    pass


@attrs.define
class CancelShipmentResponse:
    errors: "ErrorList" = attrs.field()
    payload: "Shipment" = attrs.field()
    pass


@attrs.define
class CarrierWillPickUpOption:
    pass


@attrs.define
class City:
    pass


@attrs.define
class Constraint:
    validation_reg_ex: str = attrs.field()
    validation_string: str = attrs.field()

    pass


@attrs.define
class Constraints:
    pass


@attrs.define
class CountryCode:
    pass


@attrs.define
class CreateShipmentRequest:
    shipping_service_offer_id: str = attrs.field()

    hazmat_type: "HazmatType" = attrs.field()
    label_format_option: "LabelFormatOptionRequest" = attrs.field()
    shipment_level_seller_inputs_list: "AdditionalSellerInputsList" = attrs.field()
    shipment_request_details: "ShipmentRequestDetails" = attrs.field()
    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    pass


@attrs.define
class CreateShipmentResponse:
    errors: "ErrorList" = attrs.field()
    payload: "Shipment" = attrs.field()
    pass


@attrs.define
class CurrencyAmount:
    amount: Union[float, int] = attrs.field()
    # {'schema_format': 'double'}
    currency_code: str = attrs.field()
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
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class FileContents:
    checksum: str = attrs.field()
    contents: str = attrs.field()

    file_type: "FileType" = attrs.field()
    pass


@attrs.define
class FileType:
    pass


@attrs.define
class GetAdditionalSellerInputsRequest:
    order_id: "AmazonOrderId" = attrs.field()
    ship_from_address: "Address" = attrs.field()
    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    pass


@attrs.define
class GetAdditionalSellerInputsResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetAdditionalSellerInputsResult" = attrs.field()
    pass


@attrs.define
class GetAdditionalSellerInputsResult:
    item_level_fields_list: "ItemLevelFieldsList" = attrs.field()
    shipment_level_fields: "AdditionalInputsList" = attrs.field()
    pass


@attrs.define
class GetEligibleShipmentServicesRequest:
    shipment_request_details: "ShipmentRequestDetails" = attrs.field()
    shipping_offering_filter: "ShippingOfferingFilter" = attrs.field()
    pass


@attrs.define
class GetEligibleShipmentServicesResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetEligibleShipmentServicesResult" = attrs.field()
    pass


@attrs.define
class GetEligibleShipmentServicesResult:
    rejected_shipping_service_list: "RejectedShippingServiceList" = attrs.field()
    shipping_service_list: "ShippingServiceList" = attrs.field()
    temporarily_unavailable_carrier_list: "TemporarilyUnavailableCarrierList" = attrs.field()
    terms_and_conditions_not_accepted_carrier_list: "TermsAndConditionsNotAcceptedCarrierList" = attrs.field()
    pass


@attrs.define
class GetShipmentResponse:
    errors: "ErrorList" = attrs.field()
    payload: "Shipment" = attrs.field()
    pass


@attrs.define
class HazmatType:
    pass


@attrs.define
class InputTargetType:
    pass


@attrs.define
class Item:
    item_description: "ItemDescription" = attrs.field()
    item_level_seller_inputs_list: "AdditionalSellerInputsList" = attrs.field()
    item_weight: "Weight" = attrs.field()
    order_item_id: "OrderItemId" = attrs.field()
    quantity: "ItemQuantity" = attrs.field()
    transparency_code_list: "TransparencyCodeList" = attrs.field()
    pass


@attrs.define
class ItemDescription:
    pass


@attrs.define
class ItemLevelFields:
    asin: str = attrs.field()

    additional_inputs: "AdditionalInputsList" = attrs.field()
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
    custom_text_for_label: "CustomTextForLabel" = attrs.field()
    dimensions: "LabelDimensions" = attrs.field()
    file_contents: "FileContents" = attrs.field()
    label_format: "LabelFormat" = attrs.field()
    standard_id_for_label: "StandardIdForLabel" = attrs.field()
    pass


@attrs.define
class LabelCustomization:
    custom_text_for_label: "CustomTextForLabel" = attrs.field()
    standard_id_for_label: "StandardIdForLabel" = attrs.field()
    pass


@attrs.define
class LabelDimension:
    pass


@attrs.define
class LabelDimensions:
    length: "LabelDimension" = attrs.field()
    unit: "UnitOfLength" = attrs.field()
    width: "LabelDimension" = attrs.field()
    pass


@attrs.define
class LabelFormat:
    pass


@attrs.define
class LabelFormatList:
    pass


@attrs.define
class LabelFormatOption:
    include_packing_slip_with_label: bool = attrs.field()

    label_format: "LabelFormat" = attrs.field()
    pass


@attrs.define
class LabelFormatOptionRequest:
    include_packing_slip_with_label: bool = attrs.field()

    pass


@attrs.define
class Length:
    value: Union[float, int] = attrs.field()

    unit: "UnitOfLength" = attrs.field()
    pass


@attrs.define
class OrderItemId:
    pass


@attrs.define
class PackageDimension:
    pass


@attrs.define
class PackageDimensions:
    height: "PackageDimension" = attrs.field()
    length: "PackageDimension" = attrs.field()
    predefined_package_dimensions: "PredefinedPackageDimensions" = attrs.field()
    unit: "UnitOfLength" = attrs.field()
    width: "PackageDimension" = attrs.field()
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
    carrier_name: str = attrs.field()
    rejection_reason_code: str = attrs.field()
    rejection_reason_message: str = attrs.field()
    shipping_service_name: str = attrs.field()

    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    pass


@attrs.define
class RejectedShippingServiceList:
    pass


@attrs.define
class RestrictedSetValues:
    pass


@attrs.define
class SellerInputDefinition:
    data_type: str = attrs.field()
    input_display_text: str = attrs.field()
    is_required: bool = attrs.field()

    constraints: "Constraints" = attrs.field()
    input_target: "InputTargetType" = attrs.field()
    restricted_set_values: "RestrictedSetValues" = attrs.field()
    stored_value: "AdditionalSellerInput" = attrs.field()
    pass


@attrs.define
class SellerOrderId:
    pass


@attrs.define
class Shipment:
    amazon_order_id: "AmazonOrderId" = attrs.field()
    created_date: "Timestamp" = attrs.field()
    insurance: "CurrencyAmount" = attrs.field()
    item_list: "ItemList" = attrs.field()
    label: "Label" = attrs.field()
    last_updated_date: "Timestamp" = attrs.field()
    package_dimensions: "PackageDimensions" = attrs.field()
    seller_order_id: "SellerOrderId" = attrs.field()
    ship_from_address: "Address" = attrs.field()
    ship_to_address: "Address" = attrs.field()
    shipment_id: "ShipmentId" = attrs.field()
    shipping_service: "ShippingService" = attrs.field()
    status: "ShipmentStatus" = attrs.field()
    tracking_id: "TrackingId" = attrs.field()
    weight: "Weight" = attrs.field()
    pass


@attrs.define
class ShipmentId:
    pass


@attrs.define
class ShipmentRequestDetails:
    amazon_order_id: "AmazonOrderId" = attrs.field()
    item_list: "ItemList" = attrs.field()
    label_customization: "LabelCustomization" = attrs.field()
    must_arrive_by_date: "Timestamp" = attrs.field()
    package_dimensions: "PackageDimensions" = attrs.field()
    seller_order_id: "SellerOrderId" = attrs.field()
    ship_date: "Timestamp" = attrs.field()
    ship_from_address: "Address" = attrs.field()
    shipping_service_options: "ShippingServiceOptions" = attrs.field()
    weight: "Weight" = attrs.field()
    pass


@attrs.define
class ShipmentStatus:
    pass


@attrs.define
class ShippingOfferingFilter:
    include_complex_shipping_options: bool = attrs.field()
    include_packing_slip_with_label: bool = attrs.field()

    carrier_will_pick_up: "CarrierWillPickUpOption" = attrs.field()
    delivery_experience: "DeliveryExperienceOption" = attrs.field()
    pass


@attrs.define
class ShippingService:
    carrier_name: str = attrs.field()
    requires_additional_seller_inputs: bool = attrs.field()
    shipping_service_name: str = attrs.field()
    shipping_service_offer_id: str = attrs.field()

    available_format_options_for_label: "AvailableFormatOptionsForLabelList" = attrs.field()
    available_label_formats: "LabelFormatList" = attrs.field()
    available_shipping_service_options: "AvailableShippingServiceOptions" = attrs.field()
    earliest_estimated_delivery_date: "Timestamp" = attrs.field()
    latest_estimated_delivery_date: "Timestamp" = attrs.field()
    rate: "CurrencyAmount" = attrs.field()
    ship_date: "Timestamp" = attrs.field()
    shipping_service_id: "ShippingServiceIdentifier" = attrs.field()
    shipping_service_options: "ShippingServiceOptions" = attrs.field()
    pass


@attrs.define
class ShippingServiceIdentifier:
    pass


@attrs.define
class ShippingServiceList:
    pass


@attrs.define
class ShippingServiceOptions:
    carrier_will_pick_up: bool = attrs.field()

    carrier_will_pick_up_option: "CarrierWillPickUpOption" = attrs.field()
    declared_value: "CurrencyAmount" = attrs.field()
    delivery_experience: "DeliveryExperienceType" = attrs.field()
    label_format: "LabelFormat" = attrs.field()
    pass


@attrs.define
class StandardIdForLabel:
    pass


@attrs.define
class StateOrProvinceCode:
    pass


@attrs.define
class TemporarilyUnavailableCarrier:
    carrier_name: str = attrs.field()

    pass


@attrs.define
class TemporarilyUnavailableCarrierList:
    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrier:
    carrier_name: str = attrs.field()

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
    unit: "UnitOfWeight" = attrs.field()
    value: "WeightValue" = attrs.field()
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
