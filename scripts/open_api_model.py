import json
import pathlib
from dataclasses import dataclass
from typing import Optional


@dataclass
class Base:
    pass

    @classmethod
    def parse(cls, *args, **kwargs):
        raise NotImplementedError


@dataclass
class Info(Base):
    title: str
    description: str
    version: str
    contact_name: str
    contact_url: str
    license_name: str
    license_url: str

    @classmethod
    def parse(cls, data: dict):
        title = data.pop('title')
        assert isinstance(title, str)
        description = data.pop('description')
        assert isinstance(description, str)
        version = data.pop('version')
        assert isinstance(version, str)

        contact: dict = data.pop('contact')
        contact_name = contact.pop('name')
        assert isinstance(contact_name, str)
        contact_url = contact.pop('url')
        assert isinstance(contact_url, str)
        assert not contact, contact

        license: dict = data.pop('license')
        license_name = license.pop('name')
        assert isinstance(license_name, str)
        license_url = license.pop('url')
        assert isinstance(license_url, str)
        assert not license, license

        assert not data, data
        return cls(title, description, version, contact_name, contact_url, license_name, license_url)


@dataclass
class Server(Base):
    url: str

    @classmethod
    def parse(cls, data: dict):
        url = data.pop('url')
        assert isinstance(url, str)

        assert not data, data
        return cls(url)


def assert_only(data: dict, key: str):
    assert isinstance(data, dict)
    assert len(data) == 1, data.keys()
    assert list(data.keys())[0] == key
    return list(data.values())[0]


@dataclass
class Parameter(Base):
    name: str
    location: str
    description: str
    schema_type: str
    schema_items_type: Optional[str]
    style: Optional[str]
    explode: Optional[bool]
    max_items: Optional[int]
    required: Optional[bool]

    @classmethod
    def parse(cls, data: dict):
        name = data.pop('name')
        assert isinstance(name, str)
        location = data.pop('in')
        assert isinstance(location, str)
        description = data.pop('description')
        assert isinstance(description, str)
        style = data.pop('style', None)
        assert isinstance(style, str | None)
        explode = data.pop('explode', None)
        assert isinstance(explode, bool | None)
        required = data.pop('required', None)
        assert isinstance(required, bool | None), type(required)

        schema = data.pop('schema')
        assert isinstance(schema, dict)
        schema_type = schema.pop('type')
        assert isinstance(schema_type, str)
        schema_items = schema.pop('items', {})
        assert isinstance(schema_items, dict)
        schema_items_type = schema_items.pop('type', None)
        assert isinstance(schema_items_type, str | None)
        assert not schema_items, schema_items
        max_items = schema.pop('maxItems', None)
        assert isinstance(max_items, int | None)
        assert not schema, schema

        assert not data, data
        return cls(name, location, description, schema_type, schema_items_type, style, explode, max_items, required)


@dataclass
class ResponseHeader(Base):
    name: str
    description: str
    schema_type: str

    @classmethod
    def parse(cls, name: str, data: dict):
        assert isinstance(name, str)
        assert isinstance(data, dict)

        description = data.pop('description')
        assert isinstance(description, str)

        schema = data.pop('schema')
        assert isinstance(schema, dict)
        schema_type = schema.pop('type')
        assert isinstance(schema_type, str)
        assert not schema, schema

        assert not data, data
        return cls(name, description, schema_type)


@dataclass
class ResponseContent(Base):
    schema_ref: Optional[str]
    example: dict  # not processed

    @classmethod
    def parse(cls, name: str, data: dict):
        assert isinstance(name, str)
        assert isinstance(data, dict)

        schema: dict = data.pop('schema', None)
        assert isinstance(schema, dict | None)
        if schema is None:
            schema_ref = None
        else:
            schema_ref = schema.pop('$ref')
            assert isinstance(schema_ref, str)
            assert not schema, schema

        example: dict = data.pop('example', {})
        assert isinstance(example, dict)

        assert not data, data
        return cls(schema_ref, example)


@dataclass
class Response(Base):
    status_code: str
    description: str
    headers: list[ResponseHeader]
    content: list[ResponseContent]
    sandbox: dict  # not processed

    @classmethod
    def parse(cls, code: str, data: dict):
        assert isinstance(code, str)
        assert isinstance(data, dict)

        description = data.pop('description')
        assert isinstance(description, str)

        headers = data.pop('headers')
        assert isinstance(headers, dict)
        headers = [ResponseHeader.parse(k, v) for k, v in headers.items()]

        content_source = data.pop('content')
        assert isinstance(content_source, dict)
        content = [ResponseContent.parse(k, v) for k, v in content_source.items()]

        sandbox: dict = data.pop('x-amzn-api-sandbox', {})
        assert isinstance(sandbox, dict)

        assert not data, data
        return cls(code, description, headers, content, sandbox)


@dataclass
class ResponseBody(Base):
    description: str
    required: bool
    content_ref: str

    @classmethod
    def parse(cls, data: dict):
        assert isinstance(data, dict)

        description = data.pop('description')
        assert isinstance(description, str)

        required = data.pop('required')
        assert isinstance(required, bool)

        content = data.pop('content')
        content = assert_only(content, 'application/json')
        content = assert_only(content, 'schema')
        content = assert_only(content, '$ref')
        assert isinstance(content, str)

        assert not data, data
        return cls(description, required, content)


@dataclass
class Path(Base):
    path: str
    method: str
    operation: str
    description: str
    tags: list[str]
    parameters: list[Parameter]
    responses: list[Response]
    request_body: Optional[ResponseBody]
    codegen_request_body_name: Optional[str]

    @classmethod
    def parse(cls, path, method, data: dict):
        assert isinstance(path, str)

        operation_id = data.pop('operationId')
        assert isinstance(operation_id, str)

        description = data.pop('description')
        assert isinstance(description, str)

        tags = data.pop('tags')
        assert isinstance(tags, list)
        for t in tags:
            assert isinstance(t, str)

        parameters = data.pop('parameters')
        assert isinstance(parameters, list)
        parameters = [Parameter.parse(p) for p in parameters]

        responses = data.pop('responses')
        assert isinstance(responses, dict)
        responses = [Response.parse(k, v) for k, v in responses.items()]

        request_body = data.pop('requestBody', None)
        request_body = None if request_body is None else ResponseBody.parse(request_body)

        codegen_request_body_name = data.pop('x-codegen-request-body-name', None)
        assert isinstance(codegen_request_body_name, str | None)

        assert not data, data
        return cls(path, method, operation_id, description, tags, parameters, responses, request_body,
                   codegen_request_body_name)


@dataclass
class ComponentProperty(Base):
    ref: str | None
    type_name: str | None
    description: str
    enum: list[str]
    docgen_table: list  # not processed
    items_ref: str | None

    @classmethod
    def parse(cls, name: str, data: dict):
        assert isinstance(name, str)
        assert isinstance(data, dict)

        ref = data.pop('$ref', None)
        assert isinstance(ref, str | None)

        type_name = data.pop('type', None)
        assert isinstance(type_name, str | None)

        description = data.pop('description', '')
        assert isinstance(description, str)

        enum = data.pop('enum', [])
        assert isinstance(enum, list)
        for i in enum:
            assert isinstance(i, str)

        docgen_table = data.pop('x-docgen-enum-table-extension', [])
        assert isinstance(docgen_table, list), docgen_table

        items = data.pop('items', {})
        assert isinstance(items, dict)
        items_ref = items.pop('$ref', None)
        assert isinstance(items_ref, str | None)
        assert not items

        assert not data, data
        return cls(ref, type_name, description, enum, docgen_table, items_ref)


@dataclass
class Component(Base):
    name: str
    required: list[str]
    type_name: str
    properties: list[ComponentProperty]
    description: str
    enum: list[str]
    items_type: str | None
    items_properties: list[ComponentProperty]
    items_ref: str | None

    @classmethod
    def parse(cls, name: str, data: dict):
        assert isinstance(name, str)
        assert isinstance(data, dict)

        required = data.pop('required', [])
        assert isinstance(required, list)
        for i in required:
            assert isinstance(i, str)

        type_name = data.pop('type')
        assert isinstance(type_name, str)

        properties = data.pop('properties', {})
        assert isinstance(properties, dict)
        properties = [ComponentProperty.parse(k, v) for k, v in properties.items()]

        description = data.pop('description', '')
        assert isinstance(description, str)

        enum = data.pop('enum', [])
        assert isinstance(enum, list)
        for i in enum:
            assert isinstance(i, str)

        if data:
            assert_only(data, 'items')
            items = data.pop('items')
            assert isinstance(items, dict)
            items_type = items.pop('type', None)
            assert isinstance(items_type, str | None)
            items_properties_src: dict = items.pop('properties', {})
            assert isinstance(items_properties_src, dict)
            items_properties = [ComponentProperty.parse(k, v) for k, v in items_properties_src.items()]
            items_ref = items.pop('$ref', None)
            assert isinstance(items_ref, str | None)
            assert not items, items
        else:
            items_type = None
            items_properties = []
            items_ref = None

        assert not data, data
        return cls(name, required, type_name, properties, description, enum, items_type, items_properties, items_ref)


@dataclass
class OpenApi(Base):
    openapi: str
    info: Info
    servers: list[Server]
    paths: list[Path]
    components: list[Component]

    @classmethod
    def parse(cls, data: dict):
        openapi = data.pop('openapi')
        assert openapi == '3.0.1'
        info = data.pop('info')
        info = Info.parse(info)

        servers = data.pop('servers')
        assert isinstance(servers, list)
        servers = [Server.parse(s) for s in servers]

        paths = data.pop('paths')
        assert isinstance(paths, dict)
        paths = [Path.parse(k, method, data) for k, p in paths.items() for method, data in p.items()]

        components = data.pop('components')
        components = assert_only(components, 'schemas')
        assert isinstance(components, dict), components
        components = [Component.parse(n, c) for n, c in components.items()]

        assert not data
        return cls(openapi, info, servers, paths, components)


if __name__ == '__main__':
    with open(pathlib.Path(__file__).parent.parent / 'swagger3_apis' / 'orders_v0.json') as f:
        api = OpenApi.parse(json.load(f))
    print('done')
