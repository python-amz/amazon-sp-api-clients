from dataclasses import dataclass, field
from enum import Enum, auto
from functools import cached_property
from logging import getLogger
from os import path

from jinja2 import Template

logger = getLogger(__name__)


class ParseError(Exception):
    pass


def parse_type(string):
    if (check := {'string': 'str', 'array': 'list', 'object': 'dict',
                  'boolean': 'bool', 'integer': 'int', 'number': 'float'}.setdefault(string, None)) is not None:
        return check
    prefixes = ('#/components/schemas/', '#/components/parameters/')
    for prefix in prefixes:
        if string.startswith(prefix):
            return string.removeprefix(prefix)
    print(string)


def get_item_type(item_data):
    if (no_type := 'type' not in item_data) and ('$ref' not in item_data):
        raise ParseError('dict component property item type')
    item_type = parse_type(item_data['$ref' if no_type else 'type'])
    return item_type


@dataclass
class Field:
    name: str  # property name, the identifier in python
    type: str = 'object'  # the type, used for type hint
    source: dict = field(default_factory=dict)

    @property
    def item_type(self) -> str:
        assert self.type == 'list'
        return get_item_type(self.source['items'])

    @property
    def converter(self):
        if self.type == 'bool':
            return 'convert_bool'
        else:
            return self.type


class ComponentType(Enum):
    dict = auto()
    list = auto()
    alias = auto()
    parameter = auto()


@dataclass
class Component:
    name: str
    type_category: ComponentType = ComponentType.dict
    type: str = ''  # alias type
    source: dict = field(default_factory=dict)
    properties: dict[str, Field] = field(default_factory=dict)
    item_type: str = ''  # for list component only
    base_types: list = field(default_factory=list)

    @property
    def description(self):
        return self.source.get('description', '')


def stage_1_dict_components(data: dict):
    if set(data['components'].keys()) - {'schemas', 'parameters'}:
        raise ParseError('data.components.schemas')
    components: dict[str, dict] = data['components']['schemas']
    components = {k: v for k, v in components.items() if 'type' in v and v['type'] == 'object'}

    # Parse
    # {component_name: {'properties': {property_name: {'type': property_type,
    #                                                  'item_type': item_type}}}}
    result: dict[str, Component] = {}
    for component_name, component_data in components.items():
        parsed_component = result.setdefault(component_name, Component(
            name=component_name, type_category=ComponentType.dict, source=component_data,
        ))
        if 'properties' not in component_data:
            continue
        for property_name, property_data in parsed_component.source['properties'].items():
            property_obj = parsed_component.properties.setdefault(
                property_name, Field(
                    property_name,
                    source=property_data,
                ))
            property_data: dict
            if '$ref' in property_data:
                property_obj.type = parse_type(property_data['$ref'])
            elif 'type' in property_data:
                property_obj.type = parse_type(property_data['type'])
            else:
                raise ParseError('dict component property type')
    return result


def stage_2_list_components(data: dict):
    components = data['components']['schemas']
    components = {k: v for k, v in components.items() if 'type' in v and v['type'] == 'array'}

    # Parse
    parsed_components: dict[str, Component] = {}
    for component_name, component_data in components.items():
        parsed_component_data: Component = parsed_components.setdefault(component_name, Component(
            name=component_name, type_category=ComponentType.list, source=component_data,
        ))
        if 'items' not in component_data:
            raise ParseError('list component items not found')
        parsed_component_data.item_type = get_item_type(component_data['items'])
    return parsed_components


def stage_3_alias_components(data: dict):
    components = data['components']['schemas']
    components = {k: v for k, v in components.items() if 'type' in v and v['type'] not in ('array', 'object')}

    parsed_components: dict[str, Component] = {}
    for component_name, component_data in components.items():
        parsed_components.setdefault(component_name, Component(
            name=component_name, type_category=ComponentType.alias, source=component_data,
            type=parse_type(component_data['type']),
        ))
    return parsed_components


def stage_4_parameters(data: dict):
    if 'parameters' not in data['components']:
        return {}
    parameters: dict = data['components']['parameters']
    parsed_parameters: dict[str, Component] = {}
    for parameter_name, parameter_data in parameters.items():
        parsed_parameter = parsed_parameters.setdefault(parameter_name, Component(
            name=parameter_name, type_category=ComponentType.parameter, source=parameter_data,
        ))
        parsed_parameter.type = parse_type(parsed_parameter.source['schema']['type'])
    return parsed_parameters


def stage_5_ref_components(data: dict):
    components = data['components']['schemas']
    components = {k: v for k, v in components.items() if 'type' not in v}
    if not components:
        return {}

    parsed_components: dict[str, Component] = {}
    for component_name, component_data in components.items():
        parsed_component = parsed_components.setdefault(component_name, Component(
            name=component_name, source=component_data
        ))
        extra_properties = parsed_component.properties
        base_types = parsed_component.base_types
        if '$ref' in component_data:
            base_types.append(parse_type(component_data['$ref']))
        elif 'allOf' in component_data:
            for datum in component_data['allOf']:
                if '$ref' in datum:
                    base_types.append(parse_type(datum['$ref']))
                elif datum['type'] == 'object':
                    for k, v in datum['properties'].items():
                        property_obj = extra_properties.setdefault(k, {})
                        property_obj['type'] = parse_type(v['$ref'])
                else:
                    raise NotImplementedError
        else:
            raise NotImplementedError
    return parsed_components


@dataclass
class OperationParameter:
    swagger_data: dict
    source: dict

    @cached_property
    def __parsed_source(self):
        if '$ref' in self.source:
            ref: str = self.source['$ref']
            ref = ref.rsplit('/', maxsplit=1)[1]
            return self.swagger_data['components']['parameters'][ref]
        else:
            return self.source

    @property
    def name(self):
        return self.__parsed_source['name']

    @property
    def location(self):
        return self.__parsed_source['in']

    @cached_property
    def required(self):
        return self.__parsed_source.get('required', False)

    @cached_property
    def default(self):
        return self.__parsed_source.get('default', None)

    @cached_property
    def schema_data(self):
        return self.__parsed_source.get('schema')

    @cached_property
    def type(self):
        return parse_type(self.schema_data['type'])

    @cached_property
    def item_type(self):
        assert self.type == 'list'
        return parse_type(self.schema_data['items']['type'])


@dataclass
class Operation:
    swagger_data: dict
    source_url: str
    source_method: str
    source: dict = None

    @cached_property
    def url(self):
        return self.source_url

    @cached_property
    def method(self):
        return self.source_method.upper()

    @cached_property
    def request_body(self):
        if not (self.source_method == 'post' and 'requestBody' in self.source):
            return {}
        request_body = self.source['requestBody']
        assert 'content' in request_body
        request_body_content = request_body['content']
        assert set(request_body_content.keys()) == {'application/json'}
        request_body_json = request_body_content['application/json']
        assert set(request_body_json.keys()) == {'schema'}
        request_body_schema = request_body_json['schema']
        assert '$ref' in request_body_schema
        request_body_type = parse_type(request_body_schema['$ref'])
        return {
            'type': request_body_type
        }

    @cached_property
    def __parameters(self):
        return [OperationParameter(swagger_data=self.swagger_data, source=d) for d in self.source.get('parameters', [])]

    @cached_property
    def operation_id(self):
        return self.source['operationId']

    @cached_property
    def query_parameters(self):
        return {d.name: d for d in self.__parameters if d.location == 'query'}

    @cached_property
    def path_parameters(self):
        return {d.name: d for d in self.__parameters if d.location == 'path'}

    @cached_property
    def responses(self):
        if 'responses' not in self.source:
            return {}
        result = {}
        for status_code, response_data in self.source['responses'].items():
            if 'application/json' in response_data['content']:
                parsed_response_data = result.setdefault(status_code, {})
                response_type = parse_type(response_data['content']['application/json']['schema']['$ref'])
                parsed_response_data['type'] = response_type
            elif 'application/hal+json' in response_data['content']:
                parsed_response_data = result.setdefault(status_code, {})
                response_type = parse_type(response_data['content']['application/hal+json']['schema']['$ref'])
                parsed_response_data['type'] = response_type
            elif response_data['content'] == {}:
                parsed_response_data = result.setdefault(status_code, {})
                parsed_response_data['type'] = 'None'
            else:
                raise ValueError(f'Could not parse response: {self.source_url}, {self.source_method}, {status_code}')
        return result


def stage_6_operations(data: dict):
    paths = data['paths']
    parsed_operations: dict[str, Operation] = {
        method_data['operationId']: Operation(
            swagger_data=data,
            source_url=url,
            source_method=method,
            source=method_data,
        )
        for url, url_data in paths.items()
        for method, method_data in url_data.items()
    }
    return parsed_operations


def module_to_class_name(name: str):
    result = [name[0].upper()]
    upper_flag = False
    for char in name[1:]:
        if char == '_':
            upper_flag = True
            continue
        if upper_flag:
            result.append(char.upper())
            upper_flag = False
        else:
            result.append(char)
    return ''.join(result)


def render(module: str, data: dict, template: Template = None):
    class_name = module_to_class_name(module)
    if template is None:
        template_path = path.join(path.dirname(path.abspath(__file__)), 'api.pyt') if template is None else template
        with open(template_path, 'r', encoding='utf-8') as f:
            template = Template(f.read())
    context = dict(class_name=class_name,
                   dict_components=stage_1_dict_components(data),
                   list_components=stage_2_list_components(data),
                   alias_components=stage_3_alias_components(data),
                   parameters=stage_4_parameters(data),
                   ref_components=stage_5_ref_components(data),
                   operations=stage_6_operations(data))
    return context, template.render(**context)
