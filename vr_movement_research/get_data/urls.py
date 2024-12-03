from django.urls import path
from . import views

urlpatterns = [
    path('', views.preset_list),
    path('<int:pk>', views.preset)
]