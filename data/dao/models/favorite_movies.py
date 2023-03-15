from marshmallow import Schema, fields

from sqlalchemy import Column, Integer, ForeignKey
from data.setup.db import db, models

"""Модель и схема для таблицы Favorite Movies"""


class Favorite(models.Base):
    __tablename__ = 'favorite_movies'

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = db.relationship("User")
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    movie = db.relationship("Movie")


class FavoriteSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
