class Parser:
    TRUE_VALUES = (True, 'true', 't', 'yes', 'y')
    FALSE_VALUES = (False, 'false', 'f', 'no', 'n')

    def as_bool(self, value) -> bool:
        if isinstance(value, str):
            value = value.lower()
        if value in self.TRUE_VALUES:
            return True
        elif value in self.FALSE_VALUES:
            return False
        else:
            raise ValueError('Wrong boolean value')
