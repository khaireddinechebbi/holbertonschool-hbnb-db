#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['USE_DATABASE'] = True
    db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
