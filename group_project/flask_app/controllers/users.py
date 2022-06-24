from crypt import methods
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, request, redirect, session, flash
from flask_app.models import trip, user
from flask_app.models.trip import Trip
from flask_app.models.user import User


@app.route("/")
def index_route():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate_newuser():
        return redirect('/')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_pw_hash(request.form['password']),
    }
    new_user = User.create(data)
    session['user_id'] = new_user.id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login_user():
    if not User.validate_login():
        return redirect('/')

    data = {
        'email': request.form['email']
    }
    user = User.grab_useremail(data)
    if not user:
        flash('Email not found')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password does not match')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

# see trips.py for dashboard route