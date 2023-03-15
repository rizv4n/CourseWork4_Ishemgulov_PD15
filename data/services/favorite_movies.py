from data.dao.favorite_movies import FavoriteDAO
from data.dao.user import UserDAO
from data.dao.models.user import UserSchema

u_schema = UserSchema()


class FavoriteService:
    """
    Бизнес логика для работы с моделью Favorite Movies
    """
    def __init__(self, f_dao: FavoriteDAO, u_dao: UserDAO):
        self.f_dao = f_dao
        self.u_dao = u_dao

    def create(self, data):
        user = self.u_dao.get_by_email(data['email'])

        f_movie = {
            'user_id': u_schema.dump(user)['id'],
            'movie_id': data['movie']
        }

        return self.f_dao.create(f_movie)

    def delete(self, data):
        user = self.u_dao.get_by_email(data['email'])

        f_movie = {
            'user_id': u_schema.dump(user)['id'],
            'movie_id': data['movie']
        }

        self.f_dao.delete(f_movie)
