from data.dao.movie import MovieDAO


class MovieService:
    """
    Бизнес логика для работы с моделью Movie
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, page=None, status=None):
        if page is None:
            return self.dao.get_all(status)
        else:
            page = int(page)
            return self.dao.get_all(status)[(page-1)*12:page*12]
