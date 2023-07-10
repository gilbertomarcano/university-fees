from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.
class PaymentCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            Payment = serializer.save()  # Guarda el Payment en la base de datos
            return Response(PaymentSerializer(Payment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentVerify(APIView):
    def get(self, request, payment_id):
        Payment = get_object_or_404(Payment, id=payment_id)
        serializer = PaymentSerializer(Payment)
        return Response(serializer.data)
