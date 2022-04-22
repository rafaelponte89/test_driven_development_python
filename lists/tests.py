from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve

from lists.views import home_page


# Create your tests here.

#class SmokeTest(TestCase):

#    def test_bad_maths(self):
#        self.assertEqual(1+1, 3)

class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') # faz a requisição e obtém a resposta
        self.assertTemplateUsed(response, 'home.html')