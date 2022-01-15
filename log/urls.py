from django.urls import path
from .views import *

urlpatterns = [
    path('', LogList.as_view(), name='log_list'),
    path('checkout/', CheckoutBorrower.as_view(), name='checkout_reader'), 
    path('checkout/<int:rid>/', CheckoutEquipment.as_view(), name='checkout_book'), 
    path('checkout/<int:rid>/<int:bid>/', CheckoutLog.as_view(), name='checkout_log'),
    path('return/', ReturnEquipment.as_view(), name='return_book'), 
    path('return/<int:lid>/', ReturnLog.as_view(), name='return_log'),
]