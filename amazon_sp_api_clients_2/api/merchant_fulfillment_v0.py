"""
Selling Partner API for Merchant Fulfillment
=============================================================================================

The Selling Partner API for Merchant Fulfillment helps you build applications that let sellers purchase shipping for non-Prime and Prime orders using Amazon¡¯s Buy Shipping Services.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class Error:
    pass


class ErrorList:
    pass


class LabelFormatOptionRequest:
    pass


class LabelFormatOption:
    pass


class AvailableCarrierWillPickUpOption:
    pass


class AvailableCarrierWillPickUpOptionsList:
    pass


class AvailableDeliveryExperienceOption:
    pass


class AvailableDeliveryExperienceOptionsList:
    pass


class AvailableShippingServiceOptions:
    pass


class AvailableFormatOptionsForLabel:
    pass


class AvailableFormatOptionsForLabelList:
    pass


class Constraint:
    pass


class Constraints:
    pass


class AdditionalInputs:
    pass


class SellerInputDefinition:
    pass


class InputTargetType:
    pass


class AdditionalInputsList:
    pass


class AdditionalSellerInput:
    pass


class AdditionalSellerInputs:
    pass


class AdditionalSellerInputsList:
    pass


class Address:
    pass


class AddressLine1:
    pass


class AddressLine2:
    pass


class AddressLine3:
    pass


class AddressName:
    pass


class AmazonOrderId:
    pass


class CancelShipmentResponse:
    pass


class City:
    pass


class CountryCode:
    pass


class CreateShipmentRequest:
    pass


class CreateShipmentResponse:
    pass


class ItemLevelFields:
    pass


class ItemLevelFieldsList:
    pass


class GetAdditionalSellerInputsRequest:
    pass


class GetAdditionalSellerInputsResult:
    pass


class GetAdditionalSellerInputsResponse:
    pass


class CurrencyAmount:
    pass


class CustomTextForLabel:
    pass


class DeliveryExperienceType:
    pass


class DistrictOrCounty:
    pass


class EmailAddress:
    pass


class FileContents:
    pass


class FileType:
    pass


class GetEligibleShipmentServicesRequest:
    pass


class GetEligibleShipmentServicesResponse:
    pass


class GetEligibleShipmentServicesResult:
    pass


class GetShipmentResponse:
    pass


class HazmatType:
    pass


class Item:
    pass


class ItemList:
    pass


class ItemQuantity:
    pass


class ItemDescription:
    pass


class Label:
    pass


class LabelCustomization:
    pass


class LabelDimension:
    pass


class LabelDimensions:
    pass


class LabelFormat:
    pass


class LabelFormatList:
    pass


class Length:
    pass


class OrderItemId:
    pass


class PackageDimension:
    pass


class PackageDimensions:
    pass


class PhoneNumber:
    pass


class PostalCode:
    pass


class PredefinedPackageDimensions:
    pass


class RestrictedSetValues:
    pass


class SellerOrderId:
    pass


class Shipment:
    pass


class ShipmentId:
    pass


class ShipmentRequestDetails:
    pass


class ShipmentStatus:
    pass


class DeliveryExperienceOption:
    pass


class ShippingOfferingFilter:
    pass


class ShippingService:
    pass


class ShippingServiceIdentifier:
    pass


class ShippingServiceList:
    pass


class ShippingServiceOptions:
    pass


class CarrierWillPickUpOption:
    pass


class StandardIdForLabel:
    pass


class StateOrProvinceCode:
    pass


class RejectedShippingService:
    pass


class RejectedShippingServiceList:
    pass


class TemporarilyUnavailableCarrier:
    pass


class TemporarilyUnavailableCarrierList:
    pass


class TermsAndConditionsNotAcceptedCarrier:
    pass


class TermsAndConditionsNotAcceptedCarrierList:
    pass


class Timestamp:
    pass


class TrackingId:
    pass


class TransparencyCode:
    pass


class TransparencyCodeList:
    pass


class UnitOfLength:
    pass


class UnitOfWeight:
    pass


class Weight:
    pass


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
