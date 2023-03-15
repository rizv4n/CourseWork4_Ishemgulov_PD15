from data.dao.genre import GenreDAO


class GenreService:
    """
    Бизнес логика для работы с моделью Genre
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self, page=None):
        if page is None:
            return self.dao.get_all()
        else:
            page = int(page)
            return self.dao.get_all()[(page-1)*12:page*12]
