from http import HTTPStatus
import server
from tests.conftest import client, mocker_clubs, mocker_competitions


# class TestBook:

#     @classmethod
# def setup_class(cls, mocker):
#     mocker.patch.object(server, 'clubs', mocker_clubs)
#     mocker.patch.object(server, 'competitions', mocker_competitions)

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


def test_not_enough_places(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 30
    }
    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert response.url == '/purchasePlaces'
    assert b'Great-booking complete!' in response.data
    # assert f"Max places number must be less than {mocker_competitions[0]['numberOfPlaces']}" in response.data.decode()


def test_not_enough_points(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 30
    }
    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert f"Max places number must be less than {mocker_competitions[0]['numberOfPlaces']}" in response.data.decode(
    )


def test_not_exceed_max_places(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 30
    }
    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert f"Max places number must be less than 12" in response.data.decode(
    )