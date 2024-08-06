from django.shortcuts import render
from django.http import JsonResponse
from .generator import generate_password

def password_generator(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        use_uppercase = request.POST.get('uppercase') == 'on'
        use_lowercase = request.POST.get('lowercase') == 'on'
        use_digits = request.POST.get('digits') == 'on'
        use_special_chars = request.POST.get('special') == 'on'

        password = generate_password(
            length, use_uppercase, use_lowercase, use_digits, use_special_chars
        )

        return JsonResponse({'password': password})

    return render(request, 'password_generator/templates/password_generator.html')