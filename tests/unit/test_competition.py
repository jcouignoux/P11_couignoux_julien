from http import HTTPStatus
import server
from tests.conftest import mocker_clubs, mocker_competitions


def test_passed_competitions(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', [mocker_competitions[0], ])
    data = mocker_clubs[0]
    response = client.post('/showSummary', data=data)
    assert response.status_code == HTTPStatus.OK
    assert b'Book Places' not in response.data


def test_futur_competitions(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', [mocker_competitions[2], ])
    data = mocker_clubs[0]
    response = client.post('/showSummary', data=data)
    assert response.status_code == HTTPStatus.OK
    assert b'Book Places' in response.data
