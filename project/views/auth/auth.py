from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service

api = Namespace('auth')


@api.route('/login/')
class AuthUserLoginView(Resource):

    def post(self):
        return user_service.post_auth(request.json), 201  # авторизация пользователя

    def put(self):
        return user_service.put_auth(request.json), 204  # обновление токена


@api.route('/register/')
class AuthUserRegisterView(Resource):
    def post(self):
        user_service.create(request.json)  # создание пользователя
        return '', 201