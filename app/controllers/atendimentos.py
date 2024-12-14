from app.repository.atendimentos import AtendimentoRepository

class Atendimentos():
    def __init__(self, repository:AtendimentoRepository):
        self.repository = repository

    def listar_atendimentos(self, filters):
        return self.repository.get_filtered(filters)
  
    def criar_atendimento(self, data):
        self.repository.add(data)
        return data

    def atualizar_atendimento(self, id, data):
        atendimento = self.repository.get_by_id(id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado.")
        self.repository.update(atendimento, data)
        return atendimento