import pytest
from unittest.mock import MagicMock

from data.dao.models.genre import Genre
from data.dao.genre import GenreDAO
from data.services.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(
        id=1,
        name='Comedy'
    )

    genre_2 = Genre(
        id=2,
        name='Horror'
    )

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])

    return genre_dao


class TestGenreServices:
    @pytest.fixture(autouse=True)
    def genre_services(self, genre_dao):
        self.genre_services = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_services.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_services.get_all()

        assert genre is not None
