from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.decorators import login_required
from users.models import User, UserResourceSerializer, UserSerializer

class UserAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        serializer = UserSerializer(request.current_user)
        return Response(serializer.data)

    def put(self, request, format=None):
        current_user = request.current_user
        serializer = UserSerializer(current_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        current_user = request.current_user
        current_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserResourceAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        current_user = request.current_user
        serializer = UserResourceSerializer(current_user.resources, many=True)
        return Response(serializer.data)



