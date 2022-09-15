from enum import IntEnum, Enum
from dataclasses import dataclass

class ReportTypeGroup(IntEnum):
{% for group, reports in groups.items() %}
    {{ group }} = {{ loop.index }}
{% endfor %}

    @property
    def reports(self):
        return (report for report in ReportType if report.group == self)


@dataclass
class __ReportTypeDefinition:
    __group_index: int
    __report_index: int
    upload_name: str

    @property
    def index(self):
        return self.__group_index * 100 + self.__report_index

    @property
    def group(self) -> ReportTypeGroup:
        return ReportTypeGroup(self.__group_index)

class ReportType(__ReportTypeDefinition, Enum):
{% for group, reports in groups.items() %}
    {% set outer = loop %}
    {% for report, value in reports.items() %}
    {{ report }} = {{ outer.index }}, {{ loop.index }}, "{{ value }}"
    {% endfor %}
{% endfor %}
