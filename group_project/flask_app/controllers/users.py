from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, request, redirect, session, flash
from flask_app.models import trip, user


@app.route("/")
def index_route():
    return render_template("index.html")
