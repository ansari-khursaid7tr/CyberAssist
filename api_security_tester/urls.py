from django.urls import path
from . import views

app_name = 'api_security_tester'

urlpatterns = [
    path('', views.api_security_tester, name='api_security_tester'),
]