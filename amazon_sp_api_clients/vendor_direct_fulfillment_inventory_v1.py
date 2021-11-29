from .base import BaseClient as __BaseClient, convert_bool, BaseObject as __BaseObject
from typing import List as _List


class SubmitInventoryUpdateRequest(__BaseObject):
    """
    The request body for the submitInventoryUpdate operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "inventory" in data:
            self.inventory: InventoryUpdate = InventoryUpdate(data["inventory"])
        else:
            self.inventory: InventoryUpdate = None


class InventoryUpdate(__BaseObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "isFullUpdate" in data:
            self.isFullUpdate: bool = convert_bool(data["isFullUpdate"])
        else:
            self.isFullUpdate: bool = None
        if "items" in data:
            self.items: _List[ItemDetails] = [ItemDetails(datum) for datum in data["items"]]
        else:
            self.items: _List[ItemDetails] = []


class ItemDetails(__BaseObject):
    """
    Updated inventory details for an item.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = str(data["buyerProductIdentifier"])
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "availableQuantity" in data:
            self.availableQuantity: ItemQuantity = ItemQuantity(data["availableQuantity"])
        else:
            self.availableQuantity: ItemQuantity = None
        if "isObsolete" in data:
            self.isObsolete: bool = convert_bool(data["isObsolete"])
        else:
            self.isObsolete: bool = None


class PartyIdentification(__BaseObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "partyId" in data:
            self.partyId: str = str(data["partyId"])
        else:
            self.partyId: str = None


class ItemQuantity(__BaseObject):
    """
    Details of item quantity.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "amount" in data:
            self.amount: int = int(data["amount"])
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = str(data["unitOfMeasure"])
        else:
            self.unitOfMeasure: str = None


class SubmitInventoryUpdateResponse(__BaseObject):
    """
    The response schema for the submitInventoryUpdate operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "payload" in data:
            self.payload: TransactionReference = TransactionReference(data["payload"])
        else:
            self.payload: TransactionReference = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class TransactionReference(__BaseObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "transactionId" in data:
            self.transactionId: str = str(data["transactionId"])
        else:
            self.transactionId: str = None


class Error(__BaseObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
        else:
            self.details: str = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class VendorDirectFulfillmentInventoryV1Client(__BaseClient):
    def submitInventoryUpdate(
        self,
        data: SubmitInventoryUpdateRequest,
        warehouseId: str,
    ):
        """
                Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: SubmitInventoryUpdateResponse,
            400: SubmitInventoryUpdateResponse,
            403: SubmitInventoryUpdateResponse,
            404: SubmitInventoryUpdateResponse,
            413: SubmitInventoryUpdateResponse,
            415: SubmitInventoryUpdateResponse,
            429: SubmitInventoryUpdateResponse,
            500: SubmitInventoryUpdateResponse,
            503: SubmitInventoryUpdateResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
