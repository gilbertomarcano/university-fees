# from http.client import HTTPResponse
from django.shortcuts import render
# import hhtpresponse from django.http
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index view")

def grades(request):
    return HttpResponse("grades view")