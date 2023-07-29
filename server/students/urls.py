from django.urls import path
from .views import StudentCareers, StudentCreate, StudentGenders, StudentRegions, StudentRetrieve

urlpatterns = [
    path('', StudentCreate.as_view(), name='student_create'),
    path('<int:student_id>', StudentRetrieve.as_view(), name='student_create'),
    path('careers', StudentCareers.as_view(), name='student_careers_list'),
    path('regions', StudentRegions.as_view(), name='student_regions_list'),
    path('genders', StudentGenders.as_view(), name='student_genders_list'),

]
