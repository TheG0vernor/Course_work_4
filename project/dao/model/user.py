from marshmallow import Schema, fields

from project.setup.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favorite_genre = db.Column(db.String(50))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
