"""
Selling Partner API for Shipping
=============================================================================================

Provides programmatic access to Amazon Shipping APIs.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Any, Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AcceptedRate:
    billed_weight: "Weight" = attrs.field()
    promise: "ShippingPromiseSet" = attrs.field()
    service_type: "ServiceType" = attrs.field()
    total_charge: "Currency" = attrs.field()
    pass


@attrs.define
class Account:
    account_id: "AccountId" = attrs.field()
    pass


@attrs.define
class AccountId:
    pass


@attrs.define
class Address:
    address_line1: str = attrs.field()
    # {'maxLength': 60, 'minLength': 1}
    address_line2: str = attrs.field()
    # {'maxLength': 60, 'minLength': 1}
    address_line3: str = attrs.field()
    # {'maxLength': 60, 'minLength': 1}
    copy_emails: list[str] = attrs.field()
    # {'maxItems': 2}
    email: str = attrs.field()
    # {'maxLength': 64}
    name: str = attrs.field()
    # {'maxLength': 50, 'minLength': 1}
    phone_number: str = attrs.field()
    # {'maxLength': 20, 'minLength': 1}

    city: "City" = attrs.field()
    country_code: "CountryCode" = attrs.field()
    postal_code: "PostalCode" = attrs.field()
    state_or_region: "StateOrRegion" = attrs.field()
    pass


@attrs.define
class CancelShipmentResponse:
    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class City:
    pass


@attrs.define
class ClientReferenceId:
    pass


@attrs.define
class Container:
    container_type: Union[Literal["PACKAGE"]] = attrs.field()
    items: list["ContainerItem"] = attrs.field()

    container_reference_id: "ContainerReferenceId" = attrs.field()
    dimensions: "Dimensions" = attrs.field()
    value: "Currency" = attrs.field()
    weight: "Weight" = attrs.field()
    pass


@attrs.define
class ContainerItem:
    quantity: Union[float, int] = attrs.field()
    title: str = attrs.field()
    # {'maxLength': 30}

    unit_price: "Currency" = attrs.field()
    unit_weight: "Weight" = attrs.field()
    pass


@attrs.define
class ContainerList:
    pass


@attrs.define
class ContainerReferenceId:
    pass


@attrs.define
class ContainerSpecification:
    dimensions: "Dimensions" = attrs.field()
    weight: "Weight" = attrs.field()
    pass


@attrs.define
class ContainerSpecificationList:
    pass


@attrs.define
class CountryCode:
    pass


@attrs.define
class CreateShipmentRequest:
    client_reference_id: "ClientReferenceId" = attrs.field()
    containers: "ContainerList" = attrs.field()
    ship_from: "Address" = attrs.field()
    ship_to: "Address" = attrs.field()
    pass


@attrs.define
class CreateShipmentResponse:
    errors: "ErrorList" = attrs.field()
    payload: "CreateShipmentResult" = attrs.field()
    pass


@attrs.define
class CreateShipmentResult:
    eligible_rates: "RateList" = attrs.field()
    shipment_id: "ShipmentId" = attrs.field()
    pass


@attrs.define
class Currency:
    unit: str = attrs.field()
    # {'maxLength': 3, 'minLength': 3}
    value: Union[float, int] = attrs.field()

    pass


@attrs.define
class Dimensions:
    height: Union[float, int] = attrs.field()
    length: Union[float, int] = attrs.field()
    unit: Union[Literal["IN"], Literal["CM"]] = attrs.field()
    width: Union[float, int] = attrs.field()

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
class Event:
    event_time: str = attrs.field()
    # {'schema_format': 'date-time'}

    event_code: "EventCode" = attrs.field()
    location: "Location" = attrs.field()
    pass


@attrs.define
class EventCode:
    pass


@attrs.define
class EventList:
    pass


@attrs.define
class GetAccountResponse:
    errors: "ErrorList" = attrs.field()
    payload: "Account" = attrs.field()
    pass


@attrs.define
class GetRatesRequest:
    ship_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    container_specifications: "ContainerSpecificationList" = attrs.field()
    service_types: "ServiceTypeList" = attrs.field()
    ship_from: "Address" = attrs.field()
    ship_to: "Address" = attrs.field()
    pass


@attrs.define
class GetRatesResponse:
    errors: "ErrorList" = attrs.field()
    payload: "GetRatesResult" = attrs.field()
    pass


@attrs.define
class GetRatesResult:
    service_rates: "ServiceRateList" = attrs.field()
    pass


@attrs.define
class GetShipmentResponse:
    errors: "ErrorList" = attrs.field()
    payload: "Shipment" = attrs.field()
    pass


@attrs.define
class GetTrackingInformationResponse:
    errors: "ErrorList" = attrs.field()
    payload: "TrackingInformation" = attrs.field()
    pass


@attrs.define
class Label:
    label_specification: "LabelSpecification" = attrs.field()
    label_stream: "LabelStream" = attrs.field()
    pass


@attrs.define
class LabelResult:
    tracking_id: str = attrs.field()

    container_reference_id: "ContainerReferenceId" = attrs.field()
    label: "Label" = attrs.field()
    pass


@attrs.define
class LabelResultList:
    pass


@attrs.define
class LabelSpecification:
    label_format: Union[Literal["PNG"]] = attrs.field()
    label_stock_size: Union[Literal["4x6"]] = attrs.field()

    pass


@attrs.define
class LabelStream:
    pass


@attrs.define
class Location:
    city: "City" = attrs.field()
    country_code: "CountryCode" = attrs.field()
    postal_code: "PostalCode" = attrs.field()
    state_or_region: "StateOrRegion" = attrs.field()
    pass


@attrs.define
class Party:
    account_id: "AccountId" = attrs.field()
    pass


@attrs.define
class PostalCode:
    pass


@attrs.define
class PromisedDeliveryDate:
    pass


@attrs.define
class PurchaseLabelsRequest:
    label_specification: "LabelSpecification" = attrs.field()
    rate_id: "RateId" = attrs.field()
    pass


@attrs.define
class PurchaseLabelsResponse:
    errors: "ErrorList" = attrs.field()
    payload: "PurchaseLabelsResult" = attrs.field()
    pass


@attrs.define
class PurchaseLabelsResult:
    accepted_rate: "AcceptedRate" = attrs.field()
    client_reference_id: "ClientReferenceId" = attrs.field()
    label_results: "LabelResultList" = attrs.field()
    shipment_id: "ShipmentId" = attrs.field()
    pass


@attrs.define
class PurchaseShipmentRequest:
    ship_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    client_reference_id: "ClientReferenceId" = attrs.field()
    containers: "ContainerList" = attrs.field()
    label_specification: "LabelSpecification" = attrs.field()
    service_type: "ServiceType" = attrs.field()
    ship_from: "Address" = attrs.field()
    ship_to: "Address" = attrs.field()
    pass


@attrs.define
class PurchaseShipmentResponse:
    errors: "ErrorList" = attrs.field()
    payload: "PurchaseShipmentResult" = attrs.field()
    pass


@attrs.define
class PurchaseShipmentResult:
    label_results: "LabelResultList" = attrs.field()
    service_rate: "ServiceRate" = attrs.field()
    shipment_id: "ShipmentId" = attrs.field()
    pass


@attrs.define
class Rate:
    expiration_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    rate_id: str = attrs.field()

    billed_weight: "Weight" = attrs.field()
    promise: "ShippingPromiseSet" = attrs.field()
    service_type: "ServiceType" = attrs.field()
    total_charge: "Currency" = attrs.field()
    pass


@attrs.define
class RateId:
    pass


@attrs.define
class RateList:
    pass


@attrs.define
class RetrieveShippingLabelRequest:
    label_specification: "LabelSpecification" = attrs.field()
    pass


@attrs.define
class RetrieveShippingLabelResponse:
    errors: "ErrorList" = attrs.field()
    payload: "RetrieveShippingLabelResult" = attrs.field()
    pass


@attrs.define
class RetrieveShippingLabelResult:
    label_specification: "LabelSpecification" = attrs.field()
    label_stream: "LabelStream" = attrs.field()
    pass


@attrs.define
class ServiceRate:
    billable_weight: "Weight" = attrs.field()
    promise: "ShippingPromiseSet" = attrs.field()
    service_type: "ServiceType" = attrs.field()
    total_charge: "Currency" = attrs.field()
    pass


@attrs.define
class ServiceRateList:
    pass


@attrs.define
class ServiceType:
    pass


@attrs.define
class ServiceTypeList:
    pass


@attrs.define
class Shipment:
    accepted_rate: "AcceptedRate" = attrs.field()
    client_reference_id: "ClientReferenceId" = attrs.field()
    containers: "ContainerList" = attrs.field()
    ship_from: "Address" = attrs.field()
    ship_to: "Address" = attrs.field()
    shipment_id: "ShipmentId" = attrs.field()
    shipper: "Party" = attrs.field()
    pass


@attrs.define
class ShipmentId:
    pass


@attrs.define
class ShippingPromiseSet:
    delivery_window: "TimeRange" = attrs.field()
    receive_window: "TimeRange" = attrs.field()
    pass


@attrs.define
class StateOrRegion:
    pass


@attrs.define
class TimeRange:
    end: str = attrs.field()
    # {'schema_format': 'date-time'}
    start: str = attrs.field()
    # {'schema_format': 'date-time'}

    pass


@attrs.define
class TrackingId:
    pass


@attrs.define
class TrackingInformation:
    event_history: "EventList" = attrs.field()
    promised_delivery_date: "PromisedDeliveryDate" = attrs.field()
    summary: "TrackingSummary" = attrs.field()
    tracking_id: "TrackingId" = attrs.field()
    pass


@attrs.define
class TrackingSummary:
    status: str = attrs.field()
    # {'maxLength': 60, 'minLength': 1}

    pass


@attrs.define
class Weight:
    unit: Union[Literal["g"], Literal["kg"], Literal["oz"], Literal["lb"]] = attrs.field()
    value: Union[float, int] = attrs.field()

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
