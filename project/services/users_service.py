import calendar
import datetime

import jwt
from flask_restx import abort

from project.config import BaseConfig
from project.dao.user import UserDAO
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self, new_user):  # создание пользователя
        return self.dao.create(new_user)

    def post_auth(self, data):  # авторизация пользователя, назначение токенов
        input_email = data.get('email', None)
        input_password = data.get('password', None)
        if None in [input_email, input_password]:
            abort(400)
        user_database = self.dao.find_user(input_email)
        if user_database is None:
            return {"error": "Неверные учётные данные"}, 401
        password = generate_password_hash(input_password)  # хеш пароля sha256

        if password != user_database.password:
            return {"error": "Неверные учётные данные"}, 401

        data = {"email": user_database.email,  # заносим данные из таблицы в переменную
                "password": user_database.password}

        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)  # назначение времени действия access токена
        data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)  # назначение времени действия refresh токена
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGO)
        return {"access_token": access_token, "refresh_token": refresh_token}, 201

    def put_auth(self, req):  # обновит токены
        access_token = req.get('access_token')
        if access_token is None:
            abort(400)
        refresh_token = req.get("refresh_token")
        if refresh_token is None:
            abort(400)
        elif not self.check_token(refresh_token):  # проверка токена
            abort(400)
        try:
            data = jwt.decode(jwt=refresh_token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
        except:
            abort(400)

        user_database = data.get('email')

        user = self.dao.find_user(user_database)  # получим фильтрацию из dao

        data = {"email": user.email,  # заносим данные из таблицы в переменную
                "password": user.password}

        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGO)
        return {"access_token": access_token, "refresh_token": refresh_token}, 201

    def check_token(self, refresh_token):  # метод проверки токена
        try:
            jwt.decode(refresh_token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
            return True
        except:
            return False

    def get_user(self, headers):  # отобразит профиль пользователя
        if 'Authorization' not in headers:
            abort(401)
        data = headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            data = jwt.decode(jwt=token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
            user_email = data.get('email')
            return self.dao.find_user(user_email)
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

    def patch_user(self, headers, req):  # обновление необязательных полей в профиле
        if 'Authorization' not in headers:
            abort(401)
        data = headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            data = jwt.decode(jwt=token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
            user_email = data.get('email')
            self.dao.patch_user(user_email, req)
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

    def put_password(self, headers, req):  # обновление пароля
        if 'Authorization' not in headers:
            abort(401)
        data = headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            data = jwt.decode(jwt=token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
            user_email = data.get('email')
            self.dao.put_password(user_email, req)
        except Exception as e:
            print('JWT Decode Exception or неверные учётные данные', e)
            abort(401)
