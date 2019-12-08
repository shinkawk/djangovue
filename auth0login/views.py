# auth0login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
import json
from rest_framework.response import Response
from django.http import JsonResponse
from users.models import User

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)

@login_required
def authorize(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    user_obj, created = User.objects.get_or_create(uid=auth0user.uid)
    if created:
        user_obj.name = auth0user.user.username
        user_obj.email = auth0user.user.email
        user_obj.save()
    userdata = {
        'user' : auth0user.user.username,
    }
    return JsonResponse(userdata)