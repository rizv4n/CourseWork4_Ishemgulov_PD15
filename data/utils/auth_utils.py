import calendar
import hashlib
import datetime
import jwt
import base64
import hmac

from flask import request, abort
from data.config import BaseConfig

"""Утилиты для работы с сервисами аутентификации"""


def get_hash(password):
    return base64.b64encode(hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        BaseConfig.PWD_HASH_SALT,
        BaseConfig.PWD_HASH_ITERATIONS
    ))


def generate_tokens(data):

    tok_1 = datetime.datetime.utcnow() + datetime.timedelta(minutes=BaseConfig.TOKEN_EXPIRE_MINUTES)
    data['exp'] = calendar.timegm(tok_1.timetuple())
    access_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.JWT_ALGORITHM)

    tok_2 = datetime.datetime.utcnow() + datetime.timedelta(days=BaseConfig.TOKEN_EXPIRE_DAYS)
    data["exp"] = calendar.timegm(tok_2.timetuple())
    refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.JWT_ALGORITHM)

    return {"access_token": access_token, "refresh_token": refresh_token}


def decode_refresh_token(refresh_token):
    data = jwt.decode(jwt=refresh_token, key=BaseConfig.SECRET_KEY, algorithms=BaseConfig.JWT_ALGORITHM)
    email = data.get("email")

    return email


def compare_password(password_hash, password):
    return hmac.compare_digest(base64.b64decode(password_hash), hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        BaseConfig.PWD_HASH_SALT,
        BaseConfig.PWD_HASH_ITERATIONS
    ))


def check_token(func):
    def wrapper(*args, **kwargs):
        req_data = request.json

        if "refresh_token" not in req_data:
            abort(400)

        email = decode_refresh_token(req_data['refresh_token'])

        if email != req_data['email']:
            abort(400)

        return func(*args, **kwargs)

    return wrapper


def get_email():
    return request.json['email']
