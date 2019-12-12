from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('profile/', views.UserAPIView.as_view()),
    path('inventory/files/', views.UserResourceAPIView.as_view())
]