from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_student = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_student'  # replaced 'student' with 'is_student'
        ) 
        extra_kwargs = {'password': {'write_only': True}}

    def get_is_student(self, obj):
        return hasattr(obj, 'student')
