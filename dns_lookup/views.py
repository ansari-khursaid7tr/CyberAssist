from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import dns.resolver

@csrf_exempt
def dns_lookup(request):
    if request.method == 'POST':
        domain = request.POST.get('domain', '').strip()
        if not domain:
            return JsonResponse({'error': 'Domain field cannot be empty'}, status=400)

        result = perform_dns_lookup(domain)
        return JsonResponse(result)
    elif request.method == 'GET':
        return render(request, 'dns_lookup/templates/dns_lookup.html')
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def perform_dns_lookup(domain):
    try:
        result = {
            'domain': domain,
            'a_records': get_dns_records(domain, 'A'),
            'mx_records': get_dns_records(domain, 'MX'),
            'ns_records': get_dns_records(domain, 'NS'),
            'txt_records': get_dns_records(domain, 'TXT'),
            'cname_records': get_dns_records(domain, 'CNAME')
        }
        return result
    except Exception as e:
        return {'error': f'Error performing DNS lookup: {str(e)}'}

def get_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [r.to_text() for r in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        return [f'No such domain: {domain}']
    except dns.resolver.NoNameservers:
        return [f'No nameservers found for: {domain}']
    except Exception as e:
        return [f'Error: {str(e)}']
