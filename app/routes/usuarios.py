from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from app import db
from app.models.usuarios import Usuario
from app.controllers.usuarios import Usuarios as UsuariosController
from app.schema.usuarios import UsuarioSchema, UsuarioPatchSchema

api = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@api.route('', methods=['GET'])
@jwt_required()
def get_usuarios():
  usuarios  = UsuariosController().listar_usuarios()
  return jsonify(UsuarioSchema(many=True).dump(usuarios))

@api.route('', methods=['POST'])
def create_usuario():
  try:
    data = request.get_json()
    usuario = UsuarioSchema().load(data)
    novo_usuario = UsuariosController().criar_usuario(usuario)
    return jsonify(UsuarioSchema().dump(novo_usuario)), 201
  except KeyError as e:
    return jsonify({'error': f'Missing field: {str(e)}'}), 400
  except ValidationError as err:
    return jsonify(err.messages), 400
  except ValueError as e:
    return jsonify({'error': str(e)}), 400
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@api.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_usuario(id):
  usuario = Usuario.query.get_or_404(id)
  return jsonify(UsuarioSchema().dump(usuario))

@api.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def update_usuario(id):
  try:
    data = request.get_json()
    usuario_data = UsuarioPatchSchema().load(data)
    usuario = UsuariosController().atualizar_usuario(id, usuario_data)
    return jsonify(UsuarioSchema().dump(usuario))
  except KeyError as e:
    return jsonify({'error': f'Missing field: {str(e)}'}), 400
  except ValidationError as err:
    return jsonify(err.messages), 400
  except ValueError as e:
    return jsonify({'error': str(e)}), 400
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@api.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_usuario(id):
  try:
    UsuariosController().deletar_usuario(id)
    return '', 204
  except ValueError as e:
    return jsonify({'error': str(e)}), 400
  except Exception as e:
    return jsonify({'error': str(e)}), 500