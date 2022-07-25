from http import HTTPStatus
import server
from tests.conftest import mocker_clubs, mocker_competitions


def test_passed_competitions(client, mocker):
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
