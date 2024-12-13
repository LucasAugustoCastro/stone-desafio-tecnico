from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from app.controllers.atendimentos import Atendimentos
from app.schema.atendimentos import AtendimentoSchema, AtendimentoPatchSchema

api = Blueprint('atendimento', __name__, url_prefix='/atendimentos')

@api.route('', methods=['GET'])
@jwt_required()
def get_atendimentos():
  filters = request.args.to_dict()
  atendimentos = Atendimentos()
  atendimentos = atendimentos.listar_atendimentos(filters)
  return jsonify(AtendimentoSchema().dump(atendimentos, many=True))

@api.route('', methods=['POST'])
@jwt_required()
def create_atendimento():
  try:
    data = request.get_json()
    atendimento_data = AtendimentoSchema().load(data)
    atendimentos = Atendimentos()
    atendimento = atendimentos.criar_atendimento(atendimento_data)
    return jsonify(AtendimentoSchema().dump(atendimento)), 201
  except KeyError as e:
    return jsonify({'error': f'Missing field: {str(e)}'}), 400
  except ValidationError as err:
    return jsonify(err.messages), 400
  except ValueError as e:
    return jsonify({'error': str(e)}), 400
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@api.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def update_atendimento(id):
  try:
    data = request.get_json()
    atendimento_data = AtendimentoPatchSchema().load(data)
    atendimento = Atendimentos()
    atendimento = atendimento.atualizar_atendimento(id, atendimento_data)
    return jsonify(AtendimentoSchema().dump(atendimento))
  except KeyError as e:
    return jsonify({'error': f'Missing field: {str(e)}'}), 400
  except ValidationError as err:
    return jsonify(err.messages), 400
  except ValueError as e:
    return jsonify({'error': str(e)}), 400
  except Exception as e:
    return jsonify({'error': str(e)}), 500
