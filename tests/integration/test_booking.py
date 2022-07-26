from http import HTTPStatus
import server
from tests.conftest import mocker_clubs, mocker_competitions


def test_booking(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 5
    }
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK

    response = client.post(
        '/showSummary', data=mocker_clubs[0])
    assert response.status_code == HTTPStatus.OK
    assert f'Points Board' in response.data.decode()

    response = client.get(
        '/book/' + data['competition'] + '/' + data['club'])
    assert response.status_code == HTTPStatus.OK
    assert f'How many places?' in response.data.decode()

    response = client.post(
        '/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert b'Great-booking complete!' in response.data

    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == HTTPStatus.OK
    assert f'Points available: ' + \
        str(mocker_clubs[0]['points']) in response.data.decode()

    response = client.get('/logout')
    assert response.status_code == 302
