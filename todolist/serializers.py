from rest_framework.serializers import ModelSerializer
from .models import ToDo
class ToDoSirializer(ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = '__all__'



        