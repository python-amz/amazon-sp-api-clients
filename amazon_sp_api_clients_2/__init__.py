try:
    from functools import cached_property
except ImportError:
    try:
        from cached_property import cached_property
    except ImportError:
        print('Please install cached_property for python < 3.8')
        raise

from .utils.base_client import BaseClient
from .utils.exceptions import SellingApiError


class AmazonSpApiClients(BaseClient):
    @cached_property
    def marketplaces(self):
        from .utils.marketplaces import MarketPlaces
        return MarketPlaces
