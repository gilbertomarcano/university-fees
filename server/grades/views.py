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
from students.models import Student, CareerChoices, VenezuelanRegionChoices
from course.models import Course, get_course_name_by_enum
from users.models import User

# Create your views here.
def index(request):
    return HttpResponse("index view")

# this view returns all grades for a student
def student_grades(request, student_id):
    student = Student.objects.get(id=student_id)
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
        course_enum = Course.objects.get(course_id=course.course_id).course_name
        course.name = get_course_name_by_enum(course_enum)
        if course.term not in terms:
            # course.name = 
            terms[course.term] = [course]
            print(course_enum, course.name)
            print(course.name)
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


from faker import Faker
from students.models import Student, CareerChoices, VenezuelanRegionChoices, NationalIdPrefixChoices, GenderChoices
from grades.models import Grade
from users.models import User
import random
import numpy as np

fake = Faker()

# print(User.objects.filter(student__isnull=False).delete())
# # Create 100 users
# for i in range(100):
#     # Create User
#     email = fake.email()
#     password = "test"
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)

#     # Create Student
#     career = random.choice(list(CareerChoices))
#     region = random.choice(list(VenezuelanRegionChoices))
#     national_id_prefix = random.choices(list(NationalIdPrefixChoices), weights=[70, 30], k=1)[0]  # Adjusting the distribution of V and E students
#     national_id_number = str(random.randint(1000000, 9999999))
#     gender = random.choice(list(GenderChoices))
#     student = Student.objects.create(user=user, career=career, region=region, national_id_prefix=national_id_prefix, national_id_number=national_id_number, gender=gender)

#     # Create Grades for the Student
#     for term in range(1, 4):  # Assuming 3 terms
#         course_ids = random.sample(range(100, 200), 4)  # Select 4 unique course_ids
#         for course_id in course_ids:
#             # Use a beta distribution to make grades cluster around 7 or 8
#             grade_value = round(min(np.random.beta(2, 1.5) * 10, 10), 2)
#             Grade.objects.create(student=student, term=term, course_id=course_id, grade=grade_value)
