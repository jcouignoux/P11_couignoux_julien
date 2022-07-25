from http import HTTPStatus
import server
from tests.conftest import client, mocker_clubs


def test_invalid_email(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    response = client.post(
        '/showSummary', data={'email': 'unknown@email.com'})
    data = response.data.decode()
    expected_template_name = "index.html"
    assert response.status_code == HTTPStatus.OK
    assert data.find('Unknown email, please try again.')


def test_valid_email(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    response = client.post(
        '/showSummary', data=mocker_clubs[0])
    data = response.data.decode()
    assert response.status_code == HTTPStatus.OK
    assert data.find('Welcome,')
