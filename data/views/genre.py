from flask import request
from flask_restx import Resource, Namespace

from data.container import genre_service
from data.dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

"""Вьюшки для реализации работы с таблицей Genre"""


@genre_ns.route('/')
class GenreViews(Resource):
    def get(self):
        page = request.args.get(key='page')
        all_genres = genre_service.get_all(page)
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
