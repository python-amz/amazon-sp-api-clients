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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class AcceptedRate:
    """
    The specific rate purchased for the shipment, or null if unpurchased.
    """

    billed_weight: Optional["Weight"] = attrs.field()

    promise: Optional["ShippingPromiseSet"] = attrs.field()

    service_type: Optional["ServiceType"] = attrs.field()

    total_charge: Optional["Currency"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Account:
    """
    The account related data.
    """

    account_id: Optional["AccountId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class AccountId:
    """
    This is the Amazon Shipping account id generated during the Amazon Shipping onboarding process.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    The address.
    """

    address_line1: Optional[str] = attrs.field()
    """
    First line of that address.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional address information, if required.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional address information, if required.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """

    city: Optional["City"] = attrs.field()

    copy_emails: Optional[List[str]] = attrs.field()
    """
    The email cc addresses of the contact associated with the address.

    Extra fields:
    {'maxItems': 2}
    """

    country_code: Optional["CountryCode"] = attrs.field()

    email: Optional[str] = attrs.field()
    """
    The email address of the contact associated with the address.

    Extra fields:
    {'maxLength': 64}
    """

    name: Optional[str] = attrs.field()
    """
    The name of the person, business or institution at that address.

    Extra fields:
    {'maxLength': 50, 'minLength': 1}
    """

    phone_number: Optional[str] = attrs.field()
    """
    The phone number of the person, business or institution located at that address.

    Extra fields:
    {'maxLength': 20, 'minLength': 1}
    """

    postal_code: Optional["PostalCode"] = attrs.field()

    state_or_region: Optional["StateOrRegion"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelShipmentResponse:
    """
    The response schema for the cancelShipment operation.
    """

    errors: Optional["ErrorList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class City:
    """
    The city where the person, business or institution is located.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ClientReferenceId:
    """
    Client reference id.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Container:
    """
    Container in the shipment.
    """

    container_reference_id: Optional["ContainerReferenceId"] = attrs.field()

    container_type: Optional[Union[Literal["PACKAGE"]]] = attrs.field()
    """
    The type of physical container being used. (always 'PACKAGE')
    """

    dimensions: Optional["Dimensions"] = attrs.field()

    items: Optional[List["ContainerItem"]] = attrs.field()
    """
    A list of the items in the container.
    """

    value: Optional["Currency"] = attrs.field()

    weight: Optional["Weight"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerItem:
    """
    Item in the container.
    """

    quantity: Optional[float] = attrs.field()
    """
    The quantity of the items of this type in the container.
    """

    title: Optional[str] = attrs.field()
    """
    A descriptive title of the item.

    Extra fields:
    {'maxLength': 30}
    """

    unit_price: Optional["Currency"] = attrs.field()

    unit_weight: Optional["Weight"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerList:
    """
    A list of container.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerReferenceId:
    """
    An identifier for the container. This must be unique within all the containers in the same shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerSpecification:
    """
    Container specification for checking the service rate.
    """

    dimensions: Optional["Dimensions"] = attrs.field()

    weight: Optional["Weight"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerSpecificationList:
    """
    A list of container specifications.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CountryCode:
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentRequest:
    """
    The request schema for the createShipment operation.
    """

    client_reference_id: Optional["ClientReferenceId"] = attrs.field()

    containers: Optional["ContainerList"] = attrs.field()

    ship_from: Optional["Address"] = attrs.field()

    ship_to: Optional["Address"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentResponse:
    """
    The response schema for the createShipment operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["CreateShipmentResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentResult:
    """
    The payload schema for the createShipment operation.
    """

    eligible_rates: Optional["RateList"] = attrs.field()

    shipment_id: Optional["ShipmentId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Currency:
    """
    The total value of all items in the container.
    """

    unit: Optional[str] = attrs.field()
    """
    A 3-character currency code.

    Extra fields:
    {'maxLength': 3, 'minLength': 3}
    """

    value: Optional[float] = attrs.field()
    """
    The amount of currency.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Dimensions:
    """
    A set of measurements for a three-dimensional object.
    """

    height: Optional[float] = attrs.field()
    """
    The height of the container.
    """

    length: Optional[float] = attrs.field()
    """
    The length of the container.
    """

    unit: Optional[Union[Literal["IN"], Literal["CM"]]] = attrs.field()
    """
    The unit of these measurements.
    """

    width: Optional[float] = attrs.field()
    """
    The width of the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: Optional[str] = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Event:
    """
    An event of a shipment
    """

    event_code: Optional["EventCode"] = attrs.field()

    event_time: Optional[datetime] = attrs.field()
    """
    The date and time of an event for a shipment.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    location: Optional["Location"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class EventCode:
    """
    The event code of a shipment, such as Departed, Received, and ReadyForReceive.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class EventList:
    """
    A list of events of a shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAccountResponse:
    """
    The response schema for the getAccount operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["Account"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetRatesRequest:
    """
    The payload schema for the getRates operation.
    """

    container_specifications: Optional["ContainerSpecificationList"] = attrs.field()

    service_types: Optional["ServiceTypeList"] = attrs.field()

    ship_date: Optional[datetime] = attrs.field()
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    ship_from: Optional["Address"] = attrs.field()

    ship_to: Optional["Address"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetRatesResponse:
    """
    The response schema for the getRates operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["GetRatesResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetRatesResult:
    """
    The payload schema for the getRates operation.
    """

    service_rates: Optional["ServiceRateList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentResponse:
    """
    The response schema for the getShipment operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["Shipment"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetTrackingInformationResponse:
    """
    The response schema for the getTrackingInformation operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["TrackingInformation"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Label:
    """
    The label details of the container.
    """

    label_specification: Optional["LabelSpecification"] = attrs.field()

    label_stream: Optional["LabelStream"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelResult:
    """
    Label details including label stream, format, size.
    """

    container_reference_id: Optional["ContainerReferenceId"] = attrs.field()

    label: Optional["Label"] = attrs.field()

    tracking_id: Optional[str] = attrs.field()
    """
    The tracking identifier assigned to the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelResultList:
    """
    A list of label results
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelSpecification:
    """
    The label specification info.
    """

    label_format: Optional[Union[Literal["PNG"]]] = attrs.field()
    """
    The format of the label. Enum of PNG only for now.
    """

    label_stock_size: Optional[Union[Literal["4x6"]]] = attrs.field()
    """
    The label stock size specification in length and height. Enum of 4x6 only for now.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelStream:
    """
    Contains binary image data encoded as a base-64 string.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Location:
    """
    The location where the person, business or institution is located.
    """

    city: Optional["City"] = attrs.field()

    country_code: Optional["CountryCode"] = attrs.field()

    postal_code: Optional["PostalCode"] = attrs.field()

    state_or_region: Optional["StateOrRegion"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Party:
    """
    The account related with the shipment.
    """

    account_id: Optional["AccountId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PostalCode:
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PromisedDeliveryDate:
    """
    The promised delivery date and time of a shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseLabelsRequest:
    """
    The request schema for the purchaseLabels operation.
    """

    label_specification: Optional["LabelSpecification"] = attrs.field()

    rate_id: Optional["RateId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseLabelsResponse:
    """
    The response schema for the purchaseLabels operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["PurchaseLabelsResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseLabelsResult:
    """
    The payload schema for the purchaseLabels operation.
    """

    accepted_rate: Optional["AcceptedRate"] = attrs.field()

    client_reference_id: Optional["ClientReferenceId"] = attrs.field()

    label_results: Optional["LabelResultList"] = attrs.field()

    shipment_id: Optional["ShipmentId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseShipmentRequest:
    """
    The payload schema for the purchaseShipment operation.
    """

    client_reference_id: Optional["ClientReferenceId"] = attrs.field()

    containers: Optional["ContainerList"] = attrs.field()

    label_specification: Optional["LabelSpecification"] = attrs.field()

    service_type: Optional["ServiceType"] = attrs.field()

    ship_date: Optional[datetime] = attrs.field()
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    ship_from: Optional["Address"] = attrs.field()

    ship_to: Optional["Address"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseShipmentResponse:
    """
    The response schema for the purchaseShipment operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["PurchaseShipmentResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseShipmentResult:
    """
    The payload schema for the purchaseShipment operation.
    """

    label_results: Optional["LabelResultList"] = attrs.field()

    service_rate: Optional["ServiceRate"] = attrs.field()

    shipment_id: Optional["ShipmentId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Rate:
    """
    The available rate that can be used to send the shipment
    """

    billed_weight: Optional["Weight"] = attrs.field()

    expiration_time: Optional[datetime] = attrs.field()
    """
    The time after which the offering will expire.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    promise: Optional["ShippingPromiseSet"] = attrs.field()

    rate_id: Optional[str] = attrs.field()
    """
    An identifier for the rate.
    """

    service_type: Optional["ServiceType"] = attrs.field()

    total_charge: Optional["Currency"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class RateId:
    """
    An identifier for the rating.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RateList:
    """
    A list of all the available rates that can be used to send the shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrieveShippingLabelRequest:
    """
    The request schema for the retrieveShippingLabel operation.
    """

    label_specification: Optional["LabelSpecification"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrieveShippingLabelResponse:
    """
    The response schema for the retrieveShippingLabel operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["RetrieveShippingLabelResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrieveShippingLabelResult:
    """
    The payload schema for the retrieveShippingLabel operation.
    """

    label_specification: Optional["LabelSpecification"] = attrs.field()

    label_stream: Optional["LabelStream"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceRate:
    """
    The specific rate for a shipping service, or null if no service available.
    """

    billable_weight: Optional["Weight"] = attrs.field()

    promise: Optional["ShippingPromiseSet"] = attrs.field()

    service_type: Optional["ServiceType"] = attrs.field()

    total_charge: Optional["Currency"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceRateList:
    """
    A list of service rates.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceType:
    """
    The type of shipping service that will be used for the service offering.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceTypeList:
    """
    A list of service types that can be used to send the shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Shipment:
    """
    The shipment related data.
    """

    accepted_rate: Optional["AcceptedRate"] = attrs.field()

    client_reference_id: Optional["ClientReferenceId"] = attrs.field()

    containers: Optional["ContainerList"] = attrs.field()

    ship_from: Optional["Address"] = attrs.field()

    ship_to: Optional["Address"] = attrs.field()

    shipment_id: Optional["ShipmentId"] = attrs.field()

    shipper: Optional["Party"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentId:
    """
    The unique shipment identifier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingPromiseSet:
    """
    The promised delivery time and pickup time.
    """

    delivery_window: Optional["TimeRange"] = attrs.field()

    receive_window: Optional["TimeRange"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class StateOrRegion:
    """
    The state or region where the person, business or institution is located.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TimeRange:
    """
    The time range.
    """

    end: Optional[datetime] = attrs.field()
    """
    The end date and time. This must come after the value of start. This defaults to the next business day from the start.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    start: Optional[datetime] = attrs.field()
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingId:
    """
    The tracking id generated to each shipment. It contains a series of letters or digits or both.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingInformation:
    """
    The payload schema for the getTrackingInformation operation.
    """

    event_history: Optional["EventList"] = attrs.field()

    promised_delivery_date: Optional["PromisedDeliveryDate"] = attrs.field()

    summary: Optional["TrackingSummary"] = attrs.field()

    tracking_id: Optional["TrackingId"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingSummary:
    """
    The tracking summary.
    """

    status: Optional[str] = attrs.field()
    """
    The derived status based on the events in the eventHistory.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight.
    """

    unit: Optional[Union[Literal["g"], Literal["kg"], Literal["oz"], Literal["lb"]]] = attrs.field()
    """
    The unit of measurement.
    """

    value: Optional[float] = attrs.field()
    """
    The measurement value.
    """


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
