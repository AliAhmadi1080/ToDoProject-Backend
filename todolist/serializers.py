from rest_framework.serializers import ModelSerializer
from .models import ToDo, ToDoList


class ToDoSerializer(ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoListSerializer(ModelSerializer):
    todo_list = ToDoSerializer(many=True,read_only=True)
    class Meta:
        model = ToDoList
        fields = ['id', 'user', 'name','todo_list']




        