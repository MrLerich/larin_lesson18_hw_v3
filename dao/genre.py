from dao.model.genre import Genre

#все что касается Genre методов
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).filter(Genre.id == gid).one()

