from app import db

class Atendimento(db.Model):
  # __tablename__ == 'atendimento'
  id = db.Column(db.Integer, primary_key=True)
  id_cliente = db.Column(db.Integer, nullable=False)
  angel = db.Column(db.String(50), nullable=False)
  polo = db.Column(db.String(50), nullable=False)
  data_limite = db.Column(db.Date, nullable=False)
  data_de_atendimento = db.Column(db.Date, nullable=True)

  def to_dict(self):
    return {
      'id': self.id,
      'id_cliente': self.id_cliente,
      'angel': self.angel,
      'polo': self.polo,
      'data_limite': self.data_limite,
      'data_de_atendimento': self.data_de_atendimento
    }