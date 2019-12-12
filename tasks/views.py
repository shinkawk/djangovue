from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, generics
from tasks.models import Task, TaskSerializer


class TaskAPIListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

