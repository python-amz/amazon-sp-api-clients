"""
Selling Partner API for Retail Procurement Shipments
=============================================================================================

The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class SubmitShipmentConfirmationsRequest:
    pass


class ShipmentConfirmation:
    pass


class ShipmentMeasurements:
    pass


class TransportationDetails:
    pass


class ImportDetails:
    pass


class Item:
    pass


class Carton:
    pass


class Pallet:
    pass


class ItemDetails:
    pass


class ContainerIdentification:
    pass


class ContainerItem:
    pass


class CartonReferenceDetails:
    pass


class PartyIdentification:
    pass


class TaxRegistrationDetails:
    pass


class Address:
    pass


class Route:
    pass


class Stop:
    pass


class Location:
    pass


class Dimensions:
    pass


class Volume:
    pass


class Weight:
    pass


class Money:
    pass


class Decimal:
    pass


class ItemQuantity:
    pass


class Expiry:
    pass


class Duration:
    pass


class SubmitShipmentConfirmationsResponse:
    pass


class TransactionReference:
    pass


class ErrorList:
    pass


class Error:
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
