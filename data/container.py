from data.setup.db import db

from data.dao.genre import GenreDAO
from data.dao.director import DirectorDAO
from data.dao.movie import MovieDAO
from data.dao.user import UserDAO
from data.dao.favorite_movies import FavoriteDAO

from data.services.genre import GenreService
from data.services.director import DirectorService
from data.services.movie import MovieService
from data.services.auth import AuthService
from data.services.user import UserService
from data.services.favorite_movies import FavoriteService

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
auth_service = AuthService(user_dao)

favorite_dao = FavoriteDAO(db.session)
favorite_service = FavoriteService(favorite_dao, user_dao)
