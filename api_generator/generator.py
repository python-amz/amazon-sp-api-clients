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

    @property
    def parsed_properties(self):
        return list(sorted((ParsedSchema.parse_obj(
            obj.dict() | {'name': p, 'is_property': True}
        ) for p, obj in self.properties.items()), key=lambda i: i.name))

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
    def validate_properties(cls, properties: dict[str, Schema]):
        if properties is None:
            properties = {}
        return properties

    @property
    def attrs_config(self):
        data = {}
        for p in self.parsed_properties:
            value = (p.variable_name, p.type)
            data.setdefault(p.name, value)
        # pprint(data)
        return json.dumps(data)


class ParsedParameter(Parameter):
    param_schema: Schema

    @property
    def type_hint(self):
        return Utils.get_type_hint(self.param_schema)

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

    @property
    def type_hint(self):
        return Utils.get_type_hint(self.content.get(self.media_type).media_type_schema)


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
        schemas = {k: ParsedSchema.parse_obj(v.dict() | {'name': k}) for k, v in expanded}

        for schema in schemas.values():
            for property_name, property_obj in schema.properties.items():
                if isinstance(property_obj, Reference):
                    name = re.match(r'^#/components/schemas/(.*?)$', property_obj.ref).group(1)
                    property_obj = schemas[name]
                    assert property_obj.ref_name in (None, '', name)  # Schema ref name should not change.
                    property_obj.ref_name = name
                    schema.properties[property_name] = property_obj

        return schemas


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
        components: ParsedComponents = values.get('components', ParsedComponents.parse_obj({}))

        operations = list(ParsedOperation.parse_obj(
            {'path': path, 'method': method} | getattr(item, method).dict()
        ) for path, item in values.get('paths', {}).items() for method in item.__fields_set__)
        operations = list(sorted(operations, key=lambda k: k.operationId))
        operations = {f'{o.operationId}': o for o in operations}
        values['operations'] = operations

        available_schemas: dict[str, ParsedSchema] = {s.name: s for s in components.schemas.values()}

        def resolve_ref(ref: Reference | Schema | Parameter):
            if not isinstance(ref, Reference):
                return ref
            name = re.match(r'^#/components/schemas/(.*?)$', ref.ref).group(1)
            resolved_schema = available_schemas[name]
            assert resolved_schema.ref_name in (None, '', name)  # Schema ref name should not change.
            resolved_schema.ref_name = name
            return resolved_schema

        for operation in operations.values():

            for i in operation.responses.values():
                obj = i.content.get(i.media_type)
                obj.media_type_schema = resolve_ref(obj.media_type_schema)

            if (body := operation.requestBody) is not None:
                body: ParsedRequestBody
                content = body.content
                for i in content.values():
                    i.media_type_schema = resolve_ref(i.media_type_schema)
                schemas = list(i.media_type_schema for i in body.content.values())
                body.params = []
                for media_type in schemas:
                    assert media_type.type == 'object'
                    # TODO check the parameters
                    # fields = {'required', 'properties', 'type', 'description'}
                    # assert set(chain.from_iterable(s.__fields_set__ for s in schemas)).issubset(fields)
                    for name, obj in media_type.properties.items():
                        obj = resolve_ref(obj) if isinstance(obj, Reference) else obj
                        body.params.append(ParsedParameter(
                            name=name,
                            param_in='body',
                            description=obj.description,
                            required=name in media_type.required,
                            param_schema=obj,
                        ))
                body.params.sort(key=lambda i: i.name)

            # convert post object to parameter objects, the main work of following code is data validation
            (body := operation.requestBody) is None or operation.parameters.extend(body.params)
            for parameter in operation.parameters:
                parameter.param_schema = resolve_ref(parameter.param_schema)

        return values


class Generator:
    def __init__(self, path: Path):
        """Generate a sdk client from OpenAPI json.

        Args:
            path: OpenAPI json file version 3.
        """
        self.path = path

    @cached_property
    def openapi_data(self) -> ParsedOpenApi:
        with open(self.path) as f:
            data = json.load(f)
        return ParsedOpenApi.parse_obj(data)

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
