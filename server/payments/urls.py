from django.urls import path
from .views import PaymentCreate, PaymentVerify

urlpatterns = [
    path('', PaymentCreate.as_view(), name='create_payment'),
    path('<int:payment_id>/', PaymentVerify.as_view(), name='verify_payment'),
]
