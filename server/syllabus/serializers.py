from rest_framework import serializers
from .models import Career, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        #fields = ('career', 'semester', 'name', 'code', 'prerequisites')

class CareerSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Career
        fields = '__all__'
