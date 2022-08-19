from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия')})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Поезд на Юму'),
    'description': fields.String(required=True, max_length=255, example='Однажды группа людей повезли преступника...'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtube.com/watch?v=i8GW5sb0s-c'),
    'year': fields.Integer(required=True, example=2010),
    'rating': fields.Float(required=True, example=1.2)})

director: Model = api.model('Режиссёр', {'id': fields.Integer(required=True, example=1),
                                         'name': fields.String(required=True, max_length=100, example='Тарантино')})
