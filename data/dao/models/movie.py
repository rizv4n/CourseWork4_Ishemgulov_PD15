from marshmallow import Schema, fields

from sqlalchemy import Column, String, Integer, ForeignKey
from data.setup.db import db, models

"""Модель и схема для таблицы Movie"""


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(String(255), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Int()
    director_id = fields.Int()
