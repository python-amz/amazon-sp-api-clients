from .aplus_content_2020_11_01 import AplusContent20201101Client
from .authorization_v1 import AuthorizationV1Client
from .catalog_items_2020_12_01 import CatalogItems20201201Client
from .catalog_items_v0 import CatalogItemsV0Client
from .fba_inbound_eligibility_v1 import FbaInboundEligibilityV1Client
from .fba_inventory_v1 import FbaInventoryV1Client
from .fba_small_and_light_v1 import FbaSmallAndLightV1Client
from .feeds_2020_09_04 import Feeds20200904Client
from .feeds_2021_06_30 import Feeds20210630Client
from .finances_v0 import FinancesV0Client
from .fulfillment_inbound_v0 import FulfillmentInboundV0Client
from .fulfillment_outbound_2020_07_01 import FulfillmentOutbound20200701Client
from .listings_items_2020_09_01 import ListingsItems20200901Client
from .listings_items_2021_08_01 import ListingsItems20210801Client
from .listings_restrictions_2021_08_01 import ListingsRestrictions20210801Client
from .merchant_fulfillment_v0 import MerchantFulfillmentV0Client
from .messaging_v1 import MessagingV1Client
from .notifications_v1 import NotificationsV1Client
from .orders_v0 import OrdersV0Client
from .product_fees_v0 import ProductFeesV0Client
from .product_pricing_v0 import ProductPricingV0Client
from .product_type_definitions_2020_09_01 import ProductTypeDefinitions20200901Client
from .reports_2020_09_04 import Reports20200904Client
from .reports_2021_06_30 import Reports20210630Client
from .sales_v1 import SalesV1Client
from .sellers_v1 import SellersV1Client
from .services_v1 import ServicesV1Client
from .shipment_invoicing_v0 import ShipmentInvoicingV0Client
from .shipping_v1 import ShippingV1Client
from .solicitations_v1 import SolicitationsV1Client
from .tokens_2021_03_01 import Tokens20210301Client
from .uploads_2020_11_01 import Uploads20201101Client
from .vendor_direct_fulfillment_inventory_v1 import VendorDirectFulfillmentInventoryV1Client
from .vendor_direct_fulfillment_orders_2021_12_28 import VendorDirectFulfillmentOrders20211228Client
from .vendor_direct_fulfillment_orders_v1 import VendorDirectFulfillmentOrdersV1Client
from .vendor_direct_fulfillment_payments_v1 import VendorDirectFulfillmentPaymentsV1Client
from .vendor_direct_fulfillment_sandbox_test_data_2021_10_28 import VendorDirectFulfillmentSandboxTestData20211028Client
from .vendor_direct_fulfillment_shipping_2021_12_28 import VendorDirectFulfillmentShipping20211228Client
from .vendor_direct_fulfillment_shipping_v1 import VendorDirectFulfillmentShippingV1Client
from .vendor_direct_fulfillment_transactions_2021_12_28 import VendorDirectFulfillmentTransactions20211228Client
from .vendor_direct_fulfillment_transactions_v1 import VendorDirectFulfillmentTransactionsV1Client
from .vendor_invoices_v1 import VendorInvoicesV1Client
from .vendor_orders_v1 import VendorOrdersV1Client
from .vendor_shipments_v1 import VendorShipmentsV1Client
from .vendor_transaction_status_v1 import VendorTransactionStatusV1Client
from .marketplaces import MarketPlaces
from .report_types import ReportType, ReportTypeGroup
from .base import BaseClients

try:
    from functools import cached_property
except ImportError:
    try:
        from cached_property import cached_property
    except ImportError:
        raise "Please install cached_property for python < 3.8"


class AmazonSpApiClients(BaseClients):
    @cached_property
    def aplus_content_2020_11_01(self):
        return AplusContent20201101Client(**self._parameters)

    @cached_property
    def authorization_v1(self):
        return AuthorizationV1Client(**self._parameters)

    @cached_property
    def catalog_items_2020_12_01(self):
        return CatalogItems20201201Client(**self._parameters)

    @cached_property
    def catalog_items_v0(self):
        return CatalogItemsV0Client(**self._parameters)

    @cached_property
    def fba_inbound_eligibility_v1(self):
        return FbaInboundEligibilityV1Client(**self._parameters)

    @cached_property
    def fba_inventory_v1(self):
        return FbaInventoryV1Client(**self._parameters)

    @cached_property
    def fba_small_and_light_v1(self):
        return FbaSmallAndLightV1Client(**self._parameters)

    @cached_property
    def feeds_2020_09_04(self):
        return Feeds20200904Client(**self._parameters)

    @cached_property
    def feeds_2021_06_30(self):
        return Feeds20210630Client(**self._parameters)

    @cached_property
    def finances_v0(self):
        return FinancesV0Client(**self._parameters)

    @cached_property
    def fulfillment_inbound_v0(self):
        return FulfillmentInboundV0Client(**self._parameters)

    @cached_property
    def fulfillment_outbound_2020_07_01(self):
        return FulfillmentOutbound20200701Client(**self._parameters)

    @cached_property
    def listings_items_2020_09_01(self):
        return ListingsItems20200901Client(**self._parameters)

    @cached_property
    def listings_items_2021_08_01(self):
        return ListingsItems20210801Client(**self._parameters)

    @cached_property
    def listings_restrictions_2021_08_01(self):
        return ListingsRestrictions20210801Client(**self._parameters)

    @cached_property
    def merchant_fulfillment_v0(self):
        return MerchantFulfillmentV0Client(**self._parameters)

    @cached_property
    def messaging_v1(self):
        return MessagingV1Client(**self._parameters)

    @cached_property
    def notifications_v1(self):
        return NotificationsV1Client(**self._parameters)

    @cached_property
    def orders_v0(self):
        return OrdersV0Client(**self._parameters)

    @cached_property
    def product_fees_v0(self):
        return ProductFeesV0Client(**self._parameters)

    @cached_property
    def product_pricing_v0(self):
        return ProductPricingV0Client(**self._parameters)

    @cached_property
    def product_type_definitions_2020_09_01(self):
        return ProductTypeDefinitions20200901Client(**self._parameters)

    @cached_property
    def reports_2020_09_04(self):
        return Reports20200904Client(**self._parameters)

    @cached_property
    def reports_2021_06_30(self):
        return Reports20210630Client(**self._parameters)

    @cached_property
    def sales_v1(self):
        return SalesV1Client(**self._parameters)

    @cached_property
    def sellers_v1(self):
        return SellersV1Client(**self._parameters)

    @cached_property
    def services_v1(self):
        return ServicesV1Client(**self._parameters)

    @cached_property
    def shipment_invoicing_v0(self):
        return ShipmentInvoicingV0Client(**self._parameters)

    @cached_property
    def shipping_v1(self):
        return ShippingV1Client(**self._parameters)

    @cached_property
    def solicitations_v1(self):
        return SolicitationsV1Client(**self._parameters)

    @cached_property
    def tokens_2021_03_01(self):
        return Tokens20210301Client(**self._parameters)

    @cached_property
    def uploads_2020_11_01(self):
        return Uploads20201101Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_inventory_v1(self):
        return VendorDirectFulfillmentInventoryV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_orders_2021_12_28(self):
        return VendorDirectFulfillmentOrders20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_orders_v1(self):
        return VendorDirectFulfillmentOrdersV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_payments_v1(self):
        return VendorDirectFulfillmentPaymentsV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_sandbox_test_data_2021_10_28(self):
        return VendorDirectFulfillmentSandboxTestData20211028Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_shipping_2021_12_28(self):
        return VendorDirectFulfillmentShipping20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_shipping_v1(self):
        return VendorDirectFulfillmentShippingV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_transactions_2021_12_28(self):
        return VendorDirectFulfillmentTransactions20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_transactions_v1(self):
        return VendorDirectFulfillmentTransactionsV1Client(**self._parameters)

    @cached_property
    def vendor_invoices_v1(self):
        return VendorInvoicesV1Client(**self._parameters)

    @cached_property
    def vendor_orders_v1(self):
        return VendorOrdersV1Client(**self._parameters)

    @cached_property
    def vendor_shipments_v1(self):
        return VendorShipmentsV1Client(**self._parameters)

    @cached_property
    def vendor_transaction_status_v1(self):
        return VendorTransactionStatusV1Client(**self._parameters)


version = "1.8.3"
name = "amazon-sp-api-clients"
author = "Haoyu Pan"
author_email = "panhaoyu.china@outlook.com"
description = "Amazon selling partner api clients."
url = "https://github.com/panhaoyu/sp-api-clients"
