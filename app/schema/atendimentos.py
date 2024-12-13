from marshmallow import fields
from app import db, ma
from app.models.atendimentos import Atendimento

class AtendimentoSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Atendimento
    load_instance = True

class AtendimentoPatchSchema(ma.Schema):
  class Meta:
    model = Atendimento
  
  id_cliente = fields.Integer(required=False)
  angel = fields.String(required=False)
  polo = fields.String(required=False)
  data_limite = fields.Date(required=False)
  data_de_atendimento = fields.Date(required=False)