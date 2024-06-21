from rest_framework.views import APIView
from .serializers import ToDoSirializer
from .models import ToDo
from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *


# class ToDoList(APIView):
#     def get(self,request:Request):
#         todos = ToDo.objects.all()
        
#         serialized_todos = ToDoSirializer(todos,many=True)
#         todos_data = serialized_todos.data
#         return Response(todos_data,HTTP_200_OK)
    
#     def post(self,request:Request):
#         instance = ToDoSirializer(data=request.data,many=False)
#         if instance.is_valid():
#             instance.save()
#             return Response(instance.data,HTTP_201_CREATED)
#         return Response(None,HTTP_400_BAD_REQUEST)

        
# class ToDoDetail(APIView):
#     def get(self,request:Request,pk:int):
#         todos = get_object_or_404(ToDo,pk=pk)
    
#         serialized_todos = ToDoSirializer(todos)
#         todos_data = serialized_todos.data
#         return Response(todos_data,HTTP_200_OK)

#     def put(self,request:Request,pk:int):
#         instance = get_object_or_404(ToDo,pk=pk)
#         instance = ToDoSirializer(instance,data=request.data,many=False)
#         if instance.is_valid():
#             instance.save()
#             return Response(instance.data,HTTP_201_CREATED)
#         return Response(None,HTTP_400_BAD_REQUEST)

#     def delete(self,request:Request,pk:int):

#         instance = get_object_or_404(ToDo,pk=pk)
#         instance.delete()
#         return Response("OK",HTTP_204_NO_CONTENT)
    
class ToDoGenericsList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSirializer

    
class ToDoGenericsDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ToDo.objects.all()
    serializer_class = ToDoSirializer
