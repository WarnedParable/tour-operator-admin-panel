from django.urls import path
from . import views

app_name = 'countries'

urlpatterns = [
    path('', views.country_list, name='list'),
    path('create/', views.country_create, name='create'),
    path('update/<int:pk>/', views.country_update, name='update'),
    path('delete/<int:pk>/', views.country_delete, name='delete'),
]