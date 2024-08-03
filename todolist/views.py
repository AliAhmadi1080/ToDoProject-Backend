from rest_framework.views import APIView
from .serializers import ToDoSerializer, CustomeUserSerializer
from .models import ToDo
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import\
                                     JWTAuthentication
User = get_user_model()

class ToDoList(APIView):
    def get(self,request:Request):
        all_todos = ToDo.objects.all()
        serialized_data = ToDoSerializer(all_todos,many=True)
        return Response(serialized_data.data,HTTP_200_OK)
    
    def post(self,request:Request):
        instance = ToDoSerializer(data=request.data,many=False)
        if instance.is_valid():
            instance.save()
            return Response(instance.data,HTTP_201_CREATED)
            
        return Response(None,HTTP_400_BAD_REQUEST)

    
class ToDoGenericsDetail(generics.DestroyAPIView,generics.UpdateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UserToDo(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self,request:Request):
        try:
            this_user = request.user
            these_todos = ToDo.objects.filter(user=this_user)
            serialized_data = ToDoSerializer(these_todos,many=True)
            user = CustomeUserSerializer(this_user)
        except:
            return Response({},HTTP_400_BAD_REQUEST)
        return Response({'todo':serialized_data.data,'user':user.data},HTTP_200_OK)
    

    
    

    
