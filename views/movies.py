from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

from dao.model.movie import movie_schema, Movie
from container import movie_service

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)
        if director_id:
            movies = movie_service.get_by_director(director_id)
        elif genre_id:
            movies = movie_service.get_by_genre(genre_id)
        elif year:
            movies = movie_service.get_by_year(year)
        else:
            movies = movie_service.get_all()
        return movie_schema.dump(movies, many=True)

    def post(self):
        data = request.json
        try:
            movie_schema.load(data)
        except ValidationError as e:
            return f"{e}", 400
        movie_service.create(data)
        return "", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
        except NoResultFound as e:
            return f"{e}", 400
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data["id"] = mid
        try:
            movie_schema.load(data)
        except ValidationError as e:
            return f"{e}", 400
        movie_service.update(data)
        return "Success", 201

    def delete(self, mid):
        movie_service.delete(mid)
        return "Success", 204
