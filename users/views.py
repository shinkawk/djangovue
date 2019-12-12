from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.decorators import login_required
from users.models import User, UserSerializer

class UserAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        serializer = UserSerializer(current_user)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        serializer = UserSerializer(current_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        current_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)