from django.shortcuts import render
from django.http import JsonResponse
from .tester import test_api_security


def api_security_tester(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        method = request.POST.get('method', 'GET')
        headers = request.POST.get('headers', '{}')
        data = request.POST.get('data', '{}')

        try:
            headers = eval(headers)
            data = eval(data)
        except:
            headers = {}
            data = {}

        results = test_api_security(url, method, headers, data)
        return JsonResponse({'results': results})

    return render(request, 'api_security_tester/templates/api_security_tester.html')