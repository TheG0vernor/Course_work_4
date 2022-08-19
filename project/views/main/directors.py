from flask_restx import Namespace, Resource

from project.container import director_service
from project.dao.model.director import DirectorSchema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200