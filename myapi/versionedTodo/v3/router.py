from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', api.TodoViewSet, 'todosCustom')

api_urlpatterns = router.urls