from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from tasks.models import Task, TaskSerializer, UserTaskSerializer
from users.models import UserSerializer, User
from rest_framework.response import Response


class TaskAPIListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserTaskListAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        current_user = request.current_user
        serializer = UserTaskSerializer(current_user.tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        current_user = request.current_user
        request.data['user'] = current_user.id
        serializer = UserTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTaskAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, pk, format=None):
        current_user = request.current_user
        task = current_user.tasks.filter(id=pk).first()
        if task:
            serializer = UserTaskSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        current_user = request.current_user
        request.data['user'] = current_user.id
        serializer = UserTaskSerializer(data=request.data)
        if serializer.is_valid() and current_user.tasks.filter(id=pk).first():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        current_user = request.current_user
        task = current_user.tasks.filter(id=pk).first()
        if task:
            task.delete()    
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
