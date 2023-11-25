from fastapi.testclient import TestClient

from fast_zero.app import app
from fast_zero.schemas import UserPublic

client = TestClient(app)


def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'messagem': 'Relou o mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'saci',
            'email': 'saci@folclore.br',
            'password': 'carapuća',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'saci',
        'email': 'saci@folclore.br',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'cuca',
            'email': 'cuca@folclore.br',
            'password': 's1t10',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'cuca',
        'email': 'cuca@folclore.br',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'Usuário apagado!'}
