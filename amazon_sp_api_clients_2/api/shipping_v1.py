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

    billed_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    promise: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingPromiseSet', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    service_type: Union[
        Literal["Amazon Shipping Ground"], Literal["Amazon Shipping Standard"], Literal["Amazon Shipping Premium"]
    ]
    # {'ref': '#/components/schemas/ServiceType', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    total_charge: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class Account:

    account_id: str
    # {'ref': '#/components/schemas/AccountId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class AccountId:

    pass


@attrs.define
class Address:

    address_line1: str
    # {'maxLength': 60, 'minLength': 1, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    address_line2: str
    # {'maxLength': 60, 'minLength': 1, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    address_line3: str
    # {'maxLength': 60, 'minLength': 1, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    copy_emails: list[str]
    # {'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=64, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'array', 'maxItems': 2}
    email: str
    # {'maxLength': 64, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    name: str
    # {'maxLength': 50, 'minLength': 1, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    phone_number: str
    # {'maxLength': 20, 'minLength': 1, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    city: str
    # {'ref': '#/components/schemas/City', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    country_code: str
    # {'ref': '#/components/schemas/CountryCode', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    postal_code: str
    # {'ref': '#/components/schemas/PostalCode', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    state_or_region: str
    # {'ref': '#/components/schemas/StateOrRegion', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class CancelShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
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
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string', 'enum': ['PACKAGE']}
    items: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/ContainerItem'), 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'array'}

    container_reference_id: str
    # {'ref': '#/components/schemas/ContainerReferenceId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/Dimensions', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    value: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class ContainerItem:

    quantity: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'number'}
    title: str
    # {'maxLength': 30, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    unit_price: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    unit_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class ContainerList:

    pass


@attrs.define
class ContainerReferenceId:

    pass


@attrs.define
class ContainerSpecification:

    dimensions: dict[str, Any]
    # {'ref': '#/components/schemas/Dimensions', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class ContainerSpecificationList:

    pass


@attrs.define
class CountryCode:

    pass


@attrs.define
class CreateShipmentRequest:

    client_reference_id: str
    # {'ref': '#/components/schemas/ClientReferenceId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    containers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ContainerList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_from: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_to: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class CreateShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/CreateShipmentResult', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class CreateShipmentResult:

    eligible_rates: list[dict[str, Any]]
    # {'ref': '#/components/schemas/RateList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    shipment_id: str
    # {'ref': '#/components/schemas/ShipmentId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class Currency:

    unit: str
    # {'maxLength': 3, 'minLength': 3, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    value: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'number'}

    pass


@attrs.define
class Dimensions:

    height: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'number'}
    length: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'number'}
    unit: Union[Literal["IN"], Literal["CM"]]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string', 'enum': ['IN', 'CM']}
    width: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'number'}

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class Event:

    event_time: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    event_code: str
    # {'ref': '#/components/schemas/EventCode', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    location: dict[str, Any]
    # {'ref': '#/components/schemas/Location', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class EventCode:

    pass


@attrs.define
class EventList:

    pass


@attrs.define
class GetAccountResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Account', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class GetRatesRequest:

    ship_date: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    container_specifications: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ContainerSpecificationList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    service_types: list[
        Union[
            Literal["Amazon Shipping Ground"], Literal["Amazon Shipping Standard"], Literal["Amazon Shipping Premium"]
        ]
    ]
    # {'ref': '#/components/schemas/ServiceTypeList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_from: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_to: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class GetRatesResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/GetRatesResult', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class GetRatesResult:

    service_rates: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ServiceRateList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class GetShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/Shipment', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class GetTrackingInformationResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/TrackingInformation', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class Label:

    label_specification: dict[str, Any]
    # {'ref': '#/components/schemas/LabelSpecification', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    label_stream: str
    # {'ref': '#/components/schemas/LabelStream', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class LabelResult:

    tracking_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    container_reference_id: str
    # {'ref': '#/components/schemas/ContainerReferenceId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    label: dict[str, Any]
    # {'ref': '#/components/schemas/Label', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class LabelResultList:

    pass


@attrs.define
class LabelSpecification:

    label_format: Union[Literal["PNG"]]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string', 'enum': ['PNG']}
    label_stock_size: Union[Literal["4x6"]]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string', 'enum': ['4x6']}

    pass


@attrs.define
class LabelStream:

    pass


@attrs.define
class Location:

    city: str
    # {'ref': '#/components/schemas/City', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    country_code: str
    # {'ref': '#/components/schemas/CountryCode', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    postal_code: str
    # {'ref': '#/components/schemas/PostalCode', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    state_or_region: str
    # {'ref': '#/components/schemas/StateOrRegion', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class Party:

    account_id: str
    # {'ref': '#/components/schemas/AccountId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class PostalCode:

    pass


@attrs.define
class PromisedDeliveryDate:

    pass


@attrs.define
class PurchaseLabelsRequest:

    label_specification: dict[str, Any]
    # {'ref': '#/components/schemas/LabelSpecification', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    rate_id: str
    # {'ref': '#/components/schemas/RateId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class PurchaseLabelsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/PurchaseLabelsResult', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class PurchaseLabelsResult:

    accepted_rate: dict[str, Any]
    # {'ref': '#/components/schemas/AcceptedRate', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    client_reference_id: str
    # {'ref': '#/components/schemas/ClientReferenceId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    label_results: list[dict[str, Any]]
    # {'ref': '#/components/schemas/LabelResultList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    shipment_id: str
    # {'ref': '#/components/schemas/ShipmentId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class PurchaseShipmentRequest:

    ship_date: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    client_reference_id: str
    # {'ref': '#/components/schemas/ClientReferenceId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    containers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ContainerList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    label_specification: dict[str, Any]
    # {'ref': '#/components/schemas/LabelSpecification', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    service_type: Union[
        Literal["Amazon Shipping Ground"], Literal["Amazon Shipping Standard"], Literal["Amazon Shipping Premium"]
    ]
    # {'ref': '#/components/schemas/ServiceType', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_from: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_to: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class PurchaseShipmentResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/PurchaseShipmentResult', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class PurchaseShipmentResult:

    label_results: list[dict[str, Any]]
    # {'ref': '#/components/schemas/LabelResultList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    service_rate: dict[str, Any]
    # {'ref': '#/components/schemas/ServiceRate', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    shipment_id: str
    # {'ref': '#/components/schemas/ShipmentId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class Rate:

    expiration_time: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    rate_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    billed_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    promise: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingPromiseSet', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    service_type: Union[
        Literal["Amazon Shipping Ground"], Literal["Amazon Shipping Standard"], Literal["Amazon Shipping Premium"]
    ]
    # {'ref': '#/components/schemas/ServiceType', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    total_charge: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class RateId:

    pass


@attrs.define
class RateList:

    pass


@attrs.define
class RetrieveShippingLabelRequest:

    label_specification: dict[str, Any]
    # {'ref': '#/components/schemas/LabelSpecification', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class RetrieveShippingLabelResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/RetrieveShippingLabelResult', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class RetrieveShippingLabelResult:

    label_specification: dict[str, Any]
    # {'ref': '#/components/schemas/LabelSpecification', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    label_stream: str
    # {'ref': '#/components/schemas/LabelStream', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class ServiceRate:

    billable_weight: dict[str, Any]
    # {'ref': '#/components/schemas/Weight', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    promise: dict[str, Any]
    # {'ref': '#/components/schemas/ShippingPromiseSet', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    service_type: Union[
        Literal["Amazon Shipping Ground"], Literal["Amazon Shipping Standard"], Literal["Amazon Shipping Premium"]
    ]
    # {'ref': '#/components/schemas/ServiceType', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    total_charge: dict[str, Any]
    # {'ref': '#/components/schemas/Currency', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
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

    accepted_rate: dict[str, Any]
    # {'ref': '#/components/schemas/AcceptedRate', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    client_reference_id: str
    # {'ref': '#/components/schemas/ClientReferenceId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    containers: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ContainerList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_from: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    ship_to: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    shipment_id: str
    # {'ref': '#/components/schemas/ShipmentId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    shipper: dict[str, Any]
    # {'ref': '#/components/schemas/Party', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class ShipmentId:

    pass


@attrs.define
class ShippingPromiseSet:

    delivery_window: dict[str, Any]
    # {'ref': '#/components/schemas/TimeRange', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    receive_window: dict[str, Any]
    # {'ref': '#/components/schemas/TimeRange', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class StateOrRegion:

    pass


@attrs.define
class TimeRange:

    end: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}
    start: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    pass


@attrs.define
class TrackingId:

    pass


@attrs.define
class TrackingInformation:

    event_history: list[dict[str, Any]]
    # {'ref': '#/components/schemas/EventList', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    promised_delivery_date: str
    # {'ref': '#/components/schemas/PromisedDeliveryDate', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    summary: dict[str, Any]
    # {'ref': '#/components/schemas/TrackingSummary', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    tracking_id: str
    # {'ref': '#/components/schemas/TrackingId', 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>}
    pass


@attrs.define
class TrackingSummary:

    status: str
    # {'maxLength': 60, 'minLength': 1, 'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string'}

    pass


@attrs.define
class Weight:

    unit: Union[Literal["g"], Literal["kg"], Literal["oz"], Literal["lb"]]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'string', 'enum': ['g', 'kg', 'oz', 'lb']}
    value: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001F3D53DB310>, 'type': 'number'}

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
