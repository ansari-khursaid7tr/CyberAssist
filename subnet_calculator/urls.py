from django.urls import path
from . import views

app_name = 'subnet_calculator'

urlpatterns = [
    path('', views.subnet_calculator, name='subnet_calculator'),
]