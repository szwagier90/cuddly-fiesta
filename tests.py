from django.test import TestCase

from django.http import HttpRequest
from django.urls import resolve

from .views import home_page

# Create your tests here.
class TasksPage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/tasks/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/tasks/')
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'tasks/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/tasks/', data={'task_name': 'A new task'})
        self.assertIn('A new task', response.content.decode())
        self.assertTemplateUsed(response, 'tasks/home.html')
