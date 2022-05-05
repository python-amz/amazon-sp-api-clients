from .utils.base_client import BaseAmazonSpApiClients, cached_property


class AmazonSpApiClients(BaseAmazonSpApiClients):
    @cached_property
    def aplus_content_2020_11_01(self):
        from .aplus_content_2020_11_01.api import AplusContent20201101Client

        return AplusContent20201101Client(**self._parameters)

    @cached_property
    def authorization_v1(self):
        from .authorization_v1.api import AuthorizationV1Client

        return AuthorizationV1Client(**self._parameters)

    @cached_property
    def catalog_items_2020_12_01(self):
        from .catalog_items_2020_12_01.api import CatalogItems20201201Client

        return CatalogItems20201201Client(**self._parameters)

    @cached_property
    def catalog_items_v0(self):
        from .catalog_items_v0.api import CatalogItemsV0Client

        return CatalogItemsV0Client(**self._parameters)

    @cached_property
    def fba_inbound_eligibility_v1(self):
        from .fba_inbound_eligibility_v1.api import FbaInboundEligibilityV1Client

        return FbaInboundEligibilityV1Client(**self._parameters)

    @cached_property
    def fba_inventory_v1(self):
        from .fba_inventory_v1.api import FbaInventoryV1Client

        return FbaInventoryV1Client(**self._parameters)

    @cached_property
    def fba_small_and_light_v1(self):
        from .fba_small_and_light_v1.api import FbaSmallAndLightV1Client

        return FbaSmallAndLightV1Client(**self._parameters)

    @cached_property
    def feeds_2020_09_04(self):
        from .feeds_2020_09_04.api import Feeds20200904Client

        return Feeds20200904Client(**self._parameters)

    @cached_property
    def feeds_2021_06_30(self):
        from .feeds_2021_06_30.api import Feeds20210630Client

        return Feeds20210630Client(**self._parameters)

    @cached_property
    def finances_v0(self):
        from .finances_v0.api import FinancesV0Client

        return FinancesV0Client(**self._parameters)

    @cached_property
    def fulfillment_inbound_v0(self):
        from .fulfillment_inbound_v0.api import FulfillmentInboundV0Client

        return FulfillmentInboundV0Client(**self._parameters)

    @cached_property
    def fulfillment_outbound_2020_07_01(self):
        from .fulfillment_outbound_2020_07_01.api import FulfillmentOutbound20200701Client

        return FulfillmentOutbound20200701Client(**self._parameters)

    @cached_property
    def listings_items_2020_09_01(self):
        from .listings_items_2020_09_01.api import ListingsItems20200901Client

        return ListingsItems20200901Client(**self._parameters)

    @cached_property
    def listings_items_2021_08_01(self):
        from .listings_items_2021_08_01.api import ListingsItems20210801Client

        return ListingsItems20210801Client(**self._parameters)

    @cached_property
    def listings_restrictions_2021_08_01(self):
        from .listings_restrictions_2021_08_01.api import ListingsRestrictions20210801Client

        return ListingsRestrictions20210801Client(**self._parameters)

    @cached_property
    def merchant_fulfillment_v0(self):
        from .merchant_fulfillment_v0.api import MerchantFulfillmentV0Client

        return MerchantFulfillmentV0Client(**self._parameters)

    @cached_property
    def messaging_v1(self):
        from .messaging_v1.api import MessagingV1Client

        return MessagingV1Client(**self._parameters)

    @cached_property
    def notifications_v1(self):
        from .notifications_v1.api import NotificationsV1Client

        return NotificationsV1Client(**self._parameters)

    @cached_property
    def orders_v0(self):
        from .orders_v0.api import OrdersV0Client

        return OrdersV0Client(**self._parameters)

    @cached_property
    def product_fees_v0(self):
        from .product_fees_v0.api import ProductFeesV0Client

        return ProductFeesV0Client(**self._parameters)

    @cached_property
    def product_pricing_v0(self):
        from .product_pricing_v0.api import ProductPricingV0Client

        return ProductPricingV0Client(**self._parameters)

    @cached_property
    def product_type_definitions_2020_09_01(self):
        from .product_type_definitions_2020_09_01.api import ProductTypeDefinitions20200901Client

        return ProductTypeDefinitions20200901Client(**self._parameters)

    @cached_property
    def reports_2020_09_04(self):
        from .reports_2020_09_04.api import Reports20200904Client

        return Reports20200904Client(**self._parameters)

    @cached_property
    def reports_2021_06_30(self):
        from .reports_2021_06_30.api import Reports20210630Client

        return Reports20210630Client(**self._parameters)

    @cached_property
    def sales_v1(self):
        from .sales_v1.api import SalesV1Client

        return SalesV1Client(**self._parameters)

    @cached_property
    def sellers_v1(self):
        from .sellers_v1.api import SellersV1Client

        return SellersV1Client(**self._parameters)

    @cached_property
    def services_v1(self):
        from .services_v1.api import ServicesV1Client

        return ServicesV1Client(**self._parameters)

    @cached_property
    def shipment_invoicing_v0(self):
        from .shipment_invoicing_v0.api import ShipmentInvoicingV0Client

        return ShipmentInvoicingV0Client(**self._parameters)

    @cached_property
    def shipping_v1(self):
        from .shipping_v1.api import ShippingV1Client

        return ShippingV1Client(**self._parameters)

    @cached_property
    def solicitations_v1(self):
        from .solicitations_v1.api import SolicitationsV1Client

        return SolicitationsV1Client(**self._parameters)

    @cached_property
    def tokens_2021_03_01(self):
        from .tokens_2021_03_01.api import Tokens20210301Client

        return Tokens20210301Client(**self._parameters)

    @cached_property
    def uploads_2020_11_01(self):
        from .uploads_2020_11_01.api import Uploads20201101Client

        return Uploads20201101Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_inventory_v1(self):
        from .vendor_direct_fulfillment_inventory_v1.api import VendorDirectFulfillmentInventoryV1Client

        return VendorDirectFulfillmentInventoryV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_orders_2021_12_28(self):
        from .vendor_direct_fulfillment_orders_2021_12_28.api import VendorDirectFulfillmentOrders20211228Client

        return VendorDirectFulfillmentOrders20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_orders_v1(self):
        from .vendor_direct_fulfillment_orders_v1.api import VendorDirectFulfillmentOrdersV1Client

        return VendorDirectFulfillmentOrdersV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_payments_v1(self):
        from .vendor_direct_fulfillment_payments_v1.api import VendorDirectFulfillmentPaymentsV1Client

        return VendorDirectFulfillmentPaymentsV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_sandbox_test_data_2021_10_28(self):
        from .vendor_direct_fulfillment_sandbox_test_data_2021_10_28.api import (
            VendorDirectFulfillmentSandboxTestData20211028Client,
        )

        return VendorDirectFulfillmentSandboxTestData20211028Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_shipping_2021_12_28(self):
        from .vendor_direct_fulfillment_shipping_2021_12_28.api import VendorDirectFulfillmentShipping20211228Client

        return VendorDirectFulfillmentShipping20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_shipping_v1(self):
        from .vendor_direct_fulfillment_shipping_v1.api import VendorDirectFulfillmentShippingV1Client

        return VendorDirectFulfillmentShippingV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_transactions_2021_12_28(self):
        from .vendor_direct_fulfillment_transactions_2021_12_28.api import (
            VendorDirectFulfillmentTransactions20211228Client,
        )

        return VendorDirectFulfillmentTransactions20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_transactions_v1(self):
        from .vendor_direct_fulfillment_transactions_v1.api import VendorDirectFulfillmentTransactionsV1Client

        return VendorDirectFulfillmentTransactionsV1Client(**self._parameters)

    @cached_property
    def vendor_invoices_v1(self):
        from .vendor_invoices_v1.api import VendorInvoicesV1Client

        return VendorInvoicesV1Client(**self._parameters)

    @cached_property
    def vendor_orders_v1(self):
        from .vendor_orders_v1.api import VendorOrdersV1Client

        return VendorOrdersV1Client(**self._parameters)

    @cached_property
    def vendor_shipments_v1(self):
        from .vendor_shipments_v1.api import VendorShipmentsV1Client

        return VendorShipmentsV1Client(**self._parameters)

    @cached_property
    def vendor_transaction_status_v1(self):
        from .vendor_transaction_status_v1.api import VendorTransactionStatusV1Client

        return VendorTransactionStatusV1Client(**self._parameters)
