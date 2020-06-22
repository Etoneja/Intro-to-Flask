from flask import render_template, redirect, request, url_for, Blueprint
from app.db import db
from app.db.schemas import Comments

bp = Blueprint(
    'bp', __name__, template_folder='templates'
)


@bp.route("/sign", methods=["GET"])
def sign():
    return render_template("sign.html")


@bp.route("/", methods=["GET"])
def home():
    results = Comments.query.all()
    return render_template(
        "example.html", items=results
    )


@bp.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    message = request.form["message"]

    new_message = Comments(name=name, message=message)
    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for("bp.home"))
