from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import ToDo, Status, Tag, ToDoList




class UserSirializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username',]

class StatusSirializer(ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

class TagSirializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class ToDoSirializer(ModelSerializer):
    user = UserSirializer()
    status = StatusSirializer()
    tags = TagSirializer(many=True,read_only=True)
    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoListSirializer(ModelSerializer):
    todos = ToDoSirializer(many=True,read_only=True)
    class Meta:
        model = ToDoList
        fields = '__all__'

        