import textwrap
from itertools import chain


class Utils:
    @staticmethod
    def wrap_description(text: str, initial_indent: int = 0, subsequent_indent: int = 4, width=0) -> str:
        """Wrap description with indent and width.

        Args:
            text: the description.
            initial_indent: whitespaces before line 1
            subsequent_indent: whitespaces before line 2 and more
            width: line width

        Returns:
            for indent=4 and left=8:
            --------xxxxxxxxxxxxxxxxxxxx
            ------------xxxxxxxxxxxxxxxx
            ------------xxxxxxxxxxxxxxxx
        """
        lines = text.splitlines()
        result = chain.from_iterable(textwrap.wrap(line, width=width, initial_indent=' ' * initial_indent,
                                                   subsequent_indent=' ' * subsequent_indent) for line in lines)
        return '\n'.join(result)

    @staticmethod
    def get_type_hint(schema):
        from .generator import Schema, ParsedSchema, Reference
        assert isinstance(schema, Schema)
        type_convert = {
            ('integer', None): 'int',
            ('string', None): 'str',
            ('boolean', None): 'bool',
            ('object', None): "Dict[str, {child}]",
            ('array', None): "List[{child}]",
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
        if schema is None:
            return 'Any'

        assert schema.type is not None
        probable_fields = {'generator', 'type', 'description', 'name', 'enum', 'maximum', 'minimum', 'items',
                           'minItems', 'maxItems', 'pattern', 'default', 'required', 'minLength', 'maxLength',
                           'uniqueItems', 'example',
                           'schema_format', 'properties', 'additionalProperties',
                           'ref_name'}
        fields = {f for f in schema.__fields_set__ if getattr(schema, f) is not None}
        assert fields.issubset(probable_fields), fields - probable_fields

        child = 'Any'
        if schema.type == 'array':
            child_item = schema.items
            if isinstance(child_item, Reference):
                child = schema.items.ref.split('/')[-1]
                child = f"'{child}'"
            elif isinstance(child_item, Schema):
                child = type_convert[(child_item.type, child_item.schema_format)].format(child='Any')
            else:
                raise TypeError(type(child_item))
        elif isinstance(schema, ParsedSchema) and schema.type == 'object' and schema.ref_name:
            return f"'{schema.ref_name}'"
        type_hint = type_convert[(schema.type, schema.schema_format)].format(child=child)
        assert schema.enum is None or type_hint == 'str'
        choices = ', '.join(f'Literal["{v}"]' for v in schema.enum) if schema.enum is not None else None
        type_hint = f'Union[{choices}]' if type_hint == 'str' and choices is not None else type_hint
        return type_hint
