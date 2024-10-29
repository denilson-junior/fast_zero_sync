import re
from http import HTTPStatus


def test_root_deve_retornar_html_com_frase_inicial(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
    assert (
        re.search(r'<h1 style="[^"]*">Cadastro de pessoas</h1>', response.text)
        is not None
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Jon Snow',
            'email': 'jon.snow@got.com',
            'password': 'kingofthenorth',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Jon Snow',
        'email': 'jon.snow@got.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'Jon Snow', 'email': 'jon.snow@got.com', 'id': 1}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
