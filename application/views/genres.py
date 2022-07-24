from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound


from application.dao.model.schema import GenreSchema
from container import genre_service

genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all_genres_service()
        return genres_schema.dump(genres), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one_genre_service(gid)
        except NoResultFound as e:
            return f"{e}", 400
        return genre_schema.dump(genre), 200
