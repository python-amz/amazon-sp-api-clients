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
    schema_type: str = ''

    @property
    def fields(self):
        known = {'description', 'name', 'generator', 'type', 'ref', 'enum', 'items'}
        fields = self.__fields_set__ - known
        fields = list(sorted(fields))
        fields = {k: getattr(self, k) for k in fields}
        fields = {k: v for k, v in fields.items() if v is not None}
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
        result = '' if self.description is None else self.description
        result = result.splitlines()
        result = [line.strip() for line in result]
        result = [line for line in result if line]
        return '\n        '.join(result)


class ParsedReferenceProperty(SchemaBase, Reference):
    schema_type = 'reference'


class ParsedSchemaProperty(SchemaBase, Schema):
    schema_type = 'schema'


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

    @property
    def all_properties(self) -> list[SchemaBase]:
        result: list[SchemaBase] = self.reference_properties
        result.extend(self.schema_properties)
        result.sort(key=lambda i: i.name)
        return result


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
        result = '' if self.description is None else self.description
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

    def resolve_ref(self, ref: Reference | Schema | Parameter):
        if not isinstance(ref, Reference):
            return ref
        match = re.match(r'^#/components/(.*?)/(.*?)$', ref.ref)
        category, name = match.group(1, 2)
        result = getattr(self.components, category).get(name)
        assert result is not None, f'{category}/{name}'
        return result

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
                    capitalized_sub_name = re.sub(r'^_?([a-z])', lambda s: s.group(1).upper(), sub_name)

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
        src = self.components.schemas
        src = {k: v for k, v in src.items() if isinstance(v, Schema)}
        schemas = list(src.items())
        schemas = list(chain.from_iterable(self._find_new_schema(k, v) for k, v in schemas))
        schema_names = [k for k, v in schemas]
        assert set(src).issubset(set(schema_names)), 'existing schemas should not be deleted'
        assert len(schema_names) == len(set(schema_names)), f'schema names should not conflict: {schema_names}'
        self.components.schemas = dict(schemas)

        values = [v.dict() | {'name': k, 'generator': self} for k, v in schemas]
        dst: list[ParsedSchema] = [ParsedSchema.parse_obj(v) for v in values]
        dst.sort(key=lambda i: i.name)
        return dst

    @cached_property
    def references(self) -> dict[str, Reference]:
        src = self.components.schemas
        dst = {k: v for k, v in src.items() if isinstance(v, Reference)}
        return dst

    def get_type_hint_of_schema(self, schema: Schema):
        # recursively get inline type hint of a schema

        if schema is None:
            return 'Any'

        # for ``Reference`` components, which will be created as dataclasses, the type is itself.
        if isinstance(schema, Reference):
            assert (match := re.match(r'^#/components/(.*?)/(.*?)$', schema.ref))
            name = match.group(2)
            return f"'{name}'"

        assert schema.type is not None
        probable_fields = {'generator', 'type', 'description', 'name', 'enum', 'maximum', 'minimum', 'items',
                           'minItems', 'maxItems', 'pattern', 'default', 'required', 'minLength', 'maxLength',
                           'uniqueItems', 'example',
                           'schema_format', 'properties', 'additionalProperties'}
        fields = {f for f in schema.__fields_set__ if getattr(schema, f) is not None}
        assert fields.issubset(probable_fields), fields - probable_fields

        child = self.get_type_hint_of_schema(schema.items) if schema.type in ('object', 'array') else 'Any'

        type_convert = {
            ('integer', None): 'int',
            ('string', None): 'str',
            ('boolean', None): 'bool',
            ('object', None): f'Dict[str, {child}]',
            ('array', None): f'List[{child}]',
            ('number', None): 'float',
            ('string', 'date-time'): 'datetime',
            ('string', 'date'): 'date',
            ('string', 'boolean'): 'bool',
            ('string', 'uri'): 'str',
            ('string', '[A-Z]{2}'): 'str',
            ('string', 'byte'): 'bytes',
            ('integer', 'int32'): 'int',
            ('integer', 'int64'): 'int',
            ('number', 'double'): 'float',
        }
        type_hint = type_convert[(schema.type, schema.schema_format)]

        # make string enum like Literal["v1"]
        assert schema.enum is None or type_hint == 'str'
        choices = ', '.join(f'Literal["{v}"]' for v in schema.enum) if schema.enum is not None else None
        type_hint = f'Union[{choices}]' if type_hint == 'str' and choices is not None else type_hint

        return type_hint

    @cached_property
    def operations(self) -> tuple[ParsedOperation, ...]:
        operations = tuple(ParsedOperation.parse_obj({'path': path, 'method': method} | getattr(item, method).dict())
                           for path, item in self.data.paths.items() for method in item.__fields_set__)
        operations = tuple(sorted(operations, key=lambda k: k.operationId))
        for operation in [o for o in operations if o.parameters is not None or o.requestBody is not None]:
            params_or_refs = [] if (v := operation.parameters) is None else v
            params: list[Parameter] = [self.resolve_ref(p) for p in params_or_refs]
            assert all(isinstance(p, Parameter) for p in params)
            known = {'param_in', 'name', 'param_schema', 'description', 'required',
                     'style', 'example', 'allowEmptyValue', 'allowReserved', 'deprecated', 'explode'}  # useless
            for p in params:
                assert not (fields := {f for f in p.__fields_set__ if getattr(p, f) is not None} - known), fields
                assert p.allowEmptyValue is p.allowReserved is p.deprecated is p.explode is False

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
                assert set(chain.from_iterable(s.__fields_set__ for s in schemas)).issubset(fields)
                required = tuple(chain.from_iterable(s.required for s in schemas if s.required))
                assert len(set(required)) == len(required)
                properties = tuple((name, obj) for s in schemas for name, obj in s.properties.items())
                properties = tuple((k, self.resolve_ref(v) if isinstance(v, Reference) else v) for k, v in properties)
                properties = tuple(sorted(properties, key=lambda i: i[0]))
                params.extend([Parameter(name=k, param_in='body', description=v.description,
                                         required=k in required, param_schema=v) for k, v in properties])

            assert all(isinstance(p.param_schema, Schema) for p in params)
            operation.parameters = params
            parsed_params: list[ParsedParameter] = [ParsedParameter.parse_obj(
                p.dict() | {'generator': self}) for p in params]
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

        init_content = ''
        with open(self.directory / '__init__.py', 'w+', encoding='utf-8') as f:
            existing_content = f.read()
            init_content != existing_content and f.write(init_content)
        with open(self.directory / f'{self.package_name}.py', 'w+', encoding='utf-8') as f:
            existing_content = f.read()
            self.content != existing_content and f.write(self.content)

    @classmethod
    def worker(cls, path: Path):
        obj = cls(path)
        obj.generate()
        return obj

    @classmethod
    def main(cls):
        # files = list((Path(__file__).parent.parent / 'swagger3_apis').glob('*report*21*.json'))
        files = list((Path(__file__).parent.parent / 'swagger3_apis').glob('*.json'))
        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            generators = pool.map(cls.worker, files)
        [g.generate() for g in generators]
        content = render(RequestFactory(), 'init.html', {'data': generators}).content.decode('utf-8')
        content = cls.format_python_file(content)
        with open(Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / '__init__.py', 'w') as f:
            f.write(content)


def main():
    Generator.main()


if __name__ == '__main__':
    main()
