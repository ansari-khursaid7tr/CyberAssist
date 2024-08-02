import ssl
import socket
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import certifi


@csrf_exempt
def ssl_tls_checker(request):
    if request.method == 'POST':
        domain = request.POST.get('domain', '').strip()
        domain = domain.replace('https://', '').replace('http://', '')
        if domain.startswith('www.'):
            domain = domain[4:]

        result = check_ssl_certificate(domain)
        return JsonResponse(result)
    elif request.method == 'GET':
        return render(request, 'ssl_checker/templates/ssl_checker.html')
    return JsonResponse({'error': 'Invalid request method'})


def check_ssl_certificate(domain):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context(cafile=certifi.where())

        # Establish a connection to the domain
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                cert = secure_sock.getpeercert()

        issuer = dict(x[0] for x in cert['issuer'])
        issuer_str = issuer.get('organizationName', 'Unknown')
        valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
        valid_until = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        status = 'Valid' if datetime.utcnow() < valid_until else 'Expired'

        return {
            'domain': domain,
            'issuer': issuer_str,
            'valid_from': valid_from.strftime('%Y-%m-%d %H:%M:%S'),
            'valid_until': valid_until.strftime('%Y-%m-%d %H:%M:%S'),
            'status': status
        }

    except ssl.CertificateError as e:
        return {'error': f'Certificate Error: {str(e)}'}
    except socket.gaierror as e:
        return {'error': f'Address Error: {str(e)}'}
    except socket.timeout:
        return {'error': 'Connection timed out'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}