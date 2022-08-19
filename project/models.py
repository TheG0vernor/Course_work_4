from sqlalchemy import Column, String, Float, Integer, ForeignKey

from project.setup.db import models
from sqlalchemy.orm import relationship


class Genre(models.Base):
    __tablename__ = 'genre'
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'director'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"), nullable=False)
    director = relationship("Director")