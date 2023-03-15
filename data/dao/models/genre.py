from marshmallow import Schema, fields

from sqlalchemy import Column, String
from data.setup.db import models

"""Модель и схема для таблицы Genre"""


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
