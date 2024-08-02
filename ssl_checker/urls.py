from django.urls import path
from . import views

app_name = 'ssl_checker'

urlpatterns = [
    path('', views.ssl_tls_checker, name='ssl_tls_checker'),
]