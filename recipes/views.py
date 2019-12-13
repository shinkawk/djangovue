from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from recipes.models import Recipe, RecipeSerializer, UserRecipeSerializer
from users.models import User
from rest_framework.response import Response

class RecipeAPIListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeAPIDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class UserRecipeListAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        serializer = UserRecipeSerializer(current_user.recipes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        request.data['user'] = current_user.id
        serializer = UserRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRecipeAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, pk, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        task = current_user.recipes.filter(id=pk).first()
        if task:
            serializer = UserRecipeSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        request.data['user'] = current_user.id
        serializer = UserRecipeSerializer(data=request.data)
        if serializer.is_valid() and current_user.recipes.filter(id=pk).first():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        current_user = User.objects.get(uid=auth0user.uid)
        recipe = current_user.recipes.filter(id=pk).first()
        if recipe:
            recipe.delete()    
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)