from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from users.factory import *
from users.views import UserAPIView

class ProfileTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.resources = UserResorceModelFactory.create_batch(10, user=self.user)
        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()

    def test_profile_get(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['name'], self.user.name)
        self.assertEqual(response.data['uid'], self.user.uid)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['pic'], self.user.pic)
        self.assertEqual(len(response.data['resources']), 10)

    def test_profile_post(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 403)
        
        self.client.login(username= self.auth0User.username, password = self.password)
        response = self.client.post('/profile/', {'name': 'user1', 'email': 'test@mail.com', 'pic':'dog.jpg'} )
        self.assertEqual(response.status_code, 405)

    def test_profile_put(self):
        response = self.client.put('/profile/',  {'name': 'user1', 'email': 'test@mail.com', 'pic':'dog.jpg'})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)

        response = self.client.put('/profile/', {'name': 'user1', 'email': 'test@mail.com', 'pic':'dog.jpg'} )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=self.user.id).name, 'user1')
        self.assertEqual(User.objects.get(id=self.user.id).email, 'test@mail.com')
        self.assertEqual(User.objects.get(id=self.user.id).pic, 'dog.jpg')

        response = self.client.put('/profile/', {'id': 5 ,'name': 'user1', 'uid':'this should fail' ,'email': 'test@mail.com', 'pic':'dog.jpg'} )
        self.assertEqual(User.objects.get(id=self.user.id).uid, self.user.uid)
        self.assertEqual(User.objects.get(id=self.user.id).id, self.user.id)

        response = self.client.put('/profile/', {'name': 'user1', 'email': 'test@mail.com'} )
        self.assertEqual(response.status_code, 400)

    def test_profile_delete(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.delete('/profile/')
        self.assertEqual(response.status_code, 204)
        self.assertRaises(User.DoesNotExist, User.objects.get, id=self.user.id)

class InventoryFilesTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.resources = UserResorceModelFactory.create_batch(10, user=self.user)
        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()

    def test_inventoryfiles_get(self):
        response = self.client.get('/inventory/files/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/inventory/files/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
    
    def test_inventoryfiles_post(self):
        response = self.client.post('/inventory/files/', {})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        response = self.client.post('/inventory/files/', {})
        self.assertEqual(response.status_code, 405)
    
    def test_inventoryfiles_put(self):
        response = self.client.put('/inventory/files/', {})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        response = self.client.put('/inventory/files/', {})
        self.assertEqual(response.status_code, 405)
    
    def test_inventoryfiles_delete(self):
        response = self.client.delete('/inventory/files/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        response = self.client.delete('/inventory/files/')
        self.assertEqual(response.status_code, 405)
