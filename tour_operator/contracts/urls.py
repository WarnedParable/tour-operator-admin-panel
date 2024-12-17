from django.urls import path
from . import views

app_name = 'contracts'

urlpatterns = [
    path('', views.contract_list, name='list'),
    path('create/', views.contract_create, name='create'),
    path('delete/<int:pk>/', views.contract_delete, name='delete'),
]