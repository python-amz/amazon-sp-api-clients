import re
from functools import reduce, cached_property
from pathlib import Path

import black
import requests
from bs4 import BeautifulSoup, Tag
from jinja2 import Template

base_dir = Path(__file__).absolute().parent.parent


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
    def element_groups(self):
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
        return groups

    def run(self):
        groups: dict[str, dict[str, str]] = {}
        for h2_element, *td_elements in self.element_groups:
            group_name = h2_element.text.strip().lower() \
                .replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
            group_name = re.sub(r'_+', '_', group_name)
            for row in td_elements:
                row: Tag
                lines = row.text.splitlines()
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
                        report_name, report_type_slug = m.group(1, 2)
                    case other:
                        raise NotImplementedError(f'TD element with {other} lines cannot be parsed')
                report_name = report_type_slug.lower()
                groups.setdefault(group_name, {}).setdefault(report_name, report_type_slug)

        template_path = base_dir / 'swagger_client_generator' / 'report_types.pyt'
        with open(template_path, 'r', encoding='utf-8') as f:
            template = Template(f.read())
        content = template.render(groups=groups)
        content = black.format_str(content, mode=black.Mode(line_length=120))
        content = reduce(lambda i, j: str.replace(i, '\n\n', '\n'), range(5), content)
        content = black.format_str(content, mode=black.Mode(line_length=120))
        with open(base_dir / 'amazon_sp_api_static' / 'report_types.py', 'w', encoding='utf-8') as f:
            f.write(content)
        with open(base_dir / 'amazon_sp_api_clients' / 'report_types.py', 'w', encoding='utf-8') as f:
            f.write(content)

    @classmethod
    def start(cls):
        cls().run()


if __name__ == '__main__':
    Script.start()
