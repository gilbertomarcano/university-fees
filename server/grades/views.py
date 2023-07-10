# from http.client import HTTPResponse
import html
from multiprocessing import context
from os import name
from unittest import result
from django.shortcuts import render
# import hhtpresponse from django.http
from django.http import HttpResponse
from django.core import serializers
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from students.models import Student

from .models import Grade

# Create your views here.
def index(request):
    return HttpResponse("index view")

# this view returns all grades for a student
def student_grades(request, student_id):
    student = Student.objects.get(user=student_id)
    grades = Grade.objects.filter(student_id=student.id)
    # we return grades as a json object
    grades_list = serializers.serialize('json', grades)
    return HttpResponse(grades_list, content_type="text/json-comment-filtered")


def student_term_grades(request, student_id, term):
    grades = Grade.objects.filter(student_id=student_id, term=term)
    # we return grades as a json object 
    grades_list = serializers.serialize('json', grades)
    return HttpResponse(grades_list, content_type="text/json-comment-filtered")

def student_general_report(request, student_id):
    terms = {}

    grades = Grade.objects.filter(student_id=student_id)

    for course in grades:
        if course.term not in terms:
            terms[course.term] = [course]
        else:
            terms[course.term].append(course)

    context = {
        "terms": terms, 
        "student": {
            "name": "Simón Díaz", #temporal name, we need a student model
            "id": student_id
        },
    }
    
    pdf = render_to_pdf("grades_template.html", context)
    res = HttpResponse(pdf.getvalue(), content_type="application/pdf")
    res["Content-Disposition"] = \
        f"attachment; filename=grades-report-{student_id}.pdf"
    return res

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

