#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify
from models.amenity import Amenity 
from setup import db


amenity_bp = Blueprint('amenity', __name__)


@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.all()
    return jsonify([amenity.serialize() for amenity in amenities])


@amenity_bp.route('/amenities/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.query.get_or_404(amenity_id)
    return jsonify(amenity.serialize())
