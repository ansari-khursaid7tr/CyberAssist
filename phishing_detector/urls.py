from django.urls import path
from . import views

app_name = 'phishing_detector'

urlpatterns = [
    path('', views.phishing_detector, name='phishing_detector'),
]