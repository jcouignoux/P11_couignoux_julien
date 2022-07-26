from http import HTTPStatus
import server
from tests.conftest import client, mocker_clubs, mocker_competitions


def test_not_exceed_max_places(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 13
    }
    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert b"You cannot book more than 12 places." in response.data


def test_valid_max_point_allowed(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 5
    }
    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert b'Great-booking complete!' in response.data


def test_not_enough_points(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[1]['name'],
        'competition': mocker_competitions[1]['name'],
        'places': 6
    }
    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert b"You doesnt have enough points." in response.data


def test_points_reflected(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 5
    }
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert f'Points available: ' + \
        str(mocker_clubs[0]['points']) in response.data.decode()
