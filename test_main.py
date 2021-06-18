import json
import os
import re
import shutil
import traceback
from glob import glob
from os import path
from pathlib import Path
from pprint import pprint

import black
import requests
from bs4 import BeautifulSoup, Tag
from jinja2 import Template
from markdown import markdown

from swagger_client_generator.stages import render

base_dir = Path(__file__).absolute().parent


def test_move_to_swagger_2_apis_directory():
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
    url = 'https://raw.githubusercontent.com/amzn/selling-partner-api-docs/main' \
          '/references/reports-api/reportType_string_array_values.md'
    text = requests.get(url).text
    with open('report_types.md', 'w', encoding='utf-8') as f:
        f.write(text)


def test_parse_reports():
    with open('report_types.md', 'r', encoding='utf-8') as f:
        text = f.read()
    html = markdown(text)
    soup = BeautifulSoup(html)
    print()
    groups: dict[str, dict[str, str]] = {}
    for i in soup.select('h2'):
        i: Tag
        group_name = i.text.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
        group_name = re.sub(r'_+', '_', group_name)

        for row in i.find_next('table').select('tr td:first-child'):
            row: Tag
            lines = row.text.splitlines()
            if len(lines) == 1:
                continue
            report_name = lines[0]
            if lines[-1].startswith('reportType value: '):
                report_type_slug = lines[-1].split('reportType value: ', maxsplit=1)[1]
            elif lines[-2] == 'reportType value:':
                report_type_slug = lines[-1]
            else:
                raise
            report_name = report_name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
            report_name = re.sub(r'_+', '_', report_name)

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
    with open('amazon_sp_api_clients/__init__.py', mode='r', encoding='utf-8') as f:
        init_lines = f.readlines()
    for src_path in map(Path, glob(str(base_dir / 'swagger3_apis/*.json'))):
        module_name = src_path.stem

        # usually debug a single client, so skip others to speed up
        # if 'feed' not in module_name:
        #     continue

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

        init_lines.insert(0, f'from .{package_name} import {context["class_name"]}Client\n')
    init_content = ''.join(init_lines)
    init_content = black.format_str(init_content, mode=black.Mode(line_length=120))
    with open('amazon_sp_api_clients/__init__.py', mode='w', encoding='utf-8') as f:
        f.write(init_content)


def test_upload():
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('amazon_sp_api_clients.egg-info')
