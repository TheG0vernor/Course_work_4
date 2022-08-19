from flask import request
from flask_restx import Resource, Namespace

from project.container import movie_service
from project.dao.model.movie import MovieSchema
from project.services import movies_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
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


@movie_ns.route('/<int:bid>')
class MovieView(Resource):

    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200