from project.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        session = self.dao
        if filters.get("status").upper() == 'NEW':
            session = session.get_all_new()
        if filters.get("page") is not None:
            page = int(filters.get("page"))
            session = session.get_page().paginate(page=page, per_page=12, error_out=False).items

        else:
            session = session.get_all()
        return session
