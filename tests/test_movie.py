import pytest
from unittest.mock import MagicMock

from data.dao.models.movie import Movie
from data.dao.movie import MovieDAO
from data.services.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(
        id=1,
        title='movie_1',
        description='description_1',
        trailer='trailer_1',
        year=2000,
        rating='PG13',
        genre_id=2,
        director_id=1
    )

    movie_2 = Movie(
        id=2,
        title='movie_2',
        description='description_2',
        trailer='trailer_2',
        year=2023,
        rating='PG13',
        genre_id=3,
        director_id=5
    )

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])

    return movie_dao


class TestMovieServices:
    @pytest.fixture(autouse=True)
    def movie_services(self, movie_dao):
        self.movie_services = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_services.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_services.get_all()

        assert movie is not None
