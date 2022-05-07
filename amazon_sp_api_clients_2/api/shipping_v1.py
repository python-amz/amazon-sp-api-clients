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
    """
    The weight.
    """

    promise: Optional["ShippingPromiseSet"] = attrs.field()
    """
    The promised delivery time and pickup time.
    """

    service_type: Optional["ServiceType"] = attrs.field()
    """
    The type of shipping service that will be used for the service offering.
    """

    total_charge: Optional["Currency"] = attrs.field()
    """
    The total value of all items in the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Account:
    """
    The account related data.
    """

    account_id: "AccountId" = attrs.field()
    """
    This is the Amazon Shipping account id generated during the Amazon Shipping onboarding process.
    """


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

    address_line1: str = attrs.field()
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

    city: "City" = attrs.field()
    """
    The city where the person, business or institution is located.
    """

    copy_emails: Optional[List[str]] = attrs.field()
    """
    The email cc addresses of the contact associated with the address.

    Extra fields:
    {'maxItems': 2}
    """

    country_code: "CountryCode" = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    email: Optional[str] = attrs.field()
    """
    The email address of the contact associated with the address.

    Extra fields:
    {'maxLength': 64}
    """

    name: str = attrs.field()
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

    postal_code: "PostalCode" = attrs.field()
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: "StateOrRegion" = attrs.field()
    """
    The state or region where the person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CancelShipmentResponse:
    """
    The response schema for the cancelShipment operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


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

    container_reference_id: "ContainerReferenceId" = attrs.field()
    """
    An identifier for the container. This must be unique within all the containers in the same shipment.
    """

    container_type: Optional[Union[Literal["PACKAGE"]]] = attrs.field()
    """
    The type of physical container being used. (always 'PACKAGE')
    """

    dimensions: "Dimensions" = attrs.field()
    """
    A set of measurements for a three-dimensional object.
    """

    items: List["ContainerItem"] = attrs.field()
    """
    A list of the items in the container.
    """

    value: "Currency" = attrs.field()
    """
    The total value of all items in the container.
    """

    weight: "Weight" = attrs.field()
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ContainerItem:
    """
    Item in the container.
    """

    quantity: float = attrs.field()
    """
    The quantity of the items of this type in the container.
    """

    title: str = attrs.field()
    """
    A descriptive title of the item.

    Extra fields:
    {'maxLength': 30}
    """

    unit_price: "Currency" = attrs.field()
    """
    The total value of all items in the container.
    """

    unit_weight: "Weight" = attrs.field()
    """
    The weight.
    """


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

    dimensions: "Dimensions" = attrs.field()
    """
    A set of measurements for a three-dimensional object.
    """

    weight: "Weight" = attrs.field()
    """
    The weight.
    """


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

    client_reference_id: "ClientReferenceId" = attrs.field()
    """
    Client reference id.
    """

    containers: List["Container"] = attrs.field()
    """
    A list of container.
    """

    ship_from: "Address" = attrs.field()
    """
    The address.
    """

    ship_to: "Address" = attrs.field()
    """
    The address.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentResponse:
    """
    The response schema for the createShipment operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateShipmentResult"] = attrs.field()
    """
    The payload schema for the createShipment operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateShipmentResult:
    """
    The payload schema for the createShipment operation.
    """

    eligible_rates: List["Rate"] = attrs.field()
    """
    A list of all the available rates that can be used to send the shipment.
    """

    shipment_id: "ShipmentId" = attrs.field()
    """
    The unique shipment identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Currency:
    """
    The total value of all items in the container.
    """

    unit: str = attrs.field()
    """
    A 3-character currency code.

    Extra fields:
    {'maxLength': 3, 'minLength': 3}
    """

    value: float = attrs.field()
    """
    The amount of currency.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Dimensions:
    """
    A set of measurements for a three-dimensional object.
    """

    height: float = attrs.field()
    """
    The height of the container.
    """

    length: float = attrs.field()
    """
    The length of the container.
    """

    unit: Union[Literal["IN"], Literal["CM"]] = attrs.field()
    """
    The unit of these measurements.
    """

    width: float = attrs.field()
    """
    The width of the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Event:
    """
    An event of a shipment
    """

    event_code: "EventCode" = attrs.field()
    """
    The event code of a shipment, such as Departed, Received, and ReadyForReceive.
    """

    event_time: datetime = attrs.field()
    """
    The date and time of an event for a shipment.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    location: Optional["Location"] = attrs.field()
    """
    The location where the person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class EventCode:
    """
    The event code of a shipment, such as Departed, Received, and ReadyForReceive.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetAccountResponse:
    """
    The response schema for the getAccount operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Account"] = attrs.field()
    """
    The account related data.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetRatesRequest:
    """
    The payload schema for the getRates operation.
    """

    container_specifications: List["ContainerSpecification"] = attrs.field()
    """
    A list of container specifications.
    """

    service_types: List["ServiceType"] = attrs.field()
    """
    A list of service types that can be used to send the shipment.
    """

    ship_date: Optional[datetime] = attrs.field()
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    ship_from: "Address" = attrs.field()
    """
    The address.
    """

    ship_to: "Address" = attrs.field()
    """
    The address.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetRatesResponse:
    """
    The response schema for the getRates operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetRatesResult"] = attrs.field()
    """
    The payload schema for the getRates operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetRatesResult:
    """
    The payload schema for the getRates operation.
    """

    service_rates: List["ServiceRate"] = attrs.field()
    """
    A list of service rates.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentResponse:
    """
    The response schema for the getShipment operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["Shipment"] = attrs.field()
    """
    The shipment related data.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetTrackingInformationResponse:
    """
    The response schema for the getTrackingInformation operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TrackingInformation"] = attrs.field()
    """
    The payload schema for the getTrackingInformation operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Label:
    """
    The label details of the container.
    """

    label_specification: Optional["LabelSpecification"] = attrs.field()
    """
    The label specification info.
    """

    label_stream: Optional["LabelStream"] = attrs.field()
    """
    Contains binary image data encoded as a base-64 string.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelResult:
    """
    Label details including label stream, format, size.
    """

    container_reference_id: Optional["ContainerReferenceId"] = attrs.field()
    """
    An identifier for the container. This must be unique within all the containers in the same shipment.
    """

    label: Optional["Label"] = attrs.field()
    """
    The label details of the container.
    """

    tracking_id: Optional[str] = attrs.field()
    """
    The tracking identifier assigned to the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelSpecification:
    """
    The label specification info.
    """

    label_format: Union[Literal["PNG"]] = attrs.field()
    """
    The format of the label. Enum of PNG only for now.
    """

    label_stock_size: Union[Literal["4x6"]] = attrs.field()
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
    """
    The city where the person, business or institution is located.
    """

    country_code: Optional["CountryCode"] = attrs.field()
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    postal_code: Optional["PostalCode"] = attrs.field()
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional["StateOrRegion"] = attrs.field()
    """
    The state or region where the person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Party:
    """
    The account related with the shipment.
    """

    account_id: Optional["AccountId"] = attrs.field()
    """
    This is the Amazon Shipping account id generated during the Amazon Shipping onboarding process.
    """


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

    label_specification: "LabelSpecification" = attrs.field()
    """
    The label specification info.
    """

    rate_id: "RateId" = attrs.field()
    """
    An identifier for the rating.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseLabelsResponse:
    """
    The response schema for the purchaseLabels operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["PurchaseLabelsResult"] = attrs.field()
    """
    The payload schema for the purchaseLabels operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseLabelsResult:
    """
    The payload schema for the purchaseLabels operation.
    """

    accepted_rate: "AcceptedRate" = attrs.field()
    """
    The specific rate purchased for the shipment, or null if unpurchased.
    """

    client_reference_id: Optional["ClientReferenceId"] = attrs.field()
    """
    Client reference id.
    """

    label_results: List["LabelResult"] = attrs.field()
    """
    A list of label results
    """

    shipment_id: "ShipmentId" = attrs.field()
    """
    The unique shipment identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseShipmentRequest:
    """
    The payload schema for the purchaseShipment operation.
    """

    client_reference_id: "ClientReferenceId" = attrs.field()
    """
    Client reference id.
    """

    containers: List["Container"] = attrs.field()
    """
    A list of container.
    """

    label_specification: "LabelSpecification" = attrs.field()
    """
    The label specification info.
    """

    service_type: "ServiceType" = attrs.field()
    """
    The type of shipping service that will be used for the service offering.
    """

    ship_date: Optional[datetime] = attrs.field()
    """
    The start date and time. This defaults to the current date and time.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    ship_from: "Address" = attrs.field()
    """
    The address.
    """

    ship_to: "Address" = attrs.field()
    """
    The address.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseShipmentResponse:
    """
    The response schema for the purchaseShipment operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["PurchaseShipmentResult"] = attrs.field()
    """
    The payload schema for the purchaseShipment operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PurchaseShipmentResult:
    """
    The payload schema for the purchaseShipment operation.
    """

    label_results: List["LabelResult"] = attrs.field()
    """
    A list of label results
    """

    service_rate: "ServiceRate" = attrs.field()
    """
    The specific rate for a shipping service, or null if no service available.
    """

    shipment_id: "ShipmentId" = attrs.field()
    """
    The unique shipment identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Rate:
    """
    The available rate that can be used to send the shipment
    """

    billed_weight: Optional["Weight"] = attrs.field()
    """
    The weight.
    """

    expiration_time: Optional[datetime] = attrs.field()
    """
    The time after which the offering will expire.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    promise: Optional["ShippingPromiseSet"] = attrs.field()
    """
    The promised delivery time and pickup time.
    """

    rate_id: Optional[str] = attrs.field()
    """
    An identifier for the rate.
    """

    service_type: Optional["ServiceType"] = attrs.field()
    """
    The type of shipping service that will be used for the service offering.
    """

    total_charge: Optional["Currency"] = attrs.field()
    """
    The total value of all items in the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RateId:
    """
    An identifier for the rating.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrieveShippingLabelRequest:
    """
    The request schema for the retrieveShippingLabel operation.
    """

    label_specification: "LabelSpecification" = attrs.field()
    """
    The label specification info.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrieveShippingLabelResponse:
    """
    The response schema for the retrieveShippingLabel operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["RetrieveShippingLabelResult"] = attrs.field()
    """
    The payload schema for the retrieveShippingLabel operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class RetrieveShippingLabelResult:
    """
    The payload schema for the retrieveShippingLabel operation.
    """

    label_specification: "LabelSpecification" = attrs.field()
    """
    The label specification info.
    """

    label_stream: "LabelStream" = attrs.field()
    """
    Contains binary image data encoded as a base-64 string.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceRate:
    """
    The specific rate for a shipping service, or null if no service available.
    """

    billable_weight: "Weight" = attrs.field()
    """
    The weight.
    """

    promise: "ShippingPromiseSet" = attrs.field()
    """
    The promised delivery time and pickup time.
    """

    service_type: "ServiceType" = attrs.field()
    """
    The type of shipping service that will be used for the service offering.
    """

    total_charge: "Currency" = attrs.field()
    """
    The total value of all items in the container.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ServiceType:
    """
    The type of shipping service that will be used for the service offering.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Shipment:
    """
    The shipment related data.
    """

    accepted_rate: Optional["AcceptedRate"] = attrs.field()
    """
    The specific rate purchased for the shipment, or null if unpurchased.
    """

    client_reference_id: "ClientReferenceId" = attrs.field()
    """
    Client reference id.
    """

    containers: List["Container"] = attrs.field()
    """
    A list of container.
    """

    ship_from: "Address" = attrs.field()
    """
    The address.
    """

    ship_to: "Address" = attrs.field()
    """
    The address.
    """

    shipment_id: "ShipmentId" = attrs.field()
    """
    The unique shipment identifier.
    """

    shipper: Optional["Party"] = attrs.field()
    """
    The account related with the shipment.
    """


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
    """
    The time range.
    """

    receive_window: Optional["TimeRange"] = attrs.field()
    """
    The time range.
    """


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

    event_history: List["Event"] = attrs.field()
    """
    A list of events of a shipment.
    """

    promised_delivery_date: "PromisedDeliveryDate" = attrs.field()
    """
    The promised delivery date and time of a shipment.
    """

    summary: "TrackingSummary" = attrs.field()
    """
    The tracking summary.
    """

    tracking_id: "TrackingId" = attrs.field()
    """
    The tracking id generated to each shipment. It contains a series of letters or digits or both.
    """


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

    unit: Union[Literal["g"], Literal["kg"], Literal["oz"], Literal["lb"]] = attrs.field()
    """
    The unit of measurement.
    """

    value: float = attrs.field()
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._cancel_shipment_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _cancel_shipment_params = (("shipmentId", "path"),)  # name, param in

    _cancel_shipment_responses = {
        200: CancelShipmentResponse,
        400: CancelShipmentResponse,
        401: CancelShipmentResponse,
        403: CancelShipmentResponse,
        404: CancelShipmentResponse,
        429: CancelShipmentResponse,
        500: CancelShipmentResponse,
        503: CancelShipmentResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_shipment_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _create_shipment_params = (  # name, param in
        ("clientReferenceId", "body"),
        ("containers", "body"),
        ("shipFrom", "body"),
        ("shipTo", "body"),
    )

    _create_shipment_responses = {
        200: CreateShipmentResponse,
        400: CreateShipmentResponse,
        401: CreateShipmentResponse,
        403: CreateShipmentResponse,
        404: CreateShipmentResponse,
        429: CreateShipmentResponse,
        500: CreateShipmentResponse,
        503: CreateShipmentResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_account_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_account_params = ()  # name, param in

    _get_account_responses = {
        200: GetAccountResponse,
        400: GetAccountResponse,
        401: GetAccountResponse,
        403: GetAccountResponse,
        404: GetAccountResponse,
        429: GetAccountResponse,
        500: GetAccountResponse,
        503: GetAccountResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_rates_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_rates_params = (  # name, param in
        ("containerSpecifications", "body"),
        ("serviceTypes", "body"),
        ("shipDate", "body"),
        ("shipFrom", "body"),
        ("shipTo", "body"),
    )

    _get_rates_responses = {
        200: GetRatesResponse,
        400: GetRatesResponse,
        401: GetRatesResponse,
        403: GetRatesResponse,
        404: GetRatesResponse,
        429: GetRatesResponse,
        500: GetRatesResponse,
        503: GetRatesResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipment_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_shipment_params = (("shipmentId", "path"),)  # name, param in

    _get_shipment_responses = {
        200: GetShipmentResponse,
        400: GetShipmentResponse,
        401: GetShipmentResponse,
        403: GetShipmentResponse,
        404: GetShipmentResponse,
        429: GetShipmentResponse,
        500: GetShipmentResponse,
        503: GetShipmentResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_tracking_information_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_tracking_information_params = (("trackingId", "path"),)  # name, param in

    _get_tracking_information_responses = {
        200: GetTrackingInformationResponse,
        400: GetTrackingInformationResponse,
        401: GetTrackingInformationResponse,
        403: GetTrackingInformationResponse,
        404: GetTrackingInformationResponse,
        429: GetTrackingInformationResponse,
        500: GetTrackingInformationResponse,
        503: GetTrackingInformationResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._purchase_labels_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _purchase_labels_params = (  # name, param in
        ("shipmentId", "path"),
        ("labelSpecification", "body"),
        ("rateId", "body"),
    )

    _purchase_labels_responses = {
        200: PurchaseLabelsResponse,
        400: PurchaseLabelsResponse,
        401: PurchaseLabelsResponse,
        403: PurchaseLabelsResponse,
        404: PurchaseLabelsResponse,
        429: PurchaseLabelsResponse,
        500: PurchaseLabelsResponse,
        503: PurchaseLabelsResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._purchase_shipment_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _purchase_shipment_params = (  # name, param in
        ("clientReferenceId", "body"),
        ("containers", "body"),
        ("labelSpecification", "body"),
        ("serviceType", "body"),
        ("shipDate", "body"),
        ("shipFrom", "body"),
        ("shipTo", "body"),
    )

    _purchase_shipment_responses = {
        200: PurchaseShipmentResponse,
        400: PurchaseShipmentResponse,
        401: PurchaseShipmentResponse,
        403: PurchaseShipmentResponse,
        404: PurchaseShipmentResponse,
        429: PurchaseShipmentResponse,
        500: PurchaseShipmentResponse,
        503: PurchaseShipmentResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._retrieve_shipping_label_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _retrieve_shipping_label_params = (  # name, param in
        ("shipmentId", "path"),
        ("trackingId", "path"),
        ("labelSpecification", "body"),
    )

    _retrieve_shipping_label_responses = {
        200: RetrieveShippingLabelResponse,
        400: RetrieveShippingLabelResponse,
        401: RetrieveShippingLabelResponse,
        403: RetrieveShippingLabelResponse,
        404: RetrieveShippingLabelResponse,
        429: RetrieveShippingLabelResponse,
        500: RetrieveShippingLabelResponse,
        503: RetrieveShippingLabelResponse,
    }
