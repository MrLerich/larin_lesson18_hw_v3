from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound

from dao.model.director import director_schema
from container import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return director_schema.dump(directors, many=True), 200


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        try:
            director = director_service.get_one(did)
        except NoResultFound as e:
            return f"{e}", 400
        return director_schema.dump(director), 200
