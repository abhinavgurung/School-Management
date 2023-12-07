"""Configuration variables"""
import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

class BaseConfig:
    ENV = 'development'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS= True

class DevelopmentConfig(BaseConfig):
    pass