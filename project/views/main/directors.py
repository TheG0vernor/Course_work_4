from flask_restx import Namespace, Resource

from project.container import director_service
from project.dao.model.director import DirectorSchema

api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):

    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@api.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        director = director_service.get_one(did)
        director_schema = DirectorSchema().dump(director)
        return director_schema, 200