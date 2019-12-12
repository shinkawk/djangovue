from django.urls import path
from tasks import views

app_name = 'tasks'
urlpatterns = [
    path('tasks/', views.TaskAPIListView.as_view()),
    path('tasks/<int:pk>/', views.TaskAPIDetailView.as_view())
]