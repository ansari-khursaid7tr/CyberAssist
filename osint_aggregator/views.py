import whois
import dns.resolver
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
from datetime import datetime


@csrf_exempt
def osint_aggregator(request):
    if request.method == 'POST':
        target = request.POST.get('target', '').strip()
        result = gather_osint(target)
        return JsonResponse(result)
    elif request.method == 'GET':
        return render(request, 'osint_aggregator.html')
    return JsonResponse({'error': 'Invalid request method'})


def gather_osint(target):
    result = {}

    if re.match(r"[^@]+@[^@]+\.[^@]+", target):
        # If target is an email address
        result['email_info'] = gather_email_info(target)
    else:
        # If target is a domain
        result['whois_info'] = gather_whois_info(target)
        result['dns_info'] = gather_dns_info(target)
        result['website_info'] = gather_website_info(target)

    return result


def gather_whois_info(domain):
    def format_date(date):
        if isinstance(date, list):
            return [d.strftime('%Y-%m-%d %H:%M:%S %Z') for d in date if isinstance(d, datetime)]
        elif isinstance(date, datetime):
            return date.strftime('%Y-%m-%d %H:%M:%S %Z')
        else:
            return str(date)

    try:
        w = whois.whois(domain)
        return {
            'registrar': w.registrar,
            'creation_date': format_date(w.creation_date),
            'expiration_date': format_date(w.expiration_date),
            'name_servers': w.name_servers,
        }
    except Exception as e:
        return {'error': str(e)}


def gather_dns_info(domain):
    try:
        result = {}
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                result[record_type] = [str(rdata) for rdata in answers]
            except dns.resolver.NoAnswer:
                result[record_type] = []
        return result
    except Exception as e:
        return {'error': str(e)}


def gather_website_info(domain):
    try:
        url = f"http://{domain}"
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
            'title': soup.title.string if soup.title else 'No title found',
            'meta_description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={
                'name': 'description'}) else 'No description found',
        }
    except Exception as e:
        return {'error': str(e)}


def gather_email_info(email):
    domain = email.split('@')[1]
    return {
        'domain_info': gather_dns_info(domain),
        'mx_records': gather_dns_info(domain).get('MX', []),
    }
