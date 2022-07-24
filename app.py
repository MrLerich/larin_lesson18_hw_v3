from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from application.views.directors import director_ns
from application.views.movies import movie_ns
from application.views.genres import genre_ns


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())
register_extensions(app)

if __name__ == "__main__":
    app.run()
