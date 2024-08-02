from django.urls import path
from . import views

app_name = 'dns_lookup'

urlpatterns = [
    path('', views.dns_lookup, name='dns_lookup'),
]