from app.db import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    comments = db.relationship("Comment", backref="user", lazy="dynamic")
    projects = db.relationship(
        "Project",
        secondary="user_projects",
        backref="user", lazy="dynamic"
    )


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Comment {self.message}>"


class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


db.Table(
    "user_projects",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("project_id", db.Integer, db.ForeignKey("project.id"))
)
