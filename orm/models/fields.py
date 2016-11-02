from __future__ import print_function

from ..models.base import Field


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
