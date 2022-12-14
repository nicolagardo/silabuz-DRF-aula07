from django.urls import path, include, re_path

from rest_framework import routers

from .api import AllTodo, OneTodo, TodoViewSetCustom, TodoViewSet
from versionedTodo.v2.router import api_urlpatterns as api_v2
from versionedTodo.v3.router import api_urlpatterns as api_v3

router = routers.DefaultRouter()

router.register('/v1/todos', TodoViewSet)

urlpatterns = [
    re_path('/v2/', include(api_v2)),
    re_path('/v3/', include(api_v3)),
    # path('/todos/all', AllTodo.as_view()),
    # path('/todos/create', AllTodo.as_view()),
    # path('/todos/delete', AllTodo.as_view()),
    # path('/todos/<int:pk>', OneTodo.as_view()),
    # path('/todos/getOne/<int:pk>', TodoViewSetCustom.as_view({'get':'retrieve'})),
    # path('/todosss/create', TodoViewSetCustom.as_view({'post':'create'})),
    
]

urlpatterns += router.urls