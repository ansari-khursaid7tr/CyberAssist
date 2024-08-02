from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

@csrf_exempt
def phishing_detector(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        result = check_phishing(url)
        return JsonResponse(result)
    elif request.method == 'GET':
        return render(request, 'phishing_detector/templates/phishing_detector.html')
    return JsonResponse({'error': 'Invalid request method'})

def check_phishing(url):
    score = 0
    reasons = []

    # Check if URL uses HTTPS
    if not url.startswith('https://'):
        score += 1
        reasons.append('URL does not use HTTPS')

    # Check for IP address in URL
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', urlparse(url).netloc):
        score += 1
        reasons.append('URL contains IP address instead of domain name')

    # Check for long URL
    if len(url) > 75:
        score += 1
        reasons.append('URL is unusually long')

    # Check for URL shortening services
    shortening_services = ['bit.ly', 'goo.gl', 't.co', 'tinyurl.com']
    if any(service in url for service in shortening_services):
        score += 1
        reasons.append('URL uses a shortening service')

    # Check for excessive subdomains
    if len(urlparse(url).netloc.split('.')) > 3:
        score += 1
        reasons.append('URL has an excessive number of subdomains')

    # Attempt to fetch and analyze page content
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for forms
        if soup.find('form'):
            score += 1
            reasons.append('Page contains a form, which is common in phishing')

        # Check for password input
        if soup.find('input', {'type': 'password'}):
            score += 1
            reasons.append('Page asks for password input')

    except requests.RequestException:
        score += 1
        reasons.append('Unable to fetch page content')

    # Determine result based on score
    if score >= 3:
        result = 'Potential phishing URL'
        alert_class = 'alert-danger'
    elif score >= 1:
        result = 'Suspicious URL'
        alert_class = 'alert-warning'
    else:
        result = 'Likely safe URL'
        alert_class = 'alert-success'

    return {
        'result': result,
        'score': score,
        'reasons': reasons,
        'alert_class': alert_class
    }
