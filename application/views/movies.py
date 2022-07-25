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

    # def get(self):
    #     return movies_schema.dump(movie_service.get_all_movies_service()), 200

    def get(self):
        if len(request.args) > 0:
        #если что-то подали,то ищем по id,нет: выдаем все
            return movies_schema.dump(movie_service.get_movies_by_many_filters_service(
                **request.args
                    # director_id=request.args.get("director_id", type=int),
                    # genre_id=request.args.get("genre_id", type=int),
                    # year=request.args.get("year", type=int),
                    # mid=request.args.get("mid", type=int)
            )
            )
        else:
            return movies_schema.dump(movie_service.get_all_movies_service()), 200

        # if director_id:
        #     movies_by_did = movies_schema.dump(movie_service.get_by_director_id_service(director_id=director_id))
        #     if movies_by_did == []:
        #         return f'Режиссёра с идентификатором №{director_id} нет в базе', 404
        #     return movies_by_did, 200
        # elif genre_id:
        #     movies_by_gid = movies_schema.dump(movie_service.get_by_genre_id_service(genre_id=genre_id))
        #     if movies_by_gid == []:
        #         return f'Жанра с идентификатором №{genre_id} нет в базе', 404
        #     return movies_by_gid, 200
        # elif year:
        #     movies_by_year = movies_schema.dump(movie_service.get_by_year_service(year=year))
        #     if movies_by_year == []:
        #         return f'Фильмов с годом выпуска №{year} нет в базе', 404
        #     return movies_by_year, 200

    def post(self):
        data = request.json
        try:
            movie_schema.load(data)
        except ValidationError as e:
            return f"{e}", 400
        movie_service.create_movie_service(data)
        return "Успешно добавлено", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):

    def get(self, mid: int):
        try:
            movie = movie_service.get_one_movie_service(mid)
        except NoResultFound as e:
            return f"{e}", 400
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        data = request.json
        movie_service.update_movie_service(data)
        return "Успешно обновлено", 201

    def delete(self, mid: int):
        movie_service.delete_movie_service(mid)
        return "Успешно удалено", 204
