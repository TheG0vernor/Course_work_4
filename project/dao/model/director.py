from marshmallow import Schema, fields

from project.setup.db import db


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
