from django.urls import path
from . import views

app_name = 'password_cracker'

urlpatterns = [
    path('', views.cracker, name='cracker'),
]