from users.models import User, UserResource
from factory import DjangoModelFactory, lazy_attribute
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyAttribute
from django.contrib.auth.models import User as auth0User
from social_django.models import UserSocialAuth
import datetime
from django.utils import timezone
from faker import Factory

faker = Factory.create()

class UserModelFactory(DjangoModelFactory):
    class Meta:
        model = User
    name = faker.name()
    uid = faker.uuid4()
    email = faker.email()
    pic = faker.file_path()
    
class Auth0UserModelFactory(DjangoModelFactory):
    class Meta:
        model = auth0User
    password = faker.password()
    first_name = faker.first_name()
    last_name = faker.last_name()
    username = faker.user_name()
    email = faker.email()
    last_login = timezone.now()
    date_joined = timezone.now()
    is_superuser = 0
    is_staff = 0
    is_active = 1

class UserSocialAuthModelFactory(DjangoModelFactory):
    class Meta:
        model = UserSocialAuth
    provider = "auth0"
    uid = faker.uuid4()
    user_id = FuzzyInteger(1, 100)
    extra_data = FuzzyText()

class UserResorceModelFactory(DjangoModelFactory):
    class Meta:
        model = UserResource
    path = faker.file_path()
    format = "json/text"
    user = 1

def createUserInfo():
    user = UserModelFactory.create()
    auth0User = Auth0UserModelFactory.create()
    social_auth = UserSocialAuthModelFactory(uid=user.uid, user_id=auth0User.id)
    return [user, auth0User, social_auth]