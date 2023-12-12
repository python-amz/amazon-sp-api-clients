import json
import os
import shutil
from glob import glob
from os import path
from pathlib import Path

import requests

base_dir = Path(__file__).absolute().parent.parent


def main():
    dst_dir = base_dir / 'swagger3_apis'
    path.exists(dst_dir) and shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)

    for directory in map(Path, glob(str(base_dir / 'selling-partner-api-models/models/*-api-model'))):
        module = directory.name.rsplit('-', maxsplit=2)[0].replace('-', '_')
        for src in map(Path, glob(str(directory / '*.json'))):
            print(f'Converting: {src.stem}')
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


if __name__ == '__main__':
    main()
