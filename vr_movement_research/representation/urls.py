from django.urls import path
from . import views

urlpatterns = [
    path('locomotion/', views.locomotion_charts, name='locomotion_charts'),
    path('teleportation/', views.teleportation_charts,
         name='teleportation_charts'),
    path('rotation/', views.rotation_charts, name='rotation_charts')
]