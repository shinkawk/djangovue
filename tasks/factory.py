from users.models import User
from users.factory import UserModelFactory
from tasks.models import Task, Setting, UserTask
from factory import DjangoModelFactory, lazy_attribute, SubFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyAttribute
from django.contrib.auth.models import User as auth0User
from social_django.models import UserSocialAuth
import datetime
from django.utils import timezone
from faker import Factory

faker = Factory.create()

class TaskModelFactory(DjangoModelFactory):
    class Meta:
        model = Task
    name = faker.domain_word()
    disc = faker.sentence()
    arn = faker.url()

class SettingModelFactory(DjangoModelFactory):
    class Meta:
        model = Setting
    task = SubFactory(TaskModelFactory)
    data = faker.text()
    
class UserTaskModelFactory(DjangoModelFactory):
    class Meta:
        model = UserTask
    name = faker.domain_word()
    disc = faker.sentence()
    user = SubFactory(UserModelFactory)
    task = SubFactory(TaskModelFactory)
    data = faker.text()
