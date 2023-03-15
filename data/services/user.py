from data.dao.user import UserDAO
from data.utils.auth_utils import get_hash


class UserService:
    """
    Бизнес логика для работы с моделью User
    """
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, data):
        return self.dao.create(data)

    def patch(self, data):
        user = self.get_by_email(data['email'])

        try:
            user.name = data['new_name']
        except KeyError:
            pass

        try:
            user.surname = data["new_surname"]
        except KeyError:
            pass

        try:
            user.favorite_genre = data["favorite_genre"]
        except KeyError:
            pass

        return self.dao.update(user)

    def put(self, data):
        user = self.get_by_email(data['email'])

        user.password = get_hash(data['new_password'])

        return self.dao.update(user)

    def delete(self, email):
        return self.dao.delete(email)
