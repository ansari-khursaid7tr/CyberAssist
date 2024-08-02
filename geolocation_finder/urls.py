from django.urls import path
from . import views

app_name = 'geolocation_finder'

urlpatterns = [
    path('', views.geolocation_finder, name='geolocation_finder'),
]