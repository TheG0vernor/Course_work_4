from project.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):  # отображение одного режиссёра по id
        return self.session.query(Director).get(bid)

    def get_all(self):  # отображение всех режиссёров
        return self.session.query(Director).all()
