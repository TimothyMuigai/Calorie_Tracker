from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cal, name='show_cal'),
    path('remove/<int:itemId>/', views.remove_cal, name='remove_cal'),
    path('add/', views.add_data, name='add_data'),
    path('reset/', views.reset_calories, name='reset_calories')
]
