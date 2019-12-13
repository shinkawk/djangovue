from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib import auth
from users.models import User

def get_current_user(request):
    user = auth.get_user(request)
    auth0user = user.social_auth.get(provider='auth0')
    try:
        return User.objects.get(uid=auth0user.uid)
    except Exception:
        return None

class Auth0MiddleWare(MiddlewareMixin):
    def process_request(self, request):
        request.current_user = SimpleLazyObject(lambda: get_current_user(request))