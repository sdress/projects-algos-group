from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models import trip, user
# from flask_app.models.trip import Trip
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route("/")
def index_route():
    return render_template("index2.html")

@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate_newuser(request.form):
        return redirect('/')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }
    new_user = User.register(data)
    session['user_id'] = new_user
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login_user():
    if not User.validate_login(request.form):
        # print(f'line 34: request.form = {request.form}')
        return redirect('/')
    data = {
        'email': request.form['email'],
    }
    user = User.grab_useremail(data)
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# see trips.py for dashboard route