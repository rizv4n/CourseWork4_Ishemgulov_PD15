from data.dao.models.favorite_movies import Favorite


class FavoriteDAO:
    """
    Create and Delete Favorite Movies
    """
    def __init__(self, session):
        self.session = session\

    def get_id_from_table(self, data):
        return self.session.query(Favorite).filter(
            Favorite.user_id == data['user_id'],
            Favorite.movie_id == data['movie_id']
        ).first()

    def create(self, data):
        f_movie = Favorite(**data)

        self.session.add(f_movie)
        self.session.commit()

        return f_movie

    def delete(self, data):
        self.session.delete(self.get_id_from_table(data))
        self.session.commit()

