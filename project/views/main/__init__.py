from .directors import director_ns
from .genres import api as genres_ns

__all__ = [
    'genres_ns', 'director_ns', 'movie_ns'
]

from .movies import movie_ns
