from django.urls import path
from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('recipes/', views.RecipeAPIListView.as_view()),
    path('recipes/<int:pk>/', views.RecipeAPIDetailView.as_view()),
    path('inventory/recipes/', views.UserRecipeListAPIView.as_view()),
    path('inventory/recipes/<int:pk>', views.UserRecipeAPIView.as_view())
]