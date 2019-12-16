from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
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

class UserRecipeListAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        current_user = request.current_user
        serializer = UserRecipeSerializer(current_user.recipes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        current_user = request.current_user
        if request.data['user'] != str(current_user.id):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRecipeAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, pk, format=None):
        current_user = request.current_user
        recipe = current_user.recipes.filter(id=pk).first()
        if recipe:
            serializer = UserRecipeSerializer(recipe)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        current_user = request.current_user
        user_recipe = current_user.recipes.filter(id=pk).first()
        if request.data['user'] != str(current_user.id) or user_recipe==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRecipeSerializer(user_recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        current_user = request.current_user
        recipe = current_user.recipes.filter(id=pk).first()
        if recipe:
            recipe.delete()    
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)