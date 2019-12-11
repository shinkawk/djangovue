from django.db import models
from rest_framework import serializers

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=100, editable=False)
    email = models.CharField(max_length=100)
    pic = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created_at',)
        db_table = "users"
