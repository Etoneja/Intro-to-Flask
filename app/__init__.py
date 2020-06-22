from flask import Flask
import os

PATH_BASE = os.path.dirname(os.path.abspath(__file__))
PATH_DB = os.path.join(PATH_BASE, "test.db")


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{PATH_DB}"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3308/test"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from . import db, routes
    from .db.schemas import Comments, User

    db.init_app(app)
    routes.init_app(app)

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db.db,
            "Comments": Comments,
            "User": User
        }

    return app
