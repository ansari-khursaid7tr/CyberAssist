from django.shortcuts import render

def network_speed(request):
    return render(request, 'network_speed/templates/network_speed.html')