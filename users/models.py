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
        ordering = ('id',)
        db_table = "users"

class UserResource(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=100)
    format = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resources")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        db_table = "user_resources"

    def __str__(self):
        return '%s:%s' % (self.path, self.format)


class UserSerializer(serializers.ModelSerializer):
    resources = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'uid', 'email', 'pic', 'resources' ,'created_at')

class UserResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResource
        fields = ('path', 'format', 'created_at')