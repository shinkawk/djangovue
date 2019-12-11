from django.db import models

from django.db import models
from rest_framework import serializers

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    disc =  models.CharField(max_length=100)
    arn = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('id',)
        db_table = "Tasks"
