from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la gestión de horarios y disponibilidad de profesores (administrador y personal autorizado)
    path('admin/', views.admin_schedule_list, name='admin_schedule_list'),
    path('admin/<int:professor_id>/', views.admin_manage_schedule, name='admin_manage_schedule'),

    # Ruta para la generación de horarios de clases personalizados (estudiante)
    path('student/', views.student_generate_schedule, name='student_generate_schedule'),
]
