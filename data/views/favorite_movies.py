from flask import request
from flask_restx import Resource, Namespace

from data.container import favorite_service
from data.dao.models.favorite_movies import FavoriteSchema
from data.utils.auth_utils import check_token

favorite_ns = Namespace('favorites')

favorite_schema = FavoriteSchema()

"""Вьюшки для реализации работы с таблицей Favorite Movies"""


@favorite_ns.route('/movies/<int:mid>')
class FavoritesViews(Resource):

    @check_token
    def post(self, mid: int):

        data = {
            "movie": mid,
            "email": request.json['email']
        }

        favorite_service.create(data)

        return "", 204

    @check_token
    def delete(self, mid: int):

        data = {
            "movie": mid,
            "email": request.json['email']
        }

        favorite_service.delete(data)

        return "", 204
