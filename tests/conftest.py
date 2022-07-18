import pytest
from flask import Response
import server


@pytest.fixture
def app():
    app = server.app
    app.config.update({'TESTING': True})

    yield app


class myReponses(Response):

    @property
    def clubs(self):
        clubs = [
            {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "13"
            },
            {
                "name": "Iron Temple",
                "email": "admin@irontemple.com",
                "points": "4"
            },
            {"name": "She Lifts",
             "email": "kate@shelifts.co.uk",
             "points": "12"
             }
        ]
        return clubs

    @property
    def competitions(self):
        competitions = [
            {
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "numberOfPlaces": "13"
            }
        ]
        return competitions
