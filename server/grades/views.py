# from http.client import HTTPResponse
from django.shortcuts import render
# import hhtpresponse from django.http
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index view")

# this view returns all grades for a student
def studentGrades(request, studentId):
    return HttpResponse(f"grades for student {studentId}")

def studentTermGrades(request, studentId, term):
    return HttpResponse(f"grades for student {studentId} in term {term}")