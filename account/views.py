from django.shortcuts import render

from rest_framework import generics
from .serializers import UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
