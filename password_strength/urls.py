from django.urls import path
from . import views

app_name = 'password_strength'

urlpatterns = [
    path('', views.checker, name='checker'),
]