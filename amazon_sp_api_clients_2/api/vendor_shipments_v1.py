"""
Selling Partner API for Retail Procurement Shipments
=============================================================================================

The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class SubmitShipmentConfirmationsRequest:
    pass


@attrs.define
class ShipmentConfirmation:
    pass


@attrs.define
class ShipmentMeasurements:
    pass


@attrs.define
class TransportationDetails:
    pass


@attrs.define
class ImportDetails:
    pass


@attrs.define
class Item:
    pass


@attrs.define
class Carton:
    pass


@attrs.define
class Pallet:
    pass


@attrs.define
class ItemDetails:
    pass


@attrs.define
class ContainerIdentification:
    pass


@attrs.define
class ContainerItem:
    pass


@attrs.define
class CartonReferenceDetails:
    pass


@attrs.define
class PartyIdentification:
    pass


@attrs.define
class TaxRegistrationDetails:
    pass


@attrs.define
class Address:
    pass


@attrs.define
class Route:
    pass


@attrs.define
class Stop:
    pass


@attrs.define
class Location:
    pass


@attrs.define
class Dimensions:
    pass


@attrs.define
class Volume:
    pass


@attrs.define
class Weight:
    pass


@attrs.define
class Money:
    pass


@attrs.define
class Decimal:
    pass


@attrs.define
class ItemQuantity:
    pass


@attrs.define
class Expiry:
    pass


@attrs.define
class Duration:
    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:
    pass


@attrs.define
class TransactionReference:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
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
