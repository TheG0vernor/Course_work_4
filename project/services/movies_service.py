from project.dao.movie import MovieDAO


class MoviesService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):  # отображение одного фильма по id
        return self.dao.get_one(bid)

    def get_all(self, filters):  # отображение всех фильмов, в т.ч. по фильтрам (статус-новизна, page-страница)
        session = self.dao
        if filters.get("status") == 'new' and filters.get("page") is not None:
            page = int(filters.get("page"))
            session = session.get_all_new().paginate(page=page, per_page=12, error_out=False).items
        elif filters.get("page") is not None:
            page = int(filters.get("page"))
            session = session.get_all().paginate(page=page, per_page=12, error_out=False).items
        elif filters.get("status") == 'new':
            session = session.get_all_new()
        else:
            session = session.get_all()
        return session
