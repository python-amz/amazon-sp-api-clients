from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetOrdersResponse(__BaseDictObject):
    """
    The response schema for the getOrders operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrdersList = self._get_value(OrdersList, "payload")
        else:
            self.payload: OrdersList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderResponse(__BaseDictObject):
    """
    The response schema for the getOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Order = self._get_value(Order, "payload")
        else:
            self.payload: Order = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderBuyerInfoResponse(__BaseDictObject):
    """
    The response schema for the getOrderBuyerInfo operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderBuyerInfo = self._get_value(OrderBuyerInfo, "payload")
        else:
            self.payload: OrderBuyerInfo = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderAddressResponse(__BaseDictObject):
    """
    The response schema for the getOrderAddress operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderAddress = self._get_value(OrderAddress, "payload")
        else:
            self.payload: OrderAddress = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderItemsResponse(__BaseDictObject):
    """
    The response schema for the getOrderItems operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderItemsList = self._get_value(OrderItemsList, "payload")
        else:
            self.payload: OrderItemsList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetOrderItemsBuyerInfoResponse(__BaseDictObject):
    """
    The response schema for the getOrderItemsBuyerInfo operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderItemsBuyerInfoList = self._get_value(OrderItemsBuyerInfoList, "payload")
        else:
            self.payload: OrderItemsBuyerInfoList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class OrdersList(__BaseDictObject):
    """
    A list of orders along with additional information to make subsequent API calls.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Orders" in data:
            self.Orders: OrderList = self._get_value(OrderList, "Orders")
        else:
            self.Orders: OrderList = None
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "LastUpdatedBefore" in data:
            self.LastUpdatedBefore: str = self._get_value(str, "LastUpdatedBefore")
        else:
            self.LastUpdatedBefore: str = None
        if "CreatedBefore" in data:
            self.CreatedBefore: str = self._get_value(str, "CreatedBefore")
        else:
            self.CreatedBefore: str = None


class Order(__BaseDictObject):
    """
    Order information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "SellerOrderId" in data:
            self.SellerOrderId: str = self._get_value(str, "SellerOrderId")
        else:
            self.SellerOrderId: str = None
        if "PurchaseDate" in data:
            self.PurchaseDate: str = self._get_value(str, "PurchaseDate")
        else:
            self.PurchaseDate: str = None
        if "LastUpdateDate" in data:
            self.LastUpdateDate: str = self._get_value(str, "LastUpdateDate")
        else:
            self.LastUpdateDate: str = None
        if "OrderStatus" in data:
            self.OrderStatus: str = self._get_value(str, "OrderStatus")
        else:
            self.OrderStatus: str = None
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = self._get_value(str, "FulfillmentChannel")
        else:
            self.FulfillmentChannel: str = None
        if "SalesChannel" in data:
            self.SalesChannel: str = self._get_value(str, "SalesChannel")
        else:
            self.SalesChannel: str = None
        if "OrderChannel" in data:
            self.OrderChannel: str = self._get_value(str, "OrderChannel")
        else:
            self.OrderChannel: str = None
        if "ShipServiceLevel" in data:
            self.ShipServiceLevel: str = self._get_value(str, "ShipServiceLevel")
        else:
            self.ShipServiceLevel: str = None
        if "OrderTotal" in data:
            self.OrderTotal: Money = self._get_value(Money, "OrderTotal")
        else:
            self.OrderTotal: Money = None
        if "NumberOfItemsShipped" in data:
            self.NumberOfItemsShipped: int = self._get_value(int, "NumberOfItemsShipped")
        else:
            self.NumberOfItemsShipped: int = None
        if "NumberOfItemsUnshipped" in data:
            self.NumberOfItemsUnshipped: int = self._get_value(int, "NumberOfItemsUnshipped")
        else:
            self.NumberOfItemsUnshipped: int = None
        if "PaymentExecutionDetail" in data:
            self.PaymentExecutionDetail: PaymentExecutionDetailItemList = self._get_value(
                PaymentExecutionDetailItemList, "PaymentExecutionDetail"
            )
        else:
            self.PaymentExecutionDetail: PaymentExecutionDetailItemList = None
        if "PaymentMethod" in data:
            self.PaymentMethod: str = self._get_value(str, "PaymentMethod")
        else:
            self.PaymentMethod: str = None
        if "PaymentMethodDetails" in data:
            self.PaymentMethodDetails: PaymentMethodDetailItemList = self._get_value(
                PaymentMethodDetailItemList, "PaymentMethodDetails"
            )
        else:
            self.PaymentMethodDetails: PaymentMethodDetailItemList = None
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "ShipmentServiceLevelCategory" in data:
            self.ShipmentServiceLevelCategory: str = self._get_value(str, "ShipmentServiceLevelCategory")
        else:
            self.ShipmentServiceLevelCategory: str = None
        if "EasyShipShipmentStatus" in data:
            self.EasyShipShipmentStatus: str = self._get_value(str, "EasyShipShipmentStatus")
        else:
            self.EasyShipShipmentStatus: str = None
        if "CbaDisplayableShippingLabel" in data:
            self.CbaDisplayableShippingLabel: str = self._get_value(str, "CbaDisplayableShippingLabel")
        else:
            self.CbaDisplayableShippingLabel: str = None
        if "OrderType" in data:
            self.OrderType: str = self._get_value(str, "OrderType")
        else:
            self.OrderType: str = None
        if "EarliestShipDate" in data:
            self.EarliestShipDate: str = self._get_value(str, "EarliestShipDate")
        else:
            self.EarliestShipDate: str = None
        if "LatestShipDate" in data:
            self.LatestShipDate: str = self._get_value(str, "LatestShipDate")
        else:
            self.LatestShipDate: str = None
        if "EarliestDeliveryDate" in data:
            self.EarliestDeliveryDate: str = self._get_value(str, "EarliestDeliveryDate")
        else:
            self.EarliestDeliveryDate: str = None
        if "LatestDeliveryDate" in data:
            self.LatestDeliveryDate: str = self._get_value(str, "LatestDeliveryDate")
        else:
            self.LatestDeliveryDate: str = None
        if "IsBusinessOrder" in data:
            self.IsBusinessOrder: bool = self._get_value(convert_bool, "IsBusinessOrder")
        else:
            self.IsBusinessOrder: bool = None
        if "IsPrime" in data:
            self.IsPrime: bool = self._get_value(convert_bool, "IsPrime")
        else:
            self.IsPrime: bool = None
        if "IsPremiumOrder" in data:
            self.IsPremiumOrder: bool = self._get_value(convert_bool, "IsPremiumOrder")
        else:
            self.IsPremiumOrder: bool = None
        if "IsGlobalExpressEnabled" in data:
            self.IsGlobalExpressEnabled: bool = self._get_value(convert_bool, "IsGlobalExpressEnabled")
        else:
            self.IsGlobalExpressEnabled: bool = None
        if "ReplacedOrderId" in data:
            self.ReplacedOrderId: str = self._get_value(str, "ReplacedOrderId")
        else:
            self.ReplacedOrderId: str = None
        if "IsReplacementOrder" in data:
            self.IsReplacementOrder: bool = self._get_value(convert_bool, "IsReplacementOrder")
        else:
            self.IsReplacementOrder: bool = None
        if "PromiseResponseDueDate" in data:
            self.PromiseResponseDueDate: str = self._get_value(str, "PromiseResponseDueDate")
        else:
            self.PromiseResponseDueDate: str = None
        if "IsEstimatedShipDateSet" in data:
            self.IsEstimatedShipDateSet: bool = self._get_value(convert_bool, "IsEstimatedShipDateSet")
        else:
            self.IsEstimatedShipDateSet: bool = None
        if "IsSoldByAB" in data:
            self.IsSoldByAB: bool = self._get_value(convert_bool, "IsSoldByAB")
        else:
            self.IsSoldByAB: bool = None
        if "DefaultShipFromLocationAddress" in data:
            self.DefaultShipFromLocationAddress: Address = self._get_value(Address, "DefaultShipFromLocationAddress")
        else:
            self.DefaultShipFromLocationAddress: Address = None
        if "FulfillmentInstruction" in data:
            self.FulfillmentInstruction: FulfillmentInstruction = self._get_value(
                FulfillmentInstruction, "FulfillmentInstruction"
            )
        else:
            self.FulfillmentInstruction: FulfillmentInstruction = None
        if "IsISPU" in data:
            self.IsISPU: bool = self._get_value(convert_bool, "IsISPU")
        else:
            self.IsISPU: bool = None
        if "MarketplaceTaxInfo" in data:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = self._get_value(MarketplaceTaxInfo, "MarketplaceTaxInfo")
        else:
            self.MarketplaceTaxInfo: MarketplaceTaxInfo = None
        if "SellerDisplayName" in data:
            self.SellerDisplayName: str = self._get_value(str, "SellerDisplayName")
        else:
            self.SellerDisplayName: str = None
        if "ShippingAddress" in data:
            self.ShippingAddress: Address = self._get_value(Address, "ShippingAddress")
        else:
            self.ShippingAddress: Address = None
        if "BuyerInfo" in data:
            self.BuyerInfo: BuyerInfo = self._get_value(BuyerInfo, "BuyerInfo")
        else:
            self.BuyerInfo: BuyerInfo = None


class OrderBuyerInfo(__BaseDictObject):
    """
    Buyer information for an order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "BuyerEmail" in data:
            self.BuyerEmail: str = self._get_value(str, "BuyerEmail")
        else:
            self.BuyerEmail: str = None
        if "BuyerName" in data:
            self.BuyerName: str = self._get_value(str, "BuyerName")
        else:
            self.BuyerName: str = None
        if "BuyerCounty" in data:
            self.BuyerCounty: str = self._get_value(str, "BuyerCounty")
        else:
            self.BuyerCounty: str = None
        if "BuyerTaxInfo" in data:
            self.BuyerTaxInfo: BuyerTaxInfo = self._get_value(BuyerTaxInfo, "BuyerTaxInfo")
        else:
            self.BuyerTaxInfo: BuyerTaxInfo = None
        if "PurchaseOrderNumber" in data:
            self.PurchaseOrderNumber: str = self._get_value(str, "PurchaseOrderNumber")
        else:
            self.PurchaseOrderNumber: str = None


class OrderAddress(__BaseDictObject):
    """
    The shipping address for the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None
        if "ShippingAddress" in data:
            self.ShippingAddress: Address = self._get_value(Address, "ShippingAddress")
        else:
            self.ShippingAddress: Address = None


class Address(__BaseDictObject):
    """
    The shipping address for the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Name" in data:
            self.Name: str = self._get_value(str, "Name")
        else:
            self.Name: str = None
        if "AddressLine1" in data:
            self.AddressLine1: str = self._get_value(str, "AddressLine1")
        else:
            self.AddressLine1: str = None
        if "AddressLine2" in data:
            self.AddressLine2: str = self._get_value(str, "AddressLine2")
        else:
            self.AddressLine2: str = None
        if "AddressLine3" in data:
            self.AddressLine3: str = self._get_value(str, "AddressLine3")
        else:
            self.AddressLine3: str = None
        if "City" in data:
            self.City: str = self._get_value(str, "City")
        else:
            self.City: str = None
        if "County" in data:
            self.County: str = self._get_value(str, "County")
        else:
            self.County: str = None
        if "District" in data:
            self.District: str = self._get_value(str, "District")
        else:
            self.District: str = None
        if "StateOrRegion" in data:
            self.StateOrRegion: str = self._get_value(str, "StateOrRegion")
        else:
            self.StateOrRegion: str = None
        if "Municipality" in data:
            self.Municipality: str = self._get_value(str, "Municipality")
        else:
            self.Municipality: str = None
        if "PostalCode" in data:
            self.PostalCode: str = self._get_value(str, "PostalCode")
        else:
            self.PostalCode: str = None
        if "CountryCode" in data:
            self.CountryCode: str = self._get_value(str, "CountryCode")
        else:
            self.CountryCode: str = None
        if "Phone" in data:
            self.Phone: str = self._get_value(str, "Phone")
        else:
            self.Phone: str = None
        if "AddressType" in data:
            self.AddressType: str = self._get_value(str, "AddressType")
        else:
            self.AddressType: str = None


class Money(__BaseDictObject):
    """
    The monetary value of the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: str = self._get_value(str, "Amount")
        else:
            self.Amount: str = None


class PaymentExecutionDetailItem(__BaseDictObject):
    """
    Information about a sub-payment method used to pay for a COD order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Payment" in data:
            self.Payment: Money = self._get_value(Money, "Payment")
        else:
            self.Payment: Money = None
        if "PaymentMethod" in data:
            self.PaymentMethod: str = self._get_value(str, "PaymentMethod")
        else:
            self.PaymentMethod: str = None


class BuyerTaxInfo(__BaseDictObject):
    """
    Tax information about the buyer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CompanyLegalName" in data:
            self.CompanyLegalName: str = self._get_value(str, "CompanyLegalName")
        else:
            self.CompanyLegalName: str = None
        if "TaxingRegion" in data:
            self.TaxingRegion: str = self._get_value(str, "TaxingRegion")
        else:
            self.TaxingRegion: str = None
        if "TaxClassifications" in data:
            self.TaxClassifications: _List[TaxClassification] = [
                TaxClassification(datum) for datum in data["TaxClassifications"]
            ]
        else:
            self.TaxClassifications: _List[TaxClassification] = []


class MarketplaceTaxInfo(__BaseDictObject):
    """
    Tax information about the marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        if "TaxClassifications" in data:
            self.TaxClassifications: _List[TaxClassification] = [
                TaxClassification(datum) for datum in data["TaxClassifications"]
            ]
        else:
            self.TaxClassifications: _List[TaxClassification] = []


class TaxClassification(__BaseDictObject):
    """
    The tax classification for the order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Name" in data:
            self.Name: str = self._get_value(str, "Name")
        else:
            self.Name: str = None
        if "Value" in data:
            self.Value: str = self._get_value(str, "Value")
        else:
            self.Value: str = None


class OrderItemsList(__BaseDictObject):
    """
    The order items list along with the order ID.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItems" in data:
            self.OrderItems: OrderItemList = self._get_value(OrderItemList, "OrderItems")
        else:
            self.OrderItems: OrderItemList = None
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None


class OrderItem(__BaseDictObject):
    """
    A single order item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None
        if "OrderItemId" in data:
            self.OrderItemId: str = self._get_value(str, "OrderItemId")
        else:
            self.OrderItemId: str = None
        if "Title" in data:
            self.Title: str = self._get_value(str, "Title")
        else:
            self.Title: str = None
        if "QuantityOrdered" in data:
            self.QuantityOrdered: int = self._get_value(int, "QuantityOrdered")
        else:
            self.QuantityOrdered: int = None
        if "QuantityShipped" in data:
            self.QuantityShipped: int = self._get_value(int, "QuantityShipped")
        else:
            self.QuantityShipped: int = None
        if "ProductInfo" in data:
            self.ProductInfo: ProductInfoDetail = self._get_value(ProductInfoDetail, "ProductInfo")
        else:
            self.ProductInfo: ProductInfoDetail = None
        if "PointsGranted" in data:
            self.PointsGranted: PointsGrantedDetail = self._get_value(PointsGrantedDetail, "PointsGranted")
        else:
            self.PointsGranted: PointsGrantedDetail = None
        if "ItemPrice" in data:
            self.ItemPrice: Money = self._get_value(Money, "ItemPrice")
        else:
            self.ItemPrice: Money = None
        if "ShippingPrice" in data:
            self.ShippingPrice: Money = self._get_value(Money, "ShippingPrice")
        else:
            self.ShippingPrice: Money = None
        if "ItemTax" in data:
            self.ItemTax: Money = self._get_value(Money, "ItemTax")
        else:
            self.ItemTax: Money = None
        if "ShippingTax" in data:
            self.ShippingTax: Money = self._get_value(Money, "ShippingTax")
        else:
            self.ShippingTax: Money = None
        if "ShippingDiscount" in data:
            self.ShippingDiscount: Money = self._get_value(Money, "ShippingDiscount")
        else:
            self.ShippingDiscount: Money = None
        if "ShippingDiscountTax" in data:
            self.ShippingDiscountTax: Money = self._get_value(Money, "ShippingDiscountTax")
        else:
            self.ShippingDiscountTax: Money = None
        if "PromotionDiscount" in data:
            self.PromotionDiscount: Money = self._get_value(Money, "PromotionDiscount")
        else:
            self.PromotionDiscount: Money = None
        if "PromotionDiscountTax" in data:
            self.PromotionDiscountTax: Money = self._get_value(Money, "PromotionDiscountTax")
        else:
            self.PromotionDiscountTax: Money = None
        if "PromotionIds" in data:
            self.PromotionIds: PromotionIdList = self._get_value(PromotionIdList, "PromotionIds")
        else:
            self.PromotionIds: PromotionIdList = None
        if "CODFee" in data:
            self.CODFee: Money = self._get_value(Money, "CODFee")
        else:
            self.CODFee: Money = None
        if "CODFeeDiscount" in data:
            self.CODFeeDiscount: Money = self._get_value(Money, "CODFeeDiscount")
        else:
            self.CODFeeDiscount: Money = None
        if "IsGift" in data:
            self.IsGift: bool = self._get_value(convert_bool, "IsGift")
        else:
            self.IsGift: bool = None
        if "ConditionNote" in data:
            self.ConditionNote: str = self._get_value(str, "ConditionNote")
        else:
            self.ConditionNote: str = None
        if "ConditionId" in data:
            self.ConditionId: str = self._get_value(str, "ConditionId")
        else:
            self.ConditionId: str = None
        if "ConditionSubtypeId" in data:
            self.ConditionSubtypeId: str = self._get_value(str, "ConditionSubtypeId")
        else:
            self.ConditionSubtypeId: str = None
        if "ScheduledDeliveryStartDate" in data:
            self.ScheduledDeliveryStartDate: str = self._get_value(str, "ScheduledDeliveryStartDate")
        else:
            self.ScheduledDeliveryStartDate: str = None
        if "ScheduledDeliveryEndDate" in data:
            self.ScheduledDeliveryEndDate: str = self._get_value(str, "ScheduledDeliveryEndDate")
        else:
            self.ScheduledDeliveryEndDate: str = None
        if "PriceDesignation" in data:
            self.PriceDesignation: str = self._get_value(str, "PriceDesignation")
        else:
            self.PriceDesignation: str = None
        if "TaxCollection" in data:
            self.TaxCollection: TaxCollection = self._get_value(TaxCollection, "TaxCollection")
        else:
            self.TaxCollection: TaxCollection = None
        if "SerialNumberRequired" in data:
            self.SerialNumberRequired: bool = self._get_value(convert_bool, "SerialNumberRequired")
        else:
            self.SerialNumberRequired: bool = None
        if "IsTransparency" in data:
            self.IsTransparency: bool = self._get_value(convert_bool, "IsTransparency")
        else:
            self.IsTransparency: bool = None
        if "IossNumber" in data:
            self.IossNumber: str = self._get_value(str, "IossNumber")
        else:
            self.IossNumber: str = None
        if "StoreChainStoreId" in data:
            self.StoreChainStoreId: str = self._get_value(str, "StoreChainStoreId")
        else:
            self.StoreChainStoreId: str = None
        if "DeemedResellerCategory" in data:
            self.DeemedResellerCategory: str = self._get_value(str, "DeemedResellerCategory")
        else:
            self.DeemedResellerCategory: str = None
        if "BuyerInfo" in data:
            self.BuyerInfo: ItemBuyerInfo = self._get_value(ItemBuyerInfo, "BuyerInfo")
        else:
            self.BuyerInfo: ItemBuyerInfo = None


class OrderItemsBuyerInfoList(__BaseDictObject):
    """
    A single order item's buyer information list with the order ID.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItems" in data:
            self.OrderItems: OrderItemBuyerInfoList = self._get_value(OrderItemBuyerInfoList, "OrderItems")
        else:
            self.OrderItems: OrderItemBuyerInfoList = None
        if "NextToken" in data:
            self.NextToken: str = self._get_value(str, "NextToken")
        else:
            self.NextToken: str = None
        if "AmazonOrderId" in data:
            self.AmazonOrderId: str = self._get_value(str, "AmazonOrderId")
        else:
            self.AmazonOrderId: str = None


class OrderItemBuyerInfo(__BaseDictObject):
    """
    A single order item's buyer information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "OrderItemId" in data:
            self.OrderItemId: str = self._get_value(str, "OrderItemId")
        else:
            self.OrderItemId: str = None
        if "BuyerCustomizedInfo" in data:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = self._get_value(
                BuyerCustomizedInfoDetail, "BuyerCustomizedInfo"
            )
        else:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = None
        if "GiftWrapPrice" in data:
            self.GiftWrapPrice: Money = self._get_value(Money, "GiftWrapPrice")
        else:
            self.GiftWrapPrice: Money = None
        if "GiftWrapTax" in data:
            self.GiftWrapTax: Money = self._get_value(Money, "GiftWrapTax")
        else:
            self.GiftWrapTax: Money = None
        if "GiftMessageText" in data:
            self.GiftMessageText: str = self._get_value(str, "GiftMessageText")
        else:
            self.GiftMessageText: str = None
        if "GiftWrapLevel" in data:
            self.GiftWrapLevel: str = self._get_value(str, "GiftWrapLevel")
        else:
            self.GiftWrapLevel: str = None


class PointsGrantedDetail(__BaseDictObject):
    """
    The number of Amazon Points offered with the purchase of an item, and their monetary value.
    """

    def __init__(self, data):
        super().__init__(data)
        if "PointsNumber" in data:
            self.PointsNumber: int = self._get_value(int, "PointsNumber")
        else:
            self.PointsNumber: int = None
        if "PointsMonetaryValue" in data:
            self.PointsMonetaryValue: Money = self._get_value(Money, "PointsMonetaryValue")
        else:
            self.PointsMonetaryValue: Money = None


class ProductInfoDetail(__BaseDictObject):
    """
    Product information on the number of items.
    """

    def __init__(self, data):
        super().__init__(data)
        if "NumberOfItems" in data:
            self.NumberOfItems: int = self._get_value(int, "NumberOfItems")
        else:
            self.NumberOfItems: int = None


class BuyerCustomizedInfoDetail(__BaseDictObject):
    """
    Buyer information for custom orders from the Amazon Custom program.
    """

    def __init__(self, data):
        super().__init__(data)
        if "CustomizedURL" in data:
            self.CustomizedURL: str = self._get_value(str, "CustomizedURL")
        else:
            self.CustomizedURL: str = None


class TaxCollection(__BaseDictObject):
    """
    Information about withheld taxes.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Model" in data:
            self.Model: str = self._get_value(str, "Model")
        else:
            self.Model: str = None
        if "ResponsibleParty" in data:
            self.ResponsibleParty: str = self._get_value(str, "ResponsibleParty")
        else:
            self.ResponsibleParty: str = None


class FulfillmentInstruction(__BaseDictObject):
    """
    Contains the instructions about the fulfillment like where should it be fulfilled from.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FulfillmentSupplySourceId" in data:
            self.FulfillmentSupplySourceId: str = self._get_value(str, "FulfillmentSupplySourceId")
        else:
            self.FulfillmentSupplySourceId: str = None


class BuyerInfo(__BaseDictObject):
    """
    Buyer information
    """

    def __init__(self, data):
        super().__init__(data)
        if "BuyerEmail" in data:
            self.BuyerEmail: str = self._get_value(str, "BuyerEmail")
        else:
            self.BuyerEmail: str = None
        if "BuyerName" in data:
            self.BuyerName: str = self._get_value(str, "BuyerName")
        else:
            self.BuyerName: str = None
        if "BuyerCounty" in data:
            self.BuyerCounty: str = self._get_value(str, "BuyerCounty")
        else:
            self.BuyerCounty: str = None
        if "BuyerTaxInfo" in data:
            self.BuyerTaxInfo: BuyerTaxInfo = self._get_value(BuyerTaxInfo, "BuyerTaxInfo")
        else:
            self.BuyerTaxInfo: BuyerTaxInfo = None
        if "PurchaseOrderNumber" in data:
            self.PurchaseOrderNumber: str = self._get_value(str, "PurchaseOrderNumber")
        else:
            self.PurchaseOrderNumber: str = None


class ItemBuyerInfo(__BaseDictObject):
    """
    A single item's buyer information.
    """

    def __init__(self, data):
        super().__init__(data)
        if "BuyerCustomizedInfo" in data:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = self._get_value(
                BuyerCustomizedInfoDetail, "BuyerCustomizedInfo"
            )
        else:
            self.BuyerCustomizedInfo: BuyerCustomizedInfoDetail = None
        if "GiftWrapPrice" in data:
            self.GiftWrapPrice: Money = self._get_value(Money, "GiftWrapPrice")
        else:
            self.GiftWrapPrice: Money = None
        if "GiftWrapTax" in data:
            self.GiftWrapTax: Money = self._get_value(Money, "GiftWrapTax")
        else:
            self.GiftWrapTax: Money = None
        if "GiftMessageText" in data:
            self.GiftMessageText: str = self._get_value(str, "GiftMessageText")
        else:
            self.GiftMessageText: str = None
        if "GiftWrapLevel" in data:
            self.GiftWrapLevel: str = self._get_value(str, "GiftWrapLevel")
        else:
            self.GiftWrapLevel: str = None


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


class OrderList(list, _List["Order"]):
    """
    A list of orders.
    """

    def __init__(self, data):
        super().__init__([Order(datum) for datum in data])
        self.data = data


class PaymentMethodDetailItemList(list, _List["str"]):
    """
    A list of payment method detail items.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class PaymentExecutionDetailItemList(list, _List["PaymentExecutionDetailItem"]):
    """
    A list of payment execution detail items.
    """

    def __init__(self, data):
        super().__init__([PaymentExecutionDetailItem(datum) for datum in data])
        self.data = data


class OrderItemList(list, _List["OrderItem"]):
    """
    A list of order items.
    """

    def __init__(self, data):
        super().__init__([OrderItem(datum) for datum in data])
        self.data = data


class OrderItemBuyerInfoList(list, _List["OrderItemBuyerInfo"]):
    """
    A single order item's buyer information list.
    """

    def __init__(self, data):
        super().__init__([OrderItemBuyerInfo(datum) for datum in data])
        self.data = data


class PromotionIdList(list, _List["str"]):
    """
    A list of promotion identifiers provided by the seller when the promotions were created.
    """

    def __init__(self, data):
        super().__init__([str(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class OrdersV0Client(__BaseClient):
    def getOrders(
        self,
        MarketplaceIds: _List[str],
        CreatedAfter: str = None,
        CreatedBefore: str = None,
        LastUpdatedAfter: str = None,
        LastUpdatedBefore: str = None,
        OrderStatuses: _List[str] = None,
        FulfillmentChannels: _List[str] = None,
        PaymentMethods: _List[str] = None,
        BuyerEmail: str = None,
        SellerOrderId: str = None,
        MaxResultsPerPage: int = None,
        EasyShipShipmentStatuses: _List[str] = None,
        NextToken: str = None,
        AmazonOrderIds: _List[str] = None,
        ActualFulfillmentSupplySourceId: str = None,
        IsISPU: bool = None,
        StoreChainStoreId: str = None,
    ):
        """
                Returns orders created or updated during the time frame indicated by the specified parameters. You can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is present, that will be used to retrieve the orders instead of other criteria.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/orders/v0/orders"
        params = {}
        if CreatedAfter is not None:
            params["CreatedAfter"] = CreatedAfter
        if CreatedBefore is not None:
            params["CreatedBefore"] = CreatedBefore
        if LastUpdatedAfter is not None:
            params["LastUpdatedAfter"] = LastUpdatedAfter
        if LastUpdatedBefore is not None:
            params["LastUpdatedBefore"] = LastUpdatedBefore
        if OrderStatuses is not None:
            params["OrderStatuses"] = ",".join(map(str, OrderStatuses))
        if MarketplaceIds is not None:
            params["MarketplaceIds"] = ",".join(map(str, MarketplaceIds))
        if FulfillmentChannels is not None:
            params["FulfillmentChannels"] = ",".join(map(str, FulfillmentChannels))
        if PaymentMethods is not None:
            params["PaymentMethods"] = ",".join(map(str, PaymentMethods))
        if BuyerEmail is not None:
            params["BuyerEmail"] = BuyerEmail
        if SellerOrderId is not None:
            params["SellerOrderId"] = SellerOrderId
        if MaxResultsPerPage is not None:
            params["MaxResultsPerPage"] = MaxResultsPerPage
        if EasyShipShipmentStatuses is not None:
            params["EasyShipShipmentStatuses"] = ",".join(map(str, EasyShipShipmentStatuses))
        if NextToken is not None:
            params["NextToken"] = NextToken
        if AmazonOrderIds is not None:
            params["AmazonOrderIds"] = ",".join(map(str, AmazonOrderIds))
        if ActualFulfillmentSupplySourceId is not None:
            params["ActualFulfillmentSupplySourceId"] = ActualFulfillmentSupplySourceId
        if IsISPU is not None:
            params["IsISPU"] = IsISPU
        if StoreChainStoreId is not None:
            params["StoreChainStoreId"] = StoreChainStoreId
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrdersResponse,
            400: GetOrdersResponse,
            403: GetOrdersResponse,
            404: GetOrdersResponse,
            429: GetOrdersResponse,
            500: GetOrdersResponse,
            503: GetOrdersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrder(
        self,
        orderId: str,
    ):
        """
                Returns the order indicated by the specified order ID.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/orders/v0/orders/{orderId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderResponse,
            400: GetOrderResponse,
            403: GetOrderResponse,
            404: GetOrderResponse,
            429: GetOrderResponse,
            500: GetOrderResponse,
            503: GetOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderBuyerInfo(
        self,
        orderId: str,
    ):
        """
                Returns buyer information for the specified order.
        **Important.** We recommend using the getOrders operation to get buyer information for an order, as the getOrderBuyerInfo operation is scheduled for deprecation on January 12, 2022. For more information, see the [Tokens API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/tokens-api-use-case-guide/tokens-API-use-case-guide-2021-03-01.md).
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/orders/v0/orders/{orderId}/buyerInfo"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderBuyerInfoResponse,
            400: GetOrderBuyerInfoResponse,
            403: GetOrderBuyerInfoResponse,
            404: GetOrderBuyerInfoResponse,
            429: GetOrderBuyerInfoResponse,
            500: GetOrderBuyerInfoResponse,
            503: GetOrderBuyerInfoResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderAddress(
        self,
        orderId: str,
    ):
        """
                Returns the shipping address for the specified order.
        **Important.** We recommend using the getOrders operation to get shipping address information for an order, as the getOrderAddress operation is scheduled for deprecation on January 12, 2022. For more information, see the [Tokens API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/tokens-api-use-case-guide/tokens-API-use-case-guide-2021-03-01.md).
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/orders/v0/orders/{orderId}/address"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderAddressResponse,
            400: GetOrderAddressResponse,
            403: GetOrderAddressResponse,
            404: GetOrderAddressResponse,
            429: GetOrderAddressResponse,
            500: GetOrderAddressResponse,
            503: GetOrderAddressResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderItems(
        self,
        orderId: str,
        NextToken: str = None,
    ):
        """
                Returns detailed order item information for the order indicated by the specified order ID. If NextToken is provided, it's used to retrieve the next page of order items.
        Note: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/orders/v0/orders/{orderId}/orderItems"
        params = {}
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderItemsResponse,
            400: GetOrderItemsResponse,
            403: GetOrderItemsResponse,
            404: GetOrderItemsResponse,
            429: GetOrderItemsResponse,
            500: GetOrderItemsResponse,
            503: GetOrderItemsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderItemsBuyerInfo(
        self,
        orderId: str,
        NextToken: str = None,
    ):
        """
                Returns buyer information for the order items in the specified order.
        **Important.** We recommend using the getOrderItems operation to get buyer information for the order items in an order, as the getOrderItemsBuyerInfo operation is scheduled for deprecation on January 12, 2022. For more information, see the [Tokens API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/tokens-api-use-case-guide/tokens-API-use-case-guide-2021-03-01.md).
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 0.0055 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/orders/v0/orders/{orderId}/orderItems/buyerInfo"
        params = {}
        if NextToken is not None:
            params["NextToken"] = NextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderItemsBuyerInfoResponse,
            400: GetOrderItemsBuyerInfoResponse,
            403: GetOrderItemsBuyerInfoResponse,
            404: GetOrderItemsBuyerInfoResponse,
            429: GetOrderItemsBuyerInfoResponse,
            500: GetOrderItemsBuyerInfoResponse,
            503: GetOrderItemsBuyerInfoResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
