from marshmallow import Schema, fields
from setup_db import db


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())


class DirectorSchema(Schema):
    name = fields.Str()


director_schema = DirectorSchema()
