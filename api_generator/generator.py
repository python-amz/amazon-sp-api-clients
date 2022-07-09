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
from django.conf import settings
from django.shortcuts import render
from django.test import RequestFactory
from openapi_schema_pydantic.v3.v3_0_3 import OpenAPI, Operation, Reference, Parameter, RequestBody, Schema, Response, \
    MediaType, Components
from pydantic import root_validator, validator

from api_generator.utils import Utils

settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [Path(__file__).parent / 'templates']
}])
django.setup()


class ParsedSchema(Schema):
    name: str = ''
    ref_name: str = ''
    is_property: bool = False  # both class and class property use Schema, use this flag to distinguish.
    # properties: dict[str, 'ParsedSchema'] = None
    parsed_properties: Any = None

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
    @validator('properties')
    def validate_properties(cls, properties: list[Schema]):
        return properties if properties else {}

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
    param_schema: Schema

    @property
    def variable_name(self):
        return Utils.camel_to_underline(self.name)

    @property
    def parsed_description(self):
        result = f'{self.variable_name}: {self.description if self.description else "no description"}'
        return Utils.wrap_description(result, subsequent_indent=8, initial_indent=4, width=112)

    # noinspection PyMethodParameters
    @validator('param_in')
    def validate_param_in(cls, value):
        assert value in ('query', 'path', 'body')
        return value


class ParsedResponse(Response):
    status_code: str
    media_type: str
    type_hint: str = ''


class ParsedMediaType(MediaType):
    pass


class ParsedRequestBody(RequestBody):
    content: dict[str, ParsedMediaType]
    params: list[ParsedParameter] = None

    # noinspection PyMethodParameters
    @validator('required')
    def validate_required(cls, value):
        assert value is True
        return value

    # noinspection PyMethodParameters
    @validator('content')
    def validate_content(cls, value: dict[str, ParsedMediaType]):
        assert all(k == 'application/json' for k in value.keys())
        return value


class ParsedOperation(Operation):
    path: str = ''
    method: str = ''
    requestBody: ParsedRequestBody = None
    responses: dict[str, ParsedResponse]
    parameters: list[ParsedParameter] = None

    @property
    def method_name(self):
        return Utils.camel_to_underline(self.operationId)

    # noinspection PyMethodParameters
    @validator('parameters')
    def validate_parameters(cls, parameters: list[ParsedParameter]):
        known_fields = {'param_in', 'name', 'param_schema', 'description', 'required',
                        'style', 'example', 'allowEmptyValue', 'allowReserved', 'deprecated', 'explode'}  # useless
        for p in parameters:
            assert not (fields := {f for f in p.__fields_set__ if getattr(p, f) is not None} - known_fields), fields
            assert p.allowEmptyValue is p.allowReserved is p.deprecated is p.explode is False
        # Ensure that post parameters do not conflict with path and query parameters
        assert len(parameters) == len({p.name for p in parameters})
        return parameters

    # noinspection PyMethodParameters
    @validator('responses', pre=True)
    def validate_responses(cls, responses: dict[str, Response]):
        responses = {k: Response.parse_obj(v) for k, v in responses.items()}
        for status, response in responses.items():
            for name, media in response.content.items():
                known_fields = {'example'}
                name in {'application/json', 'application/hal+json'} and known_fields.add('media_type_schema')
                assert {f for f in media.__fields_set__ if getattr(media, f) is not None}.issubset(known_fields)
        # Flatten the response objects.
        responses = {f'{status} {name}': ParsedResponse.parse_obj(
            response.dict() | {'status_code': status, 'media_type': name})
            for status, response in responses.items()
            for name, media in response.content.items()
            if name in {'application/json', 'application/hal+json'}}
        return responses

    @property
    def return_value_type_hint(self):
        """The type hint of function return value."""
        result_types = ', '.join(sorted({r.type_hint for r in self.responses.values()}))
        return f'Union[{result_types}]'

    @property
    def parsed_description(self):
        return Utils.wrap_description(self.description, subsequent_indent=0, initial_indent=0, width=112)


class ParsedComponents(Components):
    schemas: dict[str, ParsedSchema] = None

    # noinspection PyMethodParameters
    @validator('schemas')
    def validate_schemas(cls, schemas: dict[str, ParsedSchema]):
        expanded = list(chain.from_iterable(Utils.find_new_schema(k, v) for k, v in schemas.items()))
        names = [k for k, v in expanded]
        assert set(schemas).issubset(set(names)), 'existing schemas should not be deleted'
        assert len(names) == len(set(names)), f'schema names should not conflict: {names}'
        return {k: ParsedSchema.parse_obj(v.dict() | {'name': k}) for k, v in expanded}


class ParsedOpenApi(OpenAPI):
    components: ParsedComponents = None
    operations: dict[str, ParsedOperation] = None

    # noinspection PyMethodParameters
    @validator('servers')
    def validate_servers(cls, servers: list):
        # servers are useless
        # url='https://sellingpartnerapi-na.amazon.com/' description=None variables=None
        assert len(servers) == 1
        return servers

    # noinspection PyMethodParameters
    @root_validator
    def parse_operations(cls, values):
        operations: list[ParsedOperation] = list(ParsedOperation.parse_obj(
            {'path': path, 'method': method} | getattr(item, method).dict()
        ) for path, item in values.get('paths', {}).items() for method in item.__fields_set__)
        operations = list(sorted(operations, key=lambda k: k.operationId))
        values['operations'] = {f'{o.operationId}': o for o in operations}
        return values


class Generator:
    def __init__(self, path: Path):
        """Generate a sdk client from OpenAPI json.

        Args:
            path: OpenAPI json file version 3.
        """
        self.path = path
        self.feed()

    @cached_property
    def openapi_data(self) -> ParsedOpenApi:
        with open(self.path) as f:
            data = json.load(f)
        return ParsedOpenApi.parse_obj(data)

    def feed(self):

        def resolve_ref(ref: Reference | Schema | Parameter):
            if not isinstance(ref, Reference):
                return ref
            match = re.match(r'^#/components/(.*?)/(.*?)$', ref.ref)
            category, name = match.group(1, 2)
            selected = [i for i in self.openapi_data.components.schemas.values() if i.name == name]
            if not selected:
                raise ValueError(f'schema not found: {category}/{name}')
            schema = selected[0]
            schema = ParsedSchema.parse_obj(schema.dict() | {'ref_name': name})
            return schema

        for schema in self.openapi_data.components.schemas.values():
            schema.parsed_properties = list(sorted((ParsedSchema.parse_obj(
                resolve_ref(obj).dict() | {'name': p, 'is_property': True}
            ) for p, obj in schema.properties.items()), key=lambda i: i.name))
        for operation in self.openapi_data.operations.values():

            for i in operation.responses.values():
                type_hint_schema = resolve_ref(i.content.get(i.media_type).media_type_schema)
                i.type_hint = Utils.get_type_hint(type_hint_schema)

            if (body := operation.requestBody) is not None:
                schemas = list(i.media_type_schema for i in body.content.values())
                assert all(isinstance(i, Reference) for i in schemas)
                schemas = list(resolve_ref(schema) for schema in schemas)
                assert all(s.type == 'object' for s in schemas)
                # TODO check the parameters
                # fields = {'required', 'properties', 'type', 'description'}
                # assert set(chain.from_iterable(s.__fields_set__ for s in schemas)).issubset(fields)
                required = tuple(chain.from_iterable(s.required for s in schemas if s.required))
                assert len(set(required)) == len(required)
                properties = tuple((name, obj) for s in schemas for name, obj in s.properties.items())
                properties = tuple((k, resolve_ref(v) if isinstance(v, Reference) else v)
                                   for k, v in properties)
                properties = tuple(sorted(properties, key=lambda i: i[0]))
                body.params = [ParsedParameter(name=k, param_in='body', description=v.description,
                                               required=k in required, param_schema=v) for k, v in properties]

            # convert post object to parameter objects, the main work of following code is data validation
            (body := operation.requestBody) is None or operation.parameters.extend(body.params)
            for parameter in operation.parameters:
                parameter.type_hint = Utils.get_type_hint(resolve_ref(parameter.param_schema))

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
