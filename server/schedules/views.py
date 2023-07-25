from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from .models import Professor, Schedule

# Create your views here.

def admin_schedule_list(request):
    professors = Professor.objects.all()
    return render(request, 'schedules/admin/schedule_list.html', {'professors': professors})

def admin_manage_schedule(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    schedules = Schedule.objects.filter(professor=professor)
    return render(request, 'schedules/admin/manage_schedule.html', {'professor': professor, 'schedules': schedules})

def student_generate_schedule(request):
    # Lógica para generar el horario personalizado del estudiante
    # ...

    return render(request, 'schedules/student/generate_schedule.html', {'generated_schedule': generated_schedule})
