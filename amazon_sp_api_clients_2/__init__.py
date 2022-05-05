from .utils.base_client import (
    BaseAmazonSpApiClients as _Base,
    cached_property,
    MarketPlaces,
    version,
    author,
    author_email,
    description,
    url,
)

from typing import TYPE_CHECKING as _TYPE_CHECKING

if _TYPE_CHECKING:
    from .api.aplus_content_2020_11_01 import AplusContent20201101Client
    from .api.authorization_v1 import AuthorizationV1Client
    from .api.catalog_items_2020_12_01 import CatalogItems20201201Client
    from .api.catalog_items_v0 import CatalogItemsV0Client
    from .api.fba_inbound_eligibility_v1 import FbaInboundEligibilityV1Client
    from .api.fba_inventory_v1 import FbaInventoryV1Client
    from .api.fba_small_and_light_v1 import FbaSmallAndLightV1Client
    from .api.feeds_2020_09_04 import Feeds20200904Client
    from .api.feeds_2021_06_30 import Feeds20210630Client
    from .api.finances_v0 import FinancesV0Client
    from .api.fulfillment_inbound_v0 import FulfillmentInboundV0Client
    from .api.fulfillment_outbound_2020_07_01 import FulfillmentOutbound20200701Client
    from .api.listings_items_2020_09_01 import ListingsItems20200901Client
    from .api.listings_items_2021_08_01 import ListingsItems20210801Client
    from .api.listings_restrictions_2021_08_01 import ListingsRestrictions20210801Client
    from .api.merchant_fulfillment_v0 import MerchantFulfillmentV0Client
    from .api.messaging_v1 import MessagingV1Client
    from .api.notifications_v1 import NotificationsV1Client
    from .api.orders_v0 import OrdersV0Client
    from .api.product_fees_v0 import ProductFeesV0Client
    from .api.product_pricing_v0 import ProductPricingV0Client
    from .api.product_type_definitions_2020_09_01 import ProductTypeDefinitions20200901Client
    from .api.reports_2020_09_04 import Reports20200904Client
    from .api.reports_2021_06_30 import Reports20210630Client
    from .api.sales_v1 import SalesV1Client
    from .api.sellers_v1 import SellersV1Client
    from .api.services_v1 import ServicesV1Client
    from .api.shipment_invoicing_v0 import ShipmentInvoicingV0Client
    from .api.shipping_v1 import ShippingV1Client
    from .api.solicitations_v1 import SolicitationsV1Client
    from .api.tokens_2021_03_01 import Tokens20210301Client
    from .api.uploads_2020_11_01 import Uploads20201101Client
    from .api.vendor_direct_fulfillment_inventory_v1 import VendorDirectFulfillmentInventoryV1Client
    from .api.vendor_direct_fulfillment_orders_2021_12_28 import VendorDirectFulfillmentOrders20211228Client
    from .api.vendor_direct_fulfillment_orders_v1 import VendorDirectFulfillmentOrdersV1Client
    from .api.vendor_direct_fulfillment_payments_v1 import VendorDirectFulfillmentPaymentsV1Client
    from .api.vendor_direct_fulfillment_sandbox_test_data_2021_10_28 import (
        VendorDirectFulfillmentSandboxTestData20211028Client,
    )
    from .api.vendor_direct_fulfillment_shipping_2021_12_28 import VendorDirectFulfillmentShipping20211228Client
    from .api.vendor_direct_fulfillment_shipping_v1 import VendorDirectFulfillmentShippingV1Client
    from .api.vendor_direct_fulfillment_transactions_2021_12_28 import VendorDirectFulfillmentTransactions20211228Client
    from .api.vendor_direct_fulfillment_transactions_v1 import VendorDirectFulfillmentTransactionsV1Client
    from .api.vendor_invoices_v1 import VendorInvoicesV1Client
    from .api.vendor_orders_v1 import VendorOrdersV1Client
    from .api.vendor_shipments_v1 import VendorShipmentsV1Client
    from .api.vendor_transaction_status_v1 import VendorTransactionStatusV1Client


class AmazonSpApiClients(_Base):
    @cached_property
    def aplus_content_2020_11_01(self) -> "AplusContent20201101Client":
        from .api.aplus_content_2020_11_01 import AplusContent20201101Client

        return AplusContent20201101Client(**self._parameters)

    @cached_property
    def authorization_v1(self) -> "AuthorizationV1Client":
        from .api.authorization_v1 import AuthorizationV1Client

        return AuthorizationV1Client(**self._parameters)

    @cached_property
    def catalog_items_2020_12_01(self) -> "CatalogItems20201201Client":
        from .api.catalog_items_2020_12_01 import CatalogItems20201201Client

        return CatalogItems20201201Client(**self._parameters)

    @cached_property
    def catalog_items_v0(self) -> "CatalogItemsV0Client":
        from .api.catalog_items_v0 import CatalogItemsV0Client

        return CatalogItemsV0Client(**self._parameters)

    @cached_property
    def fba_inbound_eligibility_v1(self) -> "FbaInboundEligibilityV1Client":
        from .api.fba_inbound_eligibility_v1 import FbaInboundEligibilityV1Client

        return FbaInboundEligibilityV1Client(**self._parameters)

    @cached_property
    def fba_inventory_v1(self) -> "FbaInventoryV1Client":
        from .api.fba_inventory_v1 import FbaInventoryV1Client

        return FbaInventoryV1Client(**self._parameters)

    @cached_property
    def fba_small_and_light_v1(self) -> "FbaSmallAndLightV1Client":
        from .api.fba_small_and_light_v1 import FbaSmallAndLightV1Client

        return FbaSmallAndLightV1Client(**self._parameters)

    @cached_property
    def feeds_2020_09_04(self) -> "Feeds20200904Client":
        from .api.feeds_2020_09_04 import Feeds20200904Client

        return Feeds20200904Client(**self._parameters)

    @cached_property
    def feeds_2021_06_30(self) -> "Feeds20210630Client":
        from .api.feeds_2021_06_30 import Feeds20210630Client

        return Feeds20210630Client(**self._parameters)

    @cached_property
    def finances_v0(self) -> "FinancesV0Client":
        from .api.finances_v0 import FinancesV0Client

        return FinancesV0Client(**self._parameters)

    @cached_property
    def fulfillment_inbound_v0(self) -> "FulfillmentInboundV0Client":
        from .api.fulfillment_inbound_v0 import FulfillmentInboundV0Client

        return FulfillmentInboundV0Client(**self._parameters)

    @cached_property
    def fulfillment_outbound_2020_07_01(self) -> "FulfillmentOutbound20200701Client":
        from .api.fulfillment_outbound_2020_07_01 import FulfillmentOutbound20200701Client

        return FulfillmentOutbound20200701Client(**self._parameters)

    @cached_property
    def listings_items_2020_09_01(self) -> "ListingsItems20200901Client":
        from .api.listings_items_2020_09_01 import ListingsItems20200901Client

        return ListingsItems20200901Client(**self._parameters)

    @cached_property
    def listings_items_2021_08_01(self) -> "ListingsItems20210801Client":
        from .api.listings_items_2021_08_01 import ListingsItems20210801Client

        return ListingsItems20210801Client(**self._parameters)

    @cached_property
    def listings_restrictions_2021_08_01(self) -> "ListingsRestrictions20210801Client":
        from .api.listings_restrictions_2021_08_01 import ListingsRestrictions20210801Client

        return ListingsRestrictions20210801Client(**self._parameters)

    @cached_property
    def merchant_fulfillment_v0(self) -> "MerchantFulfillmentV0Client":
        from .api.merchant_fulfillment_v0 import MerchantFulfillmentV0Client

        return MerchantFulfillmentV0Client(**self._parameters)

    @cached_property
    def messaging_v1(self) -> "MessagingV1Client":
        from .api.messaging_v1 import MessagingV1Client

        return MessagingV1Client(**self._parameters)

    @cached_property
    def notifications_v1(self) -> "NotificationsV1Client":
        from .api.notifications_v1 import NotificationsV1Client

        return NotificationsV1Client(**self._parameters)

    @cached_property
    def orders_v0(self) -> "OrdersV0Client":
        from .api.orders_v0 import OrdersV0Client

        return OrdersV0Client(**self._parameters)

    @cached_property
    def product_fees_v0(self) -> "ProductFeesV0Client":
        from .api.product_fees_v0 import ProductFeesV0Client

        return ProductFeesV0Client(**self._parameters)

    @cached_property
    def product_pricing_v0(self) -> "ProductPricingV0Client":
        from .api.product_pricing_v0 import ProductPricingV0Client

        return ProductPricingV0Client(**self._parameters)

    @cached_property
    def product_type_definitions_2020_09_01(self) -> "ProductTypeDefinitions20200901Client":
        from .api.product_type_definitions_2020_09_01 import ProductTypeDefinitions20200901Client

        return ProductTypeDefinitions20200901Client(**self._parameters)

    @cached_property
    def reports_2020_09_04(self) -> "Reports20200904Client":
        from .api.reports_2020_09_04 import Reports20200904Client

        return Reports20200904Client(**self._parameters)

    @cached_property
    def reports_2021_06_30(self) -> "Reports20210630Client":
        from .api.reports_2021_06_30 import Reports20210630Client

        return Reports20210630Client(**self._parameters)

    @cached_property
    def sales_v1(self) -> "SalesV1Client":
        from .api.sales_v1 import SalesV1Client

        return SalesV1Client(**self._parameters)

    @cached_property
    def sellers_v1(self) -> "SellersV1Client":
        from .api.sellers_v1 import SellersV1Client

        return SellersV1Client(**self._parameters)

    @cached_property
    def services_v1(self) -> "ServicesV1Client":
        from .api.services_v1 import ServicesV1Client

        return ServicesV1Client(**self._parameters)

    @cached_property
    def shipment_invoicing_v0(self) -> "ShipmentInvoicingV0Client":
        from .api.shipment_invoicing_v0 import ShipmentInvoicingV0Client

        return ShipmentInvoicingV0Client(**self._parameters)

    @cached_property
    def shipping_v1(self) -> "ShippingV1Client":
        from .api.shipping_v1 import ShippingV1Client

        return ShippingV1Client(**self._parameters)

    @cached_property
    def solicitations_v1(self) -> "SolicitationsV1Client":
        from .api.solicitations_v1 import SolicitationsV1Client

        return SolicitationsV1Client(**self._parameters)

    @cached_property
    def tokens_2021_03_01(self) -> "Tokens20210301Client":
        from .api.tokens_2021_03_01 import Tokens20210301Client

        return Tokens20210301Client(**self._parameters)

    @cached_property
    def uploads_2020_11_01(self) -> "Uploads20201101Client":
        from .api.uploads_2020_11_01 import Uploads20201101Client

        return Uploads20201101Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_inventory_v1(self) -> "VendorDirectFulfillmentInventoryV1Client":
        from .api.vendor_direct_fulfillment_inventory_v1 import VendorDirectFulfillmentInventoryV1Client

        return VendorDirectFulfillmentInventoryV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_orders_2021_12_28(self) -> "VendorDirectFulfillmentOrders20211228Client":
        from .api.vendor_direct_fulfillment_orders_2021_12_28 import VendorDirectFulfillmentOrders20211228Client

        return VendorDirectFulfillmentOrders20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_orders_v1(self) -> "VendorDirectFulfillmentOrdersV1Client":
        from .api.vendor_direct_fulfillment_orders_v1 import VendorDirectFulfillmentOrdersV1Client

        return VendorDirectFulfillmentOrdersV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_payments_v1(self) -> "VendorDirectFulfillmentPaymentsV1Client":
        from .api.vendor_direct_fulfillment_payments_v1 import VendorDirectFulfillmentPaymentsV1Client

        return VendorDirectFulfillmentPaymentsV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_sandbox_test_data_2021_10_28(
        self,
    ) -> "VendorDirectFulfillmentSandboxTestData20211028Client":
        from .api.vendor_direct_fulfillment_sandbox_test_data_2021_10_28 import (
            VendorDirectFulfillmentSandboxTestData20211028Client,
        )

        return VendorDirectFulfillmentSandboxTestData20211028Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_shipping_2021_12_28(self) -> "VendorDirectFulfillmentShipping20211228Client":
        from .api.vendor_direct_fulfillment_shipping_2021_12_28 import VendorDirectFulfillmentShipping20211228Client

        return VendorDirectFulfillmentShipping20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_shipping_v1(self) -> "VendorDirectFulfillmentShippingV1Client":
        from .api.vendor_direct_fulfillment_shipping_v1 import VendorDirectFulfillmentShippingV1Client

        return VendorDirectFulfillmentShippingV1Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_transactions_2021_12_28(self) -> "VendorDirectFulfillmentTransactions20211228Client":
        from .api.vendor_direct_fulfillment_transactions_2021_12_28 import (
            VendorDirectFulfillmentTransactions20211228Client,
        )

        return VendorDirectFulfillmentTransactions20211228Client(**self._parameters)

    @cached_property
    def vendor_direct_fulfillment_transactions_v1(self) -> "VendorDirectFulfillmentTransactionsV1Client":
        from .api.vendor_direct_fulfillment_transactions_v1 import VendorDirectFulfillmentTransactionsV1Client

        return VendorDirectFulfillmentTransactionsV1Client(**self._parameters)

    @cached_property
    def vendor_invoices_v1(self) -> "VendorInvoicesV1Client":
        from .api.vendor_invoices_v1 import VendorInvoicesV1Client

        return VendorInvoicesV1Client(**self._parameters)

    @cached_property
    def vendor_orders_v1(self) -> "VendorOrdersV1Client":
        from .api.vendor_orders_v1 import VendorOrdersV1Client

        return VendorOrdersV1Client(**self._parameters)

    @cached_property
    def vendor_shipments_v1(self) -> "VendorShipmentsV1Client":
        from .api.vendor_shipments_v1 import VendorShipmentsV1Client

        return VendorShipmentsV1Client(**self._parameters)

    @cached_property
    def vendor_transaction_status_v1(self) -> "VendorTransactionStatusV1Client":
        from .api.vendor_transaction_status_v1 import VendorTransactionStatusV1Client

        return VendorTransactionStatusV1Client(**self._parameters)
