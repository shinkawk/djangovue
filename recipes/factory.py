from users.models import User
from users.factory import UserModelFactory
from tasks.factory import TaskModelFactory, UserTaskModelFactory
from tasks.models import Task, Setting, UserTask
from recipes.models import Recipe, UserRecipe
from factory import DjangoModelFactory, lazy_attribute, SubFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyAttribute
from django.contrib.auth.models import User as auth0User
from social_django.models import UserSocialAuth
import datetime
from django.utils import timezone
from faker import Factory

faker = Factory.create()

class RecipeModelFactory(DjangoModelFactory):
    class Meta:
        model = Recipe
    name = faker.domain_word()
    disc = faker.sentence()
    task1 = SubFactory(TaskModelFactory)
    task2 = SubFactory(TaskModelFactory)
    task3 = SubFactory(TaskModelFactory)
    task4 = SubFactory(TaskModelFactory)
    task5 = SubFactory(TaskModelFactory)
    task6 = SubFactory(TaskModelFactory)
    task7 = SubFactory(TaskModelFactory)
    task8 = SubFactory(TaskModelFactory)
    task9 = SubFactory(TaskModelFactory)
    task10 = SubFactory(TaskModelFactory)

class UserRecipeModelFactory(DjangoModelFactory):
    class Meta:
        model = UserRecipe
    name = faker.domain_word()
    disc = faker.sentence()
