from django.http import QueryDict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
import numpy as np
from grades.models import Grade
from students.models import Student, CareerChoices

class GradePerformanceView(APIView):
    """
    View to analyze performance per term
    """

    def get(self, request, *args, **kwargs):
        term = int(request.query_params.get('term', 1)) 

        term_grades = Grade.objects.filter(term=term)
        
        # calculate average grade per term
        average_grade = term_grades.aggregate(Avg('grade'))
        
        # calculate grade distribution per term
        grades = [grade.grade for grade in term_grades]
        bins = np.arange(0, 10.1, 1)
        histogram, bins = np.histogram(grades, bins=bins)
        grade_distribution = [{'range': f"{int(bins[i])}-{int(bins[i+1])}", 'count': histogram[i]} for i in range(len(histogram))]
        
        # calculate median grade per term
        sorted_grades = sorted([grade.grade for grade in term_grades])
        median_grade = sorted_grades[len(sorted_grades) // 2] if sorted_grades else None
        
        performance_data = {
            'term': term,
            'average_grade': round(average_grade['grade__avg'], 2),
            'median_grade': median_grade,
            'grade_distribution': grade_distribution,
        }
    
        return Response(performance_data)



class CareerPerformanceView(APIView):
    """
    View to analyze average grades per career
    """

    def get(self, request, *args, **kwargs):
        career_performance_data = []

        for career in CareerChoices.choices:
            # Get students of this career
            students_of_career = Student.objects.filter(career=career[0])
            print(career)

            # Get grades of these students
            grades_of_career_students = Grade.objects.filter(student__in=students_of_career)

            # calculate average grade
            average_grade = grades_of_career_students.aggregate(Avg('grade'))

            career_performance_data.append({
                'career': career[1],  # Getting the human-readable version of career
                'average_grade': round(average_grade['grade__avg'], 2),
            })
        
        return Response(career_performance_data)
