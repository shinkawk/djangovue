from django.db import models

from django.db import models
from rest_framework import serializers

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    disc =  models.TextField(max_length=100)
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
