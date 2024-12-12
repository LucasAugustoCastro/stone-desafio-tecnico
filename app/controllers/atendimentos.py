from sqlalchemy.exc import IntegrityError

from app import db
from app.models.atendimentos import Atendimento

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
  
  def criar_atendimento(self, data):
    try:
      db.session.add(data)
      db.session.commit()
    except IntegrityError:
      db.session.rollback()
      raise ValueError("Erro de integridade no banco de dados.")
    return data