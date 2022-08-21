from flask import request
from flask_restx import Resource, Namespace

from project.container import movie_service
from project.dao.model.movie import MovieSchema

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):


    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


@api.route('/<int:bid>')
class MovieView(Resource):

    def get(self, bid):
        movie = movie_service.get_one(bid)
        movie_schema = MovieSchema().dump(movie)
        return movie_schema, 200
