from django.db import models
from rest_framework import serializers

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created_at',)
        db_table = "users"
