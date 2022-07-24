# from application.dao import DirectorDAO
from application.dao.director import DirectorDAO
from application.dao.model.models import Director


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all_directors_service(self) -> list[Director]:
        return self.director_dao.get_all_directors_dao()

    def get_one_director_service(self, did: int):
        return self.director_dao.get_one_director_id_dao(did)
