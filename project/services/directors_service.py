from project.dao.director import DirectorDAO


class DirectorsService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):  # отображение одного режиссёра по id
        return self.dao.get_one(bid)

    def get_all(self):  # отображение всех режиссёров
        return self.dao.get_all()
