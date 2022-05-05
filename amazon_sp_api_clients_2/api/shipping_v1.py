"""
Selling Partner API for Shipping
=============================================================================================

Provides programmatic access to Amazon Shipping APIs.
API Version: v1
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
class AccountId:
    pass


@attrs.define
class ShipmentId:
    pass


@attrs.define
class ClientReferenceId:
    pass


@attrs.define
class ContainerReferenceId:
    pass


@attrs.define
class EventCode:
    pass


@attrs.define
class StateOrRegion:
    pass


@attrs.define
class City:
    pass


@attrs.define
class CountryCode:
    pass


@attrs.define
class PostalCode:
    pass


@attrs.define
class Location:
    pass


@attrs.define
class Event:
    pass


@attrs.define
class EventList:
    pass


@attrs.define
class TrackingId:
    pass


@attrs.define
class TrackingSummary:
    pass


@attrs.define
class PromisedDeliveryDate:
    pass


@attrs.define
class Address:
    pass


@attrs.define
class TimeRange:
    pass


@attrs.define
class ShippingPromiseSet:
    pass


@attrs.define
class ServiceType:
    pass


@attrs.define
class ServiceTypeList:
    pass


@attrs.define
class Rate:
    pass


@attrs.define
class RateList:
    pass


@attrs.define
class RateId:
    pass


@attrs.define
class AcceptedRate:
    pass


@attrs.define
class ServiceRate:
    pass


@attrs.define
class ServiceRateList:
    pass


@attrs.define
class Party:
    pass


@attrs.define
class Currency:
    pass


@attrs.define
class Dimensions:
    pass


@attrs.define
class Weight:
    pass


@attrs.define
class ContainerItem:
    pass


@attrs.define
class Container:
    pass


@attrs.define
class ContainerList:
    pass


@attrs.define
class ContainerSpecification:
    pass


@attrs.define
class ContainerSpecificationList:
    pass


@attrs.define
class Label:
    pass


@attrs.define
class LabelResult:
    pass


@attrs.define
class LabelResultList:
    pass


@attrs.define
class LabelStream:
    pass


@attrs.define
class LabelSpecification:
    pass


@attrs.define
class CreateShipmentRequest:
    pass


@attrs.define
class PurchaseLabelsRequest:
    pass


@attrs.define
class RetrieveShippingLabelRequest:
    pass


@attrs.define
class GetRatesRequest:
    pass


@attrs.define
class PurchaseShipmentRequest:
    pass


@attrs.define
class CreateShipmentResult:
    pass


@attrs.define
class Shipment:
    pass


@attrs.define
class PurchaseLabelsResult:
    pass


@attrs.define
class RetrieveShippingLabelResult:
    pass


@attrs.define
class Account:
    pass


@attrs.define
class GetRatesResult:
    pass


@attrs.define
class PurchaseShipmentResult:
    pass


@attrs.define
class TrackingInformation:
    pass


@attrs.define
class CreateShipmentResponse:
    pass


@attrs.define
class GetShipmentResponse:
    pass


@attrs.define
class GetRatesResponse:
    pass


@attrs.define
class PurchaseShipmentResponse:
    pass


@attrs.define
class CancelShipmentResponse:
    pass


@attrs.define
class PurchaseLabelsResponse:
    pass


@attrs.define
class RetrieveShippingLabelResponse:
    pass


@attrs.define
class GetAccountResponse:
    pass


@attrs.define
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
