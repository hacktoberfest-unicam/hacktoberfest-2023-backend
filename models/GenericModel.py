class GenericModel:
    def __repr__(self):
        pass

    def to_dict(self):
        return {param: getattr(self, param) for param in self.get_params()}

    def __setattr__(self, key, value):
        if key == 'id':
            raise AttributeError('Cannot set id attribute')
        super().__setattr__(key, value)

    def get_params(self):
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_") and not attr in ['metadata', 'query', 'registry']]
