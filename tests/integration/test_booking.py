from http import HTTPStatus
from server import loadClubs, loadCompetitions


def test_booking(client):
    data = {
        'club': loadClubs()[0],
        'competition': loadCompetitions()[0],
        'places': 5
    }
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK

    response = client.post(
        '/showSummary', data=data['club'])
    assert response.status_code == HTTPStatus.OK
    assert f'Welcome,' in response.data.decode()

    response = client.get(
        '/book/' + data['competition']['name'] + '/' + data['club']['name'])
    assert response.status_code == HTTPStatus.OK
    assert f'How many places?' in response.data.decode()

    print(data)
    response = client.post(
        '/purchasePlaces', data={
            'club': data['club']['name'],
            'competition': data['competition']['name'],
            'places': data['places']}
    )
    assert response.status_code == HTTPStatus.OK
    assert b'Great-booking complete!' in response.data
    assert f'Points available: ' + \
        str(int(data['club']['points']) -
            data['places']*3) in response.data.decode()

    response = client.get('/logout')
    assert response.status_code == 302
