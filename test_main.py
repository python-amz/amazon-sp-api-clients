import json
import os
import re
import shutil
import traceback
from glob import glob
from os import path
from pathlib import Path

import black
import requests
from bs4 import BeautifulSoup, Tag
from jinja2 import Template

from swagger_client_generator.stages import render

base_dir = Path(__file__).absolute().parent


def test_move_to_swagger_2_apis_directory():
    # git clone git@github.com:amzn/selling-partner-api-models
    dst_dir = base_dir / 'swagger2_apis'
    dst_dir.exists() and shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)
    for directory in map(Path, glob(str(base_dir / 'selling-partner-api-models/models/*-api-model'))):
        module = directory.name.rsplit('-', maxsplit=2)[0].replace('-', '_')
        for src in map(Path, glob(str(directory / '*.json'))):
            version = src.name.replace('-', '_')
            dst = base_dir / 'swagger2_apis' / f'{module}_{version}.json'
            shutil.copy(src, dst)


def test_convert_to_open_api_3():
    dst_dir = base_dir / 'swagger3_apis'
    path.exists(dst_dir) and shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)

    for directory in map(Path, glob(str(base_dir / 'selling-partner-api-models/models/*-api-model'))):
        module = directory.name.rsplit('-', maxsplit=2)[0].replace('-', '_')
        for src in map(Path, glob(str(directory / '*.json'))):
            dir_name = path.split(directory)[1]
            file_name = path.split(src)[1]
            github_url = f'https://raw.githubusercontent.com/amzn/selling-partner-api-models' \
                         f'/main/models/{dir_name}/{file_name}'
            convert_api_url = f'https://converter.swagger.io/api/convert?url={github_url}'
            content = requests.get(convert_api_url).json()
            version = content['info']['version'].replace('-', '_')
            dst = dst_dir / f'{module}_{version}.json'
            with open(dst, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=4)


def test_get_parse_report_markdown():
    url = 'https://developer-docs.amazon.com/sp-api/docs/report-type-values'
    text = requests.get(url).text
    with open('report_types.html', 'w', encoding='utf-8') as f:
        f.write(text)


def test_parse_reports():
    with open('report_types.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html)
    print()
    groups: dict[str, dict[str, str]] = {}
    soup = soup.select_one('.content-body > .markdown-body')
    elements = soup.select('h2.heading-2, div.rdmd-table > .rdmd-table-inner > table > tbody > tr > td:first-child')
    element_groups = []
    current_element_group = []
    for e in elements:
        if e.name == 'h2':
            element_groups.append(current_element_group)
            current_element_group = [e]
        else:
            current_element_group.append(e)
    element_groups.append(current_element_group)
    element_groups.pop(0)
    for h2_element, *td_elements in element_groups:
        group_name = h2_element.text.strip().lower() \
            .replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
        group_name = re.sub(r'_+', '_', group_name)
        print()
        print(f'Group: {group_name}')
        for row in td_elements:
            row: Tag
            lines = row.text.splitlines()
            lines = [i.strip() for i in lines]
            lines = [i for i in lines if i]
            match len(lines):
                case 1:
                    line1 = lines[0]
                    # like a subtitle, just skip is ok
                    if line1 in ('FBA Sales Reports',):
                        continue
                    raise NotImplementedError(f'Unsupported line: {line1}')
                # case 2:
                #     line1, line2 = lines
                #     assert (m := re.match(r'^reportType value: ?([A-Z0-9_]+?)$', line2)), line2
                #     report_type_slug = m.group(1)
                #     assert (m := re.match(r'^([A-Za-z 0-9_:\-()&]*?)$', line1)), line1
                #     report_name = re.sub(r'[-_ :()&]+', '_', m.group(1))
                case 2 | 3 | 4:
                    line = ' '.join(lines)
                    assert (m := re.match(r'^([A-Za-z 0-9_:\-()&]*?) reportType value: ?([A-Z0-9_]+?)$', line)), line
                    report_name, report_type_slug = m.group(1, 2)
                    report_name = re.sub(r'[-_ :()&]+', '_', m.group(1))
                case other:
                    raise NotImplementedError(f'TD element with {other} lines cannot be parsed')
            report_name = report_name.lower().strip('_') \
                .removeprefix('scheduled_') \
                .removeprefix('requested_or_scheduled_') \
                .replace('_report_', '_') \
                .removesuffix('_report')
            print(f'{report_name:>60} {report_type_slug}')
            groups.setdefault(group_name, {}).setdefault(report_name, report_type_slug)

    template_path = Path(__file__).parent.absolute() / 'swagger_client_generator' / 'report_types.pyt'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    content = template.render(groups=groups)
    content = black.format_str(content, mode=black.Mode(line_length=120))
    for _ in range(5):
        content = content.replace('\n\n', '\n')
    content = black.format_str(content, mode=black.Mode(line_length=120))
    with open('amazon_sp_api_static/report_types.py', 'w', encoding='utf-8') as f:
        f.write(content)
    with open('amazon_sp_api_clients/report_types.py', 'w', encoding='utf-8') as f:
        f.write(content)


def test_generate_clients():
    print()

    path.exists('amazon_sp_api_clients') and shutil.rmtree('amazon_sp_api_clients')
    shutil.copytree('amazon_sp_api_static', 'amazon_sp_api_clients')

    clients = []
    for src_path in map(Path, glob(str(base_dir / 'swagger3_apis/*.json'))):
        module_name = src_path.stem

        dst_path = path.join('amazon_sp_api_clients', f'{module_name}.py')
        with open(src_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        context, content = render(module_name, data)
        content = re.sub(r'(?=\n)\s*(?=\n)', '', content)
        try:
            content = black.format_str(content, mode=black.Mode(line_length=120))
            with open(dst_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(content)
            traceback.print_tb(e.__traceback__)
            raise
        package_name = path.split(path.splitext(src_path)[0])[1]
        clients.append({
            'package': package_name,
            'class_name': context["class_name"],
        })
    template_path = Path(__file__).parent / r'swagger_client_generator/init.pyt'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    init_content = template.render(clients=clients)
    init_content = re.sub(r'\n+', '\n', init_content)
    init_content = black.format_str(init_content, mode=black.Mode(line_length=120))

    with open('amazon_sp_api_clients/__init__.py', mode='w', encoding='utf-8') as f:
        f.write(init_content)
