from django.urls import path
from .views import *

urlpatterns = [
    path('', EquipmentList.as_view(), name='equipment_list'),
    path('add/', EquipmentAdd.as_view(), name='equipment_add'), 
    path('<int:pk>/', EquipmentView.as_view(), name='equipment_view'),
    path('<int:pk>/edit/', EquipmentEdit.as_view(), name='equipment_edit'),
    path('<int:pk>/delete/', EquipmentDelete.as_view(), name='equipment_delete'),
]