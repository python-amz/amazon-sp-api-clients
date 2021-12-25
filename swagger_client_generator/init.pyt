{% for client in clients %}
from .{{ client.package }} import {{ client.class_name }}Client
{% endfor %}

from .marketplaces import MarketPlaces
from .report_types import ReportType, ReportTypeGroup
from .base import BaseClients
from functools import cached_property

class AmazonSpApiClients(BaseClients):
    {% for client in clients %}
    @cached_property
    def {{ client.package }}(self):
        return {{ client.class_name }}Client(**self._parameters)
    {% endfor %}


version = '1.7.9'
name = "amazon-sp-api-clients"
author = "Haoyu Pan"
author_email = "panhaoyu.china@outlook.com"
description = "Amazon selling partner api clients."
url = "https://github.com/panhaoyu/sp-api-clients"
