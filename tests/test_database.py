#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db

# Test configuration
@pytest.fixture(scope='module')
def test_app():
    """
    Create a test Flask app with SQLite in-memory database.
    """
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_sqlite_connection(test_app):
    """
    Test SQLite connection and basic CRUD operations.
    """
    # Perform CRUD operations
    with test_app.app_context():

        user_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = test_app.post('/users', json=user_data)
        assert response.status_code == 201

        # Perform Read operation
        response = test_app.get('/users')
        assert response.status_code == 200
        users = response.json
        assert len(users) == 1

        # Perform Update operation
        user_id = users[0]['id']
        updated_data = {
            'email': 'updated@example.com'
        }
        response = test_app.put(f'/users/{user_id}', json=updated_data)
        assert response.status_code == 200

        # Perform Delete operation
        response = test_app.delete(f'/users/{user_id}')
        assert response.status_code == 204

def test_postgresql_connection():
    """
    Test PostgreSQL connection and basic CRUD operations.
    This test assumes a separate PostgreSQL database configured for testing.
    """
    # Configure PostgreSQL database connection
    os.environ['DATABASE_URL'] = 'postgresql://username:password@localhost/test_db'

    # Create a new Flask app instance
    test_app = Flask(__name__)
    test_app.config.from_object('config.TestConfig')  # Use a separate test configuration if needed
    db.init_app(test_app)

    # Perform CRUD operations
    with test_app.app_context():
        db.create_all()

        # Perform Create operation
        # Example: Create a new place
        place_data = {
            'name': 'Sample Place',
            'description': 'A sample place for testing',
            'address': '123 Test St',
            'city_id': 'sample_city_id',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 'sample_host_id',
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4
        }
        response = test_app.post('/places', json=place_data)
        assert response.status_code == 201

        # Perform Read operation
        response = test_app.get('/places')
        assert response.status_code == 200
        places = response.json
        assert len(places) == 1

        # Perform Update operation
        place_id = places[0]['id']
        updated_data = {
            'price_per_night': 120
        }
        response = test_app.put(f'/places/{place_id}', json=updated_data)
        assert response.status_code == 200

        # Perform Delete operation
        response = test_app.delete(f'/places/{place_id}')
        assert response.status_code == 204

        db.drop_all()

def test_database_transition(test_app):
    """
    Test switching from SQLite to PostgreSQL database.
    """
    # Perform CRUD operations with SQLite
    with test_app.app_context():
        # Perform Create operation
        user_data = {
            'email': 'transition_test@example.com',
            'first_name': 'Jane',
            'last_name': 'Doe'
        }
        response = test_app.post('/users', json=user_data)
        assert response.status_code == 201

    # Switch to PostgreSQL
    os.environ['DATABASE_URL'] = 'postgresql://username:password@localhost/test_db'
    with test_app.app_context():
        # Perform Read operation on PostgreSQL
        response = test_app.get('/users')
        assert response.status_code == 200
        users = response.json
        assert len(users) == 1

        # Clean up
        user_id = users[0]['id']
        response = test_app.delete(f'/users/{user_id}')
        assert response.status_code == 204
