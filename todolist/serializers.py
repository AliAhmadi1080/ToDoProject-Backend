from rest_framework.serializers import ModelSerializer
from account.models import CustomeUser
from .models import ToDo, ToDoList


class ToDoSerializer(ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoListSerializer(ModelSerializer):
    
    class Meta:
        model = ToDoList
        fields = '__all__'




        