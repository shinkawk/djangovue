from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from tasks.factory import *
from users.factory import *

class TasksTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.tasks = TaskModelFactory.create_batch(10)

        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()
    
    def test_tasks_list(self):
        response = self.client.get('/tasks/')
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

class InnventoryTasksTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.userTasks = UserTaskModelFactory.create_batch(10, user=self.user)

        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()
    
    def test_usertasks_list(self):
        response = self.client.get('/inventory/tasks/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/inventory/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
    
    def test_usertasks_get(self):
        response = self.client.get('/inventory/tasks/{}'.format(self.userTasks[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/inventory/tasks/{}'.format(self.userTasks[0].id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.userTasks[0].id)
        self.assertEqual(response.data['name'], self.userTasks[0].name)
        self.assertEqual(response.data['disc'], self.userTasks[0].disc)

        random_user = UserModelFactory.create(id=999999, uid="abcdefg1234")
        random_usertask = UserTaskModelFactory.create(user=random_user)
        response = self.client.get('/inventory/tasks/{}'.format(random_usertask.id))
        self.assertEqual(response.status_code, 400)

    def test_usertasks_post(self):
        task = TaskModelFactory.create()
        response = self.client.post('/inventory/tasks/', {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task': task.id, 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.post('/inventory/tasks/', {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task': task.id , 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UserTask.objects.get(name='new usertask').disc, 'this is a disc')
        self.assertEqual(UserTask.objects.get(name='new usertask').user, self.user)
        self.assertEqual(UserTask.objects.get(name='new usertask').task, task)

        response = self.client.post('/inventory/tasks/', {'name':'new usertask', 'disc': 'this is a disc', 'user': 99999, 'task': task.id, 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 400)

    def test_usertasks_put(self):
        task = TaskModelFactory.create()
        response = self.client.put('/inventory/tasks/{}'.format(self.userTasks[0].id), {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task': task.id, 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.put('/inventory/tasks/{}'.format(self.userTasks[0].id), {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task': task.id, 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserTask.objects.get(id=self.userTasks[0].id).name, 'new usertask')
        self.assertEqual(UserTask.objects.get(id=self.userTasks[0].id).disc, 'this is a disc')
        self.assertEqual(UserTask.objects.get(id=self.userTasks[0].id).user, self.user)
        self.assertEqual(UserTask.objects.get(id=self.userTasks[0].id).task, task)
        self.assertEqual(UserTask.objects.get(id=self.userTasks[0].id).data, "hogehoge")

        response = self.client.put('/inventory/tasks/{}'.format(self.userTasks[0].id), {'name':'new usertask', 'disc': 'this is a disc', 'user': 999999, 'task': task.id, 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 400)

        response = self.client.put('/inventory/tasks/99999', {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task': task.id, 'data': 'hogehoge'})
        self.assertEqual(response.status_code, 400)
    
    def test_usertasks_delete(self):
        response = self.client.delete('/inventory/tasks/{}'.format(self.userTasks[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.delete('/inventory/tasks/{}'.format(self.userTasks[0].id))
        self.assertEqual(response.status_code, 204)
        self.assertRaises(UserTask.DoesNotExist, UserTask.objects.get, id=self.userTasks[0].id)

        response = self.client.delete('/inventory/tasks/99999')
        self.assertEqual(response.status_code, 400)

        random_user = UserModelFactory.create(id=999999, uid="abcdefg1234")
        random_usertask = UserTaskModelFactory.create(user=random_user)
        response = self.client.delete('/inventory/tasks/{}'.format(random_usertask.id))
        self.assertEqual(response.status_code, 400)
