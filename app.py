#!/usr/bin/python3
from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid
import data_manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f'An unexpected error occurred: {str(e)}')
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# User Routes
@app.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def manage_users():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('users'))

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['email', 'first_name', 'last_name']):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)
        
        user_id = str(uuid.uuid4())
        created_at = updated_at = datetime.now().isoformat()
        user_data = {
            'id': user_id,
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'created_at': created_at,
            'updated_at': updated_at
        }

        data_manager.save('users', user_id, user_data)
        return make_response(jsonify(user_data), 201)

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_user(user_id):
    user = data_manager.get('users', user_id)
    if not user:
        return make_response(jsonify({'error': 'User not found'}), 404)

    if request.method == 'GET':
        return jsonify(user)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)

        user['email'] = data.get('email', user['email'])
        user['first_name'] = data.get('first_name', user['first_name'])
        user['last_name'] = data.get('last_name', user['last_name'])
        user['updated_at'] = datetime.now().isoformat()

        data_manager.update('users', user_id, user)
        return jsonify(user)

    elif request.method == 'DELETE':
        data_manager.delete('users', user_id)
        return make_response('User Successfully Deleted', 204)

# Country Routes
@app.route('/countries', methods=['GET', 'POST'], strict_slashes=False)
def manage_countries():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('countries'))

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'code']):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        country_id = str(uuid.uuid4())
        country_data = {
            'id': country_id,
            'name': data['name'],
            'code': data['code']
        }

        data_manager.save('countries', country_id, country_data)
        return make_response(jsonify(country_data), 201)

@app.route('/countries/<country_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_country(country_id):
    country = data_manager.get('countries', country_id)
    if not country:
        return make_response(jsonify({'error': 'Country not found'}), 404)

    if request.method == 'GET':
        return jsonify(country)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)

        country['name'] = data.get('name', country['name'])
        country['code'] = data.get('code', country['code'])

        data_manager.update('countries', country_id, country)
        return jsonify(country)

    elif request.method == 'DELETE':
        data_manager.delete('countries', country_id)
        return make_response('', 204)

# City Routes
@app.route('/cities', methods=['GET', 'POST'], strict_slashes=False)
def manage_cities():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('cities'))

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'country_code']):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        city_id = str(uuid.uuid4())
        city_data = {
            'id': city_id,
            'name': data['name'],
            'country_code': data['country_code']
        }

        data_manager.save('cities', city_id, city_data)
        return make_response(jsonify(city_data), 201)

@app.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_city(city_id):
    city = data_manager.get('cities', city_id)
    if not city:
        return make_response(jsonify({'error': 'City not found'}), 404)

    if request.method == 'GET':
        return jsonify(city)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)

        city['name'] = data.get('name', city['name'])
        city['country_code'] = data.get('country_code', city['country_code'])

        data_manager.update('cities', city_id, city)
        return jsonify(city)

    elif request.method == 'DELETE':
        data_manager.delete('cities', city_id)
        return make_response('', 204)

# Amenity routes
@app.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def manage_amenities():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('amenities'))

    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data:
            return make_response(jsonify({'error': 'Mandatory field "name" is required'}), 400)

        amenity_id = str(uuid.uuid4())
        amenity_data = {
            'id': amenity_id,
            'name': data['name']
        }

        data_manager.save('amenities', amenity_id, amenity_data)
        return make_response(jsonify(amenity_data), 201)

@app.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_amenity(amenity_id):
    amenity = data_manager.get('amenities', amenity_id)
    if not amenity:
        return make_response(jsonify({'error': 'Amenity not found'}), 404)

    if request.method == 'GET':
        return jsonify(amenity)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)

        amenity['name'] = data.get('name', amenity['name'])

        data_manager.update('amenities', amenity_id, amenity)
        return jsonify(amenity)

    elif request.method == 'DELETE':
        data_manager.delete('amenities', amenity_id)
        return make_response('', 204)

# Place Routes
@app.route('/places', methods=['GET', 'POST'], strict_slashes=False)
def manage_places():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('places'))

    elif request.method == 'POST':
        data = request.get_json()
        mandatory_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude',
                            'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']
        if not data or not all(key in data for key in mandatory_fields):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        place_id = str(uuid.uuid4())
        created_at = updated_at = datetime.now().isoformat()
        place_data = {
            'id': place_id,
            'name': data['name'],
            'description': data['description'],
            'address': data['address'],
            'city_id': data['city_id'],
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'host_id': data['host_id'],
            'number_of_rooms': data['number_of_rooms'],
            'number_of_bathrooms': data['number_of_bathrooms'],
            'price_per_night': data['price_per_night'],
            'max_guests': data['max_guests'],
            'created_at': created_at,
            'updated_at': updated_at
        }

        data_manager.save('places', place_id, place_data)
        return make_response(jsonify(place_data), 201)

@app.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_place(place_id):
    place = data_manager.get('places', place_id)
    if not place:
        return make_response(jsonify({'error': 'Place not found'}), 404)

    if request.method == 'GET':
        return jsonify(place)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)

        place.update(data)
        place['updated_at'] = datetime.now().isoformat()

        data_manager.update('places', place_id, place)
        return jsonify(place)

    elif request.method == 'DELETE':
        data_manager.delete('places', place_id)
        return make_response('', 204)

# Review Routes
@app.route('/reviews', methods=['GET', 'POST'], strict_slashes=False)
def manage_reviews():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('reviews'))

    elif request.method == 'POST':
        data = request.get_json()
        mandatory_fields = ['place_id', 'user_id', 'rating']
        if not data or not all(key in data for key in mandatory_fields):
            return make_response(jsonify({'error': 'Mandatory fields are required'}), 400)

        review_id = str(uuid.uuid4())
        created_at = updated_at = datetime.now().isoformat()
        review_data = {
            'id': review_id,
            'place_id': data['place_id'],
            'user_id': data['user_id'],
            'rating': data['rating'],
            'created_at': created_at,
            'updated_at': updated_at
        }

        data_manager.save('reviews', review_id, review_data)
        return make_response(jsonify(review_data), 201)

@app.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_review(review_id):
    review = data_manager.get('reviews', review_id)
    if not review:
        return make_response(jsonify({'error': 'Review not found'}), 404)

    if request.method == 'GET':
        return jsonify(review)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)

        review.update(data)
        review['updated_at'] = datetime.now().isoformat()

        data_manager.update('reviews', review_id, review)
        return jsonify(review)

    elif request.method == 'DELETE':
        data_manager.delete('reviews', review_id)
        return make_response('', 204)

@app.route('/reviews/user/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_reviews(user_id):
    reviews = data_manager.get_all('reviews')
    user_reviews = [review for review in reviews if review['user_id'] == user_id]
    return jsonify(user_reviews)

@app.route('/reviews/place/<place_id>', methods=['GET'], strict_slashes=False)
def get_place_reviews(place_id):
    reviews = data_manager.get_all('reviews')
    place_reviews = [review for review in reviews if review['place_id'] == place_id]
    return jsonify(place_reviews)

@app.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews_for_place(place_id):
    reviews = data_manager.get_all('reviews')
    place_reviews = [review for review in reviews if review['place_id'] == place_id]
    return jsonify(place_reviews)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
