import socket

domains_to_test = ['google.com', 'www.google.com', 'example.com', '8.8.8.8']

for domain in domains_to_test:
    try:
        ip = socket.gethostbyname(domain)
        print(f"Successfully resolved {domain} to {ip}")
    except socket.gaierror as e:
        print(f"Failed to resolve {domain}: {e}")