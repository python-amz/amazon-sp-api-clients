import html
import json
import multiprocessing
import re
from functools import cached_property
from itertools import chain
from pathlib import Path
from typing import Any

import black
import django.template
from django.conf import settings
from django.shortcuts import render
from django.test import RequestFactory
from openapi_schema_pydantic.v3.v3_0_3 import OpenAPI, Operation, Reference, Parameter, RequestBody, Schema, Components

settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [Path(__file__).parent / 'templates']
}])
django.setup()


class SchemaBase(Schema):
    name: str
    generator: Any

    @property
    def fields(self):
        known = {'description', 'name', 'generator', 'type', 'ref', 'enum', 'items'}
        fields = {k: getattr(self, k) for k in self.__fields_set__ - known}
        fields = {k: v for k, v in fields.items() if v is not None}
        # assert set(fields).issubset(known), fields
        if fields:
            print(fields)
        return fields

    @property
    def schema_obj(self) -> Schema:
        return self

    @property
    def type_hint(self):
        return self.generator.get_type_hint_of_schema(self.schema_obj)

    @property
    def variable_name(self):
        return re.sub('(?<=[a-z])[A-Z]+', lambda m: f'_{m.group(0).lower()}', self.name).lower()

    @property
    def parsed_description(self):
        result = 'no description.' if self.description is None else self.description
        result = result.splitlines()
        result = [line.strip() for line in result]
        result = [line for line in result if line]
        return '\n        '.join(result)


class ParsedReferenceProperty(SchemaBase, Reference):
    pass


class ParsedSchemaProperty(SchemaBase, Schema):
    pass


class ParsedSchema(SchemaBase, Schema):
    @property
    def parsed_properties(self):
        dst = self.properties
        dst = dst.items() if dst else ()
        dst = list(sorted(dst, key=lambda i: i[0]))
        return dst

    @property
    def reference_properties(self) -> list[ParsedReferenceProperty]:
        return [ParsedReferenceProperty.parse_obj({**v.dict(), 'name': k, 'generator': self.generator})
                for k, v in self.parsed_properties if isinstance(v, Reference)]

    @property
    def schema_properties(self) -> list[ParsedSchemaProperty]:
        return [ParsedSchemaProperty.parse_obj({**v.dict(), 'name': k, 'generator': self.generator})
                for k, v in self.parsed_properties if isinstance(v, Schema)]


class ParsedParameter(Parameter):
    generator: Any

    @property
    def type_hint(self):
        return self.generator.get_type_hint_of_schema(self.param_schema)

    @property
    def variable_name(self):
        return re.sub('(?<=[a-z])[A-Z]+', lambda m: f'_{m.group(0).lower()}', self.name).lower()

    @property
    def parsed_description(self):
        result = 'no description.' if self.description is None else self.description
        result = result.splitlines()
        result = [line.strip() for line in result]
        result = [line for line in result if line]
        return '\n        '.join(result)


class ParsedOperation(Operation):
    path: str
    method: str
    parsed_parameters: list[ParsedParameter] = []

    @property
    def method_name(self):
        name = re.sub('(?<=[a-z])[A-Z]+', lambda m: f'_{m.group(0).lower()}', self.operationId).lower()
        # print(f'{self.operationId:>40} | {name}')
        return name


class Generator:
    def __init__(self, path: Path):
        """Generate a sdk client from OpenAPI json.

        Args:
            path: OpenAPI json file version 3.
        """
        self.path = path

    def resolve_ref(self, ref: Reference):
        if not isinstance(ref, Reference):
            return ref
        match = re.match(r'^#/components/(.*?)/(.*?)$', ref.ref)
        category, name = match.group(1, 2)
        return getattr(self.data.components, category).get(name)

    @cached_property
    def data(self) -> OpenAPI:
        with open(self.path) as f:
            data = json.load(f)
        data = OpenAPI.parse_obj(data)

        # servers is useless
        # url='https://sellingpartnerapi-na.amazon.com/' description=None variables=None
        assert len(data.servers) == 1

        return data

    @cached_property
    def components(self) -> Components:
        return self.data.components

    @cached_property
    def schemas(self) -> list[ParsedSchema]:
        src = self.components.schemas
        src = {k: v for k, v in src.items() if isinstance(v, Schema)}
        dst: list[ParsedSchema] = [ParsedSchema.parse_obj({**v.dict(), 'name': k, 'generator': self})
                                   for k, v in src.items()]
        dst.sort(key=lambda i: i.name)
        return dst

    @cached_property
    def references(self) -> dict[str, Reference]:
        src = self.components.schemas
        dst = {k: v for k, v in src.items() if isinstance(v, Reference)}
        return dst

    def get_type_hint_of_schema(self, schema: Schema):
        # recursively get inline type hint of a schema
        if isinstance(schema, Reference):
            assert (match := re.match(r'^#/components/(.*?)/(.*?)$', schema.ref))
            name = match.group(2)
            return f"'{name}'"
        schema = self.resolve_ref(schema) if isinstance(schema, Reference) else schema
        if schema is None or (schema.type is None and schema.items is None):
            return 'Any'
        base_type_convert = {'string': 'str', 'integer': 'int', 'boolean': 'bool', 'number': 'Union[float, int]'}
        child = self.get_type_hint_of_schema(schema.items) if schema.type in ('object', 'array') else 'Any'
        type_convert = {**base_type_convert, 'array': f'list[{child}]', 'object': f'dict[str, {child}]'}
        type_hint = type_convert[schema.type]
        choices = ', '.join(f'Literal["{v}"]' for v in schema.enum) if schema.enum is not None else None
        type_hint = f'Union[{choices}]' if type_hint == 'str' and choices is not None else type_hint
        return type_hint

    @cached_property
    def operations(self) -> tuple[ParsedOperation, ...]:
        operations = tuple(ParsedOperation(**{'path': path, 'method': method, **getattr(path_item, method).dict()})
                           for path, path_item in self.data.paths.items()
                           for method in path_item.__fields_set__)
        operations = tuple(sorted(operations, key=lambda k: k.operationId))
        for operation in [o for o in operations if o.parameters is not None]:

            # convert post object to parameter objects, the main work of following code is data validation
            if (body := operation.requestBody) is not None:
                assert isinstance(body, RequestBody)
                assert body.required is True
                _ = body.description  # Useless, do not process
                content = body.content
                assert all(k == 'application/json' for k in content.keys())
                schemas = tuple(i.media_type_schema for i in content.values())
                assert all(isinstance(i, Reference) for i in schemas)
                schemas = tuple(self.resolve_ref(schema) for schema in schemas)
                assert all(s.type == 'object' for s in schemas)
                fields = {'required', 'properties', 'type', 'description'}
                assert set(chain(*(s.__fields_set__ for s in schemas))).issubset(fields)
                required = tuple(chain(*(s.required for s in schemas if s.required)))
                assert len(set(required)) == len(required)
                properties = tuple((name, obj) for s in schemas for name, obj in s.properties.items())
                properties = tuple((k, self.resolve_ref(v) if isinstance(v, Reference) else v) for k, v in properties)
                post_parameters = tuple(Parameter(name=k, param_in='body', description=v.description,
                                                  required=k in required, param_schema=v) for k, v in properties)
                operation.parameters.extend(post_parameters)

            params = tuple(self.resolve_ref(p) if isinstance(p, Reference) else p for p in operation.parameters)
            parsed_params: tuple[ParsedParameter, ...] = tuple(ParsedParameter.parse_obj(
                {**p.dict(), 'generator': self}) for p in params)
            operation.parsed_parameters = parsed_params

            # Ensure that post parameters do not conflict with path and query parameters
            assert len(operation.parsed_parameters) == len({p.name for p in operation.parsed_parameters})

        # Currently, there is no parameter in header or cookie
        assert all(p.param_in in ('query', 'path', 'body') for o in operations for p in o.parsed_parameters)
        return operations

    @cached_property
    def content(self):
        content = render(RequestFactory(), 'api.html', {'data': self}).content.decode('utf-8')
        return self.format_python_file(content)

    @staticmethod
    def format_python_file(content: str):
        content = html.unescape(content)
        # content = re.sub(r'\n+', '\n', content)
        try:
            content = black.format_str(content, mode=black.Mode(line_length=120))
        except black.parsing.InvalidInput:
            content_with_line_number = '\n'.join(
                [f'{index + 1:>3} {line}' for index, line in enumerate(content.splitlines())])
            print(content_with_line_number)
            raise
        return content

    @cached_property
    def package_name(self):
        return self.path.stem

    @cached_property
    def class_name(self):
        return ''.join(word.capitalize() for word in self.package_name.split('_'))

    @cached_property
    def directory(self):
        return Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / 'api'

    def generate(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        with open(self.directory / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(self.directory / f'{self.package_name}.py', 'w', encoding='utf-8') as f:
            f.write(self.content)

    @classmethod
    def worker(cls, path: Path):
        obj = cls(path)
        obj.generate()
        return obj

    @classmethod
    def main(cls):
        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            generators = pool.map(cls.worker, (Path(__file__).parent.parent / 'swagger3_apis').glob('*.json'))
        [g.generate() for g in generators]
        content = render(RequestFactory(), 'init.html', {'data': generators}).content.decode('utf-8')
        content = cls.format_python_file(content)
        with open(Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / '__init__.py', 'w') as f:
            f.write(content)


def main():
    Generator.main()


if __name__ == '__main__':
    main()
