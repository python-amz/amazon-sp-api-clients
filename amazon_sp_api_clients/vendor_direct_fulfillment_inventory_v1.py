from .base import BaseClient as __BaseClient
from typing import List as _List


class SubmitInventoryUpdateRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "inventory" in data:
            self.inventory: InventoryUpdate = InventoryUpdate(data["inventory"])
        else:
            self.inventory: InventoryUpdate = None


class InventoryUpdate:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "isFullUpdate" in data:
            self.isFullUpdate: bool = bool(data["isFullUpdate"])
        else:
            self.isFullUpdate: bool = None
        if "items" in data:
            self.items: _List[ItemDetails] = [ItemDetails(datum) for datum in data["items"]]
        else:
            self.items: _List[ItemDetails] = []


class ItemDetails:
    def __init__(self, data):
        super().__init__()
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
            self.isObsolete: bool = bool(data["isObsolete"])
        else:
            self.isObsolete: bool = None


class PartyIdentification:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "partyId" in data:
            self.partyId: str = str(data["partyId"])
        else:
            self.partyId: str = None


class ItemQuantity:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "amount" in data:
            self.amount: int = int(data["amount"])
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = str(data["unitOfMeasure"])
        else:
            self.unitOfMeasure: str = None


class SubmitInventoryUpdateResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: TransactionReference = TransactionReference(data["payload"])
        else:
            self.payload: TransactionReference = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class TransactionReference:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "transactionId" in data:
            self.transactionId: str = str(data["transactionId"])
        else:
            self.transactionId: str = None


class Error:
    def __init__(self, data):
        super().__init__()
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
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class VendorDirectFulfillmentInventoryV1Client(__BaseClient):
    def submitInventoryUpdate(
        self,
        data: SubmitInventoryUpdateRequest,
        warehouseId: str,
    ):
        url = "/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items".format(
            warehouseId=warehouseId,
        )
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            202: SubmitInventoryUpdateResponse,
            400: SubmitInventoryUpdateResponse,
            403: SubmitInventoryUpdateResponse,
            404: SubmitInventoryUpdateResponse,
            413: SubmitInventoryUpdateResponse,
            415: SubmitInventoryUpdateResponse,
            429: SubmitInventoryUpdateResponse,
            500: SubmitInventoryUpdateResponse,
            503: SubmitInventoryUpdateResponse,
        }[response.status_code](self.__get_response_json(response))
