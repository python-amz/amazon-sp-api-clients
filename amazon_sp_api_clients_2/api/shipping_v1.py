"""
Selling Partner API for Shipping
=============================================================================================

Provides programmatic access to Amazon Shipping APIs.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class Error:
    pass


class ErrorList:
    pass


class AccountId:
    pass


class ShipmentId:
    pass


class ClientReferenceId:
    pass


class ContainerReferenceId:
    pass


class EventCode:
    pass


class StateOrRegion:
    pass


class City:
    pass


class CountryCode:
    pass


class PostalCode:
    pass


class Location:
    pass


class Event:
    pass


class EventList:
    pass


class TrackingId:
    pass


class TrackingSummary:
    pass


class PromisedDeliveryDate:
    pass


class Address:
    pass


class TimeRange:
    pass


class ShippingPromiseSet:
    pass


class ServiceType:
    pass


class ServiceTypeList:
    pass


class Rate:
    pass


class RateList:
    pass


class RateId:
    pass


class AcceptedRate:
    pass


class ServiceRate:
    pass


class ServiceRateList:
    pass


class Party:
    pass


class Currency:
    pass


class Dimensions:
    pass


class Weight:
    pass


class ContainerItem:
    pass


class Container:
    pass


class ContainerList:
    pass


class ContainerSpecification:
    pass


class ContainerSpecificationList:
    pass


class Label:
    pass


class LabelResult:
    pass


class LabelResultList:
    pass


class LabelStream:
    pass


class LabelSpecification:
    pass


class CreateShipmentRequest:
    pass


class PurchaseLabelsRequest:
    pass


class RetrieveShippingLabelRequest:
    pass


class GetRatesRequest:
    pass


class PurchaseShipmentRequest:
    pass


class CreateShipmentResult:
    pass


class Shipment:
    pass


class PurchaseLabelsResult:
    pass


class RetrieveShippingLabelResult:
    pass


class Account:
    pass


class GetRatesResult:
    pass


class PurchaseShipmentResult:
    pass


class TrackingInformation:
    pass


class CreateShipmentResponse:
    pass


class GetShipmentResponse:
    pass


class GetRatesResponse:
    pass


class PurchaseShipmentResponse:
    pass


class CancelShipmentResponse:
    pass


class PurchaseLabelsResponse:
    pass


class RetrieveShippingLabelResponse:
    pass


class GetAccountResponse:
    pass


class GetTrackingInformationResponse:
    pass


class ShippingV1Client(BaseClient):
    def cancel_shipment(
        self,
        shipment_id: str,
    ):
        """
        Cancel a shipment by the given shipmentId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
        """
        url = "/shipping/v1/shipments/{shipmentId}/cancel"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "POST", values, self._cancel_shipment_params)
        return response

    _cancel_shipment_params = (("shipmentId", "path"),)  # name, param in

    def create_shipment(
        self,
    ):
        """
        Create a new shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/shipments"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_shipment_params)
        return response

    _create_shipment_params = ()  # name, param in

    def get_account(
        self,
    ):
        """
        Verify if the current account is valid.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/account"
        values = ()
        response = self._parse_args_and_request(url, "GET", values, self._get_account_params)
        return response

    _get_account_params = ()  # name, param in

    def get_rates(
        self,
    ):
        """
        Get service rates.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/rates"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_rates_params)
        return response

    _get_rates_params = ()  # name, param in

    def get_shipment(
        self,
        shipment_id: str,
    ):
        """
        Return the entire shipment object for the shipmentId.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
        """
        url = "/shipping/v1/shipments/{shipmentId}"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_params)
        return response

    _get_shipment_params = (("shipmentId", "path"),)  # name, param in

    def get_tracking_information(
        self,
        tracking_id: str,
    ):
        """
        Return the tracking information of a shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            tracking_id: no description.
        """
        url = "/shipping/v1/tracking/{trackingId}"
        values = (tracking_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_tracking_information_params)
        return response

    _get_tracking_information_params = (("trackingId", "path"),)  # name, param in

    def purchase_labels(
        self,
        shipment_id: str,
        rate_id: str,
        label_specification: dict[str, Any],
    ):
        """
        Purchase shipping labels based on a given rate.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
            rate_id: An identifier for the rating.
            label_specification: The label specification info.
        """
        url = "/shipping/v1/shipments/{shipmentId}/purchaseLabels"
        values = (
            shipment_id,
            rate_id,
            label_specification,
        )
        response = self._parse_args_and_request(url, "POST", values, self._purchase_labels_params)
        return response

    _purchase_labels_params = (  # name, param in
        ("shipmentId", "path"),
        ("rateId", "body"),
        ("labelSpecification", "body"),
    )

    def purchase_shipment(
        self,
    ):
        """
        Purchase shipping labels.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/shipping/v1/purchaseShipment"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._purchase_shipment_params)
        return response

    _purchase_shipment_params = ()  # name, param in

    def retrieve_shipping_label(
        self,
        shipment_id: str,
        tracking_id: str,
        label_specification: dict[str, Any],
    ):
        """
        Retrieve shipping label based on the shipment id and tracking id.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: no description.
            tracking_id: no description.
            label_specification: The label specification info.
        """
        url = "/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label"
        values = (
            shipment_id,
            tracking_id,
            label_specification,
        )
        response = self._parse_args_and_request(url, "POST", values, self._retrieve_shipping_label_params)
        return response

    _retrieve_shipping_label_params = (  # name, param in
        ("shipmentId", "path"),
        ("trackingId", "path"),
        ("labelSpecification", "body"),
    )
