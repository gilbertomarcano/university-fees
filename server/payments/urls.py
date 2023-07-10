from django.urls import path
from .views import ViewPayment, PaymentVerifyReference, PaymentList, PaymentCreate, PaymentVerify

urlpatterns = [
    path('', PaymentList.as_view(), name='payment_list'),
    path('create', PaymentCreate.as_view(), name='create_payment'),
    path('verify/<int:payment_id>', PaymentVerify.as_view(), name='verify_payment'),
    path('verify', PaymentVerifyReference.as_view(), name='verify_payment_reference'),
    path('<int:payment_id>', ViewPayment.as_view(), name='view_payment'),
]
