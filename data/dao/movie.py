from data.dao.models.movie import Movie


class MovieDAO:
    """
    Read Movie
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, status):
        if status is None:
            return self.session.query(Movie).all()
        else:
            return self.session.query(Movie).order_by(Movie.year.desc()).all()
