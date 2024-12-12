from flask import Blueprint, jsonify, request

from app.controllers.atendimentos import Atendimentos
from app.schema.atendimentos import AtendimentoSchema

api = Blueprint('atendimento', __name__, url_prefix='/atendimentos')

@api.route('', methods=['GET'])
def get_atendimentos():
    filters = request.args.to_dict()
    atendimentos = Atendimentos()
    atendimentos = atendimentos.listar_atendimentos(filters)
    return jsonify(AtendimentoSchema().dump(atendimentos, many=True))