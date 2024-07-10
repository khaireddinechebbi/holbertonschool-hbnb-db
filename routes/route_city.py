#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify, request
from models.city import City 
from setup import db


city_bp = Blueprint('city', __name__)


@city_bp.route('/cities', methods=['POST'])
def add_city():
    data = request.get_json()
    name = data.get('name')
    population = data.get('population')

    if not name or not population:
        return jsonify({'error': 'Name and population are required'}), 400

    city = City(name=name, population=population)
    db.session.add(city)
    db.session.commit()

    return jsonify({'message': 'City added successfully', 'city': city.serialize()}), 201
@city_bp.route('/cities', methods=['GET'])
def get_cities():
    cities = City.query.all()
    return jsonify([city.serialize() for city in cities])


@city_bp.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get_or_404(city_id)
    return jsonify(city.serialize())
