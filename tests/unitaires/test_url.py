from http import HTTPStatus
import server


def test_index(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


# def test_showSummary(client, mocker):
#     clubs = [{
#         "name": "Simply Lift",
#         "email": "john@simplylift.co",
#         "points": "13"
#     }]
#     competitions = [
#         {
#             "name": "Spring Festival",
#             "date": "2020-03-27 10:00:00",
#             "numberOfPlaces": "25"
#         },
#         {
#             "name": "Fall Classic",
#             "date": "2020-10-22 13:30:00",
#             "numberOfPlaces": "13"
#         }
#     ]
#     mocker.patch.object(server, 'clubs', clubs)
#     mocker.patch.object(server, 'competitions', competitions)
#     response = client.post('/showSummary')
#     print(response)
#     assert response.status_code == 400


# def test_book(client):
#     club = {
#         "name": "Simply Lift",
#         "email": "john@simplylift.co",
#         "points": "13"
#     }
#     competition = {
#         "name": "Spring Festival",
#         "date": "2020-03-27 10:00:00",
#         "numberOfPlaces": "25"
#     }
#     response = client.get('/book/' + competition['name'] + '/' + club['name'])
#     assert response.status_code == 200


# def test_purchasePlaces(client, mocker):
#     clubs = [{
#         "name": "Simply Lift",
#         "email": "john@simplylift.co",
#         "points": "13"
#     }]
#     competitions = [
#         {
#             "name": "Spring Festival",
#             "date": "2020-03-27 10:00:00",
#             "numberOfPlaces": "25"
#         },
#         {
#             "name": "Fall Classic",
#             "date": "2020-10-22 13:30:00",
#             "numberOfPlaces": "13"
#         }
#     ]
#     mocker.patch.object(server, 'clubs', clubs)
#     mocker.patch.object(server, 'competitions', competitions)
#     response = client.post('/purchasePlaces')
#     print(response)
#     assert response.status_code == 400


def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302
