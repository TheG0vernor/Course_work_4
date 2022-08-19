from sqlalchemy import desc

from project.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_new(self):
        return self.session.query(Movie).order_by(desc(Movie.year))

    def get_page(self):
        return self.session.query(Movie)
