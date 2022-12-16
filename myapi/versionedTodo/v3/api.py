from todos.models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

from rest_framework.throttling import UserRateThrottle
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'body']
    ordering = ('-id')

    throttle_classes = [UserRateThrottle]
    # throttle_scope = 'get'



    tarea = """
    
  
Posterior a la implementación y prueba del ScopedRateThrottle, 
nuestra última tarea de la unidad será la siguiente.

API de pagos
Esta api funcionará como un pequeño proyecto, en la cual deben 
hacer uso de las siguientes tecnologías.

simpleJWT

Throttling

Para esta API de pagos el enunciado es el siguiente.

Se necesitará crear una aplicación de usuarios que permita el
login como lo vimos anteriormente. Luego de esto, crear una aplicación pagos
 la cual debe registrar el usuario, el servicio, el monto, y la fecha de pago.

La aplicación de pagos solo debe admitir las siguiente operaciones:

GET (list y retrieve)

POST

Debe contener paginación y filtros de búsqueda para los campos de user__id, 
fecha_pago y servicio.

Los servicios a usar dentro de la APP para registrar los pagos son lo siguientes:

Netflix

Amazon Video

Star +

Paramount +

Recordar que esta aplicación y las vistas creadas, deben hacer uso de simpleJWT 
para que se haga uso del login de los usuarios.

Por último, la creación de pagos debe estar limitada a 1000 request por día.
    
    """