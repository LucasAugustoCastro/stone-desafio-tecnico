from app.repository.atendimentos import AtendimentoRepository

class Atendimentos():
  def __init__(self, repository:AtendimentoRepository):
    self.repository = repository

  def listar_atendimentos(self, filters, page=1, per_page=10, order_by_id=None):
    return self.repository.get_filtered(filters, page, per_page, order_by_id)

  def criar_atendimento(self, data):
    self.repository.add(data)
    return data

  def atualizar_atendimento(self, id, data):
    atendimento = self.repository.get_by_id(id)
    if not atendimento:
      raise ValueError("Atendimento não encontrado.")
    self.repository.update(atendimento, data)
    return atendimento