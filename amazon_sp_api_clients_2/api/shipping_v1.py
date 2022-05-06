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
    """
    The specific rate purchased for the shipment, or null if unpurchased.
    """

    billed_weight: "Weight" = attrs.field(
        kw_only=True,
    )

    promise: "ShippingPromiseSet" = attrs.field(
        kw_only=True,
    )

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )

    total_charge: "Currency" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Account:
    """
    The account related data.
    """

    account_id: "AccountId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class AccountId:
    """
    This is the Amazon Shipping account id generated during the Amazon Shipping onboarding process.
    """

    pass


@attrs.define
class Address:
    """
    The address.
    """

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

    country_code: "CountryCode" = attrs.field(
        kw_only=True,
    )

    postal_code: "PostalCode" = attrs.field(
        kw_only=True,
    )

    state_or_region: "StateOrRegion" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CancelShipmentResponse:
    """
    The response schema for the cancelShipment operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class City:
    """
    The city where the person, business or institution is located.
    """

    pass


@attrs.define
class ClientReferenceId:
    """
    Client reference id.
    """

    pass


@attrs.define
class Container:
    """
    Container in the shipment.
    """

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

    dimensions: "Dimensions" = attrs.field(
        kw_only=True,
    )

    value: "Currency" = attrs.field(
        kw_only=True,
    )

    weight: "Weight" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ContainerItem:
    """
    Item in the container.
    """

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

    unit_weight: "Weight" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ContainerList:
    """
    A list of container.
    """

    pass


@attrs.define
class ContainerReferenceId:
    """
    An identifier for the container. This must be unique within all the containers in the same shipment.
    """

    pass


@attrs.define
class ContainerSpecification:
    """
    Container specification for checking the service rate.
    """

    dimensions: "Dimensions" = attrs.field(
        kw_only=True,
    )

    weight: "Weight" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ContainerSpecificationList:
    """
    A list of container specifications.
    """

    pass


@attrs.define
class CountryCode:
    """
    The two digit country code. In ISO 3166-1 alpha-2 format.
    """

    pass


@attrs.define
class CreateShipmentRequest:
    """
    The request schema for the createShipment operation.
    """

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )

    containers: "ContainerList" = attrs.field(
        kw_only=True,
    )

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateShipmentResponse:
    """
    The response schema for the createShipment operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "CreateShipmentResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class CreateShipmentResult:
    """
    The payload schema for the createShipment operation.
    """

    eligible_rates: "RateList" = attrs.field(
        kw_only=True,
    )

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Currency:
    """
    The total value of all items in the container.
    """

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


@attrs.define
class Dimensions:
    """
    A set of measurements for a three-dimensional object.
    """

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


@attrs.define
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

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


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class Event:
    """
    An event of a shipment
    """

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

    location: "Location" = attrs.field(
        kw_only=True,
    )


@attrs.define
class EventCode:
    """
    The event code of a shipment, such as Departed, Received, and ReadyForReceive.
    """

    pass


@attrs.define
class EventList:
    """
    A list of events of a shipment.
    """

    pass


@attrs.define
class GetAccountResponse:
    """
    The response schema for the getAccount operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Account" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetRatesRequest:
    """
    The payload schema for the getRates operation.
    """

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

    service_types: "ServiceTypeList" = attrs.field(
        kw_only=True,
    )

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetRatesResponse:
    """
    The response schema for the getRates operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "GetRatesResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetRatesResult:
    """
    The payload schema for the getRates operation.
    """

    service_rates: "ServiceRateList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetShipmentResponse:
    """
    The response schema for the getShipment operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "Shipment" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetTrackingInformationResponse:
    """
    The response schema for the getTrackingInformation operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "TrackingInformation" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Label:
    """
    The label details of the container.
    """

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )

    label_stream: "LabelStream" = attrs.field(
        kw_only=True,
    )


@attrs.define
class LabelResult:
    """
    Label details including label stream, format, size.
    """

    tracking_id: str = attrs.field(
        kw_only=True,
    )
    """
    The tracking identifier assigned to the container.
    """

    container_reference_id: "ContainerReferenceId" = attrs.field(
        kw_only=True,
    )

    label: "Label" = attrs.field(
        kw_only=True,
    )


@attrs.define
class LabelResultList:
    """
    A list of label results
    """

    pass


@attrs.define
class LabelSpecification:
    """
    The label specification info.
    """

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


@attrs.define
class LabelStream:
    """
    Contains binary image data encoded as a base-64 string.
    """

    pass


@attrs.define
class Location:
    """
    The location where the person, business or institution is located.
    """

    city: "City" = attrs.field(
        kw_only=True,
    )

    country_code: "CountryCode" = attrs.field(
        kw_only=True,
    )

    postal_code: "PostalCode" = attrs.field(
        kw_only=True,
    )

    state_or_region: "StateOrRegion" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Party:
    """
    The account related with the shipment.
    """

    account_id: "AccountId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PostalCode:
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    pass


@attrs.define
class PromisedDeliveryDate:
    """
    The promised delivery date and time of a shipment.
    """

    pass


@attrs.define
class PurchaseLabelsRequest:
    """
    The request schema for the purchaseLabels operation.
    """

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )

    rate_id: "RateId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PurchaseLabelsResponse:
    """
    The response schema for the purchaseLabels operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "PurchaseLabelsResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PurchaseLabelsResult:
    """
    The payload schema for the purchaseLabels operation.
    """

    accepted_rate: "AcceptedRate" = attrs.field(
        kw_only=True,
    )

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )

    label_results: "LabelResultList" = attrs.field(
        kw_only=True,
    )

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PurchaseShipmentRequest:
    """
    The payload schema for the purchaseShipment operation.
    """

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

    containers: "ContainerList" = attrs.field(
        kw_only=True,
    )

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PurchaseShipmentResponse:
    """
    The response schema for the purchaseShipment operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "PurchaseShipmentResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class PurchaseShipmentResult:
    """
    The payload schema for the purchaseShipment operation.
    """

    label_results: "LabelResultList" = attrs.field(
        kw_only=True,
    )

    service_rate: "ServiceRate" = attrs.field(
        kw_only=True,
    )

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Rate:
    """
    The available rate that can be used to send the shipment
    """

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

    promise: "ShippingPromiseSet" = attrs.field(
        kw_only=True,
    )

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )

    total_charge: "Currency" = attrs.field(
        kw_only=True,
    )


@attrs.define
class RateId:
    """
    An identifier for the rating.
    """

    pass


@attrs.define
class RateList:
    """
    A list of all the available rates that can be used to send the shipment.
    """

    pass


@attrs.define
class RetrieveShippingLabelRequest:
    """
    The request schema for the retrieveShippingLabel operation.
    """

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )


@attrs.define
class RetrieveShippingLabelResponse:
    """
    The response schema for the retrieveShippingLabel operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "RetrieveShippingLabelResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class RetrieveShippingLabelResult:
    """
    The payload schema for the retrieveShippingLabel operation.
    """

    label_specification: "LabelSpecification" = attrs.field(
        kw_only=True,
    )

    label_stream: "LabelStream" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ServiceRate:
    """
    The specific rate for a shipping service, or null if no service available.
    """

    billable_weight: "Weight" = attrs.field(
        kw_only=True,
    )

    promise: "ShippingPromiseSet" = attrs.field(
        kw_only=True,
    )

    service_type: "ServiceType" = attrs.field(
        kw_only=True,
    )

    total_charge: "Currency" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ServiceRateList:
    """
    A list of service rates.
    """

    pass


@attrs.define
class ServiceType:
    """
    The type of shipping service that will be used for the service offering.
    """

    pass


@attrs.define
class ServiceTypeList:
    """
    A list of service types that can be used to send the shipment.
    """

    pass


@attrs.define
class Shipment:
    """
    The shipment related data.
    """

    accepted_rate: "AcceptedRate" = attrs.field(
        kw_only=True,
    )

    client_reference_id: "ClientReferenceId" = attrs.field(
        kw_only=True,
    )

    containers: "ContainerList" = attrs.field(
        kw_only=True,
    )

    ship_from: "Address" = attrs.field(
        kw_only=True,
    )

    ship_to: "Address" = attrs.field(
        kw_only=True,
    )

    shipment_id: "ShipmentId" = attrs.field(
        kw_only=True,
    )

    shipper: "Party" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ShipmentId:
    """
    The unique shipment identifier.
    """

    pass


@attrs.define
class ShippingPromiseSet:
    """
    The promised delivery time and pickup time.
    """

    delivery_window: "TimeRange" = attrs.field(
        kw_only=True,
    )

    receive_window: "TimeRange" = attrs.field(
        kw_only=True,
    )


@attrs.define
class StateOrRegion:
    """
    The state or region where the person, business or institution is located.
    """

    pass


@attrs.define
class TimeRange:
    """
    The time range.
    """

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


@attrs.define
class TrackingId:
    """
    The tracking id generated to each shipment. It contains a series of letters or digits or both.
    """

    pass


@attrs.define
class TrackingInformation:
    """
    The payload schema for the getTrackingInformation operation.
    """

    event_history: "EventList" = attrs.field(
        kw_only=True,
    )

    promised_delivery_date: "PromisedDeliveryDate" = attrs.field(
        kw_only=True,
    )

    summary: "TrackingSummary" = attrs.field(
        kw_only=True,
    )

    tracking_id: "TrackingId" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TrackingSummary:
    """
    The tracking summary.
    """

    status: str = attrs.field(
        kw_only=True,
    )
    """
    The derived status based on the events in the eventHistory.

    Extra fields:
    {'maxLength': 60, 'minLength': 1}
    """


@attrs.define
class Weight:
    """
    The weight.
    """

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
