import requests
from urllib.parse import urlparse


def test_api_security(url, method='GET', headers=None, data=None):
    results = []

    # Test 1: HTTPS Check
    parsed_url = urlparse(url)
    if parsed_url.scheme != 'https':
        results.append(('HTTPS', 'Failed', 'API is not using HTTPS', None))
    else:
        results.append(('HTTPS', 'Passed', 'API is using HTTPS', None))

    try:
        # Make the request
        response = requests.request(method, url, headers=headers, data=data, timeout=10, verify=False)

        # Add status code to all subsequent results
        status_code = response.status_code

        # Test 2: Authentication Check
        if 'Authorization' not in headers:
            results.append(('Authentication', 'Warning', 'No authentication header provided', status_code))
        else:
            results.append(('Authentication', 'Passed', 'Authentication header present', status_code))

        # Test 3: CORS Check
        if 'Access-Control-Allow-Origin' in response.headers:
            if response.headers['Access-Control-Allow-Origin'] == '*':
                results.append(('CORS', 'Warning', 'CORS is set to allow all origins', status_code))
            else:
                results.append(('CORS', 'Passed', 'CORS is configured', status_code))
        else:
            results.append(('CORS', 'Info', 'No CORS headers found', status_code))

        # Test 4: Content-Type Check
        if 'Content-Type' in response.headers:
            results.append(
                ('Content-Type', 'Passed', f"Content-Type is set: {response.headers['Content-Type']}", status_code))
        else:
            results.append(('Content-Type', 'Warning', 'No Content-Type header found', status_code))

        # Test 5: X-XSS-Protection Check
        if 'X-XSS-Protection' in response.headers:
            results.append(('XSS Protection', 'Passed', 'X-XSS-Protection header is set', status_code))
        else:
            results.append(('XSS Protection', 'Warning', 'X-XSS-Protection header is not set', status_code))

        # Test 6: Response Time Check
        if response.elapsed.total_seconds() > 1:
            results.append(('Response Time', 'Warning',
                            f'Slow response time: {response.elapsed.total_seconds()} seconds', status_code))
        else:
            results.append((
                           'Response Time', 'Passed', f'Good response time: {response.elapsed.total_seconds()} seconds',
                           status_code))

    except requests.exceptions.RequestException as e:
        results.append(('Connection', 'Failed', f'Failed to connect to the API: {str(e)}', None))

    return results