from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class SubmitInventoryUpdateRequest(__BaseDictObject):
    """
    The request body for the submitInventoryUpdate operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "inventory" in data:
            self.inventory: InventoryUpdate = self._get_value(InventoryUpdate, "inventory")
        else:
            self.inventory: InventoryUpdate = None


class InventoryUpdate(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "isFullUpdate" in data:
            self.isFullUpdate: bool = self._get_value(convert_bool, "isFullUpdate")
        else:
            self.isFullUpdate: bool = None
        if "items" in data:
            self.items: _List[ItemDetails] = [ItemDetails(datum) for datum in data["items"]]
        else:
            self.items: _List[ItemDetails] = []


class ItemDetails(__BaseDictObject):
    """
    Updated inventory details for an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = self._get_value(str, "buyerProductIdentifier")
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "availableQuantity" in data:
            self.availableQuantity: ItemQuantity = self._get_value(ItemQuantity, "availableQuantity")
        else:
            self.availableQuantity: ItemQuantity = None
        if "isObsolete" in data:
            self.isObsolete: bool = self._get_value(convert_bool, "isObsolete")
        else:
            self.isObsolete: bool = None


class PartyIdentification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "partyId" in data:
            self.partyId: str = self._get_value(str, "partyId")
        else:
            self.partyId: str = None


class ItemQuantity(__BaseDictObject):
    """
    Details of item quantity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "amount" in data:
            self.amount: int = self._get_value(int, "amount")
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None


class SubmitInventoryUpdateResponse(__BaseDictObject):
    """
    The response schema for the submitInventoryUpdate operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: TransactionReference = self._get_value(TransactionReference, "payload")
        else:
            self.payload: TransactionReference = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class TransactionReference(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "transactionId" in data:
            self.transactionId: str = self._get_value(str, "transactionId")
        else:
            self.transactionId: str = None


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
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
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
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
