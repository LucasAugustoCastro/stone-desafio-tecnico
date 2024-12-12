from app.models.atendimentos import Atendimento
from app import db


class Atendimentos():

  def listar_atendimentos(self, filters):
    query = Atendimento.query
    if 'tecnico' in filters:
        query = query.filter_by(angel=filters['tecnico'])
    if 'base_logistica' in filters:
        query = query.filter_by(polo=filters['base_logistica'])
    if 'data_limite_start' in filters and 'data_limite_end' in filters:
        query = query.filter(Atendimento.data_limite.between(filters['data_limite_start'], filters['data_limite_end']))
    if 'data_de_atendimento_start' in filters and 'data_de_atendimento_end' in filters:
        query = query.filter(Atendimento.data_de_atendimento.between(filters['data_de_atendimento_start'], filters['data_de_atendimento_end']))
    return query.all()
 