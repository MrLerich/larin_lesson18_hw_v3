# все что касается Director методов
from application.dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors_dao(self):
        return self.session.query(Director).all()

    def get_one_director_id_dao(self, did):
        return self.session.query(Director).filter(Director.id == did).one()
