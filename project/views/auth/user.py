from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.dao.model.user import UserSchema

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    def get(self):
        rs = user_service.get_user(request.headers)
        res = UserSchema().dump(rs)
        return res, 200

    def patch(self):
        user_service.patch_user(request.headers, request.json)
        return '', 204


@api.route('/password/')
class UserPassView(Resource):
    def put(self):
        user_service.put_password(request.headers, request.json)
        return 'Password successfully update', 204
