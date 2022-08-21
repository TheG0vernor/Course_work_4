from .main.movies import api as movie_ns
from .main.genres import api as genres_ns
from .main.directors import api as director_ns
from .auth.auth import api as auth_ns
from .auth.user import api as user_ns

__all__ = [
    'genres_ns',
    'director_ns',
    'movie_ns',
    'auth_ns',
    'user_ns'
]
