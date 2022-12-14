from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.filters import  (
    SearchFilter,
    OrderingFilter
)

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .pagination import StandardResultSetPagination
from .serializer import TodoSerializer
from .models import Todo

class AllTodo(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        ser = TodoSerializer(todos, many= True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = TodoSerializer(data= request.data)
        print("REQUEST.DATA: ", request.data)
        print(ser)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_201_CREATED)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        Todo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OneTodo(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get_one(self, pk):
        try:
            todo = Todo.objects.get(pk= pk)
            return todo
        except Todo.DoesNotExist:
            raise Http404()

    def get(self, request, pk):
        todo = self.get_one(pk)
        s = TodoSerializer(todo)
        print("permiso: ", request.user)
        return Response(s.data)
        
    def post(self, request):
        ser = TodoSerializer(data= request.data)
    
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_201_CREATED)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        todo = self.get_one(pk)
        s = TodoSerializer(todo, data= request.data)

        if s.is_valid():
            s.save()
            return Response(s.data, status= status.HTTP_202_ACCEPTED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        todo = self.get_one(pk)
        serializador = TodoSerializer(todo, data= request.data, partial= True)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status= status.HTTP_202_ACCEPTED)
        return Response({"messege": "Algo salió mal"}, 404)

    def delete(self, request, pk):
        todo = self.get_one(pk)
        todo.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class TodoViewSetCustom(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    filter_backends =[OrderingFilter, SearchFilter]
    # filterset_fields = ['status']
    # ordering_fields = ['status']
    search_fields = ['title', 'body']
    pagination_class = StandardResultSetPagination

    def get_serializer_class(self):
        return TodoSerializer

    def list(self, request):
        queryset = Todo.objects.all()
        ser = TodoSerializer(queryset, many= True)
        return Response(ser.data, status= status.HTTP_202_ACCEPTED)


    def create(self, request):
        if isinstance(request.data, list):
            ser = TodoSerializer(data= request.data, many=True)
        else:
            ser = TodoSerializer(data= request.data)
        
        if ser.is_valid():
            ser.save()
            return Response({'message': 'TODOS creados exitosamente'}, status= status.HTTP_201_CREATED)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        querset = Todo.objects.all()
        todo = get_object_or_404(querset, pk=pk)
        todo.delete()
        return Response(status=204)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultSetPagination
        