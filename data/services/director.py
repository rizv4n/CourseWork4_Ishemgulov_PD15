from data.dao.director import DirectorDAO


class DirectorService:
    """
    Бизнес логика для работы с моделью Director
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self, page=None):
        if page is None:
            return self.dao.get_all()
        else:
            page = int(page)
            return self.dao.get_all()[(page-1)*12:page*12]
