import re
from dataclasses import dataclass
from functools import reduce, cached_property
from pathlib import Path

import black
import requests
from bs4 import BeautifulSoup
from jinja2 import Template

from amazon_sp_api_static.report_types import ReportType, ReportTypeGroup

base_dir = Path(__file__).absolute().parent.parent


@dataclass
class ParsedReport:
    report_index: int = -1
    group_index: int = -1
    name: str = ''
    group_name: str = ''
    upload_name: str = ''
    description: str = ''


class Script:
    html_file_path = Path(__file__).parent / 'report_types.html'

    @cached_property
    def html(self):
        # Remove the report_files.html and rerun this script may trigger a update from server.
        url = 'https://developer-docs.amazon.com/sp-api/docs/report-type-values'
        if not self.html_file_path.exists():
            text = requests.get(url).text
            with open('report_types.html', 'w', encoding='utf-8') as f:
                f.write(text)
        with open(self.html_file_path, 'r', encoding='utf-8') as f:
            return f.read()

    @cached_property
    def markdown_body(self):
        soup = BeautifulSoup(self.html, 'lxml')
        soup = soup.select_one('.content-body > .markdown-body')
        return soup

    @cached_property
    def parsed_data(self) -> dict[str, dict[str, ParsedReport]]:
        elements = self.markdown_body.select(
            'h2.heading-2, div.rdmd-table > .rdmd-table-inner > table > tbody > tr > td:first-child')
        groups = []
        current = []
        for e in elements:
            if e.name == 'h2':
                groups.append(current)
                current = [e]
            else:
                current.append(e)
        groups.append(current)
        groups.pop(0)
        result = {}
        for first, *other in groups:
            group = re.sub(r'[_ ()-]+', '_', first.text.strip().lower())
            report_of_groups = result.setdefault(group, {})
            for report in other:
                lines = report.text.splitlines()
                lines = [i.strip() for i in lines]
                lines = [i for i in lines if i]
                match len(lines):
                    case 1:
                        line1 = lines[0]
                        # if there's only one line, then it's like a subtitle, so just skip is ok
                        if line1 in ('FBA Sales Reports',):
                            continue
                        raise NotImplementedError(f'Unsupported line: {line1}')
                    case 2 | 3 | 4:
                        line = ' '.join(lines)
                        assert (
                            m := re.match(r'^([A-Za-z 0-9_:\-()&]*?) reportType value: ?([A-Z0-9_]+?)$', line)), line
                        description, report = m.group(1, 2)
                    case other:
                        raise NotImplementedError(f'TD element with {other} lines cannot be parsed')
                report_of_groups.setdefault(report, ParsedReport(
                    name=report.lower(),
                    upload_name=report,
                    description=description,
                    group_name=group,
                ))
        return result

    @cached_property
    def group_enum(self):
        result = {i.name: i.value for i in ReportTypeGroup}
        for name in self.parsed_data:
            if name not in result:
                index = max(result.values()) + 1
                print(f'Found new group: {name} = {index}')
                result[name] = index
        return result

    @cached_property
    def report_enum(self) -> dict[str, ParsedReport]:
        result: dict[str, ParsedReport] = {}
        for i in ReportType:
            if i.upload_name in result:
                name = f'{i.upload_name}_deprecated'
                result[name] = ParsedReport(
                    name=name.lower(), group_name=i.group.name, group_index=i.group_index,
                    upload_name=i.upload_name, description='', report_index=i.report_index
                )
            else:
                result[i.upload_name] = ParsedReport(
                    name=i.upload_name.lower(), group_name=i.group.name, group_index=i.group_index,
                    upload_name=i.upload_name, description='', report_index=i.report_index
                )
        for group_name, reports in self.parsed_data.items():
            for report_name, report in reports.items():
                if report_name in result:
                    result[report_name].description = report.description
                else:
                    report.group_index = self.group_enum[group_name]
                    reports_of_group = tuple(i for i in result.values() if i.group_index == report.group_index)
                    report.report_index = max((*(i.report_index for i in reports_of_group), 0)) + 1
                    print(f'Found new report: {report.name} = {report.group_index}, {report.report_index}')
                    result.setdefault(report.upload_name, report)
        # noinspection PyTypeChecker
        result = dict(sorted(result.items(), key=lambda i: i[1].group_index * 100 + i[1].report_index))
        return result

    def run(self):
        template_path = base_dir / 'swagger_client_generator' / 'report_types.pyt'
        with open(template_path, 'r', encoding='utf-8') as f:
            template = Template(f.read())
        content = template.render(groups=self.group_enum, reports=self.report_enum)
        content = black.format_str(content, mode=black.Mode(line_length=300))
        content = reduce(lambda i, j: str.replace(i, '\n\n', '\n'), range(5), content)
        content = black.format_str(content, mode=black.Mode(line_length=300))
        with open(base_dir / 'amazon_sp_api_static' / 'report_types.py', 'w', encoding='utf-8') as f:
            f.write(content)
        with open(base_dir / 'amazon_sp_api_clients' / 'report_types.py', 'w', encoding='utf-8') as f:
            f.write(content)

    @classmethod
    def start(cls):
        cls().run()


if __name__ == '__main__':
    Script.start()
