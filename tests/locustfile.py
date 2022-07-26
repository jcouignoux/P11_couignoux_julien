from locust import HttpUser, task
from tests.conftest import mocker_clubs, mocker_competitions


class ProjectPerfTest(HttpUser):
    data = {
        'club': mocker_clubs[0]['name'],
        'competition': mocker_competitions[0]['name'],
        'places': 5
    }

    @task
    def home(self):
        self.client.get('/')

    @task
    def showSummary(self):
        response = self.client.post('/showSummary', self.data)

    @task
    def book(self):
        response = self.client.get(
            '/book/' + self.data['competition'] + '/' + self.data['club'])

    @task
    def purchasePlaces(self):
        response = self.client.post('/purchasePlaces', self.data)

    @task
    def purchasePlaces(self):
        response = self.client.post('/logout')
