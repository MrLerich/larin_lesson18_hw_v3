from application.dao.genre import GenreDAO
from application.dao.model.models import Genre


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all_genres_service(self) -> list[Genre]:
        return self.genre_dao.get_all_genres_dao()

    def get_one_genre_service(self, gid: int):
        return self.genre_dao.get_one_genre_dao(gid)

