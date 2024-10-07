from rest_framework import serializers
from .models import CustomeUser


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomeUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomeUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
