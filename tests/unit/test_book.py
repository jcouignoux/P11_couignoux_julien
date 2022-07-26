from http import HTTPStatus
import server
from tests.conftest import mocker_clubs, mocker_competitions


def test_book(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    mocker.patch.object(server, 'competitions', mocker_competitions)
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name']
    }
    response = client.get(
        '/book/' + data['competition'] + '/' + data['club'])
    # '/book/' + str(data["competition"]) + '/' + str(data["club"]), data=data)
    assert response.status_code == HTTPStatus.OK
    assert f'How many places?' in response.data.decode()
