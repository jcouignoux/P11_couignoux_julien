from http import HTTPStatus
import server


def test_index(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302
