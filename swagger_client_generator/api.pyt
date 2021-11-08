from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List

{% for component_name, component in dict_components.items() %}
class {{ component_name }}:
    """
    {{component.source.description}}
    """
    def __init__(self, data):
        super().__init__()
        self.data = data
    {% for name, property in component.properties.items() %}
        if '{{ name }}' in data:
        {% set type = property.type %}
        {% if type == 'list' %}
            {% set item_type = property.item_type %}
            self.{{ name }}: _List[{{ item_type }}] = [{{ item_type }}(datum) for datum in data['{{ name }}']]
        {% else %}
            self.{{ name }}: {{ type }} = {{ property.converter }}(data['{{ name }}'])
        {% endif %}
        else:
        {% if type == 'list' %}
            {% set item_type = property.item_type %}
            self.{{ name }}: _List[{{ item_type }}] = []
        {% else %}
            self.{{ name }}: {{ type }} = None
        {% endif %}


    {% endfor %}
{% endfor %}





{% for component_name, component in list_components.items() %}
    {% set item_type = component.item_type %}
class {{ component_name }}(list, _List['{{ item_type }}']):
    """
    {{component.source.description}}
    """
    def __init__(self, data):
        super().__init__([{{ item_type }}(datum) for datum in data])
        self.data = data
{% endfor %}

{% for component_name, component in alias_components.items() %}
class {{ component_name }}({{component.type}}):
    """
    {{component.source.description}}
    """
{% endfor %}



{% for component_name, component in parameters.items() %}
class {{ component_name }}({{component.type}}):
    """
    {{component.source.description}}
    """
{% endfor %}


{% for component_name, component in ref_components.items() %}
class {{ component_name }}({% for type in component.types %}{{ type }}, {% endfor %}):
    """
    {{component.source.description}}
    """
    def __init__(self, data):

    {% for name, property in component.properties.items() %}
        if '{{ name }}' in data:
        {% set type = property.type %}
        {% if type == 'list' %}
            {% set item_type = property.item_type %}
            self.{{ name }}: _List[{{ item_type }}] = [{{ item_type }}(datum) for datum in data.pop('{{ name }}')]
        {% else %}
            self.{{ name }}: {{ type }} = {{ type }}(data.pop('{{ name }}'))
        {% endif %}
        else:
        {% if type == 'list' %}
            {% set item_type = property.item_type %}
            self.{{ name }}: _List[{{ item_type }}] = []
        {% else %}
            self.{{ name }}: {{ type }} = None
        {% endif %}
    {% endfor %}

        self.data = data
        super().__init__(data)

{% endfor %}




class {{ class_name }}Client(__BaseClient):
{% for operation_name, operation in operations.items() %}
    """
    {{operation.source.description}}
    """
    def {{ operation_name }}(self,
        {% if operation.request_body %}
            data: {{ operation.request_body.type }},
        {% endif %}

        {% for path_parameter_name, path_parameter in operation.path_parameters.items() %}
            {% set type = path_parameter.type %}
            {% if type == 'list' %}
                {{ path_parameter_name }}: _List[{{ path_parameter.item_type }}],
            {% else %}
                {{ path_parameter_name }}: {{ type }},
            {% endif %}
        {% endfor %}
        {% for query_parameter_name, query_parameter in operation.query_parameters.items() %}
            {% if query_parameter.required == True%}
                {% set type = query_parameter.type %}
                {% set default = query_parameter.default %}
                {% if type == 'list' %}
                    {{ query_parameter_name }}: _List[{{ query_parameter.item_type }}],
                {% else %}
                    {{ query_parameter_name }}: {{ type }},
                {% endif %}
            {% endif %}
        {% endfor %}
        {% for query_parameter_name, query_parameter in operation.query_parameters.items() %}
            {% if query_parameter.required == False %}
                {% set type = query_parameter.type %}
                {% set default = query_parameter.default %}
                {% if type == 'list' %}
                    {{ query_parameter_name }}: _List[{{ query_parameter.item_type }}] = {{ query_parameter.default }},
                {% else %}
                    {{ query_parameter_name }}: {{ type }} = {{ query_parameter.default }},
                {% endif %}
            {% endif %}
        {% endfor %}
    ):
        url = '{{ operation.url }}'.format(
            {% for path_parameter_name, path_parameter in operation.path_parameters.items() %}
                {{ path_parameter_name }} = {{ path_parameter_name }},
            {% endfor %}
        )
        params = {}
        {% for query_parameter_name, query_parameter in operation.query_parameters.items() %}
        if {{ query_parameter_name }} is not None:
            {% set type = query_parameter.type %}
            {% if type == 'list' %}
            params['{{ query_parameter_name }}'] = ','.join(map(str, {{ query_parameter_name }}))
            {% else %}
            params['{{ query_parameter_name }}'] = {{ query_parameter_name }}
            {% endif %}
        {% endfor %}
        {% if operation.method == 'GET' %}
        response = self.request(url, method='{{ operation.method }}', params=params)
        {% else %}
        response = self.request(url, method='{{ operation.method }}', data=params)
        {% endif %}
        return {
            {% for status_code, response in operation.responses.items() %}
                {{ status_code }}: {{ response.type }},
            {% endfor %}
        }[response.status_code](self._get_response_json(response))

{% endfor %}
