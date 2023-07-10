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

from .models import Grade
from students.models import Student, CareerChoices, VenezuelanRegionChoices
from users.models import User

# Create your views here.
def index(request):
    return HttpResponse("index view")

# this view returns all grades for a student
def student_grades(request, student_id):
    grades = Grade.objects.filter(student_id=student_id)
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
    # we get national id prefix and number from student_id
    student_id_str = str(student_id)
    id_prefix = student_id_str[0]
    id_number = student_id_str[1:]
    print(id_prefix, id_number)

    student = Student.objects.get(national_id_prefix=id_prefix,national_id_number=int(id_number))
    print(student)
    grades = Grade.objects.filter(student_id=id_number)
    user = User.objects.get(id=student.user_id)
    print(user)

    for course in grades:
        if course.term not in terms:
            terms[course.term] = [course]
        else:
            terms[course.term].append(course)

    # we convert student career to their name on CareerChoices, using integers as keys
    # we find the dict that contains student.career
    student_career = ""
    for career in CareerChoices.choices:
        if career[0] == student.career:
            student.career = career[1]
            break

    region = ""
    # we do the same with student.region
    for region in VenezuelanRegionChoices.choices:
        if region[0] == student.region:
            student.region = region[1]
            break


    print(student_career)


    context = {
        "terms": terms, 
        "student": student,
        "user": user,
    }

    # return render(request, "grades_template.html", context)
    
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

