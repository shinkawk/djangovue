from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from users.factory import *
from users.views import UserAPIView

class ProfileTest(TestCase):

    def setUp(self):
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.client = APIClient()
        self.auth0User.set_password("abc")
        self.auth0User.save()
        #self.client.login(username= self.auth0User.username, password = "abc")

    def testGet(self):
        response = self.client.get('/profile/')
        print(response)
