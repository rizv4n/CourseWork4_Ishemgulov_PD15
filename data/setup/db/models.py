from sqlalchemy import Column, Integer

from data.setup.db import db


class Base(db.Model):
    """
    Базовая модель для импорта
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
