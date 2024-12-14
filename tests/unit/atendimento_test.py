import pytest
from app.controllers.atendimentos import Atendimentos
from tests.repository.atendimentos_fake import FakeAtendimentoRepository


@pytest.fixture
def repository():
  return FakeAtendimentoRepository()

@pytest.fixture
def controller(repository):
  return Atendimentos(repository)

def test_listar_atendimentos(controller:Atendimentos, repository: FakeAtendimentoRepository):
  filters = {'status': 'open'}
  repository.add({'descricao': 'atendimento1', 'status': 'open'})
  repository.add({'descricao': 'atendimento2', 'status': 'open'})
  result = controller.listar_atendimentos(filters)
  assert result == [{'id': 1, 'descricao': 'atendimento1', 'status': 'open'}, {'id': 2, 'descricao': 'atendimento2', 'status': 'open'}]

def test_criar_atendimento(controller:Atendimentos, repository: FakeAtendimentoRepository):
  data = {'descricao': 'Teste'}
  controller.criar_atendimento(data)
  assert repository.get_by_id(1) == {'id': 1, 'descricao': 'Teste'}

def test_atualizar_atendimento(controller:Atendimentos, repository: FakeAtendimentoRepository):
  repository.add({'descricao': 'Teste'})
  id = 1
  data = {'descricao': 'Atualizado'}
  controller.atualizar_atendimento(id, data)
  assert repository.get_by_id(id)['descricao'] == 'Atualizado'

def test_atualizar_atendimento_not_found(controller:Atendimentos, repository: FakeAtendimentoRepository):
  id = 1
  data = {'descricao': 'Atualizado'}
  with pytest.raises(ValueError):
    controller.atualizar_atendimento(id, data)
