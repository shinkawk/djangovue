from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import authentication, permissions


from .models import *

class UserListApiView(ListAPIView):
    model = User
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser)
    renderer_classes = (JSONRenderer, )
    serializer_class = UserListSerializer


class UserRetrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = UserSerializer

    def retrieve(self, request, user_id, *args, **kwargs):
        user = User.objects.get(id=user_id)
        serializer = self.serializer_class(user)

        return Response(serializer.data, status=status.HTTP_200_OK)