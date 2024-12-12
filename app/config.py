import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:1234@localhost/stone')
    SQLALCHEMY_TRACK_MODIFICATIONS = False