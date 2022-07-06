class BaseObject:
    _attrs_config: dict

    @classmethod
    def from_json(cls, data):
        data = {cls._attrs_config[k][0]: v for k, v in data.items()}
        # noinspection PyArgumentList
        return cls(**data)
