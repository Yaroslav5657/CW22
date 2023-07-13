import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or '123456512' 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False