import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app, db
from app.models.atendimentos import Atendimento
from flask_jwt_extended import create_access_token

@pytest.fixture
def app() -> Flask:
  app = create_app()
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
  app.config['TESTING'] = True

  with app.app_context():
    db.create_all()
    yield app
    db.session.remove()
    db.drop_all()

@pytest.fixture
def client(app: Flask) -> FlaskClient:
  return app.test_client()

@pytest.fixture
def token(app: Flask) -> str:
  with app.app_context():
    return create_access_token(identity='test_user')

def test_get_atendimentos(client: FlaskClient, token: str, app: Flask) -> None:
  with app.app_context():
    atendimento = Atendimento(id_cliente=1, angel='Angel Teste', polo='Polo Teste', data_limite='2023-12-31')
    db.session.add(atendimento)
    db.session.commit()

  response = client.get('/atendimentos', headers={'Authorization': f'Bearer {token}'})
  assert response.status_code == 200
  assert 'Angel Teste' in response.get_data(as_text=True)

def test_update_atendimento(client: FlaskClient, token: str, app: Flask) -> None:
    
  with app.app_context():
    atendimento = Atendimento(id_cliente=1, angel='Angel Teste', polo='Polo Teste', data_limite='2023-12-31')
    db.session.add(atendimento)
    db.session.commit()

    data = {
      'angel': 'Angel Atualizado'
    }
    response = client.patch(f'/atendimentos/{atendimento.id}', json=data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert 'Angel Atualizado' in response.get_data(as_text=True)

    updated_atendimento = Atendimento.query.get(atendimento.id)
    assert updated_atendimento.angel == 'Angel Atualizado'

def test_create_atendimento(client: FlaskClient, token: str, app:Flask) -> None:
  with app.app_context():
    data = {
      'id_cliente': 1,
      'angel': 'Novo Angel',
      'polo': 'Novo Polo',
      'data_limite': '2023-12-31'
    }
    response = client.post('/atendimentos', json=data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201
    assert 'Novo Angel' in response.get_data(as_text=True)

    new_atendimento = Atendimento.query.get(response.json['id'])
    assert new_atendimento is not None

def test_get_atendimentos_filter_tecnico(client: FlaskClient, token: str, app: Flask) -> None:
  with app.app_context():
    atendimento1 = Atendimento(id_cliente=1, angel='Angel Teste 1', polo='Polo Teste', data_limite='2023-12-31')
    atendimento2 = Atendimento(id_cliente=2, angel='Angel Teste 2', polo='Polo Teste', data_limite='2023-12-31')
    db.session.add(atendimento1)
    db.session.add(atendimento2)
    db.session.commit()

  response = client.get('/atendimentos?tecnico=Angel Teste 1', headers={'Authorization': f'Bearer {token}'})
  assert response.status_code == 200
  assert 'Angel Teste 1' in response.get_data(as_text=True)
  assert 'Angel Teste 2' not in response.get_data(as_text=True)

def test_get_atendimentos_filter_base_logistica(client: FlaskClient, token: str, app: Flask) -> None:
  with app.app_context():
    atendimento1 = Atendimento(id_cliente=1, angel='Angel Teste', polo='Polo Teste 1', data_limite='2023-12-31')
    atendimento2 = Atendimento(id_cliente=2, angel='Angel Teste', polo='Polo Teste 2', data_limite='2023-12-31')
    db.session.add(atendimento1)
    db.session.add(atendimento2)
    db.session.commit()

  response = client.get('/atendimentos?base_logistica=Polo Teste 1', headers={'Authorization': f'Bearer {token}'})
  assert response.status_code == 200
  assert 'Polo Teste 1' in response.get_data(as_text=True)
  assert 'Polo Teste 2' not in response.get_data(as_text=True)

def test_get_atendimentos_filter_data_limite(client: FlaskClient, token: str, app: Flask) -> None:
  with app.app_context():
    atendimento1 = Atendimento(id_cliente=1, angel='Angel Teste', polo='Polo Teste', data_limite='2023-12-30')
    atendimento2 = Atendimento(id_cliente=2, angel='Angel Teste', polo='Polo Teste', data_limite='2023-12-31')
    db.session.add(atendimento1)
    db.session.add(atendimento2)
    db.session.commit()

  response = client.get('/atendimentos?data_limite_start=2023-12-31&data_limite_end=2023-12-31', headers={'Authorization': f'Bearer {token}'})
  assert response.status_code == 200
  assert '2023-12-31' in response.get_data(as_text=True)
  assert '2023-12-30' not in response.get_data(as_text=True)

def test_get_atendimentos_filter_data_de_atendimento(client: FlaskClient, token: str, app: Flask) -> None:
  with app.app_context():
    atendimento1 = Atendimento(id_cliente=1, angel='Angel Teste', polo='Polo Teste', data_limite='2023-12-31', data_de_atendimento='2023-12-30')
    atendimento2 = Atendimento(id_cliente=2, angel='Angel Teste', polo='Polo Teste', data_limite='2023-12-31', data_de_atendimento='2023-12-31')
    db.session.add(atendimento1)
    db.session.add(atendimento2)
    db.session.commit()

  response = client.get('/atendimentos?data_de_atendimento_start=2023-12-31&data_de_atendimento_end=2023-12-31', headers={'Authorization': f'Bearer {token}'})
  assert response.status_code == 200
  assert '2023-12-31' in response.get_data(as_text=True)
  assert '2023-12-30' not in response.get_data(as_text=True)


