from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import ToDoSerializer,ToDoListSerializer,\
                            TagSerializer, StatusSerializer
from .models import ToDo, ToDoList, Tag, Status
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
        request.data['user'] = request.user.id
        instance = ToDoSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data,HTTP_201_CREATED)
        return Response(None,HTTP_406_NOT_ACCEPTABLE)

class ToDoListCreate(APIView):
    def post(self,request:Request):
        request.data['user'] = request.user.id
        instance = ToDoListSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data, HTTP_201_CREATED)
        return Response(None, HTTP_400_BAD_REQUEST)

class ToDoGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def update(self, request:Request, *args, **kwargs):
        try:
            request.data._mutable = True
        except:
            pass
        request.data['user'] = request.user.id
        
        return super().update(request, *args, **kwargs)

class UserToDoList(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self,request:Request):
        these_todos = ToDoList.objects.filter(user=request.user)
        serialized_data = ToDoListSerializer(these_todos,many=True)
        return Response(serialized_data.data,HTTP_200_OK)
    
class UserTag(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request:Request):
        tags = Tag.objects.filter(user=request.user)
        serialized_data = TagSerializer(tags, many=True)
        return Response(serialized_data.data,HTTP_200_OK)
    
    def post(self, request:Request):
        request.data['user'] = request.user.id
        instance = TagSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data,HTTP_201_CREATED)
        return Response(None,HTTP_406_NOT_ACCEPTABLE)

class UserStatus(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request:Request):
        tags = Status.objects.filter(user=request.user)
        serialized_data = StatusSerializer(tags, many=True)
        return Response(serialized_data.data,HTTP_200_OK)
    
    def post(self, request:Request):
        request.data['user'] = request.user.id
        instance = StatusSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data,HTTP_201_CREATED)
        return Response(None,HTTP_406_NOT_ACCEPTABLE)