import json
import os
import re
import shutil
import traceback
from glob import glob
from os import path

import black
import requests

from swagger_client_generator.stages import render


def test_move_to_swagger_2_apis_directory():
    path.exists('swagger2_apis') and shutil.rmtree('swagger2_apis')
    os.makedirs('swagger2_apis')
    for directory in glob(path.abspath('selling-partner-api-models/models/*-api-model')):
        module = path.split(directory)[1].rsplit('-', maxsplit=2)[0].replace('-', '_')
        for src in glob(path.join(directory, '*.json')):
            dst = path.join(path.abspath('.'), 'swagger2_apis', f'{module}.json')
            shutil.copy(src, dst)


def test_convert_to_open_api_3():
    path.exists('swagger3_apis') and shutil.rmtree('swagger3_apis')
    os.makedirs('swagger3_apis')
    for directory in glob(path.abspath('selling-partner-api-models/models/*-api-model')):
        module = path.split(directory)[1].rsplit('-', maxsplit=2)[0].replace('-', '_')
        for src in glob(path.join(directory, '*.json')):
            dir_name = path.split(directory)[1]
            file_name = path.split(src)[1]
            github_url = f'https://raw.githubusercontent.com/amzn/selling-partner-api-models' \
                         f'/main/models/{dir_name}/{file_name}'
            dst = path.join(path.abspath('.'), 'swagger3_apis', f'{module}.json')
            convert_api_url = f'https://converter.swagger.io/api/convert?url={github_url}'
            content = requests.get(convert_api_url).json()
            with open(dst, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=4)


def test_generate_clients():
    print()

    path.exists('sp_api_clients') and shutil.rmtree('sp_api_clients')
    shutil.copytree('sp_api_static', 'sp_api_clients')

    for src_path in glob('swagger3_apis/*.json'):
        module_name = path.split(path.splitext(src_path)[0])[1]
        dst_path = path.join('sp_api_clients', f'{module_name}.py')
        with open(src_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        content = render(module_name, data)
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
        with open('sp_api_clients/__init__.py', mode='a', encoding='utf-8') as f:
            f.write(f'from . import {package_name}\n')
    return


def test_upload():
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('sp_api_clients.egg-info')
