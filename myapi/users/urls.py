from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .api import (
    UserViewSet,
    UserViewSetOne,
    GetUsers,
    SignUpView, 
    LoginView
)


router = routers.DefaultRouter()

router.register('/v1/users', UserViewSet, 'users')
router.register('/v1/users', UserViewSetOne, 'oneUser')
router.register("/users", GetUsers)

urlpatterns = [
    path("/users/signup/", SignUpView.as_view(), name= "signup"),
    path("/users/login/", LoginView.as_view(), name= "login"),
    path("/users/jwt/create/", TokenObtainPairView.as_view(), name= "jwt_create"),
    path("/users/jwt/refresh/", TokenRefreshView.as_view(), name= "token_refresh"),
    path("/users/jwt/verify/", TokenVerifyView.as_view(), name= "token_verify"),

]

urlpatterns += router.urls