
'''
    Metaclass, adding 'custom_' prefix to original names
    of attributes and methods
'''

class CustomMeta(type):
    '''
        CustomMeta metaclass
    '''

    def __new__(cls, name, bases, attr_dict):
        new_attrs = dict()
        for attr_name, attr_val in attr_dict.items():
            if not (attr_name.startswith("__") and attr_name.endswith("__")):
                new_attrs["custom_" + attr_name] = attr_val
            else:
                new_attrs[attr_name] = attr_val
        return super().__new__(cls, name, bases, new_attrs)

    def __call__(cls, *args, **kwargs):
        new_attrs = dict()
        obj = cls.__new__(cls)
        obj.__init__(*args, **kwargs)
        for attr_name, attr_val in obj.__dict__.items():
            if not (attr_name.startswith("__") and attr_name.endswith("__")):
                new_attrs['custom_' + attr_name] = attr_val
            else:
                new_attrs[attr_name] = attr_val
        obj.__dict__ = new_attrs
        return obj
