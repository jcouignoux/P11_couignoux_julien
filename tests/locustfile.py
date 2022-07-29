from locust import HttpUser, task
from server import competitions, clubs


class ProjectPerfTest(HttpUser):
    data = {
        'club': clubs[0]['name'],
        'competition': competitions[0]['name'],
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
    def logout(self):
        response = self.client.get('/logout')
