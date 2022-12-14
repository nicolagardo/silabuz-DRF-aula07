from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .serializers import UserSerializer
from .models import Users

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()

class UserViewSet(
    ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserViewSetOne(
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    lookup_field = 'realname'

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)