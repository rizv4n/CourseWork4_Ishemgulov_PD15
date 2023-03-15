from flask import request
from flask_restx import Resource, Namespace

from data.container import user_service
from data.dao.models.user import UserSchema
from data.utils.auth_utils import check_token, get_email

user_ns = Namespace('user')

user_schema = UserSchema()

"""Вьюшки для реализации работы с таблицей User"""


@user_ns.route('/')
class UserViews(Resource):

    @check_token
    def get(self):
        email = get_email()
        user = user_service.get_by_email(email)

        return user_schema.dump(user), 200

    @check_token
    def patch(self):
        req_data = request.json

        user_service.patch(req_data)

        return "", 204

    @check_token
    def delete(self):
        email = get_email()
        user_service.delete(email)

        return "", 204


@user_ns.route('/password')
class UserViews(Resource):

    @check_token
    def put(self):
        req_data = request.json

        data = {
            "email": req_data['email'],
            "new_password": req_data['new_password']
        }

        user_service.put(data)

        return "", 204
