from marshmallow import Schema, fields, validate

class UsuarioSchema(Schema):
  id = fields.Int(dump_only=True)
  nome = fields.Str(required=True, validate=validate.Length(min=1, max=50))
  email = fields.Email(required=True, validate=validate.Length(max=100))
  senha = fields.Str(required=True, validate=validate.Length(min=6, max=100), load_only=True)

class UsuarioPatchSchema(Schema):
  id = fields.Int(dump_only=True)
  nome = fields.Str(required=False, validate=validate.Length(min=1, max=50))
  email = fields.Email(required=False, validate=validate.Length(max=100))
  senha = fields.Str(required=False, validate=validate.Length(min=6, max=100), load_only=True)