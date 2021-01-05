from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_P, name='home_P')
]
