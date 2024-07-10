#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify
from models.place import Place
from setup import db


place_bp = Blueprint('place', __name__)


@place_bp.route('/places', methods=['GET'])
def get_places():
    places = Place.query.all()
    return jsonify([place.serialize() for place in places])


@place_bp.route('/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get_or_404(place_id)
    return jsonify(place.serialize())
