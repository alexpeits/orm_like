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


class Integer(Field):

    field_type = int


class Float(Field):

    field_type = float


class String(Field):

    field_type = str


class Boolean(Field):

    field_type = bool


class List(Field):

    field_type = list


class ModelMeta(type):

    def __new__(cls, name, bases, attrs):
        for k, v in attrs.items():
            if isinstance(v, Field):
                v.name = k
        return super(ModelMeta, cls).__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMeta):
    pass
