from django.urls import path
from . import views

app_name = 'social_engineering'

urlpatterns = [
    path('', views.social_engineering_simulator, name='social_engineering_simulator'),
]