#!/usr/bin/python3
from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Country(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False)

class City(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_code = db.Column(db.String(10), nullable=False)

class Amenity(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Place(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref=db.backref('places', lazy=True))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Review(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    place_id = db.Column(db.String(36), db.ForeignKey('place.id'), nullable=False)
    place = db.relationship('Place', backref=db.backref('reviews', lazy=True))
    user_id = db.Column(db.String(36), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


with app.app_context():
    db.create_all()


@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f'An unexpected error occurred: {str(e)}')
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([user.__dict__ for user in users])

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['email', 'first_name', 'last_name']):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        user = User(
            id=str(uuid.uuid4()),
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        db.session.add(user)
        db.session.commit()

        return jsonify(user.__dict__), 201


@app.route('/countries', methods=['GET', 'POST'])
def manage_countries():
    if request.method == 'GET':
        countries = Country.query.all()
        return jsonify([country.__dict__ for country in countries])

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'code']):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        country = Country(
            id=str(uuid.uuid4()),
            name=data['name'],
            code=data['code']
        )
        db.session.add(country)
        db.session.commit()

        return jsonify(country.__dict__), 201


@app.route('/cities', methods=['GET', 'POST'])
def manage_cities():
    if request.method == 'GET':
        cities = City.query.all()
        return jsonify([city.__dict__ for city in cities])

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'country_code']):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        city = City(
            id=str(uuid.uuid4()),
            name=data['name'],
            country_code=data['country_code']
        )
        db.session.add(city)
        db.session.commit()

        return jsonify(city.__dict__), 201


@app.route('/amenities', methods=['GET', 'POST'])
def manage_amenities():
    if request.method == 'GET':
        amenities = Amenity.query.all()
        return jsonify([amenity.__dict__ for amenity in amenities])

    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data:
            return make_response(jsonify({'error': 'Mandatory field "name" is required'}), 400)

        amenity = Amenity(
            id=str(uuid.uuid4()),
            name=data['name']
        )
        db.session.add(amenity)
        db.session.commit()

        return jsonify(amenity.__dict__), 201


@app.route('/places', methods=['GET', 'POST'])
def manage_places():
    if request.method == 'GET':
        places = Place.query.all()
        return jsonify([place.__dict__ for place in places])

    elif request.method == 'POST':
        data = request.get_json()
        mandatory_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude',
                            'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']
        if not data or not all(key in data for key in mandatory_fields):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        place = Place(
            id=str(uuid.uuid4()),
            name=data['name'],
            description=data['description'],
            address=data['address'],
            city_id=data['city_id'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            host_id=data['host_id'],
            number_of_rooms=data['number_of_rooms'],
            number_of_bathrooms=data['number_of_bathrooms'],
            price_per_night=data['price_per_night'],
            max_guests=data['max_guests']
        )
        db.session.add(place)
        db.session.commit()

        return jsonify(place.__dict__), 201


@app.route('/reviews', methods=['GET', 'POST'])
def manage_reviews():
    if request.method == 'GET':
        reviews = Review.query.all()
        return jsonify([review.__dict__ for review in reviews])

    elif request.method == 'POST':
        data = request.get_json()
        mandatory_fields = ['place_id', 'user_id', 'rating', 'comment']
        if not data or not all(key in data for key in mandatory_fields):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        review = Review(
            id=str(uuid.uuid4()),
            place_id=data['place_id'],
            user_id=data['user_id'],
            rating=data['rating'],
            comment=data['comment']
        )
        db.session.add(review)
        db.session.commit()

        return jsonify(review.__dict__), 201

if __name__ == '__main__':
    app.run(debug=True)
