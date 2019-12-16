from django.test import TestCase
from users.factory import Auth0UserModelFactory, UserSocialAuthModelFactory
from users.models import User as User
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate

class AuthroizeTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.auth0User = Auth0UserModelFactory.create()
        self.social_auth = UserSocialAuthModelFactory(user_id=self.auth0User.id, extra_data={"picture":"mydog.jpg"})

        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()
    
    def test_authroize(self):
        response = self.client.get('/authorize/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)

        response = self.client.get('/authorize/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(uid=self.social_auth.uid).name, self.social_auth.user.username)
        self.assertEqual(User.objects.get(uid=self.social_auth.uid).email, self.social_auth.user.email)
        self.assertEqual(User.objects.get(uid=self.social_auth.uid).pic, self.social_auth.extra_data['picture'])
