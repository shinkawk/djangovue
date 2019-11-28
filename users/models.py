from django.db import models
from rest_framework import serializers

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    sid = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created_at',)

class UserListSerializer(serializers.ModelSerializer):
    # 名前
    name = serializers.CharField(max_length=50)
    sid = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'sid', 'created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
    # 名前
    name = serializers.CharField(max_length=50)
    sid = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'sid', 'created_at', 'updated_at')

