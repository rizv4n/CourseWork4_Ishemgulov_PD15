from flask import Flask, jsonify
from flask_cors import CORS

from data.exceptions import BaseServiceError
from data.setup.api import api
from data.setup.db import db

from data.views.genre import genre_ns
from data.views.director import director_ns
from data.views.movie import movie_ns
from data.views.auth import auth_ns
from data.views.user import user_ns
from data.views.favorite_movies import favorite_ns

"""Функции для создания приложения и эндпоинтов"""


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favorite_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
