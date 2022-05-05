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
class AcceptedRate:

    billed_weight: "Weight"
    promise: "ShippingPromiseSet"
    service_type: "ServiceType"
    total_charge: "Currency"
    pass


@attrs.define
class Account:

    account_id: "AccountId"
    pass


@attrs.define
class AccountId:

    pass


@attrs.define
class Address:

    address_line1: str
    # {'maxLength': 60, 'minLength': 1}
    address_line2: str
    # {'maxLength': 60, 'minLength': 1}
    address_line3: str
    # {'maxLength': 60, 'minLength': 1}
    copy_emails: list[str]
    # {'maxItems': 2}
    email: str
    # {'maxLength': 64}
    name: str
    # {'maxLength': 50, 'minLength': 1}
    phone_number: str
    # {'maxLength': 20, 'minLength': 1}

    city: "City"
    country_code: "CountryCode"
    postal_code: "PostalCode"
    state_or_region: "StateOrRegion"
    pass


@attrs.define
class CancelShipmentResponse:

    errors: "ErrorList"
    pass


@attrs.define
class City:

    pass


@attrs.define
class ClientReferenceId:

    pass


@attrs.define
class Container:

    container_type: Union[Literal["PACKAGE"]]
    items: list["ContainerItem"]

    container_reference_id: "ContainerReferenceId"
    dimensions: "Dimensions"
    value: "Currency"
    weight: "Weight"
    pass


@attrs.define
class ContainerItem:

    quantity: Union[float, int]
    title: str
    # {'maxLength': 30}

    unit_price: "Currency"
    unit_weight: "Weight"
    pass


@attrs.define
class ContainerList:

    pass


@attrs.define
class ContainerReferenceId:

    pass


@attrs.define
class ContainerSpecification:

    dimensions: "Dimensions"
    weight: "Weight"
    pass


@attrs.define
class ContainerSpecificationList:

    pass


@attrs.define
class CountryCode:

    pass


@attrs.define
class CreateShipmentRequest:

    client_reference_id: "ClientReferenceId"
    containers: "ContainerList"
    ship_from: "Address"
    ship_to: "Address"
    pass


@attrs.define
class CreateShipmentResponse:

    errors: "ErrorList"
    payload: "CreateShipmentResult"
    pass


@attrs.define
class CreateShipmentResult:

    eligible_rates: "RateList"
    shipment_id: "ShipmentId"
    pass


@attrs.define
class Currency:

    unit: str
    # {'maxLength': 3, 'minLength': 3}
    value: Union[float, int]

    pass


@attrs.define
class Dimensions:

    height: Union[float, int]
    length: Union[float, int]
    unit: Union[Literal["IN"], Literal["CM"]]
    width: Union[float, int]

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
class Event:

    event_time: str
    # {'schema_format': 'date-time'}

    event_code: "EventCode"
    location: "Location"
    pass


@attrs.define
class EventCode:

    pass


@attrs.define
class EventList:

    pass


@attrs.define
class GetAccountResponse:

    errors: "ErrorList"
    payload: "Account"
    pass


@attrs.define
class GetRatesRequest:

    ship_date: str
    # {'schema_format': 'date-time'}

    container_specifications: "ContainerSpecificationList"
    service_types: "ServiceTypeList"
    ship_from: "Address"
    ship_to: "Address"
    pass


@attrs.define
class GetRatesResponse:

    errors: "ErrorList"
    payload: "GetRatesResult"
    pass


@attrs.define
class GetRatesResult:

    service_rates: "ServiceRateList"
    pass


@attrs.define
class GetShipmentResponse:

    errors: "ErrorList"
    payload: "Shipment"
    pass


@attrs.define
class GetTrackingInformationResponse:

    errors: "ErrorList"
    payload: "TrackingInformation"
    pass


@attrs.define
class Label:

    label_specification: "LabelSpecification"
    label_stream: "LabelStream"
    pass


@attrs.define
class LabelResult:

    tracking_id: str

    container_reference_id: "ContainerReferenceId"
    label: "Label"
    pass


@attrs.define
class LabelResultList:

    pass


@attrs.define
class LabelSpecification:

    label_format: Union[Literal["PNG"]]
    label_stock_size: Union[Literal["4x6"]]

    pass


@attrs.define
class LabelStream:

    pass


@attrs.define
class Location:

    city: "City"
    country_code: "CountryCode"
    postal_code: "PostalCode"
    state_or_region: "StateOrRegion"
    pass


@attrs.define
class Party:

    account_id: "AccountId"
    pass


@attrs.define
class PostalCode:

    pass


@attrs.define
class PromisedDeliveryDate:

    pass


@attrs.define
class PurchaseLabelsRequest:

    label_specification: "LabelSpecification"
    rate_id: "RateId"
    pass


@attrs.define
class PurchaseLabelsResponse:

    errors: "ErrorList"
    payload: "PurchaseLabelsResult"
    pass


@attrs.define
class PurchaseLabelsResult:

    accepted_rate: "AcceptedRate"
    client_reference_id: "ClientReferenceId"
    label_results: "LabelResultList"
    shipment_id: "ShipmentId"
    pass


@attrs.define
class PurchaseShipmentRequest:

    ship_date: str
    # {'schema_format': 'date-time'}

    client_reference_id: "ClientReferenceId"
    containers: "ContainerList"
    label_specification: "LabelSpecification"
    service_type: "ServiceType"
    ship_from: "Address"
    ship_to: "Address"
    pass


@attrs.define
class PurchaseShipmentResponse:

    errors: "ErrorList"
    payload: "PurchaseShipmentResult"
    pass


@attrs.define
class PurchaseShipmentResult:

    label_results: "LabelResultList"
    service_rate: "ServiceRate"
    shipment_id: "ShipmentId"
    pass


@attrs.define
class Rate:

    expiration_time: str
    # {'schema_format': 'date-time'}
    rate_id: str

    billed_weight: "Weight"
    promise: "ShippingPromiseSet"
    service_type: "ServiceType"
    total_charge: "Currency"
    pass


@attrs.define
class RateId:

    pass


@attrs.define
class RateList:

    pass


@attrs.define
class RetrieveShippingLabelRequest:

    label_specification: "LabelSpecification"
    pass


@attrs.define
class RetrieveShippingLabelResponse:

    errors: "ErrorList"
    payload: "RetrieveShippingLabelResult"
    pass


@attrs.define
class RetrieveShippingLabelResult:

    label_specification: "LabelSpecification"
    label_stream: "LabelStream"
    pass


@attrs.define
class ServiceRate:

    billable_weight: "Weight"
    promise: "ShippingPromiseSet"
    service_type: "ServiceType"
    total_charge: "Currency"
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

    accepted_rate: "AcceptedRate"
    client_reference_id: "ClientReferenceId"
    containers: "ContainerList"
    ship_from: "Address"
    ship_to: "Address"
    shipment_id: "ShipmentId"
    shipper: "Party"
    pass


@attrs.define
class ShipmentId:

    pass


@attrs.define
class ShippingPromiseSet:

    delivery_window: "TimeRange"
    receive_window: "TimeRange"
    pass


@attrs.define
class StateOrRegion:

    pass


@attrs.define
class TimeRange:

    end: str
    # {'schema_format': 'date-time'}
    start: str
    # {'schema_format': 'date-time'}

    pass


@attrs.define
class TrackingId:

    pass


@attrs.define
class TrackingInformation:

    event_history: "EventList"
    promised_delivery_date: "PromisedDeliveryDate"
    summary: "TrackingSummary"
    tracking_id: "TrackingId"
    pass


@attrs.define
class TrackingSummary:

    status: str
    # {'maxLength': 60, 'minLength': 1}

    pass


@attrs.define
class Weight:

    unit: Union[Literal["g"], Literal["kg"], Literal["oz"], Literal["lb"]]
    value: Union[float, int]

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
