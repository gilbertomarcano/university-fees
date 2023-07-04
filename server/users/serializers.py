from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name') 
        extra_kwargs = {'password': {'write_only': True}}
