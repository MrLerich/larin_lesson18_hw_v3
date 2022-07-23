from marshmallow import Schema, fields
from setup_db import db


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(255))

    def __str__(self):
        """ Отображает имя режиссера во вьюшках /movies"""
        return self.name


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
