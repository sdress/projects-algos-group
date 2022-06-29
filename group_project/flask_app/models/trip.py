from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, trip

db = 'users_trips'

class Trip:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.city = data['city']
        self.state = data['state']
        self.description = data['description']
        self.category = data['category']
        self.cost = data['cost']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # CREATE method
    @classmethod
    def create(cls, data):
        query = "INSERT INTO trips (name, city, state, description, category, cost, user_id, created_at, updated_at) VALUES ( %(name)s, %(city)s, %(state)s, %(description)s, %(category)s, %(cost)s, %(user_id)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM trips WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        if results == False:
            return None
        print(results)
        return results

    # READ methods
    @classmethod
    def get_all(cls):
        query = "SELECT trips.* FROM trips;"
        results = connectToMySQL(db).query_db(query)
        # print(results)
        if results == False:
            print('From trip.py line 33: None found')
            return None
        all_list = []
        for row in results:
            all_list.append(row)
        return all_list

    @classmethod
    def get_all_with_username(cls):
        query = "SELECT trips.*, users.first_name FROM trips LEFT JOIN users ON users.id = trips.user_id;"
        results = connectToMySQL(db).query_db(query)
        # print(results)
        if results == False:
            print('From trip.py line 46: None found')
            return None
        all_list = []
        for row in results:
            all_list.append(row)
        return all_list

    @classmethod
    def get_all_by_state(cls, data):
        query = "SELECT * FROM trips WHERE state = %(state)s;"
        results = connectToMySQL(db).query_db(query, data)
        if results == False:
            print('From trip.py line 45: None found')
            return None
        all_by_state = []
        for row in results:
            all_by_state.append(row)
        return all_by_state
    
    @classmethod
    def get_states_list(cls):
        query = "SELECT trips.state from trips;"
        results = connectToMySQL(db).query_db(query)
        if results == False:
            print('From trip.py line 57: None found')
            return None
        states_list = []
        for state in results:
            states_list.append(state)
        return states_list

    # UPDATE method
    @classmethod
    def update(cls, data):
        query = "UPDATE trips SET name = %(name)s,  city = %(city)s, state = %(state)s, description = %(description)s, category = %(category)s, cost = %(cost)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    # DESTROY method
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM trips WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # TRIP FORM VALIDATIONS
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Name of activity must be at least 3 characters')
            is_valid = False
        if len(data['city'])< 3:
            flash('Please include a city')
            is_valid = False
        if len(data['state']) < 2:
            flash('Please select a state')
            is_valid = False
        if len(data['description']) < 3:
            flash('Please provide a description')
            is_valid = False
        if data['category'] == None:
            flash('Please provide a category')
            is_valid = False
        if not 'cost' in data:
            flash('Please input cost')
            is_valid = False
        if not 'user_id' in data:
            print('User not found')
            is_valid = False
        return is_valid
