"""
The parsing process follows the following two steps:
1. Build the pydantic hierarchy according to the parsing order;
2. Assign the parser to each object in turn to optimize the parsing process, including converting each reference into a
schema and other processes.
"""

import json
import multiprocessing
import re
from functools import cached_property
from itertools import chain
from pathlib import Path
from typing import Any

import django.template
import pydantic
from django.conf import settings
from django.shortcuts import render
from django.test import RequestFactory
from openapi_schema_pydantic.v3.v3_0_3 import OpenAPI, Operation, Reference, Parameter, RequestBody, Schema, Response, \
    MediaType

from api_generator.utils import Utils

settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [Path(__file__).parent / 'templates']
}])
django.setup()


class ParsedSchema(Schema):
    name: str
    ref_name: str = ''
    is_property: bool = False  # both class and class property use Schema, use this flag to distinguish.

    @property
    def extra_fields(self):
        known = {'description', 'name', 'generator', 'type', 'ref', 'enum', 'items', 'properties', 'required',
                 'ref_name', 'is_property', 'parsed_properties'}
        fields = self.__fields_set__ - known
        fields = list(sorted(fields))
        fields = {k: getattr(self, k) for k in fields}
        fields = {k: v for k, v in fields.items() if v is not None}
        return fields

    @property
    def type_hint(self):
        return Utils.get_type_hint(self)

    @property
    def variable_name(self):
        return Utils.camel_to_underline(self.name)

    @property
    def parsed_description(self):
        result = self.description if self.description else ''
        result = self.items.description if not result and self.items and self.items.description else result
        return Utils.wrap_description(result, subsequent_indent=4, initial_indent=4, width=120)

    @property
    def is_list(self):
        return self.type == 'array'

    @property
    def is_dict(self):
        return self.type == 'object'

    # noinspection PyMethodParameters
    @pydantic.validator('properties')
    def validate_properties(cls, properties: list[Schema]):
        return properties

    parsed_properties: Any = None

    def feed(self, generator: 'Generator'):
        parsed = self.properties
        parsed = parsed.items() if parsed else ()
        parsed = list(sorted(parsed, key=lambda i: i[0]))
        result = []
        for k, src in parsed:
            dst = generator.resolve_ref(src) if isinstance(src, Reference) else src
            dst = ParsedSchema.parse_obj(dst.dict() | {'name': k, 'is_property': True})
            dst.feed(generator)
            result.append(dst)
        result.sort(key=lambda i: i.name)
        self.parsed_properties = result

    @property
    def attrs_config(self):
        data = {}
        for p in self.parsed_properties:
            value = (p.variable_name, p.type)
            data.setdefault(p.name, value)
        # pprint(data)
        return json.dumps(data)


class ParsedParameter(Parameter):
    type_hint: str = ''

    @property
    def variable_name(self):
        return Utils.camel_to_underline(self.name)

    @property
    def parsed_description(self):
        result = f'{self.variable_name}: {self.description if self.description else "no description"}'
        return Utils.wrap_description(result, subsequent_indent=8, initial_indent=4, width=112)

    def feed(self, generator: 'Generator'):
        self.type_hint = Utils.get_type_hint(generator.resolve_ref(self.param_schema))

    # noinspection PyMethodParameters
    @pydantic.validator('param_in')
    def validate_param_in(cls, value):
        assert value in ('query', 'path', 'body')
        return value


class ParsedResponse(Response):
    status_code: str
    media_type: str
    type_hint: str = ''

    def feed(self, generator: 'Generator'):
        type_hint_schema = generator.resolve_ref(self.content.get(self.media_type).media_type_schema)
        self.type_hint = Utils.get_type_hint(type_hint_schema)


class ParsedMediaType(MediaType):
    pass


class ParsedRequestBody(RequestBody):
    content: dict[str, ParsedMediaType]

    # noinspection PyMethodParameters
    @pydantic.validator('required')
    def validate_required(cls, value):
        assert value is True
        return value

    # noinspection PyMethodParameters
    @pydantic.validator('content')
    def validate_content(cls, value: dict[str, ParsedMediaType]):
        assert all(k == 'application/json' for k in value.keys())
        return value

    def feed(self, generator: 'Generator'):
        schemas = list(i.media_type_schema for i in self.content.values())
        assert all(isinstance(i, Reference) for i in schemas)
        schemas = list(generator.resolve_ref(schema) for schema in schemas)
        assert all(s.type == 'object' for s in schemas)
        # TODO check the parameters
        # fields = {'required', 'properties', 'type', 'description'}
        # assert set(chain.from_iterable(s.__fields_set__ for s in schemas)).issubset(fields)
        required = tuple(chain.from_iterable(s.required for s in schemas if s.required))
        assert len(set(required)) == len(required)
        properties = tuple((name, obj) for s in schemas for name, obj in s.properties.items())
        properties = tuple((k, generator.resolve_ref(v) if isinstance(v, Reference) else v)
                           for k, v in properties)
        properties = tuple(sorted(properties, key=lambda i: i[0]))
        self.params = [ParsedParameter(name=k, param_in='body', description=v.description,
                                       required=k in required, param_schema=v) for k, v in properties]

    params: list[ParsedParameter] = None


class ParsedOperation(Operation):
    path: str
    method: str
    requestBody: ParsedRequestBody = None
    responses: dict[str, ParsedResponse]
    parsed_parameters: list[ParsedParameter] = None

    @property
    def method_name(self):
        return Utils.camel_to_underline(self.operationId)

    # noinspection PyMethodParameters
    @pydantic.validator('responses', pre=True)
    def validate_responses(cls, responses: dict[str, Response]):
        responses = {k: Response.parse_obj(v) for k, v in responses.items()}
        assert all({f for f in media.__fields_set__ if getattr(media, f) is not None}.issubset(
            {'example', 'media_type_schema'} if name in {'application/json', 'application/hal+json'} else {'example'})
                   for status, response in responses.items()
                   for name, media in response.content.items())
        response = ((status, name, response)
                    for status, response in responses.items()
                    for name, media in response.content.items()
                    if name in {'application/json', 'application/hal+json'})
        parsed = {f'{status} {name}': ParsedResponse.parse_obj(response.dict() | {
            'status_code': status,
            'media_type': name,
        })
                  for status, name, response in response}
        return parsed

    def feed(self, generator: 'Generator'):
        for i in self.responses.values():
            i.feed(generator)
        if (body := self.requestBody) is not None:
            body.feed(generator)

        params_or_refs = [] if (v := self.parameters) is None else v
        params: list[Parameter] = [generator.resolve_ref(p) for p in params_or_refs]
        assert all(isinstance(p, Parameter) for p in params)

        known = {'param_in', 'name', 'param_schema', 'description', 'required',
                 'style', 'example', 'allowEmptyValue', 'allowReserved', 'deprecated', 'explode'}  # useless
        for p in params:
            assert not (fields := {f for f in p.__fields_set__ if getattr(p, f) is not None} - known), fields
            assert p.allowEmptyValue is p.allowReserved is p.deprecated is p.explode is False

        # convert post object to parameter objects, the main work of following code is data validation
        if (body := self.requestBody) is not None:
            params.extend(body.params)

        assert all(isinstance(p.param_schema, Schema) for p in params)
        parsed_params: list[ParsedParameter] = [ParsedParameter.parse_obj(p.dict()) for p in params]
        [i.feed(generator) for i in parsed_params]

        # Ensure that post parameters do not conflict with path and query parameters
        assert len(parsed_params) == len({p.name for p in parsed_params})

        self.parsed_parameters = parsed_params

    @property
    def parsed_responses(self) -> list[ParsedResponse]:
        return list(self.responses.values())

    @property
    def result_type(self):
        """The type hint of function return value."""
        result_types = {r.type_hint for r in self.parsed_responses}
        result_types = list(sorted(result_types))
        result_types = ', '.join(result_types)
        return f'Union[{result_types}]'

    @property
    def parsed_description(self):
        return Utils.wrap_description(self.description, subsequent_indent=0, initial_indent=0, width=112)


class OpenApi(OpenAPI):
    # noinspection PyMethodParameters
    @pydantic.validator('servers')
    def validate_servers(cls, servers: list):
        # servers are useless
        # url='https://sellingpartnerapi-na.amazon.com/' description=None variables=None
        assert len(servers) == 1
        return servers


class Generator:
    def __init__(self, path: Path):
        """Generate a sdk client from OpenAPI json.

        Args:
            path: OpenAPI json file version 3.
        """
        self.path = path

    def resolve_ref(self, ref: Reference | Schema | Parameter):
        if not isinstance(ref, Reference):
            return ref
        match = re.match(r'^#/components/(.*?)/(.*?)$', ref.ref)
        category, name = match.group(1, 2)
        selected = [i for i in self.schemas if i.name == name]
        if not selected:
            raise ValueError(f'schema not found: {category}/{name}')
        schema = selected[0]
        schema = ParsedSchema.parse_obj(schema.dict() | {'ref_name': name})
        schema.feed(self)
        return schema

    @cached_property
    def openapi_data(self) -> OpenAPI:
        with open(self.path) as f:
            data = json.load(f)
        return OpenAPI.parse_obj(data)

    def _find_new_schema(self, name: str, schema: Schema | Reference | Parameter) -> list[tuple[str, Schema]]:
        """Find inline schemas, which are not able to convert in python.

        Python type hint for dict do not support inline type hint.
        This method will find the inline schemas and convert to reference, which will be created as classes.

        Args:
            name: the name of the new schema, will be rendered as the class name
            schema: the inline schema

        Returns:
            Like the input arguments, but as a list.
            The first of the tuple is the path of the inline schema, including parent path,
            like ``offer.price.unit``.

        """
        fields = schema.__fields_set__
        fields = {f for f in fields if getattr(schema, f) is not None}
        new_schemas: list[tuple[str, Schema]] = [(name, schema)]
        if isinstance(schema, Schema):
            fields -= {'type', 'description', 'required', 'properties', 'minLength', 'maxLength', 'enum', 'items',
                       'allOf', 'additionalProperties', 'schema_format', 'maxItems', 'minItems', 'minimum', 'maximum',
                       'example', 'pattern'}
            assert not fields

            # additional properties only contains simple types, do not need to convert
            if (additional := schema.additionalProperties) is not None:
                assert isinstance(additional, (Schema, Reference))
                if isinstance(additional, Schema):
                    assert additional.__fields_set__.issubset({'type'})

            simple_types = 'string', 'integer', 'boolean', 'number'
            if schema.properties:
                for sub_name, sub_schema in schema.properties.items():
                    if isinstance(sub_schema, Reference):
                        continue
                    assert isinstance(sub_schema, Schema)
                    if sub_schema.type in simple_types:
                        continue
                    assert sub_schema.type in ('object', 'array')
                    capitalized_sub_name = Utils.camel_to_class_name(sub_name)

                    if sub_schema.type == 'object':
                        new_schema_name = f'{name}{capitalized_sub_name}'
                        schema.properties[sub_name] = Reference(ref=f"#/components/schemas/{new_schema_name}")
                        new_schemas.extend(self._find_new_schema(new_schema_name, sub_schema))

                    if sub_schema.type == 'array':
                        item = sub_schema.items
                        if isinstance(item, Reference):
                            continue
                        assert isinstance(item, Schema)
                        if item.type in simple_types:
                            continue
                        assert item.type == 'object', item.type
                        new_schema_name = f'{name}{capitalized_sub_name}Item'
                        sub_schema.items = Reference(ref=f"#/components/schemas/{new_schema_name}")
                        new_schemas.extend(self._find_new_schema(new_schema_name, item))

            if item := schema.items:
                assert isinstance(item, (Reference, Schema))
                if isinstance(item, Schema):
                    known = {'type', 'maxLength', 'enum', 'description', 'properties'}
                    assert not (v := item.__fields_set__ - known), v
                    assert item.type in ('string', 'object')
                    if item.type == 'object':
                        assert item.properties is not None
                        new_schema_name = f'{name}Item'
                        schema.items = Reference(ref=f"#/components/schemas/{new_schema_name}")
                        new_schemas.extend(self._find_new_schema(new_schema_name, item))

        elif isinstance(schema, Reference):
            pass
        else:
            raise ValueError(f'Not supported: {type(schema)}')
        return new_schemas

    @cached_property
    def schemas(self) -> list[ParsedSchema]:
        src = self.openapi_data.components.schemas
        src = {k: v for k, v in src.items() if isinstance(v, Schema)}
        schemas = list(src.items())
        schemas = list(chain.from_iterable(self._find_new_schema(k, v) for k, v in schemas))
        schema_names = [k for k, v in schemas]
        assert set(src).issubset(set(schema_names)), 'existing schemas should not be deleted'
        assert len(schema_names) == len(set(schema_names)), f'schema names should not conflict: {schema_names}'
        self.openapi_data.components.schemas = dict(schemas)

        values = [v.dict() | {'name': k} for k, v in schemas]
        dst: list[ParsedSchema] = [ParsedSchema.parse_obj(v) for v in values]
        dst.sort(key=lambda i: i.name)
        return dst

    def feed(self):
        for i in self.schemas:
            i.feed(self)

    @cached_property
    def operations(self) -> list['ParsedOperation']:
        operations: list[ParsedOperation] = list(ParsedOperation.parse_obj(
            {'path': path, 'method': method} | getattr(item, method).dict()
        ) for path, item in self.openapi_data.paths.items() for method in item.__fields_set__)
        [i.feed(self) for i in operations]
        operations = list(sorted(operations, key=lambda k: k.operationId))
        return operations

    @cached_property
    def package_name(self):
        return self.path.stem

    @cached_property
    def class_name(self):
        return Utils.underline_to_class_name(self.package_name)

    def generate(self):
        directory = Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / 'api'
        directory.mkdir(parents=True, exist_ok=True)
        init_content = ''
        with open(directory / '__init__.py', 'w+', encoding='utf-8') as f:
            existing_content = f.read()
            init_content != existing_content and f.write(init_content)
        content = render(RequestFactory(), 'api.html', {'data': self}).content.decode('utf-8')
        content = Utils.format_python_file(content)
        with open(directory / f'{self.package_name}.py', 'w+', encoding='utf-8') as f:
            existing_content = f.read()
            content != existing_content and f.write(content)

    @classmethod
    def worker(cls, path: Path):
        obj = cls(path)
        obj.feed()
        obj.generate()
        return obj

    @classmethod
    def main(cls):
        debug = True
        glob_pattern = 'order*.json' if debug else '*.json'
        files = list((Path(__file__).parent.parent / 'swagger3_apis').glob(glob_pattern))
        if debug:
            generators = [cls.worker(f) for f in files]
        else:
            with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
                generators = pool.map(cls.worker, files)
        [g.generate() for g in generators]
        content = render(RequestFactory(), 'init.html', {'data': generators}).content.decode('utf-8')
        content = Utils.format_python_file(content)
        with open(Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / '__init__.py', 'w') as f:
            f.write(content)
