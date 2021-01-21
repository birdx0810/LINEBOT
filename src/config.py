# -*- coding: UTF-8 -*-
import os
import json

root_path = path.abspath(path.dirname(__file__))
load_dotenv(path.join(root_path, '.env'))

def get_server_config():
    """
    Get server configurations
    """
    path = os.path.abspath(
        f"{os.path.abspath(__file__)}/../config/server.json"
    )

    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist")

    with open(path, "r") as config_file:
        config = json.load(config_file)

    return config

def get_db_config():
    """
    Get database configurations
    """
    path = os.path.abspath(
        f"{os.path.abspath(__file__)}/../config/db.json"
    )

    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist")

    with open(path, "r") as config_file:
        config = json.load(config_file)

    return config

"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')