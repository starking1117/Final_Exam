from django.urls import path
from .views import *

urlpatterns = [
    path('', TypeList.as_view(), name='type_list'),
    path('add/', TypeAdd.as_view(), name='type_add'), 
    path('<int:pk>/', TypeView.as_view(), name='type_view'),
    path('<int:pk>/edit/', TypeEdit.as_view(), name='type_edit'),
    path('<int:pk>/delete/', TypeDelete.as_view(), name='type_delete'),
]