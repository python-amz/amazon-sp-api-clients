import html
import json
import re
from functools import cached_property
from pathlib import Path
from typing import Optional

import black
import django.template
from django.conf import settings
from django.shortcuts import render
from django.test import RequestFactory
from openapi_schema_pydantic.v3.v3_0_3 import OpenAPI, Operation, Reference, Parameter, RequestBody, Schema

settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [Path(__file__).parent / 'templates']
}])
django.setup()


class ParsedParameter(Parameter):
    type_hint: Optional[str] = None

    def set_parent(self, generator: 'Generator'):
        self.type_hint = generator.get_type_hint_of_schema(self.param_schema)

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


class OperationWithName(Operation):
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
        category, name = match.group(1), match.group(2)
        if category == 'schemas':
            return self.data.components.schemas.get(name)
        elif category == 'parameters':
            return self.data.components.parameters.get(name)
        else:
            raise ValueError(category)

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
    def components(self):
        return self.data.components

    def get_type_hint_of_schema(self, schema: Schema):
        if isinstance(schema, Reference):
            schema = self.resolve_ref(schema)
        if schema is None:
            return 'Any'
        if schema.type is None:
            return 'Any'
        base_type_convert = {'string': 'str', 'integer': 'int', 'boolean': 'bool', 'number': 'Union[float, int]'}
        if schema.type in ('object', 'array'):
            child = self.get_type_hint_of_schema(schema.items)
        else:
            child = ''
        type_convert = {**base_type_convert, 'array': f'list[{child}]', 'object': f'dict[str, {child}]'}
        type_hint = type_convert[schema.type]
        if type_hint == 'str' and schema.enum is not None:
            type_hint = ', '.join(f'Literal["{v}"]' for v in schema.enum)
            type_hint = f'Union[{type_hint}]'
        return type_hint

    @cached_property
    def operations(self) -> list[OperationWithName]:
        operations = [OperationWithName(**{'path': path, 'method': method, **getattr(path_item, method).dict()})
                      for path, path_item in self.data.paths.items()
                      for method in path_item.__fields_set__]
        operations.sort(key=lambda k: k.operationId)
        for operation in [o for o in operations if o.parameters is not None]:

            if (body := operation.requestBody) is not None:
                assert isinstance(body, RequestBody)
                assert body.required is True
                _ = body.description  # Useless, do not process
                for media_type, item in body.content.items():
                    assert media_type == 'application/json'
                    item = item.media_type_schema
                    assert isinstance(item, Reference), item
                    item = self.resolve_ref(item)
                    assert item.type == 'object'
                    fields = {k: getattr(item, k) for k in item.__fields_set__}
                    assert all(field in ('required', 'properties', 'type', 'description')
                               for field in item.__fields_set__), fields.keys()
                    required_fields = item.required
                    for property_name, property_obj in item.properties.items():
                        if isinstance(property_obj, Reference):
                            property_obj = self.resolve_ref(property_obj)
                        type_hint = self.get_type_hint_of_schema(property_obj)
                        print(property_name, type_hint)
                    # print(item_name, tuple(fields.keys()), fields)
                # ParsedParameter(name='body')

            if not any(isinstance(p, Reference) for p in operation.parameters):
                parsed_parameters: list[ParsedParameter] = \
                    [ParsedParameter.parse_obj(p.dict()) for p in operation.parameters]
                [p.set_parent(self) for p in parsed_parameters]
                operation.parsed_parameters = parsed_parameters
                continue
            result = []
            for parameter in operation.parameters:
                if not isinstance(parameter, Reference):
                    result.append(parameter)
                    continue
                obj = self.resolve_ref(parameter)
                result.append(obj)

            parsed_parameters: list[ParsedParameter] = [ParsedParameter.parse_obj(p.dict()) for p in result]
            [p.set_parent(self) for p in parsed_parameters]
            operation.parsed_parameters = parsed_parameters

        # Currently, there is no parameter in header or cookie
        assert all(p.param_in in ('query', 'path') for o in operations for p in o.parsed_parameters)
        return operations

    @cached_property
    def content(self):
        content = render(RequestFactory(), 'api.html', {'data': self}).content.decode('utf-8')
        for _ in range(5):
            # content = re.sub(r'\n+', '\n', content)
            content = html.unescape(content)
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
        return Path(__file__).parent.parent / 'amazon_sp_api_clients_2' / self.package_name

    def generate(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        with open(self.directory / '__init__.py', 'w') as f:
            f.write('')
        with open(self.directory / 'api.py', 'w') as f:
            f.write(self.content)


def main():
    for json_file in (Path(__file__).parent.parent / 'swagger3_apis').glob('*.json'):
        # if 'order' not in json_file.stem:
        #     continue
        Generator(json_file).generate()


if __name__ == '__main__':
    main()
