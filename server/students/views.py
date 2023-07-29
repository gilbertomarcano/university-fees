from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound

from .models import CareerChoices, GenderChoices, Student, VenezuelanRegionChoices
from .serializers import StudentSerializer

# Create your views here.
class StudentCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = Student.objects.create(**serializer.validated_data)
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentRetrieve(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(instance=student)
        data = serializer.data
        return Response(data=data)


class StudentCareers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data=CareerChoices.choices)


class StudentRegions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data=VenezuelanRegionChoices.choices)


class StudentGenders(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data=GenderChoices.choices)