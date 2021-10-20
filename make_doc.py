import os
import sys
from os import path
from pathlib import Path

from sphinx.application import Sphinx
from sphinx_inplace import RstGenerator
from sphinx_inplace.file_tree import PythonFileTreeNode

base_path = Path(__file__).parent


def main():
    # 在这个文件下定义了文档的具体生成细节，包括rst文件夹的位置、排除的文档等。

    source_dir = base_path / 'docs' / 'source'
    rst_root_dir = base_path / 'docs' / 'build' / 'rst'
    path.exists(rst_root_dir) or os.makedirs(rst_root_dir)
    generator = RstGenerator()
    generator.sync_directory(str(source_dir), str(rst_root_dir), rm=False)

    # 生成算法部分的文档
    py_dir = base_path / 'amazon_sp_api_clients'  # py源文件的目录
    rst_dir = rst_root_dir / 'amazon_sp_api_clients'  # 根据py生成的rst文件的目录
    exclude_dir = [py_dir / p for p in tuple()]
    node = PythonFileTreeNode(str(py_dir), exclude_dir)
    generator.generate_python_package_files(node, str(rst_dir), 'amazon_sp_api_clients')
    output_dir = Path(base_path / 'docs' / 'build' / 'html')

    app = Sphinx(
        srcdir=str(rst_root_dir),
        confdir=str(rst_root_dir),
        outdir=str(output_dir),
        doctreedir=str(base_path / 'docs' / 'build' / 'doctrees'),
        buildername='html',
        confoverrides=dict(),
        status=sys.stdout,
        warning=sys.stderr,
        freshenv=False,
        warningiserror=False,
        tags=[],
        verbosity=0,
        parallel=0,
        # parallel=multiprocessing.cpu_count(),
        keep_going=True)
    app.build()


if __name__ == '__main__':
    main()
