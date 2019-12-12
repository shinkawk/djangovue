from django.db import models
from tasks.models import Task, UserTask
from users.models import User

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=50)
    disc =  models.TextField(max_length=100)
    task1 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, related_name='task1')
    task2 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task2')
    task3 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task3')
    task4 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task4')
    task5 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task5')
    task6 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task6')
    task7 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task7')
    task8 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task8')
    task9 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task9')
    task10 = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=True, related_name='task10')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('id',)
        db_table = "recipes"

class UserRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    disc =  models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task1 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, related_name='task1')
    task2 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task2')
    task3 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task3')
    task4 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task4')
    task5 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task5')
    task6 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task6')
    task7 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task7')
    task8 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task8')
    task9 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task9')
    task10 = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING, null=True, related_name='task10')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('id',)
        db_table = "user_recipes"

