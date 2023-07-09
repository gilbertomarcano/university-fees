# from http.client import HTTPResponse
from django.shortcuts import render
# import hhtpresponse from django.http
from django.http import HttpResponse
from django.core import serializers

from .models import Grade

# Create your views here.
def index(request):
    return HttpResponse("index view")

# this view returns all grades for a student
def studentGrades(request, studentId):
    grades = Grade.objects.filter(studentId=studentId)
    # we return grades as a json object
    grades_list = serializers.serialize('json', grades)
    return HttpResponse(grades_list, content_type="text/json-comment-filtered")


def studentTermGrades(request, studentId, term):
    grades = Grade.objects.filter(studentId=studentId, term=term)
    # we return grades as a json object 
    grades_list = serializers.serialize('json', grades)
    return HttpResponse(grades_list, content_type="text/json-comment-filtered")