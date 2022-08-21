from project.dao import GenresDAO, MovieDAO, DirectorDAO, UserDAO

from project.services import GenresService, UsersService, MoviesService, DirectorsService

from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(dao=user_dao)