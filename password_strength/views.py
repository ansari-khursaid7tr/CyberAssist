from django.shortcuts import render
import re


def checker(request):
    strength = ''
    password = ''
    alert_class = 'alert-secondary'  # Default class

    if request.method == 'POST':
        password = request.POST.get('password', '')
        strength = check_password_strength(password)

        # Set alert class based on password strength
        if strength == 'Weak':
            alert_class = 'alert-danger'
        elif strength == 'Moderate':
            alert_class = 'alert-warning'
        elif strength == 'Strong':
            alert_class = 'alert-success'

    return render(request, 'password_strength/templates/checker.html', {
        'strength': strength,
        'password': password,
        'alert_class': alert_class,
    })


def check_password_strength(password):
    if len(password) < 8:
        return 'Weak'
    elif len(password) < 12:
        return 'Moderate'
    elif re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$', password):
        return 'Strong'
    else:
        return 'Moderate'
