from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .models import User
from .serializers import PaymentSerializer

# Create your views here.
class ViewPayment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

class PaymentList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.all().order_by('-id')
        serializer = PaymentSerializer(payments, many=True)

        # Paginated data
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 5))
        count = payments.count()
        start_index = (page - 1) * page_size
        end_index = page * page_size
        payments = serializer.data[start_index:end_index]

        response_data = {
            'count': count,
            'page': page,
            'page_size': page_size,
            'data': payments
        }
        return Response(response_data)
    
    
class PaymentCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            Payment = serializer.save()  # Guarda el Payment en la base de datos
            return Response(PaymentSerializer(Payment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentVerify(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        serializer = PaymentSerializer(Payment)        
        if payment.user:
            return Response({"error": "Payment already claimed"}, status=status.HTTP_400_BAD_REQUEST)
                
        id = request.data.get("user")
        user = get_object_or_404(User, id=id)
        if user is None:
            return Response({"error": "User not exist"}, status=status.HTTP_400_BAD_REQUEST)
        payment.user = user
        payment.save()
        
        return Response({"status": "Successfully claimed"}, status=status.HTTP_201_CREATED)

class PaymentVerifyReference(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):        
        reference = request.data.get("reference")
        payment = get_object_or_404(Payment, reference=reference)
        serializer = PaymentSerializer(Payment) 
        if payment is None:
            return Response({"error": "Payment not exist"}, status=status.HTTP_400_BAD_REQUEST)       
        if payment.user:
            return Response({"error": "Payment already claimed"}, status=status.HTTP_400_BAD_REQUEST)
                
        id = request.data.get("id")
        user = get_object_or_404(User, id=id)
        if user is None:
            return Response({"error": "User not exist"}, status=status.HTTP_400_BAD_REQUEST)
        payment.user = user
        payment.save()
        
        return Response({"status": "Successfully claimed"}, status=status.HTTP_201_CREATED)
