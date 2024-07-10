#!/usr/bin/python3

import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    JWT_SECRET_KEY = 'super-secret'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///prod.db'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'default-secret-key')


config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig
)


ENV = os.environ.get('ENV', 'development')
Config = config_by_name.get(ENV, DevelopmentConfig)
