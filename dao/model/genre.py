from marshmallow import Schema, fields
from setup_db import db


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())

    def __str__(self):
        """ Отображает название жанра во вьюшках /movies"""
        return self.name


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
