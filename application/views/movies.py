from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

from application.dao.model.schema import MovieSchema
from container import movie_service

movie_ns: Namespace = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        return movies_schema.dump(movie_service.get_all_movies_service())



    def post(self):
        data = request.json
        try:
            movie_schema.load(data)
        except ValidationError as e:
            return f"{e}", 400
        movie_service.create_movie_service(data)
        return "", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)
        mid = request.args.get("mid", type=int)
        if director_id:
            director = movie_service.get_by_director_id_service(director_id)
            if director is None:
                return f'Режиссёра с идентификатором №{director_id} нет в базе', 404
            return director, 200
    #     elif genre_id:
    #         return movie_service.get_by_genre_service(genre_id)
    #     elif year:
    #         return movie_service.get_by_year_service(year)
    #     elif mid:
    #         return movie_service.get_one_movie_service(mid)
    # return movie_schema.dump(movies, many=True)


    def get(self, mid):
        try:
            movie = movie_service.get_one_movie_service(mid)
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
        movie_service.update_movie_dao(data)
        return "Success", 201

    def delete(self, mid):
        movie_service.delete_movie_service(mid)
        return "Success", 204
