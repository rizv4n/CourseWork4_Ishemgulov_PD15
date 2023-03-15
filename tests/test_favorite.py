import pytest
from unittest.mock import MagicMock

from data.dao.models.favorite_movies import Favorite
from data.dao.models.user import User
from data.dao.favorite_movies import FavoriteDAO
from data.dao.user import UserDAO
from data.services.favorite_movies import FavoriteService


@pytest.fixture()
def favorite_dao():
    favorite_dao = FavoriteDAO(None)

    favorite_1 = Favorite(
        user_id=1,
        movie_id=2
    )

    favorite_2 = Favorite(
        user_id=2,
        movie_id=1
    )

    favorite_dao.get_id_from_table = MagicMock()
    favorite_dao.create = MagicMock()
    favorite_dao.delete = MagicMock(return_value=None)

    return favorite_dao


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    user_1 = User(
        id=1,
        email='123@mail.ru',
        password=12345678,
        name='Alex',
        surname='Smith',
        favorite_genre_id=2)

    user_2 = User(
        id=2,
        email='456@mail.ru',
        password=87654321,
        name='Alisa',
        surname='Hay',
        favorite_genre_id=1)

    user_dao.get_by_email = MagicMock()
    user_dao.create = MagicMock()
    user_dao.delete = MagicMock(return_value=None)
    user_dao.update = MagicMock()

    return user_dao


class TestFavoriteServices:
    @pytest.fixture(autouse=True)
    def favorite_services(self, favorite_dao, user_dao):
        self.favorite_services = FavoriteService(f_dao=favorite_dao, u_dao=user_dao)

    def test_create(self):
        favorite_d = {
            'email': '123@mail.ru',
            'movie': 1
        }

        movie = self.favorite_services.create(favorite_d)

        assert movie.user_id is not None
        assert movie.movie_id is not None

    def test_delete(self):
        favorite_d = {
            'email': '123@mail.ru',
            'movie': 1
        }

        movie = self.favorite_services.delete(favorite_d)

        assert movie is None
