from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
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
