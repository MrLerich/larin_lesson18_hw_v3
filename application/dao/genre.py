# все что касается Genre методов
from application.dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres_dao(self):
        return self.session.query(Genre).all()

    def get_one_genre_dao(self, gid):
        return self.session.query(Genre).filter(Genre.id == gid).one()
