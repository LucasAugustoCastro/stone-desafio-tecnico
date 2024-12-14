from datetime import timedelta

from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from app.models.usuarios import Usuario

api = Blueprint('auth', __name__, url_prefix='/auth')

@api.route('/login', methods=['POST'])
def login():
  data = request.get_json()

  if not data or not data.get('email') or not data.get('senha'):
    return jsonify({'message': 'Invalid input'}), 400

  user = Usuario.query.filter_by(email=data['email']).first()

  if not user or not check_password_hash(user.senha, data['senha']):
    return jsonify({'message': 'Email ou senha incorretos'}), 401

  user_info = {
    "user_id": user.id,
    "email": user.email,
  }
  access_token = create_access_token(
    identity=str(user.id), 
    additional_claims={'user': user_info},
    expires_delta=timedelta(hours=1))

  return jsonify({'access_token': access_token}), 200