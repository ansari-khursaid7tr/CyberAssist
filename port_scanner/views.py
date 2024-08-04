from django.shortcuts import render
from django.http import JsonResponse
from .scanner import port_scan


def port_scanner(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        start_port = int(request.POST.get('start_port', 1))
        end_port = int(request.POST.get('end_port', 1024))

        open_ports = port_scan(ip, start_port, end_port)
        return JsonResponse({'open_ports': open_ports})

    return render(request, 'port_scanner/templates/port_scanner.html')