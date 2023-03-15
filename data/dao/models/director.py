from marshmallow import Schema, fields

from sqlalchemy import Column, String
from data.setup.db import models

"""Модель и схема для таблицы Director"""


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
