from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from tasks.factory import *
from users.factory import *
from recipes.factory import RecipeModelFactory, UserRecipeModelFactory
from recipes.models import UserRecipe

class RecipesTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.recipes = RecipeModelFactory.create_batch(10)

        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()
    
    def test_receipes_list(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)

    def test_receipes_get(self):
        response = self.client.get('/recipes/{}/'.format(self.recipes[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/recipes/{}/'.format(self.recipes[0].id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.recipes[0].id)
        self.assertEqual(response.data['name'], self.recipes[0].name)
        self.assertEqual(response.data['disc'], self.recipes[0].disc)

        response = self.client.get('/recipes/{}/'.format(9999999))
        self.assertEqual(response.status_code, 404)

    def test_receipes_post(self):
        response = self.client.post('/recipes/', {})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.post('/recipes/', {})
        self.assertEqual(response.status_code, 405)

    def test_receipes_put(self):
        response = self.client.put('/recipes/{}/'.format(self.recipes[0].id), {})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.put('/recipes/{}/'.format(self.recipes[0].id), {})
        self.assertEqual(response.status_code, 405)

    def test_receipes_delete(self):
        response = self.client.delete('/recipes/{}/'.format(self.recipes[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.delete('/recipes/{}/'.format(self.recipes[0].id))
        self.assertEqual(response.status_code, 405)

class InnventoryRecipesTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, self.auth0User, self.social_auth = createUserInfo()
        self.userTasks = UserTaskModelFactory.create_batch(10, user=self.user)
        self.userRecipes = UserRecipeModelFactory.build_batch(5, user=self.user)
        self.userRecipes[0].task1 = self.userTasks[0] 
        self.userRecipes[0].task2 = self.userTasks[1] 
        self.userRecipes[0].task3 = self.userTasks[2] 
        self.userRecipes[0].task4 = self.userTasks[3] 
        self.userRecipes[0].task5 = self.userTasks[4] 
        self.userRecipes[1].task1 = self.userTasks[5] 
        self.userRecipes[2].task1 = self.userTasks[6] 
        self.userRecipes[3].task1 = self.userTasks[7] 
        self.userRecipes[4].task1 = self.userTasks[8] 
        for x in self.userRecipes:
            x.save()
        random_user = UserModelFactory.create(id=999999, uid="abcdefg1234")
        self.random_userrecipe = UserRecipeModelFactory.build(user=random_user)
        self.random_userrecipe.task1 = UserTaskModelFactory.create(user=random_user)
        self.random_userrecipe.save()

        self.password = "hogehoge"
        self.auth0User.set_password(self.password)
        self.auth0User.save()
    
    def test_userreceipes_list(self):
        response = self.client.get('/inventory/recipes/')
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/inventory/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
    
    def test_userreceipes_get(self):
        response = self.client.get('/inventory/recipes/{}'.format(self.userRecipes[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.get('/inventory/recipes/{}'.format(self.userRecipes[0].id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.userRecipes[0].id)
        self.assertEqual(response.data['name'], self.userRecipes[0].name)
        self.assertEqual(response.data['disc'], self.userRecipes[0].disc)

        response = self.client.get('/inventory/recipes/{}'.format(self.random_userrecipe.id))
        self.assertEqual(response.status_code, 400)

    def test_userreceipes_post(self):
        userTask = UserTaskModelFactory.create(user=self.user)
        userTask2 = UserTaskModelFactory.create(user=self.user)
        response = self.client.post('/inventory/recipes/', {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id,'task1': userTask.id})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.post('/inventory/recipes/', {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task1': userTask.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UserRecipe.objects.get(name='new usertask').disc, 'this is a disc')
        self.assertEqual(UserRecipe.objects.get(name='new usertask').user, self.user)
        self.assertEqual(UserRecipe.objects.get(name='new usertask').task1, userTask)

        response = self.client.post('/inventory/recipes/', {'name':'new usertask2', 'disc': 'this is a disc2', 'user': self.user.id, 'task1': userTask.id, 'task2':userTask2.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UserRecipe.objects.get(name='new usertask2').disc, 'this is a disc2')
        self.assertEqual(UserRecipe.objects.get(name='new usertask2').user, self.user)
        self.assertEqual(UserRecipe.objects.get(name='new usertask2').task1, userTask)
        self.assertEqual(UserRecipe.objects.get(name='new usertask2').task2, userTask2)

        response = self.client.post('/inventory/recipes/', {'name':'new usertask', 'disc': 'this is a disc', 'user': 99999, 'task1': userTask.id})
        self.assertEqual(response.status_code, 400)

    def test_userreceipes_put(self):
        userTask = UserTaskModelFactory.create(user=self.user)
        userTask2 = UserTaskModelFactory.create(user=self.user)
        userRecipe = UserRecipeModelFactory.create(user=self.user, task1=userTask)
        response = self.client.put('/inventory/recipes/{}'.format(userRecipe.id), {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id,'task1': userTask2.id})
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.put('/inventory/recipes/{}'.format(userRecipe.id), {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id,'task1': userTask2.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserRecipe.objects.get(id=userRecipe.id).name, 'new usertask')
        self.assertEqual(UserRecipe.objects.get(id=userRecipe.id).disc, 'this is a disc')
        self.assertEqual(UserRecipe.objects.get(id=userRecipe.id).user, self.user)
        self.assertEqual(UserRecipe.objects.get(id=userRecipe.id).task1, userTask2)

        response = self.client.put('/inventory/recipes/{}'.format(self.userRecipes[0].id), {'name':'new usertask', 'disc': 'this is a disc', 'user': 999999, 'task': userTask2.id})
        self.assertEqual(response.status_code, 400)

        response = self.client.put('/inventory/recipes/99999', {'name':'new usertask', 'disc': 'this is a disc', 'user': self.user.id, 'task': userTask2.id})
        self.assertEqual(response.status_code, 400)
    
    def test_userrecipes_delete(self):
        response = self.client.delete('/inventory/recipes/{}'.format(self.userRecipes[0].id))
        self.assertEqual(response.status_code, 403)

        self.client.login(username= self.auth0User.username, password = self.password)
        
        response = self.client.delete('/inventory/recipes/{}'.format(self.userRecipes[0].id))
        self.assertEqual(response.status_code, 204)
        self.assertRaises(UserRecipe.DoesNotExist, UserRecipe.objects.get, id=self.userRecipes[0].id)

        response = self.client.delete('/inventory/recipes/99999')
        self.assertEqual(response.status_code, 400)

        response = self.client.delete('/inventory/recipes/{}'.format(self.random_userrecipe.id))
        self.assertEqual(response.status_code, 400)
