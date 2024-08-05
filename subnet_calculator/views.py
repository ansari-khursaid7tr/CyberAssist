from django.shortcuts import render
import ipaddress


def subnet_calculator(request):
    context = {}
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address', '')
        subnet_mask = request.POST.get('subnet_mask', '')

        if not ip_address or not subnet_mask:
            context['error_message'] = "Please enter both IP address and subnet mask."
        else:
            try:
                # Try to create an IP network object
                network = ipaddress.ip_network(f'{ip_address}/{subnet_mask}', strict=False)

                context = {
                    'ip_address': ip_address,
                    'subnet_mask': subnet_mask,
                    'network_address': network.network_address,
                    'broadcast_address': network.broadcast_address,
                    'num_addresses': network.num_addresses - 2,  # Subtract network and broadcast addresses
                    'hostmask': network.hostmask,
                    'prefixlen': network.prefixlen,
                }
            except ValueError as e:
                # This will catch invalid IP addresses or subnet masks
                context['error_message'] = f"Invalid input: {str(e)}"
            except Exception as e:
                # This will catch any other unexpected errors
                context['error_message'] = f"An unexpected error occurred: {str(e)}"

    return render(request, 'subnet_calculator/templates/subnet_calculator.html', context)