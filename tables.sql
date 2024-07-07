#!/usr/bin/python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app = Flask(__name__)

if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
    if not os.path.exists(os.path.join(app.root_path, 'dev.db')):
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
