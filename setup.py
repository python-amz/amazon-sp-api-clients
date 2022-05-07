import setuptools

import amazon_sp_api_clients_2

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amazon-sp-api-clients",
    version=amazon_sp_api_clients_2.version,
    author=amazon_sp_api_clients_2.author,
    author_email=amazon_sp_api_clients_2.author_email,
    description=amazon_sp_api_clients_2.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=amazon_sp_api_clients_2.url,
    packages=['amazon_sp_api_clients'],
    install_requires=[
        'peewee',
        'cachetools',
        'requests',
        'boto3',
        'pycryptodome',
        'chardet',
        'attrs',
        'cattrs',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
