import os
import shutil
from glob import glob
from pathlib import Path

base_dir = Path(__file__).absolute().parent.parent


def main():
    # git clone git@github.com:amzn/selling-partner-api-models
    dst_dir = base_dir / 'swagger2_apis'
    dst_dir.exists() and shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)
    for directory in map(Path, glob(str(base_dir / 'selling-partner-api-models/models/*-api-model'))):
        module = directory.name.rsplit('-', maxsplit=2)[0].replace('-', '_')
        for src in map(Path, glob(str(directory / '*.json'))):
            version = src.name.replace('-', '_')
            dst = base_dir / 'swagger2_apis' / f'{module}_{version}.json'
            print(f'Moving: {src.stem}')
            shutil.copy(src, dst)


if __name__ == '__main__':
    main()
