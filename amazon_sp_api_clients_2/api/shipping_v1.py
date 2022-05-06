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
from datetime import date, datetime


@attrs.define
class AcceptedRate:

    billed_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promise: "ShippingPromiseSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_charge: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Account:

    account_id: "AccountId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AccountId:

    pass


@attrs.define
class Address:

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    First line of that address.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional address information, if required.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    copy_emails: List[str] = attrs.field(
        kw_only=True,
    )
    """
    The email cc addresses of the contact associated with the address.

    Extra fields:
    {'maxItems': 2}
    """

    email: str = attrs.field(
        kw_only=True,
    )
    """
    The email address of the contact associated with the address.

    Extra fields:
    {'maxLength': 64}
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the person, business or institution at that address.

    Extra fields:
    {'maxLength': 50, 'minLength': 1}
    """

    phone_number: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number of the person, business or institution located at that address.

    Extra fields:
    {'maxLength': 20, 'minLength': 1}
    """

    city: "City" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    country_code: "CountryCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    postal_code: "PostalCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    state_or_region: "StateOrRegion" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CancelShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class City:

    pass


@attrs.define
class ClientReferenceId:

    pass


@attrs.define
class Container:

    container_type: Union[Literal["PACKAGE"]] = attrs.field(
        kw_only=True,
    )
    """
    The type of physical container being used. (always 'PACKAGE')
    """

    items: List["ContainerItem"] = attrs.field(
        kw_only=True,
    )
    """
    A list of the items in the container.
    """

    container_reference_id: "ContainerReferenceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    dimensions: "Dimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    value: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContainerItem:

    quantity: float = attrs.field(
        kw_only=True,
    )
    """
    The quantity of the items of this type in the container.
    """

    title: str = attrs.field(
        kw_only=True,
    )
    """
    A descriptive title of the item.

    Extra fields:
    {'maxLength': 30}
    """

    unit_price: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    unit_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContainerList:

    pass


@attrs.define
class ContainerReferenceId:

    pass


@attrs.define
class ContainerSpecification:

    dimensions: "Dimensions" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ContainerSpecificationList:

    pass


@attrs.define
class CountryCode:

    pass


@attrs.define
class CreateShipmentRequest:

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    containers: "ContainerList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "CreateShipmentResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class CreateShipmentResult:

    eligible_rates: "RateList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Currency:

    unit: str = attrs.field(
        kw_only=True,
    )
    """
    A 3-character currency code.

    Extra fields:
    {'maxLength': 3, 'minLength': 3}
    """

    value: float = attrs.field(
        kw_only=True,
    )
    """
    The amount of currency.
    """

    pass


@attrs.define
class Dimensions:

    height: float = attrs.field(
        kw_only=True,
    )
    """
    The height of the container.
    """

    length: float = attrs.field(
        kw_only=True,
    )
    """
    The length of the container.
    """

    unit: Union[Literal["IN"], Literal["CM"]] = attrs.field(
        kw_only=True,
    )
    """
    The unit of these measurements.
    """

    width: float = attrs.field(
        kw_only=True,
    )
    """
    The width of the container.
    """

    pass


@attrs.define
class Error:

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

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class Event:

    event_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time of an event for a shipment.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    event_code: "EventCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    location: "Location" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class EventCode:

    pass


@attrs.define
class EventList:

    pass


@attrs.define
class GetAccountResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Account" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetRatesRequest:

    ship_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    container_specifications: "ContainerSpecificationList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_types: "ServiceTypeList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetRatesResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "GetRatesResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetRatesResult:

    service_rates: "ServiceRateList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetTrackingInformationResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "TrackingInformation" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Label:

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_stream: "LabelStream" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LabelResult:

    tracking_id: str = attrs.field(
        kw_only=True,
    )
    """
    The tracking identifier assigned to the container.
    """

    container_reference_id: "ContainerReferenceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label: "Label" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class LabelResultList:

    pass


@attrs.define
class LabelSpecification:

    label_format: Union[Literal["PNG"]] = attrs.field(
        kw_only=True,
    )
    """
    The format of the label. Enum of PNG only for now.
    """

    label_stock_size: Union[Literal["4x6"]] = attrs.field(
        kw_only=True,
    )
    """
    The label stock size specification in length and height. Enum of 4x6 only for now.
    """

    pass


@attrs.define
class LabelStream:

    pass


@attrs.define
class Location:

    city: "City" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    country_code: "CountryCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    postal_code: "PostalCode" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    state_or_region: "StateOrRegion" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Party:

    account_id: "AccountId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PostalCode:

    pass


@attrs.define
class PromisedDeliveryDate:

    pass


@attrs.define
class PurchaseLabelsRequest:

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    rate_id: "RateId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PurchaseLabelsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "PurchaseLabelsResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PurchaseLabelsResult:

    accepted_rate: "AcceptedRate" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_results: "LabelResultList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PurchaseShipmentRequest:

    ship_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    containers: "ContainerList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PurchaseShipmentResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "PurchaseShipmentResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PurchaseShipmentResult:

    label_results: "LabelResultList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_rate: "ServiceRate" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Rate:

    expiration_time: datetime = attrs.field(
        kw_only=True,
    )
    """
    The time after which the offering will expire.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    rate_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier for the rate.
    """

    billed_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promise: "ShippingPromiseSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_charge: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RateId:

    pass


@attrs.define
class RateList:

    pass


@attrs.define
class RetrieveShippingLabelRequest:

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RetrieveShippingLabelResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "RetrieveShippingLabelResult" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class RetrieveShippingLabelResult:

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    label_stream: "LabelStream" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ServiceRate:

    billable_weight: "Weight" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promise: "ShippingPromiseSet" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    total_charge: "Currency" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

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

    accepted_rate: "AcceptedRate" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    containers: "ContainerList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipper: "Party" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentId:

    pass


@attrs.define
class ShippingPromiseSet:

    delivery_window: "TimeRange" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    receive_window: "TimeRange" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class StateOrRegion:

    pass


@attrs.define
class TimeRange:

    end: datetime = attrs.field(
        kw_only=True,
    )
    """
    The end date and time. This must come after the value of start. This defaults to the next business day from the start.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    start: datetime = attrs.field(
        kw_only=True,
    )
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    pass


@attrs.define
class TrackingId:

    pass


@attrs.define
class TrackingInformation:

    event_history: "EventList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promised_delivery_date: "PromisedDeliveryDate" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    summary: "TrackingSummary" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    tracking_id: "TrackingId" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TrackingSummary:

    status: str = attrs.field(
        kw_only=True,
    )
    """
    The derived status based on the events in the eventHistory.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    pass


@attrs.define
class Weight:

    unit: Union[Literal["g"], Literal["kg"], Literal["oz"], Literal["lb"]] = attrs.field(
        kw_only=True,
    )
    """
    The unit of measurement.
    """

    value: float = attrs.field(
        kw_only=True,
    )
    """
    The measurement value.
    """

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
        client_reference_id: str,
        containers: List["Container"],
        ship_from: Dict[str, Any],
        ship_to: Dict[str, Any],
    ):
        """
        Create a new shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            client_reference_id: Client reference id.
            containers: A list of container.
            ship_from: The address.
            ship_to: The address.
        """
        url = "/shipping/v1/shipments"
        values = (
            client_reference_id,
            containers,
            ship_from,
            ship_to,
        )
        response = self._parse_args_and_request(url, "POST", values, self._create_shipment_params)
        return response

    _create_shipment_params = (  # name, param in
        ("clientReferenceId", "body"),
        ("containers", "body"),
        ("shipFrom", "body"),
        ("shipTo", "body"),
    )

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
        container_specifications: List["ContainerSpecification"],
        service_types: List["ServiceType"],
        ship_from: Dict[str, Any],
        ship_to: Dict[str, Any],
        ship_date: datetime = None,
    ):
        """
        Get service rates.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            container_specifications: A list of container specifications.
            service_types: A list of service types that can be used to send the shipment.
            ship_date: The start date and time. This defaults to the current date and time.
            ship_from: The address.
            ship_to: The address.
        """
        url = "/shipping/v1/rates"
        values = (
            container_specifications,
            service_types,
            ship_date,
            ship_from,
            ship_to,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_rates_params)
        return response

    _get_rates_params = (  # name, param in
        ("containerSpecifications", "body"),
        ("serviceTypes", "body"),
        ("shipDate", "body"),
        ("shipFrom", "body"),
        ("shipTo", "body"),
    )

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
        label_specification: Dict[str, Any],
        rate_id: str,
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
            label_specification: The label specification info.
            rate_id: An identifier for the rating.
        """
        url = "/shipping/v1/shipments/{shipmentId}/purchaseLabels"
        values = (
            shipment_id,
            label_specification,
            rate_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._purchase_labels_params)
        return response

    _purchase_labels_params = (  # name, param in
        ("shipmentId", "path"),
        ("labelSpecification", "body"),
        ("rateId", "body"),
    )

    def purchase_shipment(
        self,
        client_reference_id: str,
        containers: List["Container"],
        label_specification: Dict[str, Any],
        service_type: Union[
            Literal["Amazon Shipping Ground"], Literal["Amazon Shipping Standard"], Literal["Amazon Shipping Premium"]
        ],
        ship_from: Dict[str, Any],
        ship_to: Dict[str, Any],
        ship_date: datetime = None,
    ):
        """
        Purchase shipping labels.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            client_reference_id: Client reference id.
            containers: A list of container.
            label_specification: The label specification info.
            service_type: The type of shipping service that will be used for the service offering.
            ship_date: The start date and time. This defaults to the current date and time.
            ship_from: The address.
            ship_to: The address.
        """
        url = "/shipping/v1/purchaseShipment"
        values = (
            client_reference_id,
            containers,
            label_specification,
            service_type,
            ship_date,
            ship_from,
            ship_to,
        )
        response = self._parse_args_and_request(url, "POST", values, self._purchase_shipment_params)
        return response

    _purchase_shipment_params = (  # name, param in
        ("clientReferenceId", "body"),
        ("containers", "body"),
        ("labelSpecification", "body"),
        ("serviceType", "body"),
        ("shipDate", "body"),
        ("shipFrom", "body"),
        ("shipTo", "body"),
    )

    def retrieve_shipping_label(
        self,
        shipment_id: str,
        tracking_id: str,
        label_specification: Dict[str, Any],
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
