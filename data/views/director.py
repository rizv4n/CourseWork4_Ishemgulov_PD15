from flask import request
from flask_restx import Resource, Namespace

from data.container import director_service
from data.dao.models.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

"""Вьюшки для реализации работы с таблицей Director"""


@director_ns.route('/')
class DirectorViews(Resource):
    def get(self):
        page = request.args.get(key='page')
        all_directors = director_service.get_all(page)
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
