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
    from .api.orders_v0 import OrdersV0Client


class AmazonSpApiClients(_Base):
    @cached_property
    def orders_v0(self) -> "OrdersV0Client":
        from .api.orders_v0 import OrdersV0Client

        return OrdersV0Client(**self._parameters)
