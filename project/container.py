from project.dao import GenresDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MovieDAO

from project.services import GenresService
from project.services.directors_service import DirectorService
from project.services.movies_service import MovieService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
director_service = DirectorService(dao=director_dao)