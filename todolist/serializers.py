from rest_framework.serializers import ModelSerializer
from account.models import CustomeUser
from .models import ToDo


class ToDoSerializer(ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = '__all__'

class CustomeUserSerializer(ModelSerializer):

    class Meta:
        model = CustomeUser
        fields = ('id','username','email')



        