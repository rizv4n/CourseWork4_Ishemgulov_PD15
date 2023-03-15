from data.config import DevelopmentConfig
from data.server import create_app
from data.setup.db import db

"""Создание пустой таблицы"""


if __name__ == '__main__':
    with create_app(DevelopmentConfig).app_context():
        db.create_all()
