"""
Selling Partner API for Retail Procurement Shipments
=============================================================================================

The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class Address:
    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class Carton:
    carton_identifiers: list["ContainerIdentification"] = attrs.field()
    carton_sequence_number: str = attrs.field()
    items: list["ContainerItem"] = attrs.field()
    tracking_number: str = attrs.field()

    dimensions: "Dimensions" = attrs.field()
    weight: "Weight" = attrs.field()
    pass


@attrs.define
class CartonReferenceDetails:
    carton_count: int = attrs.field()
    carton_reference_numbers: list[str] = attrs.field()

    pass


@attrs.define
class ContainerIdentification:
    container_identification_number: str = attrs.field()
    container_identification_type: Union[
        Literal["SSCC"], Literal["AMZNCC"], Literal["GTIN"], Literal["BPS"], Literal["CID"]
    ] = attrs.field()

    pass


@attrs.define
class ContainerItem:
    item_reference: str = attrs.field()

    item_details: "ItemDetails" = attrs.field()
    shipped_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class Decimal:
    pass


@attrs.define
class Dimensions:
    unit_of_measure: Union[Literal["In"], Literal["Ft"], Literal["Meter"], Literal["Yard"]] = attrs.field()

    height: "Decimal" = attrs.field()
    length: "Decimal" = attrs.field()
    width: "Decimal" = attrs.field()
    pass


@attrs.define
class Duration:
    duration_unit: Union[Literal["Days"], Literal["Months"]] = attrs.field()
    duration_value: int = attrs.field()

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
class Expiry:
    expiry_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    manufacturer_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    expiry_after_duration: "Duration" = attrs.field()
    pass


@attrs.define
class ImportDetails:
    estimated_ship_by_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    import_containers: str = attrs.field()
    # {'maxLength': 64}
    method_of_payment: Union[
        Literal["PaidByBuyer"],
        Literal["CollectOnDelivery"],
        Literal["DefinedByBuyerAndSeller"],
        Literal["FOBPortOfCall"],
        Literal["PrepaidBySeller"],
        Literal["PaidBySeller"],
    ] = attrs.field()
    seal_number: str = attrs.field()

    billable_weight: "Weight" = attrs.field()
    route: "Route" = attrs.field()
    pass


@attrs.define
class Item:
    amazon_product_identifier: str = attrs.field()
    item_sequence_number: str = attrs.field()
    vendor_product_identifier: str = attrs.field()

    item_details: "ItemDetails" = attrs.field()
    shipped_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class ItemDetails:
    handling_code: Union[
        Literal["Oversized"], Literal["Fragile"], Literal["Food"], Literal["HandleWithCare"]
    ] = attrs.field()
    lot_number: str = attrs.field()
    purchase_order_number: str = attrs.field()

    expiry: "Expiry" = attrs.field()
    maximum_retail_price: "Money" = attrs.field()
    pass


@attrs.define
class ItemQuantity:
    amount: int = attrs.field()
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field()
    unit_size: int = attrs.field()

    pass


@attrs.define
class Location:
    country_code: str = attrs.field()
    location_code: str = attrs.field()
    type: str = attrs.field()

    pass


@attrs.define
class Money:
    currency_code: str = attrs.field()

    amount: "Decimal" = attrs.field()
    pass


@attrs.define
class Pallet:
    block: int = attrs.field()
    items: list["ContainerItem"] = attrs.field()
    pallet_identifiers: list["ContainerIdentification"] = attrs.field()
    tier: int = attrs.field()

    carton_reference_details: "CartonReferenceDetails" = attrs.field()
    dimensions: "Dimensions" = attrs.field()
    weight: "Weight" = attrs.field()
    pass


@attrs.define
class PartyIdentification:
    party_id: str = attrs.field()
    tax_registration_details: list["TaxRegistrationDetails"] = attrs.field()

    address: "Address" = attrs.field()
    pass


@attrs.define
class Route:
    stops: list["Stop"] = attrs.field()

    pass


@attrs.define
class ShipmentConfirmation:
    amazon_reference_number: str = attrs.field()
    cartons: list["Carton"] = attrs.field()
    estimated_delivery_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    pallets: list["Pallet"] = attrs.field()
    shipment_confirmation_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    shipment_confirmation_type: Union[Literal["Original"], Literal["Replace"]] = attrs.field()
    shipment_identifier: str = attrs.field()
    shipment_structure: Union[
        Literal["PalletizedAssortmentCase"],
        Literal["LooseAssortmentCase"],
        Literal["PalletOfItems"],
        Literal["PalletizedStandardCase"],
        Literal["LooseStandardCase"],
        Literal["MasterPallet"],
        Literal["MasterCase"],
    ] = attrs.field()
    shipment_type: Union[Literal["TruckLoad"], Literal["LessThanTruckLoad"], Literal["SmallParcel"]] = attrs.field()
    shipped_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    shipped_items: list["Item"] = attrs.field()

    import_details: "ImportDetails" = attrs.field()
    selling_party: "PartyIdentification" = attrs.field()
    ship_from_party: "PartyIdentification" = attrs.field()
    ship_to_party: "PartyIdentification" = attrs.field()
    shipment_measurements: "ShipmentMeasurements" = attrs.field()
    transportation_details: "TransportationDetails" = attrs.field()
    pass


@attrs.define
class ShipmentMeasurements:
    carton_count: int = attrs.field()
    pallet_count: int = attrs.field()

    gross_shipment_weight: "Weight" = attrs.field()
    shipment_volume: "Volume" = attrs.field()
    pass


@attrs.define
class Stop:
    arrival_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    departure_time: str = attrs.field()
    # {'schema_format': 'date-time'}
    function_code: Union[
        Literal["PortOfDischarge"], Literal["FreightPayableAt"], Literal["PortOfLoading"]
    ] = attrs.field()

    location_identification: "Location" = attrs.field()
    pass


@attrs.define
class SubmitShipmentConfirmationsRequest:
    shipment_confirmations: list["ShipmentConfirmation"] = attrs.field()

    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:
    errors: "ErrorList" = attrs.field()
    payload: "TransactionReference" = attrs.field()
    pass


@attrs.define
class TaxRegistrationDetails:
    tax_registration_number: str = attrs.field()
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()

    pass


@attrs.define
class TransactionReference:
    transaction_id: str = attrs.field()

    pass


@attrs.define
class TransportationDetails:
    bill_of_lading_number: str = attrs.field()
    carrier_scac: str = attrs.field()
    carrier_shipment_reference_number: str = attrs.field()
    transportation_mode: Union[Literal["Road"], Literal["Air"], Literal["Ocean"]] = attrs.field()

    pass


@attrs.define
class Volume:
    unit_of_measure: Union[Literal["CuFt"], Literal["CuIn"], Literal["CuM"], Literal["CuY"]] = attrs.field()

    value: "Decimal" = attrs.field()
    pass


@attrs.define
class Weight:
    unit_of_measure: Union[Literal["G"], Literal["Kg"], Literal["Oz"], Literal["Lb"]] = attrs.field()

    value: "Decimal" = attrs.field()
    pass


class VendorShipmentsV1Client(BaseClient):
    def submit_shipment_confirmations(
            self,
    ):
        """
        Submits one or more shipment confirmations for vendor orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/shipping/v1/shipmentConfirmations"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipment_confirmations_params)
        return response

    _submit_shipment_confirmations_params = ()  # name, param in
