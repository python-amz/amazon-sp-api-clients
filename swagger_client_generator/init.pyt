{% for client in clients %}
from .{{ client.package }} import {{ client.class_name }}Client
{% endfor %}

from .marketplaces import MarketPlaces
from .report_types import ReportType, ReportTypeGroup
from .base import BaseClients
try:
    from functools import cached_property
except ImportError:
    try:
        from cached_property import cached_property
    except ImportError:
        raise 'Please install cached_property for python < 3.8'

class AmazonSpApiClients(BaseClients):
    {% for client in clients %}
    @cached_property
    def {{ client.package }}(self):
        return {{ client.class_name }}Client(**self._parameters)
    {% endfor %}
