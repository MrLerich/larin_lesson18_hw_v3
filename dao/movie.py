from sqlalchemy.exc import NoResultFound

from dao.model.movie import Movie

#все что касается Movie методов
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def filters(self):
        return self.session.query(Movie)

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def get_by_director(self, did):
        movies = self.filters()
        return movies.filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        movies = self.filters()
        return movies.filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        movies = self.filters()
        return movies.filter(Movie.year == year).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie):
        self.session.update(movie)
        self.session.commit()

    def delete(self, mid):
        try:
            movie = self.get_one(mid)
        except NoResultFound as e:
            return f"{e}"
        self.session.delete(movie)
        self.session.commit()


