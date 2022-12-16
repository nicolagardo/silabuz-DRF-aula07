from django.contrib.auth import authenticate

from rest_framework import viewsets, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import mixins
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin)

from .serializers import UserSerializer, SignUpSerializer, GetUserSerializer
from .models import Users, User
from .tokens import create_jwt_pair_for_user

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()

class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UserViewSetOne(
    UpdateModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    lookup_field = 'username'

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data
        ser = self.serializer_class(data=data)

        if ser.is_valid():
            ser.save()
            response = {"message":" El usuario se creó correctamente", "data": ser.data}
            return Response(data= response, status=201)

        return Response(ser.errors, status=400)


class LoginView(APIView):

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email= email, password= password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            resp = {
                "message": " Logeado correctamente",
                "email": email,
                "tokens": tokens
            }
            return Response(data = resp, status=200 )
        else:
            return Response({"message":"Correo inválido o contaseña incorrecta"})

    def get(self, request: Request):
        resp = {"user": f'{request.user}', "auth":str(request.auth)}
        return Response(data= resp, status=200)

class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()