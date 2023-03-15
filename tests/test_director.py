import pytest
from unittest.mock import MagicMock

from data.dao.models.director import Director
from data.dao.director import DirectorDAO
from data.services.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(
        id=1,
        name='Alex'
    )

    director_2 = Director(
        id=2,
        name='Alisa'
    )

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])

    return director_dao


class TestDirectorServices:
    @pytest.fixture(autouse=True)
    def director_services(self, director_dao):
        self.director_services = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_services.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_services.get_all()

        assert director is not None
