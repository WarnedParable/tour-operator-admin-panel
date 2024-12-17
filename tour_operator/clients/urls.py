from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='list'),
    path('create/', views.client_create, name='create'),
    path('update/<int:pk>/', views.client_update, name='update'),
    path('delete/<int:pk>/', views.client_delete, name='delete'),
]