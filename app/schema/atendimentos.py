from marshmallow import fields
from app import db, ma
from app.models.atendimentos import Atendimento

class AtendimentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Atendimento
        load_instance = True
