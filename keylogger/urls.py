from django.urls import path
from . import views

app_name = 'keylogger'

urlpatterns = [
    path('', views.logger, name='logger'),
    path('log/', views.log_keys, name='log_keys'),
]