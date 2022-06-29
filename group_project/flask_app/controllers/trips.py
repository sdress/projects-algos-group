from calendar import c
from flask_app import app
from flask import render_template, redirect,session, request, flash
#from flask_app.models import trip, user
from flask_app.models.trip import Trip
from flask_app.models.user import User

@app.route('/dashboard')
def show_dashboard():
    if 'user_id' not in session:
        flash('You must be logged in to access site')
        return redirect('/')
    all_trips=Trip.get_all()
    print(all_trips)
    return render_template('dashboard.html', trips=all_trips)

@app.route('/trip/new')
def render_trip_form():
    return render_template('new_trip.html')

@app.route('/trip/save', methods=['POST'])
def create_trip():
    # print('Made it to trips.py, line 21')
    if not Trip.validate(request.form):
        print('trips.py line 25: validation failed')
        print(f'request.form = {request.form}')
        return redirect('/trip/new')
    data = {
        'name': request.form['name'],
        'city': request.form['city'],
        'state': request.form['state'],
        'description': request.form['description'],
        'category': request.form['category'],
        'cost': request.form['cost'],
        'user_id' : request.form['user_id']
    }
    Trip.create(data)
    print('trips.py line 38: trip saved?')
    return redirect('/dashboard')

@app.route('/delete/trip/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Trip.destroy(data)
    return redirect('/dashboard')
    
