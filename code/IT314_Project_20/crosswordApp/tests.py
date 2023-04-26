import json

from django.test import TestCase, Client


class TestAuth(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login1(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'ruchir123'})
        print(response.context['fail'])
        
        self.assertEqual(response.status_code, 200)