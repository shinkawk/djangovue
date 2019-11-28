from django.conf.urls import url
from .views import UserListApiView, UserRetrieveApiView

app_name = 'users'
urlpatterns = [
    url(r'^users/$', UserListApiView.as_view()),
    url(r'^user/(?P<user_id>\w+)/?$', UserRetrieveApiView.as_view()),
]