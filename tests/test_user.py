import pytest
from unittest.mock import MagicMock

from data.dao.models.user import User
from data.dao.user import UserDAO
from data.services.user import UserService


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


class TestDAO:
    pass


class TestUserServices:
    @pytest.fixture(autouse=True)
    def user_services(self, user_dao):
        self.user_services = UserService(dao=user_dao)

    def test_get_by_email(self):
        user = self.user_services.get_by_email('123@mail.ru')

        assert user is not None
        assert user.email is not None
        assert user.password is not None
        assert user.name is not None
        assert user.surname is not None
        assert user.favorite_genre is not None

    def test_create(self):
        user_d = {
            'email': '789@mail.ru',
            'password': 0000000
        }

        user = self.user_services.create(user_d)

        assert user.email is not None
        assert user.password is not None

    def test_patch(self):
        user_d = {
            'email': '789@mail.ru',
            'new_name': 'Mila',
            'new_surname': 'Bush',
            'favorite_genre': 'Action'
        }

        user = self.user_services.patch(user_d)

        assert user.name is not None
        assert user.surname is not None
        assert user.favorite_genre is not None

    def test_put(self):
        user_d = {
            'email': '123@mail.ru',
            'new_password': '0000000'
        }

        user = self.user_services.put(user_d)

        assert user.email is not None
        assert user.password is not None

    def test_delete(self):
        user = self.user_services.delete('123@mail.ru')

        assert user is None
