from django.urls import path
from .views import GradePerformanceView, CareerPerformanceView

urlpatterns = [
    path('performance', GradePerformanceView.as_view(), name='performance_analysis'),
    path('career', CareerPerformanceView.as_view(), name='career_analysis'),
]
