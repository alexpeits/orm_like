from __future__ import print_function


class Field(object):

    field_type = None

    def __init__(self, desc=''):
        self.desc = desc
        self.name = None

    def __get__(self, obj, cls):
        if obj is None:
            return self
        try:
            return obj.__dict__[self.name]
        except KeyError:
            raise AttributeError(
                '{} does not have attribute {}'
                .format(obj, self.name)
            )

    def __set__(self, obj, val):
        self.validate(val)
        obj.__dict__[self.name] = val

    def validate(self, val):
        if not isinstance(val, self.field_type):
            raise ValueError(
                'Invalid value {} for field with type {}'
                .format(val, self.field_type)
            )


class ModelMeta(type):

    def __new__(cls, name, bases, attrs):
        orm_fields = []
        for k, v in attrs.items():
            if isinstance(v, Field):
                v.name = k
                orm_fields.append(k.strip('_'))
        attrs['_fields'] = orm_fields
        return super(ModelMeta, cls).__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        fields = self._fields
        for k, v in kwargs.items():
            if k not in fields:
                raise ValueError(
                    '{} not an attribute of {}'
                    .format(k, self.__class__.__name__)
                )
            setattr(self, k, v)
