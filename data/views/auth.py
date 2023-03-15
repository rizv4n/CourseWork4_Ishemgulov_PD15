from flask import request
from flask_restx import Resource, Namespace

from data.container import auth_service
from data.dao.models.user import UserSchema

auth_ns = Namespace('auth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

"""Вьюшки для реализации сервисов аутентификации"""


@auth_ns.route('/register')
class AuthViews(Resource):
    def post(self):
        req_json = request.json

        auth_service.create(req_json)

        return "", 201


@auth_ns.route('/login')
class AuthViews(Resource):
    def post(self):
        req_json = request.json

        req_email = req_json['email']
        req_password = req_json['password']

        if None in [req_email, req_password]:
            return "", 400

        tokens = auth_service.generate_tokens(req_email, req_password)

        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
