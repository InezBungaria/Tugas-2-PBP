from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class WatchListTest(TestCase):
    def test_url_html(self):
        response=Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_xml(self):
        response=Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_json(self):
        response=Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
