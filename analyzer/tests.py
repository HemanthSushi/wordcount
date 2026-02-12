from django.test import TestCase, Client
from django.urls import reverse

class WordCountTests(TestCase):
    def test_home_page_status(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_analysis_logic(self):
        client = Client()
        response = client.post(reverse('home'), {'fulltext': 'Hello world'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello world')
        self.assertContains(response, '2') # Word count