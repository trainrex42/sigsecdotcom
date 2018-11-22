from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def hello_world():
  return render_template("index.html")