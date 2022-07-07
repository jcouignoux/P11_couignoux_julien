import pytest
from tests.conftest import client
from server import index


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_showSummary(client):
    response = client.get('/showSummary')
    assert response.status_code == 200


def test_book(client):
    response = client.get('/book/<competition>/<club>')
    assert response.status_code == 200


def test_purchasePlaces(client):
    response = client.get('/purchasePlaces')
    assert response.status_code == 200


def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 200
