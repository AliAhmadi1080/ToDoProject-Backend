from rest_framework.views import APIView
from .serializers import ToDoSerializer,ToDoListSerializer
from .models import ToDo, ToDoList
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import\
                                     JWTAuthentication
User = get_user_model()

class ToDoCreate(APIView):
    def post(self,request:Request):
        instance = ToDoSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data,HTTP_201_CREATED)
        return Response(None,HTTP_406_NOT_ACCEPTABLE)

class ToDoListCreate(APIView):
    def post(self,request:Request):
        instance = ToDoListSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data, HTTP_201_CREATED)
        return Response(None, HTTP_400_BAD_REQUEST)

class ToDoGenericsDetail(generics.DestroyAPIView,generics.UpdateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UserToDoList(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self,request:Request):
        this_user = request.user
        these_todos = ToDoList.objects.filter(user=this_user)
        serialized_data = ToDoListSerializer(these_todos,many=True)
        return Response(serialized_data.data,HTTP_200_OK)
    