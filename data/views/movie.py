from flask import request
from flask_restx import Resource, Namespace

from data.container import movie_service
from data.dao.models.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

"""Вьюшки для реализации работы с таблицей Movie"""


@movie_ns.route('/')
class MovieViews(Resource):
    def get(self):
        page = request.args.get(key='page')
        status = request.args.get(key='status')
        all_movies = movie_service.get_all(page, status)
        return movies_schema.dump(all_movies), 200


@movie_ns.route('/<int:did>')
class MovieViews(Resource):
    def get(self, did: int):
        movie = movie_service.get_one(did)
        return movie_schema.dump(movie), 200
