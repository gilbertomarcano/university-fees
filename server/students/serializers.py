from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, student):
        return UserSerializer(instance=student.user).data

    class Meta:
        model = Student
        fields = (
            'id',
            'user',
            'career',
            'region',
            'national_id_prefix',
            'national_id_number',
            'gender',
        ) 
