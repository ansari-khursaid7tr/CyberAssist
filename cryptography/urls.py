from django.urls import path
from . import views

app_name= 'cryptography'

urlpatterns = [
    path('', views.encrypt_decrypt, name='encrypt_decrypt'),
]
