from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self):
        return self.movie_dao.get_all()

    def filters(self):
        return self.movie_dao.filters()

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_by_director(self, director_id):
        return self.movie_dao.get_by_director(director_id)

    def get_by_genre(self, genre_id):
        return self.movie_dao.get_by_genre(genre_id)

    def get_by_year(self, year):
        return self.movie_dao.get_by_year(year)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data: dict):
        mid = data.get("id")
        movie = self.movie_dao.get_one(mid)
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        return self.movie_dao.update(movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid)
