from application.dao.model.models import Movie
from application.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all_movies_service(self) -> list[Movie]:
        return self.movie_dao.get_all_movies_dao()

    def get_one_movie_service(self, mid: int):
        return self.movie_dao.get_one_movie_dao(mid)

    def get_by_director_id_service(self, director_id: int):
        return self.movie_dao.get_by_director_id_dao(director_id)

    def get_by_genre_id_service(self, genre_id: int):
        return self.movie_dao.get_by_genre_id_dao(genre_id)

    def get_by_year_service(self, year: int):
        return self.movie_dao.get_by_year_dao(year)

    def get_movies_by_many_filters_service(self, **kwargs):
        """Универсальный поиск по нескольким параметрам"""
        return self.movie_dao.get_movies_by_many_filters_dao(**kwargs)
        # if director_id is not None:
        #     return self.movie_dao.get_movies_by_many_filters_dao(director_id=director_id)
        # if genre_id is not None:
        #     return self.movie_dao.get_movies_by_many_filters_dao(genre_id=genre_id)
        # if year is not None:
        #     return self.movie_dao.get_movies_by_many_filters_dao(year=year)
        # if id is not None:
        #     return self.movie_dao.get_movies_by_many_filters_dao(id=id)

    def create_movie_service(self, data):
        return self.movie_dao.create_movie_dao(**data)

    def update_movie_service(self, data: dict):
        self.movie_dao.update_movie_dao(data)

        # mid = data.get("id")
        # movie = self.movie_dao.get_one_movie_dao(mid)
        # movie.title = data.get("title")
        # movie.description = data.get("description")
        # movie.trailer = data.get("trailer")
        # movie.year = data.get("year")
        # movie.rating = data.get("rating")
        # movie.genre_id = data.get("genre_id")
        # movie.director_id = data.get("director_id")
        # self.movie_dao.update_movie_dao()
        # return movie

    # def update_part(self, data):
    #     movie_id = data.get('id')
    #     movie = self.get_one_movie_service(movie_id)
    #
    #     if 'title' in data:
    #         movie.title = data.get('title')
    #     if 'description' in data:
    #         movie.description = data.get('description')
    #     if 'trailer' in data:
    #         movie.trailer = data.get('trailer')
    #     if 'year' in data:
    #         movie.year = data.get('year')
    #     if 'rating' in data:
    #         movie.rating = data.get('rating')
    #     if 'genre_id' in data:
    #         movie.genre_id = data.get('genre_id')
    #     if 'genre' in data:
    #         movie.genre = data.get('genre')
    #     if 'director_id' in data:
    #         movie.director_id = data.get('director_id')
    #     if 'director' in data:
    #         movie.director = data.get('director')
    #
    #     self.dao.update_movie_dao(movie)
    #     return movie

    def delete_movie_service(self, mid):
        return self.movie_dao.delete_movie_dao(mid)
