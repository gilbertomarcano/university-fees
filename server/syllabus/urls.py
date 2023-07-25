from django.urls import path

from . import views
from .views import CareerListCreateView, CareerRetrieveUpdateDestroyView, SubjectListCreateView, SubjectRetrieveUpdateDeleteView, SubjectUpload

urlpatterns = [
    path('careers/', CareerListCreateView.as_view(), name='career-list-create'),
    path('careers/<int:pk>/', CareerRetrieveUpdateDestroyView.as_view(), name='career-retrieve-update-destroy'),  
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectRetrieveUpdateDeleteView.as_view(), name='subject-retrieve-update-delete'),
    path('subjects/upload', SubjectUpload.as_view(), name='subject-upload'),  
]