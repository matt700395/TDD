#firstapp/tests.py
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from firstapp.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))#3
        self.assertIn(b'<title>To-Do lists</title>', response.content) #4
        self.assertTrue(response.content.endwith(b'</html>'))#5
