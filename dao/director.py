from dao.model.director import Director

#все что касается Director методов
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).filter(Director.id == did).one()

