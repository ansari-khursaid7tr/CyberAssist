"""
URL configuration for cyberToolBox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('password-strength/', include('password_strength.urls')),
    path('keylogger/', include('keylogger.urls')),
    path('cryptography/', include('cryptography.urls')),
    path('password-cracker/', include('password_cracker.urls')),
    path('phishing-detector/', include('phishing_detector.urls')),
    path('geolocation-finder/', include('geolocation_finder.urls')),
    path('dns-lookup/', include('dns_lookup.urls')),
    path('ssl-checker/', include('ssl_checker.urls')),
    path('osint-aggregator/', include('osint_aggregator.urls')),
]