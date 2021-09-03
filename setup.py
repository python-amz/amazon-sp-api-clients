import setuptools

import amazon_sp_api_clients

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amazon-sp-api-clients",
    version=amazon_sp_api_clients.version,
    author=amazon_sp_api_clients.author,
    author_email=amazon_sp_api_clients.author_email,
    description=amazon_sp_api_clients.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=amazon_sp_api_clients.url,
    packages=['amazon_sp_api_clients'],
    install_requires=[
        'peewee',
        'cachetools',
        'requests',
        'boto3',
        'pycryptodome',
        'demjson',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
