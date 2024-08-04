from django.urls import path
from . import views

app_name = 'osint_aggregator'

urlpatterns = [
    path('', views.osint_aggregator, name='osint_aggregator'),
]