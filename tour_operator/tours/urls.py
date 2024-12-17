from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.tour_list, name='list'),
    path('create/', views.tour_create, name='create'),
    path('update/<int:pk>/', views.tour_update, name='update'),
    path('delete/<int:pk>/', views.tour_delete, name='delete'),
]