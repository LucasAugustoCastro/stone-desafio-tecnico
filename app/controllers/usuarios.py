from sqlalchemy.exc import IntegrityError

from app import db
from app.models.usuarios import Usuario

class Usuarios:
  def listar_usuarios(self):
    return Usuario.query.all()

  def criar_usuario(self, data):
    novo_usuario = Usuario(**data)
    try:
      db.session.add(novo_usuario)
      db.session.commit()
      return novo_usuario
    except IntegrityError:
      db.session.rollback()
      raise ValueError("Erro de integridade no banco de dados.")

  def atualizar_usuario(self, id, data):
    usuario:Usuario = Usuario.query.get(id)
    if not usuario:
      raise ValueError("Usuário não encontrado.")
    for attr in data:
      if attr == 'senha':
        usuario.set_senha(data['senha'])
      if hasattr(usuario, attr):
        setattr(usuario, attr, data[attr])
    try:
      db.session.commit()
      return usuario
    except IntegrityError:
      db.session.rollback()
      raise ValueError("Erro de integridade no banco de dados.")

  def deletar_usuario(self, id):
    usuario = Usuario.query.get(id)
    if not usuario:
      raise ValueError("Usuário não encontrado.")
    try:
      db.session.delete(usuario)
      db.session.commit()
    except IntegrityError:
      db.session.rollback()
      raise ValueError("Erro de integridade no banco de dados.")