from http import HTTPStatus
import server
from tests.conftest import client, mocker_clubs


def test_board(client, mocker):
    mocker.patch.object(server, 'clubs', mocker_clubs)
    data = {
        'cur_club': mocker_clubs[0]['email']
    }
    response = client.post('/board', data=data)
    assert response.status_code == HTTPStatus.OK
    assert f'Points Board' in response.data.decode()
