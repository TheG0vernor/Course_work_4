from sqlalchemy import desc

from project.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):  # метод возвращает один фильм по id
        return self.session.query(Movie).get(bid)

    def get_all(self):  # метод возвращает все фильмы
        return self.session.query(Movie)

    def get_all_new(self):  # метод с сортировкой фильмов по году (убывание)
        return self.session.query(Movie).order_by(desc(Movie.year))
