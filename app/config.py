import os

class Config:
  SECRET_KEY = 'your_secret_key'
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/postgres')
  SQLALCHEMY_TRACK_MODIFICATIONS = False