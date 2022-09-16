import json
import re
import shutil
import traceback
from glob import glob
from os import path
from pathlib import Path

import black
from jinja2 import Template

from swagger_client_generator.stages import render

base_dir = Path(__file__).absolute().parent


def main():
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


if __name__ == '__main__':
    main()
