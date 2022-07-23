from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound

from dao.model.genre import genre_schema
from container import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genre_schema.dump(genres, many=True), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
        except NoResultFound as e:
            return f"{e}", 400
        return genre_schema.dump(genre), 200
