from django.shortcuts import render

def home(request):
    return render(request, 'main/templates/home.html')