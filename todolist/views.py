from django.shortcuts import render
from .serializers import ToDoSirializer
from .models import ToDo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

@api_view(['GET'])
def list_todo(request:Request):
    todos = ToDo.objects.all()
    
    serialized_todos = ToDoSirializer(todos,many=True)
    todos_data = serialized_todos.data
    return Response(todos_data,HTTP_200_OK)


@api_view(['GET'])
def detail_todo(request:Request):
    try:
        payload = int(request.query_params.get('id'))
    except:
        return Response(None,HTTP_400_BAD_REQUEST)
    print(payload)
    
    
    todos = ToDo.objects.filter(id=int(payload))
    
    serialized_todos = ToDoSirializer(todos,many=True)
    todos_data = serialized_todos.data
    return Response(todos_data,HTTP_200_OK)



