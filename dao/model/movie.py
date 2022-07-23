from setup_db import db
from marshmallow import fields, Schema


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    trailer = db.Column(db.Text())
    year = db.Column(db.Integer)
    rating = db.Column(db.Float())
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))

    genre = db.relationship("Genre")
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    director_id = fields.Int()
    genre_id = fields.Int()


movie_schema = MovieSchema()

