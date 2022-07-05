class BaseObject:
    _attrs_config: dict

    @classmethod
    def from_json(cls, data):
        name_convert = cls._attrs_config['name-convert']
        data = {name_convert[k]: v for k, v in data.items()}
        # noinspection PyArgumentList
        return cls(**data)
