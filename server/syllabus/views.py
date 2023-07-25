from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

import pandas as pd
from rest_framework import generics

from .models import Career, Subject
from .serializers import CareerSerializer, SubjectSerializer

# Create your views here.

class CareerListCreateView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

from django.http import HttpResponseRedirect
from syllabus.forms import SubjectForm

class SubjectUpload(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES['file']
        
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Leer el archivo Excel usando pandas
            df = pd.read_excel(file)
            required_columns = ['Career', 'Semester', 'Name', 'Code', 'Prerequisites']

            # Iterar sobre las filas del DataFrame
            data = []
            for _, row in df[required_columns].iterrows():
                code = str(row['Code'])
                prerequisites = str(row['Prerequisites'])

                # Verificar si el código ya existe en la base de datos
                if Subject.objects.filter(code=code).exists():
                    # Si el código ya existe, levanta una excepción de validación
                    raise ValidationError(f"The code '{code}' already exists in the database.")

                subject_data = {
                    'career': row['Career'],
                    'semester': row['Semester'],
                    'name': row['Name'],
                    'code': code,
                    'prerequisites': prerequisites
                }
                # Agregar el diccionario a la lista de datos
                data.append(subject_data)

            # Validar y guardar los datos en la tabla de pagos
            serializer = SubjectSerializer(data=data, many=True)
            
            print(serializer)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)