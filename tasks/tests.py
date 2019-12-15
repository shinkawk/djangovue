from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from tasks.factory import *
from users.factory import *

class TasksTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()

        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()

        self.tasks = TaskModelFactory.create_batch(10)
    
    def test_tasks_list(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)

    def test_tasks_get(self):
        response = self.client.get('/tasks/{}/'.format(self.tasks[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/tasks/{}/'.format(self.tasks[0].id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.tasks[0].id)
        self.assertEqual(response.data['name'], self.tasks[0].name)
        self.assertEqual(response.data['disc'], self.tasks[0].disc)

        response = self.client.get('/tasks/{}/'.format(9999999))
        self.assertEqual(response.status_code, 404)

    def test_tasks_post(self):
        response = self.client.post('/tasks/', {})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.post('/tasks/', {})
        self.assertEqual(response.status_code, 405)

    def test_tasks_put(self):
        response = self.client.put('/tasks/{}/'.format(self.tasks[0].id), {})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.put('/tasks/{}/'.format(self.tasks[0].id), {})
        self.assertEqual(response.status_code, 405)

    def test_tasks_delete(self):
        response = self.client.delete('/tasks/{}/'.format(self.tasks[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.delete('/tasks/{}/'.format(self.tasks[0].id))
        self.assertEqual(response.status_code, 405)
