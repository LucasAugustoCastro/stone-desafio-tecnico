from app import db
from app.models.atendimentos import Atendimento
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class AtendimentoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, atendimento: Atendimento):
        try:
            self.session.add(atendimento)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

    def get_by_id(self, atendimento_id):
        return Atendimento.query.get(atendimento_id)

    def get_all(self):
        return Atendimento.query.all()

    def update(self, atendimento: Atendimento, data: dict):
        try:  
            atendimento.id_cliente = data.get('id_cliente', atendimento.id_cliente)
            atendimento.angel = data.get('angel', atendimento.angel)
            atendimento.polo = data.get('polo', atendimento.polo)
            atendimento.data_limite = data.get('data_limite', atendimento.data_limite)
            atendimento.data_de_atendimento = data.get('data_de_atendimento', atendimento.data_de_atendimento)
            self.session.add(atendimento)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

    def delete(self, atendimento: Atendimento):
        try:
            self.session.delete(atendimento)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

    def get_filtered(self, filters):
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
