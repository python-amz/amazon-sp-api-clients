"""
Selling Partner API for Merchant Fulfillment
=============================================================================================

The Selling Partner API for Merchant Fulfillment helps you build applications that let sellers purchase shipping for non-Prime and Prime orders using Amazon¡¯s Buy Shipping Services.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class LabelFormatOptionRequest:
    pass


@attrs.define
class LabelFormatOption:
    pass


@attrs.define
class AvailableCarrierWillPickUpOption:
    pass


@attrs.define
class AvailableCarrierWillPickUpOptionsList:
    pass


@attrs.define
class AvailableDeliveryExperienceOption:
    pass


@attrs.define
class AvailableDeliveryExperienceOptionsList:
    pass


@attrs.define
class AvailableShippingServiceOptions:
    pass


@attrs.define
class AvailableFormatOptionsForLabel:
    pass


@attrs.define
class AvailableFormatOptionsForLabelList:
    pass


@attrs.define
class Constraint:
    pass


@attrs.define
class Constraints:
    pass


@attrs.define
class AdditionalInputs:
    pass


@attrs.define
class SellerInputDefinition:
    pass


@attrs.define
class InputTargetType:
    pass


@attrs.define
class AdditionalInputsList:
    pass


@attrs.define
class AdditionalSellerInput:
    pass


@attrs.define
class AdditionalSellerInputs:
    pass


@attrs.define
class AdditionalSellerInputsList:
    pass


@attrs.define
class Address:
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
class CancelShipmentResponse:
    pass


@attrs.define
class City:
    pass


@attrs.define
class CountryCode:
    pass


@attrs.define
class CreateShipmentRequest:
    pass


@attrs.define
class CreateShipmentResponse:
    pass


@attrs.define
class ItemLevelFields:
    pass


@attrs.define
class ItemLevelFieldsList:
    pass


@attrs.define
class GetAdditionalSellerInputsRequest:
    pass


@attrs.define
class GetAdditionalSellerInputsResult:
    pass


@attrs.define
class GetAdditionalSellerInputsResponse:
    pass


@attrs.define
class CurrencyAmount:
    pass


@attrs.define
class CustomTextForLabel:
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
class FileContents:
    pass


@attrs.define
class FileType:
    pass


@attrs.define
class GetEligibleShipmentServicesRequest:
    pass


@attrs.define
class GetEligibleShipmentServicesResponse:
    pass


@attrs.define
class GetEligibleShipmentServicesResult:
    pass


@attrs.define
class GetShipmentResponse:
    pass


@attrs.define
class HazmatType:
    pass


@attrs.define
class Item:
    pass


@attrs.define
class ItemList:
    pass


@attrs.define
class ItemQuantity:
    pass


@attrs.define
class ItemDescription:
    pass


@attrs.define
class Label:
    pass


@attrs.define
class LabelCustomization:
    pass


@attrs.define
class LabelDimension:
    pass


@attrs.define
class LabelDimensions:
    pass


@attrs.define
class LabelFormat:
    pass


@attrs.define
class LabelFormatList:
    pass


@attrs.define
class Length:
    pass


@attrs.define
class OrderItemId:
    pass


@attrs.define
class PackageDimension:
    pass


@attrs.define
class PackageDimensions:
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
class RestrictedSetValues:
    pass


@attrs.define
class SellerOrderId:
    pass


@attrs.define
class Shipment:
    pass


@attrs.define
class ShipmentId:
    pass


@attrs.define
class ShipmentRequestDetails:
    pass


@attrs.define
class ShipmentStatus:
    pass


@attrs.define
class DeliveryExperienceOption:
    pass


@attrs.define
class ShippingOfferingFilter:
    pass


@attrs.define
class ShippingService:
    pass


@attrs.define
class ShippingServiceIdentifier:
    pass


@attrs.define
class ShippingServiceList:
    pass


@attrs.define
class ShippingServiceOptions:
    pass


@attrs.define
class CarrierWillPickUpOption:
    pass


@attrs.define
class StandardIdForLabel:
    pass


@attrs.define
class StateOrProvinceCode:
    pass


@attrs.define
class RejectedShippingService:
    pass


@attrs.define
class RejectedShippingServiceList:
    pass


@attrs.define
class TemporarilyUnavailableCarrier:
    pass


@attrs.define
class TemporarilyUnavailableCarrierList:
    pass


@attrs.define
class TermsAndConditionsNotAcceptedCarrier:
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
