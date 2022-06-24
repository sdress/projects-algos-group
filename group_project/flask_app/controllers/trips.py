from calendar import c
from flask_app import app
from flask import render_template, redirect,session, request
# from flask_app.models import trip, user
from flask_app.models.trip import Trip
from flask_app.models.user import User

@app.route('/dashboard')
def show_dashboard():
        # TO-DO:
        # check if user in session (logged in)
        # if 'user_id' not in session:
            # return redirect('/logout')

    return render_template('dashboard.html', all_trips=Trip.get_all())

@app.route('/trip/new')
def render_trip_form():
    return render_template('new_trip.html')

@app.route('/trip/save', methods=['POST'])
def create_trip(data):
    if not Trip.validate(request.form):
        return redirect('/trip/new')
    # name, city, state, description, category, cost, posted_by
    data = {
        'name': request.form['name'],
        'city': request.form['city'],
        'state': request.form['state'],
        'description': request.form['description'],
        'category': request.form['category'],
        'cost': request.form['cost'],
        'posted_by' : request.form['posted_by']
    }
    trip = Trip.create(data)
    return redirect('/dashboard')
