from rest_framework.serializers import ModelSerializer
from .models import ToDo, ToDoList, Tag, Status

class TagSerializer(ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'

class StatusSerializer(ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

class ToDoSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    # status = StatusSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self.tags = dict(self.initial_data).get('tags',[])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        title = validated_data['title']
        subtitle = validated_data['subtitle']
        des = validated_data['description']
        user = validated_data['user']
        status = validated_data['status']
        todo_list = validated_data['todo_list']
        tags = self.tags
        todo = ToDo(title=title,subtitle=subtitle,description=des,user=user,status=status,todo_list=todo_list)
        todo.save()
        for i in tags:
            tag = Tag.objects.get(id=i)
            todo.tags.add(tag)
        todo.save()
        return todo
        

class ToDoListSerializer(ModelSerializer):
    todo_list = ToDoSerializer(many=True,read_only=True)
    class Meta:
        model = ToDoList
        fields = ['id', 'user', 'name','todo_list']





        