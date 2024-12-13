from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  senha = db.Column(db.String(100), nullable=False)

  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.set_senha(senha)

  def set_senha(self, senha):
    self.senha = generate_password_hash(senha)
  
  def check_senha(self, senha):
    return check_password_hash(self.senha, senha)