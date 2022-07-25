from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound

from application.dao.model.schema import DirectorSchema
from container import director_service

director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all_directors_service()
        return directors_schema.dump(directors), 200


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did: int):
        try:
            director = director_service.get_one_director_id_service(did)
        except NoResultFound as e:
            return f"{e}", 400
        return director_schema.dump(director), 200
