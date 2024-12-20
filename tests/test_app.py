import re
from http import HTTPStatus

from fast_zero.schemas import UserPublic


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
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
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


def test_update_integrity_error(client, user):
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    # alterando user da fixture
    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mypassword',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }


def test_get_user_by_id(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_get_user_by_id_not_found(client):
    response = client.get('/user/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Not Found'}


def test_update_user_not_found(client):
    response = client.put(
        '/users/999',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
