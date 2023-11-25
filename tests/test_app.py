# from fastapi.testclient import TestClient

# from fast_zero.app import app


def test_root_deve_retornar_200_e_ola_mundo(client):
    # client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'messagem': 'Relou o mundo!'}


def test_create_user(client):
    # client = TestClient(app)

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
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'saci',
                'email': 'saci@folclore.br',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'cuca',
            'email': 'cuca@folclore.br',
            'password': 'pirlimpimpim',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'cuca',
        'email': 'cuca@folclore.br',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Usuário apagado!'}
