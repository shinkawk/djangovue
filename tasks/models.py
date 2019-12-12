from django.db import models
from rest_framework import serializers
from users.models import User

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    disc = models.TextField(max_length=100)
    arn = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('id',)
        db_table = "tasks"

class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.OneToOneField('Task', on_delete=models.CASCADE)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ('id', )
            db_table = "settings"

class UserTask(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    disc = models.TextField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ('id', )
            db_table = "user_tasks"