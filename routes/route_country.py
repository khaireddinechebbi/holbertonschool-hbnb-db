#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify
from models.country import Country 
from setup import db


country_bp = Blueprint('country', __name__)


@country_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    return jsonify([country.serialize() for country in countries])

@country_bp.route('/countries/<int:country_id>', methods=['GET'])
def get_country(country_id):
    country = Country.query.get_or_404(country_id)
    return jsonify(country.serialize())
