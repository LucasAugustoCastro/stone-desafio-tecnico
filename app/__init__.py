from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app, supports_credentials=True)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    with app.app_context():
      from .routes import atendimentos, usuarios, auth
      app.register_blueprint(atendimentos.api)
      app.register_blueprint(usuarios.api)
      app.register_blueprint(auth.api)

    return app