from users.models import User
from factory import DjangoModelFactory, lazy_attribute
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyAttribute
from django.contrib.auth.models import User as auth0User
from social_django.models import UserSocialAuth
import datetime
from django.utils import timezone

class UserModelFactory(DjangoModelFactory):
    class Meta:
        model = User
    id = FuzzyInteger(1, 100)
    name = FuzzyText()
    uid = FuzzyText()
    email = "test@mail.com"
    pic = FuzzyText()
    
class Auth0UserModelFactory(DjangoModelFactory):
    class Meta:
        model = auth0User
    id = FuzzyInteger(1, 100)
    password = FuzzyText()
    first_name = FuzzyText()
    last_name = FuzzyText()
    username = FuzzyText()
    email = "test@mail.com"
    last_login = timezone.now()
    date_joined = timezone.now()
    is_superuser = 0
    is_staff = 0
    is_active = 1

class UserSocialAuthModelFactory(DjangoModelFactory):
    class Meta:
        model = UserSocialAuth
    id = FuzzyInteger(1, 100)
    provider = "auth0"
    uid = FuzzyText()
    user_id = FuzzyInteger(1, 100)
    extra_data = FuzzyText()

def createUserInfo():
    user = UserModelFactory.create()
    auth0User = Auth0UserModelFactory.create()
    social_auth = UserSocialAuthModelFactory(uid=user.uid, user_id=auth0User.id)
    return [user, auth0User, social_auth]