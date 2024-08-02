from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def geolocation_finder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            ip_address = data.get('ip', '')
            result = get_geolocation(ip_address)
            return JsonResponse(result)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    elif request.method == 'GET':
        return render(request, 'geolocation_finder/templates/geolocation_finder.html')
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_geolocation(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()
        if data['status'] == 'success':
            return {
                'ip': ip_address,
                'country': data['country'],
                'isp': data['isp'],
                'region': data['regionName'],
                'city': data['city'],
                'latitude': data['lat'],
                'longitude': data['lon'],
            }
        else:
            return {'error': 'Unable to find geolocation for the given IP address'}
    except requests.RequestException:
        return {'error': 'An error occurred while fetching geolocation'}
