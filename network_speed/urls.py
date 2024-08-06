from django.urls import path
from . import views

app_name = 'network_speed'

urlpatterns = [
    path('', views.network_speed, name='network_speed'),
]