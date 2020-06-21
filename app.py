from flask import Flask
import os
from db.db import db
from routes.routes import bp

PATH_BASE = os.path.dirname(os.path.abspath(__file__))
PATH_DB = os.path.join(PATH_BASE, "test.db")


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{PATH_DB}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
