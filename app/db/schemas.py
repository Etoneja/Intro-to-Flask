from app.db import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    comments = db.relationship("Comments", backref="user", lazy="dynamic")


class Comments(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Comments {self.message}>"
