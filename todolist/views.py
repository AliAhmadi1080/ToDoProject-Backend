from rest_framework.views import APIView
from .serializers import ToDoSirializer
from .models import ToDo
from django.contrib.auth import get_user_model
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *

User = get_user_model()
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
    
class ToDoList(APIView):
    def get(self,request:Request):
        all_todos = ToDo.objects.all()
        serialized_data = ToDoSirializer(all_todos,many=True)
        return Response(serialized_data.data,HTTP_200_OK)
    
    def post(self,request:Request):
        instance = ToDoSirializer(data=request.data,many=False)
        if instance.is_valid():
            instance.save()
            return Response(instance.data,HTTP_201_CREATED)
            
        return Response(None,HTTP_400_BAD_REQUEST)

    
class ToDoGenericsDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ToDo.objects.all()
    serializer_class = ToDoSirializer

class UserToDo(APIView):
    def get(self,request:Request):
        return Response({},HTTP_400_BAD_REQUEST)
    def post(self,request:Request):
        try:
            email = request.data['email']
            this_user = User.objects.get(email=email)
            these_todos = ToDo.objects.filter(user=this_user)
            serialized_data = ToDoSirializer(these_todos,many=True)
            
        except:
            return Response({},HTTP_400_BAD_REQUEST)
        return Response({'user':serialized_data.data},HTTP_200_OK)

    
