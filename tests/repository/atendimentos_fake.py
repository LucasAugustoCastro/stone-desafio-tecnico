class FakeAtendimentoRepository:
    def __init__(self):
        self.atendimentos = []
        self.next_id = 1

    def add(self, atendimento):
        atendimento['id'] = self.next_id
        self.atendimentos.append(atendimento)
        self.next_id += 1

    def get_by_id(self, atendimento_id):
        for atendimento in self.atendimentos:
            if atendimento['id'] == atendimento_id:
                return atendimento
        return None

    def get_all(self):
        return self.atendimentos

    def update(self, atendimento, data):
        for i, existing_atendimento in enumerate(self.atendimentos):
            if existing_atendimento['id'] == atendimento['id']:
                self.atendimentos[i] = self.atendimentos[i] | data
                return

    def delete(self, atendimento):
        self.atendimentos = [a for a in self.atendimentos if a['id'] != atendimento['id']]

    def get_filtered(self, filters):
        # Implement filtering logic based on the filters provided
        result = self.atendimentos
        if 'status' in filters:
            result = [a for a in result if a.get('status') == filters['status']]
        return result
