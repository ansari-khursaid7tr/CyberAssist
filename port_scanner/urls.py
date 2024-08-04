from django.urls import path
from . import views

app_name = 'port_scanner'

urlpatterns = [
    path('', views.port_scanner, name='port_scanner'),
]