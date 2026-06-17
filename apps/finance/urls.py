from django.urls import path
from .views import create_payment, payment_list, resident_payment_status, dashboard

app_name = 'finance'
urlpatterns = [
    path('payments/', payment_list, name='payment_list'),
    path('payments/create/', create_payment, name='create_payment'),
    path('payments/status/', resident_payment_status, name='payment_status'),
    path('dashboard/', dashboard, name='dashboard'),
]