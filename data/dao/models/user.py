from marshmallow import Schema, fields

from sqlalchemy import Column, String, Integer, ForeignKey
from data.setup.db import db, models

"""Модель и схема для таблицы User"""


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre_id = Column(Integer, ForeignKey("genres.id"))
    favorite_genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre_id = fields.Int()

