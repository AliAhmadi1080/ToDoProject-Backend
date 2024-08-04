from rest_framework.serializers import ModelSerializer
from .models import ToDo, ToDoList, Tag, Status


class ToDoSerializer(ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoListSerializer(ModelSerializer):
    todo_list = ToDoSerializer(many=True,read_only=True)
    class Meta:
        model = ToDoList
        fields = ['id', 'user', 'name','todo_list']

class TagSerializer(ModelSerializer):
    todos = ToDoSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'

class StatusSerializer(ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'



        