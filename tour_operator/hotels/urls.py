from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.hotel_list, name='list'),
    path('create/', views.hotel_create, name='create'),
    path('update/<int:pk>/', views.hotel_update, name='update'),
    path('delete/<int:pk>/', views.hotel_delete, name='delete'),
]